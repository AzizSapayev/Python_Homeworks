import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def get_Uzunlik(self):
        uzunlik=2*math.pi*(self.radius)
        return uzunlik
    def get_Yuzasi(self):
        yuza=math.pi*(self.radius**2)
        return yuza
circle1=Circle(5)
uzunlik=circle1.get_Uzunlik()
print(uzunlik)
circle1=Circle(5)
yuza=circle1.get_Yuzasi()
print(yuza)
class Shahs:
    def __init__(self,ism,familiya,passport,tyil):
        self.ism=ism
        self.familiya=familiya
        self.passport=passport
        self.tyil=tyil

    def get_info(self):
        info=f"{self.ism} {self.familiya}. "
        info+=f"Passport: {self.passport}, {self.tyil}"
        return info
    def get_age(self,yil):
        return yil-self.tyil
class Calculator:
    def __init__(self,a_son,b_son):
        self.a_son=a_son
        self.b_son=b_son

    def get_qoshish(self):
        qoshish=self.a_son+self.b_son
        return qoshish
    def get_ayirish(self):
         ayirish=self.a_son-self.b_son
         return ayirish
    def get_kopaytirish(self):
        kopaytirish=self.a_son*self.b_son
        return kopaytirish
    def get_bolish(self):
        bolish=self.a_son/self.b_son
        return bolish
masala1=Calculator(10,6)
boluv=masala1.get_qoshish()
print(boluv)
import math

# Baza sinf
class Shape:
    def area(self):
        raise NotImplementedError("area() metodi aniqlanmagan")
    def perimeter(self):
        raise NotImplementedError("perimeter() metodi aniqlanmagan")

# Doira
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius

# Kvadrat
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2
    def perimeter(self):
        return 4 * self.side

# Uchburchak (uch tomonli)
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    def perimeter(self):
        return self.a + self.b + self.c

# Misollar
circle = Circle(5)
print("Doira: yuzasi =", circle.area(), ", perimetri =", circle.perimeter())

square = Square(4)
print("Kvadrat: yuzasi =", square.area(), ", perimetri =", square.perimeter())

triangle = Triangle(3, 4, 5)
print("Uchburchak: yuzasi =", triangle.area(), ", perimetri =", triangle.perimeter())
class Node:
    """
    Daraxtning bitta tuguni.
    har bir tugun quyidagi xususiyatlarga ega:
    - value: tugundagi ma'lumot (raqam yoki solishtiriladigan boshqa obyekt)
    - left: chap bolalar (Node yoki None)
    - right: o'ng bolalar (Node yoki None)
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Ikkilik qidiruv daraxti (BST).
    xususiyatlar:
    - root: daraxt ildizi (Node yoki None)
    Metodlar:
    - insert(value): yangi qiymat qo'shadi
    - search(value): qiymat daraxtda bor-yo'qligini qaytaradi (True/False)
    - inorder(): daraxtni tartiblangan holda ro'yxatga chiqaradi
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Public method: value qo'shish."""
        if self.root is None:
            self.root = Node(value)
            return True  # muvaffaqiyatli qo'shildi
        else:
            return self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """
        Rekursiv yordamchi — current_node dan boshlanib joyni topadi.
        Agar qiymat mavjud bo'lsa, uni qo'shmaydi (duplikatlar rad etiladi).
        """
        if value == current_node.value:
            # Duplikat: bu yerda tanlov qilinadi. Biz duplikatlarni rad etamiz.
            return False
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
                return True
            else:
                return self._insert_recursive(current_node.left, value)
        else:  # value > current_node.value
            if current_node.right is None:
                current_node.right = Node(value)
                return True
            else:
                return self._insert_recursive(current_node.right, value)

    def search(self, value):
        """Public method: daraxtdan value ni qidiradi. True/False qaytaradi."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        """Rekursiv qidiruv yordamchi."""
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left, value)
        else:
            return self._search_recursive(current_node.right, value)

    def inorder(self):
        """Daraxtni tartiblangan ro'yxat holida qaytaradi (chap-root-o'ng)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result_list):
        if node is None:
            return
        self._inorder_recursive(node.left, result_list)
        result_list.append(node.value)
        self._inorder_recursive(node.right, result_list)


# -----------------------
# Misol: sinov va foydalanish
# -----------------------
if __name__ == "__main__":
    bst = BinarySearchTree()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    print("Qo'shilmoqda:", values_to_insert)
    for v in values_to_insert:
        ok = bst.insert(v)
        if not ok:
            print(f"{v} — duplikat, qo'shilmadi.")

    print("Inorder (sorted):", bst.inorder())

    # Qidiruv sinovlari
    tests = [25, 30, 80, 90]
    for t in tests:
        found = bst.search(t)
        print(f"Qidirish {t}: {'topildi' if found else 'topilmadi'}")

class Stack:
    def __init__(self):
        self.items = []   # Stack ichidagi elementlar ro'yxatda saqlanadi

    def push(self, item):
        """Stek ustiga yangi element qo'shish."""
        self.items.append(item)

    def pop(self):
        """Stekdan eng oxirgi qo'shilgan elementni olish (agar bo'sh bo'lmasa)."""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack bo'sh!"

    def peek(self):
        """Stekning eng yuqorisidagi elementni ko'rish (olmasdan)."""
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack bo'sh!"

    def is_empty(self):
        """Stek bo'sh yoki yo'q ekanligini tekshirish."""
        return len(self.items) == 0

    def size(self):
        """Stekdagi elementlar sonini qaytarish."""
        return len(self.items)


