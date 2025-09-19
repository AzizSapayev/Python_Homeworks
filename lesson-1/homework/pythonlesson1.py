import math

# 1. Kvadratning perimetri va maydoni
a = float(input("Kvadratning tomoni a = "))
perimetr = 4 * a
maydon = a * a
print(f"Kvadrat perimetri = {perimetr}")
print(f"Kvadrat maydoni = {maydon}")

# 2. Doira diametri berilgan bo‘lsa, uzunligi (L = π * d)
d = float(input("Doira diametri d = "))
uzunlik = math.pi * d
print(f"Doira uzunligi = {uzunlik}")

# 3. Ikkita a va b raqami berilgan. O‘rtasini topish
a = float(input("a = "))
b = float(input("b = "))
ortacha = (a + b) / 2
print(f"a va b ning o‘rtachasi = {ortacha}")

# 4. Ikkita a va b raqami berilgan.
yigindi = a + b
kopaytma = a * b
a_kvadrat = a ** 2
b_kvadrat = b ** 2

print(f"a + b = {yigindi}")
print(f"a * b = {kopaytma}")
print(f"a^2 = {a_kvadrat}")
print(f"b^2 = {b_kvadrat}")
