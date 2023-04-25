a=[22,1,2,3,4,4,5,6,7,8,9,10,11]
b=[]
maxlength=0
lst=[]
for i in range(len(a)-1):
    if a[i]+1==a[i+1]:
        b.append(a[i])
        if i==len(a)-2:
            b.append(a[i]+1)
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

