str_bin = ""
num = int(input())

while(True):
    bin_rep = num % 2
    if (bin_rep >= 1):
        str_bin =  '1'   + str_bin
    else:
        str_bin =  '0'  + str_bin
    num = (num/2)
    if num < 1:
        break

reversed_bin = str_bin[::-1]
num = 0
count = len(reversed_bin) - 1
for element in reversed_bin:
    if element == '1':
        num = num + 2 ** count
    count = count - 1
print(num)