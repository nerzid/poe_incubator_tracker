import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QStyle

import threading
import time

from tracker import get_pretty_incubators


class StatusLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__press_pos = QPoint()
        self.initUI()

    def initUI(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint  | Qt.WindowCloseButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setText("Drag me...")
        self.setFont(QFont("Times", 10, QFont.Bold))
        self.setStyleSheet('color: yellow')
        self.adjustSize()
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                QApplication.instance().desktop().availableGeometry()
            )
        )
        print("popup")
        self.keep_getting_incubators = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = event.pos()
        if event.button() == Qt.MiddleButton:
            sys.exit()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.__press_pos = QPoint()

    def mouseMoveEvent(self, event):
        if not self.__press_pos.isNull():
            self.move(self.pos() + (event.pos() - self.__press_pos))

def get_incubators(status_label_obj):
    incubator_updater = threading.Event()
    get_incubators_rec(incubator_updater, status_label_obj)

def get_incubators_rec(incubator_updater, status_label_obj):
    if not incubator_updater.is_set():
        threading.Timer(15, get_incubators_rec, [incubator_updater, status_label_obj]).start()
    incubator_str = get_pretty_incubators()
    print(incubator_str)
    status_label_obj.setText(incubator_str)
    status_label_obj.adjustSize()


def main():
    app = QApplication(sys.argv)
    w = StatusLabel()
    get_incubators()
    w.show()
    return app.exec_()


if __name__ == '__main__':
    main()
