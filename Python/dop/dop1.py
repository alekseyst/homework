import re
from math import log
import os # собираем тексты, раскладываем их по категориям

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'

def preprocessing(text): # функция предобработки текста
    text_wo_punct = re.sub(punct, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    words = text_wo_punct.strip().split() # делим по пробелам
    return words

anek = ''
teh = ''
izvest = ''
for root, dirs, files in os.walk('texts'):
    for f in files:
        if 'anekdots' in root:
            num_anek = len(files)
            anek += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'izvest' in root:
            num_izvest = len(files)
            izvest += open(os.path.join(root, f), encoding='utf-8').read()
        elif 'teh_mol' in root:
            num_teh = len(files)
            teh += open(os.path.join(root, f), encoding='utf-8').read()
            
words_anek = preprocessing(anek) # пропроцессинг
words_teh = preprocessing(teh)
words_izvest = preprocessing(izvest)

words = words_anek + words_teh + words_izvest # в массиве words - весь наш корпус


def freq_dict(arr): # функция создания частотного словаря
    dic = {}
    for element in arr:
        if (element in dic) and (len(element)> 3): # отсекаем слова меньше четырех букв
            dic[element] += 1
        elif len(element)> 3:
            dic[element] = 1
    return dic

def delete (dic): # убираем нечастотные
    dic1=dic.copy()
    for word in dic1:
        if dic1[word] == 1:
           del dic[word]
    return dic

corpus_freq = freq_dict(words) # считаем частотные словари для каждой категории в отдельности и для всего корпуса
anek_freq = freq_dict(words_anek)
izvest_freq = freq_dict(words_izvest)
teh_freq = freq_dict(words_teh)

delete (corpus_freq) # убираем из них нечастотные
delete(anek_freq)
delete(izvest_freq)
delete(teh_freq)

def pmi_for_cats(x, y): # вычисляем pmi для слова и категории
    if y == 'anek': # определяем, что за категория нам требуется, задаем её переменные (массив слов, число текстов)
        dic = anek_freq
        arr = words_teh + words_izvest
        num = num_anek
    elif y == 'teh':
        dic = teh_freq
        arr = words_anek + words_izvest
        num = num_teh
    elif y == 'izvest':
        dic = izvest_freq
        arr = words_teh + words_anek
        num = num_izvest
    p_xy = dic[x]/len(arr) # вероятность появления слова x в текстах категории y: частота этого слова на общ. кол-во слов
    p_x, p_y = corpus_freq[x]/len(words), num/(num_izvest + num_teh + num_anek) # вероятность появления слова в корпусе
    pmi = log(p_xy/(p_x * p_y))                                                 # и вероятность категории
    return pmi


cat_pmi = {}
i = 0
for word in corpus_freq: # для каждого слова вычисляем его PMI для всех категорий
    if i > 100:
        break
    try:
        pmi_anek = pmi_for_cats(word, 'anek') # интересующую нас категорию задаем вторым аргументов функции
    except KeyError: # не во всех категориях может встретиться это слово. "Глобализации" не будет в анекдотах...
        pmi_anek = 0
    try:
        pmi_teh = pmi_for_cats(word, 'teh')
    except KeyError:
        pmi_teh = 0
    try:
        pmi_izvest = pmi_for_cats(word, 'izvest')
    except KeyError:
        pmi_izvest = 0
    max_pmi = max(pmi_anek, pmi_teh, pmi_izvest) # выбираем максиальный коэффициент PMI
    if max_pmi == 0:
        continue
    if max_pmi == pmi_anek: # находим соответствующую этому коэффициенту категорию
        cat = 'anek'
    elif max_pmi == pmi_teh:
        cat = 'teh'
    elif max_pmi == pmi_izvest:
        cat = 'izvest'
    print(word, cat) 
    i += 1


