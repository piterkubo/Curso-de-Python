# AdicionandoRetornoAFuncao

#!C:\Users\Kubo\AppData\Local\Programs\Python\Python312\python.exe

from math import pi


def circulo(raio):
    return pi * (raio**2)


raio = float(input("Digite o valor do raio: "))
area = circulo(raio)

print(f'A area do circulo: ', area)


# Para invocar a funçõa em um novo programa

#import (nome da funcao) as apelido