import math
import sys

#sys.setrecursionlimit(10)
import time
from random import randint, random


def random_int(x):
    value = []
    for i in range(x):
        value.append(randint(0, x))
    return value

def Merge_sort(list_1):
    N = len(list_1)
    if N < 2:
        return list_1
    mid = N//2
    L_half = Merge_sort(list_1[:mid])
    R_half = Merge_sort(list_1[mid:])
    return merge(L_half,R_half)

def merge(L_half,R_half):
    i = 0
    j = 0
    list_1 = []
    #L_half.append(math.inf)
    #R_half.append(math.inf)
    while i < len(L_half) and j < len(R_half):
        if L_half[i] < R_half[j]:
            list_1.append(L_half[i])
            i += 1
        else:
            list_1.append(R_half[j])
            j += 1
    list_1 +=L_half[i:]
    list_1 +=R_half[j:]
    return list_1




#list = ([54, 26, 93, 17, 77, 31, 44, 55, 20])
#xyz = []
#xyz = Merge_sort(list)
#print(xyz)
random_list = random_int(100000)
# calculate time for Insertion Sort
#random.shuffle(random_list)
t1 = time.time()
z = Merge_sort(random_list)
print(z)
print("The list len ",len(z))
t2 = time.time()
time_merge = []
time_merge.append(t2-t1)
print(time_merge)
