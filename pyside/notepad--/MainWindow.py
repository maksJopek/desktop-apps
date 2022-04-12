# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setGeometry(QRect(4419, 154, 123, 110))
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
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionLeft.setText(QCoreApplication.translate("MainWindow", u"Left", None))
#if QT_CONFIG(shortcut)
        self.actionLeft.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionMiddle.setText(QCoreApplication.translate("MainWindow", u"Middle", None))
#if QT_CONFIG(shortcut)
        self.actionMiddle.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+M", None))
#endif // QT_CONFIG(shortcut)
        self.actionRight.setText(QCoreApplication.translate("MainWindow", u"Right", None))
#if QT_CONFIG(shortcut)
        self.actionRight.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+R", None))
#endif // QT_CONFIG(shortcut)
        self.actionJustify.setText(QCoreApplication.translate("MainWindow", u"Justify", None))
#if QT_CONFIG(shortcut)
        self.actionJustify.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+J", None))
#endif // QT_CONFIG(shortcut)
        self.actionBold.setText(QCoreApplication.translate("MainWindow", u"Bold", None))
#if QT_CONFIG(shortcut)
        self.actionBold.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+B", None))
#endif // QT_CONFIG(shortcut)
        self.actionUnderline.setText(QCoreApplication.translate("MainWindow", u"Underline", None))
#if QT_CONFIG(shortcut)
        self.actionUnderline.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+U", None))
#endif // QT_CONFIG(shortcut)
        self.actionItalic.setText(QCoreApplication.translate("MainWindow", u"Italic", None))
#if QT_CONFIG(shortcut)
        self.actionItalic.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionColor.setText(QCoreApplication.translate("MainWindow", u"Color", None))
#if QT_CONFIG(shortcut)
        self.actionColor.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionFont.setText(QCoreApplication.translate("MainWindow", u"Font", None))
#if QT_CONFIG(shortcut)
        self.actionFont.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+F", None))
#endif // QT_CONFIG(shortcut)
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuDecorate.setTitle(QCoreApplication.translate("MainWindow", u"Decorate", None))
        self.menuAlign.setTitle(QCoreApplication.translate("MainWindow", u"Align", None))
    # retranslateUi

