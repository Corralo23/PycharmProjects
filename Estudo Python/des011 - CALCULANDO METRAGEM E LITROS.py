#FAÇA UM POGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA,
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M²
l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
area = l * a
tinta = area / 2
print(f'A largura da parede é {l} metros e sua altura é de {a} metros, o que representa {area} metros de area.\n Será necessário {tinta} litros de tinta para pintá-la')
print(f'Area total de {l * a} metros. Será necessário {(l * a) / 2} litros de tinta')