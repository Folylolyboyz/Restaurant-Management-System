import connection
from login import *

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

def login_button_function(username_entry, password_entry, login_text):
    username = username_entry.get()
    password = password_entry.get()
    status = openMenu(username, password)
    if status == 0:
        login_text.configure(text="Wrong username", text_color="red")
    elif status == -1:
        login_text.configure(text="Wrong password", text_color="red")
    else:
        login_text.configure(text="Done", text_color="white")