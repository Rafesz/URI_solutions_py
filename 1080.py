# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

i = 0
listaValores = []

while(i < 100):
    valor = int(input())
    listaValores.append(valor)
    i += 1

valorMax = max(listaValores)
indiceValorMax = listaValores.index(valorMax)

print("{}\n{}".format(valorMax,indiceValorMax + 1))
