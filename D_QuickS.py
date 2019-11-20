import time
from random import randint


def random_int(x):
    value = []
    for i in range(x):
        value.append(randint(0, x))
    return value
def Quick_sort(list1):
    N = len(list1)
    if N <=1:
        return list1
    pivot = list1.pop()
    # mid = len(list1)//2
    Left_H = []
    Right_H = []
    for i in range(len(list1)):
        if(list1[i]>pivot):
            Right_H.append(list1[i])
        else:
            Left_H.append(list1[i])
    return (Quick_sort(Left_H)+[pivot]+Quick_sort(Right_H))

random_list = random_int(100000)
#list2 = [0,0,99,34,56,54,-1,-1,32,2.5,-1.1,1000,1000,-2,30,21,24,15,10,6]
t1 = time.time()
Quick_sort(random_list)
t2 = time.time()
print(t2-t1)


# def Quick_Sort(list1):
#     if (list1[0]<list1[-1]):
#         partition_index =partition(list1)
#         quicksort(list1,)
#         quicksort()
