limit=int(input("Enter the count :"))
prev=0
current=1
for i in range(limit):
    if i==0 or i==1:
        print(i,end=" ")
        continue
    temp=prev+current
    prev=current
    current=temp
    print(current,end=" ")