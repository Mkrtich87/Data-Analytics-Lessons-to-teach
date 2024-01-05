#Show the picture of scheduler created by your colleague for Alation automatic reporting
#Lesson 6
#try except
'''try:
    # code that may cause exception
except:
    # code to run when exception occurs'''
#checking 0 division error
# working of try()
def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")
# Look at parameters and note the working of Program
divide(7, 2)
divide(3,0)
#same with the input
#Handling specific exception
try:
    value = int(input("Enter a number or 'q' to quit: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
#Handling multiple exceptions
try:
    value = int(input("Enter a number or 'q' to quit: "))
    result = 10 / value
except ValueError:
    print("Invalid input. Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero")
#Using else block
9:17
try:
    num = int(input("Enter a positive number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    if num <= 0:
        print("Number must be positive.")
    else:
        print("Number squared:", num ** 2)
##Using finally block
#In Python, the finally block is always executed no matter whether there is an exception or not.
#The finally block is optional. And, for each try block, there can be only one finally block.
try:
    file = open("myfile.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    file.close
#Our old example modified with try except
def username_input():
    username = input("Please enter your username")
    try:
        username_as_int = int(username)
        print("wrong input: input should be a string")
    except ValueError:
        print("good morning", username)
        print("How are you!")
username_input()
#recursive function
'''Every recursive function must have a base
condition that stops the recursion or else the function calls itself infinitely.'''
#By default, the maximum depth of recursion is 1000.
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 7
print("The factorial of", num, "is", factorial(num))
#lambda
#Syntax: lambda arguments : expression
add = lambda x, y: x + y
result = add(5, 3)  # Result will be 8
print(result)
square = lambda x: x ** 2
result = square(4)  # Result will be 16
print(result)
#Sort a List of Dictionaries by a Specific Key
students = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 30}
]
sorted_students = sorted(students, key=lambda x: x["age"])
# sorted_students will be [{'name': 'Bob', 'age': 22}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]
words = ["radar", "hello", "level", "world", "deified", "python"]
# Define a lambda function to check if a word is a palindrome
is_palindrome = lambda word: word == word[::-1]
# Use the filter function to filter out palindromes from the list of words
palindromes = list(filter(is_palindrome, words))
print(palindromes)
#decorators
# A Python decorator is a function
#that takes in a function and returns it by adding some functionality.
#Basically, a decorator takes in a function, adds some functionality and returns it.
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper
@log_args
def add(a, b):
    return a + b
add(2, 3)
'''In Python, we can pass a variable number of arguments
 to a function using special symbols. There are two special symbols:
*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)
We use *args and **kwargs as an argument when we
 are unsure about the number of arguments to pass in the functions'''
#mutiplying function with undefined number of arguments
def multiplier(*num):
    product = 1  # Initialize the product to 1
    for n in num:
        product *= n  # Multiply instead of adding
    print("Numbers:", num)
    print("Product:", product)
multiplier(3, 5)
multiplier(4, 5, 6, 7)
multiplier(1, 2, 3, 5, 6)
def concatenate_strings(*args):
    result = ""
    for string in args:
        result += string
    return result
concatenated = concatenate_strings("Hello, ", "World", "!")
print(concatenated)  # Output: Hello, World!
12:46
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York
#Python callable()
'''In Python, a callable is any object that you can call using a pair of parentheses and,
 optionally, a series of arguments.
Functions, classes, and methods are all common examples of callables in Python.'''
# string objects uncallable
unknown = "Hello darkness my old friend"
print(callable(unknown))
#functions are callabale
import  math
def new_function(a):
  return  math.factorial(a)
print(callable(new_function))
print(new_function(5))
#lists are not callable
aircraftlist = ['Ebraer', 'Bombardier', 'Boeing', 'Airbus' 'Cessna']
print(callable(aircraftlist))
# my functions is callable
# This will print True because the function is callable
def my_function():
    print("Hello, world!")
callable_result = callable(my_function)
print(callable_result)
#len
print(len(unknown))
# sorted()
list_12 = [5, 3, 100,  25, 4, 15, 4, 8, 10]
print(sorted(list_12))
#lambda
#lambda is a small anonimous function ( has no name)
# we have to assign lambda functions to be able to reference those later
anotherstring = 'THIS IS ALL IN CAPITAL'
lower = lambda string: anotherstring.lower()
print(lower)
# python modules ( lirbary is a collection of modules)
# Python DateTime – DateTime Class
import datetime
import calendar
import pytz
# if import is done on datetime level you have to do access datetime before accessing date
# this only provides date information
todays_date = datetime.date.today()
print(todays_date)
# using datetime methods. This also add info about time
print(datetime.datetime.today())
# this method is almost the same with the above one, but it allows to pass
# timezone argument
print(datetime.datetime.now())
# using datetime methods
tokyo_tz =pytz.timezone('Asia/Tokyo')
print(datetime.datetime.now(tokyo_tz))
# you can also import part of the module
# from datetime import date. This allows to access date class directly
from datetime import date
Todays_date = date.today()
print(Todays_date)
print(type(Todays_date))
# isocalendar method outputs following info. datetime.IsoCalendarDate(year=2000, week=5, weekday=7)
#shows which week and weekday of the year is the date provided
mydate = datetime.date(2000, 2, 6)
print(datetime.date.isocalendar(mydate))
print(Todays_date.isocalendar())
# datetime.datetime(year, month, day):
# Creates a custom datetime object  and assigns to the numbers we have provided
custom_datetime = datetime.datetime(2023, 8, 22, 15, 30)
print("Custom Datetime:", custom_datetime)
# Format a datetime object as a string
formatted_datetime = custom_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Datetime:", formatted_datetime)
# Parse a string into a datetime object
#parsing is the process of converting a string representation of data in to
#its corresponding data type
parsed_datetime = datetime.datetime.strptime("2023-08-22 15:30:00", "%Y-%m-%d %H:%M:%S")
print("Parsed Datetime:", parsed_datetime)
'''Following code will allow to create a one month datetime
 list when you need to assign date to some transactions'''
# Parse the input string to create a datetime object
input_string = "2023-08-22 15:30:00"
parsed_datetime = datetime.datetime.strptime(input_string, "%Y-%m-%d %H:%M:%S")
# Extract year and month from the parsed datetime
year = parsed_datetime.year
month = parsed_datetime.month
# Calculate the number of days in the month
num_days = (datetime.date(year, month + 1, 1) - datetime.date(year, month, 1)).days
# Create a list of datetime objects for each day in the month
daily_datetimes = [datetime.datetime(year, month, day, parsed_datetime.hour, parsed_datetime.minute, parsed_datetime.second)
                   for day in range(1, num_days + 1)]
# Print the list of daily datetime objects
for dt in daily_datetimes:
    print(dt)
# Access components of a datetime object
print("Year:", custom_datetime.year)
print("Month:", custom_datetime.month)
print("Day:", custom_datetime.day)
print("Hour:", custom_datetime.hour)
print("Minute:", custom_datetime.minute)
print("Second:", custom_datetime.second)
# Get date and time components separately
date_part = custom_datetime.date()
time_part = custom_datetime.time()
print("Date:", date_part)
print("Time:", time_part)
# Calculate time differences
# create time difference object and add it to our custom_datetime
time_diff = datetime.timedelta(hours=2, minutes=30)
new_datetime = custom_datetime + time_diff
print("New Datetime:", new_datetime)
# another example
time_diff1 = datetime.timedelta(hours=5, minutes=30)
now = datetime.datetime.now()
new_datetime1 = now - time_diff1
print(new_datetime1)
# Create a date object
custom_date = datetime.date(2023, 8, 22)
print("Custom Date:", custom_date)
# Get current date
today_date = datetime.date.today()
print("Today's Date:", today_date)
# Format a date in ISO format
iso_date = custom_date.isoformat()
print("ISO Formatted Date:", iso_date)
# Opening files on your machine
# readlines() and readline()
# readline prints only the first line
# With statement helps to handle execptions in reading writing files and handling file streams
# it will help us to properly close whatever we open (it may not in case of writing)
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\William.txt",
    mode="r",
) as poem:
    # first_line = poem.readline()
    # print(first_line, '\n')
    print(poem.readlines())
# mode=r : read 'w': write 'a' append 'wb' binary mode, 'x': exclusive mode-opens the file for writing but only if
# the file doesn't already exist
# using while loop to read each next line
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\William.txt",
    mode="r",
) as poem:
    while True:
        first_line = poem.readline()
        if first_line == "":
            break
        else:
            print(first_line, "\n")
# readin custom number of symbols
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\William.txt",
    mode="r",
) as poem:
    poem = poem.read(41)
    print(poem)
