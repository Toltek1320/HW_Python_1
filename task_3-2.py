# Задача 18: Требуется найти в массиве A самый близкий по величине элемент к заданному числу X. 
# Если таких элементов несколько, вы вывести один любой. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых 
# чисел Ai (можно использовать псевдогенерацию). Последняя строка содержит число X
# *Пример:*
# 5
#     7 -2 3 5 1
#     6
#     -> 7
from random import randint
input_m = [randint(-99, 99) for i in range(int(input('Введите кол-во элементов в массиве: ')))]
print(input_m)
n = int(input('Введите искомое число: '))
input_m = set(input_m)
dif = 0
if n > max(input_m):
    print(max(input_m))
elif n < min(input_m):
    print(min(input_m))
else:
    while True:
        if n - dif in input_m and n + dif in input_m and n - dif != n + dif:
            print(n - dif, n + dif)
            break
        elif n - dif in input_m:
            print(n - dif)
            break
        elif n + dif in input_m:
            print(n + dif)
            break
        else:
            dif += 1