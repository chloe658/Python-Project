from tkinter import *
from tkinter import messagebox


class Items:
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

        # Input widgets
        self.input_label = Label(self.input_frame, text="Add Information")
        self.input_output_btn = Button(self.input_frame, text="Display Information", command=self.display_information)
        self.input_label.grid(row=0, column=0)
        self.input_output_btn.grid(row=0, column=1)
        self.name_label = Label(self.input_frame, text="Item Name:")
        self.name_entry = Entry(self.input_frame, textvariable=self.name_var)
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.price_label = Label(self.input_frame, text="Item Price:")
        self.price_entry = Entry(self.input_frame, textvariable=self.price_var)
        self.price_label.grid(row=2, column=0)
        self.price_entry.grid(row=2, column=1)
        self.stock_label = Label(self.input_frame, text="Item Stock:")
        self.stock_entry = Entry(self.input_frame, textvariable=self.stock_var)
        self.stock_label.grid(row=3, column=0)
        self.stock_entry.grid(row=3, column=1)

        # Output widgets
        self.output_label = Label(self.output_frame, text="Display Information")
        self.output_input_btn = Button(self.output_frame, text="Add Information", command=self.add_information)
        self.output_label.grid(row=0, column=0)
        self.output_input_btn.grid(row=0, column=1)
        self.name_label = Label(self.output_frame, text="Item Name:")
        self.name_entry = Label(self.output_frame, text=self.name_var.get())
        self.name_label.grid(row=1, column=0)
        self.name_entry.grid(row=1, column=1)
        self.price_label = Label(self.output_frame, text="Item Price:")
        self.price_entry = Label(self.output_frame, text=self.price_var.get())
        self.price_label.grid(row=2, column=0)
        self.price_entry.grid(row=2, column=1)
        self.stock_label = Label(self.output_frame, text="Item Stock:")
        self.stock_entry = Label(self.output_frame, text=self.stock_var.get())
        self.stock_label.grid(row=3, column=0)
        self.stock_entry.grid(row=3, column=1)
        
    def display_information(self):
        self.input_frame.grid_forget()
        self.output_frame.grid()

    def add_information(self):
        self.output_frame.grid_forget()
        self.input_frame.grid()

if __name__ == "__main__":
    root = Tk()
    start = Inventory(root)
    root.title("Shop")
    root.mainloop()
