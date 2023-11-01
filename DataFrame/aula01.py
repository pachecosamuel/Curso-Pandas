import pandas as pd
import numpy as np

# data_range = To create a list
# periods = Period of time specified
# 20221201 = yyyy/mm/dd
df_pd_datas = pd.date_range(start="2024/01/01", end="2024/2/01", freq="D")
print(f"{df_pd_datas} \n\n")

df_pd_months = pd.date_range(start="2024/01/01", periods=len(df_pd_datas), freq='M')
print(f"{df_pd_months} \n\n")


# The parameters in rand receive respectively the amount of rows and columns
aleatory_numbers = pd.DataFrame(np.random.rand(5, 1))
print(f"{aleatory_numbers} \n\n")


# First you need to transform the list into a DataFrame
df1 = pd.DataFrame(df_pd_datas)
df2 = pd.DataFrame(df_pd_months)

concat_days_months = pd.concat([df1, df2])
print(concat_days_months)


# I'm gonna create a DF with two columns
super_df = pd.DataFrame({
    "Days": df_pd_datas,
    "Months": df_pd_months
})

print(f"\n\n{super_df}")
