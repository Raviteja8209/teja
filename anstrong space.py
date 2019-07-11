x,y=map(int,input().split())
a=[]
sum=0
temp=num
for num in range(n,u):
   while temp > 0:
       digit = temp % 10
       summ += digit ** 3
       temp //= 10
   if num == sum:
       a.append(str(sum))
print(" ".join(a))
