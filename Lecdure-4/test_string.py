input_string = input("Enter a string: ")
modified_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_cher = char.upper()
    if upper_cher in vowels:
        modified_string += "*"
    else:
        modified_string += upper_cher
print("Modified string:", modified_string)