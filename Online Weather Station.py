#!/usr/bin/python3

from urllib.request import urlopen
import json
import datetime 
import time 

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('World Weather Forecast')
root.configure(background='lightblue')
root.iconbitmap('codemy.ico') #E:/
image = PhotoImage(file="background.gif")
background=Label(root, image=image)
background.place(x=0,y=0,relwidth=1, relheight=1)

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
#root.wm_attributes('-transparentcolor', root['bg'])

timenow = StringVar()
timenow.set(time.strftime("%H:%M:%S"))

datenow = StringVar()
datenow.set(time.strftime("%m/%d/%Y"))

location = StringVar()
location_date = StringVar()
location_temp = StringVar()
location_hum = StringVar()
location_press = StringVar()
city = 0
#cityname = ""
time0_label = Label(root, text="Time", background='lightblue', fg="red", borderwidth=5, font=("Arial Bold", 15))
time0_label.grid(row = 5, column = 0, columnspan=2, padx=5, pady = 5)
time_label = Label(root, textvariable=timenow, background='lightblue', borderwidth=5, font=("Arial Bold", 25))
time_label.grid(row = 6, column = 0, columnspan=2, padx=5, pady = 5)
date0_label = Label(root, text="Date", background='lightblue', borderwidth=5, font=("Arial Bold", 15))
date0_label.grid(row = 5, column = 2, columnspan=2, padx=5, pady = 5)
date_label = Label(root, textvariable=datenow, background='lightblue', borderwidth=5, font=("Arial Bold", 25))
date_label.grid(row = 6, column = 2, columnspan=2, padx=5, pady = 5)
#apikey="5d9cb52a19b8b5f9e31edef7b882e8b6" # get a key from https://developer.forecast.io/register
# Latitude & longitude - current values are central Basingstoke.
#lati="21.045021"#"52.194504"
#longi="105.800690"#"0.134708"
def get_weather():
	global city
	global cityname
	global timenow
	global temp
	global hum, press, epochtime
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
	#time = datetime.datetime.utcfromtimestamp(epochtime).replace(tzinfo=datetime.timezone.utc)
	#timenow = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(epochtime)) #Replace time.localtime with time.gmtime for GMT time "%a, %d %b %Y %H:%M:%S +0000".	
	location.set(cityname)
	#location_date.set(timenow)
	location_temp.set(str(temp)+ a)
	location_hum.set(str(int(hum))+ " %")
	location_press.set(str(press)+ " mbar")
	root.after(20000, get_weather)

e = Entry(root, width=80, background='lightblue', borderwidth=0)
e.grid(row=0, column=0, columnspan=4, padx=1, pady=1)
place_label = Label(root, textvariable=location, background='lightblue', fg="red", borderwidth=5, font=("Arial Bold", 25))
place_label.grid(row = 1, column = 0, columnspan=4, rowspan=1, padx=1, pady = 1)
#date_label = Label(root, textvariable=location_date, background='lightblue', borderwidth=5, font=("Arial Bold", 20))
#date_label.grid(row = 5, column = 0, columnspan=3, padx=5, pady = 5)
temp_label = Label(root, textvariable=location_temp, background='lightblue', borderwidth=5, font=("Arial Bold", 45))
temp_label.grid(row = 2, column = 0, columnspan=4, rowspan=2, padx=1, pady = 1)

hum0_label = Label(root, text="Humidity", background='lightblue', borderwidth=5, font=("Arial Bold", 15))
hum0_label.grid(row = 4, column = 0, columnspan=1, padx=5, pady = 5)
hum_label = Label(root, textvariable=location_hum, background='lightblue', borderwidth=5, font=("Arial Bold", 15))
hum_label.grid(row = 4, column = 1, columnspan=1, padx=5, pady = 5)
press0_label = Label(root, text="Pressure", background='lightblue', borderwidth=5, font=("Arial Bold", 15))
press0_label.grid(row = 4, column = 2, columnspan=1, padx=5, pady = 5)
press_label = Label(root, textvariable=location_press, background='lightblue', borderwidth=5, font=("Arial Bold", 15))
press_label.grid(row = 4, column = 3, columnspan=1, padx=5, pady = 5)

def show_time():
		timenow.set(time.strftime("%H:%M:%S"))
		root.after(1000, show_time)

def exit():
	root.quit()

#root.after(20000, get_weather)
#root.after(1000, show_time)

root.mainloop()
