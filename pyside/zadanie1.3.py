#!/usr/bin/env python
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QPushButton
from PySide6.QtGui import QPalette, QColor
import re

class Color(QWidget):

    def __init__(self, color: str):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Layout")

        layout = QGridLayout()

        screen = QLabel('')
        layout.addWidget(screen, 0, 0, 1, 4)
        k = 0
        main_btns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '0', '=']

        def add_text(a):
            return lambda: add_text2(a)
        def add_text2(a):
            if len(screen.text()) > 0:
                if a == '=':
                    try:
                       screen.setText(str(eval(screen.text())))
                    except ZeroDivisionError:
                       screen.setText('') 
                    except SyntaxError:
                       pass
                    return 
                if a == 'C':
                    screen.setText('')
                    return
                lc = screen.text()[-1]
                if a == '-' and lc[-1] in ['*', '/']:
                    screen.setText(f"{screen.text()}{a}")
                    return
                if re.match("\\D", lc) and re.match("\\D", a):
                    return
            screen.setText(f"{screen.text()}{a}")

        for i in range(1, 5):
            for j in range(0, 3):
                btn = QPushButton(main_btns[k])
                layout.addWidget(btn, i, j)
                btn.clicked.connect(add_text(main_btns[k]))
                k += 1

        supp_btns = [0, "+", '-', '*', '/', 'C']
        for i in range(1, 6):
            btn = QPushButton(supp_btns[i])
            if i == 5:
                layout.addWidget(btn, i, 0, 1, 4)
            else:
                layout.addWidget(btn, i, 3)
            btn.clicked.connect(add_text(supp_btns[i]))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
