# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU X HORA(S) E Y MINUTO(S)” .

valores = input()

horaInicio = int(valores.split(' ')[0])
minInicio = int(valores.split(' ')[1])
horaFim = int(valores.split(' ')[2])
minFim = int(valores.split(' ')[3])

def calculaHora(horaInicio, horaFim):
    horaTotal=0
    if(horaFim > horaInicio):
        horaTotal = horaFim - horaInicio
    elif(horaFim < horaInicio):
        horaTotal = (24-horaInicio) + horaFim
    return horaTotal
        
if(minInicio > minFim):
    minTotal = 60 - (minInicio - minFim)
    horaFim -= 1
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(calculaHora(horaInicio, horaFim), minTotal))

if(minFim > minInicio):
    minTotal = minFim - minInicio
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(calculaHora(horaInicio, horaFim), minTotal))

if(minInicio == minFim == horaInicio == horaFim):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")