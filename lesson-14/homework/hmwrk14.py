import json

#1
File_name="books.json"

def load_books():

    try:
        with open(File_name,"r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    
def save_books():
    with open(File_name,"w") as file:
        json.dump(books,file,indent=4)

#yangi qosh
def add_book():
    books=load_books()
    new_id=len(books)+1
    title=input("Kitob nomi: ")
    author=input("Muallif: ")
    year=int(input("Nashr yili: "))

    new_book={"id":new_id,"title":title,"author":author,"year":year}
    books.append(new_book)
    save_books(books)
        print("✅ Yangi kitob qo‘shildi!")

# 2️⃣ Mavjud kitobni yangilash
def update_book():
    books = load_books()
    book_id = int(input("Yangilamoqchi bo‘lgan kitob ID sini kiriting: "))

    for book in books:
        if book["id"] == book_id:
            book["title"] = input(f"Yangi nom ({book['title']}): ") or book["title"]
            book["author"] = input(f"Yangi muallif ({book['author']}): ") or book["author"]
            book["year"] = int(input(f"Yangi nashr yili ({book['year']}): ") or book["year"])
            save_books(books)
            print("✏️ Kitob ma'lumotlari yangilandi!")
            return

    print("❌ Bunday ID bilan kitob topilmadi!")

# 3️⃣ Kitobni o‘chirish
def delete_book():
    books = load_books()
    book_id = int(input("O‘chirmoqchi bo‘lgan kitob ID sini kiriting: "))
    updated_books = [book for book in books if book["id"] != book_id]

    if len(updated_books) == len(books):
        print("❌ Bunday ID bilan kitob topilmadi!")
    else:
        save_books(updated_books)
        print("🗑️ Kitob o‘chirildi!")

# 🔹 Asosiy menyu
def main():
    while True:
        print("\n--- Kitoblar boshqaruvi ---")
        print("1. Yangi kitob qo‘shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o‘chirish")
        print("4. Chiqish")
        choice = input("Tanlov: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Chiqildi.")
            break
        else:
            print("❗ Noto‘g‘ri tanlov, qaytadan urinib ko‘ring!")

# Dastur ishga tushadi
main()

import requests
import random

# OMDb API kaliti (sizda o‘zingiznikini yozing)
API_KEY = "58b7ce24"

# 1️⃣ Foydalanuvchidan kino janrini so‘raymiz
genre = input("Qaysi janrdagi filmni xohlaysiz? (masalan: Action, Comedy, Drama): ")

# 2️⃣ OMDb API orqali shu janrga tegishli kinolarni izlaymiz
url = f"http://www.omdbapi.com/?apikey={API_KEY}&s={genre}"

response = requests.get(url)
data = response.json()

# 3️⃣ Agar natijalar mavjud bo‘lsa
if data.get("Response") == "True":
    movies = data.get("Search", [])
    movie = random.choice(movies)  # Tasodifiy bitta film tanlaymiz

    print("\n🎬 Tavsiya etilgan film:")
    print(f"🎞 Nomi: {movie['Title']}")
    print(f"📅 Yili: {movie['Year']}")
    print(f"🔗 IMDb ID: {movie['imdbID']}")

    # 4️⃣ Film haqida batafsil ma’lumotni olish
    movie_url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={movie['imdbID']}"
    detail = requests.get(movie_url).json()

    print(f"⭐ Reyting: {detail.get('imdbRating', 'Noma’lum')}")
    print(f"🎭 Janr: {detail.get('Genre', 'Noma’lum')}")
    print(f"🧑‍🎬 Rejissyor: {detail.get('Director', 'Noma’lum')}")
    print(f"📖 Tavsif: {detail.get('Plot', 'Tavsif yo‘q')}")
else:
    print("❌ Hech qanday film topilmadi. Boshqa janr sinab ko‘ring!")

