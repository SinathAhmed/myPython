print("hello world")

# first program done- commented out

""" multiline
comment it is"""

"""a = 5
b = "ciao"
d = complex(8, 2)
e = 5 ** 3  #power 5*5*5
f = 14//4  #floor divide
print("d is", d)
print("e is", e)
print("f is", f)"""

# typeCast
"""x = 5.86785
y = 4.001
print(x)  # x will be printed 
print(int(x))  # x has become integer
sttr = str(y)  # y has become string
print(sttr)  # y will be printed as string
print(int(y))"""

# input from user
"""c = input("enter something: ")
print(c)
name = input("what is your name: ")
print(f"my name is {name}")"""

# format specifier
"""price1 = 55.67
price2 = -3454.5678
price3 = 346.1415
print(f"price1 is {price1:.2f}")  # 2 decimal places
print(f"price2 is {price2:020}")  # 20 ta space niye print korbe, 0 diye fillup hobe samner gula
print(f"price3 is {price3:010}")  # 10 ta space niye print korbe, 0 diye fillup hobe samner gula
print(f"price1 is {price1:<6}")  # left aligned
print(f"price2 is {price2:>9}")  # right aligned
print(f"price3 is {price3:^5}")  # center aligned
print(f"price2 is {price2:,}")  # comma separated"""

# String
"""new = ''' hello 
I am a student'''
new1 = 'ciao'
print(new)
print(new[8])
for character in new1:
    print(character)"""

# string slicing
"""fruit = "mango"
print("lenth of mango is", len(fruit))
print(fruit[0:2])  # including 0 but not 2
print(fruit[1:4])  # including 1 but not 4
print(fruit[:5])  # auto putting zero before (:)
print(fruit[0:-3])  # len(fruit)= 5... 5-3=2...so answer will be[0:2]
print(fruit[:len(fruit)-3])  # same as line 39
print(fruit[-1:- 3])  # 4:2(not applicable)
print(fruit[::-1])  #reversed the string
nm = "sinath"
print(nm[::3])  #prints every 3 characters
print(nm[-4:-2])
print(nm[-3:])
number = "1234-4567-7890"
print(number[:7:2])
print(number[4::2])"""

#  string methods
"""i = "SinAth Ahmed Fahad"
print(i.lower())  # lowercase full string
print(i.upper())  # uppercase full string
print(i.rstrip("!"))
print(i.replace("sInAth", "ahmed fahad"))  # replace a string with another one
print(i.split(" "))  # makes a string to list
print(i.capitalize())  # first alphabet capital & rest are small
print(i.center(60))  # centers a string
print(i.count("a"))  # counts how many of given strings are there
print(i.endswith("Fahad"))  # checks if the string end with given value
print(i.endswith("Fahad", 13, 18))  # checks if the string end with given value between given indexes
print(i.find("F"))  # return index where string is
print(i.find("i"))  # returns -1 if none
print(i.index("l"))  # same as find(), returns error if none
print(i.isalnum())  # returns True only if the entire string only consists of A-Z, a-z, 0-9.
print(i.isalpha())  # returns True only if the entire string only consists of A-Z, a-z.
print(i.islower())  # returns True if all the characters in the string are lower case
print(i.isprintable())  # returns True if all the values within the given string are printable
print(i.isspace())  # returns True only and only if the string contains white spaces
print(i.istitle())  # returns True only if the first letter of each word of the string is capitalized
print(i.startswith("SinAth"))  # returns True if the string starts with a given value
print(i.swapcase())  # Upper case are converted to lower case and lower case to upper case.
print(i.title())  # capitalizes each letter of the word within the string."""

#  if-else statement
'''age = int(input("enter your age: "))
print("so your age is: ", age) 
if age < 18:
    print("you can't drive kiddo")
elif age >= 75:
    print("too old to put you on that driving seat, oldtimer")
else:
    print("oh, you surely can drive mate")    '''

#  match case statements
"""x = int(input("enter a number: "))
match x:
    case 0:
        print("this is zero")
    case 5:
        print("this is five")
    case _:
        print(x)"""

#  loops
# for loops
"""name = "Sinath"
for i in name:
    print(i, end=", ")
print("\n")
for k in range(5):
    print(k)
print("\n")
for n in range(3, 10):
    print(n)
print("\n")
for k in range(1, 14, 3):
    print(k)"""

# while loops
'''i = 0
while i <= 10:
    print(i)
    i+=1'''

# Function
'''def add(a, b):
    print(a + b)
add(5,8)
def minus(a, b):
    print(a - b)
minus(5,10)'''

