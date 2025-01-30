import tkinter as tk
import random

class GuessTheNumber:
    def __init__(self, master):
        self.master = master
        self.master.title("Угадай число")
        
        self.difficulty_label = tk.Label(master, text="Выберите уровень сложности:")
        self.difficulty_label.pack()
        
        self.difficulty_var = tk.StringVar(value='10')
        
        self.easy_button = tk.Radiobutton(master, text='Легкий (1-10)', variable=self.difficulty_var, value='10')
        self.medium_button = tk.Radiobutton(master, text='Средний (1-50)', variable=self.difficulty_var, value='50')
        self.hard_button = tk.Radiobutton(master, text='Сложный (1-100)', variable=self.difficulty_var, value='100')
        
        self.easy_button.pack()
        self.medium_button.pack()
        self.hard_button.pack()
        
        self.start_button = tk.Button(master, text='Начать игру', command=self.start_game)
        self.start_button.pack()
        self.message_label = tk.Label(master, text="")
        self.message_label.pack()
        
        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()
        
        self.check_button = tk.Button(master, text='Проверить', command=self.check_guess)
        self.check_button.pack()
        
        self.reset_button = tk.Button(master, text='Сыграть еще раз', command=self.reset_game)
        self.reset_button.pack()
        
        self.reset_game()

    def start_game(self):
        max_number = int(self.difficulty_var.get())
        self.random_number = random.randint(1, max_number)
        self.attempts = 0
        self.message_label.config(text=f"Я загадал число от 1 до {max_number}. Попробуйте угадать!")
    
    def check_guess(self):
        guess = int(self.guess_entry.get())
        self.attempts += 1
        
        if guess < self.random_number:
            self.message_label.config(text='Слишком мало! Попробуйте снова.')
        elif guess > self.random_number:
            self.message_label.config(text='Слишком много! Попробуйте снова.')
        else:
            self.message_label.config(text=f'Поздравляем! Вы угадали число {self.random_number} за {self.attempts} попыток.')

    def reset_game(self):
        self.message_label.config(text="")
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumber(root)
    root.mainloop()
