def __format_data__(arr):
    data_str = ""
    i = 0
    while i < len(arr) - 1:
        data_str += arr[i] + ", "
        i += 1
    return data_str + arr[i]


def __format_columns__(columns):
    string = ""
    stop = len(columns) - 1
    for i in range(0, stop):
        string += str(columns[i]) + ", "
    return string + columns[stop]


def __format_sets__(columns, data):
    sets = ""
    stop = len(columns) - 1
    for i in range(0, stop):
        sets += "{} = {}, ".format(columns[i], str(data[i]))
    return sets + "{} = {}".format(columns[stop], str(data[stop]))


def insert_data(cursor, table, columns, values):
    command = "INSERT INTO " + table + \
              " (" + __format_columns__(columns) + ")" + \
              " VALUES ( " + __format_data__(values) + ")"
    cursor.execute(command)


def insert_data_from_file(cursor, cnx, table, file, columns):
    with open(file, 'r') as products:
        line = products.readline()
        while line:
            insert_data(cursor, table, columns, line.split("  "))
            line = products.readline()
    cnx.commit()


def update_table(cursor, cnx, table, columns, data, start, stop):
    for i in range(start, stop + 1):
        command = "UPDATE " + table + \
            " SET " + __format_sets__(columns, data[i-start]) + \
            " WHERE " + table + "_id = " + str(i)
        cursor.execute(command)
    cnx.commit()
