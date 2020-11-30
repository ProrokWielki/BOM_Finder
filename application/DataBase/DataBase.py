import parts as Parts


class DataBase:
    def __init__(self):
        self.elements = []
        self.number_of_elements = 0

    def add(self, element):
        self.elements.append(element)
        self.number_of_elements += 1

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
            self.number_of_elements -= 1

    def get_number_of_elements(self):
        return self.number_of_elements

    def find_elements(self, property):
        found_elements = DataBase()

        for element in self.elements:
            if element == property:
                found_elements.add(element)

        if(found_elements.get_number_of_elements() == 0):
            return False

        return found_elements

    def __str__(self):
        str_to_return = ""

        for element in self.elements:
            str_to_return += str(element) + "\r\n"

        return str_to_return[:-2]

    def get_elements(self):
        return self.elements

    def to_json(self):
        tmp_dict = []

        for record in self.elements:
            tmp_dict.append(record.to_dictionary())

        return tmp_dict

    # TODO it makes it tightly coupled to Parts
    def from_json(self, json):
        for part in json:
            self.add(Parts.types[part["Part"]].from_dictionary(part))
