N = int(input('\nDigite a quantidade de termos da sequência de Fibonacci: '))
a = 0
b = 1

print("\nSequência de Fibonacci:")
for i in range(N):
    print(a, end=' ')
    proximo = a + b
    a = b
    b = proximo
