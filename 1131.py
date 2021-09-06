# A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:

# - Quantos GRENAIS fizeram parte da estatística.
# - O número de vitórias do Inter.
# - O número de vitórias do Grêmio.
# - O número de Empates.
# - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

# Entrada
# O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

# Saída
# Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

totalGolsInter = 0
totalGolsGremio = 0
vitoriasInter = 0
vitoriasGremio = 0
vencedor = ''
empate = 0
contador = 0
flagGrenal = True

while(True):
    while(flagGrenal):
        grenal = input().split(' ')
        
        golsInter = int(grenal[0])
        golsGremio = int(grenal[1])

        if(golsInter > golsGremio): vitoriasInter += 1
        if(golsGremio > golsInter): vitoriasGremio += 1
        if(golsGremio == golsInter): empate += 1

        if(vitoriasInter > vitoriasGremio): vencedor = 'Inter'
        else: vencedor = 'Gremio'

        totalGolsGremio += golsGremio
        totalGolsInter += golsInter
        contador += 1
        flagGrenal = False

    print("Novo grenal (1-sim 2-nao)")
    novoGrenal = input()

    if(novoGrenal == '1'):
        flagGrenal = True

    if(novoGrenal == '2'): 
        print("{} grenais\nInter:{}\nGremio:{}\nEmpates:{}\n{} venceu mais"
                .format(contador, vitoriasInter, vitoriasGremio, empate, vencedor))
        break
