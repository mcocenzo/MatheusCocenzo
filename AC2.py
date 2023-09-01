#Questão 1
def mensal(horas, salario):
    return salario * horas

def main():
    salario = int(input("Informe o salário recebido por hora: "))
    horas = int(input("Informe o número de horas trabalhadas no mês: "))
    print("O salário recebido este mês é de ", mensal(horas, salario), "reais")

main()

#Questão 2
def num1(a, b):
    return (2 * a) * (b / 2)

def num2(a, c):
    return (a * 3) + c

def num3(c):
    return c**3

def main():
    a = int(input("Informe o primeiro número: "))
    b = int(input("Informe o segundo número: "))
    c = int(input("Informe o terceiro número: "))
    print(num1(a, b))
    print(num2(a, c))
    print(num3(c))

main()

#Questão 4
bissexto = int(input("Informe um ano: "))
def ano(bissexto):
    return (bissexto % 4 == 0) and bissexto % 100 != 0 or bissexto % 400 == 0

if ano(bissexto) == True:
    print("O ano ", bissexto, "é bissexto.")
else:
    print("O ano ", bissexto, "não é bissexto.")
