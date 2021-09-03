# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.

i = 0
contadorPos = 0
contadorNeg = 0
contadorPares = 0
contadorImp = 0


while(i < 5):
    valor = int(input())
    if(valor%2 == 0): contadorPares += 1
    if(valor%2 == 1): contadorImp += 1
    if(valor>0): contadorPos += 1
    if(valor<0): contadorNeg += 1
    i += 1

print("{} valor(es) par(es)\n{} valor(es) impar(es)\n{} valor(es) positivo(s)\n{} valor(es) negativo(s)"
        .format(contadorPares, contadorImp, contadorPos, contadorNeg))
