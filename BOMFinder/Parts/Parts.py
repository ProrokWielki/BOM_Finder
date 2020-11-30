prefixes = ["p", "n", "u", "m", "", "k", "M", "G", "T"]


class Value:

    def __init__(self, value):
        self.value = 0

        if isinstance(value, str):

            value = value.replace(",", ".")

            try:
                self.value = int(value)
                return
            except ValueError:
                pass

            try:
                self.value = float(value)
                return
            except ValueError:
                pass

            tmp_list = list(value)

            prefix = ""
            prefix_position = -1

            decimal = -1

            for char in tmp_list:
                try:
                    int(char)
                    self.value = 10 * self.value
                    self.value += int(char)
                except ValueError:
                    if(char in prefixes):
                        if(prefix == ""):
                            prefix = char
                            prefix_position = len(str(self.value))
                        else:
                            raise ValueError("Only one prefix is supproted")
                    elif(char == "."):
                        if(decimal == -1):
                            decimal = len(str(self.value))
                        else:
                            raise ValueError("Only one decimal separator allowed")
                    else:
                        raise ValueError("unsupported char: '{}'".format(str(char)))

            if((prefix_position < len(str(self.value)) and prefix_position != -1) and decimal != -1):
                raise ValueError("Only one decimal separator allowed")

            elif(decimal != -1):
                self.value = self.value / (10**(len(str(self.value)) - decimal))

            elif(prefix_position < len(str(self.value)) and prefix_position != -1):
                self.value = self.value / (10**(len(str(self.value)) - prefix_position))

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

    def __str__(self):
        return str(self.get_value())

    def __sub__(self, other):
        return self.value - other


class Property:
    def __init__(self, name, value, unit=""):
        self.name = str(name)
        self.value = value
        self.unit = unit

        self.is_value_type = False
        self.is_didgit_type = False

        if(isinstance(value, str)):
            self.is_didgit_type = False
        elif(isinstance(value, (int, float))):
            self.is_didgit_type = True
        elif(isinstance(value, Value)):
            self.is_value_type = True
        else:
            raise TypeError("unsupported value type: '{}'".format(type(value)))

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    def get_property_name(self):
        return self.name

    def to_dictionary(self):
        if self.is_value_type:
            return {self.name: self.value.get_value()}
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
                    prefix += 1
                elif value_to_show < 0:
                    value_to_show *= 1000
                    prefix -= 1

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
            raise TypeError("unsupported operand for object with value not being numerical")

    def __le__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value <= other.value
            elif isinstance(other, (int, float)):
                return self.value <= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise TypeError("unsupported operand for object with value not being numerical")

    def __gt__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value > other.value
            elif isinstance(other, (int, float)):
                return self.value > other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise TypeError("unsupported operand for object with value not being numerical")

    def __ge__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                return self.name == other.name and self.value >= other.value
            elif isinstance(other, (int, float)):
                return self.value >= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise TypeError("unsupported operand for object with value not being numerical")

    def __sub__(self, other):
        if self.is_didgit_type is True:
            if isinstance(other, self.__class__):
                self.value -= other.value
            elif isinstance(other, int):
                self.value -= other
            else:
                raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))
        else:
            raise TypeError("unsupported operand for object with value not being numerical")

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
            raise TypeError("unsupported operand for object with value not being numerical")

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
            raise TypeError("unsupported operand for object with value not being numerical")

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
            raise TypeError("unsupported operand for object with value not being numerical")

        return self


class Part:
    base_properties = {"Part": "",
                       "Amount": "pcs"
                       }

    def __init__(self, Amount=1, ** kwargs):
        if len(kwargs) + len(self.base_properties) != self.num_of_properties():
            raise ValueError("Wrong number of arguments in")

        self.props = []
        self.props.append(Property("Part", self.__class__.__name__))

        for key, value in self.properties.items():
            if isinstance(key, str):
                if isinstance(value, list):
                    self.props.append(Property(key, kwargs[key]))
                elif isinstance(value, str):
                    if len(value) > 0:
                        self.props.append(Property(key, Value(kwargs[key]), value))
                    else:
                        self.props.append(Property(key, kwargs[key]))
                else:
                    raise TypeError("Wrong argument type")
            elif isinstance(key, tuple):
                for internal_key in key:
                    self.props.append(Property(internal_key, kwargs[internal_key]))
            else:
                raise TypeError("Wrong key type")

        self.props.append(Property("Amount", Value(Amount)))

    def __str__(self):
        str_to_return = ""

        for property in self.props:
            str_to_return += str(property).ljust(20) + " | "

        return str_to_return[:-2]  # return without last "\r\n"

    def has_property(self, property_to_check, in_range=0):
        return_value = False

        for property in self.props:
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
        for property in self.props:
            tmp_dictioanry = {**tmp_dictioanry, **property.to_dictionary()}

        return tmp_dictioanry

    def __eq__(self, other):
        if isinstance(other, Property):
            return other in self.props
        elif isinstance(other, Part):
            for property in self.props:
                if property.get_property_name() == "Amount":
                    continue
                if not property in other.props:
                    return False
            return True
        else:
            raise TypeError("unsupported operand type(s) for +: '{}' and '{}'".format(self.__class__, type(other)))

    @property
    def amount(self):
        for prop in self.props:
            if prop.get_property_name() == "Amount":
                return prop.value

        raise RuntimeError("Not found 'Amount' in properties")

    @amount.setter
    def amount(self, new_amount):
        if new_amount <= 0:
            raise ValueError("Amount must by > 0")

        for prop in self.props:
            if prop.get_property_name() == "Amount":
                prop.value = Value(new_amount)
                return

        raise RuntimeError("Not found 'Amount' in properties")

    @classmethod
    def num_of_properties(cls):
        num_of = 0

        for key in cls.properties.keys():
            if isinstance(key, tuple):
                for i in key:
                    num_of += 1
            else:
                num_of += 1

        return num_of + len(cls.base_properties)

    @classmethod
    def from_dictionary(cls, dictionary):
        # +1 for "Part" and +1 for Amount
        if len(dictionary) != cls.num_of_properties():
            raise ValueError("Wrong number of arguments")

        del dictionary["Part"]  # remove the Part key, it will be added agin in the constructor

        return cls(**dictionary)
