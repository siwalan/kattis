num_data = int(input())
num_sum = 0
for i in range(num_data):
    num_process = input()
    power = int(num_process[-1])
    base = int(num_process[:-1])
    power_num = base**(power)
    num_sum = num_sum + power_num
print(num_sum)x