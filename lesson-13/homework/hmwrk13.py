working with database
Yosh kalkulyatori

from datetime import date
yil = int(input("Tug'ilgan yilingizni kiriting: "))
oy = int(input("Tug'ilgan oyingizni kiriting (1-12): "))
kun = int(input("Tug'ilgan kuningizni kiriting: "))
bugun=date.today()
tugilgan=date(yil,oy,kun)
farq=bugun-tugilgan
yillar=farq.days//365
oylar=(farq.days % 365)//30
kunlar=(farq.days %365)%30
print(f"Siz {yillar} yil {oylar} oy  {kunlar} kun yashagansiz")

yil = int(input("Tug'ilgan yilingizni kiriting: "))
oy = int(input("Tug'ilgan oyingizni kiriting (1-12): "))
kun = int(input("Tug'ilgan kuningizni kiriting: "))
bugun=date.today()
tugilgan=date(bugun.year,oy,kun)
if tugilgan<bugun:
    tugilgan=date(bugun.year+1,oy,kun)

farq=(tugilgan-bugun).days
print(f"Keyingi tug'ilgan kuningizgacha {farq} kun qoldi!")
from datetime import datetime, timedelta

# Joriy sana va vaqtni so'raymiz
hozir_str = input("Joriy sana va vaqtni kiriting (masalan: 2025-10-18 14:30): ")

# Uchrashuv davomiyligi
soat = int(input("Uchrashuv davomiyligi (soat): "))
daqiqa = int(input("Uchrashuv davomiyligi (daqiqa): "))

# Stringni datetime ga aylantirish
hozir = datetime.strptime(hozir_str, "%Y-%m-%d %H:%M")

# Yangi vaqtni hisoblash
tugash_vaqti = hozir + timedelta(hours=soat, minutes=daqiqa)

print("Uchrashuv tugash vaqti:", tugash_vaqti.strftime("%Y-%m-%d %H:%M"))

from datetime import datetime, timedelta

# Foydalanuvchidan vaqtni so'raymiz
sana_vaqt_str = input("Sana va vaqtni kiriting (2025-10-18 14:30 formatida): ")

# Joriy vaqt mintaqangizning UTC farqini so'raymiz (masalan: O'zbekiston uchun +5)
src_offset = int(input("Joriy mintaqangizning UTC farqi (masalan +5 yoki -3): "))

# Qaysi mintaqaga o'tkazishini so'raymiz
dst_offset = int(input("Qaysi UTC mintaqasiga o'tkazmoqchisiz? (masalan +1 yoki -8): "))

# Sana va vaqtni datetime formatiga o'tkazamiz
sana_vaqt = datetime.strptime(sana_vaqt_str, "%Y-%m-%d %H:%M")

# Farqni hisoblaymiz
farq = dst_offset - src_offset
yangi_vaqt = sana_vaqt + timedelta(hours=farq)

print(f"Natija: {yangi_vaqt.strftime('%Y-%m-%d %H:%M')}  (UTC{dst_offset:+})")

from datetime import datetime
import time

# Kelajakdagi sana va vaqtni kiritamiz
target_str = input("Kelajakdagi sana-vaqtni kiriting (masalan: 2025-12-31 23:59:00): ")
target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    farq = target_time - now

    if farq.total_seconds() <= 0:
        print("⏰ Vaqt tugadi!")
        break

    kun = farq.days
    soat = (farq.seconds // 3600)
    daqiqa = (farq.seconds % 3600) // 60
    soniya = farq.seconds % 60

    print(f"Qoldi: {kun} kun, {soat:02d}:{daqiqa:02d}:{soniya:02d}", end="\r")

    time.sleep(1)

email = input("Elektron pochta manzilingizni kiriting: ").strip()

if "@" in email and "." in email.split("@")[-1]:
    print("Ko'rinishiga qaraganda email to'g'ri.")
else:
    print("Noto'g'ri email ko'rinishi.")

raqam = input("Telefon raqamingizni kiriting (faqat raqamlarda, masalan 901234567 yoki 998901234567): ")

raqam = "".join(filter(str.isdigit, raqam))  # Harflarni olib tashlaydi

if len(raqam) == 9:  # 901234567
    kod = raqam[:2]
    qolgani = raqam[2:]
    print(f"+998 {kod} {qolgani[:3]}-{qolgani[3:5]}-{qolgani[5:]}")
elif len(raqam) == 12 and raqam.startswith("998"):
    kod = raqam[3:5]
    qolgani = raqam[5:]
    print(f"+998 {kod} {qolgani[:3]}-{qolgani[3:5]}-{qolgani[5:]}")
else:
    print("Noto'g'ri format! 9 yoki 12 xonali raqam kiriting.")

# Juda sodda parol kuchi tekshiruvchisi
password = input("Parolni kiriting: ")

min_len = 8

has_min_len = len(password) >= min_len
has_upper = any(c.isupper() for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)

if has_min_len and has_upper and has_lower and has_digit:
    print("Parol kuchli 🟢")
else:
    print("Parol yetarli emas ❌")
    if not has_min_len:
        print(f"- Parol kamida {min_len} belgidan iborat bo'lishi kerak.")
    if not has_upper:
        print("- Kamida bitta KATTA harf mavjud bo'lishi kerak.")
    if not has_lower:
        print("- Kamida bitta kichik harf mavjud bo'lishi kerak.")
    if not has_digit:
        print("- Kamida bitta raqam mavjud bo'lishi kerak.")

matn = "Salom salom SALOM! Bugun salom deyishdan charchamaymiz."
soz = input("Qidirilayotgan so'z: ")

start = 0
while True:
    idx = matn.lower().find(soz.lower(), start)
    if idx == -1:
        break
    print("Topildi index:", idx)
    start = idx + 1

text = input("Matn kiriting: ")

sana = ""
sana_list = []

for char in text:
    if char.isdigit() or char in "-./":
        sana += char
    else:
        if len(sana) >= 8:   # Juda qisqa bo‘lsa, bu sana emas
            sana_list.append(sana)
        sana = ""

# Oxirida ham tekshirib qo‘yamiz
if len(sana) >= 8:
    sana_list.append(sana)

print("Topilgan sanalar:", sana_list if sana_list else "Yo‘q")


