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
#DESAFIO 4 AULA 6: faca um programa que leia algo pelo teclado e mostre
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

# ** potenciacao, // divisao inteira, % resto da divisao
# ordem de precedencia: ()
#                       **
#                       *, /, //, %
#                       +, -
# base**potencia = pow(base,potencia)

'''
# Apenas algumas coisas que da pra fazer com o .format()
nome = input('Qual e seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) #escreve nome em 20 espacos
print('Prazer em te conhecer {:>20}!'.format(nome)) #escreve nome em 20 espacos e alinha a direita
print('Prazer em te conhecer {:<20}!'.format(nome)) #escreve nome em 20 espacos e alinha a esquerda
print('Prazer em te conhecer {:^20}!'.format(nome)) #escreve nome em 20 espacos e alinha ao centro
print('Prazer em te conhecer {:=^20}!'.format(nome)) #escreve nome em 20 espacos, alinhado ao centro e com igual em volta
# caso eu queria que nao quebre uma linha de um print para outro basta fazer
# print('mensagem', end = ''). Quebrar linha e \n

num1 = 5
num2 = 2
s = num1 + num2
d = num1/num2
m = num1*num2
di = num1//num2
e = num1**num2
print('{}, {:.3f}, {}, {}, {}'.format(s, d, m, di, e)) #a formatacao {:.3f} especifica a quantidade de casas decimais que quero que seja mostrado do numero
'''

'''
#DESAFIO 5 AULA 7: faca um programa que leia um numero inteiro e mostre
#na tela seu sucessor e seu antecessor
num = int(input('Digite um numero inteiro: '))
print('O numero {} tem {} como seu antecessor e {} como seu sucessor'.format(num, num-1, num+1))
'''

'''
#DESAFIO 6 AULA 7: faca um algoritmo que leia um numero e mostre o seu dobro,
#triplo e raiz quadrada
num = float(input('Digite um numero: '))
print('Dobro de {}: {}\nTriplo de {}: {}\nRaiz quadrada de {}: {:.3f}'.format(num, num*2, num, num*3, num, num**(1/2)))
'''

'''
#DESAFIO 7 AULA 7: desenvolva um programa que leia as duas notas de um aluno
#calcula e mostre a sua media
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
print('A media entre {} e {} e {:.3f}'.format(num1, num2, (num1 + num2)/2))
'''

'''
#DESAFIO 8 AULA 7: escreva um programa que leia um valor em metros e o exiba
#convertido em centimetros e milimetros
num = float(input('Digite um valor em metros: '))
print('{} metros sao {} centrimetos'.format(num, num*100))
print('{} metros sao {} milimetros'.format(num, num*1000))
'''

'''
#DESAFIO 9 AULA 7: faca a tabuada de um numero qualquer
#OBS.: eu trapaceei nessa questao porque fique com preguica
num = float(input('Digite um numero: '))
print('A tabuada do numero {} e: '.format(num))
for i in range(11):
    print('{} x {} = {}'.format(num, i, num*i))
'''

'''
#DESAFIO 10 AULA 7: faca um programa que leia quantos reais uma pessoa tem
#e diga quantos dolares ela pode comprar
reais = float(input('Quantos reais voce possui? '))
print('Com {} reais voce consegue {:.2f} dolares, considerando que 1 dolar = 3.27 reais.'.format(reais, reais/3.27))
'''

'''
#DESAFIO 11 AULA 7: faca um programa que leia a largura e a altura de uma
#parede e diga a area da parede e quantos litros de tinta e necessario 
#para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 metros quadrados
largura = float(input('Escreva a largura da parede: '))
altura = float(input('Escreva a altura da parede: '))
area = largura*altura
print('Uma parede de {} metros quadrados precisa de {} litros de tinta para ser pintada.'.format(area, area/2))
'''

'''
#DESAFIO 12 AULA 7: faca um programa que leia o preco de um produto e mostre
#seu novo preco com 5% de desconto
produto = float(input('Digite o preco do produto: '))
desconto = (produto*5)/100
print('O preco original do produto e {} reais, com 5 por cento de desconto ele sai a {} reais.'.format(produto, produto - desconto))
'''

'''
#DESAFIO 13 AULA 7: faca um programa que leia o salario de um funcionario
#e mostre seu novo salario com 15% de aumento
salario = float(input('Qual valor do salario do funcionario? '))
aumento = (salario*15)/100
print('O funcionario recebia {} e agora passa a receber {} depois do aumento de 15 por cento.'.format(salario, salario + aumento))
'''

