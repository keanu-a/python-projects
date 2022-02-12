# Keanu Aloua
# December 27, 2021
# Pomodoro Timer Project

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
    global reps
    global timer

    window.after_cancel(timer)
    timer_title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_title.config(text="Work", fg=GREEN)
        count_down(work_seconds)
    elif reps == 8:
        timer_title.config(text="Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 1:
        timer_title.config(text="Break", fg=PINK)
        count_down(short_break)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:  # Dynamic Typing
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # 1000 ms == 1 second
    else:
        start_timer()
        mark = ""
        sessions = math.floor(reps/2)
        for r in range(sessions):
            mark += "✓"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()  # Creating a pop up window for the program
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_title.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")  # First we need to make the image into a variable
canvas.create_image(100, 112, image=tomato)  # The canvas will display the image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "normal"))
checkmark.grid(row=3, column=1)

window.mainloop()
