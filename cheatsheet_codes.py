# Basic print statements, single quotes and double quotes treated the same
print('Hi Py')
print('   *    ')
print('  ***   ')
# Escape characters in print - \t for tab, \n for new line
# separating print items with comma introduces space between them
print('He\tl', 'lo\n"Py\b\at\\hon"')
x = 10
y = 5
z = 'Hello'
print(x)
print(x, y, z, 'Again')

# + operator concatenates strings and adds numbers, combination of number and string results in TypError
first = 5
last = 4
print(first + last)
first = 'Hello'
last = 'Python'
print('Full name =', first + ' ' + last)
# Python is case-sensitive, identifier name can start with upper or lower case letter, remaining characters can be
# letter, number or a underscore
n1 = 10  # here we bind variable n1 to object 10
n2 = 10  # here we bind another variable n2 to object 10
n3 = 9.5
n12 = n1 + n2
n13 = n1 + n3
str4 = 'Fred'
str5 = '5'
str6 = '5.5'
# Explicit type casting - Constructor functions
# int() - integer from integer, float or string given that string is a whole number
# float() float from int, float or string which is int or float
# str() constructs string from wide variety

n3_int = int(9.5)
str5_to_int = int(str5)
# str6_to_int = int(str6) will lead to ValueError, invalid literal for int()
str6_to_float = float(str6)
str6_rounded = round(float(str6))
str6_again_str = str(str6_rounded)

print(
    type(n1), type(n2), type(n3), type(n12), type(n13),
    type(str4), type(str5), type(n3_int), type(str5_to_int),
    type(str6_to_float)
)

# Tuple assignment, both sides should have same number of items
x, y, z = 4, 5, 'hi'

# end and sep in print
print('hi', x, y, z, sep='--', end='**')
print('hi', 'without space', sep='')

# # User inputs and types, uncomment them to try
# x = input('Enter x')
# y = input('Enter y')
# print(x + y)
# # by default, input assumes string values to any input, can type convert to int, float or eval
# x = int(input('Enter x'))  # input should be only integer values
# y = int(input('Enter y'))
# print(x + y)
# x = float(input('Enter x'))  # input can be integer or float values
# y = float(input('Enter y'))
# print(x + y)
# x = eval(input('Enter x'))  # input can be integer or float value, or string in quotes
# y = eval(input('Enter y'))
# print(x + y)


# Formatting strings
print('{0:>10} {1} ** {0} -- {2:>10}'.format('format', 'check', 2 ** 5))

# Arithmetic operators
x = 9
y = 2
z = 'hi'
subop = x - y
mulop1 = x * y
mulop2 = y * z
divop = x / y
quoop = x // y  # operator which return only quotient of division
remop = x % y
powop = x ** y
'''
Precedence:
binary ** % right
unary +, -
binary *, / , //, % left to right
binary +, _ left to right
binary relational operators ==, !=, <=, >=, <, >
unary not
binary and - left associativity
binary or - left associativity
'''
d1 = +3
d2 = -4
d3 = 6
precedence_check1 = 6 * 5 + d1 ** 2 ** 2 / 5 + d2

# increment and decrement operator
xin = 6
yin = 7
xin += 5  # ans is 11
yin -= 3  # ans is 4

# Conditional executions and if, while statements
b1 = 5
b2 = False  # True and False are boolean operators, with bool as keyword
print(b1, 'is', type(b1))
# relational operators--  ==, <, >, <=, >=, !=
# if and elif are similar to switch case
if b1 == 3:
    print('b1 is 3')
elif b1 == 5:
    print('b1 is 5')
elif b1 == 6:
    print('b1 is 6')

x = 5
y = -9
z = 0
if bool(x):
    print('x is true')
if bool(y):
    print('y is true')
if not bool(z):
    print('z is false')  # False includes False, None, 0 and []
if x > 0 and y < 0 and z == 0:
    print('x is positive, y is negative and z is zero')
if x > 0 and y > 0 or z == 0:
    print('(x is positive and y is negative) or z is zero')
# iterations- while and for
while x > 0:
    print('x =', x)
    x -= 1
# for stmt
for item in range(3):
    print('y =', y, 'item =', item)
    y += 1
for i in range(-4, 5, 2):
    print(i)
for i in range(10, 3, -2):
    print(i)
name = 'tree'
st = 1
for index, letter in enumerate(name, start=1):
    print('{0} is the letter number {1} of the word'.format(letter, index), ', Step =', st)
    st += 1
# multiplication table
for i in range(5):
    for j in range(5):
        print('{} multipled by {} is '.format(i, j), i * j)
sum_total = 0

