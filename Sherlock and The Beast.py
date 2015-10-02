def answer(length):
    bleh = False
    numFive = length//3
    for x in range(numFive, -1, -1):
        xlength = length - 3*x
        numThree = xlength//5
        for y in range(numThree, -1, -1):
            if xlength - 5*y == 0:
                bleh = True
                for five in range(x):
                    print('555', end='')
                for three in range(y):
                    print('33333', end='')
                print()
                return None
    if not bleh:
        print('-1')
        return None
                
            
count = int(input())
for timeToRead in range(count):
    length = int(input())
    answer(length)