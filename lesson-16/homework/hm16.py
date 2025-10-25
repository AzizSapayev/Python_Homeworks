import numpy as np
royxat = [12.23, 13.32, 100, 36.32]
massiv=np.array(royxat)
print(royxat)
print(massiv)
matritsa=np.arange(2,11).reshape(3,3)
print(matritsa)
vektor=np.zeros(10)
vektor[5]=11
print(vektor)
massivv=np.arange(12,37).reshape(5,5)
print(massivv)
import numpy as np

# Asl massiv
arr = np.array([1, 2, 3, 4])
print("Asl massiv:", arr)

# Float turiga o‘tkazish
float_arr = arr.astype(float)
print("Float turiga o‘tkazilgan massiv:", float_arr)

import numpy as np

# Celsius qiymatlar (Santigrad)
celsius = np.array([0, 12, 45.21, 34, 99.91, 0.])

# Fahrenheitga o‘tish
fahrenheit = celsius * 9/5 + 32

print("Santigrad darajadagi qiymatlar:", np.round(celsius, 2))
print("Farengeyt darajasidagi qiymatlar:", np.round(fahrenheit, 2))

import numpy as np

# Asl massiv
arr = np.array([10, 20, 30])
print("Asl massiv:", arr)

# Qo'shiladigan qiymatlar
new_values = [40, 50, 60, 70, 80, 90]

# np.append() yordamida qo'shamiz
arr = np.append(arr, new_values)

print("Massiv oxiriga qiymatlar qo‘shgandan so‘ng:", arr)

import numpy as np

# 1. Tasodifiy massiv yaratamiz (10 ta element)
arr = np.random.randint(1, 100, size=10)  # 1 dan 100 gacha bo‘lgan sonlar
print("Massiv:", arr)

# 2. Statistik qiymatlarni hisoblaymiz
mean_value = np.mean(arr)
median_value = np.median(arr)
std_value = np.std(arr)

# 3. Natijalarni chiqaramiz
print("O‘rtacha qiymat (mean):", mean_value)
print("Mediana (median):", median_value)
print("Standart og‘ish (std):", std_value)

import numpy as np

# 10x10 o'lchamli tasodifiy massiv (0–100 oraliqda)
arr = np.random.randint(0, 100, size=(10, 10))
print("Massiv:\n", arr)

# Minimal va maksimal qiymatlarni topish
min_value = np.min(arr)
max_value = np.max(arr)

print("\nMinimal qiymat:", min_value)
print("Maksimal qiymat:", max_value)


import numpy as np

# 3x3x3 o'lchamli tasodifiy massiv
arr_3d = np.random.randint(0, 100, size=(3, 3, 3))
print("3x3x3 tasodifiy massiv:\n", arr_3d)

