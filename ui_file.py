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
        MainWindow.resize(458, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 80, 391, 371))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 301, 351))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_2)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.radioButton_3 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_3)
        self.radioButton_9 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_9.setObjectName("radioButton_9")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_9)
        self.radioButton_4 = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_4)
        self.radioButton = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 301, 351))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.radioButton_6 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.radioButton_7 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_7.setObjectName("radioButton_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.formLayoutWidget_2)
        self.radioButton_8.setObjectName("radioButton_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_8)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 431, 381))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.radioButton_10 = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.radioButton_10.setObjectName("radioButton_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_10)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_9)
        self.radioButton_11 = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.radioButton_11.setObjectName("radioButton_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_11)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_11)
        self.radioButton_5 = QtWidgets.QRadioButton(self.formLayoutWidget_3)
        self.radioButton_5.setObjectName("radioButton_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_5)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_10)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.tab_4)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 301, 351))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.radioButton_12 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_12.setObjectName("radioButton_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_12)
        self.radioButton_13 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_13.setObjectName("radioButton_13")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_13)
        self.radioButton_14 = QtWidgets.QRadioButton(self.formLayoutWidget_4)
        self.radioButton_14.setObjectName("radioButton_14")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_14)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_13)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.tab_5)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 301, 351))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 0, 0)
        self.formLayout_5.setObjectName("formLayout_5")
        self.radioButton_15 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_15.setObjectName("radioButton_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton_15)
        self.radioButton_16 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_16.setObjectName("radioButton_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_16)
        self.radioButton_17 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_17.setObjectName("radioButton_17")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_17)
        self.radioButton_18 = QtWidgets.QRadioButton(self.formLayoutWidget_5)
        self.radioButton_18.setObjectName("radioButton_18")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_18)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_16)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_17.setObjectName("label_17")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_18.setObjectName("label_18")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_18)
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 480, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 21))
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
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/R2-D2.png\"/></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/R2-D2.png\"/></p></body></html>"))
        self.radioButton_3.setText(_translate("MainWindow", "BB-8"))
        self.radioButton_9.setText(_translate("MainWindow", "R-4"))
        self.radioButton_4.setText(_translate("MainWindow", "C-3 P O"))
        self.radioButton.setText(_translate("MainWindow", "Chopper"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/BB8.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/R-4.png\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/C3PO.png\"/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/CHOPPER.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Персонажи"))
        self.radioButton_6.setText(_translate("MainWindow", "Штурмовик"))
        self.radioButton_7.setText(_translate("MainWindow", "Штурмовик Смерти"))
        self.radioButton_8.setText(_translate("MainWindow", "Дроид торговой Федерации"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/stormtrooper.png\"/></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/death-stormtrooper.png\"/></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/trade-federation-droid.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Противники"))
        self.radioButton_10.setText(_translate("MainWindow", "Ямы"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/hole.png\"/></p></body></html>"))
        self.radioButton_11.setText(_translate("MainWindow", "Мины"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/mine.png\"/></p></body></html>"))
        self.radioButton_5.setText(_translate("MainWindow", "Баст-дроиды"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/bust-droid.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Препятствия"))
        self.radioButton_12.setText(_translate("MainWindow", "Капитан Фазма"))
        self.radioButton_13.setText(_translate("MainWindow", "Генерал Гривус"))
        self.radioButton_14.setText(_translate("MainWindow", "Гранд-инквизитор"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/Fazma.png\"/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/general_grivus.png\"/></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/newPrefix/images/grand_inkvizitor.png\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Стражи"))
        self.radioButton_15.setText(_translate("MainWindow", "Элементарно"))
        self.radioButton_16.setText(_translate("MainWindow", "Легко"))
        self.radioButton_17.setText(_translate("MainWindow", "Нормально"))
        self.radioButton_18.setText(_translate("MainWindow", "Сложно"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Уровень"))
        self.pushButton.setText(_translate("MainWindow", "Сохранить настройки"))

import qwe

