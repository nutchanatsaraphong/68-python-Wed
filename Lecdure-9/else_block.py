try:
    value = input(input("Enter a number:"))
    result = 10 / value
except ZeroDivisionError:
    print("Cannot divde by zero!")
else:
    print(f"The result is{result}")

print("End of progrm")