# -*- coding: utf-8 -*-

import sys
import numpy as np
import mainwindow
from PyQt5.QtChart import QChart, QChartView, QLineSeries
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore

def series_to_polyline(xdata, ydata):
    size = len(xdata)
    polyline = QPolygonF(size)
    pointer = polyline.data()
    dtype, tinfo = np.float, np.finfo  # integers: = np.int, np.iinfo
    pointer.setsize(2 * polyline.size() * tinfo(dtype).dtype.itemsize)
    memory = np.frombuffer(pointer, dtype)
    memory[:(size - 1) * 2 + 1:2] = xdata
    memory[1:(size - 1) * 2 + 2:2] = ydata
    return polyline

class App(QMainWindow, mainwindow.Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chart = QChart()
        self.chart.legend().hide()
        self.chartView = QChartView(self.chart)
        self.chartView.setMinimumSize(QtCore.QSize(400, 300))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartLayout.addWidget(self.chartView)

        xdata = np.linspace(0, np.pi*2, 1000)
        ydata = np.sin(xdata)
        curve = QLineSeries()
        pen = curve.pen()
        pen.setWidthF(1)
        curve.setPen(pen)
        curve.append(series_to_polyline(xdata, ydata))
        self.chart.addSeries(curve)
        self.chart.createDefaultAxes()

def main():
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
