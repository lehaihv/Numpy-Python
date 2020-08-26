#!/usr/bin/python3

from urllib.request import urlopen
import json
import datetime 
from datetime import datetime
import time 

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

root = tk.Tk()
root.title('World Weather Forecast')
root.configure(background='lightblue')
root.iconbitmap('codemy.ico') #E:/
#image = PhotoImage(file="background.gif")
#background=Label(root, image=image)
#background.place(x=0,y=0,relwidth=1, relheight=1)


# centre the window
w = 480#root.winfo_reqwidth()
h = 320#root.winfo_reqheight()
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))
pad_default = 2
font_size = 20
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# this removes the maximize button
root.resizable(0,0)
#root.attributes('-toolwindow', True)
#root.wm_attributes('-transparentcolor', root['bg'])

canvas = tk.Canvas(root, height=320, width=480)
canvas.pack()
bg_img = tk.PhotoImage(file="wall1.gif")#file="C:/Users/bmg/Desktop/eh1.gif")
bg_label = canvas.create_image((0,0), image=bg_img, anchor=tk.N+tk.W)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%m/%d/%Y")


city = 0
cityname = "Hanoi"
timenow = ""
temp = 0
hum = 0
press = 0

#apikey="5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.
#lati="21.045021"#"52.194504"
#longi="105.800690"#"0.134708"

def get_weather():
	global city
	global cityname
	global timenow
	global temp
	global hum, press, epochtime, time11
	apikey = "5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
	# Latitude & longitude - current values are central Basingstoke.
	if city == 0: 
		lati = "21.045021"#"52.194504"
		longi = "105.800690"#"0.134708"
		cityname = "Hanoi"
		city = 1
	elif city == 1:
		lati = "51.508089"
		longi = "-0.076208"
		cityname = "London"
		city = 2
	elif city == 2:
		lati = "38.894893"
		longi = "-77.036552"
		cityname = "Washington DC"
		city = 3
	elif city == 3:
		lati = "55.750446"
		longi = "37.617494"
		cityname = "Moscow"
		city = 4    
	else:
		lati = "-37.721319"
		longi = "145.048809"
		cityname = "La Trobe Uni"
		city = 0    
	#if city==1:    
		#lati = "52.194504"
		#longi = "0.134708"
		#city = 0
	#city = city + 1
	#lati="21.045021"#"52.194504"
	#longi="105.800690"#"0.134708"
	city = 0
	# Add units=si to get it in sensible ISO units not stupid Fahreneheit.
	url="https://api.forecast.io/forecast/"+apikey+"/"+lati+","+longi+"?units=si"

	meteo=urlopen(url).read()
	meteo = meteo.decode('utf-8')
	weather = json.loads(meteo)
	
	temp = weather['currently']['temperature']
	hum = weather['currently']['humidity']*100
	press = weather['currently']['pressure']
	epochtime = weather['currently']['time']
	#print(weather['currently'])
	a = ' \u2103' # degree celsius sign
	canvas.itemconfig(label_place, text=cityname)
	canvas.itemconfig(label_temp, text=str(temp)+ a)
	canvas.itemconfig(label_hum, text=str(int(hum))+ " %")
	canvas.itemconfig(label_press, text=str(press)+ " mbar")

	root.after(3600000, get_weather)


def show_time():
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		canvas.itemconfig(label_time, text=current_time)
		root.after(1000, show_time)


def exit():
	root.quit()


label_place = canvas.create_text((240,40), text=cityname, font=("Arial Bold", 45), fill="#894949")
label_temp = canvas.create_text((240,180), text=temp, font=("Arial Bold", 65), fill="#1b92ed")#652828")
label_hum = canvas.create_text((100,100), text=hum, font=("Arial Bold", 30), fill="#0D3243")
label_press = canvas.create_text((350,100), text=press, font=("Arial Bold", 30), fill="#0D3243")

#label0_time = canvas.create_text((100,260), text="Time", font=("Arial Bold", 15), fill="#652828")
label_time = canvas.create_text((100,290), text=current_time, font=("Arial Bold", 30), fill="#2489B8")

#label0_date = canvas.create_text((350,260), text="Date", font=("Arial Bold", 15), fill="#652828")
label_date = canvas.create_text((350,290), text=current_date, font=("Arial Bold", 30), fill="#2489B8")

root.after(2000, get_weather)
root.after(1000, show_time)

root.mainloop()
