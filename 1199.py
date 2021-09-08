# Neste problema você é solicitado a escrever um simples programa de conversão de base. A entrada será um valor hexadecimal ou decimal. Você deverá converter cada valor da entrada. Se o valor for hexadecimal, você deve convertê-lo para decimal e vice-versa. O valor hexadecimal inicia sempre com “0x” ou também, é aquele valor cuja segunda casa contém a letra 'x'.

# Entrada
# A entrada contém vários casos de teste. Cada linha de entrada, com exceção da última, contém um número não-negativo, decimal ou hexa. O valor decimal será menor ou igual a 231. A última linha contém um número negativo que não deve ser processado, indicando o encerramento do programa.

# Saída
# Para cada linha de entrada (exceto a última) deve ser produzido uma linha de saída. Todo número hexadecimal deve ser precedido na saída por '0x' (zero xis).

while(True):
    valor = input()

    if(valor.startswith('-')): break

    else: 
        if(valor.startswith('0x')):
            dec = int(valor, 16)
            print(dec)
        else:
            valorHex = hex(int(valor))[2:]
            print("0x{}".format(valorHex.upper()))
