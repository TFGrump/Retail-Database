import random
import inserting_data as indata

MIN_MOD = 25
MAX_MOD = 200
MAX_SECTION = 5


def __generate_aisle__(letter, aisle_number):
    sections = []
    for i in range(0, MAX_SECTION):
        sections.append(__generate_section__())
    return [letter + str(aisle_number), sections]


def __generate_section__():
    return random.randrange(MIN_MOD, MAX_MOD)


def assign_aisles():
    columns = ['aisle', 'section', 'modular', 'product_id', 'facing', 'capacity']
    number_of_items = 3543
    aisle_number = 1
    aisle = __generate_aisle__('A', aisle_number)
    section = 0
    mods_used = aisle[1][section]
    aisles = [aisle]

    for i in range(0, number_of_items):
        if i - mods_used == 0:
            print("MAX_MOD: {}\n".format(aisle[1][section]))
            section += 1
            if section >= MAX_SECTION:
                aisle_number += 1
                aisle = __generate_aisle__('A', aisle_number)
                aisles.append(aisle)
                section = 0
            mods_used += aisle[1][section]

        mod_used = aisle[1][section] + 1 - (mods_used - i)
        vals = [aisle[0], section + 1, mod_used, 1, 1, 1]
        command = indata.insert_data('salesfloor', columns, vals)
        print("{}".format(command))
    print(aisles)
