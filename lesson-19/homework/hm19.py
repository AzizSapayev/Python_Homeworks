import pandas as pd
sales=pd.read_csv('sales_data.csv')
total=sales.groupby('Quantity')
len(total)
total['Quantity'].sum()
sales
import pandas as pd

# 1. CSV faylni o‘qish
df = pd.read_csv('sales_data.csv')

# 2. Har bir toifaga ko‘ra guruhlash
grouped = df.groupby('Category')

# 3. Har bir toifa uchun jami sotilgan miqdor
total_quantity = grouped['Quantity'].sum()

# 4. Bir birlik uchun o‘rtacha narx
avg_price = grouped['Price'].mean()

# 5. Bitta tranzaksiyada sotilgan maksimal miqdor
max_quantity = grouped['Quantity'].max()

# 6. Har bir toifadagi eng ko‘p sotilgan mahsulotni topish
most_sold_product = (
    df.groupby(['Category', 'Product'])['Quantity']
    .sum()
    .reset_index()
    .loc[lambda x: x.groupby('Category')['Quantity'].idxmax()]
)

# 7. Eng yuqori umumiy savdo (Quantity * Price) bo‘lgan sanani aniqlash
df['Total_Sales'] = df['Quantity'] * df['Price']
top_sales_date = df.groupby('Date')['Total_Sales'].sum().idxmax()

# 8. Natijalarni umumlashtirish
summary = pd.DataFrame({
    'Jami Sotilgan Miqdor': total_quantity,
    'O‘rtacha Narx': avg_price,
    'Maksimal Miqdor (bitta tranzaksiya)': max_quantity
})

# 9. Natijalarni chiqarish
print("=== Har bir toifa bo‘yicha umumiy statistika ===")
print(summary)
print("\n=== Eng ko‘p sotilgan mahsulotlar ===")
print(most_sold_product)
print(f"\n=== Eng yuqori umumiy savdo sodir bo‘lgan sana: {top_sales_date} ===")

customer=pd.read_csv('customer_orders.csv')
customer
low=(customer.groupby('CustomerID')['OrderID']).count().reset_index(name='OrderCount').query('OrderCount<30')
low
uniq=customer[customer['Price']>120]['CustomerID'].unique()
uniq
high_price_customers = customer[customer['Price'] > 120]['CustomerID'].unique()
high_price_customers

product_summary=customer.groupby('Product')[['Quantity','Price']].sum().reset_index()
product_summary
product_summary['TotalPrice'] = product_summary['Quantity'] * product_summary['Price']
filtered_products = product_summary[product_summary['Quantity'] < 5]
filtered_products

people=pd.read_excel('population_salary_analysis.xlsx')
people
