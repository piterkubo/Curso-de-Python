# Operadores Ternarios

estar_chovendo = True

# No ternario se true pega a 2 opção(molhada) 
print('Hoje eu estou com as roupas ' + ('secas.', 'molhadas.')[estar_chovendo])




print('Hoje eu estou com as roupas ' + ('Molhadas.' if estar_chovendo else 'secas'))