import sys

n = int(input())
refer = -1
result = []

for i in range(n):
    a = sys.stdin.readline().strip()
    if a != refer:
        result.append(a)
    refer = a

for i in result:
    print(i)