# Pivot Table is able to deal with duplicated values
# Index = what will become the rows
# Columns = columns
# Values = the cells of the new DF
# aggfunc = The function which will agregate the values

import pandas as pd

# 1° Generate a DF
baseCafeteria = pd.read_excel("Vendas_Lanchonete_Pivot_Table.xlsx")

print(f"\n Base DF:\n {baseCafeteria} \n")

# 2° - Index data, column customer, values preço desconto, aggfunc="sum"
example_1 = baseCafeteria.pivot_table(
    index="Data Venda", 
    columns="Cliente", 
    values="Preço com Desconto",
    aggfunc="sum"
)

print(f"\n Example 1:\n {example_1.fillna(0)} \n")

# 3° - Index customer, column data
example_2 = baseCafeteria.pivot_table(
    index="Cliente", 
    columns="Data Venda", 
    values="Preço com Desconto",
    aggfunc="sum"
)

print(f"\n Example 2:\n {example_2.fillna(0)} \n")

# 4° - Index data, columns customer, value [ preço total e c/ desconto ]
example_3 = baseCafeteria.pivot_table(
    index="Data Venda", 
    columns="Cliente", 
    values=["Preço com Desconto", "Preço Total"],
    aggfunc="sum"
)
print(f"\n Example 3:\n {example_3.fillna(0)} \n")


# 5° - Index data, columns [customer, produto], value preço total 
example_4 = baseCafeteria.pivot_table(
    index="Data Venda", 
    columns=["Cliente", "Produto"], 
    values="Preço Total",
    aggfunc="sum"
)
print(f"\n Example 4:\n {example_4.fillna(0)} \n")


