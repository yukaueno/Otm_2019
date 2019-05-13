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

B = np.array([[1,0],[0,1]])
N = np.array([[1,2],[2,1]])
b = np.array([[10],[10]])
Bi = [3,4]
Ni = [1,2]
cB = [0,0]
cN = [-1,-1]

print("B\n",(B))
print("N\n",(N))
print("b\n",(b))
print("Bi\n",(Bi))
print("Ni\n",(Ni))
print("cB\n",(cB))
print("cN\n",(cN))

# {calculo da solucao basica factivel}

Binv = np.linalg.inv(B)
xB = np.matmul(Binv,b)
xN = np.zeros(len(N[0]))

print("Solucao basica\n",(xB,xN))

# checando se a solucao basica encontrada eh factivel
if (all(i>=0 for i in xB)) == False:
	print("Solucao basica encontrada nao eh factivel")

# {inicio da iteracao}
# enquanto nao encontrar a solucao ou nao alcancar itr iteracoes

itr = 1
status = False

iteracao = 0
while status == False and iteracao <= itr:
	# {calculo dos custos reduzidos}

	lambdaT = np.matmul(cB,Binv)

	print("lambdaT\n",(lambdaT))	

	cNT_l = np.zeros(len(cN))

	for j in range(len(N[0])):
		cNT_l[j] = cN[j] - np.matmul(lambdaT,N[j])

	# verificando se os custos sao positivos

	k = -1
	print("cNT_l\n", cNT_l)
	for j in range(len(cNT_l)):
		if (cNT_l[j] < 0):
			k = j 

	# se todos os custos sao positivos
	# a solucao corrente eh otima
	if (k == -1):
		print("Encontramos uma solucao otima")
		status = True
		break
	# senao vamos escolher j com cNT_l[j] < 0
	else: 
		print("Elemento que vai entrar: k = ",k)
		dB = np.negative(np.matmul(Binv,N[k]))
		epsilon = []
	
		print("dB\n",(dB))
		for i in range(len(dB)):
			if (dB[i] < 0):
				epsilon.append(-xB[i]/dB[i])
		print("epsilon\n",epsilon)	
		# se nao existir epsilon, significa que o problema nunca se torna infactivel
		if epsilon == []:
			print("A solucao otima eh -infinito")
			status = True
		else:
			# calculando o minimo dos epsilons obtidos
			# encontrando o indice do primeiro minimo dentre os elemetos de epsolons
			# supomos que o primeiro elemento eh o minimo
			epsilone = epsilon[0]	
			epsiloni = 0
			# comparamos com o resto dos elementos
			# caso encontramos algum elemento que seja menor, atualizamos a variavel auxiliar
			for index in range(len(epsilon)):
				if epsilone > epsilon[index]:
					epsilone = epsilon[index]
					epsiloni = index

			print("Elemento que vai sair: ",Bi[epsiloni])
		
			# nova solucao basica apos a mudanca de base
			#B = [[1,0],[0,1]]
			#N = [[1,2],[2,1]]
			#b = [[10],[10]]
			#Bi = [3,4]
			#Ni = [1,2]
			#cB = [0,0]
			#cN = [-1,-1]
			
			auxB = []
			for b in B[:,epsiloni]:
				auxB.append(b)
			auxB = np.array(auxB)	
			auxN = N
			print("auxB\n",auxB)
			print("auxN\n",auxN)
			B[:,epsiloni] = N[:,k]
			print("auxB\n",auxB)
			N[:,k] = auxB
			
			# Atualizando os indices
			auxi = Bi[epsiloni]
			Bi[epsiloni] = k + 1
			print("k\n",k)
			Ni[k] = auxi
			
			# Atualizando os custos
			auxci = cB[epsiloni]
			cB[epsiloni] = k + 1
			cN[k] = auxci
			print("Valores atualizados")
			print("B",(B))
			print("N",(N))
			print("Bi",(Bi))
			print("Ni",(Ni))
			
			# {calculo da solucao basica}	
			xB[epsiloni] = xB[epsiloni] + epsilone*dB[epsiloni]
			xN[k] = epsilone 

			print("Solucao basica\n",(xB,xN))

			iteracao = iteracao + 1
			print("iteracao: ",itr)
