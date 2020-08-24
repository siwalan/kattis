dominant = {'A':11, 'K':4, 'Q':3, 'J':20, 'T':10, '9':14, '8':0, '7':0}
non_dominant = {'A':11, 'K':4, 'Q':3, 'J':2, 'T':10, '9':0, '8':0, '7':0}

initial, dom = (input().split())

sum_val = 0
for i in range(int(initial)*4):
    card = input()
    if card[1] == dom:
        sum_val = sum_val + dominant[card[0]]
    else:
        sum_val = sum_val + non_dominant[card[0]]

print(sum_val)
