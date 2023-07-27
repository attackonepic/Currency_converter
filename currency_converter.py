from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import requests
import json

# Initial window configuration
window = Tk()
window.geometry("400x200")
window.title("Currency Converter")
window.iconbitmap("moneda.ico")

# Manage API
api_request = requests.get("http://api.exchangeratesapi.io/v1/latest?access_key=43f0b90e97dbf540d408ce76e2be0b95&format=1")
api = json.loads(api_request.content)

# Functions
def convert():
	global api
	global api_request
	base = api["base"]
	fecha = api["date"]
	
	lbl_resultado.delete(0, END)
	currency = box_to.get()
	amount = float(ent_amount.get())
	pounds = float(api["rates"]["GBP"])
	dollar = float(api["rates"]["USD"])
	sek = float(api["rates"]["SEK"])
	nok = float(api["rates"]["NOK"])
	uyu = float(api["rates"]["UYU"])
	peso_arg = float(api["rates"]["ARS"])
	texto = f"The conversion is based on {base} \n from the date {fecha}"
	lbl_info = Label(frm_resultado, width=30, text=texto)

	if currency == monedas2[0]:
		resultado = amount * pounds
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	if currency == monedas2[1]:
		resultado = amount * dollar
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	if currency == monedas2[2]:
		resultado = amount * sek
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	if currency == monedas2[3]:
		resultado = amount * nok
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	if currency == monedas2[4]:
		resultado = amount * uyu
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	if currency == monedas2[5]:
		resultado = amount * peso_arg
		lbl_resultado.insert(0, "{:.2f}".format(resultado))
	 
	lbl_info.grid(row=2, column=1, columnspan=3, sticky="w", pady=(70, 0))

# Listas
monedas = ["Euros"]
monedas2 = ["Pounds", "US Dollar", "Swedish Crown", "Norwegian Crown", "Peso Uruguayo", "Peso Argentino"]

# Labels
lbl_from = Label(window, text="From", width=10, font="Helvetica 13")
lbl_to = Label(window, text="To", width=10, font="Helvetica 13")
frm_amount = LabelFrame(window, text="Amount")
frm_resultado = LabelFrame(window, text="Result")
lbl_resultado = Listbox(frm_resultado, width=30, height=2)

# Combobox
box_from = ttk.Combobox(values=monedas)
box_to = ttk.Combobox(values=monedas2)
box_from.set(monedas[0])
box_to.set(monedas2[3])

# Buttons
btn_convert = Button(frm_amount, text="Convert", command=convert)
btn_quit = Button(frm_amount, text="Quit", command=quit)

# Entries
ent_amount = Entry(frm_amount,text="Amount", width=30)

#Grid
frm_amount.grid(row=2, column=0, sticky="nsew", pady=20, padx=5)
frm_resultado.grid(row=2, column=1, sticky="nsew", pady=20, padx=5)
lbl_resultado.grid(row=2, column=1, pady=20)
lbl_from.grid(row=0, column=0)
lbl_to.grid(row=0, column=1)
box_from.grid(row=1, column=0, padx=5)
box_to.grid(row=1, column=1, padx=5)
ent_amount.grid(row=2, column=0, columnspan=3)
btn_convert.grid(row=4, column=0,  pady=(10, 0))
btn_quit.grid(row=4,column=1, pady=(10, 0))

window.mainloop()
