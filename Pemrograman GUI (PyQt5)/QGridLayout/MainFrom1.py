from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QGridLayout, QPushButton, QLineEdit

class Mainfrom(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.resize(300, 100)
        self.move(300, 300)
        self.setWindowTitle('DEMO QHBoxLayout')

        self.label1 = QLabel('Nama')
        self.lineedit1 = QLineEdit()

        self.label2 = QLabel('No Handphone')
        self.lineedit2 = QLineEdit()
        
        self.button4 = QPushButton('OK')

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineedit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineedit2, 1, 1)
        layout.addWidget(self.button4, 2, 0, 1, 2)

        self.setLayout(layout)