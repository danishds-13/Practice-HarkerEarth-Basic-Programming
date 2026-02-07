n = int(input().strip())
village = list(input().strip())

# Step 1: Check for adjacent houses
for i in range(n - 1):
    if village[i] == 'H' and village[i + 1] == 'H':
        print("NO")
        exit()

# Step 2: Place fences on all empty spaces
for i in range(n):
    if village[i] == '.':
        village[i] = 'B'

# Step 3: Output result
print("YES")
print("".join(village))
