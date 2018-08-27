"""
Dictionarie

Resistors  - value | power | package | tolerance | THT/SMD
Capacitor  - value | voltage | package | tolerance | type | THT/SMD
IC         - name  | package | SMD/THT
Diodes     - type  | current | Forvarde Voltage | Reverse Voltage | THT/SMD
LEDs       - color | forvard voltage | current | color | package | THT/SMD
switches   - type  | max current | package | size | THT/SMD
Inductors  - value | current | package | THT/SMD
Connectors - number of 

"""

import DataBase.DataBase as DataBase
import Parts.Parts       as Parts
import UI.UI             as UI

import json
import colorama

data_base = DataBase.DataBase()

resistor1 = Parts.Resistor(100, 10, "0603", 10, "SMD")
resistor2 = Parts.Resistor(200, 30, "0402", 5, "THT")
resistor3 = Parts.Resistor(100, 10, "0302", 7, "SMD")
resistor4 = Parts.Resistor(10000, 10, "0302", 7, "SMD")
resistor5 = Parts.Resistor(1000, 10, "0302", 7, "SMD")



data_base.add(resistor1)
data_base.add(resistor2)
data_base.add(resistor3)
data_base.add(resistor4)
data_base.add(resistor5)

print(data_base.find_elements(Parts.Property("Resistance", 100)))

records = data_base.get_records()

tmp_dict = []

print(data_base.get_number_of_parts())

print(records)


for record in records:
    tmp_dict.append(record.to_dictionary())
    
with open("debug.json", "w") as f:
    json.dump(tmp_dict, f, indent=4)
    
with open("debug.json", "r") as f:
    read_data = json.load(f)
    
for data in read_data:
    print(data["Type"])
    if data["Type"] == "Resistor":
        print(data)
        res1 = Parts.Resistor(data["Resistance"], data["Power"], data["Package"], data["Tolerance"], data["Mounting"])
        print(res1)
    else:
        print("Nope")
        
   
        
menu = UI.Interface()

menu.add_option("debug1", colorama.Fore.GREEN)
menu.add_option("debug2", colorama.Fore.BLUE)

menu.show()
    
