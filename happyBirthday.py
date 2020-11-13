import tkinter as tk
from pygame import mixer, time
from PIL import ImageTk, Image
from datetime import date
import imageio
from pathlib import Path
import time as tkm
from unittest import result

video_name = str(Path().absolute()) + '\\video.mp4'
video = imageio.get_reader(video_name)
delay = int(1000 / video.get_meta_data()['fps'])
def stream(label):

    try:
        image = video.get_next_data()
    except:
        video.close()
        return
    label.after(delay, lambda: stream(label))
    frame_image = ImageTk.PhotoImage(Image.fromarray(image))
    label.config(image=frame_image)
    label.image = frame_image

def CheckAge():

    rezultati=tk.Label(root, text="Your results are here below", font=('Verdana', 9,'bold','underline'))    #oboj gi bukvite
    rezultati.grid(row=0, column=5)

    global result # to return calculation
    result = str(bdayentry.get())
    imee = str(usentry.get())

    today = date.today()
    #Convert user input into a date
    dob_data = result.split("/")

    dobDay = int(dob_data[0])
    dobMonth = int(dob_data[1])
    dobYear = int(dob_data[2])
    dob = date(dobYear,dobMonth,dobDay)

    #Calculate number of days lived
    numberOfDays = (today - dob).days 

    #Convert this into whole years to display the age
    age = numberOfDays // 365

    label=tk.Label(root, text=str(imee)+", You are "+str(age) +" years old")
    label.grid(row=1, column=5)

    day = dob.strftime("%A")
    l1=tk.Label(root, text = "You were born on a " + day)
    l1.grid(row=2, column=5)

    l2=tk.Label(root, text="You have spent "+str(numberOfDays)+" days on Earth")
    l2.grid(row=3, column=5)

    thisYear=today.year

    nextBirthday = date(thisYear,dobMonth,dobDay)
    if today<nextBirthday:
        gap = (nextBirthday - today).days
        l3=tk.Label(root, text="Your birthday is in "+str(gap)+" days")
        l3.grid(row=4, column=5)
    elif  today == nextBirthday:
        l4=tk.Label(root, text=" Today is your birthday! Happy Birthday!")
        l4.grid(row=4, column=5)
    else:
        nextBirthday = date(thisYear+1,dobMonth,dobDay)
        gap = (nextBirthday - today).days
        l5=tk.Label(root, text="Your birthday is in "+str(gap)+" days")
        l5.grid(row=4, column=5)

    #if __name__ == '__main__':
    if (imee == "Zoran" or imee == "zoran" or imee == "Zoki" or imee == "zoki") and today == nextBirthday:
        my_label = tk.Label(root, width=490, heigh=280)
        my_label.grid(row=5, column=0, columnspan=6)
        my_label.after(delay, lambda: stream(my_label))
        #mixer.music.load('Zoran.wav')
        #mixer.music.play()
        #while mixer.music.get_busy(): time.Clock().tick(10)
root = tk.Tk()
root.title("Birthday_Card")
#root.geometry("490x425+800+100")

label1=tk.Label(root, text="Start Birthday Song: ", fg='green', anchor="w")
label1.grid(row=0, column=0)

file = 'HBD.wav'
mixer.init()
mixer.music.load(file)

play = lambda: mixer.music.play()
button1 = tk.Button(root, text = 'Play', command = play)
while mixer.music.get_busy(): time.Clock().tick(10)
button1.grid(row=0, column=1)

pause = lambda: mixer.music.pause()
button2 = tk.Button(root, text="Pause", command = pause)
button2.grid(row=0, column=2)

resume = lambda: mixer.music.unpause()
button3 = tk.Button(root, text="Resume", command = resume)
button3.grid(row=0, column=3)

stop = lambda: mixer.music.stop()
button4 = tk.Button(root, text="Stop", command=stop)
button4.grid(row=0, column=4)

username = tk.Label(root, text="Your name: ")
username.grid(row=1, column=0, sticky='W')

bday = tk.Label(root, text="B-day date: ")
bday.grid(row=2, column=0, sticky='W')

usentry = tk.Entry(root, width=15)
usentry.grid(row=1, columnspan=4)

bdayentry = tk.Entry(root, width=15)
bdayentry.grid(row=2, columnspan=4)

format=tk.Label(root, text="dd/mm/yyyy")
format.grid(row=3, column=0, sticky='W')

prazno = tk.Label(root, text="Click here to check-->")
prazno.grid(row=4, columnspan=3)

img = ImageTk.PhotoImage(Image.open("teest.jpg"))

button=tk.Button(root, text="Calculate", image=img, command=CheckAge)
button.grid(row=1, columnspan=5, rowspan=4, sticky='E')

root.mainloop()

