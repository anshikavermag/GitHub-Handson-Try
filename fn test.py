"""a function is  a block of code that performs a specific task.
Types of function:
    std lib fn: built in function in python that are available to use.
    We can create our own function based on our requirements.
    def fnname():
    def is a keyword used to declare a function. fn name is ay name given to the function.
    arguments- any value parsed to fucntion.
    return- optional keyword, that returns value from a function."""
def greet():
    print("I am bored of these basic programs")
greet()
""" an argument is  a vlaue that is accepted by a function
a fn with two arguments
def addnum(num1,num2):
    print( num1+num2)
addnum(30,302)
num1=int(input("enter any no"))
num2=int(input("enter no"))
addnum(num1,num2)"""

def sq(n):
    result=n*n
    return result
print(sq(5))
