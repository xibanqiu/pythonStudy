# 1-2+3-4...-76+78-79...+98-99

import math
k = -1
result = 0
j = 1

for i in range(100):
    if i == 77:
        continue
    result = result + i * math.pow(k, j)
    j += 1

print(result)



