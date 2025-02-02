import time
import datetime
import pygame
from PIL import Image
import os

# Инициализация Pygame для воспроизведения звука
pygame.mixer.init()

def play_sound(sound_file):
    """Воспроизводит звук."""
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Ждем, пока музыка играет
        time.sleep(1)

def show_image(image_file):
    """Показывает изображение."""
    img = Image.open(image_file)
    img.show()

def set_alarm(alarm_time, sound_file=None, image_file=None):
    """Устанавливает будильник на заданное время."""
    print(f"Будильник установлен на {alarm_time}.")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Будильник сработал!")
            if sound_file:
                play_sound(sound_file)
            if image_file:
                show_image(image_file)
            break
        time.sleep(30)  # Проверяем время каждые 30 секунд

if __name__ == "__main__":
    # Установите время будильника в формате "HH:MM"
    alarm_time = input("Введите время будильника (в формате HH:MM): ")

    # Укажите путь к аудиофайлу и изображению (если необходимо)
    sound_file = input("Введите путь к аудиофайлу (или оставьте пустым): ")
    image_file = input("Введите путь к изображению (или оставьте пустым): ")

    # Проверка наличия файлов
    if sound_file and not os.path.isfile(sound_file):
        print("Аудиофайл не найден.")
        sound_file = None

    if image_file and not os.path.isfile(image_file):
        print("Изображение не найдено.")
        image_file = None

    set_alarm(alarm_time, sound_file, image_file)
