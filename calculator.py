from tkinter import *

def button(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("Arithmetic Error!")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Invalid syntax")
        equation_text = ""

def clr():
    global equation_text
    equation_label.set('')
    equation_text = ''

window = Tk()
window.geometry('700x700')
window.title('Calculator')

equation_text = ''
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Algerian', 20), bg="#fffdd0", width=24, height=2)
label.grid(row=0, column=0, columnspan=4)

frame = Frame(window)
frame.grid(row=1, column=0, columnspan=4)

buttons = [
    ('1', 0, 0), ('2', 0, 1), ('3', 0, 2), ('/', 0, 3, 'yellow'),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3, 'yellow'),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('-', 2, 3, 'yellow'),
    ('0', 3, 0), ('.', 3, 1), ('+', 3, 3, 'yellow')
]

for (text, row, col, *bg_color) in buttons:
    Button(frame, text=text, font=('Algerian', 35), height=1, width=3,
           relief='raised', bd=5,
           command=lambda t=text: button(t), 
           background=bg_color[0] if bg_color else None).grid(row=row, column=col)

buttonEq = Button(frame, text='=', font=('Algerian', 35), height=1, width=3,
                  relief='raised', bd=5, background='yellow',
                  command=equals)
buttonEq.grid(row=3, column=2)

Clear = Button(window, text='Clear', font=('Algerian', 35), height=1, width=5, 
               command=clr, background='red', relief='raised', bd=5)
Clear.grid(row=4, column=1, columnspan=2)

window.mainloop()

