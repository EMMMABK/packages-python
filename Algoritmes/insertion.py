l = [9,8,7,6,5,4,3,2,1,0]

def insertionSort(l):
     # Traverse through 1 to len(arr)
    for i in range(len(l)):
        t = l[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and l[j] > t:
            l[j+1] = l[j]
            j-=1
        l[j+1] = t
    return l
print(insertionSort(l))