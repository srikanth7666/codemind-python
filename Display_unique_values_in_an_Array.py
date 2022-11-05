n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=0
for i in range(n):
    for j in range(i):
        if a[i]==a[j]:
            b.append(a[i])
for i in range(n):
    if a[i] not in b:
        d+=1
        c.append(a[i])
if d==0:
    print('-1')
else:
    print(*c)