'''
#DESAFIO 14: faca um programa que converta uma temperatura digitada em graus
#celsius e converta para graus fahrenheit
c = float(input("Digite uma temperatura em graus Celsius: "))
f = (c * 9 / 5) + 32
print("{} graus Celsius correspondem a {} graus Fahrenheit.".format(c,f))
'''

'''
#DESAFIO 15: Escreva um programa que pergunte a quantidade de Km 
#percorridos por um carro alugado e a quantidade de dias pelos 
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$60 por dia e R$0,15 por Km rodado.
km = float(input("Quantos kilometros o carro percorreu? "))
dias = int(input("O carro foi alugado por quantos dias? "))
valor = km*0.15 + dias*60
print("O preco a se pagar pelo aluguel do carro e de {} .".format(valor))
'''

# Para importa bibliotecas basta usar o comando: import alguma_bilbioteca
# Caso eu queira apenas uma funcionalidade especifica de uma biblioteca, basta usar o
# comando: from alguma_biblioteca import funcionalidade
# Ex.4: import math
#      from math import sqrt
#      from math import sqrt, ceil

'''
# Ex.5:
import math
#from math import sqrt, ceil #neste caso nao se usa o math., usa-se apenas sqrt(), ceil()...
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
#ceil e arredondar para cima, floor e arrendondar para baixo
print('A raiz de {} e igual a {}'.format(num, math.ceil(raiz)))
'''

# E possivel ver a lista de packages do Python na aba PyPI do site oficial do Python (https://pypi.org/)

'''
#DESAFIO 16 AULA 8: faca um programa que leia um numero real qualquer pelo teclado
#e mostre na tela a sua porcao inteira
from math import trunc
num = float(input('Digite um numero real: '))
print('O numero {} tem a parte inteira {}.'.format(num, trunc(num)))
'''

'''
#DESAFIO 17 AULA 8: faca um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt, pow
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('A hipotenusa tem {:.2f} de comprimeto.'.format(h))
# existe o metodo math.hypot(valor1, valor2) que calcula o valor da hipotenusa direto!
'''

'''
#DESAFIO 18 AULA 8: faca um programa que leia um angulo qualquer e mostre na tela o valor
#do seno, cosseno e tangente desse angulo
from math import sin, cos, tan, radians
ang = float(input('Digite um angulo qualquer: '))
rad = radians(ang)
print('Cosseno de {}: {:.3f}'.format(ang, cos(rad)))
print('Seno de {}: {:.3f}'.format(ang, sin(rad)))
print('Tangente de {}: {:.3f}'.format(ang, tan(rad)))
'''

'''
#DESAFIO 19 AULA 8: um professor quer sortear um dos seus quatro alunos para apagar o quadro
#Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
student = random.randint(1, 4)
print('O professor sorteou o numero {}, correspondente ao aluno'.format(student), lista[student-1])
'''

'''
#DESAFIO 20 AULA 8: o mesmo professor do desafio passado quer sortear a ordem de apresentacao
#de trabalho dos alunos. Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem sorteada pelo professor e a seguinte: ', lista)
'''


#DESAFIO 21 AULA 8: faca um programa que abra e reproduza o audio de um arquivo MP3
#import os
#os.startfile(r'C:\Users\testeFelipe\Desktop\Curso em video Python 3\Mundo 1\A_mp3_audio.mp3')
#Outra maneira de resolver esse exercicio e usando a biblioteca PyGame


# CADEIAS DE CARACTER
# Vamos considerar uma variavel do tipo string chamada frase. Existem varias funcoes que para
# manipular e analisar uma cadeia de caracter.
# Analise de strings: len(frase): retorna o tamanho da string
#                     frase.count(): conta quantas vezes ocorre uma determinada instancia
#                       ex.1: frase.count('o')
#                       ex.2: frase.count('o', 0, 13) #considerando apenas o intervalo de 0 a 12
#                     frase.find(): retorna a posicao onde uma determinada instancia acontece. E retornado o valor -1 caso a string nao possua a instancia mencionada
#                       ex.3: frase = 'Video'
#                             frase.find('deo') -> neste caso ele ira retornar 2
#                     'instancia' in frase: retorna TRUE se instancia existir dentro de frase, caso contrario retorna False
# Transformacao: frase.replace('a', 'b'): em frase, a instancia 'b' sera substituida por 'a'
#                frase.upper(): bota a string em caixa alta
#                frase.lower(): bota a string em minusculo
#                frase.capitalize(): apenas o primeiro caracter e colocado em maiusculo
#                frase.title(): todas as palavras dentro da string serao capitalizadas
#                frase.strip(): remove todos os espacos inuteis no inicio e ao final da string
#                  frase.rstrip(): remove os espacos apenas do lado direito da string   
#                  frase.lstrip(): remove os espacos apenas do lado esquerdo da string
# Divisao: frase.split(): quebra uma string onde houver espacos, as palavras serao colocadas dentro de uma lista
#          '-'.join(frase): faz uma juncao dos elementos de uma lista de strings em uma unica string separando-os por '-'

