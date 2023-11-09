import connection

def fetch_menu_items():
    conn = connection.conn_str()
    cursor = conn.cursor()
    query = "select * from menu"
    cursor.execute(query)
    data = cursor.fetchall()
    name_list = []
    price_list = []
    img_path_list = []
    menuid_list = []
    for i in data:
        menuid_list.append(i[0])
        name_list.append(i[1])
        price_list.append(i[2])
        img_path_list.append(i[3])
    cursor.close()
    return menuid_list, name_list, price_list, img_path_list