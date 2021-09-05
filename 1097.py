# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.

i = 1
j = 7
n = 1

while(i <= 9):
    while(n <= 3):
        print("I={} J={}".format(i, j))
        j -= 1
        n += 1
    j += 5
    i += 2
    n = 1
