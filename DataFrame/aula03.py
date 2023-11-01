import pandas as pd
import numpy as np


# 1° - df de 3 alunos e 4 notas
students_grades = pd.DataFrame({
    "Name" : ["Anne", "John", "Max"],
    "Grade 1" : [10, 9, 8],
    "Grade 2" : [9.5, 8.5, 7.5],
    "Grade 3" : [5.5, 6.7, 7.5],
    "Grade 4" : [2.5, 7.5, 9.5],
})
print(f"----- Students grades ------\n")
print(students_grades)

# 2° - nova coluna media e calcula
students_grades["Average"] = (students_grades["Grade 1"] + students_grades["Grade 2"] + students_grades["Grade 3"] + students_grades["Grade 4"]) / 4
print(f"\n----- Grades average ------\n")
print(students_grades)

# 3° - nova coluna faltas com valor default
students_grades["Absent"] = 5
print(f"\n----- Students' absent ------\n")
print(students_grades)

# 4° - criar list com values and insert os the last column added
att_absents = [1, 0, 2]
students_grades["Absent"] = att_absents
print(f"\n----- Students' absent ------\n")
print(students_grades)

# 5° - Alterar uma nota em específico
students_grades.loc[2, "Grade 4"] = 10
print(f"\n----- New value to grade 4 row 2 ------\n")
print(students_grades)

# 6° - Recalcular a média
students_grades["Average"] = (students_grades["Grade 1"] + students_grades["Grade 2"] + students_grades["Grade 3"] + students_grades["Grade 4"]) / 4
print(f"\n----- New grades average ------\n")
print(students_grades)