# writing to a file
# Open function to open the file "MyFile1.txt"
# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\mythoughts.txt",
    mode="w",
) as my_thoughts:
    my_thoughts.write("I need to gather firewood for winter, Civis Romanus sum")
# next time to change the text we use append mode mode = 'a'
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\mythoughts.txt",
    mode="a",
) as my_thoughts:
    my_thoughts.write("I need to gather firewood for winter, \n Civis Romanus sum")
# next time to change the text we use append mode mode = 'a'
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\mythoughts.txt",
    mode="a",
) as my_thoughts:
    my_thoughts.write("I need to gather firewood for winter, \n Civis Romanus sum")
# error in the code below, doesn't read back the file check it
# next time read and write and to change the text we use append mode mode = 'w+'
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\mythoughts.txt",
    mode="w+",
) as my_thoughts:
    my_thoughts.write(
        "I need to gather firewood for winter, \n Civis Romanus sum, n\ audere est facere"
    )
    my_written_thoughts = my_thoughts.readlines()
    print(my_written_thoughts)
# opening csv file
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\msft.csv",
    mode="r",
) as micrsoft:
    microsoft_stock = micrsoft.read()
    print(microsoft_stock)
#using csv module
import csv
#csv.reader arguments csvfile represents csv file i want to read,
#delimiter is used to identify the character you that separates fields
#quotechar is an optional argument that specifies the character used to enclose fields that contain special character
with open("msft.csv", newline="") as csvfile:
    msftreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in msftreader:
        print(", ".join(row))
import pandas as pd
# Read the CSV file into a pandas DataFrame object
df = pd.read_csv("node.csv")
# Get the number of rows in the DataFrame, which is equal to the number of lines in the CSV file
num_lines = df.shape[0]
# Print the number of lines in the CSV file
print("Number of lines in the CSV file: ", num_lines)
# opening json file
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\example_2.json",
    mode="r",
) as example:
    json_example = example.read()
    print(json_example)
with open(
    r"C:\Users\murumya\OneDrive - BMO Financial Group\Desktop\ACA\Python\example_2.json",
    mode="r",
) as example:
    print(json_example.readlines())
    import json
#decorators
#Pandas, numpy
#oop