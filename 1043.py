# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

# Perimetro = XX.X

# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

# Area = XX.X

# Entrada
# A entrada contém três valores reais.

# Saída
# O resultado deve ser apresentado com uma casa decimal.

valores = input()

a = float(valores.split(' ')[0])
b = float(valores.split(' ')[1])
c = float(valores.split(' ')[2])

if(abs(b-c) < a < (b+c)):
    print("Perimetro = {:.1f}".format(a+b+c))
else:
    areaTrap = ((a+b)*c)/2
    print("Area = {:.1f}".format(areaTrap))