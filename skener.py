r, c , zr, zc = map(int, input().split())
input_matrix = []
for i in range(r):
    input_matrix.insert(i, input())

max_c = zc
max_r = zr
current_col = 0
current_row = 0

for i in input_matrix:
    while(current_row < max_r):
        for j in i:
            while(current_col < max_c):
                print(j, end="")
                current_col = current_col + 1
            current_col = 0
        current_row = current_row + 1
        print("")
    current_row = 0