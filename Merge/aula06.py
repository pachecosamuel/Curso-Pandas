# Group by
import pandas as pd

#Group by = Agroup by a specified column
#dropna = delete rows which have at least one null/NaN value
#by = It uses a specified column as discretion(critério) to make the group by

dtype_dict = {
    "Vendedor": str,
    "Produto": str,
    "Data Venda": str,
    "Preço": float,
    "Qtd": float,
    "Total Vendas": float
}
salesDF = pd.read_excel("Groupby.xlsx", dtype=dtype_dict)
salesDF2 = pd.read_excel("Groupby.xlsx", dtype=dtype_dict)

print(f"\n Sales DF:\n {salesDF}\n")

salesDF = salesDF.drop(columns=["Data Venda", "Produto"])

# 1° Generate a new DF grouped by Vendedor and extract the mean in the available columns
average_salesp = salesDF.groupby(["Vendedor"]).mean()

print(f"\n Average DF:\n {average_salesp}\n")

# 2° Make the groupby using the sum
sum_salesp = salesDF.groupby(["Vendedor"]).sum()
print(f"\n Sum DF:\n {sum_salesp}\n")

# 3° Make the groupby using the sum and maintain the NaN rows
sum_nan_sales = salesDF.groupby(by=["Vendedor"], dropna=False).sum()
print(f"\n Sum DF with dropna=False:\n {sum_nan_sales}\n")

# 4° Make the groupby using the sum and REMOVING the NaN rows
sum_sales = salesDF.groupby(by=["Vendedor"], dropna=True).sum()
print(f"\n Sum NaN DF:\n {sum_sales}\n")

# 5° Make groupby using the columns vendedor and product . sum()
salesDF2 = salesDF2.drop(columns="Data Venda").groupby(["Produto", "Vendedor"]).sum()
# salesDF2 = salesDF2.groupby(["Data Venda", "Produto"]).sum()
print(f"\n {salesDF2} \n")