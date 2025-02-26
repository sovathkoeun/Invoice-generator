from tkinter import *


window = Tk()
window.title("My First GUI Program")

medicine_label = Label(text="Medicine:")
medicine_label.pack()

medicines = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 30,
    "Medicine D": 40
}

invoice_items = []

def add_medicine():
    selected_medicine = medicine_listbox.get(ANCHOR)
    quantity = int(quantity_entry.get())  # Convert to integer
    price = medicines[selected_medicine]  # Correctly get price
    item_total = price * quantity
    invoice_items.append((selected_medicine, quantity, price, item_total))
    quantity_entry.delete(0, END)  # Clear quantity entry after adding

def generate_invoice():
    total = sum(item[3] for item in invoice_items)
    customer_name = customer_entry.get()
    
    invoice_text.delete(1.0, END)  # Clear previous invoice
    invoice_text.insert(END, f"Customer: {customer_name}\n")
    invoice_text.insert(END, "==============================\n")
    for item in invoice_items:
        invoice_text.insert(END, 
            f"{item[0]} x {item[1]} @ ${item[2]} = ${item[3]}\n")
    invoice_text.insert(END, "==============================\n")
    invoice_text.insert(END, f"Total Amount: ${total}\n")
    
    total_amount_entry.delete(0, END)
    total_amount_entry.insert(0, str(total))

medicine_listbox = Listbox(window, selectmode="single")
for medicine in medicines:
    medicine_listbox.insert(END, medicine)
medicine_listbox.pack()

quantity_label = Label(text="Quantity:")
quantity_label.pack()
quantity_entry = Entry(window)  # Renamed for clarity
quantity_entry.pack()

add_button = Button(text="Add Medicine", command=add_medicine)
add_button.pack()

total_amount_label = Label(text="Total Amount:")
total_amount_label.pack()
total_amount_entry = Entry(window)
total_amount_entry.pack()

customer_label = Label(text="Customer Name:")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoice", command=generate_invoice)
generate_button.pack()

invoice_text = Text(window, width=40, height=10)
invoice_text.pack()

window.mainloop()