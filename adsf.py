def Sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
 
arr = [int(input()),int(input()),int(input()),int(input()),int(input()),int(input())]

Sort(arr)
 
print ("排序后的数组:")
for i in range(len(arr)):
    print ("%d" %arr[i]),
