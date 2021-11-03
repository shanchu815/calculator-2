"""CLI application for a prefix-notation calculator."""
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code

"repeat forever:"
input_string = input("> ")

while input_string != "q":

#"tokenize input"
    tokens = input_string.split(' ')
    num1 = int(tokens[1])
    num2 = int(tokens[2])

#"if the first token is 'q':"
#"quit"
    # if tokens[0] == "q":
    #     break

#"else:"
    if tokens[0] == "pow":
        print(power(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "cube":
        print(cube(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "square":
        print(square(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "mod":
        print(mod(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "+":
        print(add(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "-":
        print(subtract(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "/":
        print(divide(num1, num2))
        input_string = input("> ")

    elif tokens[0] == "*":
        print(multiply(num1, num2))
        input_string = input("> ")

#"(decide which math function to call based on first token)"
#"if the first token is 'pow':"
#"call the power function with the other two tokens"
