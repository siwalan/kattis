initial = int(input())
fibonnaci_array = [0,1]

# Dynamic Fibonnaci Refresher thanks to 
# https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/

def fibonnaci(number):
    if number<=len(fibonnaci_array):
        return fibonnaci_array[number-1]
    else:
        iterator_fib = fibonnaci(number-1)+fibonnaci(number-2)
        fibonnaci_array.append(iterator_fib)
        return iterator_fib

if initial == 1:
    print("0 1")
else:
    data = fibonnaci(initial+1)
    print("{} {}".format(fibonnaci(initial), fibonnaci(initial+1)))