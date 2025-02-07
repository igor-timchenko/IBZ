import tkinter as tk
from tkinter import messagebox
import random

class GuessTheNumberApp:
    def __init__(self, master):
        self.master = master
        master.title("Угадай число")

        self.difficulty = None
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 0

        self.label = tk.Label(master, text="Выберите уровень сложности:")
        self.label.pack()

        self.easy_button = tk.Button(master, text="Легкий (1-10, 5 попыток)", command=lambda: self.start_game(1, 5))
        self.easy_button.pack()

        self.medium_button = tk.Button(master, text="Средний (1-50, 7 попыток)", command=lambda: self.start_game(2, 7))
        self.medium_button.pack()

        self.hard_button = tk.Button(master, text="Сложный (1-100, 10 попыток)", command=lambda: self.start_game(3, 10))
        self.hard_button.pack()

        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.submit_button = tk.Button(master, text="Отправить", command=self.check_guess)
        self.submit_button.pack()

    def start_game(self, difficulty, max_attempts):
        self.difficulty = difficulty
        self.max_attempts = max_attempts
        if difficulty == 1:
            self.secret_number = random.randint(1, 10)
            range_text = "от 1 до 10"
        elif difficulty == 2:
            self.secret_number = random.randint(1, 50)
            range_text = "от 1 до 50"
        else:
            self.secret_number = random.randint(1, 100)
            range_text = "от 1 до 100"

        self.attempts = 0
        self.guess_label.config(text=f"Я загадал число {range_text}. У вас {max_attempts} попыток. Попробуйте угадать его!")

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if (self.max_attempts == 5 and (guess < 1 or guess > 10)) or (self.max_attempts == 7 and (guess < 1 or guess > 50)) or (self.max_attempts == 10 and (guess < 1 or guess > 100)):
                messagebox.showwarning("Ошибка", f"Пожалуйста, введите число в диапазоне от {self.max_attempts == 5 and '1 до 10' or self.max_attempts == 7 and '1 до 50' or '1 до 100'}.")
                return

            self.attempts += 1
            
            if guess < self.secret_number:
                remaining_attempts = self.max_attempts - self.attempts
                messagebox.showinfo("Результат", f"Слишком низко! Осталось попыток: {remaining_attempts}.")
            elif guess > self.secret_number:
                remaining_attempts = self.max_attempts - self.attempts
                messagebox.showinfo("Результат", f"Слишком высоко! Осталось попыток: {remaining_attempts}.")
            else:
                if self.attempts == 1:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попытку!")
                elif self.attempts == 2 or self.attempts == 3 or self.attempts == 4:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попытки!")
                else:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попыток!")
                self.reset_game()
                return

            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Игра окончена", f"Вы исчерпали все попытки! Загаданное число было {self.secret_number}.")
                self.reset_game()
                
        except ValueError:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите целое число.")

    def reset_game(self):
        self.difficulty = None
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 0
if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberApp(root)
    root.mainloop()