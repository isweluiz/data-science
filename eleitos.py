#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 23:13:32 2018
@author: Luiz Eduardo
"""

import pandas as pd
import numpy as np
#import seaborn
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#Importação de dados via httpd utilizando pandas pandas para leitura
eleitos = pd.read_csv(r'prefeito.csv')
eleitos.head() #Exibindo as 10 primeiras linhas
eleitos.dtypes #Lista colunas com os tipos de dados em cada uma
partido_lista = ['PMDB','PT','PSDB','DEM'] #Criando uma lista com os partidos contidos no dataframe
#Contador para checar todos os partidos(coluna) contidos na lista presentes no dataframe
#Resposta ex 31
partido_prefeito = [len(eleitos[eleitos['partido'] == i ]) for i in partido_lista ]
print(partido_prefeito)
eleitos.partido #Exibição de todas as linhas da coluna partido do dataframe
eleitos.columns #Exibição de todas as colunas do dataframe

#Resposta ex 32
#Contas as candidaturas por municipio e exibi o código do municipio
candidaturas = [len(eleitos[eleitos['candidaturas_mun'] == i].groupby("municipio_codigo")) for i in range(2,6)]
print(candidaturas)

#most = eleitos['estado', 'partido', 'populacao', 'ano']
most = eleitos['partido'].value_counts()
most.plot(kind = "bar", color = 'darkred', ) 
#Contando a quantidade de vezes que cada partido é encontrado no dataframe
most

#Nomes , titulos e tals
plt.title('Partidos eleitos por munincipio') #Titulo para o gráfico
plt.xlabel('Partidos') # Legenda para o eixo x
plt.ylabel('') #Legenda para o eixo y
plt.show()

#Ex 33
num_prefeito = eleitos[ eleitos['candidaturas_mun'] == max(eleitos['candidaturas_mun'])]['municipio']
num_prefeito

#Resposta ex 34
estados = eleitos[eleitos['municipio'] == 'SÃO PAULO'] ['partido'] #.value_counts().plot( kind = "bar", grid = "false")
estados









