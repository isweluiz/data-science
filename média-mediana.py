# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 16:54:25 2018

@author: Luiz Eduardo
"""

import pandas as pd 
import numpy as np 
import scipy


#Calcúlo de média  com função 

x = [3,1,2,4,15,8,9,20,21]
def media(amostra):
   numerador = sum(amostra) 
   denominador = len(amostra)
   return numerador / denominador
media(x) #Aplicapilidade da função na minha lista x
 
#Aplicando a média com a bibilioteca scipy

scipy.mean(x) #Média com scipy
scipy.median(x) #Mediana

np.mean(x) # Média com numpy
np.median(x) #Mediana 
#################################
x1 = [1,1,1,1,1,19]
y1 = [4,4,4,4,4,4,4]
np.median(x1)
np.mean(x1)

np.median(y1)
np.mean(y1)
#################################









