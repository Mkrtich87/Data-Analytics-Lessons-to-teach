Lesson 4
6:02
# for loop
# for var in iterable:cls
# for: Used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each element
# In this example you can see for loop iterates each word from the list
words = ["hello", "world", "ACA", "is", "awesome"]
for word in words:
    print("The word is:", word)
# iterating the list items
# first iteration returns item_list[0] which is AR15, second iteration returns second
# item in the list etc. until list finishes
item_list = ["AR15", "AK47", "Gatling gun GAU", "M16", "Ruger American"]
for item in item_list:
    print(item)
# running for set. For set iteration is arbiterary as we know set is unordered
# collection of unique items
item_set = {"AR15", "AK47", "Gatling gun GAU", "M16", "Ruger American"}
for item in item_set:
    print(item)
# using for loop with if-else
# printing all the even numbers from the list
numbers = [
    951,
    402,
    984,
    651,
    360,
    69,
    408,
    319,
    601,
    485,
    980,
    507,
    725,
    547,
    544,
    615,
    83,
    165,
    141,
    501,
    263,
    617,
    865,
    575,
    219,
    390,
    984,
    592,
    236,
    105,
    942,
    941,
    386,
    462,
    47,
    418,
    907,
    344,
    236,
    375,
    823,
    566,
    597,
    978,
    328,
    615,
    953,
    345,
    399,
    162,
    758,
    219,
    918,
    237,
    412,
    566,
    826,
    248,
    866,
    950,
    626,
    949,
    687,
    217,
    815,
    67,
    104,
    58,
    512,
    24,
    892,
    894,
    767,
    553,
    81,
    379,
    843,
    831,
    445,
    742,
    717,
    958,
    609,
    842,
    451,
    688,
    753,
    854,
    685,
    93,
    857,
    440,
    380,
    126,
    721,
    328,
    753,
    470,
    743,
    527,
]
# your code goes here
for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        pass
# range()function
# Range function has three areguments but can work with min one. range(start, stop, step)
# The range() function returns a sequence of numbers, starting from 0 by default,
#  and increments by 1 (by default), and stops before a specified number.
for i in range(5):
    print(i)
# we can also iterate the number of the list objects
for i in range(len(item_list)):
    print(i)
# getting out of the list.
# continue statement is used in loops to skip the code inside the current iteration
# and move to the next iteration in the loop. In our case it skips printing odd numbers
# which do not satisfy i%2!=0:
# use debugger to show how continue throws the code up after any odd number not allowing to print
for i in range(1, 101):
    if i % 2 != 0:
        continue
    print("even numbers:", i)
# break. exits the code before the break point
# In the list below if break is on Amur, the code will exit on Congo
rivers = [
    "Nile",
    "Amazon",
    "Yangtze",
    "Mississippi",
    "Yenisei",
    "Yellow",
    "Ob",
    "Parana",
    "Congo",
    "Amur",
    "Lena",
    "Mekong",
    "Mackenzie",
    "Niger",
    "Murray-Darling",
    "Volga",
    "Indus",
    "Ganges",
    "Danube",
    "Orinoco",
    "Rio Grande",
    "Tocantins",
    "Columbia",
    "St. Lawrence",
    "Tigris",
    "Euphrates",
    "Río de la Plata",
    "Brahmaputra",
    "Colorado",
    "Zambezi",
    "Don",
    "Rhine",
    "Senegal",
    "Jordan",
    "Tagus",
    "Loire",
    "Molopo",
    "Garonne",
    "Seine",
    "Thames",
]
for name in rivers:
    if name == "Amur":
        break
    print(name)
# break is very useful for while loops as we may not have any end point
# Using on dictionaries
greek_philosophers = {
    "Socrates": [
        "None written by him, but his ideas were recorded by Plato and Xenophon"
    ],
    "Plato": ["The Republic", "Phaedrus", "Symposium"],
    "Aristotle": ["Nicomachean Ethics", "Politics", "Metaphysics"],
    "Heraclitus": ["None survived, fragments of his ideas exist"],
    "Pythagoras": ["None survived, ideas attributed through later sources"],
    "Epicurus": ["Letter to Menoeceus", "Principal Doctrines"],
    "Zeno of Citium": ["None survived, ideas recorded by later Stoic philosophers"],
    "Diogenes of Sinope": ["None survived, anecdotes and sayings collected by others"],
    "Empedocles": ["None survived in full, fragments exist"],
    "Anaxagoras": ["On Nature"],
    "Thales": ["None survived, ideas attributed through later sources"],
    "Democritus": ["On the Atom", "Ethics"],
    "Protagoras": ["None survived in full, fragments exist"],
    "Xenophanes": ["None survived in full, fragments of poetry remain"],
    "Parmenides": ["On Nature"],
    "Anaximander": ["None survived, ideas attributed through later sources"],
    "Heraclides Ponticus": ["On the Apparent Motion of the Heavenly Bodies"],
    "Plotinus": ["Enneads"],
    "Cleanthes": ["Hymn to Zeus"],
    "Chrysippus": ["None survived in full, fragments of writings remain"],
}
# this will only print keys
for i in greek_philosophers:
    print(i)
# that is why we use items method:
#The items() method doesn't take any parameters.
# returns key: value tuples
for i in greek_philosophers.items():
    print(i)
# In this case we unpack explicitely i as key and k as value
# this returns separate lists of keys and values
"""The items() method returns a view object that
 displays a list of dictionary's (key, value) tuple pairs."""
for i, k in greek_philosophers.items():
    print("philosopher:", i, "book:", k)
# only values unpacking
for i, k in greek_philosophers.items():
    print("book:", k)
# or use values method
for k in greek_philosophers.values():
    print("book:", k)
# nested loop
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
# create a multiplication table for each natural number
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}") #creates multiplication table
number = int(input("Enter a natural number: "))# after we see table we can input
print_multiplication_table(number)
# while loops
# while condition is true the code will run
# below code will run forever if not break
count = 0
while count < 10:
    print("Countis:", count)
    break
# let's modify it wit +=   i=i+1 = i+=1
# will receive 0,1,2,3,..
while count < 10:
    print("Countis:", count)
    count += 1
# in this case will start from 1 : 1,2,3,4..
num = 0
while num < 15:
    num += 1
    print("Countis:", num)