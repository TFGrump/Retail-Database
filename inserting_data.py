import mysql.connector

cnx = mysql.connector.connect([REDACTED DATA])
cursor = cnx.cursor()


def insert_data(arr):
    cursor.execute("INSERT INTO product "
                   "(upc, name, price, salefloor_count, amount_sold_lifetime, amount_sold_Q1, amount_sold_Q1,"
                   " amount_sold_Q2, amount_sold_Q3, amount_sold_Q4, amount_sold_monthly, amount_sold_daily, size,"
                   " color, case_size, commodity) "
                   "VALUES (%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s)", arr)


with open("products.txt", 'r') as products:
    line = products.readline()
    while line:
        insert_data(line.split())
        line = products.readline()

cnx.commit()

cursor.close()
cnx.close()
