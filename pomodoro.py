from tkinter import *
import tkinter as tk
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 25 minutes
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("s")
window.geometry("400x600")
canvas = Canvas(width = 400, height= 500,bg = YELLOW, highlightthickness=0) # panel called canvas where image or text can be positioned
window.config(padx=75, pady=75 ,bg = YELLOW)

img = PhotoImage(file  = "C:\\Users\\Owner\\Downloads\\pomodoro-start\\tomato.png")
tomato = canvas.create_image(125,200,image = img) # adds image to the canvas panel
text = canvas.create_text(127,210, text = '25:00',fill = "white", font = (FONT_NAME, 35,"bold")) # initializes text on screen

import math

def method(count):# method to change time
    min = math.floor(count/60)
    seconds = count%60
    canvas.itemconfig(text, text = f"{min}:{seconds}")# the text on screen changes to count value
    if seconds < 10:

        seconds = f"0{seconds}"

    if count >= 0:
        window.after(1000,method,count-1) # after one second the count valuue decreases

def start_timer():
    method(WORK_MIN*60)


canvas.pack()

button = Button(text = "start", width = 10, command = start_timer) # start button
button2 = Button(text = "restart", width = 10, command = start_timer) # reset button
#label.pack()
button.place(x=0,y= 325) # SETS POSITON OF BUTTONS
button2.place(x=165,y= 325)# you dont need to pack if you use the place method




window.mainloop()

