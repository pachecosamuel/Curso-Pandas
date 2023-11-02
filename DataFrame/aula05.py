import pandas as pd

df_vendas = pd.read_excel("Vendas_Jan.xlsx", dtype=str, engine='openpyxl')

# 1° - Show some specific columns
print(f"\n Showing some specific columns:\n")
print(f"{df_vendas[['Vendedor', 'Total Vendas']]}\n")

# 2° - Showings rows from one to five
print(f"\n Showings rows from one to five:\n")
print(f"{df_vendas.loc[1:5]}\n")

# 3° - Showing only Leonardo sales
print(f"\n Showing only Leonardo sales:\n")
df_leo_sales = df_vendas.loc[df_vendas["Vendedor"] == "Leonardo Almeida"]
print(f"{df_leo_sales}\n")

# 4° - Print sales and resume the informations
print(f"\n Print sales and resume the informations:\n")
print(f"{df_leo_sales[['Vendedor', 'Total Vendas']]}")

# 5° - Print a unique index and columns
print(f"\n Print a unique index and columns:")
print(f"{df_vendas.loc[27, 'Vendedor']}\n")

# 6° - Using the shape method = Amout of rows and columns
print(f"\n Using the shape method:")
print(f"{df_vendas.shape}\n")

# 7° - Using transpose method = Transform rows in columns and columns in rows
print(f"\n Using the transpose method:")
print(f"{df_vendas.T}\n")

