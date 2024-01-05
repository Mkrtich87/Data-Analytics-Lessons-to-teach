#lesson 7
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
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\William.txt",
    mode="r",
) as poem:
    # first_line = poem.readline()
    # print(first_line, '\n')
    print(poem.readlines())
# mode=r : read 'w': write 'a' append 'wb' binary mode, 'x': exclusive mode-opens the file for writing but only if
# the file doesn't already exist
# using while loop to read each next line
with open(
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\William.txt",
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
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\William.txt",
    mode="r",
) as poem:
    poem = poem.read(41)
    print(poem)
# writing to a file
# Open function to open the file "MyFile1.txt"
# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
with open(
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\mythoughts.txt",
    mode="w",
) as my_thoughts:
    my_thoughts.write("I need to gather firewood for winter, Civis Romanus sum")
# next time to change the text we use append mode mode = 'a'
with open(
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\mythoughts.txt",
    mode="a",
) as my_thoughts:
    my_thoughts.write("I need to gather firewood for winter, \n Civis Romanus sum")
# error in the code below, doesn't read back the file check it
# next time read and write and to change the text we use append mode mode = 'w+'
with open(
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\mythoughts.txt",
    mode="w+",
) as my_thoughts:
    my_thoughts.write(
        "I need to gather firewood for winter, \n Civis Romanus sum, n\ audere est facere"
    )
    my_written_thoughts = my_thoughts.readlines()
    print(my_written_thoughts)
# opening csv file
with open(
    r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\msft.csv",
    mode="r",
) as micrsoft:
    microsoft_stock = micrsoft.read()
    print(microsoft_stock)
#using csv module
import csv
#csv.reader arguments csvfile represents csv file i want to read,
#delimiter is used to identify the character you that separates fields
#quotechar is an optional argument that specifies the character used to enclose fields that contain special character
with open(r"C:\Users\mkrti\OneDrive\Документы\Python projects\ACA python\msft.csv", newline="") as csvfile:
    msftreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in msftreader:
        print(", ".join(row))
