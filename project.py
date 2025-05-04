from tkinter import *
from tkinter import messagebox


class Item:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


class Inventory:
    def __init__(self, parent):
        
        self.input_frame = Frame(parent)
        self.input_frame.grid()
        self.output_frame = Frame(parent)
        
        # Variables
        self.name_var = StringVar()
        self.price_var = StringVar()
        self.stock_var = StringVar()
        self.items = []
        self.display_option_var = StringVar()
        WD = 15
        WD2 = 25

        # Input widgets
        self.input_label = Label(self.input_frame, text="Add Information", width=WD)
        self.input_output_btn = Button(self.input_frame, text="Display Information", command=self.display_information, width=WD)
        self.input_label.grid(row=0, column=0)
        self.input_output_btn.grid(row=0, column=1)
        self.name_label = Label(self.input_frame, text="Item Name:", width=WD)
        self.name_entry = Entry(self.input_frame, textvariable=self.name_var, width=WD)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.price_label = Label(self.input_frame, text="Item Price:", width=WD)
        self.price_entry = Entry(self.input_frame, textvariable=self.price_var, width=WD)
        self.price_label.grid(row=2, column=0)
        self.price_entry.grid(row=2, column=1)
        self.stock_label = Label(self.input_frame, text="Item Stock:", width=WD)
        self.stock_entry = Entry(self.input_frame, textvariable=self.stock_var, width=WD)
        self.stock_label.grid(row=3, column=0)
        self.stock_entry.grid(row=3, column=1)
        self.enter_data = Button(self.input_frame, text="Enter Data", command=self.save_data, width=WD)
        self.enter_data.grid(row=4, columnspan=2)

        # Output widgets
        self.output_label = Label(self.output_frame, text="Display Information", width=WD)
        self.output_label.grid(row=0, column=0)
        self.output_input_btn = Button(self.output_frame, text="Add Information", command=self.add_information, width=WD)
        self.output_input_btn.grid(row=0, column=1)
        self.search_btn = Button(self.output_frame, text="Search", command=self.search_item, width=WD)
        self.search_btn.grid(row=1, column=1)
       
        self.name_label_output = Label(self.output_frame, text="Name: No name entered", width=WD2)
        self.name_label_output.grid(row=2, columnspan=2)
        self.price_label_output = Label(self.output_frame, text="Price: No price entered", width=WD2)
        self.price_label_output.grid(row=3, columnspan=2)
        self.stock_label_output = Label(self.output_frame, text="Stock: No stock entered", width=WD2)
        self.stock_label_output.grid(row=4, columnspan=2)

    def save_data(self):
        name = self.name_var.get()
        price = self.price_var.get()
        stock = self.stock_var.get()

        self.items.append(Item(name, price, stock))
        self.name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.stock_entry.delete(0, END)
        self.name_entry.focus()

    def search_item(self):
        #if self.items[0].name == self.display_option_var.get():
        for i in range(len(self.items)):
            item = self.items[i]
            if item.name == self.display_option_var.get():
                self.name_label_output.configure(text="Name: " + item.name)
                self.price_label_output.configure(text="Price: " + item.price)
                self.stock_label_output.configure(text="Stock: " + item.stock)

        
    def display_information(self):
        self.input_frame.grid_forget()
        self.output_frame.grid()

        self.item_names = [item.name for item in self.items]
        self.display_option_var.set("Select an item")

        option = OptionMenu(self.output_frame, self.display_option_var, *self.item_names)
        option.grid(row=1, column=0)

    def add_information(self):
        self.output_frame.grid_forget()
        self.input_frame.grid()

if __name__ == "__main__":
    root = Tk()
    start = Inventory(root)
    root.title("Shop")
    root.mainloop()
