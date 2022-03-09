#FAça um programa que leia uma grase pelo teclado e mostre: => quantas vezes aparece a letra "A"; => em que posiçao ela aparece a primeira vez; => em que posição ela aparece a úlltima vez
frase = str(input('Diga uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes na frase')
print(f'A primeira posição que a letra A aparece é na posiçãõ {frase.find("A") + 1}')
print(f'A primeira posição que a letra A aparece é na posiçãõ {frase.rfind("A")}')