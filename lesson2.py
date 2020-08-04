# task 1
# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = []
some_list.append('car')
some_list.append(99)
some_list.append(99.9)
some_list.append(True)
some_list.append(None)
some_list.append(0)
some_list.append(' ')

for i in some_list:
    print(type(i))

# The end

# task 2
# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

a = input('Enter the required number of list items separated by a space: ').split()
i = 0
print(f'Original list {a}')
while i + 1 < len(a):
    if i % 2 ==0:
        a.insert(i, a.pop(i + 1))
    i += 1
    print(f'modified list {a}')

# the end

# task 3
# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
# var. 1 (list)

winter = ['1', '2', '12']
spring = ['3', '4', '5']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']

month = input('Enter the ordinal number of the month: ')

if month in winter:
    print('The winter')
elif month in spring:
    print('The spring')
elif month in summer:
    print('The summer')
elif month in autumn:
    print('The autumn')
else:
    print('The month number is entered incorrectly. Try again')

# var. 2 (dict)

seasons = {1:'winter', 2:'winter', 12:'winter',
           3:'spring', 4:'spring', 5:'spring',
           6:'summer', 7:'summer', 8:'summer',
           9:'autumn', 10:'autumn', 11:'autumn'}
month = int(input('Enter the ordinal number of the month: '))

if 1 <= month <= 12:
    print(seasons.get(month))
else:
    print('The month number is entered incorrectly. Try again')

# the end

# task 4
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

words = input('Please enter any few words separated by a space: ').split()

for number, word in enumerate(words, 1):
    print(number, word) if len(word) <= 10 else print(number, (word[:10]))

# The end

# task 5
# 5. Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
new_number = int(input('Please enter a new rating item: '))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)

# the end


# task 6
# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []
features = {'name': '', 'price': '', 'quantity': '', 'unit of measurement': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit of measurement': []}
num = 0
while True:
    if input('Press "E" to exit the application, "Enter" to continue: ').upper() =='E':
        break
    num += 1
    for f in features.keys():
        _ = input(f'Enter property value "{f}": ')
        features[f] = int(_) if (f == 'price' or f == 'quantity') else _
        analytics[f].append(features[f])
    products.append((num,features))
    print(f'\n Current analytics about the product: \n {"*" * 30}')
    for key, value in analytics.items():
        print(f'{key[:25]:>30}: {value}')
    print('*' * 30)

# the end