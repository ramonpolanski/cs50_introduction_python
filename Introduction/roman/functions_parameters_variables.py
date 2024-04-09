# I create the function "hello" that takes a parameter "to" and prints "Hello, (+ parameter "to")"
# I also set the parameter "to" to "world" by default
def hello(to = "world"):
    print("hello,", to)

# Now I ask the user to enter a name and store it in the variable "name"
# I also remove whitespace from the beginning and end of the name and capitalize the first letter of each word

name = input("What's your name? ").strip().title()

# I call the function "hello" and pass the variable "name" as the argument "to"

hello(name)

# I call the function "hello" without passing any arguments so it uses the default value "world"

hello()