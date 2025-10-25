import sqlite3
conn=sqlite3.connect('roster.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Ism TEXT,
    Tur TEXT,
    Yosh INTEGER
)
''')
cursor.execute("INSERT INTO Roster (Ism, Tur, Yosh) VALUES ('Ali', 'O‘quvchi', 20)")
cursor.execute("INSERT INTO Roster (Ism, Tur, Yosh) VALUES ('VAli', 'O‘quvchi', 21)")
cursor.execute("INSERT INTO Roster (Ism, Tur, Yosh) VALUES ('Aziz', 'O‘quvchi', 22)")
conn.commit()
cursor.execute("Select * from Roster")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
import sqlite3

# 1. Bazaga ulanamiz
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# 2. Jadvalni yaratamiz (agar mavjud bo‘lmasa)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Ism TEXT,
    Turlar TEXT,
    Yosh INTEGER
)
''')

# 3. Jadvalga qiymatlarni qo‘shamiz
cursor.execute("INSERT INTO Roster (Ism, Turlar, Yosh) VALUES ('Benjamin Sisko', 'Inson', 40)")
cursor.execute("INSERT INTO Roster (Ism, Turlar, Yosh) VALUES ('Jadzia Dax', 'Trill', 300)")
cursor.execute("INSERT INTO Roster (Ism, Turlar, Yosh) VALUES ('Kira Neris', 'Bajoran', 29)")

conn.commit()  # saqlaymiz

# 4. Jadzia Dax nomini Ezri Dax qilib yangilaymiz
cursor.execute("UPDATE Roster SET Ism = 'Ezri Dax' WHERE Ism = 'Jadzia Dax'")
conn.commit()

# 5. Bajoran turlaridagi odamlarni chiqaramiz (faqat Ism va Yosh)
cursor.execute("SELECT Ism, Yosh FROM Roster WHERE Turlar = 'Bajoran'")
natijalar = cursor.fetchall()

print("Bajoran turidagi kishilar:")
for ism, yosh in natijalar:
    print(f"{ism} — {yosh} yosh")

# 6. Bog‘lanishni yopamiz
conn.close()
