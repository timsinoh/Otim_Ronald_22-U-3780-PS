#Python Best Practices
""" _Summary_
   follow PEP 8
1. Indentation
2. Maximum line Length
3. Blank lines
4. Use meaningful names
5. Use list comprehensions
"""

# Example of Good meaningfull name
def calculate_area(radius):
    pass
total_price = 10000


#Python operators

"""_Summary_
Name of the operators      Symbol with example
Addition                      x + y
Substraction                  x - y
Multiplication                x * y
Division                      x / y
Modulus                       x %  y
Exponentiation                x ** y
floor division                x // y

Name of the operators      Symbol with example
Equal                         x == y
Not equal                     x != y
Greater than                  x >> y
Less than                     x << y
Greater than or equal to      x >= y
less than or equal to         x <= y

# Example of Python logical operators 
Name of the operators      Symbol with example
and                             and  
or                              or 
not                             not 

# Example of Membership operators
Name                        Symbol with example
in                              x in y
not in                          x not in y

# Example of Python Bitwise operators

OPERATOR	DESCRIPTION	        SYNTAX  
&	        Bitwise AND	        a & b   
|	        Bitwise OR	        a | b   
^	        Bitwise XOR	        a ^ b   
~           Bitwise NOT         ~ a     
<<          Bitwise L shift     a << b      
>>          Bitwise R shift     a >> b

#Python cases
1. snake_case
2. camelCase
3. PascalCase

"""
# Comprehensions (list, dictionary comprehensions)
"""_summary_
Comprehensions provide a concise way to crate lists and dictionaries
What is the symbol for
lists           [] square brackets used to store multipe items in a single variable
dictionaries    {} curly brackets used to store data values in key:value pairs  
    """
#Example 1: Basic List Comprehensions

#Create a list of squares in range of 10
list_of_squares = [x**2 for x in range(10)]
print(list_of_squares)

#Exercise 1: Create a list of even square in the range of 20
even_squares = [x**2 for x in range(20) if x**2 % 2 == 0]
print(even_squares)

#Example 2: Dictionary Comprehensions
# Create a dictionary comprehension for favorites cars and count the lengths of characters
favorite_cars = ['BMW', 'Jeep', 'Mercedes', 'fordraptor']
car_lengths = {car: len(car) for car in favorite_cars}
print(car_lengths)

# Exercise 2: Create a list of tuple where each tuple contains a number and its cube for numbers between 1 and 10 using a dictionary comprehension
cube_dict = {i: i**3 for i in range(1, 11)}
print(cube_dict)

