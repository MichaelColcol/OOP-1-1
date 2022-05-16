from tkinter import *

window = Tk()
window.title("Simple Calculator")
window.geometry("400x300+20+10")


class MyWindow:
    def __init__(self,window):
        self.lbl1 = Label(window, text = "Standard Calculator")
        self.lbl1.grid(row=0, column=0, columnspan=3, sticky=EW)

        self.lbl2 = Label(window, text = "Enter the 1st Number:")
        self.lbl2.grid(row=1, column=0)

        self.txt2 = Entry(window, bd=3)
        self.txt2.grid(row=1,column=1,sticky = W)

        self.lbl3 = Label(window, text="Enter the 2nd Number:")
        self.lbl3.grid(row=2,column=0,)

        self.txt3 = Entry(window,bd=3)
        self.txt3.grid(row=2,column=1)

        self.btn1 = Button(window, text="Adddition", command=self.add)
        self.btn1.grid(row=4,column=0)

        self.btn2 = Button(window, text="Subtraction", command=self.sub)
        self.btn2.grid(row=4,column=1)

        self.btn3 = Button(window, text="Multiplication", command=self.mul)
        self.btn3.grid(row=4,column=2)

        self.btn4 = Button(window, text="Division", command=self.div)
        self.btn4.grid(row=4,column=3)

        self.lbl4 = Label(window, text="Result")
        self.lbl4.grid(row=6,column=0)

        self.txt4 = Entry(window, bd=3)
        self.txt4.grid(row=6,column=1)

    def add(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 + num2
        self.txt4.insert(END, str(answer))

    def sub(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 - num2
        self.txt4.insert(END, str(answer))

    def mul(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 * num2
        self.txt4.insert(END, str(answer))

    def div(self):
        self.txt4.delete("0", END)
        num1 = int(self.txt2.get())
        num2 = int(self.txt3.get())
        answer = num1 / num2
        self.txt4.insert(END, str(answer))


mywin = MyWindow(window)
window.mainloop()
