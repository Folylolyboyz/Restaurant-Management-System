import customtkinter as ctk

import login, login_backend
import menu, menu_backend
# import orders, orders_backend

class Window(ctk.CTk):
    def __init__(self, title):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        super().__init__()
        self.geometry("960x540")
        self.title(title)
        self.resizable(False,False)
        
        self.loginframe = login.Loginframe(self)
        self.loginframe.login_button.bind("<Button-1>", self.go_to_menu)
        
        self.mainloop()

    def go_to_menu(self, event):
        username = self.loginframe.username_entry.get()
        password = self.loginframe.password_entry.get()
        status = login_backend.openMenu(username, password)
        if status == 0:
            self.loginframe.login_status_text.configure(text="Wrong username", text_color="red")
        elif status == -1:
            self.loginframe.login_status_text.configure(text="Wrong password", text_color="red")
        else:
            # login_window.withdraw()
            self.loginframe.login_status_text.configure(text="Done", text_color="white")

Window("Restaurant Management System")