"""
Dictionarie

Resistors - value | power | package | tolerance | THT/SMD
Capacitor - value | voltage | package | tolerance | type | THT/SMD
IC        - name  | package | SMD/THT
Diodes    - type  | current | Forvarde Voltage | Reverse Voltage | THT/SMD
LEDs      - color | forvard voltage | current | color | package | THT/SMD
switches  - type  | max current | package | size | THT/SMD
Inductors - value | current | package | THT/SMD

"""

import json

class Property:
    name = ""
    value = ""
    
    def __init__(self, name, value):
        self.name = str(name)
        self.value = str(value)

    def __str__(self):
        return self.name + ": " + self.value

    def __eq__(self, other):
        return self.name == other.name and self.value == other.value

class Part:
    def __str__(self):
        str_to_return = ""

        for property in self.properties:
            str_to_return += str(property) + "\r\n"

        return str_to_return[:-2]

    def has_property(self, property_to_check):
        return_value = False
        
        for property in self.properties:
            if property == property_to_check:
                return_value = True

        return return_value

class Resistor(Part):
    def __init__(self, resistance, power, package, tolerance, mounting):
        self.properties = []
        self.properties.append(Property("Resistance", resistance))
        self.properties.append(Property("Power", power))
        self.properties.append(Property("Package", package))
        self.properties.append(Property("Tolerance", tolerance))
        self.properties.append(Property("Mounting", mounting))



class DataBase:
    def __init__(self):
        self.parts = []
        self.number_of_parts = 0

    def add(self, part):
        self.parts.append(part)
        self.number_of_parts += 1

    def get_number_of_parts(self):
        return self.number_of_parts

    def find_element(self, property):
        found_parts = DataBase()

        for part in self.parts:
            if part.has_property(property) == True:
                found_parts.add(part)

        if(found_parts.get_number_of_parts() == 0):
            return False

        return found_parts

    def __str__(self):
        str_to_return = ""

        for part in self.parts:
            str_to_return += str(part) + "\r\n"

        return str_to_return[:-2]


data_base = DataBase()

resistor1 = Resistor(100, 10, "0603", 10, "SMD")
resistor2 = Resistor(200, 30, "0402", 5, "THT")

data_base.add(resistor1)
data_base.add(resistor2)

print(data_base.find_element(Property("Resistance", 100)))
