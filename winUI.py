# Form implementation generated from reading ui file 'fileUIv2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1195, 651)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Table = QtWidgets.QLabel(parent=self.centralwidget)
        self.Table.setGeometry(QtCore.QRect(140, 90, 381, 381))
        self.Table.setText("")
        self.Table.setPixmap(QtGui.QPixmap("image/table.png"))
        self.Table.setObjectName("Table")
        self.spa1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.spa1.setGeometry(QtCore.QRect(380, 260, 101, 111))
        self.spa1.setText("")
        self.spa1.setPixmap(QtGui.QPixmap("image/spa1.png"))
        self.spa1.setObjectName("spa1")
        self.spa2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.spa2.setGeometry(QtCore.QRect(270, 350, 131, 111))
        self.spa2.setText("")
        self.spa2.setPixmap(QtGui.QPixmap("image/spa1.png"))
        self.spa2.setObjectName("spa2")
        self.spa3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.spa3.setGeometry(QtCore.QRect(150, 270, 131, 111))
        self.spa3.setText("")
        self.spa3.setPixmap(QtGui.QPixmap("image/spa1.png"))
        self.spa3.setObjectName("spa3")
        self.spa5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.spa5.setGeometry(QtCore.QRect(340, 140, 101, 101))
        self.spa5.setText("")
        self.spa5.setPixmap(QtGui.QPixmap("image/spa1.png"))
        self.spa5.setObjectName("spa5")
        self.spa4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.spa4.setGeometry(QtCore.QRect(190, 140, 101, 101))
        self.spa4.setText("")
        self.spa4.setPixmap(QtGui.QPixmap("image/spa1.png"))
        self.spa4.setObjectName("spa4")
        self.fork2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.fork2.setGeometry(QtCore.QRect(320, 310, 101, 121))
        self.fork2.setText("")
        self.fork2.setPixmap(QtGui.QPixmap("image/fork2.png"))
        self.fork2.setObjectName("fork2")
        self.fork1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.fork1.setGeometry(QtCore.QRect(350, 180, 141, 141))
        self.fork1.setText("")
        self.fork1.setPixmap(QtGui.QPixmap("image/fork1.png"))
        self.fork1.setObjectName("fork1")
        self.fork3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.fork3.setGeometry(QtCore.QRect(170, 310, 141, 131))
        self.fork3.setText("")
        self.fork3.setPixmap(QtGui.QPixmap("image/fork3.png"))
        self.fork3.setObjectName("fork3")
        self.fork4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.fork4.setGeometry(QtCore.QRect(120, 190, 141, 131))
        self.fork4.setText("")
        self.fork4.setPixmap(QtGui.QPixmap("image/fork4.png"))
        self.fork4.setObjectName("fork4")
        self.fork0 = QtWidgets.QLabel(parent=self.centralwidget)
        self.fork0.setGeometry(QtCore.QRect(230, 90, 161, 161))
        self.fork0.setText("")
        self.fork0.setPixmap(QtGui.QPixmap("image/fork0.png"))
        self.fork0.setScaledContents(True)
        self.fork0.setWordWrap(False)
        self.fork0.setObjectName("fork0")
        self.face1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.face1.setGeometry(QtCore.QRect(400, 30, 131, 121))
        self.face1.setText("")
        self.face1.setPixmap(QtGui.QPixmap("image/philosopher.png"))
        self.face1.setScaledContents(True)
        self.face1.setObjectName("face1")
        self.face2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.face2.setGeometry(QtCore.QRect(480, 280, 131, 141))
        self.face2.setText("")
        self.face2.setPixmap(QtGui.QPixmap("image/philosopher.png"))
        self.face2.setScaledContents(True)
        self.face2.setObjectName("face2")
        self.face5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.face5.setGeometry(QtCore.QRect(90, 40, 121, 131))
        self.face5.setText("")
        self.face5.setPixmap(QtGui.QPixmap("image/philosopher.png"))
        self.face5.setScaledContents(True)
        self.face5.setObjectName("face5")
        self.face4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.face4.setGeometry(QtCore.QRect(20, 280, 131, 131))
        self.face4.setText("")
        self.face4.setPixmap(QtGui.QPixmap("image/philosopher.png"))
        self.face4.setScaledContents(True)
        self.face4.setObjectName("face4")
        self.face3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.face3.setGeometry(QtCore.QRect(250, 450, 131, 121))
        self.face3.setText("")
        self.face3.setPixmap(QtGui.QPixmap("image/philosopher.png"))
        self.face3.setScaledContents(True)
        self.face3.setObjectName("face3")
        self.Start_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Start_button.setGeometry(QtCore.QRect(660, 550, 141, 61))
        self.Start_button.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid red; /* Change border color to red */\n"
