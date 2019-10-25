# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication

from mdr.serial_thread import SerialThread
from mdr.ui.DebugUI import DebugUI
from mdr.ui.MonoUI import MonoUI


def main():
    serial = SerialThread()
    serial.setDaemon(True)
    serial.start()
    app = QApplication(sys.argv)
    window = DebugUI(serial=serial)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
