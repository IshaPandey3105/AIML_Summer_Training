# Python OOPS
# Classes and Objects
# Classes are templates for objects. They define the properties and methods of an object.
# Objects are instances of classes and have their own set of attributes and methods.
# Inheritance is a mechanism in which one class can inherit the properties and methods of another class.
# Polymorphism is the ability of an object to take on multiple forms.
# Encapsulation is the idea of bundling data and methods that operate on that data within a single unit.
# Abstraction is the practice of hiding the implementation details of an object from the user and only showing the necessary information.

class Detail:
    name = "Isha"
    age = 20

obj1 = Detail()
print(obj1.name)
print(obj1.age)

# self method
# The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belong to the class.
# It must be provided as the extra parameter inside the method definition.
class Details:
    name = "Yash"
    age = 22
    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")

obj2 = Details()
print(obj2.name)
print(obj2.age)
obj2.desc()


# _init__ method
# The __init__ method is used to initialize the object’s state and contains statements that are executed at the time of object creation.

# Example:
class A:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj3 = A("Crab", "Crustaceans")
print(obj3.animal, "belongs to the", obj3.group, "group.")

# We can also modify their properties:

obj3.animal = "Shrimp"  # Modify object property
print(obj3.animal, "belongs to the", obj3.group, "group.")


# and delete objects their properties:

del obj3   # delete object entirely
print(obj3.animal, "belongs to the", obj3.group, "group.") # This will raise an error because obj3 has been deleted.