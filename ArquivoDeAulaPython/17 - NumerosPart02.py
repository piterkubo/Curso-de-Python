# Numeros part 2


# Decimal


print(1.1 + 2.2)

# para evitar esse tipo de resultado 

from decimal import Decimal, getcontext

#valor com varias casas depois da virgula
print(Decimal(1) / Decimal(7))

#Colocando os valores para deixar com precisao de casas
getcontext().prec = 4;


#valor com 4 casas depois da virgula 
print(Decimal(1) / Decimal(7))

#Mostra o maior valor
print(Decimal.max(Decimal(1), Decimal(7)))

print(dir(Decimal))

print(dir())