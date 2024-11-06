#Tuplas ()

# Tuplas não pode ser modificadas!!!

tupla = tuple()

tupla = ()

print(type(tupla))

'''
Se adicionar elementos dentro de uma tupla, tomar cuidados. 

Caso a tupla seja declarado assim tupla = ('Um');

O type sera uma string

Para deixar o type como tupla, a declaração correta é colocar uma virgula no final ex: tupla = ('Um',)


'''
tupla = ('Um',)

#Acessando um elemento da tupla
print(tupla[0])



#criando uma tupla e acessando os elementos 
cores = ('verde','amarelo','azul', 'branco')
print(type(cores))

print(cores[0])
print(cores[-1])
print(cores[1:])
print(cores.index('amarelo'))


#Contar quantos azul tem dentro de uma tupla
print(cores.count('azul'))


#contando quantos elementos tem dentro de uma tupla

print(len(cores))