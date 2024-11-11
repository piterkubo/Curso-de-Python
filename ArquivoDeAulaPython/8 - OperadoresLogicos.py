# Operadores Logicos


'''

true = verdadeiro
false = falso

and = e

or  = ou

not = negação

'''


'''
Tabela verdade and

true and true = verdadeiro

true and false = falso

false and true = false

false and false = falso

'''


'''
Tabela verdade or

true and true = verdadeiro

true and false = verdadeiro

false and true = verdadeiro

false and false = falso

'''


'''
Tabela verdade xor

true != true = falso

true != false = verdadeiro

false != true = verdadeiro

false != false = falso

'''





'''
Tabela verdade not

not true = falso

not false = verdadeiro


'''


print(7 != 3 and 2 > 3)



'''
bit a bit


true & false

false | true

true ^ false


'''


# Ex de and bit

'''
3 = 11
2 = 10

'''
# O resultado sera (2) 1 & 1 = 1  e 1 & 0 = 0
print(3 & 2)


#Ex de ou bit

'''
3 = 11
2 = 10


'''
# O resultado sera (3) 1 ou 1 = 1 e 1 ou 0 = 1
print(3 | 2 )


#Ex de xor bit

'''

3 = 11
2 = 10

'''

# O resultado sera (01) 1 xor 1 = 0  e 1 xor 0 = 1
print(3 ^ 2)


# EX Um pouco de logina na realidade


saldo = 1000

salario = 4000

despesa = 2967

meta = saldo > 0 and salario - despesa >= 0.2 * salario;

print(meta)
