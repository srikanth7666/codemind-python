a=int(input())
b=int(input())
for i in range(1,b+1):
  w,h=map(int,input().split())
  if(w<a or h<a):
     print('UPLOAD ANOTHER') 
  elif((w==a and h==a)or w==h):
     print('ACCEPTED') 
  else:
     print('CROP IT') 