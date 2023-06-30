import requests

# URL для получения списка всех книг
url = 'http://127.0.0.1:8000/api/books/'

# Выполнение GET-запроса для получения списка всех книг
response = requests.get(url)

# Проверка статуса ответа
if response.status_code == 200:
    books = response.json()  # Получение данных в формате JSON
    for book in books:
        print(f"Название: {book['title']}, Автор: {book['author']}")
else:
    print('Произошла ошибка при получении списка книг.')
