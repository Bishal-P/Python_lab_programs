num=input("Enter the number :")
l=len(num)
sum=0
for i in range(l):
    sum+=int(num[i])**l
if sum==int(num):
    print("The number is an armstrong number ")
else:
    print("The number is not an armstrong number")