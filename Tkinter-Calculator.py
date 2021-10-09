import tkinter
from tkinter import *

val = ""
operator = ""


# When one is clicked
def btn_one_clicked():
    global val
    val = val + "1"
    data.set(val)


# When two is clicked
def btn_two_clicked():
    global val
    val = val + "2"
    data.set(val)


# When three is clicked
def btn_three_clicked():
    global val
    val = val + "3"
    data.set(val)


# When four is clicked
def btn_four_clicked():
    global val
    val = val + "4"
    data.set(val)


# When five is clicked
def btn_five_clicked():
    global val
    val = val + "5"
    data.set(val)


# When six is clicked
def btn_six_clicked():
    global val
    val = val + "6"
    data.set(val)


# When seven is clicked
def btn_seven_clicked():
    global val
    val = val + "7"
    data.set(val)


# When eight is clicked
def btn_eight_clicked():
    global val
    val = val + "8"
    data.set(val)


# When nine is clicked
def btn_nine_clicked():
    global val
    val = val + "9"
    data.set(val)


# When zero is clicked
def btn_zero_clicked():
    global val
    val = val + "0"
    data.set(val)


# When plus is clicked
def btn_plus_clicked():
    global operator
    global val
    operator = "+"
    val = val + "+"
    data.set(val)


# When minus is clicked
def btn_minus_clicked():
    global operator
    global val
    operator = "-"
    val = val + "-"
    data.set(val)


# When star is clicked
def btn_mult_clicked():
    global operator
    global val
    operator = "*"
    val = val + "*"
    data.set(val)


# When divide is clicked
def btn_divide_clicked():
    global operator
    global val
    operator = "/"
    val = val + "/"
    data.set(val)


# When C is pressed
def btn_C_pressed():
    global operator
    global val
    val = ""
    operator = "C"
    data.set(val)


# When C is pressed
def result():
    global operator
    global val
    operator = "="
    answer = eval(val)
    data.set(answer)
    val = str(val)


# Initialize the calculator
root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")


# Label
data = StringVar()
lbl = Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana", 22),
    textvariable=data,
    background="#ffffff",
    fg="#000000"
)
lbl.pack(expand=True, fill="both")


# Frames
btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")


# Button row first
btn1 = Button(
    btnrow1,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_one_clicked,
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_two_clicked,
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_three_clicked,
)
btn3.pack(side=LEFT, expand=True, fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_plus_clicked,
)
btnplus.pack(side=LEFT, expand=True, fill="both")


# Button row second
btn4 = Button(
    btnrow2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_four_clicked,
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_five_clicked,
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_six_clicked,
)
btn6.pack(side=LEFT, expand=True, fill="both")

btnminus = Button(
    btnrow2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_minus_clicked,
)
btnminus.pack(side=LEFT, expand=True, fill="both")


# Button row third
btn7 = Button(
    btnrow3,
    text = "7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_seven_clicked,
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_eight_clicked,
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_nine_clicked,
)
btn9.pack(side=LEFT, expand=True, fill="both")

btnmul = Button(
    btnrow3,
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_mult_clicked,
)
btnmul.pack(side=LEFT, expand=True, fill="both")


# Button row fourth
btnC = Button(
    btnrow4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_C_pressed,
)
btnC.pack(side=LEFT, expand=True, fill="both")

btn0 = Button(
    btnrow4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_zero_clicked,
)
btn0.pack(side=LEFT, expand=True, fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=result,
)
btnequal.pack(side=LEFT, expand=True, fill="both")

btndvd = Button(
    btnrow4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command=btn_divide_clicked,
)
btndvd.pack(side=LEFT, expand=True, fill="both")

root.mainloop()