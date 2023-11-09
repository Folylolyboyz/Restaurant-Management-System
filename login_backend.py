import connection

def checkAccountExist(username, password):
    conn=connection.conn_str()
    cursor=conn.cursor()

    #Get password
    cursor.execute("select pwd from user where userid = '{}'".format(username))
    data = cursor.fetchall()
    
    if not data:
        #Return 0 for wrong username
        return 0
    else:
        pwd = data[0][0]
        if pwd == password:
            #Return 1 when authenticated
            return 1
        else:
            #Return -1 for wrong password
            return -1

def openMenu(username, password):
    status = checkAccountExist(username, password)
    if status == 1:
        return status
    else:
        return status