"""Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных
(https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество
животных на каждую букву алфавита. Содержимое результирующего файла:"""


import requests
from bs4 import BeautifulSoup
import csv


def get_animal_count_by_letter():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    response = requests.get(url)
    response.raise_for_status()  # Проверка статуса ответа
    soup = BeautifulSoup(response.content, "html.parser")
    animals = {}
    for link in soup.find_all("a", href=lambda href: href and href.startswith("/wiki/")):
        animal_name = link.text.strip()
        first_letter = animal_name[0].upper()
        if first_letter in animals:
            animals[first_letter] += 1
        else:
            animals[first_letter] = 1

    with open("beasts.csv", "w", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Буква", "Количество"])
        for letter, count in animals.items():
            writer.writerow([letter, count])


if __name__ == "__main__":
get_animal_count_by_letter()