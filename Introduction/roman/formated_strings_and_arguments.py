# the print function automatically sets the argument "end" to "\n" by default.
# This means that after printing the string, it will add a newline character.
# In order to change this behavior, I set the argument "end" to an empty string.

name = input ("What's your name? ")
print("Hello,",  end=" ")
print(name)

# this is a formatted string

print(f"Hello, {name}")
