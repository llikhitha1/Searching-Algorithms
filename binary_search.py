lst=list(map(int,input().split()))
key=int(input())
flag=0
low=0
high=len(lst)-1
while(low<=high):
    mid=low+(high-low)//2
    if(lst[mid]==key):
        flag=1
        break
    elif(lst[mid]>key):
        high=mid-1
    else:
        low=mid+1
if(flag==1):
    print(key,'found')
else:
    print(key,'not found')