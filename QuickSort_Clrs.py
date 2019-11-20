#Used the Psuedo Code From CLRS
def Quick_Sort(list1,p,r):
    if p<r:
        q = partition(list1,p,r)
        Quick_Sort(list1,p,q-1)
        Quick_Sort(list1,q+1,r)

def partition(list,p,r):
    x = list[r]
    i = p-1
    #j = r+1
    for j in range(p,r):
        if list[j]<=x:
            i+=1
            list[i],list[j] = list[j],list[i]
    list[i+1],list[r] = list[r],list[i+1]
    return i+1

items = [13,19,9,5,12,8,7,4,11,2,6,21]
Quick_Sort(items, 0, len(items)-1)
print(items)