# -----------------
# Misol: foydalanish
# -----------------
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Hozirgi stack:", stack.items)  # [10, 20, 30]
    print("Tepadagi element:", stack.peek())  # 30

    print("Olingan element (pop):", stack.pop())  # 30
    print("Popdan keyin stack:", stack.items)  # [10, 20]

    print("Stack bo'shmi?", stack.is_empty())  # False
    print("Stackdagi elementlar soni:", stack.size())  # 2

class ShoppingCart:
    def __init__(self):
        # Har bir mahsulot lug'at ko'rinishida saqlanadi: nom -> {"price": narx, "qty": miqdor}
        self.items = {}

    def add_item(self, name, price, quantity=1):
        """Savatga mahsulot qo'shish yoki mavjud bo'lsa miqdorini oshirish."""
        if name in self.items:
            self.items[name]["qty"] += quantity
        else:
            self.items[name] = {"price": price, "qty": quantity}
        print(f"{quantity} ta '{name}' qo'shildi.")

    def remove_item(self, name):
        """Savatdan mahsulotni to'liq olib tashlash."""
        if name in self.items:
            del self.items[name]
            print(f"'{name}' savatdan olib tashlandi.")
        else:
            print(f"'{name}' savatda topilmadi.")

    def total_price(self):
        """Savatdagi barcha mahsulotlarning umumiy narxini hisoblash."""
        total = 0
        for item in self.items.values():
            total += item["price"] * item["qty"]
        return total

    def show_cart(self):
        """Savatdagi barcha mahsulotlarni ko'rsatish."""
        if not self.items:
            print("Savat bo'sh!")
            return
        print("🛒 Savatdagi mahsulotlar:")
        for name, info in self.items.items():
            print(f"- {name} | Narx: {info['price']} so'm | Miqdor: {info['qty']}")
        print(f"Umumiy narx: {self.total_price()} so'm")


# ------------------
# Misol: foydalanish
# ------------------
if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_item("Olma", 5000, 2)
    cart.add_item("Banana", 8000, 1)
    cart.add_item("Olma", 5000, 3)  # Mavjud bo'lsa miqdorini oshiradi

    cart.show_cart()

    cart.remove_item("Banana")
    cart.show_cart()

    print("Jami to'lov:", cart.total_price(), "so'm")

class Bank:
    def __init__(self):
        # Har bir mijoz 'hisob_raqam: balans' ko'rinishida saqlanadi
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        """Yangi mijoz (hisob) ochish."""
        if account_number in self.accounts:
            print("❌ Bu hisob raqami allaqachon mavjud!")
            return False
        self.accounts[account_number] = initial_balance
        print(f"✅ {account_number} raqamli hisob ochildi. Boshlang'ich balans: {initial_balance} so'm.")
        return True

    def deposit(self, account_number, amount):
        """Hisobga pul qo'yish."""
        if account_number not in self.accounts:
            print("❌ Bunday hisob raqami mavjud emas!")
            return False
        self.accounts[account_number] += amount
        print(f"💰 {amount} so'm qo'shildi. Yangi balans: {self.accounts[account_number]}")
        return True

    def withdraw(self, account_number, amount):
        """Hisobdan pul yechish."""
        if account_number not in self.accounts:
            print("❌ Bunday hisob raqami mavjud emas!")
            return False
        if self.accounts[account_number] < amount:
            print("❌ Balansda yetarli mablag' yo'q!")
            return False
        self.accounts[account_number] -= amount
        print(f"🏧 {amount} so'm yechildi. Yangi balans: {self.accounts[account_number]}")
        return True

    def transfer(self, from_acc, to_acc, amount):
        """Hisobdan hisobga pul o'tkazish."""
        if from_acc not in self.accounts or to_acc not in self.accounts:
            print("❌ Hisoblardan biri mavjud emas!")
            return False
        if self.accounts[from_acc] < amount:
            print("❌ Yuboruvchi hisobda mablag' yetarli emas!")
            return False
        self.accounts[from_acc] -= amount
        self.accounts[to_acc] += amount
        print(f"🔄 {from_acc} → {to_acc} ga {amount} so'm o'tkazildi.")
        return True

    def check_balance(self, account_number):
        """Hisob balansini ko'rish."""
        if account_number not in self.accounts:
            print("❌ Bunday hisob mavjud emas!")
            return None
        print(f"📊 {account_number} hisobida {self.accounts[account_number]} so'm bor.")
        return self.accounts[account_number]


# -------------------
# Misol: foydalanish
# -------------------
if __name__ == "__main__":
        bank = Bank()

        bank.create_account("ACC1001", 50000)
        bank.create_account("ACC1002", 20000)

        bank.deposit("ACC1001", 15000)
        bank.withdraw("ACC1002", 5000)

        bank.transfer("ACC1001", "ACC1002", 10000)

        bank.check_balance("ACC1001")
        bank.check_balance("ACC1002")

