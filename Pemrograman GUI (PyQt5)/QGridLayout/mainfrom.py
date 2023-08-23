from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QGridLayout, QPushButton, QLineEdit

class Mainfrom(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.resize(300, 300)
        self.move(300, 300)
        self.setWindowTitle('DEMO QHBoxLayout')

        self.button1 = QPushButton('Button 1')
        self.button2 = QPushButton('Button 2')
        self.button3 = QPushButton('Button 3')
        self.button4 = QPushButton('Button 4')

        layout = QGridLayout()
        layout.addWidget(self.button1, 0, 0)
        layout.addWidget(self.button2, 0, 1)
        layout.addWidget(self.button3, 1, 0)
        layout.addWidget(self.button4, 1, 1)

        self.setLayout(layout)