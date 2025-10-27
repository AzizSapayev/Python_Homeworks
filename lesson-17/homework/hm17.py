import pandas  as pd
malumotlar = {
    'Ism': ['Alis', 'Bob', 'Charli', 'Devid'],
    'Yosh': [25, 30, 35, 40],
    'Shahar': ['Nyu-York', 'San-Fransisko', 'Los-Anjeles', 'Chikago']
}
pf=pd.DataFrame(malumotlar)
pf
pf=pf.rename(columns={'Ism':'ism_ism','Yosh':'yosh'})
pf
print(pf.head(2))
print(pf['yosh'].mean())
print(pf[['yosh','Shahar']])
import numpy as np
pf['Ish haqi']=np.random.randint(2000,10000,size=len(pf))
print(pf)
print(pf.describe())
import pandas as pd

# Ma'lumotlar
malumotlar = {
    'Oy': ['Yanvar', 'Fevral', 'Mart', 'Aprel'],
    'Sotuvlar': [5000, 6000, 7500, 8000],
    'Xarajatlar': [3000, 3500, 4000, 4500]
}

# DataFrame yaratish
sales_and_expenses = pd.DataFrame(malumotlar)

# Natijani chop etish
print(sales_and_expenses)


# DataFrame yaratish
sales_and_expenses = pd.DataFrame(malumotlar)

# Maksimal qiymatlar
max_sotuv = sales_and_expenses['Sotuvlar'].max()
max_xarajat = sales_and_expenses['Xarajatlar'].max()

# Minimal qiymatlar
min_sotuv = sales_and_expenses['Sotuvlar'].min()
min_xarajat = sales_and_expenses['Xarajatlar'].min()

# O'rtacha qiymatlar
avg_sotuv = sales_and_expenses['Sotuvlar'].mean()
avg_xarajat = sales_and_expenses['Xarajatlar'].mean()

# Natijalarni chop etish
print("📈 Maksimal sotuv:", max_sotuv)
print("📉 Minimal sotuv:", min_sotuv)
print("⚖️  O‘rtacha sotuv:", avg_sotuv)
print("----------------------------")
print("📈 Maksimal xarajat:", max_xarajat)
print("📉 Minimal xarajat:", min_xarajat)
print("⚖️  O‘rtacha xarajat:", avg_xarajat)

import pandas as pd

# Ma'lumotlar lug'at shaklida
data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

# DataFrame yaratish
expenses = pd.DataFrame(data)

# Natijani ko‘rsatish
print(expenses)

expenses['Max_Expense'] = expenses[['January', 'February', 'March', 'April']].max(axis=1)

# Natijani chop etish
print(expenses[['Category', 'Max_Expense']])

expenses['Min_Expense'] = expenses[['January', 'February', 'March', 'April']].min(axis=1)

# Natijani chop etish
print(expenses[['Category', 'Min_Expense']])

expenses['AVG_Expense'] = expenses[['January', 'February', 'March', 'April']].mean(axis=1)

# Natijani chop etish
print(expenses[['Category', 'AVG_Expense']])


