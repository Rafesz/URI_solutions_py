# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

codigoEQuant = input()

codigo = int(codigoEQuant.split(' ')[0])
quant = int(codigoEQuant.split(' ')[1])

if(codigo == 1):
    print("Total: R$ {:.2f}".format(quant * 4.00))
elif(codigo == 2):
    print("Total: R$ {:.2f}".format(quant * 4.50))
elif(codigo == 3):
    print("Total: R$ {:.2f}".format(quant * 5.00))
elif(codigo == 4):
    print("Total: R$ {:.2f}".format(quant * 2.00))
elif(codigo == 5):
    print("Total: R$ {:.2f}".format(quant * 1.50))