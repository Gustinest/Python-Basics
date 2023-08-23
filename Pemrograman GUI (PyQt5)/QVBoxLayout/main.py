import sys
from PyQt5.QtWidgets import QApplication

from Mainfrom import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = Mainfrom()
    form.show()

    a.exec_()