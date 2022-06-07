import random
import inserting_data as indata

MIN_MOD = 25
MAX_MOD = 200
MAX_SECTION = 5


def __generate_aisle__(letter, aisle_number):
    sections = []
    for i in range(0, MAX_SECTION):
        sections.append(__generate_section__())
    return ['\'' + letter + str(aisle_number) + '\'', sections]


def __generate_section__():
    return random.randrange(MIN_MOD, MAX_MOD)


def __get_items_from_commodity__(cursor, commodity):
    command = 'SELECT product_id FROM product WHERE commodity=\'{}\''.format(commodity)
    cursor.execute(command)
    items = []
    for (product_id,) in cursor:
        items.append(product_id)
    return items


def __get_commods_from_db__(cursor):
    order = []
    command = 'SELECT commodity FROM product GROUP BY commodity ORDER BY 1'
    cursor.execute(command)
    for (commodity,) in cursor:
        order.append(commodity)
    return order


def __get_commodities__(cursor):
    commodities = __get_commods_from_db__(cursor)

    items_by_commodity = []
    for commodity in commodities:
        items_by_commodity.append(__get_items_from_commodity__(cursor, commodity))

    return items_by_commodity


def assign_aisles(cnx, cursor):
    columns = ['aisle', 'section', 'modular', 'product_id', 'facing', 'capacity']
    items_by_commodity = __get_commodities__(cursor)

    aisle_letter = 'A'
    for commodity in items_by_commodity:
        aisle_number = 1
        aisle = __generate_aisle__(aisle_letter, aisle_number)
        section = 0
        mods_used = aisle[1][section]
        for i in range(0, len(commodity)):
            if i - mods_used == 0:
                section += 1
                if section >= MAX_SECTION:
                    aisle_number += 1
                    aisle = __generate_aisle__(aisle_letter, aisle_number)
                    section = 0
                mods_used += aisle[1][section]

            random_face = int(random.random() * 4 + 1)
            random_capacity = random_face * (int(random.random() * 4 + 1))
            mod_used = aisle[1][section] + 1 - (mods_used - i)
            vals = [aisle[0], section + 1, mod_used, commodity[i], random_face, random_capacity]
            indata.insert_data(cursor, 'salesfloor', columns, vals)
        aisle_letter = chr(ord(aisle_letter) + 1)

    cnx.commit()
