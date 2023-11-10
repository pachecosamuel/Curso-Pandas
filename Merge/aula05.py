# MERGE Outer join
# O merge do tipo outer join combina os elementos de duas tabelas, incluindo todas as linhas de ambas as tabelas, 
# e preenchendo os valores ausentes com NaN (Not a Number) onde não houver correspondência entre as chaves de junção.

import pandas as pd

# 1° Generate two dataframes
sales_l1 = pd.read_excel("Outer_Vendas_Loja1.xlsx")
sales_l2 = pd.read_excel("Outer_Vendas_Loja2.xlsx")

print(f"\n Sales Store 1:\n {sales_l1} \n")
print(f"\n Sales Store 2:\n {sales_l2} \n")

# 2° Make an outer join between them, apply suffixes
outer_ = pd.merge(sales_l1, sales_l2, on="Id Vendedor", how="outer", suffixes=(" Loja 1", " Loja 2"))
print(f"\n Outer Merge:\n {outer_} \n")

# 3° Drop null values
dropped = outer_.dropna()
print(f"\n DF treated using dropna:\n {dropped} \n")

# 4° Remover coluna vendedor loja 2
treated = dropped.drop(columns="Vendedor Loja 2")
print(f"\n DF treated using drop column vendedor loja 2:\n {treated} \n")