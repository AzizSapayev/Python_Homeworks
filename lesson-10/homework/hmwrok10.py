class Vazifa:
    def __init__(self,nomi,tavsifi,tugash_sanasi,holati):
        self.nomi=nomi
        self.tavsifi=tavsifi
        self.tugash_sanasi=tugash_sanasi
        self.holati=holati
    
    def __init__(self):
        self.vazifalar={}

    def todoList(self):
        if self.nomi  not in self.vazifalar:
            self.vazifalar.append(self.nomi)

class Task:
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = False  # Boshlang'ich holat

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✅ Bajargan" if self.completed else "❌ Bajarilmagan"
        return f"Vazifa: {self.name} | {status}\nTavsif: {self.description}\nTugash sanasi: {self.due_date}"


class ToDoList:
        def __init__(self):
            self.tasks = []

        def add_task(self, task):
            self.tasks.append(task)
            print("✅ Vazifa qo'shildi!")

        def mark_task_completed(self, task_name):
            for task in self.tasks:
                if task.name == task_name:
                    task.mark_completed()
                    print("✅ Vazifa bajarilgan deb belgilandi!")
                    return
            print("❌ Bunday vazifa topilmadi!")

        def list_all_tasks(self):
            if not self.tasks:
                print("📭 Hech qanday vazifa yo'q!")
            for task in self.tasks:
                print(task, "\n" + "-" * 30)

        def list_incomplete_tasks(self):
            incomplete = [task for task in self.tasks if not task.completed]
            if not incomplete:
                print("🎉 Barcha vazifalar bajarilgan!")
            for task in incomplete:
                print(task, "\n" + "-" * 30)


# ----------------------------
# CLI (foydalanuvchi menyusi)
# ----------------------------
def main():
    todo_list = ToDoList()

    while True:
        print("\n--- 📝 ToDo List Menyu ---")
        print("1. Vazifa qo'shish")
        print("2. Vazifani bajarilgan deb belgilash")
        print("3. Barcha vazifalarni ko'rish")
        print("4. Faqat bajarilmagan vazifalarni ko'rsatish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")

        if choice == "1":
            name = input("Vazifa nomi: ")
            desc = input("Tavsif: ")
            due = input("Tugash sanasi (yyyy-mm-dd): ")
            todo_list.add_task(Task(name, desc, due))

        elif choice == "2":
            name = input("Qaysi vazifa tugallandi? Nomini kiriting: ")
            todo_list.mark_task_completed(name)

        elif choice == "3":
            todo_list.list_all_tasks()

        elif choice == "4":
            todo_list.list_incomplete_tasks()

        elif choice == "5":
            print("👋 Dasturdan chiqildi!")
            break

        else:
            print("❌ Noto'g'ri tanlov! Qaytadan urinib ko'ring.")


# Asosiy dastur
if __name__ == "__main__":
    main()

class Post:
    def __init__(self,sarlavha,kontent,muallif):
        self.sarlavha=sarlavha
        self.kontent=kontent
        self.muallif=muallif

class Blog:
    def __init__(self):
        self.royhat={}
    
    def get_add_xabar(self,sarlavha,kontent,muallif):
                self.sarlavha=sarlavha
                self.kontent=kontent
                self.muallif=muallif
                self.royhat.append(self.sarlavha,self.kontent,self.muallif)
    def get_count(self):
          sana=len(self.royhat)
          print(sana)
    def get_muallif(self):
          if self.muallif==(self.muallif in self.royhat):
                print(self.muallif)


class Post:
    def __init__(self, sarlavha, kontent, muallif):
        self.sarlavha = sarlavha
        self.kontent = kontent
        self.muallif = muallif

    def __str__(self):
        return f"{self.sarlavha} | {self.muallif}\n{self.kontent}"

class Blog:
    def __init__(self):
        self.royhat = []

    def add_xabar(self, sarlavha, kontent, muallif):
        post = Post(sarlavha, kontent, muallif)
        self.royhat.append(post)
        print("✅ Xabar qo'shildi!")

    def get_count(self):
        print(f"Jami xabarlar soni: {len(self.royhat)}")

    def get_muallif_xabarlari(self, muallif):
        print(f"\n{muallif} muallifining xabarlari:")
        for post in self.royhat:
            if post.muallif == muallif:
                print(post)
                print("-" * 30)

    def list_all(self):
        print("\nBarcha xabarlar:")
        for i, post in enumerate(self.royhat, 1):
            print(f"{i}. {post}")
            print("-" * 30)

    def delete_post(self, index):
        if 0 <= index < len(self.royhat):
            del self.royhat[index]
            print("❌ Xabar o'chirildi!")
        else:
            print("❌ Noto'g'ri indeks!")

    def edit_post(self, index, new_sarlavha=None, new_kontent=None):
        if 0 <= index < len(self.royhat):
            if new_sarlavha:
                self.royhat[index].sarlavha = new_sarlavha
            if new_kontent:
                self.royhat[index].kontent = new_kontent
            print("✏️ Xabar tahrirlandi!")
        else:
            print("❌ Noto'g'ri indeks!")

    def show_last_posts(self, n=3):
        print(f"\nSo'nggi {n} ta xabar:")
        for post in self.royhat[-n:]:
            print(post)
            print("-" * 30)