'''
#DESAFIO 22 AULA 9: crie um programa que leia o nome completo de uma pessoa e mostre:
#a)o nome com todas as letras maiusculas
#d)o nome com todas as letras minusculas
#c)quantas letras ao todo, sem considerar os espacos
#d)quantas letras tem o primeiro nome
nome = str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
print('O nome {} possui {} letras'.format(nome, len(nome) - nome.count(' ')))
a = nome.split()
print('O primeiro nome da pessoa e {} e possui {} letras'.format(a[0], len(a[0])))
'''

'''
#DESAFIO 23 AULA 9: crie um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos
#digitos separados
num = str(input('Digite um numero entre 0 a 9999: '))
t = 4 - len(num)
num = ' '*t + num 
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(num[3], num[2], num[1], num[0]))
'''

'''
#DESAFIO 24 AULA 9: crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao
#com o nome 'Santo'
cidade = str(input('Digite o nome de uma cidade: '))
if(cidade.upper().find('SANTO') == 0):
    print('Sua cidade comeca com o nome Santo.')
else:
    print('Sua cidade nao comeca com o nome Santo.')
'''

'''
#DESAFIO 25 AULA 9: Crie um programa que leia o nome de uma pessoa e diga se ela tem
#'Silva' no nome
nome = str(input('Digite seu nome: '))
if('SILVA' in nome.upper()):
    print('Voce possui Silva no nome.')
else:
    print('Voce nao possui Silva no nome.')
'''

'''
#DESAFIO 26 AULA 9: crie um programa que leia uma frase pelo teclado e mostre
#a)quantas vezes aparece a letra 'a'
#b)em que posicao ela aparece a primeira vez
#c)em que posicao ela aparece a ultima vez
frase = str(input('Digite uma frase: ')).strip()
print('A letra "a" aparece {} vezes. '.format(frase.upper().count('A')))
print('Primeira ocorrencia: {}.'.format(frase.upper().find('A')))
print('Ultima ocorrencia: {}.'.format(frase.upper().rfind('A')))
'''

'''
#DESAFIO 27 AULA 9: faca um programa que leia o nome completo de uma pessoa, mostrando em seguida
#o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome: '))
n = nome.split()
a = len(n)
print('Primeiro = {}\nUltimo = {}'.format(n[0], n[a - 1]))
'''

#Condicoes
#   if condition:
#       code
#   else:
#       code
#exemplo de condicao simplificada: tempo = int(input())
#                                  print('carro novo' if tempo <=3 else 'carro velho')
#                                  print('--Fim--')

'''
#DESAFIO 28 AULA 10: escreva um programa que faca o computador sortear um numero inteiro entre
#0 e 5 e peca para o usuario tentar adivinhar o numero e mostre na tela se ele acertou ou nao
from random import randint
numero = randint(0, 5)
num_usuario = int(input('Digite um numero entre 0 e 5: '))
if numero == num_usuario:
    print('Voce acertou!')
else:
    print('O numero sorteado foi {}'.format(numero))
'''

'''
#DESAFIO 29 AULA 10: escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
#80Km/h mostre uma mensagem dizendo que ele foi multado. A multa custa 7 reais por cada
#km/h a cima do limite
velocidade = float(input('Digite a velocidade do carro em Km/h: '))
if velocidade > 80:
    print('Voce foi multado em {} reais por ultrapassar o limite de velocidade igual a 80Km/h'.format(7*(velocidade - 80)))
else:
    print('Tudo certo, boa viagem!')
'''

'''
#DESAFIO 30 AULA 10: crie um programa que leia um numero e diga se ele e par ou impar
numero = int(input('Digite um numero inteiro qualquer: '))
if numero % 2 == 0:
    print('O numero {} e par!'.format(numero))
else:
    print('O numero {} e impar!'.format(numero))
'''

