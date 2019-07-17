k=int(input())
count=0
while(k>0):
  digit=k%10
  count+=digit
  k=k//10
print(count)
