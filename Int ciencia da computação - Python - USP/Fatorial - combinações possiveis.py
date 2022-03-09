def main():
    # leitura dos valores de entrada
    m = int(input("Digite m: "))
    n = int(input("Digite n: "))

    # calcula o fatorial de m
    k = m
    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1  # o mesmo que cont = cont + 1
    k_fat *= cont  # o mesmo que k_fat = k_fat * cont

k_fat = 1
m_fatorial = k_fat

# calcula o fatorial de n
k = n 
k_fat = 1
cont = 1
while cont < k:
    cont += 1  # o mesmo que cont = cont + 1
k_fat *= cont  # o mesmo que k_fat = k_fat * cont
n_fatorial = k_fat

# calcula o fatorial de m - n
k = m - n
k_fat = 1
cont = 1
while cont < k:
    cont += 1  # o mesmo que cont = cont + 1
k_fat *= cont  # o mesmo que k_fat = k_fat * cont

mn_fatorial = k_fat

print("Comb(", m, ",", n, "): ", m_fatorial / (mn_fatorial * n_fatorial))

# ----------------------------------------------------------
main()