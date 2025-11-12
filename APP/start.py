# 1. Импортируем нужные библиотеки
import requests
from bs4 import BeautifulSoup


url = 'https://quotes.toscrape.com/'
response = requests.get(url)

print("Статус ответа:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# Находим все блоки с тегами
tags_containers = soup.find_all(class_='col-md-8')

# Создаем пустой список для хранения всех тегов
all_tags = []

# Проходим по каждому контейнеру тегов
for container in tags_containers:
    # В каждом контейнере находим все отдельные теги
    tags_in_container = container.find_all(class_='quote')
    
    for tag in tags_in_container:
        # Добавляем каждый тег в наш список
        all_tags.append(tag.text)

# Выводим результат
print("Все теги на странице:", all_tags)
print("Количество найденных тегов:", len( tags_in_container))