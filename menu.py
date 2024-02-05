import customtkinter as ctk
from PIL import Image

import menu_backend


class Menuframe(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=960, height=540)
        # self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        bg_image = Image.open("Documents\menu_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        self.menu_scrollable_frame = Menu_Scrollable_Frame(self)
        # self.menu_scrollable_frame._scrollbar.configure(width = 15)
        self.order_button = ctk.CTkButton(master=self, text="Order", width=156, height=54, font=('Trip Sans Bold', 28), bg_color="#F14A33", fg_color="#FFC700", hover_color="#FFC700", text_color="black", corner_radius=20)
        # self.order_button.pack(padx=(0,12), pady=(5,10), anchor="e")
        self.order_button.place(x = 693, y = 460)

class Menu_Scrollable_Frame(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent, width=515, height=420, scrollbar_button_color="black", fg_color="#F5D4B7", corner_radius=0)
        self.place(x = 50, y = 104)
        self.pack_propagate(0)
        # self.item_creator(0, 0, "abc", "100", "Documents/tempic.png")
        self.item_placer()

    def item_creator(self, r, item_name, item_price, item_image_path):
        # self.item_objects = []
        # item_frame = ctk.CTkFrame(self, width=420, height=300, fg_color="hotpink")
        item_frame = ctk.CTkFrame(self, width=500, height=126, fg_color="#FFF1E2")
        item_frame.pack_propagate(0)
        item_image = Image.open(item_image_path)
        item_image = ctk.CTkImage(item_image, size=(125, 125))
        ctk.CTkLabel(item_frame, text="", image=item_image).place(x = 35, y = 0)
        ctk.CTkLabel(item_frame, text=item_name, font=('Trip Sans Bold', 24)).place(x = 196, y = 8)
        ctk.CTkLabel(item_frame, text=item_price, font=('Trip Sans Medium', 20)).place(x = 196, y = 90)
        food_quantity_options = ["0", "1", "2", "3", "4", "5"]
        food_quantity_optionmenu = ctk.CTkOptionMenu(item_frame, values=food_quantity_options, anchor="center", width=80, height=25, font=('Trip Sans Medium', 15), dropdown_font=('Trip Sans Medium', 15))
        food_quantity_optionmenu.set("0")
        food_quantity_optionmenu.place(x = 400, y = 93)
        item_frame.grid(row=r, column=0, padx=10, pady=5)
        return food_quantity_optionmenu

    def item_placer(self):
        self.item_objects_stored = []
        self.items_data = (menu_backend.fetch_menu_items())
        item_menu_ids, item_name_list, item_price_list, item_image_list = self.items_data
        number_of_items = len(item_menu_ids)
        
        for rows in range(number_of_items):
            item_object = self.item_creator(rows, item_name_list[rows].capitalize(), item_price_list[rows], item_image_list[rows])
            self.item_objects_stored.append(item_object)