# -*- coding: utf-8 -*-
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow

from mdr.messages import RequestFactory
from mdr.messages.const import STEP, SPEED
from mdr.serial_thread import SerialThread
from mdr.ui import debug_ui_wnd


class DebugUI(QMainWindow, debug_ui_wnd.Ui_DebugWindow):
    def __init__(self, serial):
        super().__init__()
        self.setupUi(self)
        self.serial = serial
        self.rf = RequestFactory()

        self.resp_timer = QTimer()
        self.resp_timer.timeout.connect(self.resp_timeout)
        self.resp_timer.start(250)

        self.intr_timer = QTimer()
        self.intr_timer.timeout.connect(self.intr_timeout)
        self.intr_timer.start(250)

        self.btnSetWL.clicked.connect(self.set_wl)
        self.btnSetWLWO.clicked.connect(self.set_wlwo)
        self.btnMeasure.clicked.connect(self.measure)
        self.btnCalib.clicked.connect(self.calibrate)
        self.btnSetFilter.clicked.connect(self.set_filter)
        self.btnManualBeginMode.clicked.connect(self.manual_begin)
        self.btnManualEndMode.clicked.connect(self.manual_end)
        self.btnManualForward.clicked.connect(self.manual_forward)
        self.btnManualReverse.clicked.connect(self.manual_reverse)
        self.btnManualStop.clicked.connect(self.manual_stop)
        self.btnManualGetWaveLength.clicked.connect(self.manual_get_wl)
        self.btnManualFaster.clicked.connect(self.manual_faster)
        self.btnManualSlower.clicked.connect(self.manual_slower)
        self.btnStop.clicked.connect(self.abort)

    def intr_timeout(self):
        if self.serial.get_blocking_event().is_set():
            self.serial.unblock()

    def resp_timeout(self):
        if not self.serial.response_factory.responses.empty():
            r = self.serial.response_factory.responses.get()
            self.labelResult.setText(str(r.process()))

    def set_wl(self):
        wl = float(self.lineSetWL.text())
        r = self.rf.get_request('SetWaveLength', wl)
        self.serial.requests.put(r)

    def set_wlwo(self):
        wl = float(self.lineSetWLWO.text())
        r = self.rf.get_request('SetWaveLengthWO', wl)
        self.serial.requests.put(r)

    def measure(self):
        r = self.rf.get_request('Measure')
        self.serial.requests.put(r)

    def calibrate(self):
        r = self.rf.get_request('Calibrate')
        self.serial.requests.put(r)

    def set_filter(self):
        f = int(self.lineFilter.text())
        r = self.rf.get_request('SetFilter', f)
        self.serial.requests.put(r)

    def manual_begin(self):
        r = self.rf.get_request('ManualBeginMode')
        self.serial.requests.put(r)

    def manual_end(self):
        r = self.rf.get_request('ManualEndMode')
        self.serial.requests.put(r)

    def manual_forward(self):
        r = self.rf.get_request('ManualForward')
        self.serial.requests.put(r)

    def manual_reverse(self):
        r = self.rf.get_request('ManualReverse')
        self.serial.requests.put(r)

    def manual_stop(self):
        r = self.rf.get_request('ManualStop')
        self.serial.requests.put(r)

    def manual_get_wl(self):
        r = self.rf.get_request('ManualGetWaveLength')
        self.serial.requests.put(r)

    def manual_faster(self):
        r = self.rf.get_request('ManualFaster')
        self.serial.requests.put(r)

    def manual_slower(self):
        r = self.rf.get_request('ManualSlower')
        self.serial.requests.put(r)

    def abort(self):
        self.serial.abort_current_task()