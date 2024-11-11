#Desafio

# trabalhoss

trabalho_terca = False
trabalho_quinta = False


Tv50 =  trabalho_terca and trabalho_quinta
Sorvete = trabalho_terca or trabalho_quinta
Tv32 = trabalho_terca or trabalho_quinta
semTrabalho = trabalho_terca == trabalho_quinta

'''
- confirmando os 2: Tv 50 + sorvete
- confirmando apenas 1: tv32 + sorverte
- nenhum confirmado: Fica em casa

'''

print(f'Tv50 {Tv50}  tv32 {Tv32} sorvete {Sorvete} semTrabalho {semTrabalho} ')
