class DataBase:
    def __init__(self):
        self.parts = []
        self.number_of_parts = 0

    def add(self, part):
        self.parts.append(part)
        self.number_of_parts += 1

    def get_number_of_parts(self):
        return self.number_of_parts

    def find_elements(self, property):
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

    def get_records(self):
        return self.parts