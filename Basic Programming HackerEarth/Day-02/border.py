t = int(input().strip())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    max_border = 0

    # 1️⃣ Check rows
    for row in grid:
        count = 0
        for cell in row:
            if cell == '#':
                count += 1
                max_border = max(max_border, count)
            else:
                count = 0

    # 2️⃣ Check columns
    for col in range(m):
        count = 0
        for row in range(n):
            if grid[row][col] == '#':
                count += 1
                max_border = max(max_border, count)
            else:
                count = 0

    # 3️⃣ Output result
    print(max_border)
