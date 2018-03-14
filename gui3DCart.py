# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(632, 464)
        MainWindow.setMaximumSize(QtCore.QSize(632, 464))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.StartProgram = QtWidgets.QPushButton(self.centralwidget)
        self.StartProgram.setGeometry(QtCore.QRect(240, 400, 141, 23))
        self.StartProgram.setObjectName("StartProgram")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 121, 20))
        self.label.setObjectName("label")
        self.SaveTextToFile = QtWidgets.QPushButton(self.centralwidget)
        self.SaveTextToFile.setGeometry(QtCore.QRect(150, 310, 321, 23))
        self.SaveTextToFile.setObjectName("SaveTextToFile")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(236, 380, 151, 20))
        self.label_2.setObjectName("label_2")
        self.EmailTextBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.EmailTextBox.setGeometry(QtCore.QRect(70, 30, 491, 271))
        self.EmailTextBox.setObjectName("EmailTextBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3D Cart Brander and Emailer"))
        self.StartProgram.setText(_translate("MainWindow", "Start 3D Cart Brander"))
        self.label.setText(_translate("MainWindow", "Paste 3D Cart Email Here"))
        self.SaveTextToFile.setText(_translate("MainWindow", "Save Text to file: \"3dcart_info_Goes_Here.txt\""))
        self.label_2.setText(_translate("MainWindow", "Save before clicking this button"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit "))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

