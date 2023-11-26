import customtkinter as ctk
from PIL import Image

import orders_backend

class OrderFrame(ctk.CTkFrame):
    def __init__(self, window):
        super().__init__(window, width=960, height=540)

        bg_image = Image.open("Documents\orders_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)

        # mainframe config
        self.frame_config()
        self.create_widgets()

        # sub total for total order
        self.sub_total = 0
        
        # left side orders frame
        self.order_frame = Ordered_Items_Frame(self)

    def frame_config(self):
        self.configure(width=960, height=540)
        self.grid_propagate(0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # row and column configure
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

    def create_widgets(self):
        self.pay_button = ctk.CTkButton(self, text="Pay", width=261, height=45, font=('Trip Sans Bold', 28), bg_color="#F14A33", fg_color="#FFC700", hover_color="#FFC700", text_color="black", corner_radius=20)
        self.pay_button.place(x = 626, y = 430)        

# right side payment frame
class Payment_Frame(ctk.CTkFrame):
    def __init__(self, parent, total_amount):
        self.total_amount = total_amount
        super().__init__(parent, width=261, height=314, fg_color="#FFF1E2")
        self.place(x = 626, y = 101)
        self.create_widgets()

    def create_widgets(self):
        payment_label = ctk.CTkLabel(self, text="PAYMENT", font=('Trip Sans Bold', 32))
        payment_label.place(x = 63, y = 20)
        service_charge = 10
        tax_charge = 10
        ctk.CTkLabel(self, text="Total Amount", font=('Trip Sans Bold', 16)).place(x = 142, y = 80)
        ctk.CTkLabel(self, text=f"₹{self.total_amount}.00", font=('Bahnschrift SemiLight', 18), width=238, height=20, anchor="e").place(x = 0, y = 101)
        ctk.CTkLabel(self, text="Service Charges", font=('Trip Sans Bold', 16)).place(x = 120, y = 119)
        ctk.CTkLabel(self, text=f"₹{service_charge}.00", font=('Bahnschrift SemiLight', 18), width=238, height=20, anchor="e").place(x = 0, y = 143)
        ctk.CTkLabel(self, text="Tax Charges", font=('Trip Sans Bold', 16)).place(x = 148, y = 161)
        ctk.CTkLabel(self, text=f"₹{tax_charge}.00", font=('Bahnschrift SemiLight', 18), width=238, height=20, anchor="e").place(x = 0, y = 185)
        ctk.CTkLabel(self, text="Total Payable Amount", font=('Trip Sans Bold', 17)).place(x = 72, y = 244)
        total = self.total_amount + service_charge + tax_charge
        ctk.CTkLabel(self, text=f"₹{total}.00", font=('Bahnschrift SemiLight', 18), width=238, height=20, anchor="e").place(x = 0, y = 268)
      
# left order frame
class Ordered_Items_Frame(ctk.CTkFrame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(parent, width=536, height=374, fg_color="#EEC0AA", corner_radius=0)
        self.place(x = 73, y = 101)
        
        ordered_items_label = ctk.CTkLabel(self, text="ORDERED ITEMS", font=('Trip Sans Bold', 32))
        ordered_items_label.place(x = 154, y = 19)
        
        # order details frame inside order mainframe
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=494, height=290, bg_color="transparent", fg_color="transparent")
        self.scrollable_frame.place(x = 10, y = 71)
        self.scrollable_frame._scrollbar.configure(width = 16)
        self.pack_propagate(0)
        # self.ordered_items_frame({"menu1": 1, "menu2":2, "menu3":3})

    def ordered_items_frame(self, ordered_items):
        food_item_list = []
        food_quantity_list = []
        food_price_list = []
        total_amount = 0

        # ordered food details
        ordered_items_list = list(ordered_items.items())
        for i in ordered_items_list:
            name, price = orders_backend.fetch_name_price(str(i[0]))
            food_item_list.append(name.capitalize())
            food_quantity_list.append(int(i[1]))
            food_price_list.append(int(price))

        number_of_items = len(food_item_list)
        
        for i in range(number_of_items):
            total_amount += food_price_list[i] * food_quantity_list[i]
        
        for i in range(number_of_items):
            self.ordered_item_creater(food_item_list[i], food_quantity_list[i], food_price_list[i])

        self.payment_frame = Payment_Frame(self.parent, total_amount)
    
    def ordered_item_creater(self, item, quantity, price):
        item_frame = ctk.CTkFrame(self.scrollable_frame, width=490, height=100, fg_color="#FFF1E2", corner_radius=20)
        ctk.CTkLabel(item_frame, text=item, font=('Trip Sans Bold', 20), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 19, y = 24)
        ctk.CTkLabel(item_frame, text=f"Quantity: {quantity}", font=('Bahnschrift SemiLight', 20), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 19, y = 50)
        ctk.CTkLabel(item_frame, text=f"₹{price}.00", font=('Bahnschrift SemiLight', 20), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 400, y = 35)
        item_frame.pack_propagate(0)
        item_frame.pack(padx = 0, pady = 5)