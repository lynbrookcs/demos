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
# %% other types of comprehension
test_set = {i for i in range(10)} # will make a set of range(10)
test_dict = {i: i + 1 for i in range(10)} # will make a dict of value: value + 1
test_generator = (i + 1 for i in range(10)) # will make a generator instead of list of range(10)
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
def var_args(*args):
    print(args)
var_args(1, 2, 3, 4)
# %% variadic keyword arguments
def var_kwargs(**kwargs):
    print(kwargs)
var_kwargs(arg1=True, arg2=1, arg3="hello")
# %% argument unpacking
data = [1, 2, 3, 4, 5, 6]
print(*data)
print(data[0], data[1], data[2], data[3], data[4], data[5]) # equivalent of above

def add(a, b):
    return a + b
my_args = {"a": 1, "b": 2}
print(add(**my_args)) # Will print 3



# %% pythonpp
# shameless plug: star pythonpp at https://github.com/KentoNishi/PythonPP
# full demo at the repo website also
# install by ``pip install pythonpp``
# adds easier encapsulation
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
