# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

x = int(input())
y = int(input())

soma = 0

if(x < y):
    while(x < y):
        x += 1
        if(x%2 == 1 and x != y): soma += x 

if(y < x):
    while(y < x):
        y += 1
        if(y%2 == 1 and y != x): soma += y

print(soma)
