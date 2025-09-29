1. Sort a Dictionary by Value
Write a Python script to sort (ascending and descending) a dictionary by value.
year=int(input("Yilni kiriting"))
if (year%4==0 and year%100 !=0) or( year%400==0 ):
    print("Bu yil kabisa yili")
else:
    print("Bu yil kabisa yili emas")

year = int(input("Yilni kiriting"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Bu yil kabisa yili")
else:
    print("Bu yil kabisa yili emas")
n = int(input("Son kiriting: "))

if n % 2 != 0:  # Toq son
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:  # 2-5 oraliqdagi juft son
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:  # 6-20 oraliqdagi juft son
    print("Weird")
elif n % 2 == 0 and n > 20:  # 20 dan katta juft son
    print("Not Weird")

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

# a va b o'rnini kerak bo'lsa almashtiramiz
if a > b:
    a, b = b, a

# Boshlang'ich juft sonni topamiz
if a % 2 != 0:
    a += 1  # Agar toq bo'lsa, keyingi juftga o'tamiz

# range + step bilan chiqaramiz (loop emas, chunki list comprehensions yoki print ichida range foydalanish loop hisoblanmaydi)
print(list(range(a, b + 1, 2)))

a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

start = a + (a % 2)  # Agar juft bo'lsa o'zi, agar toq bo'lsa +1 qilib keyingi juftni oladi

print(list(range(start, b + 1, 2)))

