import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")
        self.difficulty = tk.IntVar(value=10)
        self.random_number = None
        self.attempts = 0

        self.label = tk.Label(master, text="Выберите уровень сложности:")
        self.label.pack()

        self.easy_button = tk.Radiobutton(master, text="Легкий (1-10)", variable=self.difficulty, value=10, command=self.new_game)
        self.easy_button.pack()
        self.medium_button = tk.Radiobutton(master, text="Средний (1-50)", variable=self.difficulty, value=50, command=self.new_game)
        self.medium_button.pack()

        self.hard_button = tk.Radiobutton(master, text="Сложный (1-100)", variable=self.difficulty, value=100, command=self.new_game)
        self.hard_button.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Угадать", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def new_game(self):
        max_value = self.difficulty.get()
        self.random_number = random.randint(1, max_value)
        self.attempts = 0
        self.result_label.config(text="")

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1
        if guess == self.random_number:
            self.result_label.config(text=f"Поздравляем! Вы угадали число {self.random_number} за {self.attempts} попыток.")
        elif guess < self.random_number:
            self.result_label.config(text='Слишком маленькое число!')
        else:
            self.result_label.config(text='Слишком большое число!')

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
