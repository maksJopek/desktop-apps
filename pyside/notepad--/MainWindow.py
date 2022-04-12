# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionLeft = QAction(MainWindow)
        self.actionLeft.setObjectName(u"actionLeft")
        self.actionMiddle = QAction(MainWindow)
        self.actionMiddle.setObjectName(u"actionMiddle")
        self.actionRight = QAction(MainWindow)
        self.actionRight.setObjectName(u"actionRight")
        self.actionJustify = QAction(MainWindow)
        self.actionJustify.setObjectName(u"actionJustify")
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        self.actionUnderline = QAction(MainWindow)
        self.actionUnderline.setObjectName(u"actionUnderline")
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        self.actionColor = QAction(MainWindow)
        self.actionColor.setObjectName(u"actionColor")
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(-7, -1, 811, 621))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuDecorate = QMenu(self.menubar)
        self.menuDecorate.setObjectName(u"menuDecorate")
        self.menuAlign = QMenu(self.menuDecorate)
        self.menuAlign.setObjectName(u"menuAlign")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDecorate.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuDecorate.addAction(self.menuAlign.menuAction())
        self.menuDecorate.addSeparator()
        self.menuDecorate.addAction(self.actionColor)
        self.menuDecorate.addAction(self.actionFont)
        self.menuDecorate.addSeparator()
        self.menuDecorate.addAction(self.actionBold)
        self.menuDecorate.addAction(self.actionItalic)
        self.menuDecorate.addAction(self.actionUnderline)
        self.menuAlign.addAction(self.actionLeft)
        self.menuAlign.addAction(self.actionMiddle)
        self.menuAlign.addAction(self.actionRight)
        self.menuAlign.addAction(self.actionJustify)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.actionMiddle.setText(QCoreApplication.translate("MainWindow", u"Middle", None))
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.actionJustify.setText(QCoreApplication.translate("MainWindow", u"Justify", None))
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
        self.actionUnderline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
        self.actionColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.actionFont.setText(QCoreApplication.translate("MainWindow", u"Font", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDecorate.setTitle(QCoreApplication.translate("MainWindow", u"Decorate", None))
        self.menuAlign.setTitle(QCoreApplication.translate("MainWindow", u"Align", None))
    # retranslateUi

