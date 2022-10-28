# Variables
sumOfSquares = 0
squareOfSum = 0
sumSquareDifference = 0


for i in range(101):
  sumOfSquares += i ** 2


for i in range(101):
  squareOfSum += i
squareOfSum = squareOfSum ** 2


sumSquareDifference = squareOfSum - sumOfSquares
print(sumSquareDifference)
