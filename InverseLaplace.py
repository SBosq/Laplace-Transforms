from sympy import *
from sympy.integrals import inverse_laplace_transform
from sympy import sympify
from tkinter import *
import tkinter as tk


def answersInv():
    global AnswInv1, AnswInv2, AnswInv3, AnswInv4, AnswInv5
    a, s, t, x, y, z = symbols('a s t x y z')
    A2.delete(0, END)

    if E1.get() == '' or E1.get() == 0:
        AnswInv1 = ''
    else:
        if E1.index(0) == '-':
            AnswInv1 = sympify(inverse_laplace_transform(E1.get(), s, t, simplify=TRUE))
            sig = '-'
            AnswInv1s = sig + AnswInv1
            A2.insert(0, AnswInv1s)
        else:
            AnswInv1 = sympify(inverse_laplace_transform(E1.get(), s, t, simplify=TRUE))
            A2.insert(0, AnswInv1)

    if E2.get() == '' or E2.get() == 0:
        AnswInv2 = ''
    else:
        if E2.index(0) == '-':
            AnswInv2 = sympify(inverse_laplace_transform(E2.get(), s, t, simplify=TRUE))
            sig = ' - '
            AnswInv2s = sig + AnswInv2
            A2.insert(END, AnswInv2s)
        else:
            AnswInv2 = sympify(inverse_laplace_transform(E2.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, AnswInv2)

    if E3.get() == '' or E3.get() == 0:
        AnswInv3 = ''
    else:
        if E3.index(0) == '-':
            AnswInv3 = sympify(inverse_laplace_transform(E3.get(), s, t, simplify=TRUE))
            sig = ' - '
            AnswInv3s = sig + AnswInv3
            A2.insert(END, AnswInv3s)
        else:
            AnswInv3 = sympify(inverse_laplace_transform(E3.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, AnswInv3)

    if E4.get() == '' or E4.get() == 0:
        AnswInv4 = ''
    else:
        if E4.index(0) == '-':
            AnswInv4 = sympify(inverse_laplace_transform(E4.get(), s, t, simplify=TRUE))
            sig = ' - '
            AnswInv4s = sig + AnswInv4
            A2.insert(END, AnswInv4s)
        else:
            AnswInv4 = sympify(inverse_laplace_transform(E4.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, AnswInv4)

    if E5.get() == '' or E5.get() == 0:
        AnswInv5 = ''
    else:
        if E5.index(0) == '-':
            AnswInv5 = sympify(inverse_laplace_transform(E5.get(), s, t, simplify=TRUE))
            sig = ' - '
            AnswInv5s = sig + AnswInv5
            A2.insert(END, AnswInv5s)
        else:
            AnswInv5 = sympify(inverse_laplace_transform(E5.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, AnswInv5)

    A2.config(font=("Helvetica", 15))
    A2.config(state=DISABLED)


newWindow = tk.Tk()
newWindow.title("Inversa de Laplace")
newWindow.config(bg='SeaGreen1') # DarkOliveGreen3
newWindow.geometry('{}x{}'.format(750, 550))
newWindow.resizable(False, False)
top1 = Frame(newWindow, bg='SeaGreen1', width=425, height=150)
top2 = Frame(newWindow, bg='SeaGreen1', width=425, height=150)
top2R = Frame(top2, bg='SeaGreen1')
btm = Frame(newWindow, bg='SeaGreen1', width=700, height=450)

top1.pack()
top2.pack()
top2R.pack(side=RIGHT)
btm.pack(anchor='s')

wInv = Label(top1, text="Inversa de Laplace", bg='SeaGreen1', font=("Helvetica", 18, "bold"))
wInv.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn1 = Button(top2R, text='Calcular!', borderwidth=5, command=answersInv)

wInv1 = Label(top2, text='Ingrese el primer elemento de f(t): ', bg='SeaGreen1', font=("Helvetica", 15))
wInv1.pack(padx=(10, 10), anchor='nw', pady=(20, 0))
E1 = Entry(top2, width=15)
E1.config(font=("Helvetica", 14))
E1.pack(padx=(10, 10), pady=(5, 5))

wInv2 = Label(top2, text='Ingrese el segundo elemento de f(t): ', bg='SeaGreen1', font=("Helvetica", 15))
wInv2.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E2 = Entry(top2, width=15)
E2.config(font=("Helvetica", 14))
E2.pack(padx=(10, 10), pady=(5, 5))

wInv3 = Label(top2, text='Ingrese el tercero elemento de f(t): ', bg='SeaGreen1', font=("Helvetica", 15))
wInv3.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E3 = Entry(top2, width=15)
E3.config(font=("Helvetica", 14))
E3.pack(padx=(10, 10), pady=(5, 5))

wInv4 = Label(top2, text='Ingrese el cuarto elemento de f(t): ', bg='SeaGreen1', font=("Helvetica", 15))
wInv4.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E4 = Entry(top2, width=15)
E4.config(font=("Helvetica", 14))
E4.pack(padx=(10, 10), pady=(5, 5))

wInv5 = Label(top2, text='Ingrese el quinto elemento de f(t): ', bg='SeaGreen1', font=("Helvetica", 15))
wInv5.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E5 = Entry(top2, width=15)
E5.config(font=("Helvetica", 14))
E5.pack(padx=(10, 10), pady=(5, 5))

SInv2 = Text(top2R, height=5, width=35, borderwidth=5)
SInv2.pack(padx=(0, 10), fill=tk.Y)
btn1.config(font=("Helvetica", 14))
btn1.pack(padx=(75, 75), pady=(50, 0))
SInv2.config(font=("Helvetica", 14))

inst = """Para poder evaluar potencias es necesario    usar (**), 2**4 seria 16. Para multiplicar un       numero con una variable tendras que separar los usando un *. """

SInv2.insert(tk.END, inst)
SInv2.config(state=DISABLED)

AInv1 = Label(btm, text='Respuesta: ', bg='SeaGreen1', font=("Helvetica", 16, "bold"))
AInv1.pack(anchor='n', pady=(30, 0))

A2 = Entry(btm, width=30)
A2.pack(anchor='n', pady=(15, 0))

mainloop()
