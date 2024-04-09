# I defineńe the function "main" that takes no parameters

def main():

    # In the main function I ask the user to input a value and store it in the variable "x" as a float

    x = float(input("Enter a number: "))

    # I call the function "square" and pass the variable "x" as the argument "x" to the parameter "n"

    print("The square of", x, "is", square(x))

    # Now with a formated string again, also rounding the result to 2 decimal places

    print(f"The square of {x} is {square(x):.2f}")

# I define the function "square" that takes a parameter "n" and returns the square of "n" and round the result to 2 decimal places

def square(n):
    return round(n * n, 2)

# I call the function "main"

main()

