n = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Step 1: Find the target value (minimum of A)
target = min(A)

steps = 0

# Step 2: Try to reduce every A[i] to target
for i in range(n):
    diff = A[i] - target

    # If A[i] is already equal to target, no steps needed
    if diff == 0:
        continue

    # If we cannot reduce exactly using B[i], it's impossible
    if diff % B[i] != 0:
        print(-1)
        exit()

    # Count how many times we subtract B[i]
    steps += diff // B[i]

# Step 3: Print total steps
print(steps)
