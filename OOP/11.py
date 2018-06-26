def sayHello(name):
    print("I want to say hello with your,{0}".format(name))
    print("Hello,{0}".format(name))
    print("Done")

import os
if __name__ == "__main__":
    print("@@@"*10)
    name = input("Please enter your name:")
    print(sayHello(name))
    print("@@@"*10)
    print(os.getcwd())