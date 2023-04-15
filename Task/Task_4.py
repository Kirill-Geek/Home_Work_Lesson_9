"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
list_txt = ['разработка', 'администрирование', 'protocol',
            'standard']
new_list = []
for i in list_txt:
    res = i.encode('utf-8')
    print(res)
    new_res = res.decode('utf-8')
    new_list.append(new_res)
print(new_list)
