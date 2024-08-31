# --------- Exercicio 01 -------------
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

numero = int(input("Informe um número: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# --------- Exercicio 02 -------------
def contar_a(s):
    count = s.lower().count('a')
    return count

string = input("Informe uma string: ")
quantidade = contar_a(string)
print(f"A letra 'a' aparece {quantidade} vezes na string.")

# --------- Exercicio 03 -------------
INDICE = 12
SOMA = 0
n1 = 1

while n1 < INDICE:
    n1 = n1 + 1
    SOMA = SOMA + n1

print(SOMA)

