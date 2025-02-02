import requests
import webbrowser

def get_random_wikipedia_article():
    # Запрос к API Википедии для получения случайной статьи
    url = "https://en.wikipedia.org/wiki/Special:Random"
    return url

def main():
    while True:
        random_article_url = get_random_wikipedia_article()
        print("Случайная статья: ", random_article_url)
        
        user_input = input("Хотите открыть эту статью в браузере? (да/нет): ").strip().lower()
        
        if user_input in ['да', 'yes']:
            webbrowser.open(random_article_url)
        elif user_input in ['нет', 'no']:
            print("Хорошо, давайте попробуем снова.")
        else:
            print("Неверный ввод. Пожалуйста, введите 'да' или 'нет'.")
        
        another = input("Хотите получить другую статью? (да/нет): ").strip().lower()
        if another not in ['да', 'yes']:
            print("Спасибо за использование приложения!")
            break

if __name__ == "__main__":
    main()
