import random as rand

COLORS = ["blue", "red", "green", "yellow", "orange", "purple", "pink", "clear"]
COMMODITY = ["ambient", "produce", "general", "oversize", "chilled", "mto", "unknown"]
known_upcs = []


def generate_upc():
    i = 0
    number = 0
    while i < 12:
        number = number * 10 + int(rand.random() * 10)
        i += 1
    return number


def assign_commodity():
    return COMMODITY[int(rand.random() * len(COMMODITY))]


def assign_color():
    return COLORS[int(rand.random() * len(COLORS))]


def is_in(obj, arr):
    try:
        return arr.index(obj) + 1
    except ValueError:
        return 0


def generate_name(length):
    name = ""
    i = 0
    while i < length:
        name += chr(int(rand.random() * 94 + 32))
        i += 1
    return name


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


with open("products.txt", 'a') as products:
    i = 0
    while i < 25000:
        fake_sales = generate_sales()
        upc = generate_upc()
        while is_in(upc, known_upcs):
            upc = generate_upc()
        known_upcs.append(upc)
        price = format(rand.random() * int(rand.randrange(10, 100)), '.2f')
        salesfloor_count = int(rand.random() * 200)
        name = generate_name(int(rand.random() * 95 + 5))
        case_size = int(rand.randrange(3, 200))

        products.write("UPC: {}\nName: {}\nPrice: ${}\nSales Floor Count: {}\n"
                       "Lifetime Sales:{}\nQ1 Sales: {}\nQ2 Sales: {}\nQ3 Sales: {}\nQ4 Sales: {}\nMonthly Sales: {}\n"
                       "Daily Sales: {}\nColor: {}\nCase Size: {}\nCommodity: {}\n\n".format(
                        upc, name, price, salesfloor_count, fake_sales[0], fake_sales[1], fake_sales[2], fake_sales[3],
                        fake_sales[4], fake_sales[5], fake_sales[6], assign_color(), case_size, assign_commodity()))
        i += 1
        if i % 10000 == 0:
            print(i)
