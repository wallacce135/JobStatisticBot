import requests
import json
import os
import time


with open('jobsList.json', 'r', encoding='utf-8') as f:
    text = json.load(f)
    # print(text)

def getPage(jobName):
    params = {
        'text': jobName,
        'area': 2,
        'page': 1,
        'per_page': 30
        }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    return data


def pageProccessing(jobName):

    for page in range(0, 1):
        jsonObj = json.loads(getPage(jobName=jobName))

        fileName = 'C:/Users/Pechka/Desktop/JobStatisticsBot/{}.json'.format(
            len(os.listdir('C:/Users/Pechka/Desktop/JobStatisticsBot/pagination')))

        f = open(fileName, mode='w', encoding='utf-8')
        f.write(json.dumps(jsonObj, ensure_ascii=False))
        f.close()

        time.sleep(0.25)

for i in text['jobList']:
    pageProccessing(i)




# with open('0.json', 'r', encoding='utf-8') as f:
#     allData = json.load(f)
#     # print(allData)
#     for i in range(0, 1000000):
#         try:
#             name = allData['items'][i]['name']
#             print(name)
#         except IndexError:
#             break