from cmath import nan
import pandas as pd
import numpy as np
import math

dataset = pd.read_csv(
    'hope - Copy6.csv',
)
print(dataset['Частота процессора'])
processorToHertz = {}
processorToCores = {}
for index, row in dataset.iterrows():
    processor = row['Процессор']
    hertz = row['Частота процессора']
    cores = row['Количество ядер']
    if (not pd.isna(processor)):
        if (not pd.isna(hertz)):
            processorToHertz[processor] = hertz
        if (not pd.isna(cores)):
            processorToCores[processor] = cores
# print(processorToHertz)
# print(processorToCores)
for index, row in dataset.iterrows():
    processor = row['Процессор']
    hertz = row['Частота процессора']
    cores = row['Количество ядер']
    if (not pd.isna(processor)):
        if (pd.isna(hertz)):
            dataset['Частота процессора'][index] = processorToHertz[processor]
        if (pd.isna(cores)):
            dataset['Количество ядер'][index] = processorToCores[processor]
    isApple = row['Бренд'] == 'Apple' or row['ОС'] == 'Mac OS'
    if (isApple):
        dataset['Бренд'][index] = 'Apple'
    else:
        dataset['Бренд'][index] = 'NotApple'
    gpu = row['Видеокарта']
    is_integrated_gpu = gpu == 'Другая видеокарта' or pd.isna(gpu)
    if (is_integrated_gpu):
        dataset['Видеокарта'][index] = 'integrated'
print(dataset['Частота процессора'])
dataset.to_csv('cleaned-dataset.csv', encoding='utf-8-sig', index=False)
