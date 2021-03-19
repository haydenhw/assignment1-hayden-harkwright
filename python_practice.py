def QuestionDivider(str):
    numstars = 5 
    print("\n" + "*" * numstars + str + "*" * numstars)



QuestionDivider("Run Python Programs")
print("Hayden HarkWright")
print("Row row row your boat gently down a stream")



QuestionDivider("Variables")
for i in range(10):
    print(i)
print(64 + 32)
x = 64
y = 32
print(x + y)



QuestionDivider("Strings")
from datetime import datetime as dt
print("Willem Dafoe")
date = dt.now().strftime("%m/%d/%Y")
print(f"Today is %s" % (date,) )



QuestionDivider("String replace")
print( 
"foobar".replace("foo", "bar")
)
print( 
"foobar".replace("foo", "bar").replace("bar","foo")
)
print(
"the cat in the hat".replace("in the hat", "on your table")
)



QuestionDivider("String find")
test = "The Cat in the hat in the house"
print(
test.find("Cat")
)
print(
test.find("cat")
)
print(
test.find("in the")
)
def search_string():
    query = input("Search for term: ")
    result = test.find(query)
    print(result)
# search_string()



QuestionDivider("String join")
print(
   " ".join(["foo", "bar", "bang"]) 
)
print(
   "_".join(["foo", "bar", "bang"]) 
)



QuestionDivider("String split")
print(
    "fooabbarabbang".split("ab")
)
print(
    "World,Earth,America,Canada".split(",")
)
print(
    "The bitcoin price broke the psychological barrier early Saturday morning, returning to its blistering early-2021 bull market after taking a breather over recent weeks."
    .split("early Saturday morning")
)



QuestionDivider("Random numbers")
import random
x=random.randint(0, 10)
for i in range(3):
    print(random.randint(0,10))
freq = {}
for i in range(100):
    n = random.randint(0,10)
    if n not in freq:
        freq[n] = 1
    else: 
        freq[n] += 1
print(freq)



QuestionDivider("Keyboard input")
def getUserInfo():
    phone_number = input("Please enter your phone number")
    language = input("Please enter your preferred programming language")
# getUserInfo()




QuestionDivider("If statements")
def in_range():
    num = int(input("Enter a number between 1 and 10: "))
    if num < 0 or num > 10:
        print("Invalid Number")
    else:
        print("Valid Number")
# in_range()
def get_password():
    correct_pw = "flowers7"
    pw = input("Please enter your password: ")
    if correct_pw == pw:
        print("Password is correct")
    else:
        print("Password in incorrect")
#get_password()



QuestionDivider("For loops")
#1
print("#1")
clist = ['Canada','USA','Mexico','Australia']
for c in clist: 
    print(c)
#2
print("#2")
for i in range(101):
    print(i)
#3 
print("#3")
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
#4
print("#4")
for i in reversed(range(1,11)):
    print(i)
#5
print("#5")
for i in range(1, 11):
  if i % 2 == 0:
      print(i)
#6
print("#6")
_sum = sum([i for i in range(100, 201)])
print(f"Sum: {_sum}")



QuestionDivider("While loops")
clist = ["Canada","USA","Mexico"]

#1
count = 0
while count < len(clist):
    print(clist[count])
    count += 1

#2 
# A while loop will run indefinitely until a condition is met. 
# A for loop will run a specified number of times.

#3
# Yes
count = 0
_sum = 0
nums = [1,2,3]
while count < len(nums):
    _sum += nums[count]
    count += 1

print("While loop sum: " + str(_sum))



QuestionDivider("Functions")
#1
print("#1")
def sum_list(num_list): 
    return sum(num_list) 
print(sum_list([1,2,3,4,5]))

#2
print("#2")
def make_username(name):
    def get_randomint():
        return random.randint(1,1000)
    return name + str(get_randomint())
print(make_username("hayden"))
#3
print("#3")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
#4
print("#4")
def greet(name):
    hello = "Hello"
    def say_hello():
        print("%s, %s" % (hello, name))
    say_hello()
greet("World")



QuestionDivider("Lists")
print("All states: ")
state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
for state in state_names:
    print(state)

print("Starting with M: ")
for state in [state for state in state_names if state[0] == "M"]:
    print(state)



QuestionDivider("List operations")
y = [6,4,2] + [12,8,4]
print(y) 
y[1] = 3
print(y)



