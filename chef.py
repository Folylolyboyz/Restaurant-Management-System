import customtkinter as ctk
import tkinter 
from PIL import Image
from datetime import date
import time
import chef_backend
        
class ChefFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window, width=960, height=540)
        
        self.status_frame_config()
    
    def checked_box(self):
        ord_no = 23
        print(f"pressed order no: {ord_no}")

        
    # main frame configure
    def status_frame_config(self):
        # self.configure(width= 960, height = 540)
        bg_image = Image.open("Documents/chef_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        # self.completed_order_frame = Completed_Order_Frame(self)
        # self.completed_order_frame.place(x = 626, y = 101)
        self.pending_order_frame = Pending_Order_Frame(self)
        self.pending_order_frame.place(x = 81, y = 101)

        # for child in pending_order_frame.scrl.winfo_children(): print(child)
        # pending_order_frame.pending_item_placer(chef_backend.pending_order_items())

        # for child in completed_order_frame.scrl.winfo_children(): print(child)
        # completed_order_frame.completed_item_placer(chef_backend.completed_order_items())

    # def checkbox_command_to_reset(self, orderid):
    #     for child in self.scrl.winfo_children(): child.destroy()

class Completed_Order_Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=261, height=383, fg_color="#EEC0AA", bg_color="#EEC0AA", corner_radius=0)
        self.pack_propagate(0)
        title_label = ctk.CTkLabel(self, text="COMPLETED\nORDERS", width=261, height=55, font=('Trip Sans Bold', 32))
        title_label.place(x = 0, y = 19)
        self.scrl = ctk.CTkScrollableFrame(self, width=230, height=250, corner_radius=0)
        self.scrl._scrollbar.configure(width=16)
        self.scrl.place(x = 10, y = 120)
        self.completed_item_placer(chef_backend.completed_order_items())

    def completed_item_placer(self, completed_order_list: list):
        for orderid in completed_order_list:
            self.completed_item_creator(orderid)

    def completed_item_creator(self, orderid):
        item_frame = ctk.CTkFrame(self.scrl, height=30, fg_color="#FFF1E2")
        item_frame.pack_propagate(0)
        ctk.CTkLabel(item_frame, text=f"{orderid.upper()}", font=('Trip Sans Bold', 20)).pack()
        item_frame.pack(pady = (5,0))
        

class Pending_Order_Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=536, height=383, fg_color="#EEC0AA", corner_radius=0)
        self.pack_propagate(0)
        title_label = ctk.CTkLabel(self, text="PENDING ORDERS", width=280, height=30, font=('Trip Sans Bold', 32))
        title_label.place(x = 150, y = 19)
        self.scrl = ctk.CTkScrollableFrame(self, width=494, height=293, corner_radius=0)
        self.scrl._scrollbar.configure(width=16)
        self.scrl.place(x = 10, y = 78)

        self.pending_item_placer(chef_backend.pending_order_items())

        self.completed_order_frame = Completed_Order_Frame(parent)
        self.completed_order_frame.place(x = 626, y = 101)
        
        # self.pending_item_creator("OD12", 1, {'burger': 1, 'sandwich': 2})
        

    def pending_item_placer(self, pending_order_dictionary: dict):
        # self.item_objects_stored = {}
        for orderid in pending_order_dictionary:
            item_object = self.pending_item_creator(orderid, 1, pending_order_dictionary[orderid])
            # self.item_objects_stored[item_object[0]] = item_object[1]
            

    def pending_item_creator(self, orderid, tableid, items):
        item_frame = ctk.CTkFrame(self.scrl, width=480, fg_color="#FFF1E2")
        # item_frame.pack_propagate(0)

        upper_row = ctk.CTkFrame(item_frame, width=470, height=30, fg_color="#FFF1E2", corner_radius=0)
        upper_row.pack_propagate(0)
        upper_row.pack(pady = 5)

        order_checkbox = ctk.CTkCheckBox(upper_row, text="", width=25, height=25, command=lambda:self.update_orders(orderid))
        order_label = ctk.CTkLabel(upper_row, text=f"Order: {orderid.upper()}", font=('Trip Sans Bold', 20))
        table_label = ctk.CTkLabel(upper_row, text=f"Table: {tableid}", font=('Trip Sans Bold', 20))

        order_checkbox.pack(side="left", expand = True)
        order_label.pack(side="left", expand = True)
        table_label.pack(side="left", expand = True)
        for i in items:
            food_label = f"{items[i]} X {i.capitalize()}"
            ctk.CTkLabel(item_frame, text=food_label, font=('Trip Sans Medium', 16)).pack(padx=0)

        item_frame.pack(pady = 5)

        return orderid, order_checkbox

    def update_orders(self, orderid):
        chef_backend.update_to_complete(orderid)
        for child in self.scrl.winfo_children():
            child.destroy()

        for child in self.completed_order_frame.scrl.winfo_children():
            child.destroy()
        self.pending_item_placer(chef_backend.pending_order_items())
        self.completed_order_frame.completed_item_placer(chef_backend.completed_order_items())
        
        
        
        

# class Window(ctk.CTk):
#     def __init__(self, title):
#         ctk.set_appearance_mode("light")
#         ctk.set_default_color_theme("blue")
        
#         super().__init__()
#         self.geometry("960x540")
#         self.title(title)
#         self.resizable(False,False)

        
#         ChefFrame(self)
#         self.mainloop()

# Window("Chef Status")