import pandas as pd

# 1° Open a Sales DF
sales_df = pd.read_excel("Vendas_merge.xlsx")
print(f"\n Sales DF:\n {sales_df} \n")

# 2° Open a Salesperson DF
salesperson_df = pd.read_excel("Vendedores_Merge.xlsx")
print(f"\n Salesperson DF:\n {salesperson_df} \n")

# 3° Open a Product DF
products_df = pd.read_excel("Produtos_Merge.xlsx")
print(f"\n Product DF:\n {products_df} \n")

# 4° Merge among Sales and Salesperson bringing two data column from Salesperson DF 
merge_sales_and_salesperson = sales_df.merge(salesperson_df)
print(f"\n Merge sales and salesperson DF:\n {merge_sales_and_salesperson} \n")

# 5° Merge among Sales and Product, bringing the product name
marge_sales_and_products = sales_df.merge(products_df) 
print(f"\n Merge sales and products DF:\n {marge_sales_and_products} \n")

# 6° Print all columns
print(f"\nColumns = {marge_sales_and_products.columns}")

# 7° Summarize DF Merge
resumoDF = marge_sales_and_products[["Produto", "Valor Unitário", "Quantidade Vendida"]]
print(f"\n Resumo: \n {resumoDF.sort_values(by='Quantidade Vendida', ascending=False)}\n\n")