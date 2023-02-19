#  Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

list_0 = [random.randint(1, 30) for i in range(10)]
res = []
the_range = [int(input()) for _ in range(2)]
print(list_0)

if the_range[1] > len(list_0):
    print('the numbers that ware put by you are out of renge ')
elif the_range[0] + 1 >= the_range[1]:
    print("the range doesn't have numbers between ")
else:
    for i in range(the_range[1] - the_range[0]):
        res.append(list_0[the_range[0] + i])
    print(res)


