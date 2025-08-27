total_sales = 0
with open('sales.txt', 'r') as sales_file:
    for line in sales_file:
        amount = float(line)
        total_sales += amount

print(f"Totat sales: {total_sales:.2f}")