f,l=map(int,input().split())
for i in range(f+1,l):
  for k in range(2,i):
    if i%k==0:
      break
  else:
      print(i,end=" ")
