def media_ponderada(notas_pesos):
    soma_ponderada = sum(nota * peso for nota, peso in notas_pesos)
    soma_pesos = sum(peso for _, peso in notas_pesos)
    return soma_ponderada / soma_pesos if soma_pesos != 0 else 0


notas = [(7.5, 2), (8.0, 3), (6.5, 5)]
resultado = media_ponderada(notas)
print(f"Média Ponderada: {resultado:.2f}")
