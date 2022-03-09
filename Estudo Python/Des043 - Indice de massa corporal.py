#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tavela abaixo:
#IMC abaixo 18,5 = abaixo do peso; entre 18,5 e 25 =  peso ideal; 25 até 30 = sobrepeso; 30 a 40 = obesidade; acima de 40 = obesidade morbida
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura * 2)
print(f'Seu IMC é {imc :.2f}')
if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso Ideal')
elif imc < 30:
    print('sobrepeso')
elif imc < 40:
    print('obesidade')
else:
    print('obedidade morbida')