n=int(input())
a=list(map(int,input().split()))
r=int(input())
temp=0
for i in  range(0,n):
    for j in range(i+1,n):
        if a[i]-a[j]==r:
         temp=1  
         break
if temp==1:
    print('yes')
else:
    print('no')