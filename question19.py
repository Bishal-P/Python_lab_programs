def largestsubstring(a,c="",mainstring=""):
    for i in range(len(a)):
        for i in range(i,len(a)):
            if a[i] not in c:
                c=c+a[i]
            else:
                if len(c)>len(mainstring):
                    mainstring=c
                c=""
                c+=a[i]
        if len(c)>len(mainstring):
                    mainstring=c
        c=""
    return mainstring
print("The largest substring is :",largestsubstring(input("Enter the string :")))
    