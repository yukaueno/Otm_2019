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
N = np.array([[-1,1],[2,-1]])
b = np.array([[2],[6]])
Bi = [3,4]
Ni = [1,2]
cB = [0,0]
cN = [-1,-1]

print("B",(B))
print("N",(N))
print("Bi",(Bi))
print("Ni",(Ni))
print("cB",(cB))
print("cN",(cN))

# {calculo da solucao basica factivel}

Binv = np.linalg.inv(B)
xB = np.dot(Binv,b)
xN = np.zeros((len(N[0]),1))

print("Solucao basica ",(xB,xN))

print("###################################################")

# checando se a solucao basica encontrada eh factivel
if (all(i>=0 for i in xB)) == False:
	print("Solucao basica encontrada nao eh factivel")

# {inicio da iteracao}
# enquanto nao encontrar a solucao ou nao alcancar itr iteracoes

#==============================================================
itr = 5 
#==============================================================

status = False
iteracao = 0

while status == False and iteracao <= itr:

	# {calculo dos custos reduzidos}

	lambdaT = np.dot(cB,Binv)

	print("lambdaT",(lambdaT))	

	cNT_l = np.zeros(len(cN))

	for j in range(len(N[0])):
		cNT_l[j] = cN[j] - np.dot(lambdaT,N[j])

	# verificando se os custos sao positivos

	j = -1 
	find = False
	print("cNT_l\n", cNT_l)
	for i in range(len(cNT_l)):
		if (cNT_l[i] < 0) and find == False:
			j = i
			find == True 

	# se todos os custos sao positivos
	# a solucao corrente eh otima
	if (j == -1):
		print("Encontramos uma solucao otima")
		status = True
		break
	# senao vamos escolher j com cNT_l[j] < 0
	else: 
		print("Elemento que vai entrar: j = ",j)

		dB = np.negative(np.dot(Binv,N[j]))	
		print("dB ",(dB))
		
		l = []
		e = []
		for i in range(len(dB)):
			if (dB[i] < 0):
				l.append(i)
				e.append(-xB[i]/dB[i])
		print("l ",l)	
		# se todos os componentes de dB forem positivos temos que o problemas eh infactivel
		if l == []:
			print("A solucao otima eh -infinito")
			status = True
			break
		else:
			# calculando o minimo dos epsilons obtidos
			# encontrando o indice do primeiro minimo dentre os elemetos de epsolons
			# supomos que o primeiro elemento eh o minimo
			l = 0
			emin = e[0]
			# comparamos com o resto dos elementos
			# caso encontramos algum elemento que seja menor, atualizamos a variavel auxiliar
			for i in range(len(e)):
				if emin > e[i]:
					emin = e[i]
					l = i

			print("Elemento que vai sair: ",Bi[l])
		
			# nova solucao basica apos a mudanca de base
			#B = [[1,0],[0,1]]
			#N = [[1,2],[2,1]]
			#b = [[10],[10]]
			#Bi = [3,4]
			#Ni = [1,2]
			#cB = [0,0]
			#cN = [-1,-1]
			
			auxB = []
			for b in B[:,l]:
				auxB.append(b)
			auxB = np.array(auxB)	
			auxN = N
			print("auxB\n",auxB)
			print("auxN\n",auxN)
			B[:,l] = N[:,j]
			print("auxB\n",auxB)
			N[:,j] = auxB
			
			# Atualizando os indices
			auxl = Bi[l]
			Bi[l] = Ni[j]
			Ni[j] = auxl
			
			# Atualizando os custos
			auxci = cB[l]
			cB[l] = Ni[j]
			cN[j] = auxci
			print("Valores atualizados")
			print("B",(B))
			print("N",(N))
			print("Bi",(Bi))
			print("Ni",(Ni))
			
			# {calculo da solucao basica}	
			for ib in range(len(xB)):
				if ib != l:
					xB[ib] = xB[ib] + emin*dB[ib]
			xN[j] = emin 
			
			print("###########################################")
			print("Solucao basica\n",(xB,xN))

			iteracao = iteracao + 1
			print("iteracao: ",itr)
