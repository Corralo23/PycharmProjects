#As principais operações que vamos aprender são fatiamento de String.
# Analise com len(), count(), find(), transformaões com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().
#FATIAMENTO = len(), count(), find()
#TRANSFORMAÇÃO = replace(), upper(), lower(), capitalize(), title(), strip()
#JUNÇÃO = join() ==> vai pegar um lista e gerar uma string ('-'.join(frase))
#DIVISÃO = split() ==> vai dividir uma string em uma lista

frase = 'curso em video Python'
print(frase[3])
print(frase[3:14])
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.split())

frase = frase.replace('python', 'programação')
print(frase)

texto = 'curso em video python'
dividido = texto.split()
print(dividido[2][4])