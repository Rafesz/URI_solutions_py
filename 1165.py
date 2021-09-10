# Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 100), indicando o número de casos de teste da entrada. Cada uma das N linhas seguintes contém um valor inteiro X (1 < X ≤ 107), que pode ser ou não, um número primo.

# Saída
# Para cada caso de teste de entrada, imprima a mensagem “X eh primo” ou “X nao eh primo”, de acordo com a especificação fornecida.

i = 0

n = int(input())

while(i < n):
    x = int(input())
    contador = 0
    for valor in range(1, x+1):
        if(x%valor==0): contador += 1
    if(contador==2): print("{} eh primo".format(x))
    if(contador!=2): print("{} nao eh primo".format(x))
    i += 1
