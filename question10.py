prev=0
current=1
i=0
lst=[]
while (current<=200):
    if i==0 or i==1:
        i+=1
        continue
    temp=prev+current
    prev=current
    current=temp
    if current>=100 and current<=200:
        lst.append(current)
for i in range(100,201):
    if i not in lst:
        print(i,end=" ")

# OR

# import math
# def PerfectSquare(num):
#     s = int(math.sqrt(num))
#     return s*s == num
    
# for i in range(100,201):
#     a=PerfectSquare(5*i**2 + 4) or PerfectSquare(5*i**2 - 4)
#     if a==False:
#         print(i,end=" ")
    