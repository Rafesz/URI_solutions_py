# Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

# Entrada
# A entrada contém 20 valores inteiros, positivos ou negativos.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

i = 0
n = 19
listaVetores = []

while(i < 20):
    vetor = int(input())
    listaVetores.append(vetor)
    i += 1
for index in range(len(listaVetores)):
    print("N[{}] = {}".format(index, listaVetores[n]))
    n -= 1
