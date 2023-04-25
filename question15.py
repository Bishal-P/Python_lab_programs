a=input("Enter the string :")
index=0
vowels=[]
newString=""
for i in range(len(a)):
    if a[i] in "aeiou":
        vowels.append(a[i])
vowels=sorted(vowels)
for i in range(len(a)):
    if a[i] in "aeiou":
        newString+=vowels[index]
        index+=1
    else:
        newString+=a[i]
print(newString)