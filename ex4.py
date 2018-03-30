

# Questão 4: Escreva uma função que receba um número m como argumento de entrada e retorne uma lista com todos os divisores de m.
# Não se esqueça de testar a sua função.


# Functions
def getDivisorsForNumber(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Input
stringInput = input("Wich number do you want to know the divisors?\n")
print("The divisors are: ", getDivisorsForNumber(int(stringInput)))