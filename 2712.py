# O rodízio municipal de veículos de São Paulo é uma restrição à circulação de veículos automotores na cidade. Implantado desde 1996 com o propósito de melhorar as condições ambientais reduzindo a carga de poluentes na atmosfera, se consolidou como um instrumento para reduzir congestionamentos nas principais vias da cidade, nos horários de maior movimento. Nas vias delimitadoras não é permitido o tráfego de caminhões e automóveis que estejam dentro da restrição. Há uma escala que determina em quais dias da semana quais veículos não podem circular. Essa escala é regida pelo último dígito da placa do veículo, sendo:

# Segunda-feira, digito final da placa 1 e 2
# Terça-feira, digito final da placa 3 e 4
# Quarta-feira, digito final da placa 5 e 6
# Quinta-feira, digito final da placa 7 e 8
# Sexta-feira, digito final da placa 9 e 0
# Os motoristas que são flagrados violando a restrição de circulação são autuados com multa e quatro pontos na carteira de habilitação.

# Entrada
# A primeira linha de entrada representa a quantidade de testes N (0 <= N < 1000) que deverão ser considerados. As demais entradas são cadeia de caracteres com tamanho máximo S (1 <= S <= 100) que representam cada placa que deverá ser analisada, de tal forma que, cada placa fique em uma única linha de entrada. O formato esperado para uma placa veicular válida em São Paulo é "AAA-9999", tal que A é um caracter válido em [A-Z], e 9 um dígito numérico válido em [0-9].

# Saída
# O conjunto de valores válidos como saída são: MONDAY, TUESDAY, WEDNESDAY, THURSDAY e FRIDAY, de acordo com a tabela de restrições predefinida, e FAILURE caso a placa não apresente o padrão definido.

def confereHifen(placa):
    if(len(placa) < 8 or placa[3] != '-'): return False

def confereTamanLetras(placa):
    letras = placa.split('-')[0]
    if(len(letras) != 3):
        return False

def confereNum(placa):
    numeros = placa.split('-')[1]
    for numero in numeros:
        if(ord(numero)>57 or ord(numero)<48):
            return False

def confereCarac(placa):
    letras = placa.split('-')[0]
    for caracter in letras:
        if(ord(caracter)>90 or ord(caracter)<64):
            return False

def confereTamanNumeros(placa):
    numeros = placa.split('-')[1]
    if(len(numeros) != 4):
        return False

def diaRodizio(placa):
    numeros = placa.split('-')[1]
    if('1'<=numeros[3]<='2'): dia = "MONDAY"
    if('3'<=numeros[3]<='4'): dia = "TUESDAY"
    if('5'<=numeros[3]<='6'): dia = "WEDNESDAY"
    if('7'<=numeros[3]<='8'): dia = "THURSDAY"
    if(numeros[3]=='9' or numeros[3]=='0'): dia = "FRIDAY"
    return print(dia)

i = 0

n = int(input())

while(i < n):
    placa = input() 
    
    if(
        confereHifen(placa) == False or
        confereTamanLetras(placa) == False or
        confereCarac(placa) == False or
        confereNum(placa) == False or
        confereTamanNumeros(placa) == False):
        print("FAILURE")
    else:
        diaRodizio(placa)
    i += 1
