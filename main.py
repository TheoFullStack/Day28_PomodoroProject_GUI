from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 









# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Title and checkmark
label1= Label(text="Timer",font=(FONT_NAME,20,"bold"),fg=GREEN,bg=YELLOW)
label1.grid(column=1,row=0)

checkmark = Label(text="✔",fg=GREEN,bg=YELLOW,font=(FONT_NAME,10,"bold"))
checkmark.grid(column=1,row=3)

#button (Start) and (Reset)

button_start = Button(text="Start",width=5)
button_start.grid(column=0,row=2)
button_reset = Button(text="Reset",width=5)
button_reset.grid(column=2,row=2)



#Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)














window.mainloop()