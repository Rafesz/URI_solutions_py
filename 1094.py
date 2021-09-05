# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

i = 0

n = int(input())

total = 0
totalCoelhos = 0
totalRatos = 0
totalSapos = 0

while(i < n):
    teste = input().split(' ')
    quantia = int(teste[0])
    tipo = teste[1]

    if(tipo == 'C'): totalCoelhos += quantia
    if(tipo == 'R'): totalRatos += quantia
    if(tipo == 'S'): totalSapos += quantia

    total += quantia

    i += 1

print(
    "Total: {} cobaias\nTotal de coelhos: {}\nTotal de ratos: {}\nTotal de sapos: {}\n"
        .format(total, totalCoelhos, totalRatos, totalSapos) +
    "Percentual de coelhos: {:.2f} %\nPercentual de ratos: {:.2f} %\nPercentual de sapos: {:.2f} %"
        .format((totalCoelhos/total) * 100, (totalRatos/total) * 100, (totalSapos/total) * 100)
    )
