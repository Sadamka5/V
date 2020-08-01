import sys

k = int(input())
r = [0] * 101

for i in range(k):
    f = sys.stdin.readline().strip()
    for j, element in enumerate(f.split()):
        if j == 0:
            continue
        else:
            r[int(element)] += 1
    del f

for i in range(101):
    if r[i]:
        print(' '.join([str(i)] * r[i]), end=' ')