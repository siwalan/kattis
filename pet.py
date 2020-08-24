num = 0
max_score = 0
for i in range(5):
    a, b , c, d = map(int, input().split())
    f = a+b+c+d
    if f> max_score:
        max_score = f
        num = i

print("{} {}".format((num+1), max_score))