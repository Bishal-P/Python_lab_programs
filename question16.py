a=[1,2,3,3,4,5,5,5,5,6,7,8]
b=[]
for i in range(len(a)-1):
    if a[i] != a[i+1]:
        b.append(a[i])

print(b)