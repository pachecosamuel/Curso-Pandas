import numpy as np
import pandas as pd

aleatory_nums = pd.DataFrame(np.random.rand(5, 5) * 100, columns=["A", "B", "C", "D", "E"])
print(aleatory_nums)
print(f"\n{aleatory_nums.columns}\n")

# 2° dataframe de notas de alunos a partir de um dict
students_grade = pd.DataFrame({
    "Name" : ["John", "Anne", "Sam"],
    "Grades" : [10, 9, 8]
})
print(f"Notas alunos:\n{students_grade}")