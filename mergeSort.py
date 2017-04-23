unsorted = [1,45,23,12,45,56,23,67]
def mergesort(alist):
  if len(alist) > 1:
    size = len(alist)
    mid = size//2
    left = alist[mid:]
    right = alist[:mid]
    mergesort(left)
    mergesort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        #print(left[i], right[j])
        if left[i] < right[j]:
            alist[k] = left[i]
            i = i+1
        else:
            alist[k] = right[j]
            j= j+1
        k = k+1
    while j < len(right):
      alist[k] = right[j]
      j= j+1
      k= k+1
    while i < len(left):
      alist[k] = left[i]
      i = i+1
      k= k+1
    return(alist)

print(mergesort(unsorted))

a = (mergesort(unsorted))
for i in range(len(a)):
  print(a[i])





  
