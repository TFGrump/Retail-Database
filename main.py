import mysql.connector
import inserting_data as indata
import random_product_generator as rpg

cnx = mysql.connector.connect('[REDEACTED]')
cursor = cnx.cursor()


def __get_items_from_commodity(commodity):
    command = 'SELECT name, upc FROM product WHERE commodity=\'{}\''.format(commodity)
    cursor.execute(command)
    items = []
    for (name, upc) in cursor:
        items.append((name, upc))
    return items


def __get_order__():
    order = []
    command = 'SELECT commodity, COUNT(*) FROM product GROUP BY commodity ORDER BY 2 DESC'
    cursor.execute(command)
    for (commodity, count) in cursor:
        order.append(commodity)
    return order


columns = ['upc', 'name', 'price', 'salesfloor_count', 'amount_sold_lifetime', 'amount_sold_Q1',
           'amount_sold_Q2', 'amount_sold_Q3', 'amount_sold_Q4', 'amount_sold_monthly',
           'amount_sold_daily', 'size', 'color', 'case_size', 'commodity', 'length', 'depth', 'height']
# rpg.generate_random_products(25000, "products.txt")
# indata.insert_data_from_file(cursor, cnx, "product", "products.txt", columns)


def get_commodities():
    commodity_order = __get_order__()
    items_by_commodity = []
    for commodity in commodity_order:
        items_by_commodity.append(__get_items_from_commodity(commodity))

    for i in range(0, len(commodity_order)):
        print("{}: {}".format(commodity_order[i], len(items_by_commodity[i])))


def update_dimensions():
    command = 'SELECT MIN(product_id) min_id, MAX(product_id) max_id FROM product'
    cursor.execute(command)
    for (min_id, max_id) in cursor:
        new_dimensions = []
        for i in range(min_id, max_id + 1):
            new_dimensions.append(rpg.generate_dimensions())
        dimension_columns = ['length', 'depth', 'height']
        indata.update_table(cursor, cnx, 'product', dimension_columns, new_dimensions, min_id, max_id)


update_dimensions()

cursor.close()
cnx.close()
