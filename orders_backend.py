import connection

#database connection
conn = connection.conn_str()
cursor = conn.cursor()


def generate_order_id(ordered_items: dict):
    global details
    conn = connection.conn_str()
    cursor = conn.cursor()
    query = "select count(distinct orderid) from orders"
    cursor.execute(query)
    data = cursor.fetchall()
    oid = (f"od{data[0][0]}")
    continue_orders(oid, ordered_items)


def continue_orders(order_id, menu_items_dict):
    conn = connection.conn_str()
    cursor = conn.cursor()
    payment_status = 0
    order_status = 0

    #NOTE: check query

    # store order details in database
    for menu_items_key in menu_items_dict:
        quantity = menu_items_dict[menu_items_key]
        print([order_id, menu_items_key, quantity, payment_status, order_status])
        query = f"insert into orders values('{order_id}', '{menu_items_key}', {quantity}, {payment_status}, {order_status})"
        cursor.execute(query)
        conn.commit()

    # fetch menuid from order table using orderid
    menuid_query = f"select menuid from orders where orderid = '{order_id}'"
    cursor.execute(menuid_query)
    # get menuid using order id from order id
    menu_ids = cursor.fetchall()
    
    #to store food names
    food_names = []  
    # fetch food names for each menuid from menu table
    for menu_item_name in menu_ids:
        food_name_query = f"select name from menu where menuid = '{menu_item_name[0]}'"
        cursor.execute(food_name_query)
        food_name = cursor.fetchall()
        # storing all food names inside food_names list
        food_names.append(food_name[0][0])
    print(food_names)

    # fetch food quantity from order table
    food_quantity_query = f"select quantity from orders where orderid = '{order_id}'"
    cursor.execute(food_quantity_query)
    food_quantities = cursor.fetchall()
    # list of food_quantity
    food_quantity = []
    for quantity in food_quantities:
        # storing food quantity for each food ordered
        food_quantity.append(quantity[0])
    print(food_quantity)


    # # fetch food price from menu table
    food_price = []
    for price in menu_ids:
        food_price_query = f"select price from menu where menuid = '{price[0]}'"
        cursor.execute(food_price_query)
        food_prices = cursor.fetchall()
        # storing food prices for each food
        food_price.append(food_prices[0][0])
    print(food_price)

    # item price and quantity
    # def order_details():
    #     # ordered items info
    #     food_items = list(food_items)
    #     food_quantity = list(food_quantity)
    #     food_price = list(food_price)

    
    # tax percentage and service charge
    tax_charge = 0.18
    service_charge = 1.5
        
    # return all variables for gui use
    return food_names, food_quantity, food_price, tax_charge, service_charge

def fetch_name_price(menu_id):
    conn = connection.conn_str()
    cursor = conn.cursor()
    query = f"select name, price from menu where menuid='{menu_id}'"
    cursor.execute(query)
    data = cursor.fetchall()
    # print(data[0][0], data[0][1])
    food_name = data[0][0]
    food_price = data[0][1]
    return food_name, food_price

fetch_name_price("menu1")