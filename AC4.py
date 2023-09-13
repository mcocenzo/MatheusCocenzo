# Exercicio 1
def primo(num):
    divisores = 0
    if num >= 1:
        for div in range(2, num):
            if num % div == 0:
                divisores += 1
                print("O número é divisivel por: ", div)

    if divisores == 0:
        print("O número é primo")
    else:
        print("O número não é primo")

# primo(10)
# print("-" * 20)
# primo(7)

# Exercicio 2
def taxa_juros(num_parc):
    if num_parc == 1:
        juros = 0 
    elif num_parc == 3:
        juros = 0.1  
    elif num_parc == 6:
        juros = 0.15 
    elif num_parc == 9:
        juros = 0.2 
    elif num_parc == 12:
        juros = 0.25 
    return juros

def dados(divida, num_parc):
    valor_juros = divida * taxa_juros(num_parc)
    total = divida + valor_juros
    valor_parcelas = total / num_parc
    print(valor_juros, total, num_parc, valor_parcelas)

def opcoes_divida(divida):
    print("Valor dos Juros", "Valor Total", "Quantidade de parcelas", "Valor da Parcela")
    print("0 R$", divida, "1 R$", divida)
    for n in range(3, 13, 3):
        dados(divida, n)

# opcoes_divida(1000)

# Exercicio 3
def nums():
    a = 0
    b = 0
    c = 0
    d = 0
    while True:
        num = int(input("Insira números entre 0 e 100: "))
        if num < 0:
            break
        if 0 <= num <= 25:
            a += 1
        elif 25 < num <= 50:
            b += 1
        elif 50 < num <= 75:
            c += 1
        elif 75 < num <= 100:
            d += 1
        else:
            print("Número inválido, tente novamente: ")

    print("Há ", a, "números no primeiro intervalo, ",
               b, "no segundo, ", c, "no terceiro e ", d, "no quarto.")

# nums()
