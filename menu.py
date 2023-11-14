import customtkinter as ctk
from PIL import Image

import menu_backend


class Menuframe(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=720, height=400, corner_radius=15)
        # self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        menu_text = ctk.CTkLabel(master=self, text="Menu",font=('Trip Sans Medium', 40))
        menu_text.pack()
        self.menu_scrollable_frame = Menu_Scrollable_Frame(self)
        self.order_button = ctk.CTkButton(master=self, text="Order", width=60, height=40, font=('Trip Sans Medium', 20))
        self.order_button.pack(padx=(0,12), pady=(5,10), anchor="e")

class Menu_Scrollable_Frame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, width=720, height=280, fg_color="transparent")
        self.pack()
        # self.item_creator(0, 0, "abc", "100", "Documents/tempic.png")
        self.item_placer(5)

    def item_creator(self, r, c, item_name, item_price, item_image_path):
        self.item_objects = []
        item_frame = ctk.CTkFrame(self, width=420, height=300, fg_color="hotpink")
        item_image = Image.open(item_image_path)
        item_image = ctk.CTkImage(item_image, size=(120,120))
        ctk.CTkLabel(item_frame, text="", image=item_image).pack()
        ctk.CTkLabel(item_frame, text=item_name, font=('Trip Sans Medium', 20)).pack()
        ctk.CTkLabel(item_frame, text=item_price, font=('Trip Sans Medium', 20)).pack()
        food_quantity_options = ["0", "1", "2", "3", "4", "5"]
        food_quantity_optionmenu = ctk.CTkOptionMenu(item_frame, values=food_quantity_options, anchor="center", width=0, height=25, font=('Trip Sans Medium', 15), dropdown_font=('Trip Sans Medium', 15))
        food_quantity_optionmenu.set("0")
        food_quantity_optionmenu.pack(padx=5, pady=(0,5), fill="x")
        item_frame.grid(row=r, column=c, padx=10, pady=10)
        return food_quantity_optionmenu

    def item_placer(self, items_in_row):
        self.item_objects_stored = []
        self.items_data = (menu_backend.fetch_menu_items())
        item_menu_ids, item_name_list, item_price_list, item_image_list = self.items_data
        number_of_items = len(item_menu_ids)
        temp = number_of_items
        counter = 0
        
        for rows in range(number_of_items):
            n = items_in_row

            if temp < items_in_row:
                n = temp

            for column in range(n):
                item_object = self.item_creator(rows, column, item_name_list[counter], item_price_list[counter], item_image_list[counter])
                self.item_objects_stored.append(item_object)
                counter += 1

            temp -= items_in_row