# list
"""listt = [1, 5, 44, "sinath", True, 'c', 5.6]
print(listt, type(listt))
print(len(listt))
print(listt[4])
print(listt[-5])  # negative index, pichon the count hobe...44 will be printed
print(len(listt) - 5)  # making positive index...print 7-5 = 2
print(listt[len(listt) - 5])  # ekhane len(listt)-5 er value 2, so print 44
print(listt[-1])  # last element of the list
print("Yes" if True in listt else "No")  # ternary operator
print(listt[1:5])  # 1 to 4; 5 er value print hobe na
print(listt[-5:-2])  # 7-5=1, 7-2=4; print 5 to sinath
print(listt[-6:-1:2])  # 7-5=1, 7-1=6; print- 5 to sinath; jumps 2 index
print(listt[:])  # 0:len(listt)
print(listt[::2])  # from zero to last, skips every 2 index"""


# list method
'''l = [1, 5, 10, 6, 0, 1, 3]
print(l, type(l))
l.append(7)  # adds 7 in the end of list
l.sort()  # sorts in assending order(choto theke boro)
l.sort(reverse=True)  # sorts in desending order(boro theke choto)
l.reverse()  # reverse a list(pichon theke sajay)
print(l.index(0))  # return index of given value
print(l.count(1))  # returns number how many times value appeared
m = l.copy()  # creates a copy of list, thus no changes in main list
m[0] = 2
print(m)
l.insert(2, 25)  # inserts a value in given index
n = [50, 70, 90]
l.extend(n)  # new list er content gulake ager list er sathe add kore modify kore dey
k = l+n  # list+list. new list create hoy, konota modify hoy na
print(k)
print(l)'''

# tuple
'''tup = (1, 5, 6)
print(tup, type(tup))
print(type(tup))
print(tup[2])
print(tup[-1])
if 7 in tup:
    print("yes")
else:
    print("no")'''

# Operations on tuple
'''countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)
print(countries)
tup1 = (1, 2, 3, 3, 7, 8, 5, 2, 1)
res = tup1.count(3)  # counts a value
res1 = tup1.index(8)  # gives index of given value
res2 = tup1.index(7, 2, 8)
print("3 comes ", res, " times")
print("8 is in index", res1)
print("7 is in index", res2)'''

# indirectly changing tuple since it can't be changed straight away
'''tup = (1, 5, "santiago", "nou")
print(tup, type(tup))
ltt = list(tup)
print(ltt, type(ltt))
ltt.pop(3)
print(ltt,)
ltt.append("bernabeu")
print(ltt)
tup = tuple(ltt)
print(tup)'''

# f-strings
'''message = "Hey, I am {} and ami {} cdi"
name = "Sinath"
country = "india"
# print(message.format(name, country))
print(f"Hey, I am {name} and ami {country} cdi")'''

# Doc-string
'''def square(n):
    """Takes in a number n, returns the square of n"""
    return n**2
print(square.__doc__)'''

'''def square(n):
    """takes a number n, returns the square of n"""
    print(n ** 2)
square(8)
print(square.__doc__)'''

# recursion
'''def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)
num = 7
print("Number: ", num)
print("Factorial: ", factorial(num))'''

# set
'''info = {"Carlo", 19, False, 5.9, 19}
print(info, type(info))  # doesn't add duplicate, no order    

nset = set()  # creates an empty set
print(type(nset))'''

# set methods
'''s1 = {1, 2, 3, 5, 6}
s2 = {4, 6, 3, 7}
print(type(s1))
print(s1.union(s2))  # merge 2 sets but none get changed
s1.intersection(s2)  # updates and add values of a set with another set
print(s1)
cities1 = {"Tokyo", "Madrid", "Berlin", "Dhaka"}
cities2 = {"Tokyo", "Seoul", "helsinki", "Madrid"}
cities3 = cities1.update(cities2)  # updates and add values of a set with another set
print(cities3)'''

# Dictionary
"""info = {"name": "sinath", "age": 22, "job": "student"}
print(f"main dictionary: {info}")
print(f"key name = {info["name"]}")
print(f"all the keys are: {info.keys()}")
print(f"all the values: {info.values()}")
print(info.items())

for keys in info.keys():
    print(f"{keys} = {info[keys]}") """

# Decorators
"""def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thnx for using this function!")
    return mfx

@greet
def hello():
    print("hello world")


def add(a, b):
    print(a+b)


hello()
"""
"""
class Book:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name


book1 = Book("English 1st")
book2 = Book("Physics")
book3 = Book("Biology")

print(book1)
print(book2)
print(book3)
"""