# break statement takes the control out of loop
x = 5
while True:
    sum_total += x
    x -= 1
    if x < 0:
        print('the item is ', x)
        break
print(sum_total)

# else clause can be used with while and for if required

# Functions
# syntax to import: import module / from module import function or list of functions
import math  # Example for syntax import module
from math import sqrt  # Example for syntax, from module import function

# math module has functions including sqrt, cos, exp, log, log10, pow, degrees, radians, fabs
# time module has functions- perf_counter() is like stop clock, sleep(2) makes the execution sleep for 2 seconds
print(math.sqrt(8))
dir(__builtins__)  # gives list of all builtin module
dir(math)  # list of functions in the module
help(print)
help(math.sqrt)
# form random module, functions include random, randint, seed, choice
from random import random, randint, seed, choice

seed(30)  # Pseudo random number generator is used in Python, seed provides a starting point
print(random())
print(randint(1, 4))
print(choice(('one', 'two', 'three')))

# *args stands for wildcard formal positional arguments, **kwargs stands for wildcard keyword arguments
# *args and **kwargs can also be used in function calls



# da argument in this function can be set if you pass it as keyword argument or second positional argument


def func1(x_f, da=7, *args, **kwargs):
    print(x_f, da)
    argsvs = []
    kwargsvs_key_only = []
    kwargsvs_key = []
    kwargsvs_value = []
    alocal = 500
    # initialize global variables as global inside function before assigning a value, but dont need it to print
    global aglobal1
    aglobal1 = 601
    aglobal2 = 602
    for arg in args:
        argsvs.append(arg)
        print(arg)
        # return argsvs
    for key, value in kwargs.items():
        kwargsvs_key.append(key)
        kwargsvs_value.append(value)
        print(key, value)
    for key in kwargs:
        kwargsvs_key_only.append(key)
        print(key)
    return x_f, da, argsvs, kwargsvs_key, kwargsvs_value, kwargsvs_key_only


# aa, ab = func1(3, 5, cc=6, dd=2)
aa = func1(6)  # x_f is 6, da is 7, args=(), kwargs={}
ab = func1(6, 8)  # same as above except da is 8
ac = func1(6, da=9)
ad = func1(6, 5, 'a', 'b')  # x_f is 5, da is 5, args=('a','b')
ae = func1(6, 5, 'a', 'b', k1=8, k2='d')
af = func1(6, 5, k1='c', k2='d')
ag = func1(6, k1='c', k2='d')
ah = func1(6, k1='c', da=90)


def menu():  # a function can return input function
    return input('enter value')


# global and local variables
aglobal1 = 501
aglobal2 = 502
aglobal3 = 503


def global2p():
    global aglobal1
    aglobal1 = 600
    alocal1 =200
    print(aglobal1, aglobal2, aglobal3, alocal1)


global2p()


# sending function as a parameter


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def arith(f, a, b):
    d = f(a, b)
    print(d)


arith(add, 5, 6)
arith(sub, 5, 6)

# lambda expressions, syntax: lambda parameterlist: expression , note that parameterlist does not have parenthesis and
# expression cannot be a block of stmt, expression is more of a return value
# lambda can be passed as a function, returned as a function
a = 5
b = 8

print(lambda a, b: a + b)  # returns object location
arith(lambda a, b: a + b, 5, 90)
arith(lambda a, b: a if a > b else b, 5, 90)
f = lambda a, b: print(a ** b)
f(4, 3)

# map expects a function object and any number of iterables such list or dictionary
map_out = map(add, [1, 2, 3, 4], [2, 3, 4, 5])
print(list(map_out))
# filter - apply function to the following iterable
filter_out = filter(lambda x: x > 2, [0, 1, 2, 4, 5])
print(list(filter_out))

# generators -- functions with a yield statement instead of return statement
# once the function yields, function is paused and control is transferred to caller
# __iter__() and __next__() are implemented automatically
# when function terminates, StopIteration is raised automatically


def gen_ex():
    i = 1
    yield i
    i += 1
    yield i
    i += 2
    yield i


print(gen_ex())
t = gen_ex()
print(next(gen_ex()))
print(next(t))
print(t.__next__())
for item in gen_ex():
    print(item)

# Fibonacci example for generator
# for i in range(limit):


def fib_gen(limit):
    i = 0
    a, b = 0, 1
    while i < limit:
        a, b = b, a + b
        yield a
        i +=1


t = fib_gen(10)
for i in range(7):
    print(next(t))

print(sum(t))

# generator expressions
# are like list comprehensions, but returns generator instead of list
a = (x*x for x in range(5))
print(a)
print(next(a))
print(next(a))
a_iter = iter([1, 2, 3])
print(a_iter)


