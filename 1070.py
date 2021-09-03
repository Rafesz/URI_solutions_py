# Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

# Entrada
# A entrada será um valor inteiro positivo.

# Saída
# A saída será uma sequência de seis números ímpares.

i = 0
x = int(input())

if(x%2 == 0):
    x += 1
    print(x)
    while(i < 5):
        x += 2
        print(x)
        i += 1
else:
    print(x)
    while(i < 5):
        x += 2
        print(x)
        i += 1
