# Variables
firstNumber = 100
secondNumber = 100
product = 0
palindrome = 0
reverse = 0


def checkIfPalindrome(number):
    reverse = str(number)[::-1]
    if str(number) == str(reverse):
        print(str(number) + " is a palindromic number.\n")
    else:
        print(str(number) + " is not a palindromic number.\n")


# Gets the product of all numbers from 100 * 100 to 999 * 999.
while secondNumber <= 999:
    while firstNumber <= 999:
        product = firstNumber * secondNumber
        reverse = str(product)[::-1]
        if str(product) == str(reverse) and int(product) > int(palindrome):
            palindrome = int(product)
        firstNumber += 1
    secondNumber += 1
    firstNumber = 100


# Prints the largest palindromic number from multiplying two 3-digit numbers together.
print(str(palindrome) + " is the largest palindromic number from multiplying two 3-digit numbers together.")
