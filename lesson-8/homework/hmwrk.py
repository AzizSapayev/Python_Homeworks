try:
    a=int(input("1chi sonni kiriting "))
    b=int(input("2chi sonni kiriting "))
    print(a/b)
except ZeroDivisionError:
    print("2chi son nol bolmasligi kerak Nolga bolib bolmaydi")
try:
    a=int(input("1chi sonni kiriting "))
    b=int(input("2chi sonni kiriting "))
    print(a/b)
except ValueError:
    print("Butun son kiriting")
try:
    with open("examplee.txt","r") as fayl:
     print(fayl.read)
except FileNotFoundError:
   print("Fayl topilamdi")

try:
    a = input("Birinchi sonni kiriting: ")
    b = input("Ikkinchi sonni kiriting: ")

    # Son emasligini tekshiramiz
    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        raise TypeError("Faqat son kiriting!")

    # Raqamga aylantiramiz
    a = float(a)
    b = float(b)

    print("Yig'indisi:", a + b)

except TypeError as e:
    print("Xato:", e)

try:
    file=open("example.txt","w")
except PermissionError:
    print("bu faylni oqishga ruhsat yoq")
my_list = [1, 2, 3, 4, 5]

try:
    index = int(input("Indeks kiriting: "))
    print("Qiymat:", my_list[index])
except IndexError:
    print("IndexError: Indeks diapazondan tashqarida!")
try:
    while True:
        print("Toxtatish uchun Ctr+C")
except KeyboardInterrupt:
    print("dastur toxtadi")
try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting (bo'luvchi): "))
    
    natija = a / b  # Bo'linish
    print("Natija:", natija)

except ArithmeticError:
    print("Arifmetik xato yuz berdi! (Ehtimol nolga bo'ldingiz)")

matn = "Salom 😊"

try:
    # ASCII ga o‘tkazishga harakat qilamiz (emoji ASCII da ishlamaydi)
    natija = matn.encode('ascii')
    print(natija)
except UnicodeError:
    print("⚠️ UnicodeError: Matnni ASCII ga aylantirib bo‘lmadi. UTF-8 dan foydalanamiz.")
    print(matn.encode('utf-8'))  # Zaxira variant

my_list = [1, 2, 3, 4, 5]

try:
    # Ataylab xato metod chaqiramiz (listda upper() metodi yo‘q)
    my_list.upper()
except AttributeError:
    print("⚠️ AttributeError: Bu ro'yxatda bunday atribut/metod mavjud emas!")
    print("O'rniga to'g'ri metodlardan foydalaning. Masalan: append(), remove(), sort() va h.k.")

try:
    with open("matn.txt", "r", encoding="utf-8") as file:
        content = file.read()  # Butun faylni o'qish
        print(content)
except FileNotFoundError:
    print("⚠️ Fayl topilmadi! Iltimos, 'matn.txt' nomli fayl mavjudligini tekshiring.")

try:
    with open("matn.txt", "r", encoding="utf-8") as file:
        first_line = file.readline()
        print(first_line)
except FileNotFoundError:
    print("⚠️ Fayl topilmadi!")

ism = input("Ismingizni kiriting: ")

with open("users.txt", "a", encoding="utf-8") as file:
    file.write(ism + "\n")

print("Ism faylga saqlandi ✅")

n = 3  # Nechta oxirgi qatorni o'qimoqchisiz

try:
    with open("users.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        print("Oxirgi satrlar:")
        for line in lines[-n:]:
            print(line, end="")
except FileNotFoundError:
    print("⚠️ Fayl topilmadi!")


