import math
r,d= map(int, input().split())
print(math.ceil(r / math.sin(math.radians(d))))