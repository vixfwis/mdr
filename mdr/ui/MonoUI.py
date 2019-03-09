# -*- coding: utf-8 -*-

import numpy as np
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

from mdr.messages.const import STEP, SPEED
from mdr.serial_thread import SerialThread
from mdr.ui import mono_ui_wnd


class MonoUI(QMainWindow, mono_ui_wnd.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.step.clear()
        self.step.addItems([str(s) for s in STEP.keys()])
        self.speed.clear()
        self.speed.addItems([str(s) for s in SPEED.keys()])
        self.chart = QChart()
        self.chart.legend().hide()
        self.chartView = QChartView(self.chart)
        self.chartView.setMinimumSize(QtCore.QSize(400, 300))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartLayout.addWidget(self.chartView)

        self.serial = None

        self.curve = QLineSeries()
        pen = self.curve.pen()
        pen.setWidthF(1)
        self.curve.setPen(pen)
        self.chart.addSeries(self.curve)

        self.ax = QValueAxis()
        self.ay = QValueAxis()
        self.ax.setRange(0, 600)
        self.ay.setRange(0, 100)
        self.ax.setTickCount(7)
        self.ay.setTickCount(11)
        self.ax.setMinorTickCount(1)
        self.ay.setMinorTickCount(1)

        self.chart.setAxisX(self.ax, self.curve)
        self.chart.setAxisY(self.ay, self.curve)

        self.menuConnect.triggered.connect(self.actMenuConnect)

    def actMenuConnect(self):
        if self.serial is not None:
            self.serial.stop()
        self.serial = SerialThread(port='COM4')
        self.serial.setDaemon(True)
        self.serial.start()

    def rescale_chart(self):
        xmax = 1
        xmin = 0
        ymax = 1
        ymin = 0
        for p in self.curve.pointsVector():
            if p.x() > xmax:
                xmax = p.x()
            if p.x() < xmin:
                xmin = p.x()
            if p.y() > ymax:
                ymax = p.y()
            if p.y() < ymin:
                ymin = p.y()
        self.ax.setMax(xmax)
        self.ax.setMin(xmin)
        self.ay.setMax(ymax)
        self.ay.setMin(ymin)

    def series_to_polyline(self, xdata, ydata):
        size = len(xdata)
        polyline = QPolygonF(size)
        pointer = polyline.data()
        dtype, tinfo = np.float, np.finfo  # integers: = np.int, np.iinfo
        pointer.setsize(2 * polyline.size() * tinfo(dtype).dtype.itemsize)
        memory = np.frombuffer(pointer, dtype)
        memory[:(size - 1) * 2 + 1:2] = xdata
        memory[1:(size - 1) * 2 + 2:2] = ydata
        return polyline


