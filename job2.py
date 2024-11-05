import random
L = []
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
m=[]
for i in L:
    cnt=0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        m.append(i)
print("prime numbers in a list",m)
print("sum of prime numbers in a list",sum(m))
