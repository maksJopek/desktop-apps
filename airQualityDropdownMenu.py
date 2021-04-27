from tkinter import *
import requests
import json

root = Tk()
root.title("Air quality")

modes = [
    "Kraków, Aleja Krasińskiego",
    "Kraków, ul. Dietla",
    "Kraków, ul. Złoty Róg",
    "Kraków, ul. Bujaka",
]
sensor = StringVar()
sensor.set(modes[0])

appWidth = 861
appHeight = 500
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = (screenWidth / 2) - (appWidth / 2)
y = (screenHeight / 2) - (appHeight / 2)

root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

root.configure(background='black')

cityLabel = Label(root, background='black', font=('Helvetica', 20))
cityLabel.grid(column=0, row=0, columnspan=2, sticky=EW)
co2LabelName = Label(root, background='black', font=('Helvetica', 20))
co2LabelName.grid(column=0, row=2, sticky=NS)
co2LabelValue = Label(root, background='black', font=('Helvetica', 20))
co2LabelValue.grid(column=1, row=2, sticky=NS)
pm10LabelName = Label(root, background='black', font=('Helvetica', 20))
pm10LabelName.grid(column=0, row=3, sticky=NS)
pm10LabelValue = Label(root, background='black', font=('Helvetica', 20))
pm10LabelValue.grid(column=1, row=3, sticky=NS)
pm25LabelName = Label(root, background='black', font=('Helvetica', 20))
pm25LabelName.grid(column=0, row=4, sticky=NS)
pm25LabelValue = Label(root, background='black', font=('Helvetica', 20))
pm25LabelValue.grid(column=1, row=4, sticky=NS)


try:
    def showAll(empty=''):
        global cityLabel, co2LabelName, co2LabelValue, pm10LabelName, pm10LabelValue, pm25LabelName, pm25LabelValue

        apiRequestsCity = requests.get(
            "http://api.gios.gov.pl/pjp-api/rest/station/findAll")
        apiCity = json.loads(apiRequestsCity.content)

        ida = None
        for c in apiCity:
            if c['stationName'] == sensor.get():
                ida = c['id']

        co2 = "tlenek węgla"
        pm10 = "pył zawieszony PM10"
        pm25 = "pył zawieszony PM2.5"

        apiValue = requests.get(
            f"http://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/{ida}")
        apiValue = json.loads(apiValue.content)
        co2Value = "brak danych"
        pm10Value = "brak danych"
        pm25Value = "brak danych"

        for key in apiValue:
            # apiValue[key] is not None:
            if key == "coIndexLevel" and apiValue[key]:
                co2Value = apiValue[key]['indexLevelName']
            # apiValue[key] is not None:
            elif key == "pm10IndexLevel" and apiValue[key]:
                pm10Value = apiValue[key]['indexLevelName']
            # apiValue[key] is not None:
            elif key == "pm25IndexLevel" and apiValue[key]:
                pm25Value = apiValue[key]['indexLevelName']

        cityLabel['text'] = sensor.get()

        if co2Value == 'Bardzo dobry':
            color = 'green'
        elif co2Value == 'Dobry':
            color = 'orange'
        elif co2Value == 'Umiarkowany':
            color = 'red'
        else:
            color = 'white'

        co2LabelName['text'] = co2
        co2LabelValue['text'] = co2Value
        co2LabelValue['fg'] = color

        if pm10Value == 'Bardzo dobry':
            color = 'green'
        elif pm10Value == 'Dobry':
            color = 'orange'
        elif pm10Value == 'Umiarkowany':
            color = 'red'
        else:
            color = 'white'

        pm10LabelName['text'] = pm10
        pm10LabelValue['text'] = pm10Value
        pm10LabelValue['fg'] = color

        if pm25Value == 'Bardzo dobry':
            color = 'green'
        elif pm25Value == 'Dobry':
            color = 'orange'
        elif pm25Value == 'Umiarkowany':
            color = 'red'
        else:
            color = 'white'

        pm25LabelName['text'] = pm25
        pm25LabelValue['text'] = pm25Value
        pm25LabelValue['fg'] = color

    changeCityLabel = OptionMenu(root, sensor, *modes, command=showAll)
    changeCityLabel.grid(column=0, row=1, columnspan=2, sticky=EW)
    showAll()
except Exception as apiError:
    print(apiError)
    newWindow = Toplevel(root)
    newWindow.title("ERROR!")
    appWidth = 770
    appHeight = 300
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    x = (screenWidth / 2) - (appWidth / 2)
    y = (screenHeight / 2) - (appHeight / 2)
    newWindow.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')
    newWindow.configure(background='black')
    error = Label(newWindow, text="ERROR", background='black',
                  fg='white', font=('Helvetica', 20))
    error.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=NS)

root.mainloop()
