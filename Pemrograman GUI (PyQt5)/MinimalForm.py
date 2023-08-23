from PyQt5.QtWidgets import QWidget, QLabel, QDesktopWidget

class MinimalForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(500, 400)
        self.move(400, 600)
        self.setWindowTitle('GUI minimal')

        self.label = QLabel('Hello world lorem ipsum doloe sie Met')  # Anda juga bisa menambahkan parent saat membuat QLabel.
        self.label.move(55,40)
        self.label.setParent(self)
        
    def setcenter(self):
        desktop = QDesktopWidget()
        screenwidht = desktop.screen(). width()
        screenheight = desktop.screen().height()

        self.setGeometry((screenwidht - self.width()) // 2,
                         (screenheight - self.height()) // 2,
                         self.width(),
                         self.height())