word=input("Enter the sentence :")
word=word.split(" ")
dic=dict()
for i in word:
    if i not in dic:
        dic[i[0]]=i
print(dic)