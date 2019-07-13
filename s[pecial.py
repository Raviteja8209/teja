ss=input()
c=0
for i in range(len(ss)):
    if (ss[i].isalpha() or ss[i].isnumeric() or ss[i]==" "):
        continue
    c=c+1 
else:
    print(c)
