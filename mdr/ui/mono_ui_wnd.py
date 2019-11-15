# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mono_ui_wnd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 683)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chartLayout = QtWidgets.QGridLayout()
        self.chartLayout.setSpacing(6)
        self.chartLayout.setObjectName("chartLayout")
        self.horizontalLayout.addLayout(self.chartLayout)
        self.verticalWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalWidget.setObjectName("verticalWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.verticalWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.step = QtWidgets.QComboBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.step.setFont(font)
        self.step.setObjectName("step")
        self.step.addItem("")
        self.step.addItem("")
        self.step.addItem("")
        self.step.addItem("")
        self.step.addItem("")
        self.step.addItem("")
        self.step.addItem("")
        self.gridLayout.addWidget(self.step, 1, 2, 1, 2)
        self.statusLabel = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 8, 1, 1, 2)
        self.btnStop = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btnStop.setFont(font)
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 10, 1, 1, 3)
        self.label = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.btnStart = QtWidgets.QPushButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.gridLayout.addWidget(self.btnStart, 9, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.repeat = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.repeat.setFont(font)
        self.repeat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.repeat.setObjectName("repeat")
        self.gridLayout.addWidget(self.repeat, 3, 2, 1, 1)
        self.voltagePEM1 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.voltagePEM1.setFont(font)
        self.voltagePEM1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltagePEM1.setObjectName("voltagePEM1")
        self.gridLayout.addWidget(self.voltagePEM1, 4, 2, 1, 1)
        self.voltagePEM2 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.voltagePEM2.setFont(font)
        self.voltagePEM2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.voltagePEM2.setObjectName("voltagePEM2")
        self.gridLayout.addWidget(self.voltagePEM2, 5, 2, 1, 1)
        self.rangeHigh = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rangeHigh.setFont(font)
        self.rangeHigh.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rangeHigh.setObjectName("rangeHigh")
        self.gridLayout.addWidget(self.rangeHigh, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.statusBtn = QtWidgets.QPushButton(self.verticalWidget)
        self.statusBtn.setObjectName("statusBtn")
        self.gridLayout.addWidget(self.statusBtn, 8, 3, 1, 1)
        self.speed = QtWidgets.QComboBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.speed.setFont(font)
        self.speed.setObjectName("speed")
        self.speed.addItem("")
        self.speed.addItem("")
        self.speed.addItem("")
        self.speed.addItem("")
        self.speed.addItem("")
        self.speed.addItem("")
        self.speed.addItem("")
        self.gridLayout.addWidget(self.speed, 2, 2, 1, 2)
        self.rangeLow = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.rangeLow.setFont(font)
        self.rangeLow.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rangeLow.setObjectName("rangeLow")
        self.gridLayout.addWidget(self.rangeLow, 0, 2, 1, 1)
        self.statusLabel_2 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.statusLabel_2.setFont(font)
        self.statusLabel_2.setObjectName("statusLabel_2")
        self.gridLayout.addWidget(self.statusLabel_2, 7, 1, 1, 3)
        self.horizontalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1178, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menuDebug = QtWidgets.QMenu(self.menuBar)
        self.menuDebug.setObjectName("menuDebug")
        self.menuConnect = QtWidgets.QMenu(self.menuBar)
        self.menuConnect.setObjectName("menuConnect")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionPLACEHOLDER = QtWidgets.QAction(MainWindow)
        self.actionPLACEHOLDER.setObjectName("actionPLACEHOLDER")
        self.menuExit = QtWidgets.QAction(MainWindow)
        self.menuExit.setObjectName("menuExit")
        self.actionShow = QtWidgets.QAction(MainWindow)
        self.actionShow.setObjectName("actionShow")
        self.actionMDRConnect = QtWidgets.QAction(MainWindow)
        self.actionMDRConnect.setObjectName("actionMDRConnect")
        self.actionCalibrate = QtWidgets.QAction(MainWindow)
        self.actionCalibrate.setObjectName("actionCalibrate")
        self.menu.addAction(self.actionPLACEHOLDER)
        self.menu.addSeparator()
        self.menu.addAction(self.menuExit)
        self.menuDebug.addAction(self.actionShow)
        self.menuConnect.addAction(self.actionMDRConnect)
        self.menuConnect.addAction(self.actionCalibrate)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuConnect.menuAction())
        self.menuBar.addAction(self.menuDebug.menuAction())

        self.retranslateUi(MainWindow)
        self.step.setCurrentIndex(5)
        self.speed.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Число повторов"))
        self.step.setCurrentText(_translate("MainWindow", "1"))
        self.step.setItemText(0, _translate("MainWindow", "0.002"))
        self.step.setItemText(1, _translate("MainWindow", "0.01"))
        self.step.setItemText(2, _translate("MainWindow", "0.05"))
        self.step.setItemText(3, _translate("MainWindow", "0.1"))
        self.step.setItemText(4, _translate("MainWindow", "0.5"))
        self.step.setItemText(5, _translate("MainWindow", "1"))
        self.step.setItemText(6, _translate("MainWindow", "5"))
        self.statusLabel.setText(_translate("MainWindow", "."))
        self.btnStop.setText(_translate("MainWindow", "СТОП"))
        self.label.setText(_translate("MainWindow", "Шаг дискретизации (нм)"))
        self.btnStart.setText(_translate("MainWindow", "ПУСК"))
        self.label_2.setText(_translate("MainWindow", "Диапазон (200-25000 нм)"))
        self.repeat.setText(_translate("MainWindow", "1"))
        self.voltagePEM1.setText(_translate("MainWindow", "1100"))
        self.voltagePEM2.setText(_translate("MainWindow", "400"))
        self.rangeHigh.setText(_translate("MainWindow", "600"))
        self.label_5.setText(_translate("MainWindow", "Напряжение ФЭУ-100 (400-1900)"))
        self.label_6.setText(_translate("MainWindow", "Напряжение ФЭУ-62 (400-1600)"))
        self.label_3.setText(_translate("MainWindow", "Скорость (нм/мин)"))
        self.statusBtn.setText(_translate("MainWindow", "OK"))
        self.speed.setCurrentText(_translate("MainWindow", "70"))
        self.speed.setItemText(0, _translate("MainWindow", "200"))
        self.speed.setItemText(1, _translate("MainWindow", "70"))
        self.speed.setItemText(2, _translate("MainWindow", "30"))
        self.speed.setItemText(3, _translate("MainWindow", "10"))
        self.speed.setItemText(4, _translate("MainWindow", "3.3"))
        self.speed.setItemText(5, _translate("MainWindow", "1"))
        self.speed.setItemText(6, _translate("MainWindow", "0.6"))
        self.rangeLow.setText(_translate("MainWindow", "500"))
        self.statusLabel_2.setText(_translate("MainWindow", "TextLabel"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menuDebug.setTitle(_translate("MainWindow", "Debug"))
        self.menuConnect.setTitle(_translate("MainWindow", "Connect"))
        self.actionPLACEHOLDER.setText(_translate("MainWindow", "PLACEHOLDER"))
        self.menuExit.setText(_translate("MainWindow", "Выход"))
        self.actionShow.setText(_translate("MainWindow", "Show"))
        self.actionMDRConnect.setText(_translate("MainWindow", "MDR"))
        self.actionCalibrate.setText(_translate("MainWindow", "Calibrate"))


