import customtkinter as ctk
from pyglet import font

#fonts
font.add_file("Documents/Trip_Sans/TripSans-Medium.ttf")
loginfont = ('Trip Sans Medium',40)
entryfont = ('Trip Sans Medium',20)

#System Settings

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Window
app = ctk.CTk()
app.geometry("1280x720")
app.title("Frontend")
app.resizable(False, False)
app.lift()
app.attributes('-topmost',True)
app.after_idle(app.attributes,'-topmost',False)

#frame
ctk.CTkLabel(master=app, text="Hello", font=loginfont).pack()

#Run
app.mainloop()