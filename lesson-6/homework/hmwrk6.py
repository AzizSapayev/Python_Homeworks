def modify_string(txt):
    vowels = "aeiouAEIOUo'IO'"  # Unlilar
    result = ""
    count = 0  # Harflarni sanash

    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1

        # Har 3-ta belgidan keyin tekshiramiz
        if count == 3:
            # Oxiriga underscore qo‘ymaslik uchun
            if i + 1 < len(txt):
                # Agar keyingi belgi unli yoki '_' bo'lsa, keyingi belgidan keyin qo'yamiz
                if txt[i + 1] in vowels or txt[i + 1] == "_":
                    result += txt[i + 1]  # Keyingi belgini qo‘shamiz
                    result += "_"  # Underscore qo‘shamiz
                    i += 1  # Bitta qo‘shimcha siljitamiz
                else:
                    result += "_"
            count = 0  # Sanashni qayta boshlaymiz
        i += 1

    # Agar oxirida '_' tushib qolgan bo‘lsa, olib tashlaymiz
    if result.endswith("_"):
        result = result[:-1]

    return result


# SINAB KO'RAMIZ
print(modify_string("hello"))         # hel_lo
print(modify_string("assalom"))       # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abcab_cdeabcd_efabcdef_g

a = int(input("sonni kiriting: "))
for n in range(a):
    print(n**2)


a = int(input("sonni kiriting: "))
count=0
for i in range(1,a+1):
    count+=i
    i+1
print(count)

a = int(input("sonni kiriting: "))
count = len(str(a))
print(count)
a = int(input("sonni kiriting: "))
teskari=str(a)[::-1]
print(teskari)
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1, -1):
    print(list1[i])
for i in range(-10,-1+1):
    print(i)
    i+1
a1 = int(input("1chi sonni kiriting: "))
a2 = int(input("2chi sonni kiriting: "))
tublar=[]
for num in range(a1,a2):
        is_tublar=True
        if num < 2:
            continue
        for i in range(2,num):
            if num% i==0:
             is_tublar=False
             break
        if is_tublar:
            tublar.append(num)
print(tublar)


a1 = int(input("1chi sonni kiriting: "))
a2 = int(input("2chi sonni kiriting: "))
tublar = []
for num in range(a1, a2):
    is_tublar = True
    if num < 2:
        continue
    for i in range(2, num):
        if num % i == 0:
            is_tublar = False
            break
    if is_tublar:
        tublar.append(num)
print(tublar)
limit=int(input("chegarani kiriting"))
primes=[]
for num in range(2,limit+1):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        primes.append(num)
print(primes)
a, b = 0, 1   # Boshlang'ich ikkita son

print("Fibonacci sequence:")

for i in range(10):   # 10 marta takrorlaymiz
    print(a, end=" ")  # Har safar hozirgi sonni chiqaramiz
    a, b = b, a + b    # Yangi qiymatlarni hisoblaymiz

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Foydalanuvchi kiritadi
count = int(input("Nechta Fibonacci soni chiqaray? "))
fibonacci(count)

def faktorial(n):
    S=1
    A=0
    for i in range(1,n+1):
        S*=i
    return S
print(faktorial(5))

        
def uncommon(list1,list2):
    result=[]
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result
print(uncommon(list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]))
