#Lesson 2 Python
#data types
# to find out datatype use method type
nm = "My name is what, my name is who"
print(type(nm))
num = 25
print(type(num))
print('')
print(type(num))
# forcing print function to print on the next line
nm = 'my name \n is Qerop'
print(nm)
# changing print function enter parameter in the end. by default it ignores lines witin code.
#there will be no gap between this and next output
print("this is test")
#after this we will have separation within lines. In output there will be gap
print("this is test", end ='\n \n')
print("this is test")
#this will separate to variables within print function and show below each other
print("this is test", 'this is another test', sep ='\n', end ='\n \n')
# string data type is immutable
sometext = 'this is test'
# index     012345...
#           ..........-1
first_letter = sometext[0]
print(first_letter)
rest_value = sometext[1:]
print(rest_value)
# testing if it is immutable
#sometext[0] = 'z' this will return error:
#'str' object does not support item assignment as string is unmutable
print(sometext[2:4])
# adding step to calling
# in this case step is two
print(sometext[0::2])
# in this case step is 9
print(sometext[0::9])
# finally first parameter when calling string parts is index, second parameter is is position,
#third parameter is the step. sometext = 'this is test'
print(sometext[11::-2])
#Trying to concat different data types
txt1 = 'Leopold'
txt2 = 25
txt3 = 'engineer'
# we can cast integer to  string. For example
person1 = str(txt1)+str(txt2)+str(txt3)
print(person1)
# or use formatted string
person1 = f'{txt1} {txt2} {txt3}'
print(person1)
#another tyoe of formatting with the same result
person1 = f'Name:{txt1}, Age:{txt2}, Specialty:{txt3}'
print(person1)
#another tyoe of formatting with the same result
person1 = f'Name:{txt1}, Age:{txt2}, Specialty:{txt3}'
print(person1)
person1 = 'Name:{}, Age:{}, Specialty:{}'.format(txt1,txt2,txt3)
print(person1)
person1 = 'Name:{0}, Age:{1}, Specialty:{2} loves nature'.format(txt1,txt2,txt3)
print(person1)
#if we want to make changes in the text we can change age from integer to float
person1 = 'Name:{0}, Age:{1:.2f}, Specialty:{2} loves nature'.format(txt1,txt2,txt3)
print(person1)
#we can check other functions we can implement on string with the help of adding dot to string name
#person1
print(person1.count(txt1))
# finding length
print(len(person1))
#printing second half of the string
print(person1[len(person1)//2:])
# finding something int the text. In this case it finds the index of txt3
print(person1.find(txt3))
#List defintnion lst = []
#list is mutable
list1 = [1,2,3,4,5,6, 'Lernik', 'Ando']
print(list1[7])
#changing list member
list1[2] = 25000
print(list1)
#printing one of the members of list1 using index
print(list1[2:5])
print(list[5:])
#length of the list1
print(len(list1))
list2 = ['Qerob', 'Rubo']
#adding list2 as one combined member of list
list1.append(list2)
print(list1)
# making list2 members separate members of list. For this we use extend function
list1.extend(list2)
print(list1)
# Insert method to add on the desired position
#Python List insert()
# insert an element to the list
list1.insert(1,'Vasya')
print(list1)
list3 =list1
# copying list1 to another list
# the ouptut of the command below shows that if we change list, list3 will be changed too
#as it is a mere pointer
print(id(list3), id(list1))
'''Python List index()
returns the index of the element in the list
Python List reverse()
reverses the list
t'''
#let's delete something from list and print list3
# checking the list3
print(list3)
#deleting the last element of list
#Python List pop()
#Removes element at the given index
list1.pop()
#checking if it has affected list3
print(list3)
#to avoid this we can use copy method
list3 = list1.copy()
print(id(list3), id(list1))
# Also pop can help to take last member as a variable
print(list3)
name = list3.pop()
print(name)
#also with pop() we can use remove. For example
#Python List remove()
#Removes item from the list
print(list1)
list1.remove(5)
print(list1)
#list of lists and
# calling object from the inside of second list
list7 = ['Amazon', 'Apple', 'Google']
list8 = [6, 7, 9, 10 , 12]
list7.append(list8)
print(list7)
print(list7[3][-3])
#operations with list additiom subtraction multiplication
#doubles the list members
doublelist = list8 * 2
print(doublelist)
# changing list member: list first object multiplied by two
doublelist = list8[0] * 2
print(doublelist)
#adding separate list objects to each other
list9 = [10, 9, 8, 7, 6]
x = list8[3] + list9[0]
#tuple is a sequence data type
# tpl = ()
tpl = (1,2,3,4)
set = {1,2,3,4}
print(type(tpl), type(set))
#adding member to tuple
# we need to change type
#changing to list
tpl1 = (10,)
print(type(tpl1))
#ist_n = list(tpl1)
#Python List sort()
#sorts elements of a lis
#sorting method of prime numbers
prime_numbers = [4,5,2,6,1,3,2,1,4,5,6,9]
prime_numbers.sort()
print(prime_numbers)
# reversing prime numbers
prime_numbers.reverse()
print(prime_numbers)
#Python List reverse()
#reverses the list
"""print(type(list_1))
#adding 15 to list
list_1.append(15)
#changing back to tuple
tpl = tuple(list_1)
print(tpl)
print(type(tpl))"""