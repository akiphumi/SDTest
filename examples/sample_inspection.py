import os
from datetime import datetime
from shutil import move, copy2
import imageio
from module.novelty_detector import NoveltyDetector
from module.trimming_data import TrimmingData
import argparse
import cv2
import time
from pathlib import Path


def predict(image_paths_list, model):
    return model.predict_paths(image_paths_list)


def save_frame_camera_key(device_num, dir_path, basename, timestamp, ext='jpg', delay=10, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    if not cap.isOpened():
        return

    base_path = os.path.join(dir_path, basename)
    while True:
        cv2.startWindowThread()
        ret, frame = cap.read()
        # TODO:ここのエラー対処
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay)
        if key == ord('c'):
            cv2.waitKey(10)
            cv2.destroyAllWindows()
            cv2.waitKey(10)
            cv2.imwrite('{}_{}.{}'.format(base_path, timestamp, ext), frame)
            cv2.waitKey(10)
            break


def inspection(args):
    # TODO:パス関係の整理（いまぐちゃぐちゃすぎる）
    Path('captured_image').mkdir(exist_ok=True)
    Path('captured_image/tmp').mkdir(exist_ok=True)

    timestamp = str(datetime.now().isoformat()).replace(':', '-')
    if args.camera:
        save_frame_camera_key(args.camera_id, 'capimg', 'cap', timestamp)
        time.sleep(1)
        original_image_path = 'capimg/cap_' + timestamp + '.jpg'
    elif args.fastmode:
        original_image_path = 'testimages/kakipi/test/OK/camera_0_2019-06-19T17-46-52.730279.jpg'
    elif args.path:
        original_image_path = args.path
    else:
        original_image_path = input('image path: ')

    _, ext = os.path.splitext(original_image_path)
    file_name = f'cam{args.camera_id}_{timestamp}{ext}'
    copied_image_path = os.path.join(os.path.dirname(__file__), 'captured_image', 'tmp', file_name)
    copy2(original_image_path, copied_image_path)

    image_paths = [copied_image_path]
    image_path = copied_image_path
    save_path = os.path.dirname(image_path)

    im = imageio.imread(image_path)
    im_width, im_height = im.shape[1], im.shape[0]

    if args.nn == 'vgg':
        tr_width, tr_height = (200, 200)
    elif args.nn == 'MobileNet':
        tr_width, tr_height = (224, 224)
    else:
        tr_width, tr_height = int(args.trimming_size[0]), int(args.trimming_size[1])

    trimming = not (im_width <= tr_width and im_height <= tr_height)

    if args.center:
        trimming_data = TrimmingData((((im_width - tr_width) / 2), ((im_height - tr_height) / 2)), (tr_width, tr_height), trimming)
    else:
        trimming_data = TrimmingData(args.anchor_point, args.trimming_size, trimming)

    # img = imageio.imread(image_path)
    file_name = os.path.basename(image_path)
    position = trimming_data.position
    size = trimming_data.size
    rect = im[int(position[1]):int(position[1]) + size[1], int(position[0]):int(position[0]) + size[0]]
    imageio.imwrite(os.path.join(save_path, file_name), rect)

    model = NoveltyDetector(nth_layer=args.layer, nn_name=args.nn, detector_name=args.detector, pool=args.pool, pca_n_components=args.pca)
    model.load(args.joblib)

    score = predict(image_paths, model)[0]
    if score >= args.threshold:
        print('良品 スコア：', score)
    else:
        print('不良品です　スコア：', score)

    os.remove(os.path.join('captured_image/tmp', file_name))


def execute_cmdline():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--path',
                        default=None,
                        help='''path to image file like testimages/campbelle/test/OK/soup_28.jpg.''',
                        type=str)

    parser.add_argument('-ap', '--anchor_point',
                        default=(0, 0),
                        help='''explanation''',
                        type=tuple)

    parser.add_argument('-ts', '--trimming_size',
                        default=(224, 224),
                        help='''(width, height)''',
                        type=tuple)

    parser.add_argument('-t', '--threshold',
                        default=-0.5,
                        help='Threshold to split scores of predicted items. Default is -0.5',
                        type=float)

    parser.add_argument('-n', '--nn',
                        nargs='?',
                        default='vgg',
                        help='''Select neural network model among Xception, ResNet(Default),
                            InceptionV3, InceptionResNetV2, MobileNet, MobileNetV2, DenseNet, NASNet''',
                        type=str)

    parser.add_argument('-l', '--layer',
                        nargs='?',
                        default=18,
                        help='Select which layer to use as feature. Less channels work better.',
                        type=int)

    parser.add_argument('-jl', '--joblib',
                        default='learned_weight/sample.joblib',
                        help='select .joblib file',
                        type=str)

    parser.add_argument('-d', '--detector',
                        default='svm',
                        help='Select novelty detector among RobustCovariance, IsolationForest, LocalOutlierFactor, ABOD, kNN',
                        type=str)

    parser.add_argument('-pl', '--pool',
                        default=None,
                        type=str)
    parser.add_argument('-pca', '--pca',
                        type=int,
                        default=None)

    parser.add_argument('-c', '--center',
                        action='store_true')

    parser.add_argument('-cam', '--camera',
                        action='store_true')

    parser.add_argument('-f', '--fastmode',
                        action='store_true')

    parser.add_argument('-ci', '--camera_id',
                        default=0,
                        type=int)

    args = parser.parse_args()

    if args.fastmode:
        inspection(args)
    else:
        while True:
            inputtext = input('start or exit (s or e): ')

            if inputtext in ['exit', 'e']:
                break
            elif inputtext in ['start', 's']:
                inspection(args)
                continue
            else:
                print('try again')
                continue


if __name__ == '__main__':
    execute_cmdline()
