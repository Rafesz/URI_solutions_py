# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

i = 0
contadorPares = 0

while(i < 5):
    valor = int(input())
    if(valor%2 == 0): contadorPares += 1
    i+=1

print("{} valores pares".format(contadorPares))
