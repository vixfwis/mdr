# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'debug_ui_wnd.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DebugWindow(object):
    def setupUi(self, DebugWindow):
        DebugWindow.setObjectName("DebugWindow")
        DebugWindow.resize(668, 554)
        self.centralWidget = QtWidgets.QWidget(DebugWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSetWL = QtWidgets.QPushButton(self.centralWidget)
        self.btnSetWL.setMinimumSize(QtCore.QSize(50, 0))
        self.btnSetWL.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSetWL.setObjectName("btnSetWL")
        self.gridLayout.addWidget(self.btnSetWL, 0, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnManualBeginMode = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualBeginMode.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualBeginMode.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualBeginMode.setObjectName("btnManualBeginMode")
        self.gridLayout.addWidget(self.btnManualBeginMode, 5, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralWidget)
        self.label_9.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.btnKinetic = QtWidgets.QPushButton(self.centralWidget)
        self.btnKinetic.setMinimumSize(QtCore.QSize(50, 0))
        self.btnKinetic.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnKinetic.setObjectName("btnKinetic")
        self.gridLayout.addWidget(self.btnKinetic, 14, 6, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 13, 0, 1, 1)
        self.btnSetFilter = QtWidgets.QPushButton(self.centralWidget)
        self.btnSetFilter.setMinimumSize(QtCore.QSize(50, 0))
        self.btnSetFilter.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSetFilter.setObjectName("btnSetFilter")
        self.gridLayout.addWidget(self.btnSetFilter, 4, 6, 1, 1)
        self.lineKinWTime = QtWidgets.QLineEdit(self.centralWidget)
        self.lineKinWTime.setMinimumSize(QtCore.QSize(30, 0))
        self.lineKinWTime.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineKinWTime.setObjectName("lineKinWTime")
        self.gridLayout.addWidget(self.lineKinWTime, 14, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnManualStop = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualStop.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualStop.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualStop.setObjectName("btnManualStop")
        self.gridLayout.addWidget(self.btnManualStop, 9, 6, 1, 1)
        self.btnSetWLWO = QtWidgets.QPushButton(self.centralWidget)
        self.btnSetWLWO.setMinimumSize(QtCore.QSize(50, 0))
        self.btnSetWLWO.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSetWLWO.setObjectName("btnSetWLWO")
        self.gridLayout.addWidget(self.btnSetWLWO, 1, 6, 1, 1)
        self.btnManualFaster = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualFaster.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualFaster.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualFaster.setObjectName("btnManualFaster")
        self.gridLayout.addWidget(self.btnManualFaster, 11, 6, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 14, 0, 1, 1)
        self.btnManualSlower = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualSlower.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualSlower.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualSlower.setObjectName("btnManualSlower")
        self.gridLayout.addWidget(self.btnManualSlower, 12, 6, 1, 1)
        self.btnManualReverse = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualReverse.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualReverse.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualReverse.setObjectName("btnManualReverse")
        self.gridLayout.addWidget(self.btnManualReverse, 8, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralWidget)
        self.label_10.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.centralWidget)
        self.btnStop.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 16, 6, 1, 1)
        self.btnMeasure = QtWidgets.QPushButton(self.centralWidget)
        self.btnMeasure.setMinimumSize(QtCore.QSize(50, 0))
        self.btnMeasure.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnMeasure.setObjectName("btnMeasure")
        self.gridLayout.addWidget(self.btnMeasure, 2, 6, 1, 1)
        self.btnCalib = QtWidgets.QPushButton(self.centralWidget)
        self.btnCalib.setMinimumSize(QtCore.QSize(50, 0))
        self.btnCalib.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnCalib.setObjectName("btnCalib")
        self.gridLayout.addWidget(self.btnCalib, 3, 6, 1, 1)
        self.btnManualGetWaveLength = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualGetWaveLength.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualGetWaveLength.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualGetWaveLength.setObjectName("btnManualGetWaveLength")
        self.gridLayout.addWidget(self.btnManualGetWaveLength, 10, 6, 1, 1)
        self.btnManualForward = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualForward.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualForward.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualForward.setObjectName("btnManualForward")
        self.gridLayout.addWidget(self.btnManualForward, 7, 6, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 15, 0, 1, 1)
        self.lineKinRTime = QtWidgets.QLineEdit(self.centralWidget)
        self.lineKinRTime.setMinimumSize(QtCore.QSize(30, 0))
        self.lineKinRTime.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineKinRTime.setObjectName("lineKinRTime")
        self.gridLayout.addWidget(self.lineKinRTime, 14, 2, 1, 1)
        self.labelResult = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")
        self.gridLayout.addWidget(self.labelResult, 16, 0, 1, 5)
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 11, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineKinWL = QtWidgets.QLineEdit(self.centralWidget)
        self.lineKinWL.setMinimumSize(QtCore.QSize(30, 0))
        self.lineKinWL.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineKinWL.setObjectName("lineKinWL")
        self.gridLayout.addWidget(self.lineKinWL, 14, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 12, 0, 1, 1)
        self.btnManualEndMode = QtWidgets.QPushButton(self.centralWidget)
        self.btnManualEndMode.setMinimumSize(QtCore.QSize(50, 0))
        self.btnManualEndMode.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnManualEndMode.setObjectName("btnManualEndMode")
        self.gridLayout.addWidget(self.btnManualEndMode, 6, 6, 1, 1)
        self.lineKinLen = QtWidgets.QLineEdit(self.centralWidget)
        self.lineKinLen.setMinimumSize(QtCore.QSize(30, 0))
        self.lineKinLen.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineKinLen.setObjectName("lineKinLen")
        self.gridLayout.addWidget(self.lineKinLen, 14, 5, 1, 1)
        self.btnMono = QtWidgets.QPushButton(self.centralWidget)
        self.btnMono.setMinimumSize(QtCore.QSize(50, 0))
        self.btnMono.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnMono.setObjectName("btnMono")
        self.gridLayout.addWidget(self.btnMono, 13, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 10, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralWidget)
        self.label_11.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        self.comboMonoSpeed = QtWidgets.QComboBox(self.centralWidget)
        self.comboMonoSpeed.setMinimumSize(QtCore.QSize(30, 0))
        self.comboMonoSpeed.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboMonoSpeed.setObjectName("comboMonoSpeed")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.comboMonoSpeed.addItem("")
        self.gridLayout.addWidget(self.comboMonoSpeed, 13, 5, 1, 1)
        self.comboMonoStep = QtWidgets.QComboBox(self.centralWidget)
        self.comboMonoStep.setMinimumSize(QtCore.QSize(30, 0))
        self.comboMonoStep.setMaximumSize(QtCore.QSize(60, 16777215))
        self.comboMonoStep.setObjectName("comboMonoStep")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.comboMonoStep.addItem("")
        self.gridLayout.addWidget(self.comboMonoStep, 13, 4, 1, 1)
        self.lineMonoEnd = QtWidgets.QLineEdit(self.centralWidget)
        self.lineMonoEnd.setMinimumSize(QtCore.QSize(30, 0))
        self.lineMonoEnd.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineMonoEnd.setObjectName("lineMonoEnd")
        self.gridLayout.addWidget(self.lineMonoEnd, 13, 3, 1, 1)
        self.lineMonoStart = QtWidgets.QLineEdit(self.centralWidget)
        self.lineMonoStart.setMinimumSize(QtCore.QSize(30, 0))
        self.lineMonoStart.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineMonoStart.setObjectName("lineMonoStart")
        self.gridLayout.addWidget(self.lineMonoStart, 13, 2, 1, 1)
        self.lineSetWL = QtWidgets.QLineEdit(self.centralWidget)
        self.lineSetWL.setMinimumSize(QtCore.QSize(30, 0))
        self.lineSetWL.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineSetWL.setObjectName("lineSetWL")
        self.gridLayout.addWidget(self.lineSetWL, 0, 5, 1, 1)
        self.lineSetWLWO = QtWidgets.QLineEdit(self.centralWidget)
        self.lineSetWLWO.setMinimumSize(QtCore.QSize(30, 0))
        self.lineSetWLWO.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineSetWLWO.setObjectName("lineSetWLWO")
        self.gridLayout.addWidget(self.lineSetWLWO, 1, 5, 1, 1)
        self.lineFilter = QtWidgets.QLineEdit(self.centralWidget)
        self.lineFilter.setMinimumSize(QtCore.QSize(30, 0))
        self.lineFilter.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineFilter.setObjectName("lineFilter")
        self.gridLayout.addWidget(self.lineFilter, 4, 5, 1, 1)
        DebugWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(DebugWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menuBar.setObjectName("menuBar")
        DebugWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(DebugWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        DebugWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(DebugWindow)
        self.statusBar.setObjectName("statusBar")
        DebugWindow.setStatusBar(self.statusBar)

        self.retranslateUi(DebugWindow)
        self.comboMonoSpeed.setCurrentIndex(2)
        self.comboMonoStep.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(DebugWindow)

    def retranslateUi(self, DebugWindow):
        _translate = QtCore.QCoreApplication.translate
        DebugWindow.setWindowTitle(_translate("DebugWindow", "MainWindow"))
        self.btnSetWL.setText(_translate("DebugWindow", "OK"))
        self.label.setText(_translate("DebugWindow", "Установить длину волны"))
        self.btnManualBeginMode.setText(_translate("DebugWindow", "OK"))
        self.label_9.setText(_translate("DebugWindow", "Остановить р.р.у"))
        self.btnKinetic.setText(_translate("DebugWindow", "OK"))
        self.label_5.setText(_translate("DebugWindow", "Сканирование"))
        self.btnSetFilter.setText(_translate("DebugWindow", "OK"))
        self.lineKinWTime.setText(_translate("DebugWindow", "1"))
        self.label_12.setText(_translate("DebugWindow", "Р.Р.У: Остановить"))
        self.label_3.setText(_translate("DebugWindow", "Измерить"))
        self.btnManualStop.setText(_translate("DebugWindow", "OK"))
        self.btnSetWLWO.setText(_translate("DebugWindow", "OK"))
        self.btnManualFaster.setText(_translate("DebugWindow", "OK"))
        self.label_6.setText(_translate("DebugWindow", "Кинетика"))
        self.btnManualSlower.setText(_translate("DebugWindow", "OK"))
        self.btnManualReverse.setText(_translate("DebugWindow", "OK"))
        self.label_4.setText(_translate("DebugWindow", "Калибровать"))
        self.label_10.setText(_translate("DebugWindow", "Р.Р.У: Вперед"))
        self.btnStop.setText(_translate("DebugWindow", "STOP"))
        self.btnMeasure.setText(_translate("DebugWindow", "OK"))
        self.btnCalib.setText(_translate("DebugWindow", "OK"))
        self.btnManualGetWaveLength.setText(_translate("DebugWindow", "OK"))
        self.btnManualForward.setText(_translate("DebugWindow", "OK"))
        self.lineKinRTime.setText(_translate("DebugWindow", "10"))
        self.labelResult.setText(_translate("DebugWindow", "0"))
        self.label_7.setText(_translate("DebugWindow", "Установить фильтр"))
        self.label_14.setText(_translate("DebugWindow", "Р.Р.У: Скорость - быстрее"))
        self.label_8.setText(_translate("DebugWindow", "Начать режим ручного управления"))
        self.lineKinWL.setText(_translate("DebugWindow", "550"))
        self.label_15.setText(_translate("DebugWindow", "Р.Р.У: Скорость - медленнее"))
        self.btnManualEndMode.setText(_translate("DebugWindow", "OK"))
        self.lineKinLen.setText(_translate("DebugWindow", "5"))
        self.btnMono.setText(_translate("DebugWindow", "OK"))
        self.label_13.setText(_translate("DebugWindow", "Р.Р.У: Получить длину волны"))
        self.label_2.setText(_translate("DebugWindow", "Установить длину волны без учета д.р."))
        self.label_11.setText(_translate("DebugWindow", "Р.Р.У: Назад"))
        self.comboMonoSpeed.setItemText(0, _translate("DebugWindow", "200"))
        self.comboMonoSpeed.setItemText(1, _translate("DebugWindow", "70"))
        self.comboMonoSpeed.setItemText(2, _translate("DebugWindow", "30"))
        self.comboMonoSpeed.setItemText(3, _translate("DebugWindow", "10"))
        self.comboMonoSpeed.setItemText(4, _translate("DebugWindow", "3.3"))
        self.comboMonoSpeed.setItemText(5, _translate("DebugWindow", "1"))
        self.comboMonoSpeed.setItemText(6, _translate("DebugWindow", "0.6"))
        self.comboMonoStep.setCurrentText(_translate("DebugWindow", "0.5"))
        self.comboMonoStep.setItemText(0, _translate("DebugWindow", "0.002"))
        self.comboMonoStep.setItemText(1, _translate("DebugWindow", "0.01"))
        self.comboMonoStep.setItemText(2, _translate("DebugWindow", "0.05"))
        self.comboMonoStep.setItemText(3, _translate("DebugWindow", "0.1"))
        self.comboMonoStep.setItemText(4, _translate("DebugWindow", "0.5"))
        self.comboMonoStep.setItemText(5, _translate("DebugWindow", "1"))
        self.comboMonoStep.setItemText(6, _translate("DebugWindow", "5"))
        self.lineMonoEnd.setText(_translate("DebugWindow", "600"))
        self.lineMonoStart.setText(_translate("DebugWindow", "500"))
        self.lineSetWL.setText(_translate("DebugWindow", "600"))
        self.lineSetWLWO.setText(_translate("DebugWindow", "300"))
        self.lineFilter.setText(_translate("DebugWindow", "1"))