'''
#DESAFIO 31 AULA 10: desenvolva um programa que pergunte a distancia de uma viagem em Km
#e calcule o preco das passagem cabrando 0.50 centavos por Km para viagens de ate 200Km
#e 0.45 centavos para viagens mais longas
distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    print('O valor da sua passagem ficou em R${}'.format(distancia*0.5))
else:
    print('O valor da sua passagem ficou em R${}'.format(distancia*0.45))
'''

'''
#DESAFIO 32 AULA 10: faca um programa que leia um ano qualquer e mostre se ele e bissexto
ano = int(input('Digite um ano qualquer: '))
if (ano % 4 == 0) and (ano % 100 != 0) :
    print('O ano {} e bissexto!'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} e bissexto!'.format(ano))
    else:
        print('O ano {} nao e bissexto!'.format(ano))
'''

#Como pegar o ano atual da maquina :D
#from datetime import date
#ano = date.today().year

'''
#DESAFIO 33 AULA 10: faca um programa que leia tres numeros e mostre qual o maior e qual o menor
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

if num1 > num2:
    maior = num1
else:
    maior = num2
if maior > num3:
    print('O maior numero e {}'.format(maior))
else:
    print('O maior numero e {}'.format(num3))

if num1 < num2:
    menor = num1
else:
    menor = num2
if menor < num3:
    print('O menor numero e {}'.format(menor))
else:
    print('O menor numero e {}'.format(num3))
'''

'''
#DESAFIO 34 AULA 10: escreva um programa que pergunte o salario de um funcionario e calcule
#seu aumento, para salarios superiores a 1250.00 reais calcule um aumento de 10%, para inferiores
#ou iguais calcule um aumento de 15%
salario = float(input('Digite o valor do salario do funcionario: R$'))
if salario > 1250:
    aumento = salario * 0.1
    print('Seu aumento e de R${:.2f} e voce passara a receber R${:.2f}'.format(aumento, salario + aumento))
else:
    aumento = salario * 0.15
    print('Seu aumento e de R${:.2f} e voce passara a receber R${:.2f}'.format(aumento, salario + aumento))
'''

'''
#DESAFIO 35 AULA 10: desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario
#se elas podem ou nao formar um triangulo
import math
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))

if (r1 < r2 + r3) and (r1 > math.fabs(r2 - r3)) :
    if (r2 < r1 + r3) and (r2 > math.fabs(r1 - r3)) :
        if (r3 < r1 + r2) and (r3 > math.fabs(r2 - r1)) :
            print('As retas {:.1f}, {:.1f} e {:.1f} formam um tringulo!'.format(r1, r2, r3))
        else:
            print('As retas {:.1f}, {:.1f} e {:.1f} nao formam um tringulo!'.format(r1, r2, r3))
    else:
            print('As retas {:.1f}, {:.1f} e {:.1f} nao formam um tringulo!'.format(r1, r2, r3))
else:
            print('As retas {:.1f}, {:.1f} e {:.1f} nao formam um tringulo!'.format(r1, r2, r3))
'''

# Cores no Terminal em Python!
# Para adicionar cores no padrao ANSI usando escape sequence basta utilizar a seguinte expressao
# \033[STYLE;TEXT;BACKGROUNDm
# Ex.: \033[0;33;44m

# Estilo: 0 --> sem estilo
#         1 --> negrito
#         4 --> sublinhado
#         7 --> negativo

# Texto: 30 --> branco
#        31 --> vermelho
#        32 --> verde
#        33 --> amarelo
#        34 --> azul
#        35 --> roxo
#        36 --> ciano
#        37 --> cinza

# Backg: 40 --> branco
#        41 --> vermelho
#        42 --> verde
#        43 --> amarelo
#        44 --> azul
#        45 --> roxo
#        46 --> ciano
#        47 --> cinza

# Obs.: para retornar pro padrao do terminal basta fazer \033[m

'''
#Ex.:
print('\033[7mOla mundo\033[m')

    #uso do .format para facilitar o uso de cores
nome = 'Gustavo'
print('Ola {}{}{} !!'.format('\033[36m', nome, '\033[m'))

    #criacao de uma lista de cores
cores = {'limpa':'\033[m', 'azul':'\033[34m'} 
print('Ola {}{}{} !!'.format(cores['azul'], nome, cores['limpa']))
'''

#TESTE MUNDO 1 PYTHON
