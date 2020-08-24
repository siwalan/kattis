x, y, n = map(int, input().split())

for i in range(1, n+1):
    fizz= False
    buzz= False
    if (i % x) == 0:
        fizz = True
    if (i % y) == 0:
        buzz = True
        
    if fizz == True and buzz == True:
        print('FizzBuzz')
    elif fizz==True:
        print('Fizz')
    elif buzz==True:
        print('Buzz')
    else:
        print(i)
        
