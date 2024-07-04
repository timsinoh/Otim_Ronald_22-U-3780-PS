# Inheritance and Polymorphism
"""_summary_
Inheritance and method overriding
Polymorphism and method resolution
order
Abstract classes and interfaces
    """

# Inheritace and method overriding
"""_summary_
  ---description
  Inheritance and method overriding allows a class(child class) to inherit attributes and methods
  from another class(parent class).
    """
    
# Example 1: Syntax create a class where a dog inherits from animal and overrides with a speak method

class Animal:
    def speak(self):
        return 'Mwe Mwe Mwe'
    
class Dog(Animal):
    def speak(self):
        return 'Barks'

#Implementation of inherited classes
animal = Animal()
dog = Dog()

print(animal.speak())
print(dog.speak())

# Polymorphism and method resolution
# Polymorphism allows objects of different classes to be treated as object of a common superclass.
# Method resolutiom order (MRO). Is order in which python looks for a method in a hierarchy classes.

# Example 2: How polymorphism works in python

class Animal:
    def speak(self):
        return "Croock"
    
class Dog(Animal):
    def speak(self):
        return "Barks"
    
class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())
    
make_animal_speak(Dog())
make_animal_speak(Cat())

# Exercise 1: Create a simple application to manage different types of vehicles. Implement
# derived class to demonstrate inheritance and polymorhism.
"""_summary_
Requirements
1. Base class to vechicle
attribtes: make, model and year
methods: display_info()

2. Derived classes:
Car: inherits from vechile
attributes: number_of_doors
overrides: display_info()

3. Motorcycle: Inherit from vehicle
Attributes: type_of_bike(cruiser, sport, touring)
Override: display_info()

# Exercise 2: Polymorphism
Create a function that accepts a list of vehicle objects and call their display_info() 
method to print details of each vehicle
    """
    
# Exercise 1: Create a simple application to manage different types of vehicles.

# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


# Derived class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")


# Derived class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_of_bike}")


# Exercise 2: Polymorphism
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # empty line for readability


# Create instances of vehicles
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Softail", 2019, "Cruiser")

# Create a list of vehicles
vehicles = [car, motorcycle]

# Call the display_vehicle_info function
display_vehicle_info(vehicles)

# Reading and writing files in python

"""_summary_
Working with text files
Handling CSV files
JSON and XML file processing
    """
    
# Reading and writing text files and close
# Note: Python provides inbuilt functions to handle text files.
# key concepts
"""_summary_
Opening File: open() function (r, w, a, r+)
Reading file: read() function
Writing file: write() function
Close file: close() function
    """
# Example 3: write a file and read a file 

# Writing to a text file
with open('sample.txt', 'w') as file:
    file.write('Learning python is easier compared to Java.\n')
    file .write('Python has less syntax')
    
# Reading from a text file
with open('sample.txt', 'r') as file:
    okay = file.read()
    print(okay)
    
# Handling CSV files
# CSV stands for Comma Separated Values. It is a common file format used to store tab
# lar data, such as spreadsheets or tables. Python provides a module called csv 
# to handle CSV files.
"""_summary_
CSV ( Comma Separated Values) file widely for data exchange.
keeps Data integrity
Key concepts
Reading CSV files: Using 'csv.reader()'
Writing CSV files: Using 'csv.writer'
DictReader and DictWriter: The class read and write  CSV files as dictionaries

    """
# Example 4: Writing and Reading CSV files

import csv

# Writing to a CSV files

with open ('otim.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position', 'course'])
    writer.writerow(['Otim Ronald', 'Student', 'BSSE'])
    
# Read from a CSV file
with open('otim.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
        
# JSON and XML file processing
"""
JSON (Javascript Object Notation) and XML (extensible Markup Language) are formats used to
structure data.

Key Concepts
Loading JSON Data: using json.load() for reading JSON file
Dumping JSON Data: using json.dump() for writing JSON file
Parsing JSON Data: using json.loads() for handling JSON strings

"""

# Example 5: write and read JSON file
import json

# Writing to a JSON file
student_data = {
    'name': 'Otim Ronald',
    'course': 'BSSE',
    'year': 'Year Two'
}
# Writing the JSON file
with open('student.json', 'w') as json_file:
    json.dump(student_data, json_file)

# Reading the JSON file
with open('student.json', 'r') as json_file:
    loaded_data = json.load(json_file)
    print(loaded_data)
     
# Exercise 2: Write and read the xml file.

import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("students")

# Create some student elements
student1 = ET.SubElement(root, "student", id="s101")
name1 = ET.SubElement(student1, "name")
name1.text = "John Doe"
major1 = ET.SubElement(student1, "major")
major1.text = "Computer Science"
gpa1 = ET.SubElement(student1, "gpa")
gpa1.text = "3.5"

student2 = ET.SubElement(root, "student", id="s102")
name2 = ET.SubElement(student2, "name")
name2.text = "Jane Smith"
major2 = ET.SubElement(student2, "major")
major2.text = "Engineering"
gpa2 = ET.SubElement(student2, "gpa")
gpa2.text = "3.8"

student3 = ET.SubElement(root, "student", id="s103")
name3 = ET.SubElement(student3, "name")
name3.text = "Bob Johnson"
major3 = ET.SubElement(student3, "major")
major3.text = "Business"
gpa3 = ET.SubElement(student3, "gpa")
gpa3.text = "3.2"

# Create a tree and write to a file
tree = ET.ElementTree(root)
tree.write("students.xml")

print("Student data XML file written successfully!")

# Parse the XML file
tree = ET.parse("students.xml")
root = tree.getroot()

print("Student data XML file read successfully!")

# Iterate over the students
for student in root:
    print("Student ID:", student.get("id"))
    print("Name:", student.find("name").text)
    print("Major:", student.find("major").text)
    print("GPA:", student.find("gpa").text)
    print("---")
    

# Exercise 3: Using abstraction calculate the area and perimeter of a rectangle

from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete class
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create a rectangle object
rect = Rectangle(5, 3)

# Calculate and print the area and perimeter
print("Area: ", rect.area())
print("Perimeter: ", rect.perimeter())