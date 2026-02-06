n = int(input())
arr = list(map(int, input().split()))

# Check last digit of the last number
if arr[-1] % 10 == 0:
    print("Yes")
else:
    print("No")
