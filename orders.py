import customtkinter as ctk
from pyglet import font
import orders_backend

font.add_file("Documents/Trip_Sans/TripSans-Medium.ttf")
font.add_file("Documents/Trip_Sans/TripSans-Bold.ttf")
ffont = ('Trip Sans Bold', 40)
ffont1 = ('Trip Sans Medium', 20)
ffont2 = ('Trip Sans Medium', 16)

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  # creating cutstom tkinter window
app.geometry("1280x720")
app.title('Orders')

app.resizable(False, False)
app.lift()
app.attributes('-topmost', True)
app.after_idle(app.attributes, '-topmost', False)

# row and column configure
app.rowconfigure(0, weight=1)
app.rowconfigure(1, weight=4)
app.columnconfigure(0, weight=1)
app.columnconfigure(1, weight=1)
app.columnconfigure(2, weight=1)

#frame containing


# menu label on top
title = ctk.CTkLabel(master=app, text="ORDER", font=ffont)
title.grid(row=0, column=1, pady=30)
# title.pack(expand=True, pady=10)

# # item price and quantity
# food_items = ["Burger", "Chicken Sandwich", "some food", "some another food",
#               "something", "its tasty food", "something new thistym"]
# food_quantity = [2, 3, 2, 1, 4, 1, 2]
# food_price = [69, 45, 34, 23, 12, 54, 12]

# # tax percentage and service charge
# tax_charge = 0.18
# service_charge = 15

# order details frame -left
odrframe = ctk.CTkScrollableFrame(master=app, width=700, height=450)
odrframe.grid(row=1, columnspan=2, padx=10, sticky="ne")

# payment details frame -right
payframe = ctk.CTkFrame(master=app, width=100, height=360)
payframe.grid(row=1, column=2, padx=10, sticky="nw")

# order category frame
catframe = ctk.CTkFrame(master=odrframe, width=600,
                        fg_color="#333333")
catframe.pack(expand=True, fill="x")

# food details frame inside orderframe
foodordered = ctk.CTkFrame(master=odrframe, width=200, fg_color="#38618c")
foodordered.pack(expand=True, fill="x", pady=6)

# order category labels
fooditem = ctk.CTkLabel(master=catframe, width=100,
                        height=50, text="Order Name", font=ffont1)
fooditem.pack(side="left", expand=True)
fquantity = ctk.CTkLabel(master=catframe, width=100,
                         text="Quantity", font=ffont1)
fquantity.pack(side="left", expand=True)
fprice = ctk.CTkLabel(master=catframe, width=100,
                      text="Price", font=ffont1)
fprice.pack(side="right", expand=True)

# food ordered details


def order(food_item, quantity, price, rowq):
    item1 = ctk.CTkLabel(master=foodordered, width=230,
                         height=40, text="{}".format(food_item), font=ffont2, fg_color="#294868")
    quantity1 = ctk.CTkLabel(
        master=foodordered, width=230, text="{}".format(quantity), font=ffont2)
    price1 = ctk.CTkLabel(master=foodordered, width=230,
                          text="${}".format(price), font=ffont2)
    # place them
    item1.grid(sticky="ew", row=rowq, column=0)
    quantity1.grid(sticky="ew", row=rowq, column=1)
    price1.grid(sticky="ew", row=rowq, column=2)


# order_info = [0,0,0,0,0]
# food_items = order_info[0]
# food_quantity = order_info[1]
# food_price = order_info[2]
# tax_charge = order_info[3]
# service_charge = order_info[4]

food_items = ["osmething", "nothign"]
food_quantity = [2,4]
food_price = [34.6,453.5]
tax_charge = 1.5
service_charge = 1.3

# declaring sub_total amount as 0
sub_total = 0
for i in range(len(food_items)):
    order(food_items[i], food_quantity[i], food_price[i], i)
    order(food_items[i], food_quantity[i], food_price[i], i)
    sub_total += food_quantity[i] * food_price[i]

# payment details


def payment_details(sub_t, tax, service):
    chargesframe = ctk.CTkFrame(
        master=payframe)
    chargesframe.grid(row=0, sticky="new", padx=10, pady=10)
    paycharges = ctk.CTkLabel(
        master=chargesframe, text="Sub Total: ${}\n\nTax Charges: ${}\n\nService Charges: ${}"
                    .format(sub_t, tax, service), font=ffont2, height=150, pady=10, padx=10)
    total_amount = sub_t + sub_t * tax + service
    payamount = ctk.CTkLabel(
        master=payframe, text="Total amount: \n${}".format(total_amount), width=280, font=ffont1, height=205)
    paybtn = ctk.CTkButton(master=payframe, text="Pay",
                           width=200, height=60, font=ffont1)
    paycharges.grid(row=0, sticky="n")
    payamount.grid(row=1, sticky="n")
    paybtn.grid(row=2, sticky="ns", pady=14)

    # sub total , tax , service charge
payment_details(sub_total, tax_charge, service_charge)

app.mainloop()
