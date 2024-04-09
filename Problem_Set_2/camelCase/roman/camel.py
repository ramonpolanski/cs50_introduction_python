name = input("Enter a variable name in camelCase: ")
print(name)
capital_letters = [char for char in name if char.isupper()]
print(capital_letters)