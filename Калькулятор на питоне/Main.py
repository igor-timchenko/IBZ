import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Калькулятор")
        self.master.geometry("400x600")

        self.expression = ""
        self.memory = 0

        # Экран ввода
        self.input_var = tk.StringVar()
        self.input_frame = tk.Entry(master, textvariable=self.input_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.input_frame.grid(row=0, column=0, columnspan=4)

        # Кнопки
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            '√', '^', 'M+', 'M-'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_var.set("")
        elif char == '=':
            try:
                result = str(eval(self.expression.replace('^', '**').replace('√', 'math.sqrt')))
                self.input_var.set(result)
                self.expression = result
            except Exception as e:
                messagebox.showerror("Ошибка", "Неверное выражение")
                self.expression = ""
                self.input_var.set("")
        elif char in ['M+', 'M-']:
            if char == 'M+':
                try:
                    self.memory += float(self.input_var.get())
                    messagebox.showinfo("Память", f"Сохранено в памяти: {self.memory}")
                except ValueError:
                    messagebox.showerror("Ошибка", "Неверное число")
            elif char == 'M-':
                try:
                    self.memory -= float(self.input_var.get())
                    messagebox.showinfo("Память", f"Из памяти: {self.memory}")
                except ValueError:
                    messagebox.showerror("Ошибка", "Неверное число")
        else:
            self.expression += str(char)
            self.input_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
