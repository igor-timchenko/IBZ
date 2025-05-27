# Импорт модуля для создания тестов (базовый класс TestCase)
import unittest  

# Импорт инструментов для мокирования объектов (замены реальных зависимостей)
from unittest.mock import patch, MagicMock  

# Импорт библиотеки для создания графического интерфейса (тестируемое приложение использует Tkinter)
import tkinter as tk  

# Импорт тестируемого класса из основного файла приложения
from guess_the_number_app import GuessTheNumberApp  

# Объявление тестового класса, наследующегося от TestCase (обязательно для unittest)
class TestGuessTheNumberApp(unittest.TestCase):

    # Метод, который выполняется ПЕРЕД КАЖДЫМ тестом для подготовки окружения
    def setUp(self):
        # Создание главного окна Tkinter (необходимо для работы виджетов)
        self.root = tk.Tk()  
        # Создание экземпляра тестируемого приложения, передача окна в конструктор
        self.app = GuessTheNumberApp(self.root)  
        # Принудительное обновление интерфейса (чтобы виджеты стали доступны для тестирования)
        self.root.update()  

    # Метод, который выполняется ПОСЛЕ КАЖДОГО теста для очистки ресурсов
    def tearDown(self):
        # Уничтожение окна Tkinter (предотвращение утечек памяти)
        self.root.destroy()  

    # Тест №1: Проверка начального состояния приложения после инициализации
    def test_initial_state(self):
        # Проверка, что уровень сложности не выбран (значение None)
        self.assertIsNone(self.app.difficulty)  
        # Проверка, что загаданное число отсутствует
        self.assertIsNone(self.app.secret_number)  
        # Проверка, что счетчик попыток равен 0
        self.assertEqual(self.app.attempts, 0)  
        # Проверка, что максимальное число попыток не установлено
        self.assertEqual(self.app.max_attempts, 0)  
        # Проверка, что текст в метке подсказки пустой
        self.assertEqual(self.app.guess_label['text'], "")  

    # Тест №2: Проверка запуска игры на легком уровне сложности
    @patch('random.randint')  # Замена функции random.randint на mock-объект
    def test_start_game_easy(self, mock_randint):
        # Устанавливаем возвращаемое значение для мокированного random.randint
        mock_randint.return_value = 7  
        # Вызов метода start_game с параметрами: уровень 1, 5 попыток
        self.app.start_game(1, 5)  
        # Проверка, что уровень сложности установлен правильно
        self.assertEqual(self.app.difficulty, 1)  
        # Проверка, что загаданное число соответствует мокированному значению
        self.assertEqual(self.app.secret_number, 7)  
        # Проверка установки максимального числа попыток
        self.assertEqual(self.app.max_attempts, 5)  
        # Проверка, что счетчик попыток сброшен
        self.assertEqual(self.app.attempts, 0)  
        # Проверка, что текст подсказки содержит правильный диапазон
        self.assertIn("от 1 до 10", self.app.guess_label['text'])  

    # Тест №3: Проверка обработки некорректного ввода (два сценария в одном тесте)
    @patch('tkinter.messagebox.showwarning')  # Мокирование диалогового окна
    def test_invalid_input_handling(self, mock_showwarning):
        # Запуск игры для активации проверок
        self.app.start_game(1, 5)  
        # Эмуляция ввода текста 'invalid' в поле ввода
        self.app.guess_entry.insert(0, 'invalid')  
        # Вызов метода проверки предположения
        self.app.check_guess()  
        # Проверка, что showwarning вызван с правильными аргументами
        mock_showwarning.assert_called_with("Ошибка", "Пожалуйста, введите целое число.")  

        # Очистка поля ввода (от 0 до конца)
        self.app.guess_entry.delete(0, 'end')  
        # Эмуляция ввода числа 15 (вне диапазона для уровня 1)
        self.app.guess_entry.insert(0, '15')  
        # Повторный вызов проверки
        self.app.check_guess()  
        # Проверка сообщения для числа вне диапазона
        mock_showwarning.assert_called_with("Ошибка", "Пожалуйста, введите число в диапазоне от 1 до 10.")  

    # Тест №4: Проверка полного цикла угадывания (три попытки)
    @patch('tkinter.messagebox.showinfo')  # Мокирование информационных сообщений
    def test_game_flow(self, mock_showinfo):
        # Запуск игры с 3 попытками
        self.app.start_game(1, 3)  
        # Принудительная установка загаданного числа (для предсказуемости теста)
        self.app.secret_number = 5  

        # Попытка 1: Ввод числа 3 (меньше загаданного)
        self.app.guess_entry.insert(0, '3')  
        self.app.check_guess()  
        # Проверка сообщения "Слишком низко"
        mock_showinfo.assert_called_with("Результат", "Слишком низко! Осталось попыток: 2.")  
        # Проверка счетчика попыток
        self.assertEqual(self.app.attempts, 1)  

        # Попытка 2: Ввод числа 7 (больше загаданного)
        self.app.guess_entry.delete(0, 'end')  
        self.app.guess_entry.insert(0, '7')  
        self.app.check_guess()  
        # Проверка сообщения "Слишком высоко"
        mock_showinfo.assert_called_with("Результат", "Слишком высоко! Осталось попыток: 1.")  
        self.assertEqual(self.app.attempts, 2)  

        # Попытка 3: Ввод правильного числа 5
        self.app.guess_entry.delete(0, 'end')  
        self.app.guess_entry.insert(0, '5')  
        self.app.check_guess()  
        # Проверка сообщения об успехе
        mock_showinfo.assert_called_with("Поздравляю!", "Вы угадали число 5 за 3 попытки!")  
        # Проверка, что игра сброшена (secret_number = None)
        self.assertIsNone(self.app.secret_number)  

    # Тест №5: Проверка завершения игры при исчерпании попыток
    @patch('tkinter.messagebox.showinfo')  
    def test_game_over(self, mock_showinfo):
        # Запуск игры с 2 попытками
        self.app.start_game(1, 2)  
        self.app.secret_number = 5  

        # Попытка 1: Ввод 1
        self.app.guess_entry.insert(0, '1')  
        self.app.check_guess()  

        # Попытка 2: Ввод 2
        self.app.guess_entry.delete(0, 'end')  
        self.app.guess_entry.insert(0, '2')  
        self.app.check_guess()  

        # Проверка финального сообщения
        mock_showinfo.assert_called_with(
            "Игра окончена", 
            "Вы исчерпали все попытки! Загаданное число было 5."
        )  
        # Проверка сброса игры
        self.assertIsNone(self.app.secret_number)  

    # Тест №6: Проверка сброса состояния игры
    def test_reset_game(self):
        # Запуск игры с параметрами
        self.app.start_game(2, 7)  
        # Вызов метода сброса
        self.app.reset_game()  

        # Проверка, что все параметры вернулись в исходное состояние
        self.assertIsNone(self.app.difficulty)  
        self.assertIsNone(self.app.secret_number)  
        self.assertEqual(self.app.attempts, 0)  
        self.assertEqual(self.app.max_attempts, 0)  

# Стандартная проверка для запуска тестов при выполнении файла
if __name__ == '__main__':
    unittest.main()  # Запуск всех тестов, объявленных в классе
