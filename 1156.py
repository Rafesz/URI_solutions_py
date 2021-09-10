# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

s = 1
dd = 3
ds = 2

while(dd < 39):
    s += dd/ds
    dd += 2
    ds *= 2

print("{:.2f}".format(s))
