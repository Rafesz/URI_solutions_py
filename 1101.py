# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

while(True):
    valores = input().split(' ')
    m = int(valores[0])
    n = int(valores[1])

    if(m > n):
        listaValores = list(range(n,m+1))

    if(n > m):
        listaValores = list(range(m,n+1))

    if(m <= 0 or n <= 0): break

    for valor in listaValores:
        print("{}".format(valor),end=" ")
    
    print("Sum={}".format(sum(listaValores)))
