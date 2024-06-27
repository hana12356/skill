from tkinter import *

window = Tk()
window.geometry("500x600+150+90")
window.title("Calculator")

expression = StringVar()
expression.set("")

def button_click(number):
    current_expression = expression.get()
    current_expression += str(number)
    expression.set(current_expression)

def clear_display():
    expression.set("")

def eval_exp():
    try:
        result = eval(expression.get())
        expression.set(str(result))
    except Exception as e:
        expression.set("Error")

buttons = [
    ("7", 1, 1), ("8", 1, 2), ("9", 1, 3), ("/", 1, 4),
    ("4", 2, 1), ("5", 2, 2), ("6", 2, 3), ("*", 2, 4),
    ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("-", 3, 4),
    ("0", 4, 1), ("C", 4, 2), ("=", 4, 3), ("+", 4, 4)
]

for (text, row, column) in buttons:
    if text == "C":
        Button(window, text=text,bg="#0000FF",fg="#000000" ,font=("Arial", 18, "bold"), width=5, height=2,
               command=clear_display).grid(row=row, column=column, padx=5, pady=5)
    elif text == "=":
        Button(window, text=text,bg="#0000FF",fg="#000000", font=("Arial", 18, "bold"), width=5, height=2,
               command=eval_exp).grid(row=row, column=column, padx=5, pady=5)
    else:
        Button(window, text=text, bg="#0000FF",fg="#000000",font=("Arial", 18, "bold"), width=5, height=2,
               command=lambda num=text: button_click(num)).grid(row=row, column=column, padx=5, pady=5)

Entry(window, textvariable=expression, font=("Arial", 18, "bold"), width=15, bd=5,
      justify="right").grid(row=0, column=0, columnspan=5, pady=10)

window.mainloop()
