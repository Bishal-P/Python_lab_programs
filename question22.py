a=[10,20,30,40]
li=[]
def cumulative(arr,li,last,index):
    if index==len(arr):
        return 0
    sum=arr[index]+last
    li.append(sum)
    cumulative(arr,li,sum,index+1)
    return li

print(cumulative(a,li,0,0))
    
    