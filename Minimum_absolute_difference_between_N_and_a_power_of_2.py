import math
n=int(input())
b=pow(2,int(math.log2(n)))
r=b*2
if(n-b>r-n):
   print(abs(r-n))
else:
    print(abs(n-b))
    