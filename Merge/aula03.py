# Merge full!
import pandas as pd

sp1 = pd.read_excel("Vendedores_Join_Full_Loja1.xlsx")
sp2 = pd.read_excel("Vendedores_Join_Full_Loja2.xlsx")

print(f"\n Salesperson store 1:\n {sp1} \n")
print(f"\n Salesperson store 2:\n {sp2} \n")

# 1° Concat = unir arquivos, que é um tipo de Join Full
both_stores = pd.concat([sp1, sp2])
print(f"\n Concat both stores:\n {both_stores} \n")

# 2° Drop duplicates
both_stores_without_duplicates = both_stores.drop_duplicates(subset=["Id Vendedor"])
print(f"\n Both stores without duplicate:\n {both_stores_without_duplicates} \n")

# 3° Data Treatment
treat_sales = both_stores_without_duplicates.fillna(both_stores_without_duplicates["Vendas"].mean())

trying = treat_sales["Meta"]
print(f"\n Trying:\n {trying} \n")

treat_sales["Meta"] = trying


print(f"\n Treated data:\n {treat_sales} \n")

