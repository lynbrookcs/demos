# Syntax Sugars in Python

# %% Ternary operator
num = 0
print("zero" if num == 0 else "one")
num = 1
print("zero" if num == 0 else "one")
# %% from 0 to 9
print([i for i in range(10)])
# %% from 69 to 420
print([i for i in range(69, 421)])
# %% reverse a list
my_list = [i for i in range(5)]
print(my_list[::-1])
# %% advanced list comprehension
my_list = [i for i in range(10) if i % 3 == 0]
print(my_list)
# %% Get items in a list from backwards indices
print(my_list[-1])
# %% iterate through a list
my_list = ["item 1", "item 2", "item 3"]
for item in my_list:
    print("Item is:", item)
# %% join a list
print(", ".join(my_list))
# %% unpacking values
var_a, var_b, var_c = "hello", "cs", "club"
print(var_a)
print(var_b)
print(var_c)
# %% returning multiple values
def myFunction1():
    return "value 1", "value_2"


val_1, val_2 = myFunction1()
print(val_1)
print(val_2)
# %% swap variables
print(val_1, val_2)
val_1, val_2 = val_2, val_1
print(val_1, val_2)
# %% repeat a string N times
print("This is repeated 5 times. " * 5)

# %% lambda functions
add = lambda a, b: a + b

print(add(9, 10))
# %% wrappers
def wrapper(my_class):
    print(my_class)


@wrapper
class SomeClass:
    pass


# %% operator overloading
class MyClass:
    def __getattribute__(self, name):
        # fstring
        return f"You tried to access {name}"

    def __setattr__(self, name, value):
        # fstring
        print(f"You tried to set {name} to {value}")


myObj = MyClass()
myObj.myAttr = "some value"
print(myObj.myAttr)
# %% variadic arguments
def add(*args):
    count = 0
    for arg in args:
        count += arg
    return count
print(add(1, 2, 3, 4)) # Will be 10
# %% variadic keyword arguments
def get_options(**kwargs):
    return {"flag": kwargs.get("flag", False), "arg": kwargs.get("arg", 0)}
print(get_options(flag=True, arg=1)) # Will be {"flag": True, "arg": 1}
print(get_options()) # Will be {"flag": False, "arg": 0}
# %% argument unpacking
data = [1, 2, 3, 4, 5, 6]
print(*data)
print(data[0], data[1], data[2], data[3], data[4], data[5]) # Equivalent of above
def testfunc(a, b):
    return a + b
testfunc_args = {"a": 1, "b": 2}
print(testfunc(**testfunc_args)) # Will print 3
# %% set comprehension
test_set = {i for i in range(10)} # Will make a set of range(10)
# %% dictionary comprehension
test_dict = {i: i + 1 for i in range(10)} # Will make a dict of value: value + 1
# %% generator comprehension
comp_gen = (i + 1 for i in range(10)) # Will make a generator instead of list of range(10)
# %% inline iterable for function
def sum_of_list(lyst):
    count = 0
    for i in lyst:
        count += i
    return i
print(sum_of_list([1, 2, 3, 4]))
print(sum_of_list(i + 1 for i in range(4)))
# %% pythonpp
# Shameless plug: star pythonpp at https://github.com/KentoNishi/PythonPP
# Full demo at the repo website also
# Install by ``pip install pythonpp``
# Adds easier encapsulation
from pythonpp import *
@PythonPP
class MyClass:
    def namespace(public, private):
        @constructor
        def Constructor(value):
            public.public_var = value + 1
            private.private_var = value

        @method(public)
        def public_method():
            private.private_method()
            return private.private_var

        @method(private)
        def private_method():
            print("EnCApSuLAtIOn")

obj = MyClass(0)
print(obj.public_var)
print(obj.public_method())
