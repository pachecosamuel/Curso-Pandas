# Data ordenation
import pandas as pd
df = pd.read_excel("Ordenação.xlsx")

# 1° Print an ordinary df
print(f"\nJust the DF: \n {df} \n")

# 2° Order the df by salesperson's name A-Z
print(f"\nOrder asceding by Salesperson's name: \n {df.sort_values(by='Vendedor')} \n")

# 3° Order the df by products's name A-Z
print(f"\nOrder asceding by Products' name: \n {df.sort_values(by='Produto')} \n")

# 4° Order the df by Data-Vendas's value
print(f"\nOrder asceding by DataVendas' value: \n {df.sort_values(by='Data Venda')} \n")

# 5° Order the df by TotalSales' value 0-100k
print(f"\nOrder asceding by TotalSale' value: \n {df.sort_values(by='Total Vendas')} \n")

# 6° Order the df by salesperson's name A-Z and products' name A-Z
print(f"\nOrder asceding by Salesperson's and Product's values: \n {df.sort_values(by=['Vendedor', 'Produto'])} \n")

# 7° Order the df by salesperson's name Z-A
print(f"\nOrder asceding by Salesperson's name: \n {df.sort_values(by='Vendedor', ascending=False)} \n")

# 8° Order the df by TotalSales' value 100k-0
print(f"\nOrder asceding by TotalSale' value: \n {df.sort_values(by='Total Vendas', ascending=False)} \n")