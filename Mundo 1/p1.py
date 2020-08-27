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

