from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import requests
from dateutil import parser
import datetime
import math
import json

API = "b744285416bdf9133f32148bb25a0edf"

Town = input('Enter your town/villege name : ').title()
State = input('Enter your state code : ').upper()

current_url = "http://api.openweathermap.org/data/2.5/weather?" + 'appid=' + API + '&q=' + Town
live_response = requests.get(current_url)
live_data = live_response.json()

forecast_url = 'https://api.openweathermap.org/data/2.5/forecast?' + 'appid=' + API + '&q=' + Town
forecast_response = requests.get(forecast_url)
forecast_response.raise_for_status()

forecast_data = forecast_response.json()['list']

################################################ Weather forecast_data ############################################

day_list = []

for i in range(0, len(forecast_data)):
    data = {
        "Temp" : math.ceil(forecast_data[i]['main']['temp'] - 273.15),
        "Feels_like" : math.ceil(forecast_data[i]['main']['feels_like'] - 273.15),
        "Pressure" : forecast_data[i]['main']['pressure'],
        "Humidity" : forecast_data[i]['main']['humidity'],
        "Weather_description" : forecast_data[i]['weather'][0]['description'],
        "Wind_speed" : math.ceil(forecast_data[i]['wind']['speed'] / 1000),
        "Visibility" : math.ceil(forecast_data[i]['visibility'] / 1000),
        "date" : forecast_data[i]['dt_txt']
    }     
    day_list.append(data)  

date2 = parser.parse(day_list[-29]['date'])
date3 = parser.parse(day_list[-21]['date'])
date4 = parser.parse(day_list[-13]['date'])
date5 = parser.parse(day_list[-5]['date'])

day2 = []
day3 = []
day4 = []
day5 = []
for i in range(0, len(day_list)):
    if (parser.parse(day_list[i]['date']).date() == date2.date()):
        day2.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date3.date()):
        day3.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date4.date()):
        day4.append(day_list[i])
    if (parser.parse(day_list[i]['date']).date() == date5.date()):
        day5.append(day_list[i])                 

first_time = '09:00:00'
first_time = (datetime.datetime.strptime(first_time, '%H:%M:%S')).time()
second_time = '15:00:00'
second_time = (datetime.datetime.strptime(second_time, '%H:%M:%S')).time()
third_time = '21:00:00'
third_time = (datetime.datetime.strptime(third_time, '%H:%M:%S')).time()

# ################################################# weather UI ###############################################

window = Tk()
canvas = Canvas(window, width=900, height=600)
def animate(counter):
    canvas.itemconfig(image, image = sequence[counter])
    window.after(33, lambda: animate((counter+1) % len(sequence)))

if (live_data['weather'][0]['description'] == 'clear sky'):
    sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('sky.gif'))]
    image = canvas.create_image(450, 300, image = sequence[0])
    animate(1)
    canvas.create_text(330, 100, text='🔆', fill='#182747', font=('times', 50, 'bold'))
    canvas.create_text(480, 40, text=f"{Town}, {State}", fill='#182747', font=('times', 36, 'normal'))
    canvas.create_text(470, 100, text=f"{math.ceil(live_data['main']['temp'] - 273.15)}°C", font=('times', 50, 'bold'), fill='#182747')
    canvas.create_text(600, 100, text='Today', fill='black', font=('jetbrains mono', 15, 'normal'))
    canvas.create_text(450, 160, text=f"Feel like:{math.ceil(live_data['main']['feels_like'] - 273.15)}°C  |  Pressure:{live_data['main']['pressure']} hPa  |  Humidity:{live_data['main']['humidity']}%", fill = '#182747',font = ('jetbrains mono', 15, 'normal'))
    canvas.create_text(460, 190, text=f"Wind speed:{math.ceil(live_data['wind']['speed'] / 1000)}km/s  |  Visibility:{math.ceil(live_data['visibility'] / 1000)}km", fill = '#182747', font = ('jetbrains mono', 15,'normal'))
elif ((live_data['weather'][0]['description'] == 'scattered clouds') or (live_data['weather'][0]['description'] == 'few clouds') or (live_data['weather'][0]['description'] == 'broken clouds')): 
    sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('cloudy.gif'))]
    image = canvas.create_image(450, 300, image = sequence[0])
    animate(1)
    canvas.create_text(330, 100, text='⛅', fill='#182747', font=('times', 50, 'bold'))
    canvas.create_text(480, 40, text=f"{Town}, {State}", fill='#182747', font=('times', 36, 'normal'))
    canvas.create_text(470, 100, text=f"{math.ceil(live_data['main']['temp'] - 273.15)}°C", font=('times', 50, 'bold'), fill='#182747')
    canvas.create_text(600, 100, text='Today', fill='black', font=('jetbrains mono', 15, 'normal'))
    canvas.create_text(450, 160, text=f"Feel like:{math.ceil(live_data['main']['feels_like'] - 273.15)}°C  |  Pressure:{live_data['main']['pressure']} hPa  |  Humidity:{live_data['main']['humidity']}%", fill = '#182747',font = ('jetbrains mono', 15, 'normal'))
    canvas.create_text(460, 190, text=f"Wind speed:{math.ceil(live_data['wind']['speed'] / 1000)}km/s  |  Visibility:{math.ceil(live_data['visibility'] / 1000)}km", fill = '#182747', font = ('jetbrains mono', 15,'normal'))
