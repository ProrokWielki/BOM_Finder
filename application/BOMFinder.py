import DataBase.DataBase as DataBase
import Parts.Parts as Parts
import UI.UI as UI

import helpers

from parts import Resistor, Capacitor, Bipolar_transistor, types

import sys
import json
import colorama

data_base = DataBase.DataBase()

with open("debug.json", "r") as f:
    data_base.from_json(json.load(f))

take_menu_prompt = UI.ListPrompt("", [])


main_menu = UI.Submenu()
result_list = UI.ResultList()

choosen_part = None


def add(data):
    part = None

    for key, value in types.items():
        try:
            part = value(**data)
        except ValueError:
            pass

    if part is None:
        raise RuntimeError("Could not create a part")

    existing_part = data_base.find_elements(part)

    if existing_part:
        data_base.remove(existing_part.get_elements()[0])
        part.amount += existing_part.get_elements()[0].amount()

    data_base.add(part)
    with open("debug.json", "w") as f:
        json.dump(data_base.to_json(), f, indent=4)


def update_result(data):
    value = None

    for part_key, part_value in types.items():
        try:
            if isinstance(part_value.properties[list(data.keys())[0]], str):
                if len(part_value.properties[list(data.keys())[0]]) > 0:
                    value = Parts.Value(data[list(data.keys())[0]])
                else:
                    value = data[list(data.keys())[0]]
        except:
            pass

    if value is None:
        raise RuntimeError("Counld not create value")

    elements = data_base.find_elements(
        Parts.Property(list(data.keys())[0], value))
    result_list.set_results(elements.get_elements())


def take(data):
    global choosen_part
    data_base.remove(choosen_part)

    if choosen_part.amount - int(data["Amount"]) > 0:
        choosen_part.amount = choosen_part.amount - int(data["Amount"])

        data_base.add(choosen_part)

    with open("debug.json", "w") as f:
        json.dump(data_base.to_json(), f, indent=4)


def set_choosen_part(data):
    global choosen_part
    choosen_part = data[list(data.keys())[0]]


def update_take(data):
    global take_menu_prompt

    value = Parts.Value(data[list(data.keys())[0]])
    elements = data_base.find_elements(
        Parts.Property(list(data.keys())[0], value))

    take_menu_prompt.set_values(
        "Parts", elements.get_elements(), set_choosen_part)


def exit():
    sys.exit(0)


find_menu = UI.Submenu(main_menu)
add_menu = UI.Submenu(main_menu)
take_menu = UI.Submenu(main_menu)

take_resistor_menu = UI.Submenu(take_menu)
take_capacitor_menu = UI.Submenu(take_menu)

add_menus = []
find_menus = []
take_menus = []

for key, value in types.items():
    add_menus.append(UI.PromptSequence(helpers.to_prompt_sequence(value), add))
    find_menus.append(UI.Submenu(find_menu))
    take_menus.append(UI.Submenu(take_menu))

    for prop_key, prop_value in value.properties.items():
        if isinstance(prop_key, str):
            find_menus[-1].add_option(prop_key[0].lower(), prop_key, UI.PromptSequence(
                [UI.ValuePrompt(prop_key, update_result), result_list]), colorama.Fore.GREEN)
            take_menus[-1].add_option(prop_key[0].lower(), prop_key, UI.PromptSequence([UI.ValuePrompt(
                prop_key, update_take), take_menu_prompt, UI.ValuePrompt("Amount", take)]), colorama.Fore.GREEN)

    if isinstance(key, str):
        add_menu.add_option(key[0].lower(), key,
                            add_menus[-1], colorama.Fore.GREEN)
        find_menu.add_option(key[0].lower(), key,
                             find_menus[-1], colorama.Fore.GREEN)
        take_menu.add_option(key[0].lower(), key,
                             take_menus[-1], colorama.Fore.GREEN)


interface = UI.Interface(main_menu)


colorama.init(autoreset=True)

main_menu.add_option("f", "find", find_menu, colorama.Fore.GREEN)
main_menu.add_option("a", "add", add_menu, colorama.Fore.GREEN)
main_menu.add_option("t", "take", take_menu, colorama.Fore.GREEN)
main_menu.add_option("e", "exit", exit, colorama.Fore.GREEN)

while True:
    interface.execute()


menu.clear()
