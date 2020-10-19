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
