# Merge on dataframes
import pandas as pd

sales_jan = pd.read_excel("Vendas_Jan.xlsx")
sales_feb = pd.read_excel("Vendas_Fev.xlsx")
sales_mar = pd.read_excel("Vendas_Mar.xlsx")

# 1° Merge january_sales with february_sales
merged_jan_feb = pd.concat([sales_jan, sales_feb])
# print(f"\n January & February:\n {merged_jan_feb} \n")

# 2° Merge january_sales with february_sales and march_sales using concat
full_merge = pd.concat([sales_jan, sales_feb, sales_mar])
print(f"\n Full merge:\n {full_merge} \n")

# 3° Printing three columns of the merged Dataframe
print(f"\n Full merge with specific columns:\n {full_merge[['Vendedor', 'Total Vendas']]} \n")

# 4° Creating a unique DF grouped by months
full_merge_grouped = pd.concat([sales_jan, sales_feb, sales_mar], keys=["January", "February", "March"])
print(f"\n Grouped by months:\n {full_merge_grouped} \n")

# 5° Separate from this unique DF the february month
print(f"\n Extracting february:\n {full_merge_grouped.loc['February']} \n")

