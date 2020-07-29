n = int(input())
a = []
temp = 0
maximum = 0


for i in range(n):
    a.append(int(input()))

for i in a:
    if i == 1:
        temp += 1
    elif i != 1:
        if maximum < temp:
            maximum = temp
        temp = 0

if set(a) == {1}:  # Если последовательность состоит только из единиц
    maximum = n

if maximum > temp:
    print(maximum)
elif temp > maximum:
    print(temp)
elif temp == maximum:
    print(temp)