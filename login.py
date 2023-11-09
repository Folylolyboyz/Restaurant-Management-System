import customtkinter as ctk
from pyglet import font

from login_backend import *

#Font setup
login_font = ('Trip Sans Medium', 40)
entry_font = ('Trip Sans Medium', 20)

#Mode setup
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  #creating cutstom tkinter window
app.geometry("960x540")
app.title('Login')
app.resizable(False,False)
app.lift()
app.attributes('-topmost',True)
app.after_idle(app.attributes,'-topmost',False)


def login_button_function():
    username = username_entry.get()
    password = password_entry.get()
    status = openMenu(username, password)
    if status == 0:
        login_text.configure(text="Wrong username")
    elif status == -1:
        login_text.configure(text="Wrong password")
    else:
        login_text.configure(text="Done", text_color="white")
        #Configure going to menu here


#Login Frame
login_frame = ctk.CTkFrame(master=app, width=300, height=400, corner_radius=15)
login_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
login_frame.pack_propagate(0)

login_text = ctk.CTkLabel(master=login_frame, text="Log In",font=login_font)
# login_text.pack(padx=30, pady=(40,20), anchor="w")
login_text.pack(padx=30, pady=(40,20))

#Frame Widgets
username_entry=ctk.CTkEntry(master=login_frame, width=220, placeholder_text='Username', font=entry_font)
username_entry.pack(padx=30, pady=5)

password_entry=ctk.CTkEntry(master=login_frame, width=220, placeholder_text='Password', font=entry_font, show="*")
password_entry.pack(padx=30, pady=5)

login_button = ctk.CTkButton(master=login_frame, width=220, text="Login", font=entry_font, command=login_button_function, corner_radius=6)
login_button.pack(padx=30, pady=5)

login_text = ctk.CTkLabel(master=login_frame, text="", font=entry_font, text_color="red")
login_text.pack(padx=30, pady=5)

app.mainloop()