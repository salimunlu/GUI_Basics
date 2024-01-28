import sys

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QApplication, QWidget, QSlider


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pencere başlığı ve boyutları
        self.setWindowTitle('My Application')
        self.setGeometry(100, 100, 300, 200)

        # QVBoxLayout ve QHBoxLayout örnekleri
        vbox1 = QVBoxLayout()
        hbox1 = QHBoxLayout()
        vbox2 = QVBoxLayout()
        hbox2 = QHBoxLayout()

        # QLabel widget'ı oluştur
        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')
        button3 = QPushButton('Button 3')
        button4 = QPushButton('Button 4')
        button5 = QPushButton('Button 5')
        button6 = QPushButton('Button 6')
        slider1 = QSlider()

        # 1 buton ve 1 label widget'ını QHBoxLayout'a ekle
        hbox1.addWidget(button1)
        hbox1.addWidget(button2)

        # 1 buton ve 1 label widget'ını QVBoxLayout'a ekle
        vbox1.addWidget(button3)
        vbox1.addWidget(button4)

        vbox2.addWidget(button5)
        vbox2.addLayout(hbox1)
        vbox2.addLayout(vbox1)
        vbox2.addWidget(button6)
        vbox2.addWidget(slider1)

        widget = QWidget()
        widget.setLayout(vbox2)
        self.setCentralWidget(widget)

# PyQT uygulamasını başlat
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()




