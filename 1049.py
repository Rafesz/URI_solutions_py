# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

def vertebrado(palavra2, palavra3):
    if(palavra2 == 'ave' and palavra3 == 'carnivoro'): return "aguia"
    if(palavra2 == 'ave' and palavra3 == 'onivoro'): return "pomba"
    if(palavra2 == 'mamifero' and palavra3 == 'onivoro'): return "homem"
    if(palavra2 == 'mamifero' and palavra3 == 'herbivoro'): return "vaca"
    

def invertebrado(palavra2, palavra3):
    if(palavra2 == 'inseto' and palavra3 == 'hematofago'): return "pulga"
    if(palavra2 == 'inseto' and palavra3 == 'herbivoro'): return "lagarta"
    if(palavra2 == 'anelideo' and palavra3 == 'hematofago'): return "sanguessuga"
    if(palavra2 == 'anelideo' and palavra3 == 'onivoro'): return "minhoca"

palavra1 = input()
palavra2 = input()
palavra3 = input()

if(palavra1 == 'vertebrado'): print(vertebrado(palavra2, palavra3))
else: print(invertebrado(palavra2, palavra3))
