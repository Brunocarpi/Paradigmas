def fibonacci(n):
    if n <= 0:
        return "Entrada inválida. O número do mês deve ser maior ou igual a 1."
    
    fib = [0] * (n + 1)
    fib[1] = 1
    if n > 1:
        fib[2] = 1
    
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

n = int(input("Digite o número do mês: "))
resultado = fibonacci(n)
print(f"O valor investido no mês {n} será: {resultado}")
