# import sympy
# from sympy.abc import s, t, x, y, z

# Laplace Transform
# U = laplace_transform(t**2-t+sym.exp(-t), t, s)
# print("1. " + str(U[0]) + '\n')

# V = laplace_transform(3*sym.cos(5*t), t, s)
# print("2. " + str(V[0]) + '\n')

# Z = laplace_transform(3*sym.cosh(5*t)-4*sym.sinh(5*t), t, s)
# print("3. " + str(Z[0]) + '\n')

# Q = laplace_transform((5*sym.exp(2*t)-3)**2, t, s)
# print("4. " + str(Q[0]) + '\n')

# S = laplace_transform(3*t**4-2*t**3+4*sym.exp(-3*t)-2*sym.sin(5*t)+3*sym.cos(2*t), t, s)
# print("5. " + str(S[0]) + '\n')

# H = laplace_transform(t**3*sym.exp(-3*t), t, s)
# print("6. " + str(H[0]) + '\n')

# W = laplace_transform(sym.exp(-t)*(3*sym.sinh(2*t)-5*sym.cosh(2*t)), t, s)
# print("7. " + str(W[0]) + '\n')

# D = laplace_transform((1+t*sym.exp(-t))**3, t, s)
# print("8. " + str(D[0]))


from sympy import *
from sympy import sympify
from sympy.integrals import laplace_transform
from tkinter import *
import tkinter as tk


def answers():
    global Answ1, Answ2, Answ3, Answ4, Answ5
    s, t, x, y, z = symbols('s t x y z')
    A2.delete(0, END)

    if E1.get() == '' or E1.get() == 0:
        Answ1 = ''
    else:
        if E1.index(0) == '-':
            Answ1 = sympify(laplace_transform(E1.get(), t, s, noconds=True))
            sig = '-'
            Answ1s = sig + Answ1
            A2.insert(0, Answ1s)
        else:
            Answ1 = sympify(laplace_transform(E1.get(), t, s, noconds=True))
            A2.insert(0, Answ1)

    if E2.get() == '' or E2.get() == 0:
        Answ2 = ''
    else:
        if E2.index(0) == '-':
            Answ2 = sympify(laplace_transform(E2.get(), t, s, noconds=True))
            sig = ' - '
            Answ2s = sig + Answ2
            A2.insert(END, Answ2s)
        else:
            Answ2 = sympify(laplace_transform(E2.get(), t, s, noconds=True))
            A2.insert(END, ' + ')
            A2.insert(END, Answ2)

    if E3.get() == '' or E3.get() == 0:
        Answ3 = ''
    else:
        if E3.index(0) == '-':
            Answ3 = sympify(laplace_transform(E3.get(), t, s, noconds=True))
            sig = ' - '
            Answ3s = sig + Answ3
            A2.insert(END, Answ3s)
        else:
            Answ3 = sympify(laplace_transform(E3.get(), t, s, noconds=True))
            A2.insert(END, ' + ')
            A2.insert(END, Answ3)

    if E4.get() == '' or E4.get() == 0:
        Answ4 = ''
    else:
        if E4.index(0) == '-':
            Answ4 = sympify(laplace_transform(E4.get(), t, s, noconds=True))
            sig = ' - '
            Answ4s = sig + Answ4
            A2.insert(END, Answ4s)
        else:
            Answ4 = sympify(laplace_transform(E4.get(), t, s, noconds=True))
            A2.insert(END, ' + ')
            A2.insert(END, Answ4)

    if E5.get() == '' or E5.get() == 0:
        Answ5 = ''
    else:
        if E5.index(0) == '-':
            Answ5 = sympify(laplace_transform(E5.get(), t, s, noconds=True))
            sig = ' - '
            Answ5s = sig + Answ5
            A2.insert(END, Answ5s)
        else:
            Answ5 = sympify(laplace_transform(E5.get(), t, s, noconds=True))
            A2.insert(END, ' + ')
            A2.insert(END, Answ5)

    A2.config(font=("Helvetica", 15))
    A2.config(state=DISABLED)


main = tk.Tk()
main.geometry('{}x{}'.format(750, 550))
main.resizable(False, False)
main.config(bg="light blue")
main.title('Laplace Transforms')
top_frame1 = Frame(main, bg='light blue', width=425, height=150)
top_frame2 = Frame(main, bg='light blue', width=425, height=150)
top_frame2R = Frame(top_frame2, bg='light blue')
btm_frame = Frame(main, bg='light blue', width=700, height=450)

top_frame1.pack()
top_frame2.pack()
top_frame2R.pack(side=RIGHT)
btm_frame.pack(anchor='s')

w = Label(top_frame1, text="Transformada de Laplace", bg='light blue', font=("Helvetica", 18, "bold"))
w.pack(side=LEFT, padx=(50, 25), pady=(20, 0))

btn = Button(top_frame2R, text='Calcular!', borderwidth=5, command=answers)

w1 = Label(top_frame2, text='Ingrese el primer elemento de f(t): ', bg='light blue', font=("Helvetica", 15))
w1.pack(padx=(10, 10), anchor='nw', pady=(20, 0))
E1 = Entry(top_frame2, width=15)
E1.config(font=("Helvetica", 14))
E1.pack(padx=(10, 10), pady=(5, 5))

w2 = Label(top_frame2, text='Ingrese el segundo elemento de f(t): ', bg='light blue', font=("Helvetica", 15))
w2.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E2 = Entry(top_frame2, width=15)
E2.config(font=("Helvetica", 14))
E2.pack(padx=(10, 10), pady=(5, 5))

w3 = Label(top_frame2, text='Ingrese el tercero elemento de f(t): ', bg='light blue', font=("Helvetica", 15))
w3.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E3 = Entry(top_frame2, width=15)
E3.config(font=("Helvetica", 14))
E3.pack(padx=(10, 10), pady=(5, 5))

w4 = Label(top_frame2, text='Ingrese el cuarto elemento de f(t): ', bg='light blue', font=("Helvetica", 15))
w4.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E4 = Entry(top_frame2, width=15)
E4.config(font=("Helvetica", 14))
E4.pack(padx=(10, 10), pady=(5, 5))

w5 = Label(top_frame2, text='Ingrese el quinto elemento de f(t): ', bg='light blue', font=("Helvetica", 15))
w5.pack(padx=(10, 10), anchor='nw', pady=(5, 0))
E5 = Entry(top_frame2, width=15)
E5.config(font=("Helvetica", 14))
E5.pack(padx=(10, 10), pady=(5, 5))


# S1 = tk.Scrollbar(top_frame2R)
S2 = Text(top_frame2R, height=5, width=35, borderwidth=5)
# S1.pack(side=tk.RIGHT, fill=tk.Y, pady=(10, 0), anchor='e')
S2.pack(padx=(0, 10), fill=tk.Y)
btn.config(font=("Helvetica", 14))
btn.pack(padx=(75, 75), pady=(50, 0))
# S1.config(command=S2.yview)
S2.config(font=("Helvetica", 14))  # yscrollcommand=S1.set,

inst = """Para poder evaluar potencias es necesario    usar (**), 2**4 seria 16. Para multiplicar un       numero con una variable tendras que separar los usando un *. """

S2.insert(tk.END, inst)
S2.config(state=DISABLED)

A1 = Label(btm_frame, text='Respuesta: ', bg='light blue', font=("Helvetica", 16, "bold"))
A1.pack(anchor='n', pady=(30, 0))

A2 = Entry(btm_frame, width=30)
A2.pack(anchor='n', pady=(15, 0))

mainloop()
