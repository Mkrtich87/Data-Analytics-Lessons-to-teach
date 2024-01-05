lesson 5
# instead of while n<m we can use While True which can run forever
step = 0
while True:
    step += 1
    print("step", step)
    if step == 20:
        break
# skip the beginning of the count
r = 0
while True:
    r += 1
    if r < 10:
        continue
    print("the number is:", r)
    if r == 25:
        break
print('')
# skip the middle of the  count
r = 0
while True:
    r += 1
    if r > 11 and r < 20:
        continue
    print("the number is:", r)
    if r == 25:
        break
# sentinel while number example
#this is a calculator that keeps adding number until sentinel number is provided
total = 0  # Initialize the total variable
sentinel = -1  # Define the sentinel value
print("Enter numbers to calculate their sum.")
print("Enter", sentinel, "to finish.")
user_input = float(input("Enter a number: "))
while user_input != sentinel:  # Condition: Continue loop until sentinel is entered
    total += user_input
    user_input = float(input("Enter a number: "))
print("The sum of the entered numbers is:", total)
exit
#User defined functions
# return is used to provide a result that can be used by the rest of the code
def add_numbers(a, b):
    return a + b
print(add_numbers(20,15))
# cube function
def cube(x):
   r=x**3
   return r
print(cube(10))
# default value when argument is not mentioned
def power(base, exponent=2):
    return base ** exponent
print(power(3))       # This will print 9 (3 raised to the power of 2) because 2 is the default value
print(power(2, 4))    # This will print 16 (2 raised to the power of 4)
#function checking the argument
#isintstance() is used to check if of specified type: returns true or fals
def username_input():
   username =input ("Please enter your username")
   if isinstance(username, str):
        print("good morning", username)
        print("How are you!")
   else:
        print("wrong input")
username_input()
#Function returning another function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  # This will print 10 (5 multiplied by 2)
print(triple(5))  # This will print 15 (5 multiplied by 3)
#python built in functions
#square root sqrt()
import math
x = 625
square_root = math.sqrt(128)
print(math.sqrt(x))
# function definition
def get_square(num):
    return num * num
for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)
#Lesson 6
#Python callable()
'''n Python, a callable is any object that you can call using a pair of parentheses and,
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
#recursive
#decorators
#try except
#Pandas, numpy
#oop