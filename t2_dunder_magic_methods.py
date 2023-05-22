import inspect
from queue import Queue as q

# TODO Tutorial #2
# NOTE LISTS ARE ALL OBJECTS even functions * + etc, are objects
# x = [1,2, 3]
# y = [4,5]

# print(x+y)
# print(type(x))
# print(x)

# NOTE

class Person:
  def __init__(self, name):
    self.name = name

  # NOTE Change a printable return of a built-in function 
  # def __repr__(self):
  #   return f"Person({self.name})"

  # NOTE Magic method of multiplication, if we woudn't overwrite it, it would throught an error
  # def __mul__(self, x):
  #   if type(x) is not int:
  #     raise ValueError("Invalid argument, must be int")
  #   self.name = self.name * x

  # NOTE Magic method of 
  # def __call__(self, y):
  #   print(y)
    
  # # NOTE Magic method of 
  # def __len__(self):
  #   return len(self.name)
  
# p = Person('tim')
# p * 4
# print(len(p))

# q = Queue()
# print(q)
# print(inspect.getsource(Queue))


class Queue(q):
  def __repr__(self):
    return f"Queue({self._qsize()})"

  def __add__(self, item):
    self.put(item)
  
  def __sub__(self, item):
    self.get()
qu = Queue()
qu + 9
qu + 7
qu - 0
print(qu)