
# Questão 1: Faça um programa em Python que leia uma string e conte:
# • o número de caracteres alfabéticos;
# • o número de caracteres numéricos;
# • o número de caracteres não alfabéticos;
# • o número de palavras (assuma que entra cada par de palavras existe ao menos um caracter de espaço, tabulação ou "/n");
# • o número de consoantes.

# Functions
def countLettersFrom(string):
    letters = 0
    for letter in string:
        letters += letter.isalpha()
    return letters


def countNumbersFrom(string):
    numbers = 0
    for letter in string:
        numbers += letter.isdigit()
    return numbers

def countNonAlphasFrom(string):
    alphas = 0
    for letter in string:
        alphas += not(letter.isalpha())
    return alphas

def countWordsFrom(string):
    return len(string.split())

def countConsonantsFrom(string):
    consonants = 0
    for character in string:
        consonants += not(character in ('a', 'e', 'i', 'o', 'u'))
    return consonants

# Input
stringInput = input("Give me the input:\n")
print("Letters = %s" %(countLettersFrom(stringInput)))
print("Numbers = %s" %(countNumbersFrom(stringInput)))
print("NonAlphas = %s" %(countNonAlphasFrom(stringInput)))
print("Words = %s" %(countWordsFrom(stringInput)))
print("Consonants = %s" %(countConsonantsFrom(stringInput)))


