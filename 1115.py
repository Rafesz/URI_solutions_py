# Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).

# Entrada
# A entrada contém vários casos de teste. Cada caso de teste contém 2 valores inteiros.

# Saída
# Para cada caso de teste mostre em qual quadrante do sistema cartesiano se encontra a coordenada lida, conforme o exemplo.

while(True):
    valores = input().split(' ')
    x = int(valores[0])
    y = int(valores[1])

    if(x>0 and y>0): print("primeiro")
    if(x<0 and y>0): print("segundo")
    if(x<0 and y<0): print("terceiro")
    if(x>0 and y<0): print("quarto")

    if(x==0 or y==0): break