# list comprehensions
b = [x*x for x in range(5)]
print(b)


# Decorators are adding functionality to arbitrary fns


def dec1(f):
    def wrapper(a, b):
        print('Start of fn')
        result = f(a, b)
        print('result is {} and its End of fn'.format(result))
        return result
    return wrapper


@dec1
def adder_dec(a, b):
    return a+b


adder_dec(5, 6)

# String as an object
s = '  ILovePython  '
print(s.upper())
print(s.lower())
print(s.rjust(10, "*"))
print(s.strip())
print(s.__getitem__(5))
print(s[5])
print(len(s))
print(s.__len__())
print(s)

# File handling
with open('hello.txt', 'r+') as f:
    f.write('stop it pls')
    for line in f:
        print(line.strip())

list_ex1 = [3, 5, 8, 'sam', [3, 5]]
for num in reversed(list_ex1):
    print(num)

list_ex2 = [4.7, 5, 4.8, 2, 3]
for num in sorted(list_ex2, reverse=True):
    print(num)

list_ex3 = ['aa', 'bb']
for num in sorted(list_ex3, reverse=True):
    print(num)

list_ex4 = ['kk', 'aa', 'bb']
for num in sorted(list_ex4):
    print(num)
# sorted not supported between str and int

a = [9, 11, 2, 5, 6, 7, 9]
a.sort()
a.reverse()
a.remove(9)
a_ind = a.index(5)
a.append(111)
a.insert(1, 2)
# list slicing
print(a[1:3])
print(a[-1: -5: -1])
print(a[1:6:2])
# del a[1:3]
# list can be sent as argument of the function
# list comprehensions
l2 = [x/2 for x in [6, 7]]
print(l2)
l3 = [(x,y**2) for x in ['a', 7] for y in [2, 3]]
print(l3)
l4 = [x/2 for x in [6, 7, 'les'] if type(x) == int]
print(l4)

# Two dimensional matrix
a_matrix = [[2, 3, 4], [2, 5, 6]]
for i in a_matrix:
    for j in i:
        print(j, end=' ')
    print()
a_matrix[1][1] = 100
for i in a_matrix:
    for j in i:
        print(j, end=' ')
    print()

# _ as a throwaway variable
for aaa in range(100):
    print(aaa)

for _ in range(100):
    print(_)

a5 = [[0 for _ in range(4)] for _ in range(2)]
a5[0][2] = 6

# Tuples -- immutable
tuple_ex = (2, 3, 7, 1, 6, 'str3', [2, 4], (4, 7))
print(tuple_ex[2:], tuple_ex[7])
for item in tuple_ex:
    print(item)

# element modification like tuple_ex[2] = 10 is not possible in tuple
# addition like append, insert, removal like del tuple_ex[2] are not possible

a1 = [2, 3, (3, 5)]
a2 = ('a', 'b', 'c', 'd')
a3 = zip(a1, a2)

print(list(a3))
a3 = zip(a1, a2)

for t in a3:
    print(t)

# zip can also be used with generator yield element in run time
# list comprehension with zip
print([x + y for x, y in zip([1, 2, 2], [3, 4, 5])])

# *args - another example


def summer(*args):
    s = 0
    print('inside fn1')
    for arg in args:
        s += arg
    print('inside fn2')
    return s
    print('inside fn3')


print(summer(3, 4, 6, 5))
print(summer(*(3, 4, 6, 5)))  # have to unpack tuple into separate arg

# dictionaries
di = {'c': 50, 'd': 60}
di2 = {}  # this is how you initialize empty dictionary
di[5] = 30
di['b_obj'] = 40
print(di)
print(di[5])
if 5 in di:
    print(di['b_obj'])
else:
    print(di['a_obj'])

# keys method of dictionary class
for k in di.keys():
    print(k)
# also this works
for k in di:
    print(k)
# values method of dictionary class
for v in di.values():
    print(v)
# for key, values pair
for k, v in di.items():
    print(k, v)

# Forming dictionary from zip, di key can be string, int or tuple  which are immutable or even a function i think
a1 = [4, 5, 'a']
a2 = [2, 5, 6]
d4 = dict(zip(a1, a2))
print(d4)

# split fn
s = 'i am always right and you are left'
print(s.split())

# Set {}, but no : pair to differentiate from dictionary, set values are non-repetitive and no order

a = [2, 2, 1, 'a', 'b', 'a', 1]
a = set(a)
b = {2, 4, 'c'}
print(a | b)
print(a & b)
print(a - b)  # set difference
print(a ^ b)  # elements in a or b but not both
print('a' in a)
print('a' not in a)


