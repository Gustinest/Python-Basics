from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget

class TextFrom(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 400)
        self.move(400, 600)
        self.setWindowTitle('GUI HTML dann CSS')

        self.label1 = QLabel(
            '<H1> Hello <font color=red>Wold</font><.h1>'
        )
        self.label1.move(10, 10)
        self.label1.setParent(self)

        self.label2 = QLabel('''
        conroh teks <b>tebal</b>, <i>miring</i>, dan <u>bergaris bawah</u>
        ''')
        self.label2.setWordWrap(True)
        self.label2.move(10, 50)
        self.label2.setParent(self)

        self.setStyleSheet('background-color: blue;')

    def setcenter(self):
        desktop = QDesktopWidget()
        screenwidht = desktop.screen(). width()
        screenheight = desktop.screen().height()

        self.setGeometry((screenwidht - self.width()) // 2,
                         (screenheight - self.height()) // 2,
                         self.width(),
                         self.height())