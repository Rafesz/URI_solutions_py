# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

totalSegundos = int(input())

horas = int(totalSegundos/3600)
totalSegundos = totalSegundos % 3600

minutos = int(totalSegundos/60)
totalSegundos = totalSegundos % 60

segundos = totalSegundos

print("{}:{}:{}".format(horas, minutos, segundos))