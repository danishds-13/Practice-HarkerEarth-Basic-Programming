# Read input
n = int(input().strip())
arr = list(map(int, input().split()))

MOD = 10**9 + 7

product = 1
for num in arr:
    product = (product * num) % MOD

print(product)