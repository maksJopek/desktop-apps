#!/usr/bin/env python
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sample Qt App")
        self.setFixedSize(QSize(300, 300))

        button = QPushButton("Click me")
        button.setCheckable(True)
        button.clicked.connect(self.clicked)
        button.clicked.connect(self.toogled)

        self.setCentralWidget(button)

    def clicked(self):
        print("CLicked")

    def toogled(self, checked):
        print("Clicked?", checked)


window = MainWindow()
window.show()
app.exec()
