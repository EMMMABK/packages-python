from turtle import right


listt = [345,345,45,6,45,6,56,8,0,8,65,43,2,3,5,7,9,0,9]
def merge(l):
    if len(l)>1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        merge(left);merge(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j +=1
            k +=1
        while i<len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j<len(right):
            l[k] = right[j]
            j +=1 
            k +=1
merge(listt)
print(listt)