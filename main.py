import mysql.connector
import inserting_data as indata
import random_product_generator as rpg

cnx = mysql.connector.connect(user='TJ', password='Rub!kSCub3SQL', database='retail')
cursor = cnx.cursor()

columns = ['upc', 'name', 'price', 'salesfloor_count', 'amount_sold_lifetime', 'amount_sold_Q1',
           'amount_sold_Q2', 'amount_sold_Q3', 'amount_sold_Q4', 'amount_sold_monthly',
           'amount_sold_daily', 'size', 'color', 'case_size', 'commodity', 'length', 'depth', 'height']
# rpg.generate_random_products(25000, "products.txt")
indata.insert_data_from_file(cursor, cnx, "product", "products.txt", columns)
"""command = 'SELECT MAX(product_id) max FROM product'
cursor.execute(command)
for max_num in cursor:
    temp = max_num[0]
    print(temp)"""


cursor.close()
cnx.close()
