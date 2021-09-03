# Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

# Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
# DDD nao cadastrado

# Entrada
# A entrada consiste de um único valor inteiro.

# Saída
# Imprima o nome da cidade correspondente ao DDD existente na entrada. Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.

codigo = int(input())

if(codigo == 11): print("Sao Paulo")
elif(codigo == 19): print("Campinas")
elif(codigo == 21): print("Rio de Janeiro")
elif(codigo == 27): print("Vitoria")
elif(codigo == 31): print("Belo Horizonte")
elif(codigo == 32): print("Juiz de Fora")
elif(codigo == 61): print("Brasilia")
elif(codigo == 71): print("Salvador")
else: print("DDD nao cadastrado")
