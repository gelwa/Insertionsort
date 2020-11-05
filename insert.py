
def insertsort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a


def insertrev(a):  #umgekehrt
    for j in range(1, len(a)):
        key = a[j]
        i = j-1
        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i = i-1
        a[i+1] = key
    return a


lists = [[10,9,8,7,6,5,4,3,2,1], [1,2,3,4,5,6,7,8,9,10], [4,6,7,1,14,16,9,8,2]]


for l in lists:
    print("To be sorted:", l)
    print(insertsort(list(l)))
    print(insertrev(list(l)))
    print()



