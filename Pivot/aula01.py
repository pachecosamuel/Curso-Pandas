import pandas as pd
# Pivot - This method doesn't agree duplicated values as source

# 1° Print the dataframe
sales = pd.read_excel("Vendas_Lanchonete_Pivot.xlsx")
print(f"\n DF:\n {sales} \n")


# 2° method .pivot(index="Data Venda", columns="Cliente", values="Preço com desconto")
    # print customers / Discount price
pivot_date = sales.pivot(index="Data Venda", columns="Cliente", values="Preço com Desconto")
print(f"\n DF:\n {pivot_date} \n")

# 3° (index="Cliente", columns="Data Venda", values="Preço com desconto")
pivot_customer = sales.pivot (index="Cliente", columns="Data Venda", values="Preço Total")
print(f"\n DF:\n {pivot_customer} \n")

# 4° 