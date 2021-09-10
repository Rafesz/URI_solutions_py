# Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

# Entrada
# A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

# Saída
# Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.

i = 0
listaVetores = []

while(i < 100):
    vetor = float(input())
    if(vetor<=10): listaVetores.append(str(vetor))
    if(vetor>10): listaVetores.append('nulo')
    i += 1

for idx in range(len(listaVetores)):
    if(listaVetores[idx] != 'nulo'):
        print("A[{}] = {}".format(idx, listaVetores[idx]))
