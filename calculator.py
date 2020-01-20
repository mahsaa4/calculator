from tkinter import *

window = Tk()
window.title("calculator")
window.geometry("333x445")
windowlabel = Label(window, text="CALCULATOR", bg="gray", fg="black", font=("Times", 25, "bold"))
windowlabel.pack(side=TOP)
window.config(background="gray")
text_input = StringVar()
operator = ""
output = Entry(window, width=30, bd=8, textvar=text_input, background="light blue")
output.pack()


def clickbut(number):
    global operator
    operator = operator + str(number)
    text_input.set(operator)


def equlbut():
    global operator
    add = str(eval(operator))
    text_input.set(add)
    operator = ""


def equlbut():
    global operator
    sub = str(eval(operator))
    text_input.set(sub)
    operator = ""


def equlbut():
    global operator
    mul = str(eval(operator))
    text_input.set(mul)
    operator = ""


def equlbut():
    global operator
    div = str(eval(operator))
    text_input.set(div)
    operator = ""


def clrbut():
    text_input.set(' ')


but1 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(1), text="1",
              font=("Courier New", 14, "bold"))
but1.place(x=1,y=100)
but2 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(2), text="2",
              font=("Courier New", 14, "bold"))
but2.place(x=65, y=100)
but3 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(3), text="3",
              font=("Courier New", 14, "bold"))
but3.place(x=130, y=100)
but4 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(4), text="4",
              font=("Courier New", 14, "bold"))
but4.place(x=1, y=170)
but5 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(5), text="5",
              font=("Courier New", 14, "bold"))
but5.place(x=65, y=170)
but6 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(6), text="6",
              font=("Courier New", 14, "bold"))
but6.place(x=130, y=170)
but7 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(7), text="7",
              font=("Courier New", 14, "bold"))
but7.place(x=1, y=240)
but8 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(8), text="8",
              font=("Courier New", 14, "bold"))
but8.place(x=65, y=240)
but9 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(9), text="9",
              font=("Courier New", 14, "bold"))
but9.place(x=130, y=240)
but0 = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut(0), text="0",
              font=("Courier New", 14, "bold"))
but0.place(x=1, y=310)
butdot = Button(window, padx=50, pady=14, bd=4, bg="white", command=lambda: clickbut("."), text=".",
                font=("Courier New", 14, "bold"))
butdot.place(x=65, y=310)
butpl = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut("+"), text="+",
               font=("Courier New", 14, "bold"))
butpl.place(x=195, y=100)
butsub = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut("-"), text="-",
                font=("Courier New", 14, "bold"))
butsub.place(x=195, y=170)
butml = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut("*"), text="*",
               font=("Courier New", 14, "bold"))
butml.place(x=195, y=240)
butdiv = Button(window, padx=17, pady=14, bd=4, bg="white", command=lambda: clickbut("/"), text="/",
                font=("Courier New", 14, "bold"))
butdiv.place(x=195, y=310)
butclear = Button(window, padx=17, pady=119, bd=4, bg="white", command=clrbut, text="CE",
                  font=("Courier New", 14, "bold"))
butclear.place(x=260, y=100)
butequal = Button(window, padx=153, pady=14, bd=4, bg="white", command=equlbut, text="=",
                  font=("Courier New", 14, "bold"))
butequal.place(x=1, y=380)
window.mainloop()
