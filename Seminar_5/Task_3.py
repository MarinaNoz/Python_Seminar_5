# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце:

from functools import reduce



lst_length = []
with open("programm_language.txt", "r") as data:
    lst_length = data.read().splitlines()

lst_numbers = list(range(1, len(lst_length) + 1))

#print(lst_numbers)

def create_tuple(lst1, lst2):
    lst2 = [x.upper() for x in lst2]
    lst_tuple = list(zip(lst1, [x.upper() for x in lst2])) 
    return lst_tuple

lst_tuple = (create_tuple(lst_numbers, lst_length))
#print(lst_tuple)


def filter_list_tuple(lst_tuple):
    result_list = []
    result = 0
    for number, lenguage in lst_tuple[ : : ]:
        point = reduce(lambda a, b: a+b, [ord(char) for char in lenguage])
        if point % number == 0:
            result += point
            result_list.append((point, lenguage))
    del lst_tuple
    return result_list

print(filter_list_tuple(lst_tuple))


