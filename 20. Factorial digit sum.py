# Variables
factorialSum = 100
numberSum = 0


for i in range(99, 1, -1):
  factorialSum *= i


for i in range(len(str(factorialSum))):
  numberSum += int(str(factorialSum)[i])


print(numberSum)
