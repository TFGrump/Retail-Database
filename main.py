import mysql.connector
import inserting_data as indata
import random_product_generator as rpg
import random_aisle_generator as rag

cnx = mysql.connector.connect('[REDACTED]')
cursor = cnx.cursor()


def update_dimensions():
    command = 'SELECT MIN(product_id) min_id, MAX(product_id) max_id FROM product'
    cursor.execute(command)
    for (min_id, max_id) in cursor:
        new_dimensions = []
        for i in range(min_id, max_id + 1):
            new_dimensions.append(rpg.generate_dimensions())
        dimension_columns = ['length', 'depth', 'height']
        indata.update_table(cursor, cnx, 'product', dimension_columns, new_dimensions, min_id, max_id)


columns = ['upc', 'name', 'price', 'salesfloor_count', 'amount_sold_lifetime', 'amount_sold_Q1',
           'amount_sold_Q2', 'amount_sold_Q3', 'amount_sold_Q4', 'amount_sold_monthly',
           'amount_sold_daily', 'size', 'color', 'case_size', 'commodity', 'length', 'depth', 'height']
# rpg.generate_random_products(25000, "products.txt")
# indata.insert_data_from_file(cursor, cnx, "product", "products.txt", columns)
# update_dimensions()


cursor.close()
cnx.close()
