import tkinter as tk
from tkinter import messagebox

def convert_to_decimal(number: str, base: int) -> int:
    """Конвертирует число из заданной системы счисления в десятичную."""
    return int(number, base)

def convert_from_decimal(number: int, base: int) -> str:
    """Конвертирует десятичное число в заданную систему счисления."""
    if base == 2:
        return bin(number)[2:]  # Убираем '0b' в начале
    elif base == 8:
        return oct(number)[2:]  # Убираем '0o' в начале
    elif base == 16:
        return hex(number)[2:].upper()  # Убираем '0x' и делаем заглавными
    else:
        return str(number)  # Для десятичной системы

def convert_number():
    """Обрабатывает конвертацию числа и выводит результат."""
    number = entry_number.get()
    from_base = int(entry_from_base.get())
    to_base = int(entry_to_base.get())

    try:
        decimal_number = convert_to_decimal(number, from_base)
        converted_number = convert_from_decimal(decimal_number, to_base)
        result_label.config(text=f"Результат: {converted_number}")
    except ValueError:
        messagebox.showerror("Ошибка", "Неверный ввод. Проверьте число и системы счисления.")

# Создание основного окна приложения
root = tk.Tk()
root.title("Калькулятор перевода систем счисления")

# Создание и размещение элементов интерфейса
tk.Label(root, text="Введите число:").grid(row=0, column=0)
entry_number = tk.Entry(root)
entry_number.grid(row=0, column=1)

tk.Label(root, text="Система счисления (из):").grid(row=1, column=0)
entry_from_base = tk.Entry(root)
entry_from_base.grid(row=1, column=1)

tk.Label(root, text="Система счисления (в):").grid(row=2, column=0)
entry_to_base = tk.Entry(root)
entry_to_base.grid(row=2, column=1)

convert_button = tk.Button(root, text="Конвертировать", command=convert_number)
convert_button.grid(row=3, columnspan=2)

result_label = tk.Label(root, text="Результат:")
result_label.grid(row=4, columnspan=2)

# Запуск главного цикла приложения
root.mainloop()
