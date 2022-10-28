# Variables
number = 0
divisor = 1


# Main part
while divisor != 20:
  if number % divisor == 0 and number != 0:
    divisor += 1
  else:
    divisor = 1
    number += 20

print(number)