#numpy module
import numpy as np
# Create a 1D NumPy array filled with zeros, with a length of 3
a = np.zeros(3)
# Check the type of the variable 'a' (it should be a NumPy array)
type(a)
# Create another 1D NumPy array filled with zeros, with a length of 10
z = np.zeros(10)
z
# Display the contents of the 'z' array
# Check the shape (dimensions) of the 'z' array
z.shape
# Display the shape of the 'z' array
# Reshape the 'z' array into a 5x2 matrix
z.shape = (5, 2)
z
# Display the reshaped 'z' array
# Create a 1D NumPy array with 10 evenly spaced values between 2 and 5
y = np.linspace(2, 5, 10)
y
# Display the contents of the 'y' array
# Create a Python list
a_list = [1, 2, 3, 4, 5, 6, 7]
# Convert the Python list into a NumPy array
z = np.array([a_list])
z
# Display the contents of the 'z' array
# Create a nested Python list
b_list = [[9, 8, 7, 5, 6], [1, 2, 3, 8, 5]]
# Convert the nested Python list into a NumPy array
z = np.array([b_list])
z
# Display the contents of the 'z' array
# Check the type of the variable 'z' (it should be a NumPy array)
type(z)
# Display the type of the 'z' variable
# Set a random seed for reproducibility
np.random.seed(0)
# Generate a 1D NumPy array with 6 random integers between 0 and 9
zl = np.random.randint(10, size=6)
zl
# Display the contents of the 'zl' array
# Import the 'io' module from scikit-image
from skimage import io
# Read an image file named 'Dodge.jpg' and store it in the 'photo' variable
photo = io.imread('Dodge.jpg')
# Check the type of the 'photo' variable (it should be a NumPy array)
type(photo)
# Display the type of the 'photo' variable
# Check the shape (dimensions) of the 'photo' array, representing the image
photo.shape
# Display the shape of the 'photo' array
# Import the 'pyplot' module from Matplotlib
import matplotlib.pyplot as plt
# Display the image stored in the 'photo' array
plt.imshow(photo)
# Display the image using Matplotlib
# Display the image with rows reversed (vertical flip)
plt.imshow(photo[::-1])
# Display a cropped region of the image (rows 500 to 1099, columns 150 to 639)
plt.imshow(photo[500:1100, 150:640])
# Transform the image using the sine function element-wise
photo_sin = np.sin(photo)
photo_sin
# Display the contents of the 'photo_sin' array
# Perform various calculations on the 'photo' array
print(np.sum(photo))  # Sum of all elements
print(np.prod(photo))  # Product of all elements
print(np.mean(photo))  # Mean (average) of all elements
print(np.std(photo))   # Standard deviation of all elements
print(np.mean(photo))  # Mean (average) of all elements (repeated)
print(np.max(photo))   # Maximum value in the array
# Create a binary mask where values above 200 become 100, otherwise 0
photo_masked = np.where(photo > 200, 100, 0)
plt.imshow(photo_masked)
import numpy as np
# Create an array of sample data
data = np.array([10, 15, 12, 8, 20, 5, 16, 14, 7, 11])
# Calculate the mean (average) of the data
mean_value = np.mean(data)
print("Mean:", mean_value)
# Calculate the median (middle value) of the data
median_value = np.median(data)
print("Median:", median_value)
# Calculate the standard deviation of the data
std_deviation = np.std(data)
print("Standard Deviation:", std_deviation)
#import numpy as np`: This line imports the NumPy library and assigns it the alias `np`.
import numpy as np
#heights_and_ages`: This line creates a new list by concatenating the `heights` and `ages` lists together. So, `heights_and_ages` contains all the height values followed by all the age values.
heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]
ages = [57, 61, 57, 57, 58, 57, 61, 54, 68, 51, 49, 64, 50, 48, 65, 52, 56, 46, 54, 49, 51, 47, 55, 55, 54, 42, 51, 56, 55, 51, 54, 51, 60, 62, 43, 55, 56, 61, 52, 69, 64, 46, 54, 47, 70]
#heights_and_ages`: This line creates a new list by concatenating the `heights` and `ages` lists together. So, `heights_and_ages` contains all the height values followed by all the age values.
heights_and_ages = heights + ages
# Here, we convert the `heights_and_ages` list into a NumPy array using `np.array()`. This allows us to perform array operations on the data.
heights_and_ages_arr = np.array(heights_and_ages)
#This line reshapes the NumPy array `heights_and_ages_arr` into a 9x10 matrix. The `reshape()` function is used to change the shape of the array, and here we
heights_and_ages_arr = heights_and_ages_arr.reshape(9,10)
print(heights_and_ages_arr)
#finally, this line prints an element of the reshaped array. `heights_and_ages_arr[5, 9]` refers to the element in the 6th row and 10th column of the 2D array
print(heights_and_ages_arr[5,9])
#Lesson 64 Simple return
#Obtaining info
#Calculating simple return
#Plotting
#pip install pandas, pandas_datareader
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Read a CSV file named "PG.csv" into a pandas DataFrame
PG = pd.read_csv("PG.csv")
# Display the first 5 rows of the DataFrame
print(PG.head())
# Display the last 5 rows of the DataFrame
print(PG.tail())
# Create a line plot of the data in the DataFrame with a specified figure size
PG.plot(figsize=(16, 6))
# Select the data at the first row of the DataFrame
PG.iloc[0]
# Select the data at the 11th row of the DataFrame
PG.iloc[10]
# Calculate the simple daily returns and add them as a new column
PG["simple_return"] = (PG['Adj Close'] / PG['Adj Close'].shift(1)) - 1
# Display the last 5 rows of the simple returns column
print(PG.simple_return.tail())
# Create a line plot of the simple returns with a specified figure size
PG['simple_return'].plot(figsize=(8, 5))
# Show the plot
plt.show()
# Calculate the average daily return
avg_returns_d = PG['simple_return'].mean()
print(avg_returns_d)
# Calculate the average annual return by multiplying the daily average by 250 (assuming 250 trading days in a year)
avg_returns_a = avg_returns_d * 250
print(avg_returns_a)
# Print the average annual return as a percentage rounded to 5 decimal places
print(str(round(avg_returns_a, 5) * 100) + '%')
# Calculate the maximum closing price in the DataFrame
max_close_price = PG['Adj Close'].max()
print("Maximum Closing Price:", max_close_price)
# Calculate the minimum closing price in the DataFrame
min_close_price = PG['Adj Close'].min()
print("Minimum Closing Price:", min_close_price)
# Calculate the cumulative sum of the 'simple_return' column and add it as a new column
PG['cumulative_return'] = PG['simple_return'].cumsum()
# Display the first 5 rows of the DataFrame with the cumulative return
print(PG.head())
# Calculate the rolling mean (moving average) of the 'Adj Close' column with a window of 30 days
PG['30_day_ma'] = PG['Adj Close'].rolling(window=30).mean()
# Display the first 5 rows of the DataFrame with the rolling mean
print(PG.head())
# Calculate the number of missing values (NaN) in each column of the DataFrame
missing_values = PG.isnull().sum()
print("Missing Values:")
print(missing_values)
# Fill missing values in the DataFrame with a specified value (e.g., 0)
PG.fillna(0, inplace=True)
# Display the first 5 rows of the DataFrame after filling missing values
print(PG.head())
# Create a new DataFrame containing only the 'Date' and 'Adj Close' columns
date_adj_close_df = PG[['Date', 'Adj Close']]
# Display the first 5 rows of the new DataFrame
print(date_adj_close_df.head())
# Sort the DataFrame by the 'Date' column in ascending order
PG_sorted = PG.sort_values(by='Date')
# Display the first 5 rows of the sorted DataFrame
print(PG_sorted.head())