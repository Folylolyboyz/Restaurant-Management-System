import customtkinter as ctk
from PIL import Image

class Login_frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=460, height=540, bg_color="white", fg_color="white")
        # self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        login_text = ctk.CTkLabel(master=self,text="Login",font=('Trip Sans Bold', 40))
        # login_text.pack(padx=30, pady=(40,20))
        line = ctk.CTkCanvas(master=self, width=198, height=3, bg = "white", highlightthickness = 0)
        line.create_line((0,2,198,2),fill="black",width=2)
        username_text = ctk.CTkLabel(master=self,text="Username", font=('Trip Sans Medium', 20))
        self.username_entry=ctk.CTkEntry(master=self, width=355 , height=44, font=('Trip Sans Medium', 20), corner_radius=10, border_color="black" , bg_color="white", fg_color="white")
        password_text = ctk.CTkLabel(master=self,text="Password", font=('Trip Sans Medium', 20))
        self.password_entry=ctk.CTkEntry(master=self, width=355, height=44, font=('Trip Sans Medium', 20), show="•", corner_radius=10, border_color="black" , bg_color="white", fg_color="white")
        self.login_status_text = ctk.CTkLabel(master=self, text="", font=('Trip Sans Medium', 20))
        self.login_button = ctk.CTkButton(master=self, width=170, height=44, text="LOG IN", font=('Trip Sans Medium', 20), corner_radius=20, fg_color="#2860F0", text_color="white")

        #-15 to make it okay  -15+ for line
        login_text.place(x = 179, y = 83)
        line.place(x = 131, y = 145)
        username_text.place(x = 62, y = 194)
        self.username_entry.place(x = 52, y = 219)
        password_text.place(x = 62, y = 285)
        self.password_entry.place(x = 52, y = 310)
        self.login_button.place(x = 144, y = 399)

class Login_Frame_Background(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=500, height=540)
        bg_image = Image.open("Documents\login_background1.png")
        bg_image = ctk.CTkImage(bg_image, size = (500,540))
        ctk.CTkLabel(self, text="", image = bg_image).place(relx = 0, rely = 0)

class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=960, height=540)
        self.loginframe = Login_frame(self)
        self.login_frame_background = Login_Frame_Background(self)

        self.loginframe.grid(row = 0, column = 1)
        self.login_frame_background.grid(row = 0, column = 0)
        self.place(x=0,y=0)