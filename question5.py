num=int(input("Enter the number :"))
fact=1
for i in range(num,1,-1):
    fact*=i

print("The factorial of the number is :",fact)