"    border-radius: 5px;\n"
"    color: red; /* Set text color to red */\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    font-weight: bold;\n"
"    font-size: 18px; /* Make the font bold */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: red; /* Change background color on hover */\n"
"    color: white;\n"
"}")
        self.Start_button.setObjectName("Start_button")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 0, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 240, 121, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 560, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 121, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 0, 121, 31))
        self.label_5.setObjectName("label_5")
        self.Phi1 = QtWidgets.QWidget(parent=self.centralwidget)
        self.Phi1.setGeometry(QtCore.QRect(830, 10, 261, 131))
        self.Phi1.setAutoFillBackground(False)
        self.Phi1.setStyleSheet("background-color: white; /* Set the background color to white */\n"
"border: 2px solid #000000; ")
        self.Phi1.setObjectName("Phi1")
        self.label_6 = QtWidgets.QLabel(parent=self.Phi1)
        self.label_6.setGeometry(QtCore.QRect(130, 20, 121, 31))
        self.label_6.setStyleSheet("border: none;")
        self.label_6.setObjectName("label_6")
        self.Button0 = QtWidgets.QPushButton(parent=self.Phi1)
        self.Button0.setGeometry(QtCore.QRect(130, 60, 111, 61))
        self.Button0.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db; /* Add a blue border */\n"
"    border-radius: 5px; /* Round the corners */\n"
"    color: #3498db; /* Set text color to blue */\n"
"    padding: 5px 10px; /* Add padding */\n"
"}\n"
"QPushButton {\n"
"    font-size: 18px;\n"
"    font-weight: bold; /* Change the font size to 12 pixels */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* Change background color on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}")
        self.Button0.setObjectName("Button0")
        self.phi1 = QtWidgets.QLabel(parent=self.Phi1)
        self.phi1.setGeometry(QtCore.QRect(10, 20, 91, 101))
        self.phi1.setText("")
        self.phi1.setPixmap(QtGui.QPixmap("image/phi_thinking0.jpg"))
        self.phi1.setScaledContents(True)
        self.phi1.setObjectName("phi1")
        self.Phi2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.Phi2.setGeometry(QtCore.QRect(830, 140, 261, 121))
        self.Phi2.setAutoFillBackground(False)
        self.Phi2.setStyleSheet("background-color: white; /* Set the background color to white */\n"
"border: 2px solid #000000; ")
        self.Phi2.setObjectName("Phi2")
        self.Button1 = QtWidgets.QPushButton(parent=self.Phi2)
        self.Button1.setGeometry(QtCore.QRect(130, 50, 111, 61))
        self.Button1.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db; /* Add a blue border */\n"
"    border-radius: 5px; /* Round the corners */\n"
"    color: #3498db; /* Set text color to blue */\n"
"    padding: 5px 10px; /* Add padding */\n"
"}\n"
"QPushButton {\n"
"    font-size: 20px;\n"
"    font-weight: bold; /* Change the font size to 12 pixels */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* Change background color on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}")
        self.Button1.setObjectName("Button1")
        self.phi2 = QtWidgets.QLabel(parent=self.Phi2)
        self.phi2.setGeometry(QtCore.QRect(10, 10, 91, 101))
        self.phi2.setText("")
        self.phi2.setPixmap(QtGui.QPixmap("image/phi_thinking0.jpg"))
        self.phi2.setScaledContents(True)
        self.phi2.setObjectName("phi2")
        self.label_7 = QtWidgets.QLabel(parent=self.Phi2)
        self.label_7.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.label_7.setStyleSheet("border: none; /* Removes the border */\n"
"")
        self.label_7.setObjectName("label_7")
        self.Phi3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.Phi3.setGeometry(QtCore.QRect(830, 260, 261, 121))
        self.Phi3.setAutoFillBackground(False)
        self.Phi3.setStyleSheet("background-color: white; /* Set the background color to white */\n"
"border: 2px solid #000000; ")
        self.Phi3.setObjectName("Phi3")
        self.phi3 = QtWidgets.QLabel(parent=self.Phi3)
        self.phi3.setGeometry(QtCore.QRect(10, 10, 91, 101))
        self.phi3.setText("")
        self.phi3.setPixmap(QtGui.QPixmap("image/phi_thinking0.jpg"))
        self.phi3.setScaledContents(True)
        self.phi3.setObjectName("phi3")
        self.label_8 = QtWidgets.QLabel(parent=self.Phi3)
        self.label_8.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.label_8.setStyleSheet("border: none; /* Removes the border */\n"
"")
        self.label_8.setObjectName("label_8")
        self.Button2 = QtWidgets.QPushButton(parent=self.Phi3)
        self.Button2.setGeometry(QtCore.QRect(130, 50, 111, 61))
        self.Button2.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db; /* Add a blue border */\n"
