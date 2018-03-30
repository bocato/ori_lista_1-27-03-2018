
# Questão 3: A mediana é uma medida estatística definida como o termo central de uma amostra após sua ordenação.
#
# Por exemplo, a amostra:
# {2, 1, 2, 5, 6,11,9}
#
# ao ser ordenada fica:
# {1,2,2,5,6,9,11}
#
# Logo, sua mediana é 5, pois este é o elemento presente na quarta posição (posição central) da ordenação.
# Para uma amostra com número par de termos, a mediana é tomada como a média aritmética entre as duas posições centrais.
#
# Por exemplo, a mediana da amostra ordenada:
# {−1, 6, 7, 18}
# é 6+7 / 2 = 6,5 2
#
# Escreva um programa que leia uma amostra de números do teclado e informe a sua mediana.
# Os números devem ser lidos separadamente. A parte específica do cálculo da mediana deve ser feita em uma função separada apenas para este fim.
# Esta função deve receber como argumento de entrada uma lista com a amostra e então retornar o valor da mediana. Obs: a função não deve alterar a
# amostra original do usuário, portanto, para fazer a ordenação da amostra, a função deve ordenar uma cópia da lista recebida como argumento de entrada.


# Functions
def calculateMedianForList(list):
    sortedList = sorted(list)
    center =  len(sortedList) // 2
    if len(sortedList) % 2 == 0:
        return (sortedList[center - 1] + sortedList[center]) / 2.0
    else:
        return sortedList[center]


def calculateMedianFromString(string):
    list = string.split(',')
    return calculateMedianForList(list)

# Input
stringInput = input("Give me the list with format '0, 1, 2, 10, 99':\n")
print("The median is %s", calculateMedianFromString(stringInput))