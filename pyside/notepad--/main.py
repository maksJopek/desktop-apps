#!/usr/bin/env python
import sys
import os
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QColorDialog, QFontDialog
from MainWindow import Ui_MainWindow
from darkPalette import darkPalette

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.fname = ""
        self.actionNew.triggered.connect(self.new) #type: ignore
        self.actionOpen.triggered.connect(self.open) #type: ignore
        self.actionSave.triggered.connect(self.save) #type: ignore
        self.actionBold.triggered.connect(self.set_bold) #type: ignore
        self.actionItalic.triggered.connect(self.set_italic) #type: ignore
        self.actionUnderline.triggered.connect(self.set_underline) #type: ignore
        self.actionColor.triggered.connect(self.set_color) #type: ignore
        self.actionFont.triggered.connect(self.set_font) #type: ignore
        self.actionJustify.triggered.connect(self.align_justify) #type: ignore
        self.actionRight.triggered.connect(self.align_right) #type: ignore
        self.actionMiddle.triggered.connect(self.align_middle) #type: ignore
        self.actionLeft.triggered.connect(self.align_left) #type: ignore

    # Menu `Decorate`
    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft) #type: ignore
    def align_middle(self):
        self.textEdit.setAlignment(Qt.AlignCenter) #type: ignore   
    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight) #type: ignore
    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify) #type: ignore
    def set_color(self):
        self.textEdit.setTextColor(QColorDialog.getColor())
    def set_font(self):
        font = QFontDialog.getFont()
        if font[0] == True:
            self.textEdit.setFont(font[1])
    def set_bold(self):
        self.textEdit.setFontWeight(800 if self.textEdit.fontWeight() == 400 else 400)
    def set_italic(self):
        self.textEdit.setFontItalic(not self.textEdit.fontItalic())
    def set_underline(self):
        self.textEdit.setFontUnderline(not self.textEdit.fontUnderline())

    # Menu `File`
    def new(self):
        self.textEdit.setText("")
        self.fname = ""
    def open(self):
        file_name = QFileDialog.getOpenFileName(self, "Open Text File", os.path.expanduser("~") + "/school/desktopApps/pyside/notepad--", "Text Files (*.txt)") 
        if file_name[0] == "":
            return
        with open(file_name[0], 'r') as f:
            self.textEdit.setPlainText(f.read())
        self.fname = file_name[0]
    def save(self):
        file_name = QFileDialog.getSaveFileName(self, "Save Text File", os.path.expanduser("~") + "/school/desktopApps/pyside/notepad--/" + self.fname, "Text Files (*.txt)") 
        if file_name[0] == "":
            return
        with open(file_name[0], 'w') as f:
            f.write(self.textEdit.toPlainText())


app = QApplication(sys.argv)
app.setPalette(darkPalette())
app.setStyle("Fusion")
font = app.font()
font.setPointSize(30)
app.setFont(font)
w = MainWindow()
w.show()
app.exec()

