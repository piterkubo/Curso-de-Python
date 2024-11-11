# Dicionarios {}


pessoa = {'Nome': 'Prof(a) Ana', 'Idade': 39, 'Curso': ['Ingles', 'Portugues']}

print(type(pessoa))



#Contando a quantidade de caracteres
print(len(pessoa))



#Imprimindo caracteres
print(pessoa['Nome'])
print(pessoa['Idade'])
print(pessoa['Curso'][1])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('Idade'))


# Procedimento para um retorno default caso a propriedade não exista
print(pessoa.get('tags', []))
