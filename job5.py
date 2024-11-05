import random
L = []
for i in range(10):
    ele = random.randint(100, 200)
    L.append(ele)
print("The generated random list of 10 - element", L)
print("reversed list is",L[::-1])