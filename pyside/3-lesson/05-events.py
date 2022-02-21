#!/usr/bin/env python
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

app = QApplication(sys.argv)
windowTitles = ['1', '2', '3', '4']

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.timesClicked = 0
        self.setWindowTitle("Moja aplikacja")

        self.button = QPushButton("Change title")
        self.button.clicked.connect(self.buttonClicked)

        self.windowTitleChanged.connect(self.mineWindowTitleChange)
        self.setCentralWidget(self.button)

    def buttonClicked(self):
        print("Btn clicked")
        newTitle = choice(windowTitles)
        print(f"Ustawiono {newTitle}")
        self.setWindowTitle(newTitle)

    def mineWindowTitleChange(self, windowTitle):
        if windowTitle == '4':
            self.button.setDisabled(True)


window = MainWindow()
window.show()
app.exec()
