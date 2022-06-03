#Escreva uma função que recebe uma lista de números;
#Calcule a média dos números da lista;

from statistics import median


def calc_media(lista):
  media = 0
  soma = 0

  for n in lista:
    #soma = soma + n
    soma += n

  media = soma / len(lista)

  return media

notas = [9,8,7,3]

media_prova = calc_media(notas)
print(notas)
print(media_prova)