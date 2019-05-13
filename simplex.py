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

# {inicio da iteracao simplex}
# Sao dados A = [B N]
# tal que B^-1 existe e xB = B^-1b >= 0

B = [[1,0],[0,1]]
N = [[1,2],[2,1]]
b = [[10],[10]]
Bi = [3,4]
Ni = [1,2]
cB = [0,0]
cN = [-1,-1]

# {calculo da solucao basica factivel}

Binv = np.linalg.inv(B)
xB = np.matmul(Binv,b)
xN = np.zeros(len(N[0]))

print("Solucao basica")
print((xB,xN))

# checando se a solucao basica encontrada eh factivel
if (all(i>=0 for i in xB)) == False:
	print("Solucao basica encontrada nao eh factivel")

# {calculo dos custos reduzidos}
lambdaT = np.matmul(cB,Binv)
print((lambdaT))	
cNT_l = np.zeros(len(cN))

for j in range(len(N[0])):
	cNT_l[j] = cN[j] - np.matmul(lambdaT,N[j])

# verifica se os custos sao positivos
# se todos os custos sao positivos
# a solucao corrente eh otima
# senao vamos escolher j com cNT_l[j] < 0 
k = -1

for j in range(len(cNT_l)):
	if (cNT_l[j] < 0):
		k = j
if (k == -1):
	print("Encontramos uma solucao otima")
else: 
	dB = np.negative(np.matmul(Binv,N[k]))
	epsilon = []
	
	print("dB")
	print((dB))
	for i in range(len(dB)):
		if (dB[i] < 0):
			epsilon.append(-xB[i]/dB[i])
			
	if epsilon == []:
		print("A solucao otima eh -infinito")
	else:
		# calculando o minimo dos episolons obtidos
		# encontrando o indice
		aux = epsilon[0]	
		epsiloni = 0
		for index in range(len(epsilon)):
			if aux > epsilon[index]:
				aux = epsilon[index]
				epsiloni = index
		print("Epsilon")
		print((epsiloni))
		# nova solucao basica apos a mudanca de base
		#B = [[1,0],[0,1]]
		#N = [[1,2],[2,1]]
		#b = [[10],[10]]
		#Bi = [3,4]
		#Ni = [1,2]
		#cB = [0,0]
		#cN = [-1,-1]
		
		#PROBLEMAS AQUI....
		auxB = B
		auxN = N
		B[:,epsiloni] = auxN[:,k]
		N[:,k] = auxB[:epsiloni]
		
		# Atualizando os indices
		for b in Bi:
			if b == index:
				Bi = k
				break
		for n in Ni:
			if n == k:
				Ni = index
				break

		print("Valores atualizados")
		print("B",(B))
		print("N",(N))
		print("Bi",(Bi))
		print("Ni",(Ni))
		 
