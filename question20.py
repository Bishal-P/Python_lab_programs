z="acedfghijkl"
s=""
k=[]
for i in z:
    if(i not in "aeiou"):
        s=s+i
    else:
        if(len(s)>0):
            k.append(s)
        s=""
k.sort(key=len)
p=len(k)
print(k[p-1])




        
    
        
        
