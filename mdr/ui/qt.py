from PyQt5.QtChart import QChartView
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QWheelEvent
from PyQt5.QtWidgets import QRubberBand

SCROLL_VALUE = 0.05


class ChartView(QChartView):
    def __init__(self, *args):
        super().__init__(*args)
        self._band = QRubberBand(QRubberBand.Rectangle, self)
        self._origin = QPoint()
        self._xmax = 600
        self._xmin = 0
        self._ymax = 100
        self._ymin = 0

    def setXMaxLE(self, val):
        self._xmaxLE.setText('{0:.1f}'.format(val))

    def setYMaxLe(self, val):
        self._ymaxLE.setText('{0:.1f}'.format(val))

    def setXMinLE(self, val):
        self._xminLE.setText('{0:.1f}'.format(val))

    def setYMinLe(self, val):
        self._yminLE.setText('{0:.1f}'.format(val))

    def linkLE(self, xmaxLE, ymaxLE, xminLE, yminLE):
        self._xmaxLE = xmaxLE
        self._ymaxLE = ymaxLE
        self._xminLE = xminLE
        self._yminLE = yminLE

    def rescale(self):
        xmax = self._xmax
        ymax = self._ymax
        xmin = self._xmin
        ymin = self._ymin
        try:
            xmax = float(self._xmaxLE.text())
            ymax = float(self._ymaxLE.text())
            xmin = float(self._xminLE.text())
            ymin = float(self._yminLE.text())
        except ValueError:
            pass
        self._xmax = xmax
        self._ymax = ymax
        self._xmin = xmin
        self._ymin = ymin
        for axis in self.chart().axes(Qt.Horizontal):
            axis.setMax(xmax)
            axis.setMin(xmin)
        for axis in self.chart().axes(Qt.Vertical):
            axis.setMax(ymax)
            axis.setMin(ymin)

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._origin = QPoint(event.pos())
            self._band.setGeometry(QRect(self._origin, QSize()))
            self._band.show()
        event.accept()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        if self._band.isVisible():
            if abs(event.pos().x() - self._origin.x()) > 3 and abs(event.pos().y() - self._origin.y()) > 3:
                src = self.chart().mapToValue(self._origin)
                dst = self.chart().mapToValue(event.pos())
                self.setXMaxLE(max(dst.x(), src.x()))
                self.setYMaxLe(max(dst.y(), src.y()))
                self.setXMinLE(min(dst.x(), src.x()))
                self.setYMinLe(min(dst.y(), src.y()))
            self._band.hide()
        event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if not self._origin.isNull():
            self._band.setGeometry(QRect(self._origin, event.pos()).normalized())
        event.accept()

    def wheelEvent(self, event: QWheelEvent):
        scrollAngle = event.angleDelta().y()
        try:
            ratio = (self._xmax - self._xmin) / (self._ymax - self._ymin)
            if scrollAngle > 0:
                nxmax = self._xmax * (1 - SCROLL_VALUE)
                nxmin = self._xmin + (self._xmax - nxmax)
                nydiff = abs(((nxmax - nxmin) / ratio) - (self._ymax - self._ymin))
                nymax = self._ymax - nydiff / 2
                nymin = self._ymin + nydiff / 2
                self.setXMaxLE(nxmax)
                self.setYMaxLe(nymax)
                self.setXMinLE(nxmin)
                self.setYMinLe(nymin)
            if scrollAngle < 0:
                nxmax = self._xmax * (1 + SCROLL_VALUE)
                nxmin = self._xmin - (nxmax - self._xmax)
                nydiff = abs(((nxmax - nxmin) / ratio) - (self._ymax - self._ymin))
                nymax = self._ymax + nydiff / 2
                nymin = self._ymin - nydiff / 2
                self.setXMaxLE(nxmax)
                self.setYMaxLe(nymax)
                self.setXMinLE(nxmin)
                self.setYMinLe(nymin)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        event.accept()

