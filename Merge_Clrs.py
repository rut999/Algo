import math

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
    w = 0
    list_1 = []
    L_half.append(math.inf)
    R_half.append(math.inf)
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
