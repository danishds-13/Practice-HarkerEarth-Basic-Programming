# Matchsticks needed for each digit
matchsticks = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}

t = int(input())

for _ in range(t):
    N = input().strip()
    
    # Calculate total matchsticks used
    total_sticks = sum(matchsticks[d] for d in N)
    
    # Construct the largest number
    if total_sticks % 2 == 0:
        # All 1s
        print("1" * (total_sticks // 2))
    else:
        # One 7, rest 1s
        print("7" + "1" * ((total_sticks - 3) // 2))
