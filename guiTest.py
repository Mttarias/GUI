import tkinter as tk
import math

#Increments number by 1
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
    if int(lbl_value["text"]) >= cost:
        btn_auto['state'] = tk.NORMAL

#Recursive function that acts as an automatic incrementer
def autoIncrement():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
    window.after(1000, autoIncrement)
    if int(lbl_value["text"]) >= cost:
        btn_auto['state'] = tk.NORMAL
    
#Defines logic for auto increment button
def pay():
    global cost
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - cost}"
    window.after(1000, autoIncrement)
    btn_auto["state"] = tk.DISABLED
    cost = math.ceil(cost * 1.25)
    #Updates the display label for the increased cost
    lbl2.config(text=f"Cost: {cost}")

window = tk.Tk()
cost = 10

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

lbl2 = tk.Label(master=window, text=f"Cost: {cost}")
lbl2.grid(row=2, column=0)

btn_auto = tk.Button(master=window,
                        text="auto",
                        relief="groove",
                        command=pay,
                        state="disabled")
btn_auto.grid(row=3, column=0, sticky="nsew")


btn_increase = tk.Button(master=window,
                         text="+",
                         command=increase,
                         relief="groove")
btn_increase.grid(row=3, column=2, sticky="nsew")

window.mainloop()