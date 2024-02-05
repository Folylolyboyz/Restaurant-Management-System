import connection

#database connection
conn = connection.conn_str()
cursor = conn.cursor()

def pending_order_items():
    query = "select orderid, name, quantity from orders left join menu on orders.menuid = menu.menuid where payment_status = 1 and order_status = 0;"
    conn = connection.conn_str()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    # query = "select distinct(orderid) from orders where payment_status = 0;"
    # cursor.execute(query)
    # active_orders = cursor.fetchall()
    active_orders = []
    # print(data)

    for i in data:
        if i[0] not in active_orders:
            active_orders.append(i[0])
    # print(active_orders)
    l = {}
    orders = {}
    for order_id in active_orders:
        # print(order_id)
        for j in data:
            if j[0] == order_id:
                food_name = j[1]
                food_quantity = j[2]
                l[food_name] = food_quantity
        # print(l)
        orders[order_id] = l
        l={}
    return orders
# pending_order_items()

def completed_order_items():
    query = "select distinct(orderid) from orders where payment_status = 1 and order_status = 1;"
    conn = connection.conn_str()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    data = [i[0] for i in data]
    return data
# completed_order_items()

def update_to_complete(orderid):
    query = f"update orders set order_status = 1 where orderid = '{orderid}';"
    conn = connection.conn_str()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    # query = "select distinct(orderid) from orders where payment_status = 1 and order_status = 1;"
    # conn = connection.conn_str()
    # cursor = conn.cursor()
    # cursor.execute(query)
    # conn.commit()