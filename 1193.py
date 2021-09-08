# O professor de matemática de Juliano marcou uma prova cujo conteúdo será apenas conversão entre valores decimais, hexadecimais e binários. Uma das coisas mais complexas para Juliano é fazer estas conversões de base entre números. Por mais que estude, tem muita dificuldade para entender. Portanto, como você entende de computação e é amigo(a) de Juliano, ele solicitou a tua ajuda para que faça um programa que verifique se as conversões feitas por ele estão correta.

# Entrada
# A entrada contém vários casos de teste. A primeira linha da entrada contém um inteiro N, indicando o número de casos de teste que virão a seguir, um por linha. Cada caso de teste contém um valor X (X > 0) seguido de um texto Y com três caracteres, indicando se o valor X está no formato binário, decimal ou hexadecimal. Independente do formato, qualquer dos números deverá caber em um inteiro de 32 bits.

# Saída
# Para cada caso de teste, você deve apresentar o número de caso de teste seguido por duas linhas, que contém a conversão do valor fornecido para as outras duas bases. A sequência das bases de saída será sempre: decimal, hexadecimal (em minúsculo) e binário, ou seja deve-se respeitar esta ordem excluindo obviamente o formato de entrada.

# Obs: deverá ser impressa uma linha em branco após cada caso de teste, inclusive após o último caso de teste.

while(True):
    n = int(input())

    i = 1
    while(i <= n):

        valores = input().split(' ')
        x = valores[0]
        y = valores[1]

        if(y == 'bin'):
            dec = int(x, 2)
            valorHex = hex(dec)[2:]
            print("Case {}:\n{} dec\n{} hex\n".format(i,dec,valorHex))

        if(y == 'dec'):
            x = int(x)
            valorHex = hex(x)[2:]
            valorBin = bin(x)[2:]
            print("Case {}:\n{} hex\n{} bin\n".format(i,valorHex,valorBin))

        if(y == 'hex'):
            dec = int(x, 16)
            valorBin = bin(dec)[2:]
            print("Case {}:\n{} dec\n{} bin\n".format(i,dec,valorBin))

        i += 1
    break
