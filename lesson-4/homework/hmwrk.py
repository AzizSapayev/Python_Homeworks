Uyga vazifa
my_dict = {"apple": 10, "banana": 5, "cherry": 20, "date": 15}

my_dict = {"apple": 10, "banana": 5, "cherry": 20, "date": 15}
ascending=dict(sorted(my_dict.items(),key=lambda x:x[1]), reverse=True)
print(ascending)

descending = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))
print( descending)


my_dict = {0: 10, 1: 20}

# Yangi key/value qo‘shamiz
my_dict[2] = 30

print(my_dict)
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dict = {}       # Bo‘sh dictionary yaratamiz
new_dict.update(dic1)
new_dict.update(dic2)
new_dict.update(dic3)

print(new_dict)
my_dict={}
def myfunction(n):
    for i in range(1,n+1):
        my_dict[i]=i**2
myfunction(5)
print(my_dict)
my_dict={}
def myfunction(n):
    for i in range(1,n+1):
        my_dict[i]=i**2
myfunction(15)
print(my_dict)
my_set={1,2,3,4,5,6}
print(my_set)
items=input("elementlarni vergul bilan kiriting")
my_set=set(items.split(","))
print("Natija: ", my_set)
my_set={"apple","Cherry","banana"}
for item in my_set:
    print(item)

for index,item in enumerate(my_set):
    print(index,item)
my_set={1,2,3,4,5,6}
my_set.add(8)
print(my_set)

my_set={1,2,3,4,5,6}
my_set.update([8,9,10,11])
print(my_set)
my_set = {1, 2, 3, 4}
my_set.remove(3)
print(my_set)

my_set = {1, 2, 3, 4}
my_set.discard(3)
my_set.discard(10)  # Xato bermaydi
print(my_set)