# enumerating data structure
for i, j in enumerate(a):
    print(i, j)

# Exception handling -- try, except

try:
    # a_num = int(input('Enter a value to array'))
    # print('You entered a number', a_num)
    # divans = 5/0  # ZeroDivisionError
    [][5] = 8  # Index out of bound error
except ValueError:
    print('You did not enter a number')
except ZeroDivisionError:
    print('Division by zero error')
except IndexError:
    print('out of bound in array')

# catch all handler
try:
    i = 5/0
except Exception:
    print('Some error occurred')
# true catching
try:
    sys.exit(0)
except:  # catches the exceptions that even Exceptions can't catch
    print('again some error')

# catching exception as objects
import random
ain2 = [2, 3]
adi2 = {'a': 5, 'b': 7}
try:
    ain = random.randint(1,6)
    if ain == 1:
        print(zee)  # there is no name named zee, so it will throw name error
    elif ain == 2:
        from random import randint2  # will throw import error
    elif ain == 3:
        print(ain2[4])  # index out of bound error
    elif ain == 3:
        print(adi2['c'])  # key error since there is no key as c in dictionary
    elif ain == 4:
        print(ain2['a'])  # inappropriate type
    elif ain == 5:
        print(int('b'))  # operation applied to inappropriate value inside the '', value error, '5' will not throw error
    elif ain == 6:
        print(6/0)
except NameError as n:
    print('name error', n, type(n))
except ImportError as i:
    print(i, type(i))
except IndexError as ie:
    print (ie, type(ie))
except TypeError:
    print('te')
except ValueError:
    print('ve')


# Raising exceptions, making custom exceptions
# raise Exception('Cannot')

# optional else in try
# try, except, else -- it there is an exception in try block, except is executed. if not, else is executed
try:
    a = 5/5
except:
    print('Exception occurred')
else:
    print('No exception dividing 5 by 5')

try:
    a = 5/0
except:
    print('Exception occurred')
else:
    print('No exception dividing 5 by 0')


# try, except, finally - finally is executed no matter what
try:
    a = 5/5
except:
    print('Exception occurred')
finally:
    print('No exception dividing 5 by 5')

try:
    a = 5/0
except:
    print('Exception occurred')
finally:
    print('No exception dividing 5 by 0')


# Classes and objects
# class variables and instance variables
class Country:
    city = 'sask'
    weather = 'cold'

    def __init__(self):
#        self.city = 'london'
        self.act = 'fringe fest'
    def __call__(self):
        print('hello')

# __init__ is executed when object is created
# __call__ is executed when object is called


x = Country()
y = Country()
print(Country.city)
print(x.city)
print(y.city)
# print(Country.act)  # this will throw attribute error
print(x.act)
print(y.act)
x()


class Robot:
    increase_per_term = 1.03  # class variable
    number_of_robots = 0

    def __init__(self, name, duty, cost):
        self.name = name  # instance variable
        self.duty = duty
        self.cost = cost
        Robot.number_of_robots += 1

    def aboutme(self):
        print('{} does {}'.format(self.name, self.duty))

    def increase_cost(self):
        self.cost = self.cost * self.increase_per_term
        print(self.cost)

    @classmethod
    def set_increase_per_term(cls, amount):
        cls.increase_per_term = amount

    @staticmethod  # if the method does not access class or instance variable, it will be a static method
    def maintainance_due(number_of_days_since_bought):
        if number_of_days_since_bought > 365:
            print('yes, its due')

r1 = Robot('John', 'cleaning', 500)
r2 = Robot('Corey', 'making food', 1500)
r1.aboutme()
Robot.aboutme(r1)
r1.increase_cost()
print(r1.__dict__)
print(Robot.__dict__)

r2.aboutme()
r2.increase_cost()
r2.increase_per_term = 1.09
r2.increase_cost()
print(Robot.increase_per_term)
print(r1.increase_per_term)
print(r2.increase_per_term)
Robot.set_increase_per_term(1.06)
print(Robot.increase_per_term)
print(r1.increase_per_term)
print(r2.increase_per_term)
r2.maintainance_due(500)


class Android(Robot):
    increase_per_term = 1.12

    def __init__(self, name, duty, cost, smartness_level):
        super().__init__(name, duty, cost)
        self.smartness_level = smartness_level

    def __add__(self, other):
        return self.cost + other.cost

    def __repr__(self):
        return('explanation obout the object')



a1 = Android('James', 'speaking', 9000, 5)
print(a1.name)
print(a1.increase_per_term)

# operator overloding
print(a1+r1)
print(a1)
