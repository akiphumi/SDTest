from PyQt5.QtCore import pyqtSignal, QObject, QThread
from module import top16
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
        top16.setup()
        top16.queryVersion()
        self.is_waiting_req = True
        self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req, daemon=True)
        self.__waiting_dobot_req_thread.start()

    def waiting_dobot_req(self):
        self.is_waiting_req = True
        while self.is_waiting_req:
            inputs = top16.getInputs()
            print("Inputs = %d" % inputs)

            if inputs:
                self.dobot_req.emit()
                self.is_waiting_req = False

    def sending_inspection_result(self, result):
        if not self.is_waiting_req:
            if result:
                top16.setOutputs(1, 0xFF)
            else:
                top16.setOutputs(0, 0xFF)
            self.__waiting_dobot_req_thread = threading.Thread(target=self.waiting_dobot_req, daemon=True)
            self.__waiting_dobot_req_thread.start()