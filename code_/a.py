import time
start = time.time()
a = 0
for i in range(100000, 2100000):
    #a += i*i
    a += i**2
print(a)
print(time.time()-start)