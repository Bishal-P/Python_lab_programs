arr=[1,2,3,4,5,6,7,8,9]
rot=int(input("Enter the number of time you want to rotate :"))
for i in range(rot):
    arr.insert(0,arr[len(arr)-1])
    del arr[len(arr)-1]
print(arr)