QuestionDivider("Sorting List")
x = [(3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key = lambda x: x[0])
print(x)
x.sort(key = lambda x: x[1])



QuestionDivider("Range function")
n1000 = list(range(1, 1001))
print(n1000)
print("largest: " + str(max(n1000)))
print("smallest: " + str(min(n1000)))



QuestionDivider("Dictionary")
import csv
countries = {}
with open("countries.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for c in list(reader)[0:20]:
        countries[c[0]] = c[1]

for key, val in countries.items():
    print(key, val)



QuestionDivider("Read file")
with open("countries.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    count = 0
    for c in list(reader)[0:20]:
        print(f"{count} {' '.join(c)}")
        count += 1

# f = open("nonexistant.txt", "r") 
# throws FileNotFound error



QuestionDivider("Write file")
with open("output.txt", "w") as f:
    f.write("Take it easy")

with open("output2.txt", "w") as f:
    f.write("""open("text.txt")""")



QuestionDivider("Nested Loops")
for i in range(1,4):
    for j in range(1,4):
      print(i, j)

persons = ["John", "Marissa", "Pete", "Dayton"]
for i in persons:
    for j in persons:
        if i != j:
            print(f"{i} meets {j}")

# A nested for loop has runtime complexity of O(n^k) where k corresesponds 
# to the number of level deep the loop goes



QuestionDivider("Slices")
pizzas = ["Hawai","Pepperoni","Fromaggi","Napolitana","Diavoli"]
print(
    pizzas[3:5]
)
print(
    "Hello, World"[-5:]
)



QuestionDivider("Multiple return")
def multi_return(a, b):
    return (a,b), (a+b)
print(multi_return(2, 3))

def return5vars():
    a = "foo"
    b = "bar"
    c = "bang"
    d = "baz"
    e = "fizz"
    return a, b, c, d, e
print(return5vars())



QuestionDivider("Scope")
balance = { "amt": 100}
def reduce_amount(n):
    balance["amt"] -= n
reduce_amount(15)
print(balance)

def with_local():
  local_var = "I am local"
  print(local_var)
with_local()



QuestionDivider("Time and date")
print(
    dt.today().strftime("%Y-%m-%d")
)



QuestionDivider("Try except")
def catch_invalid_keyboard_input():
    try:
        keyboard_input = input("Press the 'a' key: ")
        if keyboard_input != "a":
            raise ValueError("Wrong key entered")
    except ValueError as e:
        print(e)
#catch_invalid_keyboard_input()

try:
    f = open("nosuchfile.txt")
except: 
    print("File does not exist")



QuestionDivider("OOP Exercises")
def display_location(self):
    print("Oakland, CA")
class Foo:
    def make_class(self):
        return type("Bang", (object, ), {
          "location": display_location
        })
class Bar:
    pass
foo1 = Foo()
foo2 = Foo()
Bang = foo1.make_class()
bang = Bang()
bang.location()



QuestionDivider("Getter and setter")
class Person:
    def __init__(self):
        self.age = 0
    @property
    def age(self):
      return self._age
    @age.setter
    def age(self, val):
        if val < 0:
            raise("Age must be positive")
        self._age = val

# Use getters and setters to acheive encapsulation and validate inputs to keep object states valid



QuestionDivider("Modules")
import math
print(math.sin(3.1234))
from my_module import snake
snake()



QuestionDivider("Inheritance")
class App:
    def speak(self):
        print("I am an app")
class Program:
    def speak2(self):
        print("I am also a program")
class TodoApp(App):
    pass
t = TodoApp()
t.speak()
class ProgramApp(App, Program):
  pass
pa = ProgramApp()
pa.speak()
pa.speak2()



QuestionDivider("Static method")
class StaticDemo():
    @staticmethod
    def staticproof():
      print("Hello from static method")

StaticDemo.staticproof()

# Some consider static methods to be unneccsary because when  
# you want to create a collection of utilty methods with a namespace 
# you can do it is more idomatic to simply create a module with a collection of functions



QuestionDivider("Iterables")
# An iterable is an object that can be iterated of in a for loop
# The all have an iter() method which is returns an terator
# In Python, lists, tuples, and string are iterables
it = iter([1,2,3])
print(next(it))
print(next(it))
print(next(it))



QuestionDivider("Classmethod")
# With class methods, the class of the object instance is passed in as the 
# first arugment istead of self

# Neither self or cls are passed into static methods. Static methods are simply
# regular functions that can be called using either the object or the class



QuestionDivider("Multiple Inheritance")
# No, for example Java and Scala do not support multiple inheritance
#
# You might avoid using multiple inheritance because of the classic "Diamond Problem"
# where a subclass inherits two methods with the same name from two superclasses
# and there is ambiguity as to which definiton will be used when the method is called
#
# No, you can inherit as many classes as you want with multiple inheritance 



