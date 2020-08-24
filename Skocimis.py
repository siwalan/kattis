a,b,c= map(int, input().split())

far_left = min(a,b,c)
far_right = max(a,b,c)

if (a == far_left):
    if (c == far_right):
        mid = b
    else:
        mid = c
elif (c == far_left):
    if (a == far_right):
        mid= b
    else:
        mid =a

max_combo = max(abs(far_right - mid), abs(far_left - mid))-1
print (max_combo)
