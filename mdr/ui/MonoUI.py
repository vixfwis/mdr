# -*- coding: utf-8 -*-
from threading import Event

import numpy as np
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QPolygonF
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

from mdr.messages import RequestFactory
from mdr.const import STEP, SPEED
from mdr.messages.responses.responses import GetFloatValue
from mdr.serial_thread import SerialThread
from mdr.ui import mono_ui_wnd
from mdr.ui.DebugUI import DebugUI
from mdr.utils.converter import get_scan_array_len


class MonoUI(QMainWindow, mono_ui_wnd.Ui_MainWindow):
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

        self.rf = RequestFactory()
        self.dbg_wnd = None
        self.current_response = None
        self.blocking_event = Event()

        self.resp_timer = QTimer()
        self.resp_timer.timeout.connect(self.resp_timeout)
        self.resp_timer.start(50)

        self.actionShow.triggered.connect(self.actionShowDebugWnd)
        self.btnStart.clicked.connect(self.actionMonoScan)
        self.btnStop.clicked.connect(self.actionStop)
        self.menuExit.triggered.connect(self.actionExit)
        self.actionMDRConnect.triggered.connect(self.actionConnect)
        self.actionCalibrate.triggered.connect(self.actionCalib)
        self.statusBtn.clicked.connect(self.actionStatusReset)

        self.mono_data = []
        self.mono_wls = None

    def actionStatusReset(self):
        if self.blocking_event.is_set():
            self.blocking_event.clear()
            self.serial.unblock()
            self.statusLabel.setText('')

    def resp_timeout(self):
        if self.serial is not None:
            creq = None
            if not self.serial.requests.empty():
                req_d = self.serial.requests.queue
                creq = req_d[0]
            cres = None
            if not self.serial.response_factory.responses.empty():
                res_d = self.serial.response_factory.responses.queue
                cres = res_d[0]
            self.statusLabel_2.setText(f'ReC: {creq} RqC: {cres} W: {self.serial.mode}')
            if self.current_response or not self.serial.response_factory.responses.empty():
                if self.current_response is None:
                    self.current_response = self.serial.response_factory.responses.get()
                if not self.blocking_event.is_set():
                    if self.serial.get_blocking_event().is_set():
                        pass  # todo: set status message and blocking event
                        self.statusLabel.setText(str(self.current_response.process()))
                        self.blocking_event.set()
                    else:
                        pass  # todo: switch case on response class and process data
                        if isinstance(self.current_response, GetFloatValue):
                            x = float(self.mono_wls[0])
                            y = float(self.current_response.process())
                            self.mono_data.append((x, y))
                            print(y)
                            self.curve.append(x, y)
                            self.mono_wls = self.mono_wls[1:]

    def actionExit(self):
        exit(0)

    def actionStop(self):
        if self.serial is not None:
            self.serial.abort_current_task()

    def actionMonoScan(self):
        startWL = float(self.rangeLow.text())
        stopWL = float(self.rangeHigh.text())
        step = STEP[self.step.currentText()]
        speed = SPEED[self.speed.currentText()]
        empty = 0
        length = get_scan_array_len(startWL, stopWL, float(self.step.currentText()))
        mono_request = self.rf.get_request('MonoScan', startWL, stopWL, step, speed, empty, length)
        vol1_request = self.rf.get_request('SetVoltage', 1, float(self.voltagePEM1.text()))
        vol2_request = self.rf.get_request('SetVoltage', 2, float(self.voltagePEM2.text()))
        self.mono_wls = list(np.linspace(startWL, stopWL, length))
        self.serial.requests.put(vol1_request)
        self.serial.requests.put(vol2_request)
        self.serial.requests.put(mono_request)


    def actionShowDebugWnd(self):
        if self.serial is None:
            self.serial = SerialThread()
            self.serial.setDaemon(True)
            self.serial.start()
        self.dbg_wnd = DebugUI(self.serial)
        self.dbg_wnd.show()

    def actionCalib(self):
        r = self.rf.get_request('Calibrate')
        self.serial.requests.put(r)

    def setStatus(self, status):
        self.setStatusBar(status)

    def actionConnect(self):
        if self.serial is not None:
            self.serial.abort_current_task()
            self.serial.stop()
            self.serial.join()
            self.serial = None
        self.serial = SerialThread()
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


