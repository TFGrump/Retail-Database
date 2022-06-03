import random as rand

COLORS = ["blue", "red", "green", "yellow", "orange", "purple", "pink", "clear"]
COMMODITY = ["ambient", "produce", "general", "oversize", "chilled", "mto", "unknown"]
known_upcs = []


def generate_upc():
    digit = 0
    number = 0
    while digit < 12:
        number = number * 10 + int(rand.random() * 10)
        digit += 1
    return number


def add_surrounding_symbols(string, symbol):
    return symbol + string + symbol


def assign_commodity():
    return add_surrounding_symbols(COMMODITY[int(rand.random() * len(COMMODITY))], '\'')


def assign_color():
    return add_surrounding_symbols(COLORS[int(rand.random() * len(COLORS))], '\'')


def is_in(obj, arr):
    try:
        return arr.index(obj) + 1
    except ValueError:
        return 0


def generate_dimensions():
    lengths = []
    for i in range(0, 3):
        lengths.append(rand.random() * 100)
    return lengths


def generate_name(name_len):
    rand_name = ""
    cur_len = 0
    while cur_len < name_len:
        letter = rand.random() * 25
        if rand.random() <= .5:
            rand_name += chr(int(letter + 65))
        else:
            rand_name += chr(int(letter + 97))
        cur_len += 1
    return add_surrounding_symbols(rand_name, '\'')


def generate_sale(max_sales):
    return int(rand.random() * max_sales)


def generate_sales():
    """
    sales:
        sold_lifetime
        sold_Q1
        sold_Q2
        sold_Q3
        sold_Q4
        sold_monthly
        sold_daily
    """
    sales = []
    i = 0
    lifetime = generate_sale(1000)
    sales.append(lifetime)
    while i < 4:
        sale = generate_sale(lifetime)
        lifetime -= sale
        sales.append(sale)
        i += 1
    monthly_sale = generate_sale(lifetime)
    sales.append(monthly_sale)
    sales.append(generate_sale(monthly_sale))
    return sales


def generate_size():
    oz = [' fl oz', ' oz']
    str_size = str(rand.randrange(1, 100)) + oz[int(rand.random() * 2)]
    return add_surrounding_symbols(str_size, '\'')


def generate_random_products(num_products, file):
    with open(file, 'a') as products:
        for i in range(0, num_products):
            fake_sales = generate_sales()
            upc = generate_upc()
            while is_in(upc, known_upcs):
                upc = generate_upc()
            known_upcs.append(upc)
            price = format(rand.random() * int(rand.randrange(10, 100)), '.2f')
            salesfloor_count = int(rand.random() * 200)
            name = generate_name(int(rand.random() * 95 + 5))
            case_size = int(rand.randrange(3, 200))
            size = generate_size()
            dimensions = generate_dimensions()

            # File Line Order:
            # UPC, Name, Price, Sales Floor Count, Lifetime Sales, Q1 Sales, Q2 Sales, Q3 Sales, Q4 Sales,
            # Monthly Sales, Daily Sales, Size, Color, Case Size, Commodity, Length, Depth, Height
            products.write("{}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}\n".format(
                upc, name, price, salesfloor_count,  fake_sales[0], fake_sales[1], fake_sales[2], fake_sales[3],
                fake_sales[4], fake_sales[5], fake_sales[6], size, assign_color(), case_size, assign_commodity(),
                dimensions[0], dimensions[1], dimensions[2]))
            if i % 5000 == 0:
                print(i)
