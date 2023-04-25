num=[70,30,24,20]
lst=[]
def isPrime(n):
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    if c==1:
        return "yes"
    else:
        return "no"

def isDivby3(a):
    count=0
    for i in range(2,a):
        if isPrime(i)=="yes":
            if a%i==0:
                count+=1
    if count==3:
        lst.append(a)

for i in num:
    isDivby3(i)
print(lst)


