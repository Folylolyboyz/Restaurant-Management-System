import customtkinter as ctk
from pyglet import font
from login_backend import *

#Font setup
login_font = ('Trip Sans Medium', 40)
entry_font = ('Trip Sans Medium', 20)

def login_start():
    #Mode setup
    #Modes: system (default), light, dark
    ctk.set_appearance_mode("dark")
    
    # Themes: blue (default), dark-blue, green
    ctk.set_default_color_theme("blue")

    main_window = ctk.CTk()
    main_window.geometry("960x540")
    main_window.title('Login')
    main_window.resizable(False,False)
    main_window.lift()
    main_window.attributes('-topmost',True)
    main_window.after_idle(main_window.attributes,'-topmost',False)

    #Login Frame
    login_frame = ctk.CTkFrame(master=main_window, width=300, height=400, corner_radius=15)
    login_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    login_frame.pack_propagate(0)

    login_text = ctk.CTkLabel(master=login_frame, text="Log In",font=login_font)
    # login_text.pack(padx=30, pady=(40,20), anchor="w")
    login_text.pack(padx=30, pady=(40,20))

    #Frame Widgets
    username_entry=ctk.CTkEntry(master=login_frame, width=220, placeholder_text='Username', font=entry_font)
    password_entry=ctk.CTkEntry(master=login_frame, width=220, placeholder_text='Password', font=entry_font, show="*")
    login_text = ctk.CTkLabel(master=login_frame, text="", font=entry_font)
    login_button = ctk.CTkButton(master=login_frame, width=220, text="Login", font=entry_font, command=lambda: login_button_function(username_entry, password_entry, login_text), corner_radius=6)

    #Widget Pack
    username_entry.pack(padx=30, pady=5)
    password_entry.pack(padx=30, pady=5)
    login_button.pack(padx=30, pady=5)
    login_text.pack(padx=30, pady=5)

    
    main_window.mainloop()