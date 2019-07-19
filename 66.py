
numbers=int(input())
if numbers>1:
  for i in range(2,numbers):
    if numbers%i==0:
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
