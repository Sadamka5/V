j = str(input())
s = str(input())
count = 0

for i in s:
    if i in j:
        count += 1

print(count)