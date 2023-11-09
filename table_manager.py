import connection

def truncate_orders():
    conn = connection.conn_str()
    cursor = conn.cursor()
    cursor.execute("truncate orders")
    conn.commit()
    cursor.close()
    conn.close()
    

def show_orders():
    conn = connection.conn_str()
    cursor = conn.cursor()
    cursor.execute("select * from orders")
    for i in cursor.fetchall():
        print(i)
    cursor.close()
    conn.close()

show_orders()