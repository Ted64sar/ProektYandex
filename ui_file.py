# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_file.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 80, 421, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 421, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_9 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.verticalLayout.addWidget(self.radioButton_9)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 421, 371))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_2.addWidget(self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_2.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.verticalLayout_2.addWidget(self.radioButton_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 421, 371))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton_10 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_3.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_3.addWidget(self.radioButton_11)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_3.addWidget(self.radioButton_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 421, 371))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.radioButton_13 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_13.setObjectName("radioButton_13")
        self.verticalLayout_4.addWidget(self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_14.setObjectName("radioButton_14")
        self.verticalLayout_4.addWidget(self.radioButton_14)
        self.radioButton_12 = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        self.radioButton_12.setObjectName("radioButton_12")
        self.verticalLayout_4.addWidget(self.radioButton_12)
        self.tabWidget.addTab(self.tab_4, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 500, 131, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_2.setText(_translate("MainWindow", "R-2 D-2"))
        self.radioButton_3.setText(_translate("MainWindow", "BB-8"))
        self.radioButton_9.setText(_translate("MainWindow", "R-4"))
        self.radioButton_4.setText(_translate("MainWindow", "C-3 P O"))
        self.radioButton.setText(_translate("MainWindow", "Chopper"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Персонажи"))
        self.radioButton_6.setText(_translate("MainWindow", "Штурмовик"))
        self.radioButton_7.setText(_translate("MainWindow", "Штурмовик Смерти"))
        self.radioButton_8.setText(_translate("MainWindow", "Дроид торговой Федерации"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Противники"))
        self.radioButton_10.setText(_translate("MainWindow", "Ямы"))
        self.radioButton_11.setText(_translate("MainWindow", "Мины"))
        self.radioButton_5.setText(_translate("MainWindow", "Баст-дроиды"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Препятствия"))
        self.radioButton_13.setText(_translate("MainWindow", "Татуин"))
        self.radioButton_14.setText(_translate("MainWindow", "Эндор"))
        self.radioButton_12.setText(_translate("MainWindow", "Серый Фон"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Фон"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить настройки"))
