import tkinter as tk # Импортируем библиотеку tkinter для создания графического интерфейса
from tkinter import messagebox # Импортируем модуль для отображения диалоговых окон
import random # Импортируем модуль random для генерации случайных чисел

# Приложение "Угадай число"
class GuessTheNumberApp:
    # Функция - инициализация главного окна приложения
    def __init__(self, master):
        
        self.master = master # Сохраняем ссылку на главное окно
        master.title("Угадай число") # Устанавливаем заголовок окна 

        # Переменные для хранения состояния игры
        self.difficulty = None # Уровень сложности (пока не установлен) 
        self.secret_number = None # Загаданное число (пока не установлено) 
        self.attempts = 0 # Счетчик попыток (начинается с нуля)
        self.max_attempts = 0 # Максимальное количество попыток (пока не установлено)

        # Метка для выбора уровня сложности
        self.label = tk.Label(master, text="Выберите уровень сложности:") # Создаем метку с текстом
        self.label.pack() # Размещаем метку в окне

        # Кнопки для выбора уровня сложности с соответствующим количеством попыток
        self.easy_button = tk.Button(master, text="Легкий (1-10, 5 попыток)", command=lambda: self.start_game(1, 5)) # Кнопка для легкого уровня 
        self.easy_button.pack() # Размещаем кнопку в окне

        self.medium_button = tk.Button(master, text="Средний (1-50, 7 попыток)", command=lambda: self.start_game(2, 7)) # Кнопка для среднего уровня 
        self.medium_button.pack() # Размещаем кнопку в окне

        self.hard_button = tk.Button(master, text="Сложный (1-100, 10 попыток)", command=lambda: self.start_game(3, 10)) # Кнопка для сложного уровня
        self.hard_button.pack() # Размещаем кнопку в окне

        # Метка для отображения подсказок по игре
        self.guess_label = tk.Label(master, text="") # Создаем пустую метку для подсказок
        self.guess_label.pack() # Размещаем метку в окне

        # Поле ввода для ввода предположения игрока
        self.guess_entry = tk.Entry(master) # Создаем поле ввода
        self.guess_entry.pack() # Размещаем поле ввода в окне

        # Кнопка для отправки предположения
        self.submit_button = tk.Button(master, text="Отправить", command=self.check_guess) # Создаем кнопку "Отправить"
        self.submit_button.pack() # Размещаем кнопку в окне 

    # Функция - начало новой игры с заданным уровнем сложности и количеством попыток
    def start_game(self, difficulty, max_attempts):
        
        self.difficulty = difficulty # Устанавливаем уровень сложности
        self.max_attempts = max_attempts # Устанавливаем максимальное количество попыток

        # Генерация загадочного числа в зависимости от уровня сложности
        if difficulty == 1:

            self.secret_number = random.randint(1, 10) # Генерируем случайное число от 1 до 10
            range_text = "от 1 до 10" # Текст диапазона для подсказки
            
        elif difficulty == 2:
            
            self.secret_number = random.randint(1, 50) # Генерируем случайное число от 1 до 50
            range_text = "от 1 до 50" # Текст диапазона для подсказки
            
        else:
            
            self.secret_number = random.randint(1, 100) # Генерируем случайное число от 1 до 100
            range_text = "от 1 до 100" # Текст диапазона для подсказки

        # Сброс счетчика попыток и обновление метки с подсказкой
        self.attempts = 0 # Сбрасываем счетчик попыток на ноль
        self.guess_label.config(text=f"Я загадал число {range_text}. У вас {max_attempts} попыток. Попробуйте угадать его!") # Обновляем текст метки с подсказкой о загаданном числе и количестве попыток

    # Функция - проверка предположения игрока
    def check_guess(self):

        try:
            guess = int(self.guess_entry.get()) # Получаем предположение из поля ввода и преобразуем его в целое число

            # Проверка на допустимость введенного числа в зависимости от уровня сложности
            if (self.max_attempts == 5 and (guess < 1 or guess > 10)) or (self.max_attempts == 7 and (guess < 1 or guess > 50)) or (self.max_attempts == 10 and (guess < 1 or guess > 100)):
                messagebox.showwarning("Ошибка", f"Пожалуйста, введите число в диапазоне от {self.max_attempts == 5 and '1 до 10' or self.max_attempts == 7 and '1 до 50' or '1 до 100'}.")
                return # Выводим предупреждение и выходим из метода, если число вне диапазона

            self.attempts += 1 # Увеличиваем счетчик попыток на единицу

            # Проверка предположения и вывод соответствующего сообщения
            if guess < self.secret_number:
                remaining_attempts = self.max_attempts - self.attempts # Вычисляем оставшиеся попытки
                messagebox.showinfo("Результат", f"Слишком низко! Осталось попыток: {remaining_attempts}.")# Выводим сообщение о том, что число слишком низкое и сколько осталось попыток 
            elif guess > self.secret_number:
                remaining_attempts = self.max_attempts - self.attempts # Вычисляем оставшиеся попытки 
                messagebox.showinfo("Результат", f"Слишком высоко! Осталось попыток: {remaining_attempts}.") # Выводим сообщение о том, что число слишком высокое и сколько осталось попыток 
            else:
                # Поздравление игрока с победой и вывод количества попыток
                if self.attempts == 1:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попытку!")
                elif self.attempts == 2 or self.attempts == 3 or self.attempts == 4:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попытки!")
                else:
                    messagebox.showinfo("Поздравляю!", f"Вы угадали число {self.secret_number} за {self.attempts} попыток!")
                self.reset_game() # Сбрасываем игру после победы
                return
            
            # Проверка на окончание игры при исчерпании всех попыток
            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Игра окончена", f"Вы исчерпали все попытки! Загаданное число было {self.secret_number}.") # Выводим сообщение о том, что игра окончена и показываем загаданное число
                self.reset_game() # Сбрасываем игру после окончания

        # Обработка случая, когда введено не целое число      
        except ValueError:
            messagebox.showwarning("Ошибка", "Пожалуйста, введите целое число.") # Выводим предупреждение об ошибке ввода

    # Функция - сброс переменных состояния игры
    def reset_game(self):
        
        self.difficulty = None # Сбрасываем уровень сложности
        self.secret_number = None # Сбрасываем загаданное число
        self.attempts = 0 # Сбрасываем счетчик попыток на ноль
        self.max_attempts = 0 # Сбрасываем максимальное количество попыток на ноль

# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk() # Создаем главное окно приложения
    app = GuessTheNumberApp(root) # Создаем экземпляр нашего приложения
    root.mainloop() # Запускаем главный цикл обработки событий приложения
