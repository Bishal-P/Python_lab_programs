sentence="aeiou"
vowels=0
for i in sentence:
    if i in "aeiouAEIOU":
        vowels+=1
print("The number of vowels present in the sentence is ",vowels)