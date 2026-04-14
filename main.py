import tkinter as tk
import math
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


calculator_window = tk.Tk()
calculator_window.title("My Calculator")

icon = tk.PhotoImage(file=resource_path("calculator.png"))
calculator_window.iconphoto(True, icon)

display_screen = tk.Entry(
    calculator_window,
    width=20,
    font=('Arial' , 24),
    justify='right',
    border=3,
    relief='solid'
)

display_screen.grid(
    row=0,
    column=0,
    columnspan=3,
    padx=5,
    pady=5,
    sticky="nsew"
)

backspace_button = tk.Button(
    calculator_window,
    text='⌫',
    width=5,
    height=1,
    font=('Arial', 14),
    command=lambda: button_clicked('⌫')
)

backspace_button.grid(
    row=0,
    column=3,
    padx=2,
    pady=2
)

calculator_buttons = [
    ['√', '^', '%', 'Clear'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

operators = ['+', '-', '*', '/', '^']

last_result = False

def button_clicked(button_text):
    global last_result

    if button_text == "Clear":
        display_screen.delete(0, tk.END)


    elif button_text == "⌫":
        current_text = display_screen.get()
        display_screen.delete(0, tk.END)
        display_screen.insert(0, current_text[:-1])

    elif button_text == "=":
        try:
            expression = display_screen.get()
            expression = expression.replace("^", "**")
            result = eval(expression)
            display_screen.delete(0, tk.END)
            display_screen.insert(0, str(result))
            last_result = True
        except Exception:
            display_screen.delete(0, tk.END)
            display_screen.insert(0, "Error")

    elif button_text == "√":
        try:
            value = float(display_screen.get())
            result = math.sqrt(value)
            display_screen.delete(0, tk.END)
            display_screen.insert(0, str(result))
        except Exception:
            display_screen.delete(0, tk.END)
            display_screen.insert(0, "Error")

    elif button_text == "%":
        try:
            value = float(display_screen.get())
            result = value / 100
            display_screen.delete(0, tk.END)
            display_screen.insert(0, str(result))
        except Exception:
            display_screen.delete(0, tk.END)
            display_screen.insert(0, "Error")



    else:

        current_text = display_screen.get()

        # If a number is pressed after a result, start new calculation

        if last_result and button_text not in operators:
            display_screen.delete(0, tk.END)

            current_text = ""

            last_result = False

        # Prevent two operators in a row

        if button_text in operators:

            if not current_text:
                return

            if current_text[-1] in operators:
                return
            last_result = False

        display_screen.insert(tk.END, button_text)

for row_number, button_row in enumerate(calculator_buttons):
    for column_number, button_text in enumerate(button_row):
        calculator_button = tk.Button(
            calculator_window,
            text=button_text,
            width=5,
            height=2,
            font=('Arial', 18),
            activebackground='darkgray',
            command=lambda btn=button_text: button_clicked(btn)
        )

        calculator_button.grid(
            row=row_number + 1,
            column=column_number,
            padx=2,
            pady=2,
            sticky="nsew"
        )


def key_pressed(event):
    key = event.char

    if key in "0123456789.+-*/":
        button_clicked(key)

    elif key == "\r":   # Enter key
        button_clicked("=")

    elif event.keysym == "BackSpace":
        button_clicked("⌫")

    elif event.keysym == "Delete":
        button_clicked("Clear")


calculator_window.configure(padx=20, pady=20)
calculator_window.bind("<Key>", key_pressed)

for col in range(4):
    calculator_window.grid_columnconfigure(col, weight=1)

for row in range(6):
        calculator_window.grid_rowconfigure(row, weight=1)

calculator_window.mainloop()
