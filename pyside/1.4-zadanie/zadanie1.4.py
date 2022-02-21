#!/usr/bin/env python
import sys
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QToolBar, QStatusBar, QLineEdit, QWidget
from PySide6.QtGui import QAction, QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Menu")

        input = QLineEdit()
        input.setAlignment(Qt.AlignCenter)
        self.input = input
        # self.setCentralWidget(input)

        label = QLabel('')
        label.setAlignment(Qt.AlignCenter)
        self.label = label

        layout = QVBoxLayout()
        layout.addWidget(input)
        layout.addWidget(label)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        toolBar = QToolBar('Menu główne')
        toolBar.setIconSize(QSize(22, 22))
        self.addToolBar(toolBar)

        actBubel = QAction(QIcon("bubble.png"), 'Bubel sort', self)
        actBubel.setStatusTip('Algorytm babelkowy')
        actBubel.triggered.connect(self.bubelSort)
        toolBar.addAction(actBubel)
        toolBar.addSeparator()

        actstalin = QAction(QIcon("stalin.png"),'Stalin sort', self)
        actstalin.setStatusTip('Sort inspired by stalin')
        actstalin.triggered.connect(self.stalinSort)
        toolBar.addAction(actstalin)
        toolBar.addSeparator()

        actquick = QAction(QIcon("def.png"), 'Python default sort funtion', self)
        actquick.setStatusTip('array.sort()')
        actquick.triggered.connect(self.quickSort)
        toolBar.addAction(actquick)

        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        fileMenu = menu.addMenu('&Algorytmy')
        fileMenu.addAction(actBubel)
        fileMenu.addSeparator()
        fileMenu.addAction(actquick)
        fileMenu.addSeparator()
        fileMenu.addAction(actstalin)

    def get_data(self):
        data = self.input.text()
        data = [int(x) for x in data.split(',')]
        return data

    def bubelSort(self):
        arr = self.get_data()
        n = len(arr)
 
        # Traverse through all array elements
        for i in range(n):
 
            # Last i elements are already in place
            for j in range(0, n-i-1):
 
                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        
        self.label.setText(str(arr)[1:-1])

    def stalinSort(self):
        l = self.get_data()
        max_val = l[0]
        
        def add_val(num):
            nonlocal max_val
            max_val = num
            return num
       
        self.label.setText(str([add_val(x) for x in l if x >= max_val])[1:-1])
                
    def quickSort(self):
        a = self.get_data()
        a.sort()
        self.label.setText(str(a)[1:-1])

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()

