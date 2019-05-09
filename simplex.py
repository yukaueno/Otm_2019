######################################
# Implementacao do SIMPLEX em Python
######################################

######################################
# Bibliotecas que serao utilizadas 
######################################
import numpy as np

######################################
# Supondo que temos o seguinte problema

# minimizar f(x)=cTx
# sujeita a Ax = b, x >= 0

######################################

# FASE I
# E que sao dados A = [B N]
# tal que B^-1 existe e xB = B^-1b >= 0

B = [[1,0],[0,1]]
N = [[1,2],[2,1]]
b = [[10],[10]]

print((B,N))

# FASE II
# {inicio da iteracao simplex}

#  Passo 1: {calculo da solucao basica}

Binv = np.linalg.inv(B)
print((Binv))

xB = Binv*b
 

