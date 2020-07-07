from tkinter import *
from tkinter.scrolledtext import ScrolledText


class Calc(Tk):
    def __init__(self):
        super().__init__()
        self.gui()
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

    def gui(self):
        self.text_entry()
        self.buttons_0_9()
        self.button_signs()
        self.btn_delete()
        self.btn_clear()

    def text_entry(self):
        self.text = Entry(borderwidth=3, justify=RIGHT)
        self.text.grid(column=0, columnspan=4, row=0, sticky=E + W, padx=5)

    def buttons_0_9(self):
        self.button_1 = Button(text=1, width=10, height=3, command=lambda: self.click(1))
        self.button_1.grid(column=0, row=2, sticky=N + S + E + W)
        self.button_2 = Button(text=2, width=10, height=3, command=lambda: self.click(2))
        self.button_2.grid(column=1, row=2, sticky=N + S + E + W)
        self.button_3 = Button(text=3, width=10, height=3, command=lambda: self.click(3))
        self.button_3.grid(column=2, row=2, sticky=N + S + E + W)

        self.button_4 = Button(text=4, width=10, height=3, command=lambda: self.click(4))
        self.button_4.grid(column=0, row=3, sticky=N + S + E + W)
        self.button_5 = Button(text=5, width=10, height=3, command=lambda: self.click(5))
        self.button_5.grid(column=1, row=3, sticky=N + S + E + W)
        self.button_6 = Button(text=6, width=10, height=3, command=lambda: self.click(6))
        self.button_6.grid(column=2, row=3, sticky=N + S + E + W)

        self.button_7 = Button(text=7, width=10, height=3, command=lambda: self.click(7))
        self.button_7.grid(column=0, row=4, sticky=N + S + E + W)
        self.button_8 = Button(text=8, width=10, height=3, command=lambda: self.click(8))
        self.button_8.grid(column=1, row=4, sticky=N + S + E + W)
        self.button_9 = Button(text=9, width=10, height=3, command=lambda: self.click(9))
        self.button_9.grid(column=2, row=4, sticky=N + S + E + W)

        self.button_0 = Button(text=0, width=10, height=3, command=lambda: self.click(0))
        self.button_0.grid(column=0, row=5, sticky=N + S + E + W)

    def button_signs(self):
        self.button_add = Button(text="+", width=10, height=3, command=lambda: self.click("+"))
        self.button_add.grid(column=3, row=2, sticky=N + S + E + W)

        self.button_sub = Button(text="-", width=10, height=3, command=lambda: self.click("-"))
        self.button_sub.grid(column=3, row=3, sticky=N + S + E + W)

        self.button_mul = Button(text="*", width=10, height=3, command=lambda: self.click("*"))
        self.button_mul.grid(column=3, row=4, sticky=N + S + E + W)

        self.button_div = Button(text="/", width=10, height=3, command=lambda: self.click("/"))
        self.button_div.grid(column=3, row=5, sticky=N + S + E + W)

        self.button_dot = Button(text=".", width=10, height=3, command=lambda: self.click("."))
        self.button_dot.grid(column=1, row=5, sticky=N + S + E + W)

        self.button_equal = Button(text="=", width=10, height=3, command=self.perform)
        self.button_equal.grid(column=2, row=5, sticky=N + S + E + W)

    def btn_delete(self):
        self.button_delete = Button(text="delete", width=10, height=3, command=self.delete)
        self.button_delete.grid(column=2, columnspan=2, row=1, pady=5, sticky=N + S + E + W)

    def btn_clear(self):
        self.button_clear = Button(text="clear", width=10, height=3, command=self.clear)
        self.button_clear.grid(column=0, columnspan=2, row=1, pady=5, sticky=N + S + E + W)

    def click(self, value):
        operators = ['+', '-', '/', '*', '.']

        equation = self.text.get()
        self.text.delete(0, "end")
        equation += str(value)
        self.text.insert(0, equation)

    def perform(self):
        text = self.text.get()
        self.text.delete(0, "end")
        try:
            self.text.insert(0, eval(text))
        except SyntaxError:
            self.text.delete(0, "end")
            self.text.insert(0, "Syntax Error")

    def delete(self):
        self.text.delete(len(self.text.get()) - 1, "end")

    def clear(self):
        self.text.delete(0, "end")


root = Calc()
root.mainloop()
