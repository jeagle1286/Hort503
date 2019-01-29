# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# DO not start a function name with a number
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
# Args is like Argv which allows you to add arguments in a function
# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")
#Checklists are helpful
#this one takes no argument
def print_none():
    print("I got nothing")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
