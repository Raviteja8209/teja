f,l=map(int(input())
for i range(a+1,b):
  for k in range(2,i):
    if i%k==0:
      break
  else:
      print(i,end=" ")
