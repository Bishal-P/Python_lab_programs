string=input("Enter the string  :")
a=""
for i in range(len(string)-1,-1,-1):
    a+=string[i]
print(a)