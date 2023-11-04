import pandas as pd

df_del = pd.read_excel("Deletar_Linhas_Colunas.xlsx", dtype=str)
print(f"\n{df_del}\n")

# 1° Import and delete blank rows
df_del_null = df_del.dropna()
print(f"\n--- Deleting blank values through dropna ---\n")
print(f"{df_del_null}")

# 2° Delete the Data-Venda column
df_del_null = df_del_null.drop(columns="Data Venda")
df_del_null = df_del_null.drop(axis=0, index=7)
print(f"\n--- Droping column 'Data Venda' throughout drop ---\n")
print(f"{df_del_null}")

# 3° Using drop to delete more than one column
# when you're using axis 0 = linha, 1 = coluna
df_del_null = df_del_null.drop(axis=0, index=[0, 1])
print(f"\n--- Droping two lines throughout drop using axis and index ---\n")
print(f"{df_del_null}")

# 4° Delete six row
print(f"\n--- Droping the six line throughout drop using axis and index ---\n")
df_del_null = df_del_null.drop(axis=0, index=6)
print(f"{df_del_null}")