else:
    sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('rain.gif'))]
    image = canvas.create_image(450, 300, image = sequence[0])
    animate(1)
    canvas.create_text(330, 100, text='⛈️', fill='#182747', font=('times', 50, 'bold'))
    canvas.create_text(480, 40, text=f"{Town}, {State}", fill='#182747', font=('times', 36, 'normal'))
    canvas.create_text(470, 100, text=f"{math.ceil(live_data['main']['temp'] - 273.15)}°C", font=('times', 50, 'bold'), fill='#182747')
    canvas.create_text(600, 100, text='Today', fill='black', font=('jetbrains mono', 15, 'normal'))
    canvas.create_text(450, 160, text=f"Feel like:{math.ceil(live_data['main']['feels_like'] - 273.15)}°C  |  Pressure:{live_data['main']['pressure']} hPa  |  Humidity:{live_data['main']['humidity']}%", fill = '#182747',font = ('jetbrains mono', 15, 'normal'))
    canvas.create_text(460, 190, text=f"Wind speed:{math.ceil(live_data['wind']['speed'] / 1000)}km/s  |  Visibility:{math.ceil(live_data['visibility'] / 1000)}km", fill = '#182747', font = ('jetbrains mono', 15,'normal'))   

for i in range(0, len(day2)):
    if (parser.parse(day2[i]['date']).time() == first_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(110, 360, text=f"{parser.parse(day2[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(110, 400, text='🔆', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(110, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds') or (day2[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(110, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(110, 400, text='⛅', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(110, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(110, 360, text=f"{parser.parse(day2[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(110, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(110, 435, text=f"9AM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day2[i]['date']).time() == second_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(110, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds') or (day2[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(110, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(110, 455, text=f"3PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day2[i]['date']).time() == third_time):
        if(day2[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(110, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day2[i]['Weather_description'] == 'scattered clouds') or (day2[i]['Weather_description'] == 'few clouds') or (day2[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(110, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(110, 475, text=f"9PM : {day2[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day3)):
    if (parser.parse(day3[i]['date']).time() == first_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(330, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(330, 400, text='🔆', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(330, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds') or (day3[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(330, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(330, 400, text='⛅', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(330, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(330, 360, text=f"{parser.parse(day3[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(330, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(330, 435, text=f"9AM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day3[i]['date']).time() == second_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(330, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds') or (day3[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(330, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(330, 455, text=f"3PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day3[i]['date']).time() == third_time):
        if(day3[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(330, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day3[i]['Weather_description'] == 'scattered clouds') or (day3[i]['Weather_description'] == 'few clouds') or (day3[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(330, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(330, 475, text=f"9PM : {day3[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day4)):
    if (parser.parse(day4[i]['date']).time() == first_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(560, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(560, 400, text='🔆', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(560, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds') or (day4[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(560, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(560, 400, text='⛅', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(560, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(560, 360, text=f"{parser.parse(day4[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(560, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(560, 435, text=f"9AM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day4[i]['date']).time() == second_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(560, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds') or (day4[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(560, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(560, 455, text=f"3PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day4[i]['date']).time() == third_time):
        if(day4[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(560, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day4[i]['Weather_description'] == 'scattered clouds') or (day4[i]['Weather_description'] == 'few clouds') or (day4[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(560, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(560, 475, text=f"9PM : {day4[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))

for i in range(0, len(day5)):
    if (parser.parse(day5[i]['date']).time() == first_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(780, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(780, 400, text='🔆', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(780, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds') or (day5[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(780, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='black', font=('cascedia code', 10, 'normal'))
            canvas.create_text(780, 400, text='⛅', fill='black', font=('times', 30, 'normal'))
            canvas.create_text(780, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(780, 360, text=f"{parser.parse(day5[i]['date']).date()}", fill='white', font=('cascedia code', 10, 'normal'))
            canvas.create_text(780, 400, text='⛈️', fill='white', font=('times', 30, 'normal'))
            canvas.create_text(780, 435, text=f"9AM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day5[i]['date']).time() == second_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(780, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds') or (day5[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(780, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(780, 455, text=f"3PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
    if (parser.parse(day5[i]['date']).time() == third_time):
        if(day5[i]['Weather_description'] == 'clear sky'):
            canvas.create_text(780, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        elif ((day5[i]['Weather_description'] == 'scattered clouds') or (day5[i]['Weather_description'] == 'few clouds') or (day5[i]['Weather_description'] == 'broken clouds')):
            canvas.create_text(780, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='black', font=('Jetbrains mono', 10, 'normal'))
        else:
            canvas.create_text(780, 475, text=f"9PM : {day5[i]['Temp']}°C", fill='white', font=('Jetbrains mono', 10, 'normal'))
                
canvas.pack()

window.mainloop()