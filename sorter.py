from time import time
from random import randint


data = list(randint(-30, 30) for i in range(40))
print(f"Origin list: {data}")

start_time = time()
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[j] < data[i]:
            data[j], data[i] = data[i], data[j]
end_time = time() - start_time

print(f"Sorted list: {data}")
print(f"Function running time: {end_time}")
