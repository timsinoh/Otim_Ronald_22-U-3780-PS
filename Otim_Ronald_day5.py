# Defining Functions

#Functions syntax and parameters
#Return values

# Functions in python are defined using the 'def' keyword, followed by the function name
# parentheses (), inside the parentheses you put a parameter name, and the colon.


# Example 1:
def multiply(a, b):
    return a * b
result = multiply(5, 10)
print(result)

# Example 2: Multiple return values

def get_coordinates():
    return 10, 20

x,y = get_coordinates()
print (x, y)

# Exercise 1: Define a function greet with a parameter name, set to 'Guest', and print a message
# I am a software programer

def greet(name='Otim'):
    print(f"I am the College president of NutriMind Makerere, {name}")


greet()

# Example 3: Return multiple values 
def get_name_and_position():
    name = 'Otim Ronald'
    position = 'I am the College president of NutriMind Makerere'
    return name, position
name, position = get_name_and_position()
print(name, position)

# Exercise 4: Return multiple return vales of your name and age

def get_name_and_age():
    name = 'Otim Ronald'
    age = 25
    return name, age
name, age = get_name_and_age()
print(name, age)

# Notes

"""_summary_
def: keyword to define a function
function_name: name of the function
parameters: Optional, arguments passed to the function
Docstrings: Optional, describes the function purpose
return: optional, returns a value from the function
    """
# Syntax for defining a function
#def function_name(parameters):
#   """_summary_"""
#    function body
#    return value
 
#Lambda function
# Lambda functions a small anonymous functions defined using the lambda keyword
# They are restricted to a single expression

# Syntax for lambda function
#lymbda parameter: expression

#Example 4: Create a lambda function to add two numbers

add = lambda a, b: a+b
print(add(45, 70))

#Example 5: Use cases of lambda function for sorting

coordinates = [(1,2),(2,3),(3,1),(5,0)]

coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map, Filter and Reduce
#Example 6: Get the squares of 1 to 5 using map, filter and reduce

number_squares = [1,2,3,4,5]

squares = list(map(lambda x: x**2, number_squares))

print(squares)

# Exercise 4: Define a function to get user info that accepts arbitrary keyword arguments and prints each key value pair

get_user_info = lambda **kwargs: [print(f"{key}: {value}") for key, value in kwargs.items()]
get_user_info(name="Otim", age=25, occupation="I am the College president of NutriMind Makerere")


