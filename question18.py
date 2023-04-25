string=input("Enter a string :")
lst=[]
for i in range(len(string)-1,0,-1):
    for j in range(i):
        if string[j]==string[i]:
            lst.append(string[j:i+1])
maxlength=0
st=""
yes=0
for i in lst:
    for j in range(len(i)//2):
        if i[j]==i[len(i)-1-j]:
            yes=1
            continue
        else:
            yes=0
            break
    if yes==1:
        if len(i)>maxlength:
            maxlength=len(i)
            st=i
print(st)


