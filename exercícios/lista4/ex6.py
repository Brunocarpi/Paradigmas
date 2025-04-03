def caminho_minimo(matriz):
    n = len(matriz)
    m = len(matriz[0])
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = matriz[0][0]
    
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]
    
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = matriz[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

def expressao_valida(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expressao:
        if char in "({[":
            pilha.append(char)
        elif char in ")}]":
            if not pilha or pilha.pop() != pares[char]:
                return False
    
    return not pilha

matriz = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

resultado = caminho_minimo(matriz)
print(f"Custo mínimo do caminho: {resultado}")

teste1 = "{[()]}()"
teste2 = "{[(])}"
print(f"Expressão {teste1} válida? {expressao_valida(teste1)}")
print(f"Expressão {teste2} válida? {expressao_valida(teste2)}")
