import sys
from collections import Counter

data = sys.stdin.read().strip().split()

n = int(data[0])
singers = list(map(int, data[1:]))

freq = Counter(singers)
max_count = max(freq.values())

ans = sum(1 for v in freq.values() if v == max_count)
print(ans)
