# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.uic'
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 806, 581))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.b_divide = QPushButton(self.gridLayoutWidget)
        self.b_divide.setObjectName(u"b_divide")
        font = QFont()
        font.setPointSize(16)
        self.b_divide.setFont(font)

        self.gridLayout.addWidget(self.b_divide, 5, 3, 1, 1)

        self.b9 = QPushButton(self.gridLayoutWidget)
        self.b9.setObjectName(u"b9")
        self.b9.setFont(font)

        self.gridLayout.addWidget(self.b9, 4, 2, 1, 1)

        self.b_dctg = QPushButton(self.gridLayoutWidget)
        self.b_dctg.setObjectName(u"b_dctg")
        self.b_dctg.setFont(font)

        self.gridLayout.addWidget(self.b_dctg, 6, 4, 1, 1)

        self.b_ctg = QPushButton(self.gridLayoutWidget)
        self.b_ctg.setObjectName(u"b_ctg")
        self.b_ctg.setFont(font)

        self.gridLayout.addWidget(self.b_ctg, 5, 4, 1, 1)

        self.b_period = QPushButton(self.gridLayoutWidget)
        self.b_period.setObjectName(u"b_period")
        self.b_period.setFont(font)

        self.gridLayout.addWidget(self.b_period, 5, 0, 1, 1)

        self.b2 = QPushButton(self.gridLayoutWidget)
        self.b2.setObjectName(u"b2")
        self.b2.setFont(font)

        self.gridLayout.addWidget(self.b2, 2, 1, 1, 1)

        self.b0 = QPushButton(self.gridLayoutWidget)
        self.b0.setObjectName(u"b0")
        self.b0.setFont(font)

        self.gridLayout.addWidget(self.b0, 5, 1, 1, 1)

        self.b4 = QPushButton(self.gridLayoutWidget)
        self.b4.setObjectName(u"b4")
        self.b4.setFont(font)

        self.gridLayout.addWidget(self.b4, 3, 0, 1, 1)

        self.b_tg = QPushButton(self.gridLayoutWidget)
        self.b_tg.setObjectName(u"b_tg")
        self.b_tg.setFont(font)

        self.gridLayout.addWidget(self.b_tg, 4, 4, 1, 1)

        self.b_equal = QPushButton(self.gridLayoutWidget)
        self.b_equal.setObjectName(u"b_equal")
        self.b_equal.setFont(font)

        self.gridLayout.addWidget(self.b_equal, 5, 2, 1, 1)

        self.b8 = QPushButton(self.gridLayoutWidget)
        self.b8.setObjectName(u"b8")
        self.b8.setFont(font)

        self.gridLayout.addWidget(self.b8, 4, 1, 1, 1)

        self.b5 = QPushButton(self.gridLayoutWidget)
        self.b5.setObjectName(u"b5")
        self.b5.setFont(font)

        self.gridLayout.addWidget(self.b5, 3, 1, 1, 1)

        self.b_asterisk = QPushButton(self.gridLayoutWidget)
        self.b_asterisk.setObjectName(u"b_asterisk")
        self.b_asterisk.setFont(font)

        self.gridLayout.addWidget(self.b_asterisk, 4, 3, 1, 1)

        self.b_dcos = QPushButton(self.gridLayoutWidget)
        self.b_dcos.setObjectName(u"b_dcos")
        self.b_dcos.setFont(font)

        self.gridLayout.addWidget(self.b_dcos, 6, 2, 1, 1)

        self.b_dtg = QPushButton(self.gridLayoutWidget)
        self.b_dtg.setObjectName(u"b_dtg")
        self.b_dtg.setFont(font)

        self.gridLayout.addWidget(self.b_dtg, 6, 3, 1, 1)

        self.b_dsin = QPushButton(self.gridLayoutWidget)
        self.b_dsin.setObjectName(u"b_dsin")
        self.b_dsin.setFont(font)

        self.gridLayout.addWidget(self.b_dsin, 6, 1, 1, 1)

        self.b_sin = QPushButton(self.gridLayoutWidget)
        self.b_sin.setObjectName(u"b_sin")
        self.b_sin.setFont(font)

        self.gridLayout.addWidget(self.b_sin, 2, 4, 1, 1)

        self.b6 = QPushButton(self.gridLayoutWidget)
        self.b6.setObjectName(u"b6")
        self.b6.setFont(font)

        self.gridLayout.addWidget(self.b6, 3, 2, 1, 1)

        self.b_c = QPushButton(self.gridLayoutWidget)
        self.b_c.setObjectName(u"b_c")
        self.b_c.setFont(font)

        self.gridLayout.addWidget(self.b_c, 6, 0, 1, 1)

        self.b7 = QPushButton(self.gridLayoutWidget)
        self.b7.setObjectName(u"b7")
        self.b7.setFont(font)

        self.gridLayout.addWidget(self.b7, 4, 0, 1, 1)

        self.b_cos = QPushButton(self.gridLayoutWidget)
        self.b_cos.setObjectName(u"b_cos")
        self.b_cos.setFont(font)

        self.gridLayout.addWidget(self.b_cos, 3, 4, 1, 1)

        self.b_minus = QPushButton(self.gridLayoutWidget)
        self.b_minus.setObjectName(u"b_minus")
        self.b_minus.setFont(font)

        self.gridLayout.addWidget(self.b_minus, 3, 3, 1, 1)

        self.b1 = QPushButton(self.gridLayoutWidget)
        self.b1.setObjectName(u"b1")
        self.b1.setFont(font)

        self.gridLayout.addWidget(self.b1, 2, 0, 1, 1)

        self.screen = QLineEdit(self.gridLayoutWidget)
        self.screen.setObjectName(u"screen")
        self.screen.setMinimumSize(QSize(766, 81))
        font1 = QFont()
        font1.setPointSize(48)
        self.screen.setFont(font1)
        self.screen.setLayoutDirection(Qt.RightToLeft)
        self.screen.setAlignment(Qt.AlignCenter)
        self.screen.setReadOnly(True)

        self.gridLayout.addWidget(self.screen, 0, 0, 1, 5)

        self.b_plus = QPushButton(self.gridLayoutWidget)
        self.b_plus.setObjectName(u"b_plus")
        self.b_plus.setFont(font)

        self.gridLayout.addWidget(self.b_plus, 2, 3, 1, 1)

        self.b3 = QPushButton(self.gridLayoutWidget)
        self.b3.setObjectName(u"b3")
        self.b3.setFont(font)

        self.gridLayout.addWidget(self.b3, 2, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.b_divide.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.b_dctg.setText(QCoreApplication.translate("MainWindow", u"Draw ctg", None))
        self.b_ctg.setText(QCoreApplication.translate("MainWindow", u"ctg", None))
        self.b_period.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b_tg.setText(QCoreApplication.translate("MainWindow", u"tg", None))
        self.b_equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b_asterisk.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.b_dcos.setText(QCoreApplication.translate("MainWindow", u"Draw cos", None))
        self.b_dtg.setText(QCoreApplication.translate("MainWindow", u"Draw tg", None))
        self.b_dsin.setText(QCoreApplication.translate("MainWindow", u"Draw sin", None))
        self.b_sin.setText(QCoreApplication.translate("MainWindow", u"sin", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.b_c.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b_cos.setText(QCoreApplication.translate("MainWindow", u"cos", None))
        self.b_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.screen.setText("")
        self.b_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
    # retranslateUi

