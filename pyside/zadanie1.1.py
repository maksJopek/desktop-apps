#!/usr/bin/env python
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QLabel
import sys
from random import choice

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('App')
        layout = QVBoxLayout()

        self.textL = QLineEdit(self)
        layout.addWidget(self.textL)

        self.button = QPushButton('Calc my numbers', self)
        layout.addWidget(self.button)
        self.button.clicked.connect(self.click_handle)

        self.sortedL = QLabel(self)
        self.minL = QLabel(self)
        self.maxL = QLabel(self)
        self.avgL = QLabel(self)

        layout.addWidget(self.sortedL)
        layout.addWidget(self.minL)
        layout.addWidget(self.maxL)
        layout.addWidget(self.avgL)

        widget = QWidget() 
        widget.setLayout(layout) 
        self.setCentralWidget(widget) 

    def click_handle(self):
        t = self.textL.text()

        ta = filter(lambda x: x != "", t.split(','))
        ta = map(lambda x: int(x), ta)

        ta = sorted(ta, reverse=True)
        st = ','.join(map(lambda x: str(x), ta))

        self.sortedL.setText(st)
        self.minL.setText(str(min(ta)))
        self.maxL.setText(str(max(ta)))
        self.avgL.setText(str(round(sum(ta) / len(ta), 2)))


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

