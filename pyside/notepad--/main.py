#!/usr/bin/env python
import sys
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel, QLineEdit, QMainWindow, QPlainTextEdit, QPushButton, QSpinBox, QVBoxLayout, QWidget)
from MainWindow import Ui_MainWindow
from darkPalette import darkPalette

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

app = QApplication(sys.argv)
app.setPalette(darkPalette())
app.setStyle("Fusion")
w = MainWindow()
w.show()
app.exec()

