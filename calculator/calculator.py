from tkinter import *
import math 

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=28, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def button_subtratc():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def button_mutiply():
    first_number = e.get()
    global f_num
    global math
    math = "mutiplication"
    f_num = float(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def button_percentege():
    first_number = e.get()
    global f_num
    global math
    math = "percentege"
    f_num = float(first_number)
    e.delete(0, END)


def button_sign():
    first_number = e.get()
    global f_num
    global math
    math = "sign change"
    f_num = float(first_number)
    e.delete(0, END)    


def button_equals():
    second_number = e.get()
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "mutiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

    if math == "percentege":
        e.insert(0, f_num / 100)
    if math == "sign change":
        e.insert(0, f_num * (-1))

def Numbers():
    #define buttons
    null = Button(root, text="0", padx=93, pady=15, command=lambda: button_click(0))
    number1 = Button(root, text="1", padx=25, pady=15, command=lambda: button_click(1))
    number2 = Button(root, text="2", padx=25, pady=15, command=lambda: button_click(2))
    number3 = Button(root, text="3", padx=25, pady=15, command=lambda: button_click(3))
    number4 = Button(root, text="4", padx=25, pady=15, command=lambda: button_click(4))
    number5 = Button(root, text="5", padx=25, pady=15, command=lambda: button_click(5))
    number6 = Button(root, text="6", padx=25, pady=15, command=lambda: button_click(6))
    number7 = Button(root, text="7", padx=25, pady=15, command=lambda: button_click(7))
    number8 = Button(root, text="8", padx=25, pady=15, command=lambda: button_click(8))
    number9 = Button(root, text="9", padx=25, pady=15, command=lambda: button_click(9))

    add = Button(root, text="+", padx=25, pady=15, command=button_add)
    subtract = Button(root, text="-", padx=26, pady=15, command=button_subtratc)
    multiply = Button(root, text="×", padx=25, pady=15, command=button_mutiply)
    divide = Button(root, text="÷", padx=25, pady=15, command=button_divide)
    equals = Button(root, text="=", padx=25, pady=15, command=button_equals)
    clear = Button(root, text="AC", padx=19, pady=15, command=button_clear)
    percentege = Button(root, text="%", padx=24, pady=15, command=button_percentege)
    sign = Button(root, text="+/-", padx=20, pady=15, command=button_sign)
#Put on Screen
    #first Row
    clear.grid(row=1, column=0)
    sign.grid(row=1, column=1)
    percentege.grid(row=1, column=2)
    divide.grid(row=1, column=3)
    #Second Row
    number7.grid(row=2, column=0)
    number8.grid(row=2, column=1)
    number9.grid(row=2, column=2)
    multiply.grid(row=2, column=3)
    #Third Row
    number4.grid(row=3, column=0)
    number5.grid(row=3, column=1)
    number6.grid(row=3, column=2)
    subtract.grid(row=3, column=3)
    #Fourth Row
    number1.grid(row=4, column=0)
    number2.grid(row=4, column=1)
    number3.grid(row=4, column=2)
    add.grid(row=4, column=3)
    #Fifth Row
    null.grid(row=5, column=0, columnspan=3)
    equals.grid(row=5, column=3)
    


Numbers()
root.mainloop()


