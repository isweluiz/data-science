# -*- coding: utf-8 -*-
"""Spyder Editor
"""
##Autor: Luiz Eduardo
## Data: 03/05/2018

#Resposta para a lista de exercícios de nome lista_exercicios01
# Algumas resoluções não estão nessa lista - 
#
#
#
import pandas as pd
import numpy as np


x = ["Oi!", 2/3, 4/4, 2**2, 10 < 100]   
type(x[0])  #Utilizado para saber o tipo de dado do primeiro índece 
type(x[1])
type(x[2])
type(x[3])
type(x[4])


# 4 - a
x = list(range(0,9))
x
# 5 - a
x = "Eu adoro estudar estatı́stica!"
y = " e"
y = x[8:10]
y

#Ex 6 - b
y = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
y

#Ex 7 - a
dict = {'a'+str(i): 10 ** i for i in range(0,10)}
dict

#Ex 16
x = [3, 15, 23, 31, 42, 57, 68, 71, 73, 98]
np.mean(x)
np.var(x)
np.std(x)



#Ex 17 
x = {3, 15, 23, 31, 42, 57, 68, 71, 73, 98}
media = (42+57)/2
media
primeiroq = (15+23)/2
primeiroq
terceiroq = (73+78)/2
terceiroq

#Ex 18
x = [6, 24, 34, 35, 45, 45, 56, 65, 85]
np.mean(x)
np.var(x)
np.std(x)

#Ex 19
x = [6, 24, 34, 35, 45, 45, 56, 65, 85]
mediana = 45
pq = (24+34)/2
pq
tq = (56+65)/2
tq

#Ex 24
x = [1, 4, 8, 9, 12, 15, 20]
np.std(x)
x = [i+1000 for i in x]

#Ex 25
x = [1, 4, 8, 9, 12, 15, 20]
np.std(x)
x = [i*1000 for i in x]


#Ex 20
x = [1, 4, 8, 9, 12, 15, 20]
np.mean(x)
np.sum(x) #Numerador 69
len(x) #Denominador 7 
media = (69/7)
media

#Ex 21
x = [1, 4, 8, 9, 12, 15, 20]
np.var(x)
###Media
#Numerador 69
#Denominador 7 
# Exemplo de como calcular a variância https://pt.wikihow.com/Calcular-a-Vari%C3%A2ncia
media = (69/7)
media
x1 =  1  - media
x1**2 # - 8  =78
x2 =  4 - media  
x2**2  # - 5 = 34
x3 =  8  - media 
x3**2 #  - 1 == 3
x4 =  9 - media 
x4**2 #  - 0   = 0 
x5 =  12 - media 
x5 **2 #  2 = 4
x6 =  15 - media
x6**2 # 5 = 26
x7 =  20 - media 
x7 **2  #  10 = 102

soma = 78 + 34 + 3 + 0 + 4 + 26 + 102
soma # 247
vari = (247/7)
vari

np.std(x)

#Ex 22
x = [22, 44, 48, 49, 49, 56, 69, 85, 86]
np.mean(x)
len(x)
sum(x)

#Ex 23
x = [22,44, 48, 49, 49, 56, 69, 85, 86]
np.var(x)
#Media 56
#Numerador 508
#Denominador 9
media = np.mean(x)
media
#Observações menos a média
ob1 = 22 - media 
ob1 
ob1m = ob1**2  #Resultado da soma da media menos as observações ao quadrado
ob1m

ob2 = 44 - media
ob2
ob2m = ob2 ** 2
ob2m

ob3 = 48 - media
ob3
ob3m = ob3**2
ob3m

ob4 = 49 - media
ob4
ob4m = ob4 **2
ob4m

ob5 = 49 - media
ob5
ob5m = ob5 **2 
ob5m

ob6 = 56 - media
ob6
ob6m = ob6 **2
ob6m

ob7 = 69 - media
ob7
ob7m = ob7 **2
ob7m

ob8 = 85 - media
ob8
ob8m = ob8 **2
ob8m

ob9 = 86 - media
ob9
ob9m = ob9 **2
ob9m

soma_ob = (ob1m+ob2m+ob3m+ob4m+ob5m+ob6m+ob7m+ob8m+ob9m)/9
soma_ob




#------------
# 1 = c String; Float; Integer; Integer; Boolean.
# 2 = b  3
# 3 = b 3
# 4 = a x = list(range(0,9))
# 5 = a y = x[8:10]
# 6 = b y = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# 7 = a  dict = {'a'+str(i): 10 ** i for i in range(0,10)}
# 8 = a Quantitativa discreta
# 9 = b Quantitativa contínua
# 10 = c Qualitativa categoria
#11 = c Qualitativa categorica
#12 = d Reais e racionais
#13 = a (corte transversal ou cross-section)
#14 = b series temporais
#15 = c Dados em paineis
#16 
##A = 48.10
##B = 819.88
##C = 28.633
#17
##a = Peimeiro quartil 19.0
##b = A mediana - 49.5
##c = O terceiro quartil 75.5
##d = intervalo interquartil - 98
#18
##a = Media - 43.88
##b = variância - 476.98
##c = 21.84
#19 
##A = primeiro quartul  - 29.0
##B =Mediana = 45
##C = 60.5
##D Intervalo interquartil - 85
#20
##(a) O numerador da média. = 67
##(b) O denominador da média. =  7
##(c) A média. = 9 
##21
##(a) O numerador da variância.  = 247 
##(b) O denominador da variância. = 7 
##(c) A variância. -  = 35
##(d) O desvio padrão = 5
#22
##(a) O numerador da media.= 508
##(b) O denominador da media. =  9 
##(c) A media. = 56
#23
#(a) O numerador da vari^ancia. = 3374
#(b) O denominador da vari^ancia. =  9
#(c) A variância. = 374
#(d) O desvio padrão
#24 - C = Manter-se inalterado
#25 - A = Aumentar
#26 - D = Ajustar o eixo Y fazendo com que ele comece do 0
#27 - A = 4,75 - 8 - 9,75 - 12
#28  (a) 5% e 8%; 15% e 45%; 51% e 95%.
#29 
#30
#31 
##A - PMDB 2273
## B - PT -1179
## C - 1242
## D - 624
#32 
## A - Dois candidatos a prefeito - 2582
## B - Três candidatos a prefeito - 1564 
## C - Quatro candidatos a prefeito - 690
## D - Cinco candidatos a prefeito - 321
#33  
## (a) Campo Grande. 15156
#34
##(a) PCdoB -- False
##(b) PCO. --  True
##(c) PSDB.---Truue
##(d) PRB. --True
##(e) PT. -- True
##(f) REDE. -- True
#------------


