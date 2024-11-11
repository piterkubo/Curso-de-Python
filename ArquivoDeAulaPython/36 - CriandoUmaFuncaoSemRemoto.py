# Criação de funções

#!C:\Users\Kubo\AppData\Local\Programs\Python\Python312\python.exe

from math import pi


def circulo(raio):
    print('Area do circulo e', pi * (raio**2))


raio = float(input("Digite o valor do raio: "))
circulo(raio)