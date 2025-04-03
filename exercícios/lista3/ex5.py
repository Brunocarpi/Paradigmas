

def caminho_minimo(matriz, N):
    dp = [[0] * N for _ in range(N)]
    
    dp[0][0] = matriz[0][0]
    
    for j in range(1, N):
        dp[0][j] = dp[0][j - 1] + matriz[0][j]
    
    for i in range(1, N):
        dp[i][0] = dp[i - 1][0] + matriz[i][0]
    
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = matriz[i][j] + min(dp[i - 1][j], dp[i][j - 1])
    
    return dp[N-1][N-1]

N = int(input("Digite a ordem da matriz (N): "))
matriz = []
print("Digite a matriz linha por linha:")

for i in range(N):
    linha = list(map(int, input().split()))
    matriz.append(linha)
    
if len(matriz) != N or any(len(linha) != N for linha in matriz):
    print("Erro: A matriz inserida não possui as dimensões corretas.")

print("Matriz lida:", matriz)
resultado = caminho_minimo(matriz, N)
print(f"Custo mínimo do caminho: {resultado}")


