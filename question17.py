a=[int(input("Enter the element :")) for i in range(int(input("Enter the size of the list :")))]
b=[]
maxlength=0
lst=[]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        b.append(a[i])
        if i==len(a)-2:
            b.append(a[i+1])
            if len(b)>maxlength:
                maxlength=len(b)
                lst=b
    else:
        b.append(a[i])
        if len(b)>maxlength:
                maxlength=len(b)
                lst=b
        b=[]
print(lst)

