# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

# Entrada
# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

i = 0
listaVetores = []

while(i < 10):
    vetor = int(input())
    if(vetor<=0): listaVetores.append(1)
    if(vetor>0): listaVetores.append(vetor)
    i += 1
for index in range(len(listaVetores)):
    print("X[{}] = {}".format(index, listaVetores[index]))
