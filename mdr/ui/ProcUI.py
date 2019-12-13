import os

from PyQt5 import QtCore, QtGui
from PyQt5.QtChart import QChart, QLineSeries, QValueAxis
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QCheckBox, QWidget
from mdr.ui import proc_ui_wnd
from mdr.ui.qt import ChartView
from mdr.utils.io import deserialize


class ProcUI(QMainWindow, proc_ui_wnd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chart = QChart()
        self.chart.legend().hide()
        self.chartView = ChartView(self.chart)
        self.chartView.setMinimumSize(QtCore.QSize(400, 300))
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.linkLE(self.lineXMax, self.lineYMax, self.lineXMin, self.lineYMin)
        self.chartLayout.addWidget(self.chartView)
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

        self.charts = []

        self.curve = QLineSeries()
        pen = self.curve.pen()
        pen.setWidthF(1)
        self.curve.setPen(pen)
        self.chart.addSeries(self.curve)
        self.chart.setAxisX(self.ax, self.curve)
        self.chart.setAxisY(self.ay, self.curve)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_timeout)
        self.update_timer.start(50)

        self.qActionExit.triggered.connect(self.actionExit)
        self.qActionOpen.triggered.connect(self.actionOpen)
        self.btnTest.clicked.connect(self.actionBtn)

    # TODO: finish layoutl dynamically add checkboxes as needed from left side
    def actionBtn(self):
        c = self.get_checkbox(self.chartViewControl, 5)
        self.chartViewControl.layout().addWidget(c)
        self.charts.append(c)

    def actionExit(self):
        self.close()

    def actionOpen(self):
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

    def update_timeout(self):
        self.chartView.rescale()

    @staticmethod
    def get_checkbox(parent: QWidget, text: int) -> QCheckBox:
        c = QCheckBox(parent)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        c.setFont(font)
        c.setText(str(text))
        c.setObjectName(f'chkChart{text}')
        return c
