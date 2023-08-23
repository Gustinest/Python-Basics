import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

if __name__ == '__main__':
    a = QApplication(sys.argv)

    form = QWidget()
    form.resize(500, 400)
    form.move(400, 600)
    form.setWindowTitle('GUI minimal')

    label = QLabel('Hello world lorem ipsum doloe sie Met', parent=form)  # Anda juga bisa menambahkan parent saat membuat QLabel.

    form.show()  # Perlu menambahkan tanda kurung untuk menampilkan form.

    sys.exit(a.exec_())  # Menggunakan sys.exit untuk keluar dari aplikasi setelah a.exec_() selesai.
