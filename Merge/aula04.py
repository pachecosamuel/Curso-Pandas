# Left Join
import pandas as pd
salesperson = pd.read_excel("Vendedores_LEFT_JOIN.xlsx")
sales = pd.read_excel("Vendas_LEFT_JOIN.xlsx")

print(f"\n Salesperson:\n {salesperson} \n")
print(f"\n Sales:\n {sales} \n")

# We gonna make the popular PROCV - Bring data from another table

# We gonna lookup for salesperson which made sales on the xlsx

# The left join will bring all content from the first table
# and brinb only the match data from the second table

# 1° Left
merged = pd.merge(sales, salesperson, on="Id Vendedor", how="left")
print(f"\n Left JOIN:\n {merged} \n")
print(f"\n Left JOIN:\n {merged} \n")

# 2° Rename columns
merged = pd.merge(sales, salesperson, on="Id Vendedor", how="left", suffixes=("", " Checagem"))
print(f"\n Renamed column:\n {merged} \n")

# 3° Drop duplicates, dropna - drop rows which have at least one void value
merged = merged.dropna()
print(f"\n Data treatment:\n {merged} \n")

# 4° Dropping one specif column
merged = merged.drop(columns="Vendedor Checagem")
print(f"\n Clean DF:\n {merged} \n")