from PyQt5.QtCore import pyqtSignal, QObject, QThread
from model.project import Project
import socket
import threading


class ServingDobot(QObject):
    __default_instance = None
    dobot_req = pyqtSignal()

    @classmethod
    def default(cls):
        """returns default instance of LearningModel class."""
        if cls.__default_instance is None:
            cls.__default_instance = ServingDobot()
        return cls.__default_instance

    def __init__(self):
        QObject.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((Project.plc_ip_address(), 8501))
        self.is_waiting_req = True
        self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req, daemon=True)
        self.__waiting_dobot_req_thread.start()

    def waiting_dobot_req(self):
        self.is_waiting_req = True
        while self.is_waiting_req:
            comand = "RD DM05000.U"
            separator = "\r"
            msg = comand + separator
            self.socket.send(msg.encode("ascii"))

            message = self.socket.recv(1024)
            message = int(message)

            if message:
                self.dobot_req.emit()
                self.is_waiting_req = False

    def sending_inspection_result(self, result):
        if not self.is_waiting_req:
            if result:
                comand = "WR DM05001.U 00001"
                separator = "\r"  # 区切り符号CRの16進数表記
                msg = comand + separator
                self.socket.send(msg.encode("ascii"))
                self.socket.recv(1024)
            else:
                comand = "WR DM05001.U 00000"
                separator = "\r"  # 区切り符号CRの16進数表記
                msg = comand + separator
                self.socket.send(msg.encode("ascii"))
                self.socket.recv(1024)
            self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req, daemon=True)
            self.__waiting_dobot_req_thread.start()



