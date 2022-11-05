n=int(input())
a=list(map(int,input().split()))
b=0
for i in range(n):
    if(len(str(a[i]))%2==0):
        b+=1
print(b)