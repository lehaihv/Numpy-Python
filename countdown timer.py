import datetime
import tkinter as tk


def round_time(dt, round_to):
    seconds = (dt - dt.min).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)


def ct(label):
    def count():
        now = round_time(datetime.datetime.now(), round_to=1)
        eh = datetime.datetime(2019, 3, 31, 20, 30)
        tte = eh - now
        label.config(text=str(tte))
        label.after(50, count)

    count()


root = tk.Tk()
root.title("Earth Hour Countdown!")
now = round_time(datetime.datetime.now(), round_to=1)
eh = datetime.datetime(2019, 3, 31, 20, 30)
tte = eh - now
frame = tk.Frame(root, bg="#486068")
frame.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, height=200, width=500)
canvas.place(relwidth=1, relheight=1)

bg_img = tk.PhotoImage(file="background.gif")#file="C:/Users/bmg/Desktop/eh1.gif")
bg_label = tk.Label(canvas, image=bg_img)
bg_label.place(relwidth=1, relheight=1)

label_msg = tk.Label(root, text="Earth Hour Countdown:", font="MSGothic 50 bold", bg="black", fg="#652828", bd=1)
label_msg.place(relx=0.035, rely=0.1)

label_cd = tk.Label(root, text=str(tte), font="MSGothic 50 bold", bg="black", fg="#652828", bd=1)
label_cd.place(relx=0.590, rely=0.1)

ehtime_label = tk.Label(root, text=("Earth Hour:" + eh.strftime("%d-%m-%Y %H:%M:%S")), font="MSGothic 50 bold", bg="black", fg="#652828", bd=1)
ehtime_label.place(relx=0.13, rely=0.3)

ct(label_cd)

root.mainloop()