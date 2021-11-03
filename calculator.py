"""CLI application for a prefix-notation calculator."""
from functools import reduce
#reduce(lambda a, b: a+b, lis)
#reduce(lambda a, b: b = int(b), lis) ???

from arithmetic import (add, add_infinite, subtract, multiply, divide, square, cube,
                        power, mod)


# Replace this with your code

"repeat forever:"
input_string = input("> ")

while input_string != "q":

#"tokenize input"
    tokens = input_string.split(' ')
    num1 = int(tokens[1])
    num2 = int(tokens[2])

    #store first value of tokens in new variable "command"
    #command = tokens[0]

    #remove first value from tokens?
    #tokens.pop(0)

    #convert the rest of the values in tokens into integers
    #tokens = [int(x) for x in tokens]

    #so now all if statements in the while loop will check what command is
    #& then they run the now shorter tokens list (of NUMBERS) through the function

    #if command == "pow":
    #   print(infinite_pow(tokens))
    #   input_string = input("> ")

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

'''    elif tokens[0] == "+":
        print(add_infinite(tokens))
        input_string = input("> ")'''

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
