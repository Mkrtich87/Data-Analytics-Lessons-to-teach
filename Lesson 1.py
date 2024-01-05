# Save the file wit ctrl S
print('where is my money')
txt1 = 'mek chakert'
txt2 ="erku chakert text"
txt3 = '''chanparh chanaprh kt
rem ancnem'''
print(txt3)
#for commmenting in one line in python you can use #
'''python does not support multiline commenting but it ignores string literals.
Tha is why you can use those for commenting try quotes or double quotes for three times'''
'''hello
world'''
#python is dynamic language you don't need to declare the type of the variable
#You can use double quotes if you have single quote in the text. Example:
txt4 = "this is Anna's umbrella"
#If you have both ' and "" you can escape ""
txt5 = " flight number is \"LO727\" "
print(txt5)
#toxadards
sum_amount = 1+5+7+\
8+9
print(sum_amount)
name ='Artur'
print(name)
#talk about debugging the code
#ctrl shift p start debugging.
#The code will run until the red dot and after that you can debug with F10
#Arthmetic operators
#exponent **
print(4**2)
#another example
a=5
b =a**2
c=a**3
print(b,c)
# //, % ><, !=
a=15
b=10
print(a/b) # division
print(a//b) #amboxj mas@
print(a%b) #remainder
# == checking the value output should be true or false
a = 4
b = 5
print(a == b)
# != is not equal
a = 20
b = 8
print (a!=b)
# >=
p = 15
q = 15
print(p >= q)
print(p <= q)
#assignment operator
# addition and assignment operator
# +=  I+=J that means I = I + J do the addition and assign to left operand
total = 10
amount = 5
total += amount
print(total)
#subtarction and assignment
# -= I-=J that means I = I – J
balance = 100
withdrawal = 25
balance -= withdrawal
print (balance)
# multiplication and assignment
# I*=J that means I = I * J
quantity = 4
price = 10
total_cost = quantity * price
total_cost *= 2
print(total_cost)
# division and assignment
# I/=J that means I = I / J
total_amount = 100
num_people = 5
amount_per_person = total_amount / num_people
amount_per_person /= 2
print(amount_per_person)
# memory management is active
a=5
b=a
c=7
print('a=', a, 'b=', b, 'c=', c)
# To check if b is referencing a and not using more memory space
print ('a id:', id(a), 'b id:', id(b), 'c id:', id(c))
# we can see both a and b have the same memory address, on contrary the c has different address
print ('a id:', hex(id(a)), 'b id:', hex(id(b)), 'c id:', hex(id(c)))