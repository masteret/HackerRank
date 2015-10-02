input()
bleh = sorted(list(set([int(x) for x in input().split()])))
min = 100000000
result = []
for ind, val in enumerate(bleh[:-1]):
    if abs(val - bleh[ind+1]) < min:
        result = [val, bleh[ind+1]]
        min = abs(val - bleh[ind+1])
    elif abs(val - bleh[ind+1]) == min:
        result += [val, bleh[ind+1]]
for x in result:
    print(x, end=" ")