# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

contador = 0
i = 0

while(i < 6):
    valor = float(input())
    if(valor >= 0): contador += 1
    i += 1

print("{} valores positivos".format(contador))
