from tkinter import *

root = Tk()

dic = {
    '+': '+',
    '-': '-',
    '*': '*',
    '/': '/',
    '=': '=',
}

inputField = Entry(root, width=50)
inputField.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


def click(number):
    global num1
    var = inputField.get()
    inputField.delete(0, END)
    inputField.insert(0, str(var) + str(number))
    num1 = int(inputField.get())


def btn_add():
    global perform
    perform = "add"
    inputField.delete(0, END)


def btn_sub():
    global perform
    perform = "sub"
    inputField.delete(0, END)


def btn_mul():
    global perform
    perform = "mul"
    inputField.delete(0, END)


def btn_div():
    global perform
    perform = "div"
    inputField.delete(0, END)


def btn_equal():
    global perform
    global num1

    if perform == "add":
        num1 += int(inputField.get())
        inputField.insert(0, num1)

    if perform == "sub":
        num1 -= int(inputField.get())
        inputField.insert(0, num1)

    if perform == "mul":
        num1 *= int(inputField.get())
        inputField.insert(0, num1)

    if perform == "div":
        num1 /= int(inputField.get())
        inputField.insert(0, num1)


button_1 = Button(root, text="1", padx=35, pady=35, command=lambda: click(1))
button_2 = Button(root, text="2", padx=35, pady=35, command=lambda: click(2))
button_3 = Button(root, text="3", padx=35, pady=35, command=lambda: click(3))
button_4 = Button(root, text="4", padx=35, pady=35, command=lambda: click(4))
button_5 = Button(root, text="5", padx=35, pady=35, command=lambda: click(5))
button_6 = Button(root, text="6", padx=35, pady=35, command=lambda: click(6))
button_7 = Button(root, text="7", padx=35, pady=35, command=lambda: click(7))
button_8 = Button(root, text="8", padx=35, pady=35, command=lambda: click(8))
button_9 = Button(root, text="9", padx=35, pady=35, command=lambda: click(9))
button_0 = Button(root, text="0", padx=35, pady=35, command=lambda: click(0))

button_add = Button(root, text="+", padx=35, pady=35, command=btn_add)
button_sub = Button(root, text="-", padx=35, pady=35, command=btn_sub)
button_mul = Button(root, text="*", padx=35, pady=35, command=btn_mul)
button_div = Button(root, text="/", padx=35, pady=35, command=btn_div)

button_dot = Button(root, text=".", padx=35, pady=35, command=lambda: click("."))
button_equal = Button(root, text="=", padx=35, pady=35, command=btn_equal)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_dot.grid(row=4, column=1)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

button_equal.grid(row=4, column=2)

root.mainloop()
