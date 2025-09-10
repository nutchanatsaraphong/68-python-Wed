try:
    value = input(input("Enter a number:"))
    value = 10 / value
except ValueError:

    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divde by zero!")
print("End of progrm")