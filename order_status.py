import customtkinter as ctk
from PIL import Image
from datetime import date
        
class OrderStatusFrame(ctk.CTkFrame):
    def __init__(self,window):
        super().__init__(window, width=960, height=540)
        self.grid_propagate(0)
        
        # font config
        self.ffont = ('Trip Sans Bold', 40)
        self.ffont1 = ('Trip Sans Medium', 20)
        self.ffont2 = ('Trip Sans Medium', 16)
        self.status_frame_config()

        #call create_widgets from backend with the order number
        self.create_widgets()

    def create_widgets(self):
        self.order_number_text = ctk.StringVar()
        self.order_number_text.set("ORDER NUMBER: OD26231")
        self.table_number_text = ctk.StringVar()
        self.table_number_text.set("TABLE NUMBER: 1")
        date_today = date.today()
        date_today = date_today.strftime("%d/%m/%Y")
        
        ctk.CTkLabel(self, textvariable=self.order_number_text, font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 82, y = 111)
        ctk.CTkLabel(self, textvariable=self.table_number_text, font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 400, y = 111)
        ctk.CTkLabel(self, text=f"DATE: {date_today}", font=('Trip Sans Medium', 24), fg_color="#FFF1E2", bg_color="#FFF1E2").place(x = 690, y = 111)
        ctk.CTkLabel(self, text="GIVE US FEEDBACK: ", font=('Trip Sans Medium', 20), fg_color="white", bg_color="white").place(x = 551, y = 506)

        self.return_to_menu = ctk.CTkLabel(self, text="Return to Menu", font=('Trip Sans Medium', 20), text_color="black", fg_color="white", bg_color="white")
        self.return_to_menu.place(x = 46, y = 505)
        
        star = Image.open("Documents/rating_star_selected.png")
        star_unselected = Image.open("Documents/rating_star_unselected.png")
        star = ctk.CTkImage(star, size = (35,35))
        star_unselected = ctk.CTkImage(star_unselected, size = (35,35))
        self.star0 = ctk.CTkLabel(self, text="", fg_color="white", bg_color="white", image = star_unselected)
        self.star1 = ctk.CTkLabel(self, text="", fg_color="white", bg_color="white", image = star_unselected)
        self.star2 = ctk.CTkLabel(self, text="", fg_color="white", bg_color="white", image = star_unselected)
        self.star3 = ctk.CTkLabel(self, text="", fg_color="white", bg_color="white", image = star_unselected)
        self.star4 = ctk.CTkLabel(self, text="", fg_color="white", bg_color="white", image = star_unselected)
        
        self.star0.place(x = 735, y = 501)
        self.star1.place(x = 780, y = 501)
        self.star2.place(x = 825, y = 501)
        self.star3.place(x = 870, y = 501)
        self.star4.place(x = 915, y = 501)
    
    # main frame configure
    def status_frame_config(self):
        # self.configure(width= 960, height = 540)
        bg_image = Image.open("Documents/order_status_background.png")
        bg_image = ctk.CTkImage(bg_image, size = (960,540))
        menu_text = ctk.CTkLabel(master=self, text="", image = bg_image)
        menu_text.place(relx = 0, rely = 0)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        