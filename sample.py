from matplotlib import pyplot as plt
import time
from random import randint, sample
import copy
import sys
sys.setrecursionlimit(10**9)
"""
function :Sorted numbers using Insertion Sort
input    :Array
Output   :Sorted Array
"""
def insertion_sort(arr):
     n = len(arr)
     for i in range(1,n):
          key = arr[i]
          j=i-1
          while j>=0 and key<arr[j]:
               arr[j+1]=arr[j]
               j= j-1
          arr[j+1] = key
     return(arr)
"""
function : Merge Sort
input    :Unsorted List
"""
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
"""
function :Deterministic QuickSort
"""
#Used the Psuedo Code From CLRS
def Quick_Sort(list1,c,v):
    if c<v:
        q = partition(list1,c,v)
        Quick_Sort(list1,c,q-1)
        Quick_Sort(list1,q+1,v)

def partition(list,k,l):
    x = list[l]
    i = k-1
    for j in range(k,l):
        if list[j]<=x:
            i+=1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[l] = list[l],list[i+1]
    return i+1
"""
function : Generate Random Numbers
"""
def random_int(x):
    value = []
    for i in range(x):
        value.append(randint(1, x+1))
    return value
"""
function :Graph Plotting 
input    :Insertion Sort Time ,Merge Sort Time , Quick Sort Time
Output   :Insertion Sort vs Merge Sort vs Quick Sort Graph 
"""
def graph_plot(z,w,k):
     x = [5000, 10000, 15000, 20000, 25000, 30000]
     y1 = z
     y2 = w
     y3 = k
     plt.title('Insertion Sort Vs Merge Sort Vs Quick Sort')
     plt.ylabel('time to sort')
     plt.xlabel('input number')
     plt.plot(x, y1, '-b', x, y2, '-g',x, y3,'-r')
     plt.gca().legend(('Insertion Sort', 'Merge Sort','Quick Sort'))
     plt.show()
"""
 Input/Plot 1: Large random inputs
"""
time_plot_insert = []
time_plot_merge = []
time_plot_quickS = []
time_insert = []
time_merge = []
time_QuickS = []
for x in range(5000, 31000, 5000):
     for y in range(3):
          random_list = random_int(x)
          random_list1 = copy.deepcopy(random_list)
          random_list3 = copy.deepcopy(random_list)
          # calculate time for Insertion Sort
          t1 = time.time()
          insertion_sort(random_list)
          t2 = time.time()

          time_insert.append(t2-t1)
          #calculate time for Merge Sort
          t3 = time.time()
          Merge_sort(random_list1)
          t4 = time.time()

          time_merge.append(t4-t3)
          #calculate time for Quick Sort
          t5 = time.time()
          Quick_Sort(random_list3,0,len(random_list3)-1)
          t6 = time.time()

          time_QuickS.append(t6-t5)
     time_plot_insert.append((sum(time_insert))/3)
     time_plot_merge.append((sum(time_merge))/3)
     time_plot_quickS.append((sum(time_QuickS))/3)
#plotting graph using insertion sort ,Merge sort & Quick Sort times.
graph_plot(time_plot_insert,time_plot_merge,time_plot_quickS)
"""
Input/Plot 2:  Non-decreasing inputs
"""
time_insert = []
time_merge = []
time_QuickS = []
count = 0
for x in range(5000, 31000, 5000):
     count+=1
     print(count)
     random_list = random_int(x)
     sort_random_list = sorted(random_list)
     sort_random_list2 = copy.deepcopy(sort_random_list)
     sort_random_list3 = copy.deepcopy(sort_random_list)
     #calculate time for insertion sort
     t1 = time.time()
     insertion_sort(sort_random_list)
     t2 = time.time()
     time_insert.append(t2-t1)
     #calculate time for merge sort
     t3 = time.time()
     Merge_sort(sort_random_list2)
     t4 = time.time()
     time_merge.append(t4-t3)
     #calculate time for Quick Sort
     t5 = time.time()
     Quick_Sort(sort_random_list3, 0, len(sort_random_list3) - 1)
     t6 = time.time()
     time_QuickS.append(t6-t5)
#plotting graph using insertion sort & selection sort performance
graph_plot(time_insert,time_merge,time_QuickS)
"""
Input/Plot 3: Non-increasing inputs
"""
time_insert = []
time_merge = []
time_QuickS = []
for x in range(5000, 31000, 5000):
     random_list = random_int(x)
     sort_random_list = sorted(random_list,reverse=True)
     sort_random_list2 = copy.deepcopy(sort_random_list)
     sort_random_list3 = copy.deepcopy(sort_random_list)
     # calculate time for insertion sort
     t1 = time.time()
     insertion_sort(sort_random_list)
     t2 = time.time()
     time_insert.append(t2-t1)
     #calculate time for Merge sort
     t3 = time.time()
     Merge_sort(sort_random_list2)
     t4 = time.time()
     time_merge.append(t4-t3)
     #calculate time for quick Sort
     t5 = time.time()
     Quick_Sort(sort_random_list3, 0, len(sort_random_list3) - 1)
     t6 = time.time()
     time_QuickS.append(t6 - t5)
     # plotting graph using insertion sort & selection sort times.
graph_plot(time_insert, time_merge,time_QuickS)

"""
Input/Plot 4: Noisy non-decreasing inputs
"""
time_plot_insert = []
time_plot_merge = []
time_plot_QuickS = []
time_insert = []
time_merge = []
sort_random_list1 = []
time_QuickS = []
for x in range(5000, 31000, 5000):
     random_list = random_int(x)
     sort_random_list = sorted(random_list)
     for i in range(50):
          l,m = sample(list(range(0,len(sort_random_list))),2)
          sort_random_list[l], sort_random_list[m] = sort_random_list[m], sort_random_list[l]
     sort_random_list2 = copy.deepcopy(sort_random_list)
     sort_random_list3 = copy.deepcopy(sort_random_list)
     for j in range(3):
      #calculate time for Insertion Sort
          t1 = time.time()
          insertion_sort(sort_random_list)
          t2 = time.time()
          time_insert.append(t2-t1)
     #calculate time for Merge sort
          t3 = time.time()
          Merge_sort(sort_random_list2)
          t4 = time.time()
          time_merge.append(t4-t3)
     #calculate time for Quick Sort
          t5 = time.time()
          Quick_Sort(sort_random_list3, 0, len(sort_random_list3) - 1)
          t6 = time.time()
          time_QuickS.append(t6 - t5)
     time_plot_insert.append((sum(time_insert)) / 3)
     time_plot_merge.append((sum(time_merge)) / 3)
     time_plot_QuickS.append((sum(time_QuickS))/3)
#plotting graph using insertion sort & selection sort times.
graph_plot(time_plot_insert, time_plot_merge, time_plot_QuickS)

"""
Input 5: Small random inputs
"""
time_insert = 0
time_merge = 0
time_QuickS = 0
for i in range(100000):
     value = random_int(50)
     value2 = copy.deepcopy(value)
     value3 = copy.deepcopy(value)

     t1 = time.time()
     insertion_sort(value)
     t2 = time.time()
     time_insert+=(t2-t1)

     t3 = time.time()
     Merge_sort(value2)
     t4 = time.time()
     time_merge+=(t4-t3)

     t5 = time.time()
     Quick_Sort(value3, 0, len(value3)-1)
     t6 = time.time()
     time_QuickS+=(t6-t5)
print("Insertion Sort Time",time_insert)
print("Merge Sort Time",time_merge)
print("Quick Sort Time ",time_QuickS)









