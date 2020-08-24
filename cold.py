num_data = input().split()
data_base = input().split()
below_zero = 0
for data in data_base:
    if int(data) < 0 :
        below_zero = below_zero+1
print(below_zero)

