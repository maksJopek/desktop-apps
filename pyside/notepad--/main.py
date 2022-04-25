#!/usr/bin/env python
import sys
import os
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QColorDialog, QFontDialog
from PySide6.QtCore import Qt
from MainWindow import Ui_MainWindow
from darkPalette import darkPalette

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.actionNew.triggered.connect(self.new) #type: ignore
        self.actionOpen.triggered.connect(self.open) #type: ignore
        self.actionSave.triggered.connect(self.save) #type: ignore
        self.actionSave_as.triggered.connect(self.save_as) #type: ignore
        self.actionBold.triggered.connect(self.set_bold) #type: ignore
        self.actionItalic.triggered.connect(self.set_italic) #type: ignore
        self.actionUnderline.triggered.connect(self.set_underline) #type: ignore
        self.actionColor.triggered.connect(self.set_color) #type: ignore
        self.actionFont.triggered.connect(self.set_font) #type: ignore
        self.actionJustify.triggered.connect(self.align_justify) #type: ignore
        self.actionRight.triggered.connect(self.align_right) #type: ignore
        self.actionMiddle.triggered.connect(self.align_middle) #type: ignore
        self.actionLeft.triggered.connect(self.align_left) #type: ignore

        if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
            self.fpath = sys.argv[1]
            self.open(self.fpath)
        else:
            self.fpath = ""

    # Menu `Decorate`
    def align_left(self):
        self.textEdit.setAlignment(Qt.AlignLeft)
    def align_middle(self):
        self.textEdit.setAlignment(Qt.AlignCenter)
    def align_right(self):
        self.textEdit.setAlignment(Qt.AlignRight)
    def align_justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)
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
    def open(self, path=""):
        file_path = path if isinstance(path, str) and path != "" else (QFileDialog.getOpenFileName(self, "Open Text File", self.dir_to_open(), "HTML Files (*.html)")[0])
        if file_path == "":
            return
        self.fpath = file_path
        with open(file_path, 'r') as f:
            self.textEdit.setHtml(f.read())
    def save(self):
        if self.fpath == "":
            file_path = QFileDialog.getSaveFileName(self, "Save Text File", self.dir_to_open(), "HTML Files (*.html)") [0]
            if file_path == "":
                return
            self.fpath = file_path
        else:
            file_path = self.fpath
        with open(file_path, 'w') as f:
            f.write(self.textEdit.toHtml())
    def save_as(self):
        file_path = QFileDialog.getSaveFileName(self, "Save Text File", self.dir_to_open(), "HTML Files (*.html)") [0]
        if file_path == "":
            return
        self.fpath = file_path
        with open(file_path, 'w') as f:
            f.write(self.textEdit.toHtml())
    def dir_to_open(self):
        if self.fpath == "":
            return os.path.expanduser("~") + "/school/desktopApps/pyside/notepad--/"
        else:
            return os.path.dirname(self.fpath)


app = QApplication(sys.argv)
app.setPalette(darkPalette())
app.setStyle("Fusion")
font = app.font()
font.setPointSize(30)
app.setFont(font)
w = MainWindow()
w.show()
app.exec()

