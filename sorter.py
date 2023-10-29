from time import time
from random import randint




data = list(randint(-30, 30) for i in range(40))
print(data)

# start_time = time()
# for i in range(len(data)):
#     for j in range(i+1, len(data)):
#         if data[j] < data[i]:
#             data[j], data[i] = data[i], data[j]
# end_time = time() - start_time

# print(data)
# print(end_time)


for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[j] < data[i]:
            data[j], data[i] = data[i], data[j]

print(data)