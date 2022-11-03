# Variables
number = 2 ** 1000
numberSum = 0


for i in range(len(str(number))):
  numberSum += int(str(number)[i])


print(numberSum)