"    border-radius: 5px; /* Round the corners */\n"
"    color: #3498db; /* Set text color to blue */\n"
"    padding: 5px 10px; /* Add padding */\n"
"}\n"
"QPushButton {\n"
"    font-size: 20px;\n"
"    font-weight: bold; /* Change the font size to 12 pixels */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* Change background color on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}")
        self.Button2.setObjectName("Button2")
        self.Phi4 = QtWidgets.QWidget(parent=self.centralwidget)
        self.Phi4.setGeometry(QtCore.QRect(830, 380, 261, 121))
        self.Phi4.setAutoFillBackground(False)
        self.Phi4.setStyleSheet("background-color: white; /* Set the background color to white */\n"
"border: 2px solid #000000; ")
        self.Phi4.setObjectName("Phi4")
        self.phi4 = QtWidgets.QLabel(parent=self.Phi4)
        self.phi4.setGeometry(QtCore.QRect(10, 10, 91, 101))
        self.phi4.setText("")
        self.phi4.setPixmap(QtGui.QPixmap("image/phi_thinking0.jpg"))
        self.phi4.setScaledContents(True)
        self.phi4.setObjectName("phi4")
        self.label_9 = QtWidgets.QLabel(parent=self.Phi4)
        self.label_9.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.label_9.setStyleSheet("border: none; /* Removes the border */\n"
"")
        self.label_9.setObjectName("label_9")
        self.Button3 = QtWidgets.QPushButton(parent=self.Phi4)
        self.Button3.setGeometry(QtCore.QRect(130, 50, 111, 61))
        self.Button3.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db; /* Add a blue border */\n"
"    border-radius: 5px; /* Round the corners */\n"
"    color: #3498db; /* Set text color to blue */\n"
"    padding: 5px 10px; /* Add padding */\n"
"}\n"
"QPushButton {\n"
"    font-size: 20px;\n"
"    font-weight: bold; /* Change the font size to 12 pixels */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* Change background color on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}")
        self.Button3.setObjectName("Button3")
        self.Phi5 = QtWidgets.QWidget(parent=self.centralwidget)
        self.Phi5.setGeometry(QtCore.QRect(830, 500, 261, 121))
        self.Phi5.setAutoFillBackground(False)
        self.Phi5.setStyleSheet("background-color: white; /* Set the background color to white */\n"
"border: 2px solid #000000; ")
        self.Phi5.setObjectName("Phi5")
        self.phi5 = QtWidgets.QLabel(parent=self.Phi5)
        self.phi5.setGeometry(QtCore.QRect(10, 10, 91, 101))
        self.phi5.setText("")
        self.phi5.setPixmap(QtGui.QPixmap("image/phi_thinking0.jpg"))
        self.phi5.setScaledContents(True)
        self.phi5.setObjectName("phi5")
        self.label_10 = QtWidgets.QLabel(parent=self.Phi5)
        self.label_10.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.label_10.setStyleSheet("border: none; /* Removes the border */\n"
"")
        self.label_10.setObjectName("label_10")
        self.Button4 = QtWidgets.QPushButton(parent=self.Phi5)
        self.Button4.setGeometry(QtCore.QRect(130, 50, 111, 61))
        self.Button4.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid #3498db; /* Add a blue border */\n"
"    border-radius: 5px; /* Round the corners */\n"
"    color: #3498db; /* Set text color to blue */\n"
"    padding: 5px 10px; /* Add padding */\n"
"}\n"
"QPushButton {\n"
"    font-size: 20px;\n"
"    font-weight: bold; /* Change the font size to 12 pixels */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3498db; /* Change background color on hover */\n"
"    color: white; /* Change text color on hover */\n"
"}")
        self.Button4.setObjectName("Button4")
        self.Reset_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Reset_button.setGeometry(QtCore.QRect(660, 470, 141, 61))
        self.Reset_button.setStyleSheet("QPushButton {\n"
"    background-color: white;\n"
"    border: 2px solid black; /* Change border color to red */\n"
"    border-radius: 5px;\n"
"    color: black; /* Set text color to red */\n"
"    padding: 5px 10px;\n"
"    font-weight: bold;\n"
"    font-size: 18px; /* Make the font bold */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: black; /* Change background color on hover */\n"
"    color: white;\n"
"}")
        self.Reset_button.setObjectName("Reset_button")
        self.Phi5.raise_()
        self.Phi4.raise_()
        self.Phi3.raise_()
        self.Phi2.raise_()
        self.Phi1.raise_()
        self.Table.raise_()
        self.spa1.raise_()
        self.spa2.raise_()
        self.spa3.raise_()
        self.spa5.raise_()
        self.spa4.raise_()
        self.fork2.raise_()
        self.fork1.raise_()
        self.fork3.raise_()
        self.fork4.raise_()
        self.fork0.raise_()
        self.face1.raise_()
        self.face2.raise_()
        self.face5.raise_()
        self.face4.raise_()
        self.face3.raise_()
        self.Start_button.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.Reset_button.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Start_button.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher1</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher2</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher3</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher4</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher5</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher1</span></p></body></html>"))
        self.Button0.setText(_translate("MainWindow", "Button0"))
        self.Button1.setText(_translate("MainWindow", "Button1"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher2</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher3</span></p></body></html>"))
        self.Button2.setText(_translate("MainWindow", "Button2"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher4</span></p></body></html>"))
        self.Button3.setText(_translate("MainWindow", "Button3"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">Philosopher5</span></p></body></html>"))
        self.Button4.setText(_translate("MainWindow", "Button4"))
        self.Reset_button.setText(_translate("MainWindow", "Reset"))
