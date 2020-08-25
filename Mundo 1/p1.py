# Zen do Python: import this (no terminal python)
# Strings sao delimitadas por ' '
    #OBS.: e possivel usar " " para delimitar strings, mas por padrao os programadores usam ' '
# A funcao print() mostra coisas na tela
# O operador de + pode ser usado para concatenar strings
    #ex.: '7' + '4' = '74'
# Toda variavel em python e um objeto
# = significa recebe
    #ex2.: nome = 'Joao'
# A funcao input() recebe informacoes do usuario
    #ex3.: nome = input('Qual seu nome?')
    
'''
#DESAFIO 1 AULA 4
nome = input('Qual seu nome? ')
print('Ola ', nome, ' ! Prazer em te conhecer!')
'''

'''
#DESAFIO 2 AULA 4
dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')
print('Voce nasceu no dia ', dia, ' de ', mes, ' de ', ano, '. Correto?')
'''

'''
#DESAFIO 3 AULA 4
num1 = input('Primeiro numero ') # num1 = int(input('Primeiro numero'))
num2 = input('Segundo numero ') # num2 = int(input('Segundo numero'))
sum = int(num1) + int(num2) # sum = num1 + num2
print('A soma entre {} e {} e {}'.format(num1, num2, sum))
'''

# Tipos primitivos: int(), float(), bool() --> True or False, str()
# E possivel usar um metodo da funcao input para configurar as variaveis
# que serao mostradas na tela. 
# print('Mensagem qualquer {}'.format(variavel))
# veja, os {} serao substituidos pela variavel formatada seguindo
# algum padrao.
# Para ver o tipo primitivo de uma variavel basta usar o type(variavel)
# variavel.isnumeric() retorna verdadeiro caso a variavel seja um numero
# ou falso se a variavel nao for do tipo numerico (se e possivel converter
# essa variavel para um tipo primitivo numerico)
# variavel.isalpha() retorna True caso seja um caracter ou False caso contrario
# variavel.isalnum() retorna True caso seja um alfanumerico e False caso contrario
# existem varias funcoes para teste de tipo, pesquisar mais depois

'''
#DESAFIO 2 AULA 6: faca um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informacoes possiveis sobre ele
var = input('Digite algo: ')
print('O tipo primitivo desse valor e {}'.format(type(var)))
print('So tem espacos? {}'.format(var.isspace()))
print('E um numero? {}'.format(var.isnumeric()))
print('E alfabetico? {}'.format(var.isalpha()))
print('E alfanumerico? {}'.format(var.isalnum()))
print('Esta em maiusculo? {}'.format(var.isupper()))
print('Esta em minusculo? {}'.format(var.islower()))
print('Esta capitalizada? {}'.format(var.istitle()))
'''

# 