import random
L = []
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
m=[]
for i in L:
    if i%2==0:
        m.append(i)
print("even numbers in a list is",m)
print("sum of even numbers in a list is",sum(m))