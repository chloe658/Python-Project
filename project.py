from tkinter import *
from tkinter import messagebox


class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self, parent):

        # Variables
        self.name_var = StringVar()
        self.price_var = StringVar()
        self.stock_var = StringVar()
        self.items = []
        self.display_option_var = StringVar()
        WD1 = 15
        WD2 = 25
        BGCOLOUR = "light blue"

        self.input_frame = Frame(parent, bg=BGCOLOUR)
        self.input_frame.grid()
        self.output_frame = Frame(parent, bg=BGCOLOUR)
        self.edit_frame = Frame(parent, bg=BGCOLOUR)

        # Input widgets
        self.input_label = Label(self.input_frame, text="Add Information", width=WD1, bg=BGCOLOUR)
        self.input_output_btn = Button(self.input_frame, text="Display Information", command=self.display_information, width=WD1, state="disabled")
        self.edit_item_btn = Button(self.input_frame, text="Edit Existing Item", command=self.input_edit, width=WD1, state="disabled")
        self.input_label.grid(row=0, column=0)
        self.input_output_btn.grid(row=0, column=1)
        self.edit_item_btn.grid(row=1, column=1)
        self.name_label = Label(self.input_frame, text="Item Name:", width=WD1, bg=BGCOLOUR)
        self.name_entry = Entry(self.input_frame, textvariable=self.name_var, width=WD1)
        self.name_label.grid(row=2, column=0)
        self.name_entry.grid(row=2, column=1)
        self.price_label = Label(self.input_frame, text="Item Price:", width=WD1, bg=BGCOLOUR)
        self.price_entry = Entry(self.input_frame, textvariable=self.price_var, width=WD1)
        self.price_label.grid(row=3, column=0)
        self.price_entry.grid(row=3, column=1)
        self.stock_label = Label(self.input_frame, text="Item Stock:", width=WD1, bg=BGCOLOUR)
        self.stock_entry = Entry(self.input_frame, textvariable=self.stock_var, width=WD1)
        self.stock_label.grid(row=4, column=0)
        self.stock_entry.grid(row=4, column=1)
        self.enter_data = Button(self.input_frame, text="Enter Data", command=self.save_data, width=WD1)
        self.enter_data.grid(row=5, columnspan=2)

        # Output widgets
        self.output_label = Label(self.output_frame, text="Display Information", width=WD1, bg=BGCOLOUR)
        self.output_label.grid(row=0, column=0)
        self.output_input_btn = Button(self.output_frame, text="Add Information", command=self.add_information, width=WD1)
        self.output_input_btn.grid(row=0, column=1)
        self.search_btn = Button(self.output_frame, text="Search", command=self.search_item, width=WD1)
        self.search_btn.grid(row=1, column=1)
        self.name_label_output = Label(self.output_frame, text="Name: No name entered", width=WD2, bg=BGCOLOUR)
        self.name_label_output.grid(row=2, columnspan=2)
        self.price_label_output = Label(self.output_frame, text="Price: No price entered", width=WD2, bg=BGCOLOUR)
        self.price_label_output.grid(row=3, columnspan=2)
        self.stock_label_output = Label(self.output_frame, text="Stock: No stock entered", width=WD2, bg=BGCOLOUR)
        self.stock_label_output.grid(row=4, columnspan=2)

        # Edit widgets
        self.output_label = Label(self.edit_frame, text="Display Information", width=WD1, bg=BGCOLOUR)
        self.output_label.grid(row=0, column=0)
        self.output_input_btn = Button(self.edit_frame, text="Add Information", command=self.add_information, width=WD1)
        self.output_input_btn.grid(row=0, column=1)
        # edit_option.grid(row=1, column=0)
        number_label = Label(self.edit_frame, text="Number: ", width=WD1, bg=BGCOLOUR)
        number_label.grid(row=2, column=0)
        number_entry = Entry(self.edit_frame, text="Display Information", width=WD1, bg=BGCOLOUR)
        number_entry.grid(row=2, column=1)
        sell_btn = Button(self.edit_frame, text="Sell", command=self.sell_item, width=WD1)
        sell_btn.grid(row=3, column=0)
        restock_btn = Button(self.edit_frame, text="Restock", command=self.restock_item, width=WD1)
        restock_btn.grid(row=3, column=1)
    
    def sell_item(self):
        pass

    def restock_item(self):
        pass


    def save_data(self):
        name = self.name_var.get()
        price = self.price_var.get()
        stock = self.stock_var.get()

        if name == "":
            messagebox.showerror("Error", "Please enter a name.")
            self.name_entry.delete(0, END)
            self.name_entry.focus()

        else:
            try:
                float(price)
                int(stock)
                self.items.append(Item(name, price, stock))
                self.name_entry.delete(0, END)
                self.price_entry.delete(0, END)
                self.stock_entry.delete(0, END)
                self.name_entry.focus
                self.input_output_btn.configure(state="normal")
                self.edit_item_btn.configure(state="normal")
            except ValueError:
                messagebox.showerror("Error", "Please enter an integer.")
                # shows 2 error messages at one, one for price and one for stock.
                # fixed by having one error message for boh but i cant delete of focus because it could be either.

    def search_item(self):
        for i in range(len(self.items)):
            item = self.items[i]
            if item.name == self.display_option_var.get():
                self.name_label_output.configure(text="Name: " + item.name)
                self.price_label_output.configure(text="Price: " + item.price)
                self.stock_label_output.configure(text="Stock: " + item.stock)
    
    def input_edit(self):
        self.input_frame.grid_forget()
        self.edit_frame.grid()
        # find way to initiate with other widgets because why it it here
        self.edit_option = OptionMenu(self.edit_frame, self.display_option_var, *self.item_names)
        self.edit_option.grid(row=1, column=0)

    def display_information(self):
        self.input_frame.grid_forget()
        self.edit_frame.grid_forget()
        self.output_frame.grid()

        self.item_names = [item.name for item in self.items]
        self.display_option_var.set("Select an item")

        # find way to initiate with other widgets because why it it here
        display_option = OptionMenu(self.output_frame, self.display_option_var, *self.item_names)
        display_option.grid(row=1, column=0)

    def add_information(self):
        self.output_frame.grid_forget()
        self.edit_frame.grid_forget()
        self.input_frame.grid()


if __name__ == "__main__":
    root = Tk()
    start = Inventory(root)
    root.title("Shop")
    root.mainloop()
