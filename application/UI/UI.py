import os

class Interface:
    def __init__(self):
        self.options = []
        self.title   = []
        self.prompt  = ">>"    
            
    def set_title(self, title, color = ""):
        self.title = [title, color] 
        
    def add_option(self, assigned_key, option_name, color = ""):
        self.options.append([assigned_key, option_name, color])
    
    def show(self):
        self.clear()
        if len(self.title) == 2:
            print(self.title[1] + self.title[0])
        
        for option in self.options:
            print( option[2] + "[" + option[0] + "] " + option[1])

    def clear(self):
        if os.name == "nt":
            os.system('cls')
        else:
            os.system('clear')
            
    def set_prompt(self, prompt):
        self.prompt = promt
        
    def show_prompt(self):
        return input(self.prompt)
        
    def execute(self):
        self.clear()
        self.show()
        return self.show_prompt()
        