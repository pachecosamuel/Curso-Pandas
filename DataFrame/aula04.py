import pandas as pd

# 1° - Ler e exibir um excel
df_vendas = pd.read_excel("Vendas_Jan.xlsx", dtype=str, engine='openpyxl')
print(df_vendas)

# 2° - Exibir qts linhas e colunas
print(f"\n--- Amount of rows and columns ---\n")
print(f"Linhas -> {df_vendas.index}")

# 3° - Exibir o nome de cada coluna
print(f"Colunas -> {df_vendas.columns}\n")

# 4° - Exibir as 5 primeiras linhas
print(f"First five rows :\n {df_vendas.head()}\n")

# 5° - Exibir as 10 primeiras linhas
print(f"First ten rows :\n {df_vendas.head(10)}\n")

# 6° - Exibir as 3 últimas 
print(f"Last rows :\n {df_vendas.tail(3)}\n")

# 7 - Exibir somente a coluna vendedor
print(f"Sales columns :\n {df_vendas['Vendedor']}\n")

