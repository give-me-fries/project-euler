x = 1
y = 2
z = 3
totalSum = 0

while y < 4000000:
    totalSum += y
    x = y + z
    y = x + z
    z = x + y

print(totalSum)
