tag = input().strip()

vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

# Check letter rule
if tag[2] in vowels:
    print("invalid")
    exit()

# Correct digit pairs (skip '-')
pairs = [(0, 1), (3, 4), (4, 5), (7, 8)]

for i, j in pairs:
    if (int(tag[i]) + int(tag[j])) % 2 != 0:
        print("invalid")
        exit()

print("valid")
