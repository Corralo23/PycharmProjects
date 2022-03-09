num = int(input('Digite um número inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
m1 = num // 10000 % 10
m2 = num // 100000 % 10
m3 = num // 1000000 % 10
m4 = num // 10000000 % 10
m5 = num // 100000000 % 10
print(u + d + c + m + m1 + m2 + m3 + m4 + m5)
