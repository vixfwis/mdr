# -*- coding: utf-8 -*-
import logging
import sys
from PyQt5.QtWidgets import QApplication
from mdr.ui.MonoUI import MonoUI
from mdr.ui.ProcUI import ProcUI


def main():
    # logging.basicConfig(filename='mdr.log', level=logging.DEBUG)
    app = QApplication(sys.argv)
    window = MonoUI()
    #window = ProcUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
