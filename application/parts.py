from Parts.Parts import Part


class Resistor(Part):
    properties = {"Resistance": "R",
                  "Power": "W",
                  "Tolerance": "%",
                  ("Mounting", "Package"): [("SMD", ["0402", "0805", "1206"]),
                                            ("THT", ["2x3", "5x7"])]}


class Capacitor(Part):
    properties = {"Capacitance": "F",
                  "Type": ["Electrolitic", "Ceramic"],
                  "Voltage": "V",
                  "Tolerance": "%",
                  ("Mounting", "Package"): [("SMD", ["0402", "0805", "1206"]),
                                            ("THT", ["2x3", "4x7", "5x7", "2.54", "5"])]}


class Bipolar_transistor(Part):
    properties = {"Model number": "",
                  "Type": ["NPN", "PNP"],
                  "C-E voltage": "V",
                  "C current": "A",
                  ("Mounting", "Package"): [("SMD", ["SOT23"]),
                                            ("THT", ["TO92"])]}


types = {"Resistor": Resistor,
         "Capacitor": Capacitor,
         "Bipolar_transistor": Bipolar_transistor}
