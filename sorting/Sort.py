import timeit

def bubbleSort(x):
    start_time = timeit.default_timer()
    for i in range(len(x)-1):
        for j in range(len(x)-1):
            if x[j]> x[j+1]:
                x[j], x[j + 1] = x[j+1],x[j]
    terminate_time = timeit.default_timer()
    terminate_time = terminate_time - start_time
    return x , terminate_time

def quickSort(x):
    if len(x) <= 1:
        return x
    pivot = x[len(x)//2]
    left,right,equal =[],[],[]
    for a in x:
        if a < pivot:
            left.append(a)
        elif a > pivot:
            right.append(a)
        else:
            equal.append(a)
            
    return quickSort(left) + equal + quickSort(right)




def insertionSort(x):
    for i in range(1,len(x)):
        j, key = i -1, x[i]
        while x[j] > key and j >= 0:
            x[j+1] = x[j]
            j = j - 1
        x[j+1] = key
    return x

def mergetSort(x):
    if len(x) <= 1:
        return x
    left = mergetSort(x[:len(x)//2])
    right = mergetSort(x[len(x)//2: ])

    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            x[k] = left[i]
            i += 1
        else:
            x[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            x[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1
    return x




arr = [3,1,2,12,4,5,6,12,4,13]
a , x = bubbleSort(arr)
print("%f초 걸렸습니다"%x)
print(quickSort(arr))
print(insertionSort(arr))
print(mergetSort(arr))

