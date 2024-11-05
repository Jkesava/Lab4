import random
L = []
for i in range(40):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
m=[]
for i in L:
    rev=0
    t=i
    while i>0:
        r=i%10
        rev=rev*10+r
        i=i//10
    if t==rev:
        m.append(t)
print("palidrons are",m)