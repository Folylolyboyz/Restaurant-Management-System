import connection
import customtkinter as ctk
from PIL import Image

import login, login_backend
import menu
import orders, orders_backend
import order_status
import chef
# import orders, orders_backend

conn = connection.conn_str()
cursor = conn.cursor()

class Window(ctk.CTk):
    def __init__(self, title):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        super().__init__()
        self.geometry("960x540")
        self.title(title)
        self.resizable(False,False)
        # self.wm_attributes("-transparentcolor", "grey")

        self.wholeloginframe = login.LoginFrame(self)
        
        # self.loginframe = login.Loginframe(self)
        self.wholeloginframe.loginframe.login_button.bind("<Button-1>", self.go_to_menu)
        # self.wholeloginframe.place_forget()

        self.menuframe = menu.Menuframe(self)
        self.menuframe.order_button.bind("<Button-1>", self.go_to_orders)
        self.menuframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.menuframe.place_forget()

        self.orderframe = orders.OrderFrame(self)
        self.orderframe.pay_button.bind("<Button-1>", self.go_to_order_status)
        self.orderframe.place_forget()

        self.orderstatusframe = order_status.OrderStatusFrame(self)
        self.orderstatusframe.return_to_menu.bind("<Button-1>", self.go_to_menu_from_status)
        self.orderstatusframe.star0.bind("<Button-1>", self.star_color_change0)
        self.orderstatusframe.star1.bind("<Button-1>", self.star_color_change1)
        self.orderstatusframe.star2.bind("<Button-1>", self.star_color_change2)
        self.orderstatusframe.star3.bind("<Button-1>", self.star_color_change3)
        self.orderstatusframe.star4.bind("<Button-1>", self.star_color_change4)
        self.star = Image.open("Documents/rating_star_selected.png")
        self.star_unselected = Image.open("Documents/rating_star_unselected.png")
        self.star = ctk.CTkImage(self.star, size = (35,35))
        self.star_unselected = ctk.CTkImage(self.star_unselected, size = (35,35))
        self.orderstatusframe.place_forget()

        self.chefframe = chef.ChefFrame(self)
        self.chefframe.place_forget()
        self.mainloop()

    def go_to_menu(self, event):
        self.username = self.wholeloginframe.loginframe.username_entry.get() #00B2FF
        password = self.wholeloginframe.loginframe.password_entry.get()
        status = login_backend.openMenu(self.username, password)
        if status == 0:
            self.wholeloginframe.loginframe.login_status_text.configure(text="Wrong username", text_color="red")
            self.wholeloginframe.loginframe.login_status_text.place(x = 244, y = 204)
        elif status == -1:
            self.wholeloginframe.loginframe.login_status_text.configure(text="Wrong password", text_color="red")
            self.wholeloginframe.loginframe.login_status_text.place(x = 248, y = 295)
        else:
            # login_window.withdraw()
            # self.wholeloginframe.loginframe.login_status_text.configure(text="Done", text_color="white")
            if self.username.lower() == "chef":
                self.wholeloginframe.place_forget()
                self.chefframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            else:
                self.wholeloginframe.place_forget()
                self.menuframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            

    def go_to_orders(self, event):
        #Clear the scrollable frame in orders.py as it was having multiple child frames inside it when returned to menu and proceeded
        for child in self.orderframe.order_frame.scrollable_frame.winfo_children(): child.destroy()
        
        #The item objects
        item_objects_stored = self.menuframe.menu_scrollable_frame.item_objects_stored
        items_quantity = [int(item_objects_stored[i].get()) for i in range(len(item_objects_stored))]
        item_menu_ids = self.menuframe.menu_scrollable_frame.items_data[0]
        items_quantity = dict(zip(item_menu_ids, items_quantity))
        self.ordered_items = {key:value for key, value in items_quantity.items() if value!=0}

        #Resets the optionmenu values to 0
        for i in item_objects_stored: i.set("0")
        
        # print(self.ordered_items)
        if self.ordered_items:
            self.menuframe.place_forget()
            self.orderframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            self.orderframe.order_frame.ordered_items_frame(self.ordered_items)
        else:
            print("No items")

    def go_to_order_status(self, event):
        orderid = orders_backend.generate_order_id(self.ordered_items)
        print(orderid)
        # print("Check orders")
        # query = "update orders set payment_status = 1 where orderid"
        self.orderframe.place_forget()
        self.orderstatusframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        try:
            self.orderstatusframe.order_number_text.set(f"ORDER NUMBER: {orderid.upper()}")
            self.orderstatusframe.table_number_text.set(f"TABLE NUMBER: {self.username.capitalize()}")
        except:
            self.orderstatusframe.table_number_text.set("TABLE NUMBER: Not Found")
        # print("Works")

    def go_to_menu_from_status(self, event):
        self.orderstatusframe.place_forget()
        self.menuframe.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    def star_color_change0(self, event):
        self.orderstatusframe.star0.configure(image = self.star)
        self.orderstatusframe.star1.configure(image = self.star_unselected)
        self.orderstatusframe.star2.configure(image = self.star_unselected)
        self.orderstatusframe.star3.configure(image = self.star_unselected)
        self.orderstatusframe.star4.configure(image = self.star_unselected)

    def star_color_change1(self, event):
        self.orderstatusframe.star0.configure(image = self.star)
        self.orderstatusframe.star1.configure(image = self.star)
        self.orderstatusframe.star2.configure(image = self.star_unselected)
        self.orderstatusframe.star3.configure(image = self.star_unselected)
        self.orderstatusframe.star4.configure(image = self.star_unselected)

    def star_color_change2(self, event):
        self.orderstatusframe.star0.configure(image = self.star)
        self.orderstatusframe.star1.configure(image = self.star)
        self.orderstatusframe.star2.configure(image = self.star)
        self.orderstatusframe.star3.configure(image = self.star_unselected)
        self.orderstatusframe.star4.configure(image = self.star_unselected)

    def star_color_change3(self, event):
        self.orderstatusframe.star0.configure(image = self.star)
        self.orderstatusframe.star1.configure(image = self.star)
        self.orderstatusframe.star2.configure(image = self.star)
        self.orderstatusframe.star3.configure(image = self.star)
        self.orderstatusframe.star4.configure(image = self.star_unselected)

    def star_color_change4(self, event):
        self.orderstatusframe.star0.configure(image = self.star)
        self.orderstatusframe.star1.configure(image = self.star)
        self.orderstatusframe.star2.configure(image = self.star)
        self.orderstatusframe.star3.configure(image = self.star)
        self.orderstatusframe.star4.configure(image = self.star)

        
Window("Restaurant Management System")