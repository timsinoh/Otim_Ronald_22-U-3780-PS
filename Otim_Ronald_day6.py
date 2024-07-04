# Error Handling in Python
# Exception Handling with try, except, else, and finally
# Custom exceptions

"""_summary_
Notes:
Error handling in python it helps to handle unexpected situations and errors.

1. Try: contains code that might throw an exception
NB: If an exception occurs the rest of the code in the try block is skipped or ignored

2. Except: catches and handles exceptions
NB: You can specify different handlers for different exception types

3. Else: the code runs if no exception occurs
If no exception are raised in the try block it runs.

4. Finally: It runs whether an exception is raised / occured or not
NB: Used for cleaning up actions

    """
# Example 1: Handle exceptions with division by zero

try:
    number = int(input('Enter a number: '))
    result = 20 / number
    
except ValueError:
    print("Invalid number! Please enter a valid number")
    
except ZeroDivisionError:
    print("Error! Division by zero is not allowed") 
    
else:
    print(f"Result is {result}")
    
finally:
    print("Excecution completed successfully")


# Exercise 1: Write a function that converts a string to an integer and handle both valueError
# if the string cannot be converted to an integer and the TypeError if the input is not a string. 
# Use multiple except block to handle these exceptions.

def convert_to_integer():
    try:
        # Get input from user
        value = input('Enter a value to convert to integer: ')
        # Attempt to convert the value to an integer
        result = int(value)
        print(f'The converted integer is: {result}')
    except ValueError:
        # Handle the case where the string cannot be converted to an integer
        print('Error: The provided string cannot be converted to an integer.')
    except TypeError:
        # Handle the case where the input is not a string
        print('Error: The provided input is not a string.')
    finally:
        print('Execution completed.')

# Call the function
convert_to_integer()
           
# Custom exception handling
# Example 2: Exception raised for error in the input, if funds are sufficient.

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Attempt to withdraw {self.amount} with only {self.balance} in account"
        super().__init__(self.message)

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Custom exception handling
try:
    balance = 200000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
    
except InsufficientFundsError as e:
    print(f"Error: {e.message}")
    
else:
    print(f"Withdrawal Successfully! {new_balance} ")
    
finally:
    print("Transaction completed")
    
"""_summary_
# Defining a Custom Exception

Class CustomError(Exception):
### Custom Exception for specific error cases
 
 def_init_(self, message):
     super()._init_(message)
     self.message = message
     
### Raising a Custom Exception
def check_value(value):
    if value is < 0 or value:
        raise CustomError("Value should be negative")
    return value
    
# Handle exceptions with try, except, else, and finally
try:
result = check_value(-10)

except CustomError as e:
    print(f"Custom error caught: {e.message}")
    
"""
    
# Exercise 2: Create a custom exception InvalidAgeError and write a function that raises
# this exception if the given age is negative. Handle this custom exception when calling the function.   

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Age {self.age} is invalid. Age cannot be negative."
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise InvalidAgeError(age)
    return age

# Get user input at runtime
try:
    while True:
        age = int(input("Enter your age: "))
        age = check_age(age)
        print(f"Age is valid: {age}")
        break
except InvalidAgeError as e:
    print(f"Error: {e.message}")
else:
    print("Age validation successful!")
finally:
    print("Age validation completed")