"""
Написать функцию, которая используя модуль requests скачивает файл сохраняет его на файловой системе, функция имеет
два параметра: ссылка на файл и имя на файловой системе. В качестве примера ссылки на файл можно использовать лицензию
из ГитХаба из вашего репозитория: https://raw.githubusercontent.com/manti-by/lessons/master/LICENSE
"""
import requests
import os


def get_content(url, file_name):
    req = requests.get(url)  # получаем веб-страницу
    path = os.path.expanduser('~')  # путь к текущему пользователю

    # сохраняем файл на рабочий стол с расширением ".txt"
    with open(f"{path}/Рабочий стол/{file_name}.txt", "wb") as file:
        file.write(req.content)


if __name__ == "__main__":
    get_content("https://raw.githubusercontent.com/DedRobin/lessons/master/LICENSE", "content")
