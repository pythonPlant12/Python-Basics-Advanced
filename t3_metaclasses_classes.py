# def hello():
#   class Hi:
#     pass
#   return Hi

# class Test:
#   pass

# def func():
#   pass

# NOTE All in python are objects and have types

# print(type(Test()))
# print(type(2))
# print(type(func))
# print(type(Test))

# print(Test)
# print(Test())
# NOTE this Test line 22 and 25 are the same objects/classes
# class Test:
#   pass

# class Foo:
#   def show(self):
#     print("Hi")

# NOTE How to add methods to a classes
# 1. Define a method 2. Look line 36 we pass this function to an attribute parameter when creating a class
# def add_attribute(self):
#   self.z = 9

# NOTE 1. parameter: name of the class / 2. parameter, inheritance of another class, 3. parameter: attributes

# Test = type('Test', (Foo, ), {"x":5, "add_attribute":add_attribute})
# t = Test()
# t.wy = "hello"
# print(Test)
# print(t.x)
# t.add_attribute()
# t.show()
# print(t.z)

# NOTE as on creating a class it calls type() so in order to create a Meta class it should have as parameter(type)...
# ! Important, this is how you create metaclasses
class Meta(type):
  # The __new__() is the first what is called when creating an objects
  # Here is a constructor to construct a Class (Look type() function is the same)
  def __new__(self, class_name, bases, attrs):
    print("ATTRS: ---------- ", attrs)

    a = {}
    print("ATTRS ITEMS: ---------- ", attrs.items())
    for name, val in attrs.items():
      if name.startswith("__"):
        a[name] = val
      else:
        a[name.upper()] = val
    print(a)
        
    return type(class_name, bases, a)

class Dog(metaclass=Meta):
  x = 5
  y = 8

  def hello(self):
    print("hi")
  

d = Dog()
print(d.HELLO)
  # The __init__() is the second called after the __new__()
  # def __init__():
    