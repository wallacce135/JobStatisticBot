import requests
import json
import os
import time
import pandas as pd



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
        file.close()

    # Чтение названия из вакансий по профессии

    time.sleep(2)
    dataArr = {'Название': [], 'Зарплата(От)': [], 'Зарплата(До)': [], 'График': [], 'Ссылка': []}
    with open('result.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, 5):

            # print(i)
            name = data['items'][i]['name']
            salaryFrom = data['items'][i]['salary']['from']
            salaryTo = data['items'][i]['salary']['to']
            schedule = data['items'][i]['schedule']['name']
            url = data['items'][i]['alternate_url']

            dataArr['Название'].append(name)
            dataArr['Зарплата(От)'].append(salaryFrom)
            dataArr['Зарплата(До)'].append(salaryTo)
            dataArr['График'].append(schedule)
            dataArr['Ссылка'].append(url)

    return dataArr


# Открытие файла с профессиями для чтения

with open('jobsList.json', 'r', encoding='utf-8') as file:
    values = json.load(file)
    jobList = values['jobList']
    print(jobList)

# Вызов функции для каждой профессии

fullData = {'Название': [], 'Зарплата(От)': [], 'Зарплата(До)': [], 'График': [], 'Ссылка': []}

for vacancy in jobList:
    data = getData(vacancy)
    fullData['Название'] = fullData['Название'] + [vacancy]
    fullData['Зарплата(От)'] = fullData['Зарплата(От)'] + [""]
    fullData['Зарплата(До)'] = fullData['Зарплата(До)'] + [""]
    fullData['График'] = fullData['График'] + [""]
    fullData['Ссылка'] = fullData['Ссылка'] + [""]


    fullData['Название'] = fullData['Название'] + data['Название']
    fullData['Зарплата(От)'] = fullData['Зарплата(От)'] + data['Зарплата(От)']
    fullData['Зарплата(До)'] = fullData['Зарплата(До)'] + data['Зарплата(До)']
    fullData['График'] = fullData['График'] + data['График']
    fullData['Ссылка'] = fullData['Ссылка'] + data['Ссылка']

df = pd.DataFrame(fullData)
df.to_excel('salary.xlsx', index=False)