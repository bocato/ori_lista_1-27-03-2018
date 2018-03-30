
# Questão 6: Use a função gerada no exercício anterior para fazer um programa que imprime os n
# primeiros números perfeitos, onde n é uma entrada lida do teclado repetidamente até ser inteira positiva.
# Assuma que o usuário sempre entrará com números para o valor de n.

# Functions
def getDivisorsForNumber(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def isNumberPerfect(number):
    divisorsExcludingNumber = getDivisorsForNumber(number)
    divisorsExcludingNumber.remove(number)
    divisorsSum = sum(divisorsExcludingNumber)
    return divisorsSum == number

def getAllPerfectNumbersInRange(start, end):
    perfectNumbers = []
    for i in range(start, end + 1):
        if isNumberPerfect(i):
            perfectNumbers.append(i)
    return perfectNumbers

# Input
print("Give me a number to find the perfect ones from 0 to the given number:\n")
stringInput = input()
while int(stringInput) <= 0:
    print("Invalid input, you need to give me a positive number! Input something again: \n")
    stringInput = input()

perfectNumbersInRange = getAllPerfectNumbersInRange(1, int(stringInput))

if len(perfectNumbersInRange) > 0:
    print("The perfect numbers from 0 to {} are: {}".format(stringInput, perfectNumbersInRange))
else:
    print("The are no perfect numbers from 0 to {}".format(stringInput))

