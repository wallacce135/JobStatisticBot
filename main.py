import requests
import json
import os
import time


with open('jobsList.json', 'r', encoding='utf-8') as file:
    listOfJobs = json.load(file)


def getData(vacancyName):

    params = {
        'text': vacancyName,
        'area': 2,
        'page': 0,
        'per_page': 5
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()

    # Запись полученного с API резльтата
    with open('result.json', 'w', encoding='utf-8') as file:
        file.write(data)

    # Чтение названия из вакансий по профессии

    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0,100000000):
            try:
                print(data['items'][i]['name'])
            except IndexError:
                break


# Открытие файла с профессиями для чтения
with open('jobsList.json', 'r', encoding='utf-8') as file:
    values = json.load(file)
    jobList = values['jobList']
    print(jobList)

# Вызов функции для каждой профессии

for vacancy in jobList:
    getData(vacancy)






# with open('result.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for i in range(0, 100000):
#         try:
#             name = data['items'][i]['name']
#             print(name)
#         except IndexError:
#             break
