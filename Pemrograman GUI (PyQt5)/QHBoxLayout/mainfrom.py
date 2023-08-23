from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget, QHBoxLayout, QPushButton

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

        layout = QHBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)