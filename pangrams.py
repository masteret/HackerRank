string = input().lower().replace(" ","")
alphabet = [0]*26
for char in string:
    alphabet[ord(char)-97] += 1
if all(alphabet):
    print("pangrams")
else:
    print("not pangram")