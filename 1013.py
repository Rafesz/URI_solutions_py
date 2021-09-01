# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

# Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

linhasValores = input()
valores = linhasValores.split(' ')

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maiorAB = (a+b+abs(a-b))/2
maior = int((maiorAB+c+abs(maiorAB-c))/2)

print("{} eh o maior".format(maior))