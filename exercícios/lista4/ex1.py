'''
1) Considere que você é o gerente de uma empresa que trabalha em diversas áreas do mercado de forma simultânea. Você recebeu a tarefa de criar um conjunto de dados (dataframe) para analisar o desempenho de três filiais dessa empresa em diferentes áreas de negócio. Cada coluna representa uma filial e cada linha representa o desempenho da empresa (avaliado a partir de uma nota de 0 até 10) em uma de 5 diferentes áreas de negócio. Para realizar essa tarefa, siga as instruções abaixo:
a) Apresente o código em Python utilizado para criar um data frame composto pelos dados da tabela abaixo:
Área de Negócio     Filial A    Filial B    Filial C
    Segurança         7,8         6,2         9,8
    Financeiro        6,7         4,1         7,3
    Transporte        2,8         9,2         3,4
    Tecnologia        5,6         4,5         7,2
    Marketing         8,3         7,5         9,1
b) Escreva o código em Python para:
    • Inserir uma nova coluna ao data frame, chamada “Media Desempenho”, com a média de desempenho de cada filial em todas as áreas de negócio. Utilize a função mean();
    • Inserir uma nova coluna ao data frame, chamada “Melhor Desempenho”, com a área de negócio em que cada filial teve o melhor desempenho. Utilize a função idxmax();
    • Imprimir o total de desempenho para cada área considerando todas as filiais. Utilize a função sum().
c) Escreva o código em Python para:
    • Exportar o data frame resultante para um arquivo CSV com um nome de sua escolha;
    • Efetuar a leitura do arquivo CSV gerado e o atribuir a um novo data frame.
'''

import pandas as pd
import matplotlib as plt

# a)
print('Exercício A')
dados = {'Área de Negócio':['Segurança', 'Financeiro', 'Transporte', 'Tecnologia', 'Marketing'],
        'Filial A':[7.8, 6.7, 2.8, 5.6, 8.3],
        'Filial B':[6.2, 4.1, 9.2, 4.5, 7.5],
        'Filial C':[9.8, 7.3, 3.4, 7.2, 9.1]}

dataframe = pd.DataFrame(dados)
print(dataframe)

print('*'*50)

print('Exercício B')
# b)1)
'''
dataframe.iloc[:, 1:]: Seleciona todas as linhas (:) e todas as colunas a partir da segunda (1:), ou seja, pega só as colunas das filiais (ignorando "Área de Negócio").

.iloc[] → É usado para acessar elementos de um DataFrame com índices numéricos (como se fosse uma matriz)

.mean(axis=1): Calcula a média linha por linha (axis=1 significa "por linha" em vez de "por coluna").
'''
dataframe["Media Desempenho"] = dataframe.iloc[:, 1:].mean(axis=1)
print(dataframe)

print('*'*50)

# b)2)

dataframe["Melhor Desempenho"] = dataframe.iloc[:, 1:].idxmax(axis=1)
print(dataframe)

print('*'*50)

# b)3)

# Certificando-se de que está pegando apenas colunas numéricas (Filial A, B e C)
dataframe["Total Desempenho"] = dataframe.iloc[:, 1:4].sum(axis=1)
print(dataframe)

print('*'*50)

# c)

print('Exercício C')
# Exportar o DataFrame para um arquivo CSV
dataframe.to_csv('desempenho_filiais.csv', index=False)

# Fazendo a leitura do arquivo
novo_dataframe = pd.read_csv('Lista_4/desempenho_filiais.csv')

print(novo_dataframe)

