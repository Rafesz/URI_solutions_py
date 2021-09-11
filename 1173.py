# Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

# Entrada
# A entrada contém um valor inteiro (V<=50).

# Saída
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.

listaVetores = []

v = int(input())
listaVetores.append(v)

i = 1

while(i < 10):
    v*=2
    listaVetores.append(v)
    i += 1

for index in range(len(listaVetores)):
    print("N[{}] = {}".format(index, listaVetores[index]))
