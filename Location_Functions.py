# This file holds all of the functions
def initialize():  # This writes the information from Places_config.txt as objets in a class called Locations
    place_names_file = open("Places_config.txt", "r")
    place_name_list = place_names_file.readlines()
    loc_temp_file = open("Locations_temp.py", "w")
    loc_temp_file.write('')
    loc_temp_file.close()
    loc_temp_file = open("Locations_temp.py", "a")
    loc_temp_file.write('class Locations:\n\n    def __init__(self, name, area, money, am_here):\n        '
                        'self.name = name\n        self.area = area\n        self.money = money\n        '
                        'self.am_here = am_here\n\n\n')
    import random
    area_code = 1
    for place_names in place_name_list:
        place_init = newline_remover(place_names)
        place_name = newline_space_remover(place_names)
        money_init = random.randint(500, 2000)
        if area_code == 1:
            loc_temp_file.write(place_name + ' = Locations("' + place_init + '", ' + str(area_code) + ', ' +
                                str(money_init) + ', True)')
        else:
            loc_temp_file.write('\n' + place_name + ' = Locations("' + place_init + '", ' + str(area_code) + ', ' +
                                str(money_init) + ', False)')
        area_code += 1
    loc_temp_file.write('\n\nplaces = [\n')

    for place_names in place_name_list:
        place_name = newline_space_remover(place_names)
        loc_temp_file.write('    ' + place_name + ',\n')

    loc_temp_file.write("]\n\n\n")
    place_names_file.close()
    loc_temp_file.close()


def in_town():  # This loop gives you in town options
    response = ""
    print("Welcome to " + location_list("here") + ".")
    while response != "0":
        in_a_town = open('In_a_town.txt', 'r')
        print(in_a_town.read())
        response = input()
        if response == "1":
            print("You are in " + location_list("here") + ".\nOther places include " + location_list("other") + ".")
        elif response == "2":
            in_a_town.close()
            travel()
            print("Welcome to " + location_list("here") + ".")
        elif response == "9":
            status()
        elif response == "0":
            print("Fine then.")
        else:
            print("That's not what I asked for.\n")
        in_a_town.close()
    else:
        print("You have decided to no longer participate.")


def newline_space_remover(placename):  # This removes spaces and newlines from the data in placename
    name_from_which_spaces_will_be_taken = ""
    for letter in placename:
        if letter in "\n ":
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + ""
        else:
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + letter
    return name_from_which_spaces_will_be_taken


def newline_remover(placename):  # This only removes newlines from data in placename
    name_from_which_spaces_will_be_taken = ""
    for letter in placename:
        if letter in "\n":
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + ""
        else:
            name_from_which_spaces_will_be_taken = name_from_which_spaces_will_be_taken + letter
    return name_from_which_spaces_will_be_taken


def how_much_money():
    from Locations_temp import places
    for place in places:
        if place.am_here:
            return place.money


def location_list(which):
    from Locations_temp import places
    if which == "here":
        for place in places:
            if place.am_here:
                return place.name
    elif which == "all":
        place_all = ""
        iteration = 1
        for place in places:
            if iteration <= len(places) - 2:
                place_all = place_all + place.name + ', '
            elif iteration == len(places) - 1:
                place_all = place_all + place.name + 'and '
            elif iteration == len(places):
                place_all = place_all + place.name + ' '
            iteration += 1
        return place_all
    elif which == "other":
        place_other = ""
        iteration = 1
        for place in places:
            if not place.am_here:
                if iteration <= len(places) - 3:
                    place_other = place_other + place.name + ', '
                elif iteration == len(places) - 2:
                    place_other = place_other + place.name + ' and '
                elif iteration == len(places) - 1:
                    place_other = place_other + place.name + ' '
                iteration += 1
        return place_other


def status():  # This lists all cities and all current data for them
    from Locations_temp import places
    for place in places:
        print(place.name + ' ' + str(place.area) + ' ' + str(place.money) + ' ' + str(place.am_here))


def travel():  # This changes the current am_here statuses
    from Locations_temp import places
    print("Where would you like to go?")
    for place in places:
        print('    (' + str(place.area) + ') ' + place.name)
    where = input()
    for place in places:
        if str(place.area) == where and place.am_here:
            print("You are already in " + place.name)
        elif str(place.area) == where and not place.am_here:
            for place_not in places:
                place_not.am_here = False
            place.am_here = True
            print("You are now in " + place.name)
