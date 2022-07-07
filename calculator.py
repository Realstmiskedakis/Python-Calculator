'''
@Author: Stelios Miskedakis - @Realstmiskedakis / @Acidshell.gr
Language: Python '3.10.5'
Version: '1.0V'
About this program:

This program is a simple calculator that takes the user's data and then calculates it so,
( e.g User Input = 1 + 1, output(calculate => user input = 2))

'''

# Packages / Libraries
import math

# The Calculation Functions

'''
This program defines six different functions that each perform a different mathematical operation. 

The add function takes in two parameters and returns the sum of those two numbers. 
The subtract function takes in two parameters and returns the difference of those two numbers. 
The multiply function takes in two parameters and returns the product of those two numbers. 
The divide function takes in two parameters and returns the quotient of those two numbers. 
The remainder function takes in two parameters and returns the remainder of those two numbers. 
The power function takes in two parameters and returns the value of the first parameter raised to the power of the second parameter. 
The cos function takes in one parameter and returns the cosine of that number. 
The sin function takes in one parameter and returns the sine of that number. 
The pi function takes no parameters and returns the value of pi. 
The square_root function takes in one parameter and returns the square root of that number.

'''


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def remainder(x, y):
    return x % y


def power(x, y):
    return x ** y


def cos_(x):
    return math.cos(x)


def sin_(x):
    return math.sin(x)


def pi():
    return math.pi


def square_root(x):
    return math.sqrt(x)


# The Main Function

def calculator(add, subtract, multiply, divide, remainder, power, cos, sin, pi, square_root):
    """
    This function prints out the options for the calculator.

    :param add: adds two numbers
    :param subtract: Subtracts the second number from the first number
    :param multiply: multiply two numbers
    :param divide: /
    :param remainder: %
    :param power: **
    :param cos: cosine
    :param sin: The sine of a number
    :param pi: 3.14
    :param square_root: square root of a number

    """
    print("1. Add +")
    print("2. Subtract - ")
    print("3. Multiply *")
    print("4. Divide / ")
    print("5. Remainder %")
    print("6. Power **")
    print("7. Cos")
    print("8. Sin")
    print("9. pi 3.14")
    print("10. Squareroot ")

    user_choice = input(">> Choose one of these, Answer w/ ( e.g 2 for subtract ): ")
    # This is a conditional statement. It checks if the user_choice is in the list of numbers.
    if user_choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10'):
        try:
            if user_choice == '1':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "+", user_num2, "=", add(user_num1, user_num2))

            elif user_choice == '2':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "-", user_num2, "=", subtract(user_num1, user_num2))

            elif user_choice == '3':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "*", user_num2, "=", multiply(user_num1, user_num2))

            elif user_choice == '4':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "/", user_num2, "=", divide(user_num1, user_num2))

            elif user_choice == '5':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "%", user_num2, "=", remainder(user_num1, user_num2))

            elif user_choice == '6':
                user_num1 = float(input(">> Enter your 1st number: "))
                user_num2 = float(input(">> Enter your 2st number: "))
                print(">>", user_num1, "**", user_num2, "=", power(user_num1, user_num2))

            elif user_choice == '7':
                user_num1 = float(input(">> Enter your 1st number: "))
                print(">> The Cos of", user_num1, "=", cos_(user_num1))

            elif user_choice == '8':
                user_num1 = float(input(">> Enter your 1st number: "))
                print(">> The Sin of", user_num1, "=", sin_(user_num1))

            elif user_choice == '9':
                print(">>", math.pi)

            elif user_choice == '10':
                user_num1 = float(input(">> Enter your 1st number: "))
                print(">> The Squareroot of", user_num1, "=", square_root(user_num1))

        # This is a try/except block. It is used to catch errors that may occur in the code.
        except (ValueError, ZeroDivisionError, InterruptedError):
            print("Invalid Input, Exit..")
            quit()


# Calling the calculator function and passing in the functions that we defined earlier as parameters.
calculator(add, subtract, multiply, divide, remainder, power, cos_, sin_, pi, square_root)
