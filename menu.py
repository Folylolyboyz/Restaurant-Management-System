import customtkinter as ctk
from PIL import Image
from pyglet import font

import menu_backend
import orders_backend

#Fonts
font.add_file("Documents/Trip_Sans/TripSans-Medium.ttf")
font.add_file("Documents/Trip_Sans/TripSans-Bold.ttf")
ffont=('Trip Sans Bold',40)
ffont1=('Trip Sans Medium',20)
ffont2=('Trip Sans Medium',15)

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = ctk.CTk()  #creating cutstom tkinter window
app.geometry("960x540")
app.title('Table')
app.resizable(False,False)
app.lift()
app.attributes('-topmost',True)
app.after_idle(app.attributes,'-topmost',False)

#Frame
menu_frame=ctk.CTkFrame(master=app, width=720, height=400)
menu_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
menu_frame.pack_propagate(0)

#Menu label
menu_label=ctk.CTkLabel(master = menu_frame, width=300, text="Menu", font=ffont)
menu_label.pack(padx=0, pady=0)

#scrollable menu_frame
menu_scrollable_frame=ctk.CTkScrollableFrame(master=menu_frame, width=720, height=280, fg_color="transparent")
menu_scrollable_frame.pack()

# #frame2 config not needed as of now
# frame2=ctk.CTkFrame(master=menu_scrollable_frame, width=420, height=300, fg_color="#FFFDD0")
# frame2.pack()

#itemCreator config
def itemCreator(r, c, itemname, itemprice, imagepath):
    itemCreatorFrame=ctk.CTkFrame(master=menu_scrollable_frame, width=420, height=300, fg_color="hotpink")
    imageFile=Image.open(imagepath)
    tempic = ctk.CTkImage(light_image=imageFile, size=(120,120))
    tempicl = ctk.CTkLabel(master=itemCreatorFrame, text="", image=tempic)
    tempicl.pack()
    ctk.CTkLabel(master=itemCreatorFrame, text=itemname, font=ffont1).pack()
    ctk.CTkLabel(master=itemCreatorFrame, text=itemprice, font=ffont1).pack()
    foodQuantityValues = ["0", "1", "2", "3", "4", "5"]
    foodQuantityMenu = ctk.CTkOptionMenu(master=itemCreatorFrame, values=foodQuantityValues, width=0, height=25, font=ffont2, dropdown_font=ffont2, anchor="center")
    foodQuantityMenu.set("0")
    foodQuantityMenu.pack(padx=5, pady=(0,5), fill="x")
    itemCreatorFrame.grid(row=r, column=c, padx=10, pady=10)
    return foodQuantityMenu

item_data = (menu_backend.fetch_menu_items())

#items
menu_id_list = item_data[0]
item_names = item_data[1]
item_prices=item_data[2]
image_path=item_data[3]

# item_names=["f1", "f2", "f3", "f4"]
# item_prices=["10", "10", "10", "10"]
# image_path=["Documents/tempic.png", "Documents/tempic.png", "Documents/tempic.png", "Documents/tempic.png"]

items=[]
def item_placer(items_in_row: int):
    item_length = len(item_names)
    t=item_length
    i=0
    for r in range(len(item_names)):
        if t<items_in_row:
            n=t
        else:
            n=items_in_row
        for c in range(n):
            option=itemCreator(r, c, item_names[i], item_prices[i], image_path[i])
            items.append(option)
            i+=1
        t-=items_in_row
item_placer(4)

#order button
item_length=len(items)

def orderfunction():
    item_quantity = [int(items[i].get()) for i in range(item_length)]
    item_quantity = dict(zip(menu_id_list, item_quantity))
    ordered_items = {key:value for key, value in item_quantity.items() if value!=0} #returns menuid and quantity {'menu1': 1, 'menu2' : 2}
    return orders_backend.generate_order_id(ordered_items) if ordered_items else print("No items")

order_button = ctk.CTkButton(master=menu_frame, text="Order", width=60, height=40, font=ffont1, command=orderfunction)
order_button.pack(padx=(0,12), pady=(5,10), anchor="e")


app.mainloop()