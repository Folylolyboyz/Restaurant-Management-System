import customtkinter as ctk

class Loginframe(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=400, corner_radius=15)
        self.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.pack_propagate(0)
        self.create_widgets()

    def create_widgets(self):
        login_text = ctk.CTkLabel(master=self,text="Log In",font=('Trip Sans Medium', 40))
        login_text.pack(padx=30, pady=(40,20))
        self.username_entry=ctk.CTkEntry(master=self, width=220, placeholder_text='Username', font=('Trip Sans Medium', 20))
        self.password_entry=ctk.CTkEntry(master=self, width=220, placeholder_text='Password', font=('Trip Sans Medium', 20), show="*")
        self.login_status_text = ctk.CTkLabel(master=self, text="", font=('Trip Sans Medium', 20))
        self.login_button = ctk.CTkButton(master=self, width=220, text="Login", font=('Trip Sans Medium', 20), corner_radius=6)

        self.username_entry.pack(padx=30, pady=5)
        self.password_entry.pack(padx=30, pady=5)
        self.login_button.pack(padx=30, pady=5)
        self.login_status_text.pack(padx=30, pady=5)