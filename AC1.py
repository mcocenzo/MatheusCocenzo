
a = float(input("Informe o valor de a: "))
b = float(input("Informe o valor de b "))
c = float(input("Informe o valor de c: "))

raiz1 = (-b + (b**2 - 4 * a * c)** 0.5) / 2 * a
raiz2 = (-b - (b**2 - 4 * a * c)** 0.5) / 2 * a

print(f"X1 = {raiz1} e X2 = {raiz2}")


ano = int(input("Informe um ano: "))
bissexto = (ano % 4 == 0) and ano % 100 != 0 or ano % 400 == 0
print(bissexto)

