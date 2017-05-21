# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from project.WithGmailAsInput import Gmail
from project.plottingOfData import dataPlot
import threading
from threading import Thread


class Ui_Dialog(object):

    def __init__(self):
        self.usermail = ""
        self.password = ""


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1041, 610)

        # palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtCore.Qt.lightGray)
        # Dialog.setPalette(palette)
#         Dialog.setStyleSheet(#"QDialog{\n"
# "    background-color:qlineargradient(spread:pad, x1:0.45, y1:0.3695, x2:0.426, y2:0, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
# #"}\n"
# )
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(340, 140, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.u_name_label.setFont(font)
        self.u_name_label.setObjectName("u_name_label")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(340, 190, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.email_line = QtWidgets.QLineEdit(Dialog)
        self.email_line.setGeometry(QtCore.QRect(490, 130, 201, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.email_line.setFont(font)
#         self.email_line.setStyleSheet("QLineEdit{\n"
# "    background-color:rgb(255, 255, 255);\n"
# "}")
        self.email_line.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.email_line.setObjectName("email_line")
        self.pass_line = QtWidgets.QLineEdit(Dialog)
        self.pass_line.setGeometry(QtCore.QRect(490, 180, 201, 32))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pass_line.setFont(font)
        self.pass_line.setInputMethodHints(QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText)
        self.pass_line.setEchoMode(QtWidgets.QLineEdit.Password)
        # self.pass_line.setStyleSheet("QLineEdit[type=password]{\n"
        #                              "    background-color:rgb(255, 255, 255);\n"
        #                              "}")
        # self.pass_line.setObjectName("pass_line")
        self.login_Button = QtWidgets.QPushButton(Dialog)
        self.login_Button.setGeometry(QtCore.QRect(490, 260, 94, 30))
#         self.login_Button.setStyleSheet("QPushButton{\n"
# "    background-color:qlineargradient(spread:pad, x1:0.45, y1:0.3695, x2:0.426, y2:0, stop:0 rgba(255, 170, 0, 228), stop:1 rgba(255, 255, 255, 255));\n"
# "border:none;\n"
# "}")
        self.login_Button.setObjectName("login_Button")
        self.login_Button.clicked.connect(self.loginCheck)

        self.exit_Button = QtWidgets.QPushButton(Dialog)
        self.exit_Button.setGeometry(QtCore.QRect(600, 260, 94, 30))
#         self.exit_Button.setStyleSheet("QPushButton{\n"
# "    background-color:qlineargradient(spread:pad, x1:0.45, y1:0.3695, x2:0.426, y2:0, stop:0 rgba(255, 170, 0, 228), stop:1 rgba(255, 255, 255, 255));\n"
# "border:none;\n"
# "}")
        self.exit_Button.setObjectName("exit_Button")
        self.exit_Button.clicked.connect(self.exitCheck)

        self.header_label = QtWidgets.QLabel(Dialog)
        self.header_label.setGeometry(QtCore.QRect(380, 30, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.header_label.setFont(font)
        self.header_label.setObjectName("header_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.u_name_label.setText(_translate("Dialog", "Email Address"))
        self.pass_label.setText(_translate("Dialog", "Password"))
        self.login_Button.setText(_translate("Dialog", "Analyze"))
        self.exit_Button.setText(_translate("Dialog", "Exit"))
        self.header_label.setText(_translate("Dialog", "Sentiment Analyzer"))

    def loginCheck(self):
        self.usermail = self.email_line.text()
        self.password = self.pass_line.text()
        #os.system("python test.py")
        gmail = Gmail(userMail=self.usermail, userPass=self.password)
        plott = dataPlot(textName="gmail_out.txt")
        Thread(target=plott.plot).start()
        Thread(target=gmail.compute).start()
        #pos, neg = gmail.get_Pos_Neg()
        #print(pos,neg)
        #print(self.usermail, self.password)
        Form.hide()

    def getUsermail(self):
        return self.usermail


    def getPassword(self):
        return self.password


    def exitCheck(self, event):
        msgBox = QMessageBox()
        msgBox.setText("Do you want to exit?");
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No);
        msgBox.setWindowTitle("Exit")
        result = msgBox.exec_()
        if result == QMessageBox.Yes:
            sys.exit()
        else:
            pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.setWindowTitle("Sentiment Analyzer")
    Form.show()
    app.exec()