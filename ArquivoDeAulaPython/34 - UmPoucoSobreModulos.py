# Um Pouco Sobre Modulos


# Chamando os modulos para ver seu tipo.




#!C:\Users\Kubo\AppData\Local\Programs\Python\Python312\python.exe


from math import pi

raio = float(input('Informe o raio: '))

print(f'Area da circuferencia e', pi * (raio**2) )


print("Nome do modulo", __name__)
print("Nome do pacote", __package__)
