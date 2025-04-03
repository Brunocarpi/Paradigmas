import pandas as pd

estoque = [
    {"nome": "Camiseta", "quantidade": 10, "minimo": 15},
    {"nome": "Calça de Moletom", "quantidade": 25, "minimo": 15},
    {"nome": "Calça Jeans", "quantidade": 8, "minimo": 10},
    {"nome": "Casaco de Lã", "quantidade": 30, "minimo": 15},
    {"nome": "Gorro", "quantidade": 10, "minimo": 10}
]

def produtos_abaixo_minimo(estoque):
    lista_abaixo_minimo = []
    df = pd.DataFrame({"nome": [], "quantidade": [], "minimo": []})
    for i in estoque:
        df.loc[len(df)] = [i["nome"], i["quantidade"], i["minimo"]]

    item_abaixo_minimo = df[["nome"]].loc[df["quantidade"] < df["minimo"]].reset_index()
    for i in range(len(item_abaixo_minimo)):
        lista_abaixo_minimo.append(item_abaixo_minimo.loc[i, "nome"])

    return lista_abaixo_minimo

lista_resultado = produtos_abaixo_minimo(estoque)
print(lista_resultado)