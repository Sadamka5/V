import sys

x = list(sys.stdin.readline().strip())
f = list(sys.stdin.readline().strip())

f = list(f)
x = list(x)

f.sort()
x.sort()

print(1 if f == x else 0)
