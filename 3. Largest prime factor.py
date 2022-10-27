# Variables
factors = []
primeNumbers = []
divisors = []
number = 600851475143
divisor = 2
result = 0


# Find factors of "number" besides 1 and itself
while divisor < number:
    result = number / divisor
    if float(result).is_integer() == True:
      factors.append(int(result))
      number = result
      divisors.append(divisor)
      divisor = 2
    divisor += 1


# Combine "factors" with "divisors"
combinedList = factors + divisors
combinedList.sort(reverse = True)


# Check if each number is prime
for i in range(len(combinedList)):
  number = combinedList[i]
  divisor = 2
  if number == 2:
    primeNumbers.append(2)
  for i in range(number - 2):
      result = number / divisor
      if float(result).is_integer() == True:
          break
      divisor += 1
      if divisor == number:
          primeNumbers.append(divisor)

print(str(primeNumbers[0]) + " is the largest prime factor.")
