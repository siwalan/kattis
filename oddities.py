num_data = int(input())
database = []
for i in range(num_data):
    database.append(int(input()))
 
for i in database:
    if (i % 2) == 0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))

    