count = int(input())
for time in range(count):
    cycle = int(input())
    length = 1
    for cur in range(cycle):
        if cur %2 == 0:
            length *= 2
        else:
            length += 1
    print(length)