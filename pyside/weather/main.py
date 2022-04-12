#!/usr/bin/env python
import sys
from datetime import datetime
from PySide6.QtGui import QAction 
from PySide6.QtWidgets import QApplication, QDateTimeEdit, QLayout, QLineEdit, QMainWindow, QScrollArea, QSizePolicy, QStatusBar, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QCheckBox, QFormLayout, QGroupBox, QToolBar, QMenu
from PySide6.QtCore import QDate, QSize, Qt, QDateTime
import requests
import qtawesome as qta

def API_URL(x):
    return f"https://api.openweathermap.org/data/2.5/weather?q={x}&appid=d7eea7960e9b5024b8441fb6f9344ce4&units=metric"

def create_title():
    lh = QLabel("QWeather App")
    lhf = lh.font()
    lhf.setPointSize(50)
    lhf.setBold(True)
    lh.setFont(lhf)
    return lh

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Weather app")

        widget = QWidget()
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        main_layout = QFormLayout()
        main_layout.setSizeConstraint(QLayout.SetMinimumSize)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(40)

        self.main_layout = main_layout
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.refresh("Wieliczka")

    def refresh(self, city):
        def clearLayout(layout):
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    clearLayout(child.layout())
        clearLayout(self.main_layout)
        self.main_layout.addWidget(create_title())
        self.city = city
        # self.data = {'main': {'temp': 1.15, 'pressure': 1031}, 'wind': {'speed': 5.66}, 'clouds': {'all': 40}, 'rain': {'1h': 11}}
        self.data = requests.get(API_URL(self.city)).json()

        temp = self.data["main"]["temp"]
        humidity = self.data["main"]["pressure"]
        clouds = self.data["clouds"]["all"]
        wind = self.data["wind"]["speed"]
        rain = self.data.get("rain")
        rain = 0 if rain is None else rain["1h"]

        it = qta.IconWidget()
        it.setIconSize(QSize(40, 40))
        if temp > 15:
            it.setIcon(qta.icon('mdi6.fire', color="red"))
        else:
            it.setIcon(qta.icon('mdi6.snowflake', color="blue"))

        ih = qta.IconWidget()
        ih.setIconSize(QSize(40, 40))
        if humidity > 1000:
            ih.setIcon(qta.icon('fa5s.compress-alt', color="green"))
        else:
            ih.setIcon(qta.icon('fa5s.compress-arrows-alt', color="orange"))

        ic = qta.IconWidget()
        ic.setIconSize(QSize(40, 40))
        if clouds > 75:
            ic.setIcon(qta.icon('mdi6.cloud', color="blue"))
        elif clouds > 37:
            ic.setIcon(qta.icon('mdi6.weather-sunny-off', color="darkorange"))
        else:
            ic.setIcon(qta.icon('mdi6.weather-sunny', color="yellow"))

        iw = qta.IconWidget()
        iw.setIconSize(QSize(40, 40))
        if wind > 15:
            iw.setIcon(qta.icon('mdi6.windsock', color="darkgrey"))
        else:
            iw.setIcon(qta.icon('mdi6.weather-windy', color="gray"))

        ir = qta.IconWidget()
        ir.setIconSize(QSize(40, 40))
        if rain == 0:
            ir.setIcon(qta.icon('ri.emotion-happy-fill', color="green"))
        elif rain > 10:
            ir.setIcon(qta.icon('mdi6.weather-pouring', color="darkblue"))
        else:
            ir.setIcon(qta.icon('mdi6.weather-rainy', color="blue"))

        icons = [it, ih, ic, iw, ir]

        temp = str(temp) + "°C"
        humidity = str(humidity) + "hPa"
        clouds = str(clouds) + "%"
        wind = str(wind) + "m/s"
        rain = str(rain) + "mm"
        data = {
            "temp": temp,
            "humidity": humidity,
            "clouds": clouds,
            "wind": wind,
            "rain": rain
        }

        lh = QLabel(self.city)
        lhf = lh.font()
        lhf.setPointSize(30)
        lhf.setBold(True)
        lh.setFont(lhf)
        self.main_layout.addRow(lh)
        for i, (key, value) in enumerate(data.items()):
            k = QLabel(f"{key.title()}: {value}")
            lhf = k.font()
            lhf.setPointSize(20)
            k.setFont(lhf)

            self.main_layout.addRow(icons[i], k)
        l = QLabel("To change city press anywhere with right mouse button")
        lf = l.font()
        lf.setPointSize(25)
        l.setFont(lf)
        self.main_layout.addRow(l)

    def contextMenuEvent(self, e):
        context = QMenu(self)

        qk = QAction("Zakopane", self)
        qk.triggered.connect(lambda: self.refresh("Zakopane")) #type: ignore
        context.addAction(qk)

        qk = QAction("Gniezno", self)
        qk.triggered.connect(lambda: self.refresh("Gniezno")) #type: ignore
        context.addAction(qk)

        qk = QAction("Gdynia", self)
        qk.triggered.connect(lambda: self.refresh("Gdynia")) #type: ignore
        context.addAction(qk)

        qk = QAction("Warszawa", self)
        qk.triggered.connect(lambda: self.refresh("Warszawa")) #type: ignore
        context.addAction(qk)

        qk = QAction("Wieliczka", self)
        qk.triggered.connect(lambda: self.refresh("Wieliczka")) #type: ignore
        context.addAction(qk)
        
        context.exec(e.globalPos())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    app.exec()
