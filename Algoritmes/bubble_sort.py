l = [9,8,7,6,5,4,3,2,1,0]

def bubble_sort(l):
    # Traverse through all array elements
    for i in range(len(l)-1):
        # Last i elements are already in place
        for j in range(len(l)-1-i):
             # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if l[j] > l[j+1]:
                l[j+1], l[j] = l[j], l[j+1]
    return l
print(bubble_sort(l))