a=[1,2,3,4,5,67,8,9,0]
b={1,3,4}
pos=int(input("Enter the position :"))-1
for i in range(len(a)):
    if i==pos:
        a.insert(pos,b)
print(a)

    
    