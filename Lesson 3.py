#Lists can contain any type of data for example
random_list = [1, 23.5,'true', 9, [5 ,4 ,3 ,2 , 1] ]
print (random_list[4])
#lists are changeable
random_list.extend('Zangezur')
random_list.append('Zangezur')
print(random_list)
#set you can see it returns only one of 25 s as it keeps only one of the duplicates.
#also it has no order
#two ways to define sets
st =set()
# or
st1 ={25, 25, 34, 47, 62}
print(st, st1)
#getting rid of duplicates with the help of set
lst1 = [32,45,76,76,32, 12, 34, 55, 89]
set1 =set(lst1)
print(set1)
# set is quicker than listbecause has less methods. A method is a function that “belongs to” an object.
#Set methods: .add
# new member is added to random position
set1.add(24000)
print(set1)
#copy method
set2 = set1.copy()
print(set2)
#difference method
set3 =set1.difference(set2)
print(set3)
#Another example of set difference method
stx = {'apple', 'banana', 'orange', 'blackberry'}
sty = {'apple', 'banana', 'orange'}
#just prints the difference
print(stx.difference(sty))
#Assiging new set to be the difference
stz = stx.difference(sty)
print(stz)
#changes the stx permanently with the difference
stx.difference_update(sty)
print(stx)
#deleting stx with del command. Uncomment the next line
#del stx
print(stx)
#intersection method
x = {'apple', 'banana', 'orange', 'blackberry'}
y = {'apple', 'banana', 'orange'}
print(x.intersection(y))
#dicitionary is mapping data type
#Declareing dictionary
#empty dictionary
dict = {}
print(type(dict))
#dictionary with key:value
dict_1 = {'Armenia': 'Yerevan', 'Russia': 'Moscow', 'USA': 'Washington', 'France': 'Paris', 'Columbia': 'Bogota'}
dict_2 = {'Name': 'Qerob', 'LastName': 'Aslanyan', 'age': 25, 'Gender': 'Male', 'birthdate': '1981-05-06'}
#key cannot be changed, value can be changed
#dictionary methods: get
#get method takes to arguments: key and default value if key is non existent
#get method is used to avoid exceptions
print(dict_1.get('USA'))
print(dict_2.get('Gender'), dict_2.get('Name') )
#checking second value if key is not existent
print(dict_1.get('Kongo', "There is no such country"))
print(dict_2.get('Armenia'), dict_2.get('Name'))
#if get function refers to wrong key python returns none
print(dict_2.get('Name'), dict_1.get('Armenia') )
#if using square brackets error. Uncomment next command
#print(dict_2.get('Gendername'), dict_2['age0'] )
#nested dictionaries
dict_1 = {'Armenia': {'Yerevan', 'Vanadzor', 'Gyumri', 'Kapan', 'Hadrut'}, 'Russia': 'Moscow', 'USA': 'Washington', 'France': 'Paris', 'Columbia': 'Bogota'}
#calling with square brackets
print(dict_1['Armenia'])
#calling nested dictionary with get method
print(dict_1.get('Armenia'))
#modifing nested dictionary with the key and calling it. Creating Json
#you can go several levels
dict_1 = {'Armenia': {'Captial': 'Yerevan',
                      'Second city': 'Vanadzor',
                       'Third City': 'Gyumri',
                        'population':'3.5'},
                        'Russia': 'Moscow', 'USA': 'Washington', 'France': 'Paris', 'Columbia': 'Bogota'}
print(dict_1.get('Armenia')['Third City'])
print(dict_1['Armenia']['Third City'])
# items method turns key: value pairs in to tuples and returns them as a list
#good for iterating through both key and value
print(dict_1.items())
print(dict_2.items())
# values method
print(dict_2.values())
#pop method. lLt's delete birthdate
print(dict_2)
dict_2.pop('birthdate')
print(dict_2)
#key cannot be list
#using integer keys
integer_dict = {1: 'Armen', 2: 'Arsen', 3: 'Valod'}
print(integer_dict[1])
#updating dict
#Update method. Adding object to dictionary
integer_dict.update({4: 'Grenik'})
print(integer_dict)
#update method. Changing existing dicitionary members
integer_dict.update({1: 'Vazgen', 2: 'Levon'})
#another way to update the dicitionary is with square brackets
print(dict_2)
dict_2['LastName'] = 'Urumyan'
print(dict_2)
#Flow
#If statement
#if: Used to execute a block of code only if a certain condit
a = (1,2,3,4)
b = (5,6,7,8)
if b > a:
    print('this is excpected')
if b < a:
    print('this is excpected')
#checking if the number is even or odd with the help of if statement
t = 4
f = 5
if t % 2==0:
    print('even')
pass
if f % 2==0:
    print('even')
pass
#if-else
if b < a:
    print('this is excpected')
else:
    print('this is not expected')
#expanding our even odd example with else
if t % 2==0:
    print('even')
else:
    print('odd')
if f % 2==0:
    print('even')
else:
    print('odd')
#if-elif-else example
#expanding our case considering 0
a = 0
if a == 0:
    print('number is zero')
elif a%2!=0:
    print('odd')
else:
    print('even')
#other if-elif example where we are checking if number is positive, negative or zero
x = 10
if x > 0:
    print('x is positive')
elif x == 0:
    print('x is zero')
else:
    print('x is negative')
#small app with if-elif-else
#create a program that determines category of given age
# first learn how to use user input
z = input('input number')
print(type(z))
z = int(input('input number'))
print(type(z))
#create a program that determines category of given age
age = int(input('input your age: '))
if age < 0:
    print("age can't be negative!")
elif age < 18:
    print('you are minor')
elif 18 < age < 65:
    print('you are an adult')
else:
    print('you are a senior citizen')