import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
    if int(lbl_value["text"]) >= 10:
        btn_auto['state'] = tk.NORMAL
    
def autoIncrement():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
    window.after(1000, autoIncrement)
    if int(lbl_value["text"]) >= 10:
        btn_auto['state'] = tk.NORMAL
    
def pay():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 10}"
    window.after(1000, autoIncrement)
    btn_auto["state"] = tk.DISABLED

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

lbl2 = tk.Label(master=window, text="Cost 10")
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