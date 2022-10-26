def lcm(n,m):
  c=m
  while True:
   if(c%n==0)and(c%m==0):
      return c
   c+=1
a,b=map(int,input().split())
print(lcm(a,b))
