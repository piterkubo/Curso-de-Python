# Mais Operadores(Membros/Indentidade)

lista = [1,2,3, 'Ana', 'Karla']

#procurando por operador de membro 
print(2 in lista)

print('Ana' not in lista)








# Ex operador por indentidade

x = 3 

y = x

z = 3

#operador por indentidade
print (x is y)

print(x is not z)




# outro exemplo

lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]


# quando é comparado em lista a comparação por mais que seja os mesmos valores, as listas são armazenada em lugares diferente em memoria
print(lista_a is lista_b)
print(lista_b is lista_c)
print(lista_a is not lista_c)