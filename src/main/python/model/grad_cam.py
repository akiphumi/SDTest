import glob
import os
import pathlib

import numpy as np
import cv2
from keras import backend as K
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from keras.models import load_model
import tensorflow as tf
import imageio
import skimage.transform
import cmapy


class GradCam:
    @staticmethod
    def loadmodel(path):
        return load_model(path)

    def __init__(self):
        self.input_shape = None
        self.model = None

        K.clear_session()

    def _load_model(self, input_shape=(229, 229, 3)):
        """
        This method should be called after loading images to set input shape.
        """
        self.input_shape = input_shape
        self.graph = None

        weights_path = pathlib.Path("./main/python/module/weights.h5")
        if weights_path.is_file():
            path = weights_path.resolve()
            self.model = self.loadmodel(str(path))
            self.graph = tf.get_default_graph()

        return self.model

    def predict(self, imgs):
        if self.model is None:
            self._load_model(imgs[0].shape)

        with self.graph.as_default():
            predictions = self.model.predict(imgs)

            class_idx = np.argmax(predictions[0])
            class_output = self.model.output[:, class_idx]

            conv_output = self.model.get_layer('block5_conv3').output
            grads = K.gradients(class_output, conv_output)[0]
            gradient_function = K.function([self.model.input], [conv_output, grads])

            output, grads_val = gradient_function([imgs])
        output, grads_val = output[0], grads_val[0]

        weights = np.mean(grads_val, axis=(0, 1))
        cam = np.dot(output, weights)

        cam = cv2.resize(cam, (self.input_shape[:2]), cv2.INTER_LINEAR)
        cam = np.maximum(cam, 0)
        cam = cam / cam.max()

        img = imgs[0]
        img *= 255
        
        jetcam = cv2.applyColorMap(np.uint8(255 * cam), cmapy.cmap('inferno'))
        jetcam = cv2.cvtColor(jetcam, cv2.COLOR_BGR2RGB)
        jetcam = (np.float32(jetcam) + img / 2)

        return jetcam


    def predict_paths(self, paths):
        imgs = self._read_imgs(paths)
        return self.predict(imgs)


    def _read_imgs(self, paths):
        paths = [ os.path.expanduser(path) for path in paths]
        if self.input_shape is None:
            self.input_shape = imageio.imread(paths[0], as_gray=False, pilmode='RGB').shape
        imgs = []
        for path in paths:
            img = imageio.imread(path, as_gray=False, pilmode='RGB').astype(np.float)
            img = skimage.transform.resize(img, self.input_shape[:2])
            img /= 255
            imgs.append(img)
        imgs = np.array(imgs)
        imgs = imgs.reshape(-1, *self.input_shape)
        return imgs

