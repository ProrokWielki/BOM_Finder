import os
 
header = "\
_________               .__    __________                   __               __\n\
\_   ___ \  ____   ____ |  |   \______   \_______  ____    |__| ____   _____/  |_\n\
/    \  \/ /  _ \ /  _ \|  |    |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\\\n\
\     \___(  <_> |  <_> )  |__  |    |     |  | \(  <_> )  |  \  ___/\  \___|  |\n\
 \______  /\____/ \____/|____/  |____|     |__|   \____/\__|  |\___  >\___  >__|\n\
        \/                                             \______|    \/     \/      \n"

import colorama

class Colors:
    blue  = '\033[94m'
    pink  = '\033[95m'
    green = '\033[92m'

class Interface:
    def __init__(self):
        self.options = []
        self.title   = []
        colorama.init(autoreset=True)
        
    def set_title(self, title, color = ""):
        self.title = [title, color] 
        
    def add_option(self, assigned_key, option_name, color = ""):
        self.options.append([assigned_key, option_name, color])
    
    def show(self):
        self.clear()
        if len(self.title) == 2:
            print(self.title[1] + self.title[0])
        
        for option in self.options:
            print(option[1] + option[0])

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
            

 

 
def colorize(string, color):
    if not color in colors: return string
    return colors[color] + string + '\033[0m'
 
def foo():
    print("You called foo()")
    input("Press [Enter] to continue...")
 
def bar():
    print("You called bar()")
    input("Press [Enter] to continue...")
 
menuItems = [
    { "Call foo": foo },
    { "Call bar": bar },
    { "Exit": exit },
]
 
def menu():
        # Print some badass ascii art header here !
        print(colorize(header, 'pink'))
        print(colorize('version 0.1\n', 'green'))
        for item in menuItems:
            print(colorize("[" + str(menuItems.index(item)) + "] ", 'blue') + list(item.keys())[0])
        choice = input(">> ")
        try:
            if int(choice) < 0 : raise ValueError
            # Call the matching function
            list(menuItems[int(choice)].values())[0]()
        except (ValueError, IndexError):
            pass