import sys
from PyQt5.QtWidgets import QApplication

from Mainfrom import *

if __name__ == '__main__':
    a = QApplication(sys.argv)

    minform = Mainfrom()
    minform.show()

    a.exec_()