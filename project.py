import pandas as pd
import numpy as np
from tkinter import *
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        
        self.df = pd.DataFrame(columns=["Website", "Username", "Password"])
        self.load_data()
        
        self.website_entry = Entry(master, width=30)
        self.website_entry.grid(row=0, column=1, padx=20, pady=(20, 0))
        
        self.username_entry = Entry(master, width=30)
        self.username_entry.grid(row=1, column=1)
        
        self.password_entry = Entry(master, width=30)
        self.password_entry.grid(row=2, column=1)
        
        self.website_label = Label(master, text="Website:")
        self.website_label.grid(row=0, column=0, pady=(20, 0))
        
        self.username_label = Label(master, text="Username:")
        self.username_label.grid(row=1, column=0)
        
        self.password_label = Label(master, text="Password:")
        self.password_label.grid(row=2, column=0)
        
        self.add_button = Button(master, text="Add Entry", command=self.add_entry)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.suggest_button = Button(master, text="Suggest Password", command=self.suggest_password)
        self.suggest_button.grid(row=4, column=0, columnspan=2)
        
    def load_data(self):
        try:
            self.df = pd.read_csv("passwords.csv")
        except FileNotFoundError:
            pass
        
    def save_data(self):
        self.df.to_csv("passwords.csv", index=False)
        
    def add_entry(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        if website and username and password:
            new_entry = pd.DataFrame({"Website": [website], "Username": [username], "Password": [password]})
            self.df = pd.concat([self.df, new_entry], ignore_index=True)
            self.save_data()
            messagebox.showinfo("Success", "Entry added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")
    def add_entry(self):
        website = self.website_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if website and username and password:
            new_entry = pd.DataFrame({"Website": [website], "Username": [username], "Password": [password]})
            self.df = pd.concat([self.df, new_entry], ignore_index=True)
            self.save_data()
            messagebox.showinfo("Success", "Entry added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

        
    def clear_entries(self):
        self.website_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        
    def suggest_password(self):
        suggested_password = ''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'), size=12))
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, suggested_password)

def main():
    root = Tk()
    app = PasswordManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()

