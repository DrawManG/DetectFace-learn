#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtCore import *
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
from cv2 import cv2

from Info_Base.informers import path_file_learn, process_this_frame_procent, url_stream, resize_image, message,Camera_intro
from Info_Base.informers import process_this_frame as TEMP_process,path_train3,n_neighbors,path_project
from Program.predict import predict

from Program.show_prediction_labels_on_image import show_prediction_labels_on_image
from Program.start_script_with_timer import start_script_with_timer
from Program.Train import train
from io import StringIO
import sys


class Thread(QThread):
    class OutputInterceptor(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self

        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio
            sys.stdout = self._stdout

    changePixmap = pyqtSignal(QImage,str)
    log_learn = pyqtSignal(str)
    def run_run(self):

        Thread.run()

    def disconnect_run(self):
        self.Turn = False

    def train_data(self):

        return train(path_train3, model_save_path=path_file_learn, n_neighbors=n_neighbors)





    def run(self):
        self.Turn = True

        timer = 0
        whole_numb = 0
        massive_name = []
        process_this_frame = TEMP_process
        cap = cv2.VideoCapture(0)
        while self.Turn == True:

            ret, frame = cap.read()
            if ret:
                img = cv2.resize(frame, resize_image[0], fx=resize_image[1], fy=resize_image[2])
                process_this_frame = process_this_frame + 1
                if process_this_frame % process_this_frame_procent == 0:
                    predictions = predict(img, model_path=path_file_learn)
                frame, whole_numb, massive_name, timer = show_prediction_labels_on_image(frame, predictions, whole_numb,
                                                                                         massive_name, timer,
                                                                                         )
                start_script_with_timer(timer, massive_name)
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgbImage.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
                p = convertToQtFormat.scaled(int(w*0.9), int(h*0.9), Qt.KeepAspectRatio)
                self.changePixmap.emit(p,str(massive_name).replace("]","").replace("[",""))






class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    @pyqtSlot(QImage,str)
    def setImage(self, image,txt):
        self.label.setPixmap(QPixmap.fromImage(image))
        self.txtbox_logger.setText(txt)

    @pyqtSlot(str)
    def learn_thread(self,txt):
        self.txtbox_logger(txt)




    def initUI(self):

        rgbImage = cv2.cvtColor(Camera_intro, cv2.COLOR_BGR2RGB)
        h, w, ch = rgbImage.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
        self.p = convertToQtFormat.scaled(int(w), int(h), Qt.KeepAspectRatio)


        self.main_grid = QGridLayout()
        self.layout_center_button = QHBoxLayout()
        self.main_left = QGridLayout()
        self.main_right = QGridLayout()

        self.main_grid.addItem(self.main_left,0,0)
        self.main_grid.addItem(self.main_right,0,1)

        self.button_OpenFolder = QPushButton('Open folder learn',self)
        self.button_OpenFolder.clicked.connect(self.btn_openfolder)
        self.button_Learn = QPushButton('Learn face',self)
        self.button_Learn.clicked.connect(self.btn_learn)
        self.button_Start = QPushButton('Start',self)
        self.button_Start.clicked.connect(self.btn_start)

        self.button_Stop = QPushButton('Stop',self)
        self.button_Stop.clicked.connect(self.btn_stop)

        self.txtbox_logger = QTextEdit()


        self.button_Stop.setDisabled(True)





        self.main_left.addWidget(self.button_Start)
        self.main_left.addItem(self.layout_center_button)
        self.main_left.addWidget(self.button_Stop)
        self.main_left.addWidget(self.txtbox_logger)

        self.th = Thread(self)

        self.layout_center_button.addWidget(self.button_Learn)
        self.layout_center_button.addWidget(self.button_OpenFolder)

        self.label = QLabel(self)
        self.label.move(280, 120)
        self.label.resize(640, 480)
        self.label.setPixmap(QPixmap.fromImage(self.p))
        self.main_right.addWidget(self.label)

        #----------------------------
        self.setLayout(self.main_grid)
        self.setGeometry(40, 100, 1000, 500)
        self.setWindowTitle('FACE-DETECTOR')
        self.show()




    def btn_start(self):

        self.th.changePixmap.connect(self.setImage)
        self.th.start()
        self.button_Stop.setDisabled(False)
        self.button_Learn.setDisabled(True)
        self.button_Start.setDisabled(True)

    def btn_stop(self):
        #self.th.terminate()
        self.th.disconnect_run()
        self.th.quit()
        self.th.wait()
        self.button_Stop.setDisabled(True)
        self.label.setPixmap(QPixmap.fromImage(self.p))
        self.button_Learn.setDisabled(False)
        self.button_Start.setDisabled(False)



    def btn_learn(self):
        self.btn_stop()

        a,b = self.th.train_data()
        msg = QMessageBox()
        msg.setText("Learn Complete. Сheck console for face detection errors")
        msg.exec_()
        self.txtbox_logger.setText(str(b).replace("[","").replace("]","").replace("', '","\n").replace("'",""))
        self.button_Stop.setDisabled(True)
        self.button_Start.setDisabled(False)

    def btn_openfolder(self):
        import os
        os.listdir(path_project +"/"+ path_train3)











if __name__ == "__main__":


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

