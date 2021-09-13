class Locations:

    def __init__(self, name, area, money, am_here):
        self.name = name
        self.area = area
        self.money = money
        self.am_here = am_here


Oakvale = Locations("Oakvale", 1, 1044, True)
Lumbridge = Locations("Lumbridge", 2, 931, False)
Targovishta = Locations("Targovishta", 3, 1141, False)
Whiterun = Locations("Whiterun", 4, 1132, False)
LasVegas = Locations("Las Vegas", 5, 1101, False)

places = [
    Oakvale,
    Lumbridge,
    Targovishta,
    Whiterun,
    LasVegas,
]


