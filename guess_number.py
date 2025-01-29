import tkinter as tk
import random

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Угадай число")
        
        self.difficulty_label = tk.Label(root, text="Выберите уровень сложности:")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar(value='easy')
        self.easy_radio = tk.Radiobutton(root, text='Легкий (1-10)', variable=self.difficulty_var, value='easy')
        self.medium_radio = tk.Radiobutton(root, text='Средний (1-50)', variable=self.difficulty_var, value='medium')
        self.hard_radio = tk.Radiobutton(root, text='Сложный (1-100)', variable=self.difficulty_var, value='hard')

        self.easy_radio.pack()
        self.medium_radio.pack()
        self.hard_radio.pack()
        self.start_button = tk.Button(root, text='Начать игру', command=self.start_game)
        self.start_button.pack()

        self.guess_label = tk.Label(root, text='Угадайте число:')
        self.guess_label.pack()
        
        self.guess_entry = tk.Entry(root)
        self.guess_entry.pack()

        self.guess_button = tk.Button(root, text='Угадать', command=self.check_guess)
        self.guess_button.pack()

        self.message_label = tk.Label(root, text='')
        self.message_label.pack()

        self.secret_number = None
        self.attempts = 0

    def start_game(self):
        difficulty = self.difficulty_var.get()
        
        if difficulty == 'easy':
            self.secret_number = random.randint(1, 10)
        elif difficulty == 'medium':
            self.secret_number = random.randint(1, 50)
        else:
            self.secret_number = random.randint(1, 100)

        self.attempts = 0
        self.message_label.config(text='')

    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.attempts += 1
        
        if guess == self.secret_number:
            self.message_label.config(text=f'Поздравляем! Вы угадали число {self.secret_number} за {self.attempts} попыток.')
            self.guess_entry.delete(0, tk.END)
        elif guess < self.secret_number:
            self.message_label.config(text='Слишком низкое число!')
        else:
            self.message_label.config(text='Слишком высокое число!')

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
