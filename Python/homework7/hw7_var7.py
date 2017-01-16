def questions():
    file = input('Введите название файла на английском: ')
    leng = int(input('Введите длину слова: '))
    quant = open_file(file)
    output = perc(quant, leng)
    return output

def open_file(file):
    f = open(file, 'r')
    file = f.read()
    file = file.split()
    return file

def perc(quant, leng):
    i = 0
    j = 0
    for item in quant:
        if item.startswith('un'):
            i += 1
            if len(item) > leng:
                j += 1
    if i != 0:
        print ('Количество слов, начинающихся с un-, в тексте: ', i)
        return round(j / i * 100)
    else:
        return 'В тексте нет слов, начинающихся на un-'

print('Проценты: ', questions())
