# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_incubator.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from signal import signal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QStyle, QApplication, QWidget, QDialog

from status_label import StatusLabel
from status_label import main as mmm
from tracker import get_pretty_incubators, set_param_values
from status_label import get_incubators

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Incubator Status Viewer")
        Dialog.resize(300, 224)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 111, 20))
        self.label_2.setObjectName("label_2")
        self.txtbox_account_name = QtWidgets.QLineEdit(Dialog)
        self.txtbox_account_name.setGeometry(QtCore.QRect(134, 30, 113, 20))
        self.txtbox_account_name.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbox_account_name.setObjectName("txtbox_account_name")
        self.txtbox_realm = QtWidgets.QLineEdit(Dialog)
        self.txtbox_realm.setGeometry(QtCore.QRect(134, 70, 113, 20))
        self.txtbox_realm.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbox_realm.setObjectName("txtbox_realm")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 111, 20))
        self.label_3.setObjectName("label_3")
        self.txtbox_character_name = QtWidgets.QLineEdit(Dialog)
        self.txtbox_character_name.setGeometry(QtCore.QRect(134, 110, 113, 20))
        self.txtbox_character_name.setAlignment(QtCore.Qt.AlignCenter)
        self.txtbox_character_name.setObjectName("txtbox_character_name")
        # self.txtbox_request_rate = QtWidgets.QLineEdit(Dialog)
        # self.txtbox_request_rate.setGeometry(QtCore.QRect(134, 150, 113, 20))
        # self.txtbox_request_rate.setAlignment(QtCore.Qt.AlignCenter)
        # self.txtbox_request_rate.setObjectName("txtbox_request_rate")
        # self.label_4 = QtWidgets.QLabel(Dialog)
        # self.label_4.setGeometry(QtCore.QRect(20, 150, 111, 20))
        # self.label_4.setObjectName("label_4")
        self.btn_get_character_inventory = QtWidgets.QPushButton(Dialog)
        self.btn_get_character_inventory.setGeometry(QtCore.QRect(90, 190, 127, 23))
        self.btn_get_character_inventory.setObjectName("btn_get_character_inventory")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.label.setObjectName("label")
        self.btn_get_character_inventory.clicked.connect(self.btn_clicked)

        self.__press_pos = QPoint()


        self.incubator = StatusLabel()


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Realm"))
        self.label_3.setText(_translate("Dialog", "Character Name"))
        # self.txtbox_request_rate.setText(_translate("Dialog", "60"))
        # self.label_4.setText(_translate("Dialog", "Request Rate(in secs)"))
        self.btn_get_character_inventory.setText(_translate("Dialog", "Get Character Inventory"))
        self.label.setText(_translate("Dialog", "Account Name"))


    def btn_clicked(self):
        print("Button clicked")
        print(self.txtbox_account_name.text())
        # self.incubator.setText(get_pretty_incubators())
        # self.incubator.adjustSize()
        set_param_values(self.txtbox_account_name.text(), self.txtbox_realm.text(), self.txtbox_character_name.text())
        get_incubators(self.incubator)
        self.incubator.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

