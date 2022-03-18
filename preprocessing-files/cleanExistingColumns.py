from difflib import SequenceMatcher
from cmath import nan
import pandas as pd
import numpy as np
import math
import re


def removeNonNumericCharacters(inputStr):
    if (type(inputStr) == str):
        return re.sub('[^0-9.]', '', inputStr)
    return inputStr


def cleanHertz(hertzStr):
    if(type(hertzStr) == str):
        if ('-' in hertzStr):
            firstPart, secondPart = hertzStr.split('-')
            minHertz = float(removeNonNumericCharacters(firstPart))
            maxHertz = float(removeNonNumericCharacters(secondPart))
            return (minHertz + maxHertz) / 2
        if ('До' in hertzStr):
            maxHertz = float(removeNonNumericCharacters(hertzStr))
            return maxHertz - 0.2
        if ('Более' in hertzStr):
            minHertz = float(removeNonNumericCharacters(hertzStr))
            return minHertz + 0.2
    else:
        return hertzStr
    raise 'unexpected hertz'


def cleanPrice(priceStr):
    priceNum = 0
    if ('USD' in priceStr):
        priceNum = float(removeNonNumericCharacters(priceStr)) * 104
    else:
        priceNum = float(removeNonNumericCharacters(priceStr))
    return priceNum


def cleanDiskSize(sizeStr):
    if(type(sizeStr) == str):
        if ('ТБ' in sizeStr):
            return int(removeNonNumericCharacters(sizeStr)) * 1000
    return int(removeNonNumericCharacters(sizeStr))


dataset = pd.read_csv(
    'cleaned-dataset.csv',
)
dataset['Оперативная память (ГБ)'] = dataset['Оперативная память (ГБ)'].str.extract(
    '(\d+)', expand=False)

for index, row in dataset.iterrows():
    hertz = row['Частота процессора']
    cores = row['Количество ядер']
    diskSize = row['Объем накопителя']
    price = row['Price']
    dataset['Частота процессора'][index] = cleanHertz(hertz)
    dataset['Количество ядер'][index] = removeNonNumericCharacters(cores)
    dataset['Объем накопителя'][index] = cleanDiskSize(diskSize)
    dataset['Price'][index] = cleanPrice(price)


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


gpudf = pd.read_csv('GPU_UserBenchmarks.csv')


def findBenchmarkOfGpu(gpuName):
    if (gpuName == 'integrated'):
        return 4.7
    bestSimilarityRatio = 0
    benchmarkOfBestSimilar = 0
    for index, row in gpudf.iterrows():
        similarityRatio = similar(row['Brand'] + ' ' + row['Model'], gpuName)
        if (similarityRatio > bestSimilarityRatio and removeNonNumericCharacters(row['Model']) == removeNonNumericCharacters(gpuName)):
            bestSimilarityRatio = similarityRatio
            benchmarkOfBestSimilar = row['Benchmark']
    if (benchmarkOfBestSimilar == 0):
        return 4.7
    else:
        return benchmarkOfBestSimilar


for index, row in dataset.iterrows():
    dataset['Видеокарта'][index] = findBenchmarkOfGpu(row['Видеокарта'])


dataset.to_csv('cleaned-dataset2.csv', encoding='utf-8-sig', index=False)
