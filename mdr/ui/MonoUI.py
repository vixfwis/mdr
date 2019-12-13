# -*- coding: utf-8 -*-
import os
from threading import Event

import numpy as np
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtCore

from mdr.messages import RequestFactory
from mdr.const import STEP, SPEED
from mdr.messages.responses.responses import GetFloatValue
from mdr.serial_thread import SerialThread
from mdr.ui import mono_ui_wnd
from mdr.ui.DebugUI import DebugUI
from mdr.ui.qt import ChartView
from mdr.utils.converter import get_scan_array_len
from mdr.utils.io import serialize, deserialize, add_dt_str


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
        self.chartView = ChartView(self.chart)
        self.chartView.setMinimumSize(QtCore.QSize(400, 300))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.linkLE(self.lineXMax, self.lineYMax, self.lineXMin, self.lineYMin)
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
        self.ax.setTickCount(11)
        self.ay.setTickCount(11)
        self.ax.setMinorTickCount(4)
        self.ay.setMinorTickCount(4)
        self.ax.setLabelFormat('%.1f')
        self.ay.setLabelFormat('%.1f')

        self.chart.setAxisX(self.ax, self.curve)
        self.chart.setAxisY(self.ay, self.curve)

        self.rf = RequestFactory()
        self.dbg_wnd = None
        self.current_response = None
        self.blocking_event = Event()

        self.resp_timer = QTimer()
        self.resp_timer.timeout.connect(self.resp_timeout)
        self.resp_timer.start(50)

        self.qActionShow.triggered.connect(self.actionShowDebugWnd)
        self.btnStart.clicked.connect(self.actionMonoScan)
        self.btnStop.clicked.connect(self.actionStop)
        self.menuExit.triggered.connect(self.actionExit)
        self.qActionMDRConnect.triggered.connect(self.actionConnect)
        self.qActionCalibrate.triggered.connect(self.actionCalibrate)
        self.statusBtn.clicked.connect(self.actionStatusReset)
        self.qActionOpenFile.triggered.connect(self.actionOpenFile)

        self.mono_wls = None
        self.scan_data = None
        self.filename = None

        # TODO: remove it
        if self.serial is not None:
            self.serial.abort_current_task()
            self.serial.stop()
            self.serial.join()
            self.serial = None
        self.serial = SerialThread()
        self.serial.setDaemon(True)
        self.serial.start()
        # r = self.rf.get_request('Calibrate')
        # self.serial.requests.put(r)

    def actionOpenFile(self):
        dlg = QFileDialog()
        dlg.setAcceptMode(QFileDialog.AcceptOpen)
        dlg.setFileMode(QFileDialog.ExistingFile)
        name, flt = dlg.getOpenFileName(caption='Open file', directory=os.getcwd(), filter='MonoScan files(*.mcs)')
        with open(name, 'r', encoding='utf-8') as f:
            data = f.read()
        self.scan_data = deserialize(data)
        self.curve.clear()
        ymin = 2 ** 32
        ymax = 0
        for e in self.scan_data['data']:
            self.curve.append(e[0], e[1])
            if float(e[1]) > ymax:
                ymax = float(e[1])
            if float(e[1]) < ymin:
                ymin = float(e[1])
        self.lineXMin.setText(str(self.scan_data['header'][0]))
        self.lineXMax.setText(str(self.scan_data['header'][1]))
        self.lineYMin.setText(f'{ymin:.3}')
        self.lineYMax.setText(f'{ymax:.3}')


    def actionStatusReset(self):
        if self.blocking_event.is_set():
            self.blocking_event.clear()
            self.serial.unblock()
            self.statusLabel.setText('')

    def resp_timeout(self):
        self.chartView.rescale()
        if self.serial is not None:
            req_size = self.serial.requests.qsize()
            res_size = self.serial.response_factory.responses.qsize()
            creq = None
            if not self.serial.requests.empty():
                req_d = self.serial.requests.queue
                creq = req_d[0]
            cres = None
            if not self.serial.response_factory.responses.empty():
                res_d = self.serial.response_factory.responses.queue
                cres = res_d[0]
            self.statusLabel_2.setText(f'ReS: {req_size} RqS: {res_size} ReC: {creq} RqC: {cres} W: {self.serial.mode}')
            if self.current_response or not self.serial.response_factory.responses.empty():
                if self.current_response is None:
                    self.current_response = self.serial.response_factory.responses.get()
                if not self.blocking_event.is_set():
                    if self.serial.get_blocking_event().is_set():
                        self.statusLabel.setText(str(self.current_response.process()))
                        self.blocking_event.set()
                    else:
                        if isinstance(self.current_response, GetFloatValue):
                            x = float(self.mono_wls[0])
                            y = float(self.current_response.process())
                            self.curve.append(x, y)
                            self.mono_wls = self.mono_wls[1:]
                            self.scan_data['data'].append([x, y])
                            with open(self.filename, 'w', encoding='utf-8') as f:
                                f.write(serialize(self.scan_data))
                            # self.writer.write(x, y)
                            # print(f'{x} : {y}; {len(self.mono_wls)}')
                        self.current_response = None

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
        vol1 = float(self.voltagePEM1.text())
        vol2 = float(self.voltagePEM2.text())
        if self.filename is None:
            self.filename = add_dt_str(f'monoscan-{startWL}-{stopWL}')
        self.scan_data = {
            'header': [startWL, stopWL, self.step.currentText(), self.speed.currentText(), vol1, vol2],
            'data': []
        }
        empty = 0
        length = get_scan_array_len(startWL, stopWL, float(self.step.currentText()))
        mono_request = self.rf.get_request('MonoScan', startWL, stopWL, step, speed, empty, length)
        vol1_request = self.rf.get_request('SetVoltage', 1, vol1)
        vol2_request = self.rf.get_request('SetVoltage', 2, vol2)
        self.mono_wls = list(np.linspace(startWL, stopWL, length))
        self.curve.clear()
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

    def actionCalibrate(self):
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
