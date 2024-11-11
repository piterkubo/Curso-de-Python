# Conjuntos {}


# conjuntos é delimitado por chaves{} e recebe apenas valores

'''

* Conjuntos não garante a order de sessao.

* Não é indexado.

* Não aceita repetições


'''


a = {1,2,3}
print(type(a))


# criando um conjunto com string sem ordenação
b = set('codigo')
print(b)


# verificando se há elementos
print(3 in a, 4 not in b)


# verificando se ha elementos! OBS lembrando que o numero repetido é descartado.
print({1,2,3} == {3,2,1,3})



# Operações com conjuntos fazendo a união.
c1 = {1,2}
c2 = {2,3}
print(c1.union(c2))


# Fazendo uma interseção ira mostrar o numero que esta repetido
print(c1.intersection(c2))


# Usando o update ira adicionar o numero que não tem no cj 1.
c1.update(c2) 
print(c1)




# Verificando se um cj é subconjunto de outro cj
print(c2 <= c1)


# Fazendo a diferença entre os cj
print({1,2,3} - {2})


# Fazendo um subtração de cj

c1 -={2}
print(c1)