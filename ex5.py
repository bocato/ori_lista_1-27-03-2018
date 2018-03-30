
# Questão 5:
# Em Matemática, um número perfeito é um número natural para o qual a soma de todos os seus divisores
# positivos próprios (excluindo ele mesmo) é igual ao próprio número.
#
# Por exemplo, o número 6 é um número perfeito, pois:
# 6=1+2+3
# O próximo número perfeito é o 28, pois:
# 28 = 1 + 2 + 4 + 7 + 14.
# Os quatro primeiros números perfeitos são: 6, 28, 496 e 8128.
#
# Escreva uma função que recebe um número m como entrada e retorna True se o m for perfeito e False caso contrário.
# Para fazer essa função, use a função gerada no exercício anterior.

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

# Input
stringInput = input("Wich number do you want to check for 'perfection'?\n")
perfectionString  = "perfect" if isNumberPerfect(int(stringInput)) else "not perfect"
print("The number {} is {}.".format(stringInput, perfectionString))