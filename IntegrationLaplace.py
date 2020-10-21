import numpy as np
import sympy
from sympy import *

from tkinter import *
import tkinter as tk

s = sympy.Symbol('s')
t = sympy.Symbol('t')


def answersInt():
    global ans1, ans2, ans3, ans4, ans5
    a, s, t, x, y, z = symbols('a s t x y z')
    A2.delete(0, END)

    if E1.get() == '' or E1.get() == 0:
        ans1 = ''
    else:
        if E1.index(0) == '-':
            ans1 = integrate(sympify(E1.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            sig = '-'
            ans1s = sig + ans1
            A2.insert(0, ans1s)
        else:
            ans1 = integrate(sympify(E1.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            A2.insert(0, ans1)

    if E2.get() == '' or E2.get() == 0:
        ans2 = ''
    else:
        if E2.index(0) == '-':
            ans2 = integrate(sympify(E2.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            sig = ' - '
            ans2s = sig + ans2
            A2.insert(END, ans2s)
        else:
            ans2 = integrate(sympify(E2.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            A2.insert(END, ' + ')
            A2.insert(END, ans2)

    if E3.get() == '' or E3.get() == 0:
        ans3 = ''
    else:
        if E3.index(0) == '-':
            ans3 = integrate(sympify(E3.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            sig = ' - '
            ans3s = sig + ans3
            A2.insert(END, ans3s)
        else:
            ans3 = integrate(sympify(E3.get()) * (exp((-s * t))), (t, int(E4.get()), sympify(E5.get())))
            A2.insert(END, ' + ')
            A2.insert(END, ans3)

    """if E4.get() == '' or E4.get() == 0:
        ans4 = ''
    else:
        if E4.index(0) == '-':
            ans4 = sympify(inverse_laplace_transform(E4.get(), s, t, simplify=TRUE))
            sig = ' - '
            ans4s = sig + ans4
            A2.insert(END, ans4s)
        else:
            ans4 = sympify(inverse_laplace_transform(E4.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, ans4)

    if E5.get() == '' or E5.get() == 0:
        ans5 = ''
    else:
        if E5.index(0) == '-':
            ans5 = sympify(inverse_laplace_transform(E5.get(), s, t, simplify=TRUE))
            sig = ' - '
            ans5s = sig + ans5
            A2.insert(END, ans5s)
        else:
            ans5 = sympify(inverse_laplace_transform(E5.get(), s, t, simplify=TRUE))
            A2.insert(END, ' + ')
            A2.insert(END, ans5)"""

    A2.config(font=("Helvetica", 15))
    A2.config(state=DISABLED)


newWindow = tk.Tk()
newWindow.title("Laplace por Integracion")
newWindow.config(bg='DarkOliveGreen3') # DarkOliveGreen3
newWindow.geometry('{}x{}'.format(750, 550))
newWindow.resizable(False, False)
top1 = Frame(newWindow, bg='DarkOliveGreen3', width=425, height=150)
top2 = Frame(newWindow, bg='DarkOliveGreen3', width=425, height=150)
top2R = Frame(top2, bg='DarkOliveGreen3')
btm = Frame(newWindow, bg='DarkOliveGreen3', width=700, height=450)

top1.pack()
top2.pack()
top2R.pack(side=RIGHT)
btm.pack(anchor='s')

wInv = Label(top1, text="Laplace por Integracion", bg='DarkOliveGreen3', font=("Helvetica", 18, "bold"))
wInv.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn1 = Button(top2R, text='Calcular!', borderwidth=5, command=answersInt)

wInv1 = Label(top2, text='Ingrese el primer elemento de f(t): ', bg='DarkOliveGreen3', font=("Helvetica", 15))
wInv1.pack(padx=(10, 10), anchor='nw', pady=(20, 0))
E1 = Entry(top2, width=15)
E1.config(font=("Helvetica", 14))
E1.pack(padx=(10, 10), pady=(5, 5))

wInv2 = Label(top2, text='Ingrese el segundo elemento de f(t): ', bg='DarkOliveGreen3', font=("Helvetica", 15))
wInv2.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E2 = Entry(top2, width=15)
E2.config(font=("Helvetica", 14))
E2.pack(padx=(10, 10), pady=(5, 5))

wInv3 = Label(top2, text='Ingrese el tercero elemento de f(t): ', bg='DarkOliveGreen3', font=("Helvetica", 15))
wInv3.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E3 = Entry(top2, width=15)
E3.config(font=("Helvetica", 14))
E3.pack(padx=(10, 10), pady=(5, 5))

wInv4 = Label(top2, text='Ingrese el limite inferior: ', bg='DarkOliveGreen3', font=("Helvetica", 15))
wInv4.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E4 = Entry(top2, width=15)
E4.config(font=("Helvetica", 14))
E4.pack(padx=(10, 10), pady=(5, 5))

wInv5 = Label(top2, text='Ingrese el limite superior: ', bg='DarkOliveGreen3', font=("Helvetica", 15))
wInv5.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E5 = Entry(top2, width=15)
E5.config(font=("Helvetica", 14))
E5.pack(padx=(10, 10), pady=(5, 5))

SInv2 = Text(top2R, height=7, width=35, borderwidth=5)
SInv2.pack(padx=(0, 10), fill=tk.Y)
btn1.config(font=("Helvetica", 14))
btn1.pack(padx=(75, 75), pady=(50, 0))
SInv2.config(font=("Helvetica", 14))

inst = """Para poder evaluar potencias es necesario    usar (**), 2**4 seria 16. Para multiplicar un       numero con una variable tendras que separar los usando un *. Para indicar infinito por favor usar 'oo'. En esta calculadora 'exp' significa     euler. """

SInv2.insert(tk.END, inst)
SInv2.config(state=DISABLED)

AInv1 = Label(btm, text='Respuesta: ', bg='DarkOliveGreen3', font=("Helvetica", 16, "bold"))
AInv1.pack(anchor='n', pady=(30, 0))

S1 = tk.Scrollbar(btm, orient='horizontal')
A2 = Entry(btm, width=50)
A2.config(xscrollcommand=S1.set)
A2.pack(anchor='n', pady=(15, 0))
S1.config(command=A2.xview)
S1.pack(fill=tk.X, anchor='s')

mainloop()
