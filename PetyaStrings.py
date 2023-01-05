s1 = input().lower()
s2 = input().lower()

def compareS(s1,s2):
    for a1, a2 in zip(s1, s2):
        if ord(a1) < ord(a2):
            return -1
        elif ord(a2) < ord(a1):
            return 1
    return 0

print(compareS(s1,s2))


