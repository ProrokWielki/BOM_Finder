import os


class Submenu:
    def __init__(self, supermenu=None):
        self.options = []
        self.supermenu = supermenu

    def add_option(self, assigned_key, option_name, action=None, color=""):
        self.options.append([assigned_key, option_name, action, color])

    def show(self):
        for option in self.options:
            print(option[3] + "[" + option[0] + "] " + option[1])

    def get_supermenu(self):
        return self.supermenu

    def get_action(self, button_pressed):
        for option in self.options:
            if option[0] == button_pressed:
                return option[2]

        return None


class EmbeddedListPrompt:
    def __init__(self, title, names, prompts, action=None):
        self.title = title
        self.names = names
        self.prompts = prompts
        self.main_showed = False
        self.action = action
        self.option = -1

    def show(self):
        if self.main_showed:
            self.prompts[self.option].show()
        else:
            print(f"{self.title}:")
            iter = 0
            for name in self.names:
                print(f"[{iter}] {name}")
                iter += 1
            self.main_showed = True

    def get_value(self, button_pressed):
        if self.option == -1:
            self.option = int(button_pressed)
            return None

        ret = self.prompts[self.option].get_value(button_pressed)

        if ret is not None:
            ret[self.title] = self.names[self.option]

            if self.action is not None:
                self.action(ret)

            self.main_showed = False
            self.option = -1

        return ret


class ListPrompt:
    def __init__(self, value_name, values, action=None):
        self.value_name = value_name
        self.values = values
        self.action = action

    def show(self):
        print(f"{self.value_name}:")
        iter = 0
        for value in self.values:
            print(f"[{iter}] {value}")
            iter += 1

    def get_value(self, button_pressed):
        if self.action is not None:
            self.action({self.value_name: self.values[int(button_pressed)]})

        return {self.value_name: self.values[int(button_pressed)]}

    def set_values(self, value_name, values, action=None):
        self.value_name = value_name
        self.values = values
        self.action = action


class ValuePrompt:
    def __init__(self, value_name, action=None):
        self.value_name = value_name
        self.action = action

    def get_value(self, button_pressed):
        if self.action is not None:
            self.action({self.value_name: button_pressed})

        return {self.value_name: button_pressed}

    def show(self):
        print(f"{self.value_name}:")


class ResultList:
    def __init__(self):
        self.result_list = []

    def set_results(self, results):
        self.result_list = results

    def get_value(self, button_pressed):
        return {}

    def show(self):
        for result in self.result_list:
            print(result)


class PromptSequence:
    def __init__(self, sequence, action=None):
        self.sequence = sequence
        self.action = action
        self.dic = {}
        self.dic_current_value = 0

    def get_action(self, button_pressed):

        ret = self.sequence[self.dic_current_value].get_value(button_pressed)

        if ret is None:
            return self
        else:
            self.dic.update(ret)
            self.dic_current_value += 1

            if self.dic_current_value < len(self.sequence):
                return self

            if self.action is not None:
                self.action(self.dic)

            self.dic_current_value = 0

            return None

    def show(self):
        self.sequence[self.dic_current_value].show()

    def update_sequence(self, new_sequence):
        self.sequence = new_sequence


class Interface:
    def __init__(self, main_menu):
        self.current_submenu = main_menu
        self.list_of_submenus = [main_menu]
        self.title = []
        self.super_menu = main_menu
        self.prompt = ">>"

    def set_title(self, title, color=""):
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

        self.current_submenu = self.current_submenu.get_action(button_pressed)

        if self.current_submenu is None:
            self.current_submenu = self.super_menu
