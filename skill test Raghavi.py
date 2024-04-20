import time
start=time.time()
def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=key
arr=[42,50,8,12,32]
print("The given array is: ",arr)
insertionsort(arr)
print("The sorted array is:")
for i in range(len(arr)):
    print("%d"%arr[i])
end=time.time()
print("Runtime of the program is: {end-start}")
