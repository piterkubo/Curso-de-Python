#Dicionarios Part 02  manipular os dados


pessoa = {'nome': 'Prof(o)Alberto', 'idade':43, 'curso': ['React', 'Python']}



# Modificando uma lista

pessoa['idade'] = 44


# declaração para adicionar um valor  dentro de um dicionario

pessoa['curso'].append('Angular')
print(pessoa)


# Retirando a chave e o valor de um dicionario
pessoa.pop('idade')
print(pessoa)

'''
ou
'''

del pessoa['curso']
print(pessoa)



# Adicionando chave e valor dentro de um dicionario
pessoa.update({'idade':39,'sexo': 'M'})
print(pessoa)



# Adicionando chave e valor com uma lista 
pessoa.update({'Curso':['Angular', 'React', 'Python']})
print(pessoa)


# Deixando o dicionario zerado
pessoa.clear()
print(pessoa)