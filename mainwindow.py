##!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import random_password
import string


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(410, 322)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.specialCharCheckbox = QtWidgets.QCheckBox(self.centralWidget)
        self.specialCharCheckbox.setObjectName("specialCharCheckbox")
        self.gridLayout_2.addWidget(self.specialCharCheckbox, 4, 0, 1, 1)
        self.passwordEditLine = QtWidgets.QLineEdit(self.centralWidget)
        self.passwordEditLine.setObjectName("passwordEditLine")
        self.gridLayout_2.addWidget(self.passwordEditLine, 0, 0, 1, 1)
        self.alphabetCheckbox = QtWidgets.QCheckBox(self.centralWidget)
        self.alphabetCheckbox.setObjectName("alphabetCheckbox")
        self.gridLayout_2.addWidget(self.alphabetCheckbox, 3, 0, 1, 1)
        self.generateButton = QtWidgets.QPushButton(self.centralWidget)
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(self.rnd_pass_generator)
        self.gridLayout_2.addWidget(self.generateButton, 9, 2, 1, 1)
        self.numbersCheckbox = QtWidgets.QCheckBox(self.centralWidget)
        self.numbersCheckbox.setObjectName("numbersCheckbox")
        self.gridLayout_2.addWidget(self.numbersCheckbox, 2, 0, 1, 1)
        self.lengthSlider = QtWidgets.QSlider(self.centralWidget)
        self.lengthSlider.setMinimum(6)
        self.lengthSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lengthSlider.setObjectName("lengthSlider")
        self.lengthSlider.valueChanged.connect(self.change_label_value)
        self.gridLayout_2.addWidget(self.lengthSlider, 1, 0, 1, 1)
        self.lengthLable = QtWidgets.QLabel(self.centralWidget)
        self.lengthLable.setObjectName("lengthLable")
        self.lengthLable.setText(str(self.lengthSlider.value()))
        self.gridLayout_2.addWidget(self.lengthLable, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 410, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCreate = QtWidgets.QAction(MainWindow)
        self.actionCreate.setObjectName("actionCreate")
        self.actionCreate.triggered.connect(self.rnd_pass_generator)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.menuFile.addAction(self.actionCreate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.passwordEditLine, self.lengthSlider)
        MainWindow.setTabOrder(self.lengthSlider, self.numbersCheckbox)
        MainWindow.setTabOrder(self.numbersCheckbox, self.alphabetCheckbox)
        MainWindow.setTabOrder(self.alphabetCheckbox, self.specialCharCheckbox)
        MainWindow.setTabOrder(self.specialCharCheckbox, self.generateButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Random Password Generator"))
        self.specialCharCheckbox.setText(_translate("MainWindow", "!@#$%^&*()_+=-[]/"))
        self.alphabetCheckbox.setText(_translate("MainWindow", "a-z"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.numbersCheckbox.setText(_translate("MainWindow", "0-9"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionCreate.setText(_translate("MainWindow", "Create"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def rnd_pass_generator(self):
        self.length = self.lengthSlider.value()
        self.chars = ''
        if self.alphabetCheckbox.isChecked():
            self.chars += string.ascii_letters
        if self.numbersCheckbox.isChecked():
            self.chars += string.digits
        if self.specialCharCheckbox.isChecked():
            self.chars += '!@#$%^&*()_+=-[]/'
        self.rnd_pass_class = random_password.random_password()
        self.rnd_pass = self.rnd_pass_class.create_random_password(chars=self.chars ,seq=self.length)
        self.passwordEditLine.setText(self.rnd_pass)
        QtWidgets.QApplication.clipboard().setText(self.rnd_pass, mode=QtWidgets.QApplication.clipboard().Clipboard)
        self.statusBar.showMessage('Copied To Clipboard')

    def change_label_value(self):
        self.lengthLable.setText(str(self.lengthSlider.value()))
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = Ui_MainWindow()
    mw.show()
    sys.exit(app.exec_())
