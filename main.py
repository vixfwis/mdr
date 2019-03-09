# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from mdr.ui.MonoUI import MonoUI


def main():
    app = QApplication(sys.argv)
    window = MonoUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
