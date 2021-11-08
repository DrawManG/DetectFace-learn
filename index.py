#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication, QGridLayout, QHBoxLayout, QTextEdit, QLabel)
from PyQt5.QtGui import QFont, QPixmap

from Info_Base.informers import CamFrapsDemo

#----
from Old_project.facerec_ipcamera_knn import *
from Info_Base.informers import path_file_learn, process_this_frame,process_this_frame_procent,url_stream,resize_image,message,anti_double_message,timer,whole_numb,massive_name,path_train,n_neighbors

from Program.Train import train
from Program.show_prediction_labels_on_image import show_prediction_labels_on_image
from Program.start_script_with_timer import start_script_with_timer
#-----


def starter():
    pass

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):



        self.main_grid = QGridLayout()
        self.layout_center_button = QHBoxLayout()
        self.main_left = QGridLayout()
        self.main_right = QGridLayout()

        self.main_grid.addItem(self.main_left,0,0)
        self.main_grid.addItem(self.main_right,0,1)

        self.button_OpenFolder = QPushButton('Открыть обучение')
        self.button_Learn = QPushButton('Обучить')
        self.button_Start = QPushButton('Запустить')
        self.button_Stop = QPushButton('Остановить')

        self.txtbox_logger = QTextEdit()

        self.label_for_image = QLabel()
        self.cam_frame = QPixmap(CamFrapsDemo)

        self.label_for_image.setPixmap(self.cam_frame)
        self.label_for_image.resize(self.cam_frame.width(),self.cam_frame.height())


        self.main_left.addWidget(self.button_Start)
        self.main_left.addItem(self.layout_center_button)
        self.main_left.addWidget(self.button_Stop)
        self.main_left.addWidget(self.txtbox_logger)

        self.main_right.addWidget(self.label_for_image)

        self.layout_center_button.addWidget(self.button_Learn)
        self.layout_center_button.addWidget(self.button_OpenFolder)



        #----------------------------
        self.setLayout(self.main_grid)
        self.setGeometry(40, 100, 1000, 500)
        self.setWindowTitle('FACE-DETECTOR')
        self.show()



if __name__ == "__main__":


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())







