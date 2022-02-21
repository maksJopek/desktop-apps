#!/usr/bin/env python
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zmiana interfejsu")

        self.button = QPushButton("Zmien")
        self.button.clicked.connect(self.buttonClicked) 
    
        self.setCentralWidget(self.button)

    def buttonClicked(self):
        self.button.setText("Interfejs ostal zmieniony")
        self.button.setEnabled(False)

        self.setWindowTitle('Nowy tytul okna')


window = MainWindow()
window.show()
app.exec()
