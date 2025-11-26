import ipdb

def this_function():
    inside = "I'm inside the function"
    print(inside)
    print("we're about to stop because of ipdb!")
    ipdb.set_trace()
    print("this line hasn't been interpreted yet - The program froze!")

this_function()
