import time
import datetime
import winsound
from threading import Thread
from tkinter import Tk, Label, Frame, StringVar, OptionMenu, Button, LEFT

root = Tk()
root.geometry("400x200")
root.title("Python Alarm")

def threading():
    t1 = Thread(target=alarm)
    t1.start()
    t1.joim()
    
    
def alarm():
    while True:
        set_alarm_time = f"{hour.get(),minute.get(),second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        
        if current_time == set_alarm_time:
            print("Bangun WOI UDAH BEDUG")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        

Label(root, text="Python Alarm", font="Arial 20 bold", fg="red").pack(pady=10)
Label(root, text="Atur Waktu", font="Arial 15 bold").pack()


frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = tuple(f"{i:02}" for i in range(24))
hour.set(hours[0])
h = OptionMenu(frame, hour, *hours)
h.pack(side=LEFT)

minute = StringVar(root)
minutes = tuple(f"{i:02}" for i in range(60))
minute.set(minutes[0])
m = OptionMenu(frame, minute, *minutes)
m.pack(side=LEFT)

second = StringVar(root)
seconds = tuple(f"{i:02}" for i in range(60))
second.set(seconds[0])
s = OptionMenu(frame, second, *seconds)
s.pack(side=LEFT)

Button(root, text="Atur Alarm", font="Arial 15", command=threading).pack(pady=20)
root.mainloop()