from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QImage, QPixmap
import cv2

from img import Ui_MainWindow
images_list = ["1.jpg", "2.jpg", "3.jpg","4.PNG"]
i = 0


class MainWindow_controller(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()   
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.pushButton.setText('run all')
        self.ui.pushButton_2.setText('prev')
        self.ui.pushButton_2.clicked.connect(self.prev)
        self.ui.pushButton_3.setText('next')
        self.ui.pushButton_3.clicked.connect(self.next)
        self.ui.pushButton_4.setText('資料庫')
        self.display_img()

    def prev(self):
        global images_list
        global i
        if i > 0:
            i -= 1
            self.display_img()
        else:
            i = len(images_list)-1
            self.display_img()

    def next(self):
        global images_list
        global i
        if i >= len(images_list)-1:
            i = 0
            self.display_img()
        else:
            i += 1
            self.display_img()

    def display_img(self):
        global images_list
        global i
        self.img = cv2.imread(images_list[i])
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped()
        self.ui.label.setPixmap(QPixmap.fromImage(self.qimg))