import os

class Submenu:
    def __init__(self, supermenu = None):
        self.options = []
        self.supermenu = supermenu
        
    def add_option(self, assigned_key, option_name, action = None, color = ""):
        self.options.append([assigned_key, option_name, action, color])
    
    def show(self):
        for option in self.options:
            print( option[3] + "[" + option[0] + "] " + option[1])
            
    def get_supermenu(self):
        return self.supermenu
    
    def get_action(self, button_pressed):
        for option in self.options:
            if option[0] == button_pressed:
                return option[2]
        
        return None

class Interface:
    def __init__(self, main_menu):
        self.current_submenu = main_menu
        self.list_of_submenus = [main_menu]
        self.title   = []
        self.prompt  = ">>"    
            
    def set_title(self, title, color = ""):
        self.title = [title, color] 
           
    def add_submenu(self, submenu):
        self.list_of_submenus.append(submenu)
    
    def show(self):
        self.clear()
        if len(self.title) == 2:
            print(self.title[1] + self.title[0])
        
        self.current_submenu.show()

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
        
        button_pressed = self.show_prompt()
        
        if(self.current_submenu.get_action(button_pressed) != None):
            self.current_submenu = self.current_submenu.get_action(button_pressed);
        
        