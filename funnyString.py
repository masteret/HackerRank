numOfTC = int(input())
for x in range(numOfTC):
    forward = input()
    def judge(forward):
        for ind in range(len(forward)//2):
            if abs(ord(forward[ind])-ord(forward[ind+1])) != abs(ord(forward[len(forward)-ind-1])-ord(forward[len(forward)-ind-2])):
                return False
        return True
    if judge(forward):
        print("Funny")
    else:
        print("Not Funny")
    