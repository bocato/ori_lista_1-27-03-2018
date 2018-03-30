
# Questão 2: Escreva um programa que imprima uma pirâmide de números se- gundo o exemplo abaixo:
#
# Exemplo:
# Entre com o numero de linhas da piramide: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# Exemplo:
# Entre com o numero de linhas da piramide: 8
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8

# Functions
def printPiramidWithSize(size):
    for i in range(size+1):
        for j in range(i):
            print(j+1, end = " ")
        print()


# Input
stringInput = input("Give me the piramid size:\n")
printPiramidWithSize(int(stringInput))
