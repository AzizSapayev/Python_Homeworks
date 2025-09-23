# 1. Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))
from datetime import date
age = date.today().year - birth_year
print(f"Hello {name}, you are {age} years old.")

# 2. Extract Car Names
txt = 'LMaasleitbtui'
cars = ["Lamborghini", "Maserati", "Bentley", "Audi", "BMW", "Toyota"]
for car in cars:
    if all(c.lower() in txt.lower() for c in car.lower() if c.isalpha()):
        print(car)

# 3. Extract Car Names
txt = 'MsaatmiazD'
cars = ["Mazda", "Daimler", "Mitsubishi"]
for car in cars:
    if all(c.lower() in txt.lower() for c in car.lower() if c.isalpha()):
        print(car)

# 4. Extract Residence Area
txt = "I'am John. I am from London"
area = txt.split("from")[-1].strip()
print("Residence area:", area)

# 5. Reverse String
s = input("Enter a string: ")
print("Reversed string:", s[::-1])

# 6. Count Vowels
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for c in s if c in vowels)
print("Number of vowels:", count)

# 7. Find Maximum Value
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Maximum value:", max(nums))

# 8. Check Palindrome
word = input("Enter a word: ")
if word.lower() == word[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")

# 9. Extract Email Domain
email = input("Enter your email: ")
domain = email.split("@")[-1]
print("Domain:", domain)

# 10. Generate Random Password
import random, string
length = 12
chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(chars) for _ in range(length))
print("Generated password:", password)
