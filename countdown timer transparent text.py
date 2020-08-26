import datetime
import tkinter as tk


def round_time(dt, round_to):
    seconds = (dt - dt.min).seconds
    rounding = (seconds + round_to / 2) // round_to * round_to
    return dt + datetime.timedelta(0, rounding - seconds, -dt.microsecond)


def ct():
    def count():
        now = round_time(datetime.datetime.now(), round_to=1)
        eh = datetime.datetime(2019, 3, 31, 20, 30)
        tte = eh - now
        canvas.itemconfig(label_cd, text=str(tte))
        root.after(50, count)

    count()


root = tk.Tk()
root.title("Earth Hour Countdown!")
now = round_time(datetime.datetime.now(), round_to=1)
eh = datetime.datetime(2019, 3, 31, 20, 30)
tte = eh - now

canvas = tk.Canvas(root, height=360, width=1333)
canvas.pack()

bg_img = tk.PhotoImage(file="background.gif")#file="C:/Users/bmg/Desktop/eh1.gif")
bg_label = canvas.create_image((0,0), image=bg_img, anchor=tk.N+tk.W)

label_msg = canvas.create_text((410, 120), text="Earth Hour Countdown:", font="MSGothic 50 bold", fill="#652828")

label_cd = canvas.create_text((1030,120), text=str(tte), font="MSGothic 50 bold", fill="#652828")

ehtime_label = canvas.create_text((650,240), text=("Earth Hour:" + eh.strftime("%d-%m-%Y %H:%M:%S")), font="MSGothic 50 bold", fill="#652828")

ct()

root.mainloop()