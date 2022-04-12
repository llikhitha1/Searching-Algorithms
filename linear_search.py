lst=list(map(int,input().split()))
key=int(input())
flag=0
for i in lst:
    if(i==key):
        flag=1
        break
if(flag==1):
    print(key,'found in the list')
else:
    print(key,'not found in the list')