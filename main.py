from tkinter import *


window = Tk()
window.title("My First GUI Program")

medicine_label = Label(text="Medicine:")
medicine_label.pack()


medicine_listbox = Listbox(window, selectmode="single")
medicine_listbox.pack()

quantity_label = Label(text="Quantity:")
quantity_label.pack()
quantity_label = Entry(window)
quantity_label.pack()

add_button = Button(text="Add", command=lambda: medicine_listbox.insert(END, quantity_label.get()))
add_button.pack()

total_amount_label = Label(text="Total Amount:")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(text="Customer Name:")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoice")

invoice_text = Text(window, width=40, height=10)
invoice_text.pack()


window.mainloop()