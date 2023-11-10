# Merge -> Inner join = When an entity is present on both or more dataframes
# this method will only catch these present values on all dataframes
import pandas as pd

loja1 = pd.read_excel("VendasLoja1.xlsx")
loja2 = pd.read_excel("VendasLoja2.xlsx")

# 1° Salespersons which sold on both stores, on = column, how = type of merge, suffixes = rename columns
# _x = store 1
# _y = store 2
sales_on_both_stores = pd.merge(loja1, loja2, on="Vendedor", how="inner")
print(f"\n Sales on both stores: \n{sales_on_both_stores}\n")

# 2 ° print the columns of the merged DF
print(f"\n {sales_on_both_stores.columns} \n")

# 3° We gonna see the inner join result
salesperson_summarize = pd.merge(loja1, loja2[["Vendedor", "Total Vendas"]], on="Vendedor", how="inner", suffixes=(" Loja 1", " Loja 2"))
print(f"\n Summarize: \n{salesperson_summarize}\n")

# 4° Make a summarize of the sales made on the first and second store
summarize = salesperson_summarize[["Vendedor", "Total Vendas Loja 1", "Total Vendas Loja 2"]]
print(f"\n Summarize: \n{summarize}\n")