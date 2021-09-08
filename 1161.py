# Leia dois valores inteiros M e N indefinidamente. A cada leitura, calcule e escreva a soma dos fatoriais de cada um dos valores lidos. Utilize uma variável apropriada, pois cálculo pode resultar em um valor com mais de 15 dígitos.

# Entrada
# O arquivo de entrada contém vários casos de teste. Cada caso contém dois números inteiros M (0 ≤ M ≤ 20) e N (0 ≤ N ≤ 20). O fim da entrada é determinado por eof.

# Saída
# Para cada caso de teste de entrada, seu programa deve imprimir uma única linha, contendo um número que é a soma de ambos os fatoriais (de M e N).

def calculafatorial(valor):
    fatorial = 1
    for valor in range(1, valor+1):
        fatorial *= valor
    return fatorial

while(True):
    try:
        valores = input().split(' ')
        m = int(valores[0])
        n = int(valores[1])

        print(calculafatorial(m) + calculafatorial(n))

    except EOFError:
        break
