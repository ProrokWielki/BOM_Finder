prefixes = ["p", "n", "u", "m", "", "k", "M", "G", "T"]

class Value:
    
    def __init__(self, value):      
        self.value = 0
        
        if isinstance(value, str):         
               
            tmp_list = list(value)
            
            prefix = ""
            prefix_position = -1
            
            decimal = -1
            
            for char in tmp_list:
                try:
                    int(char)
                    self.value  = 10 * self.value 
                    self.value += int(char)
                except ValueError:
                    if(char in prefixes ):
                        if(prefix == ""):
                            prefix = char
                            prefix_position = len(str(self.value))
                        else:
                            raise ValueError("Only one prefix is supproted")    
                    elif(char == "." or char == ","):
                        if(decimal == -1):
                            decimal = len(str(self.value))
                        else:
                            raise ValueError("Only one decimal separator allowed")      
                    else:
                        raise ValueError("unsupported char: '{}'".format(str(char)))  
            
            if((prefix_position < len(str(self.value)) and prefix_position != -1) and decimal != -1):
                raise ValueError("Only one decimal separator allowed")
            
            elif(decimal != -1):
                self.value = self.value/(10**(len(str(self.value)) - decimal))
                
            elif(prefix_position < len(str(self.value)) and prefix_position != -1):
                self.value = self.value/(10**(len(str(self.value)) - prefix_position))  
            
            if(prefix_position != -1):
                self.value *= 1000**(prefixes.index(prefix) - prefixes.index("")) 
                
        elif(isinstance(value, (int, float))):
            self.value = value
            
        else:
            raise TypeError("unsupported value type: '{}'".format(type(value)))
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.value == self.value
        elif isinstance(other, (int, float)):
            return other == self.value
        else:
            raise TypeError("unsupported value type: '{}'".format(type(value)))
    
    def get_value(self):
        return self.value

class Property:  
    def __init__(self, name, value, unit = ""):
        self.name = str(name)
        self.value = value
        self.unit = unit
        
        if(isinstance(value, str)):
            self.is_didgit_type = False
        elif(isinstance(value, (int, float))):
            self.is_didgit_type = True
        else:
            raise TypeError("unsupported value type: '{}'".format(type(value)))

    def get_property_name(self):
        return self.name
    
    def to_dictionary(self):
        return {self.name: self.value}

    def is_numerical(self):
        return self.is_didgit_type
    
    def __str__(self): 
        prefix = prefixes.index("")
        value_to_show = self.value
        if self.is_didgit_type is True:
            while value_to_show >= 1000 or value_to_show < 0:
                if value_to_show >= 1000:
                    value_to_show /= 1000
                    prefix +=1
                elif value_to_show < 0:
                    value_to_show *= 1000
                    prefix -=1
    
        return self.name + ": " + str(value_to_show) + " " + prefixes[prefix] + self.unit
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.name == other.name and self.value == other.value
        elif isinstance(other, (int, float)) and self.is_didgit_type is True:
            return self.value == other
        elif isinstance(other, str):
            return self.name == other
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))
    
    def __lt__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value < other.value
            elif isinstance(other, (int, float)):
                return self.value < other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")

    def __le__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value <= other.value
            elif isinstance(other, (int, float)):
                return self.value <= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")


    def __gt__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value > other.value
            elif isinstance(other, (int, float)):
                return self.value > other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")


    def __ge__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value >= other.value
            elif isinstance(other, (int, float)):
                return self.value >= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")


    def __sub__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                self.value -= other.value
            elif isinstance(other, int):
                self.value -= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")

        return self

    def __add__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                self.value += other.value
            elif isinstance(other, int):
                self.value += other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")
            
        return self


    def __mul__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                self.value *= other.value
            elif isinstance(other, int):
                self.value *= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")
            
        return self


    def __truediv__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                self.value /= other.value
            elif isinstance(other, int):
                self.value /= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise  TypeError("unsupported operand for object with value not being numerical")
            
        return self

class Part:
    def __str__(self):
        str_to_return = ""

        for property in self.properties:
            str_to_return += str(property) + "\r\n"

        return str_to_return[:-2] #return without last "\r\n"

    def has_property(self, property_to_check, in_range = 0):
        return_value = False
        
        for property in self.properties:
            if property.get_property_name == property_to_check.get_property_name:
                if property_to_check.is_numerical() is True: 
                    if (property >= property_to_check - in_range 
                      and property <= property_to_check + in_range):
                        return_value = True
                else:
                    if property == property_to_check:
                        return_value = True

        return return_value
    
    def to_dictionary(self):
        tmp_dictioanry = {}
        for property in self.properties:
            tmp_dictioanry = {**tmp_dictioanry, **property.to_dictionary()}
        
        return tmp_dictioanry
    
    def __eq__(self, other):
        if isinstance(other, Property):
            return other in self.properties
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))
    
class Resistor(Part):
    number_of_parameters = 6
    unit = "R"
    def __init__(self, resistance, power, package, tolerance, mounting, number_of = 1):        
        self.properties = []
        self.properties.append(Property("Type", "Resistor"))      
        self.properties.append(Property("Resistance", resistance, self.unit))
        self.properties.append(Property("Power", power))
        self.properties.append(Property("Package", package))
        self.properties.append(Property("Tolerance", tolerance))
        self.properties.append(Property("Mounting", mounting))
        self.properties.append(Property("Amount", number_of))
               
class Capacitor(Part):
    number_of_parameters = 6
    unit = "F"
    
    def __init__(self, capacitance, volatage, package, tolerance, mounting, number_of = 1):
        self.properties = []
        self.properties.append(Property("Type", "Capacitor"))      
        self.properties.append(Property("Resistance", capacitance, self.unit))
        self.properties.append(Property("Power", volatage))
        self.properties.append(Property("Package", package))
        self.properties.append(Property("Tolerance", tolerance))
        self.properties.append(Property("Mounting", mounting))
        self.properties.append(Property("Amount", number_of))