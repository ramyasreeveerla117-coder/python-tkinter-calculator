import tkinter as tk
from tkinter import *

window = Tk()
window.geometry("312x324")
window.resizable(0,0)
window.title("calculator")

# Functions
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except:
        input_text.set("Error")
        expression = ""

expression = ""
input_text = StringVar()

# Input frame
input_frame = Frame(window, width=312, height=50, bd=0,highlightbackground="black", highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'),textvariable=input_text, width=22,bg="#eee", bd=0, justify="right")
input_field.pack(ipady=10)

# Buttons frame
btns_frame = Frame(window, width=312, height=275, bg="grey")
btns_frame.pack()

# Row 1
clear = Button(btns_frame, text='C', width=32, height=3, bg="#eee", fg="black", command=btn_clear)
clear.grid(row=0, column=0, columnspan=3)

divide = Button(btns_frame, text='/', width=10, height=3, bg="#eee", fg="black", command=lambda: btn_click("/"))
divide.grid(row=0, column=3)

# Row 2
seven = Button(btns_frame, text='7', width=10, height=3, bg="#fff", command=lambda: btn_click("7"))
seven.grid(row=1, column=0)

eight = Button(btns_frame, text='8', width=10, height=3, bg="#fff",command=lambda: btn_click("8"))
eight.grid(row=1, column=1)

nine = Button(btns_frame, text='9', width=10, height=3, bg="#fff", command=lambda: btn_click("9"))
nine.grid(row=1, column=2)

multiply = Button(btns_frame, text='*', width=10, height=3,bg="#eee", command=lambda: btn_click("*"))
multiply.grid(row=1, column=3)

# Row 3
four = Button(btns_frame, text='4', width=10, height=3, bg="#fff",command=lambda: btn_click("4"))
four.grid(row=2, column=0)

five = Button(btns_frame, text='5', width=10, height=3, bg="#fff",command=lambda: btn_click("5"))
five.grid(row=2, column=1)

six = Button(btns_frame, text='6', width=10, height=3, bg="#fff",command=lambda: btn_click("6"))
six.grid(row=2, column=2)

minus = Button(btns_frame, text='-', width=10, height=3,bg="#eee", command=lambda: btn_click("-"))
minus.grid(row=2, column=3)

# Row 4
one = Button(btns_frame, text='1', width=10, height=3, bg="#fff",command=lambda: btn_click("1"))
one.grid(row=3, column=0)

two = Button(btns_frame, text='2', width=10, height=3, bg="#fff",command=lambda: btn_click("2"))
two.grid(row=3, column=1)

three = Button(btns_frame, text='3', width=10, height=3, bg="#fff",command=lambda: btn_click("3"))
three.grid(row=3, column=2)

plus = Button(btns_frame, text='+', width=10, height=3,bg="#eee", command=lambda: btn_click("+"))
plus.grid(row=3, column=3)

# Row 5
zero = Button(btns_frame, text='0', width=21, height=3,bg="#eee", command=lambda: btn_click("0"))
zero.grid(row=4, column=0, columnspan=2)

equal = Button(btns_frame, text='=', width=21, height=3,bg="#eee", command=btn_equal)
equal.grid(row=4, column=2, columnspan=2)

window.mainloop()