# CLI
def main():
    blog = Blog()
    # Namuna xabarlar
    blog.add_xabar("Python yangiliklari", "Python 3.12 chiqdi!", "Azizbek")
    blog.add_xabar("Django darsi", "Django asoslari", "Azizbek")
    blog.add_xabar("AI", "AI haqida maqola", "Ali")

    while True:
        print("\n--- 📰 Blog Menyu ---")
        print("1. Xabar qo'shish")
        print("2. Barcha xabarlarni ko'rish")
        print("3. Muallif xabarlarini ko'rish")
        print("4. Xabarni o'chirish")
        print("5. Xabarni tahrirlash")
        print("6. So'nggi xabarlarni ko'rsatish")
        print("7. Xabarlar soni")
        print("0. Chiqish")

        tanlov = input("Tanlang (0-7): ")

        if tanlov == "1":
            sarlavha = input("Sarlavha: ")
            kontent = input("Kontent: ")
            muallif = input("Muallif: ")
            blog.add_xabar(sarlavha, kontent, muallif)

        elif tanlov == "2":
            blog.list_all()

        elif tanlov == "3":
            muallif = input("Muallif ismi: ")
            blog.get_muallif_xabarlari(muallif)

        elif tanlov == "4":
            blog.list_all()
            try:
                index = int(input("O'chirmoqchi bo'lgan xabar raqamini kiriting: ")) - 1
                blog.delete_post(index)
            except ValueError:
                print("❌ Raqam kiriting!")

        elif tanlov == "5":
            blog.list_all()
            try:
                index = int(input("Tahrirlamoqchi bo'lgan xabar raqamini kiriting: ")) - 1
                new_sarlavha = input("Yangi sarlavha (bo'sh qoldirsangiz o'zgarmaydi): ")
                new_kontent = input("Yangi kontent (bo'sh qoldirsangiz o'zgarmaydi): ")
                blog.edit_post(index, new_sarlavha or None, new_kontent or None)
            except ValueError:
                print("❌ Raqam kiriting!")

        elif tanlov == "6":
            try:
                n = int(input("Nechta so'nggi xabar ko'rsatilsin? (standart 3): ") or 3)
                blog.show_last_posts(n)
            except ValueError:
                print("❌ Raqam kiriting!")

        elif tanlov == "7":
            blog.get_count()

        elif tanlov == "0":
            print("👋 Dasturdan chiqildi!")
            break

        else:
            print("❌ Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()
class Account:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 {amount} so'm qo'shildi. Yangi balans: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Balansda yetarli mablag' yo'q!")
        else:
            self.balance -= amount
            print(f"🏧 {amount} so'm yechildi. Yangi balans: {self.balance}")

    def __str__(self):
        return f"Hisob: {self.account_number} | Egasi: {self.owner} | Balans: {self.balance} so'm"


class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        if account.account_number in self.accounts:
            print("❌ Bu hisob allaqachon mavjud!")
        else:
            self.accounts[account.account_number] = account
            print("✅ Hisob muvaffaqiyatli yaratildi!")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if not sender or not receiver:
            print("❌ Hisoblardan biri topilmadi!")
            return

        if sender.balance < amount:
            print("❌ Yuboruvchi hisobda mablag' yetarli emas!")
            return

        sender.balance -= amount
        receiver.balance += amount
        print(f"🔄 {from_acc} → {to_acc} ga {amount} so'm o'tkazildi.")


# ----------------------------
# CLI (foydalanuvchi menyusi)
# ----------------------------
def main():
    bank = Bank()

    while True:
        print("\n--- 🏦 Bank Tizimi Menyu ---")
        print("1. Hisob qo'shish")
        print("2. Balansni tekshirish")
        print("3. Pul qo'yish (Deposit)")
        print("4. Pul yechib olish")
        print("5. Hisobdan hisobga pul o'tkazish")
        print("6. Barcha hisoblarni ko'rsatish")
        print("7. Chiqish")

        choice = input("Tanlang (1-7): ")

        if choice == "1":
            acc_num = input("Hisob raqami kiriting: ")
            owner = input("Egasi nomi: ")
            bank.add_account(Account(acc_num, owner))

        elif choice == "2":
            acc_num = input("Hisob raqami: ")
            acc = bank.get_account(acc_num)
            print(acc if acc else "❌ Hisob topilmadi!")

        elif choice == "3":
            acc_num = input("Hisob raqami: ")
            amount = int(input("Summani kiriting: "))
            acc = bank.get_account(acc_num)
            acc.deposit(amount) if acc else print("❌ Hisob topilmadi!")

        elif choice == "4":
            acc_num = input("Hisob raqami: ")
            amount = int(input("Summani kiriting: "))
            acc = bank.get_account(acc_num)
            acc.withdraw(amount) if acc else print("❌ Hisob topilmadi!")

        elif choice == "5":
            from_acc = input("Qaysi hisobdan: ")
            to_acc = input("Qaysi hisobga: ")
            amount = int(input("Summani kiriting: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == "6":
            for acc in bank.accounts.values():
                print(acc)

        elif choice == "7":
            print("👋 Chiqildi!")
            break

        else:
            print("❌ Noto'g'ri tanlov!")


if __name__ == "__main__":
    main()

