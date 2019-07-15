ln=list(map(int,input().split()))
h=ln[0]
p=ln[1]
h=h^p
p=h^p
h=h^p
print(h,p)
