import tkinter
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    # work_sec = 10
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps%8==0:
        count_down(long_break_sec)
        title_label.config(text="Break",fg=RED)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    if count_min <10:
        count_min=f"0{count_min}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for i in range(reps//2):
            mark+="✔️"
        check_marks.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(pady=50,padx=100,bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
title_label.grid(column=1,row=0)

canvas = Canvas(width=205,height=225,bg=YELLOW,highlightthickness=0)
tom_img = PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=tom_img)
timer_text = canvas.create_text(103,131,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# canvas.pack()
start_btn = Button(text="Start",highlightthickness=0,command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_btn.grid(column=2,row=2)

check_marks = Label(fg=GREEN,bg=YELLOW)
check_marks.grid(row=3,column=1)

window.mainloop()