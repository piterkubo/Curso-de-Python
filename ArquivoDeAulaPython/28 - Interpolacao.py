# Interpolação

'''
Interpolação é para uma string (substituir valores dentro de uma string)




'''

from string import Template


Nome, Idade = 'Ana', 30.97885655


# 1 forma de interpolar %s (string) %d(int)
print('Nome: %s Idade: %d' % (Nome,Idade))



# Interpolar com float %s (string) %f(int)
print('Nome: %s Idade: %.2f' % (Nome,Idade))


# Interpolar valores booleano
print('Nome: %s Idade: %d %r %r' % (Nome,Idade,True,False))


# Interpolar valores convertendo o booleano para binario
print('Nome: %s Idade: %d %d %d' % (Nome,Idade,True,False))



# 2 forma de interpolação
print('Nome: {0} Idade:{1}'.format(Nome,Idade))



# 3 Forma de interpolação
print(f'Nome: {Nome}, Idade: {Idade}')



# 4 Forma de interpolação
s = Template('Nome: $Nome Idade: $Idade')
print(s.substitute(Nome = Nome, Idade = Idade))