iteration_counter = 0
miles_list = []

while True:
    n_speed = int(input())
    if n_speed == -1:
        break
    ot_time_elapsed = 0
    miles = 0
    for i in range (n_speed):
        speed, time_elapsed = map(int, input().split())
        miles = (time_elapsed-ot_time_elapsed)* speed + miles
        ot_time_elapsed = time_elapsed
    miles_list.append(miles)

for data in miles_list:
    print("{} miles".format(data))