# Read number of test cases
t = int(input())

for _ in range(t):
    # Read cost of green and purple balloons
    green_cost, purple_cost = map(int, input().split())
    
    # Read number of participants
    n = int(input())
    
    # Counters for solved problems
    problem1_solved = 0
    problem2_solved = 0
    
    # Read participant data
    for _ in range(n):
        p1, p2 = map(int, input().split())
        problem1_solved += p1
        problem2_solved += p2
    
    # Option 1: Green for problem 1, Purple for problem 2
    cost1 = problem1_solved * green_cost + problem2_solved * purple_cost
    
    # Option 2: Purple for problem 1, Green for problem 2
    cost2 = problem1_solved * purple_cost + problem2_solved * green_cost
    
    # Print minimum cost
    print(min(cost1, cost2))
