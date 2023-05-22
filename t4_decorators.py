
# ! Decorators allow us to change the behavior of our function without modifying its own code


# NOTE This is a decorator, you should create a function of wrapper to wrap another function, and call another function inside
def func(f):
  # In order to pass through arguments in decorator in wrapper, you should use *args and **kwargs as if you pass normal arguments,
  # you'll probably have an error as some functions can pass args, some don't 
  def wrapper(*args, **kwargs):
    print("Started")
    returned_value = f(*args, **kwargs)
    print("Ended")
    return returned_value
 
  return wrapper
# @func
# def func2():
#   print("i am func2")
@func
def func2(x, y):
  print(x)
  return y
  
@func # NOTE This is decorator, it's the exactly the same as func3 = func(func3) NOTE This is the name of the function a want to run!
def func3():
  print("i am func3")
  
#  NOTE This is how we can call the functions 
# x = func(func3)
# y = func(func2)
# print(x)
# x() 
# y()
# NOTE personal function to print args as many parameters as we want
# def functionTest(*args):
#   print(*args)
# functionTest("hello", "hi")

# ! But instead of doing it we can pass a function to a variable as a function and call it
# func3 = func(func3) 
# func2 = func(func2)
# NOTE In order to be able to call this function with an argument, a wrapper should have the same nº of parameters to intrudce
x = func2(5, 6)
print(x)
# But now we CAN'T call this function as it doesn't pass any arguments, the point of decorators is to use for multiple functions
# how can we solve it?
func3()

print("-------------------------------------------------")
import time
def timer(func):
  def wrapper(*args, **kwargs):
    start = time.time()
    returned_value = func()
    total = time.time() - start
    print("Time: ", total)
    return returned_value
  return wrapper

@timer
def test():
  for _ in range(1000000):
    pass

@timer 
def test2():
  time.sleep(2)

test()
test(2)