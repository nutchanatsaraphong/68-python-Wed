try:
    value = input(input("Enter a number:"))
    value = 10 / value
except Exception as e:
    print(f"An error occurred: {e}")

print("End of progrm")