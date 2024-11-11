# ObtendoArgumentosViaTerminal com sys


'''

    para obter os argumentos sem usar o input diretamente no terminal é necessario
    declarar a tecla sys.

    OBS: chama o nome do arquivo via terminal com espaço e o valor.


'''

#!C:\Users\Kubo\AppData\Local\Programs\Python\Python312\python.exe

from math import pi
import sys

def circulo(raio):
    return pi * float(raio) **2


raio = sys.argv[1]
area = circulo(raio)

print(f'A area do circulo: ', area)

