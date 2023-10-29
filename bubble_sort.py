from time import time
from random import randint


data = [randint(-30, 30) for i in range(40)]
print(f"Original list: {data}")

start_time = time()
n = (len(data)) - 1
while n > 0:
    for i in range(n):
        if data[i] > data[i + 1]:
            data[i] = data[i] + data[i + 1]
            data[i + 1] = data[i] - data[i + 1]
            data[i] = data[i] - data[i + 1]
        else:
            n -= 1
end_time = time() - start_time

print(f"Sorted list: {data}")
print(f"Function running time: {end_time}")
