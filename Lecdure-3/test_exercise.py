hours = int(input("Enter the number of hours worked: "))
pay = 40
if hours > 40:
    pay = ((hours - 40) *1.5*pay) + (40 * pay)
else :
    pay = (hours * pay) 
print(pay)