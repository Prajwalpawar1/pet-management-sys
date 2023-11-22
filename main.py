import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def add_pet():
    pet_name = pet_name_entry.get()
    pet_type = pet_type_entry.get()
    pet_price = pet_price_entry.get()
    pet_address = pet_address_entry.get()

    if pet_name and pet_type and pet_price and pet_address:
        # Update the list of pets
        pets.append({"Name": pet_name, "Type": pet_type, "Price": pet_price, "Address": pet_address})

        messagebox.showinfo('Success', 'Pet added successfully')
        clear_entries()

        # Update the admin display
        display_admin_data()
    else:
        messagebox.showwarning('Incomplete Information', 'Please fill in all fields')

def clear_entries():
    pet_name_entry.delete(0, tk.END)
    pet_type_entry.delete(0, tk.END)
    pet_price_entry.delete(0, tk.END)
    pet_address_entry.delete(0, tk.END)

def admin_login():
    def check_credentials():
        entered_name = username_entry.get()
        entered_password = password_entry.get()

        # Check if the entered username and password match the predefined values
        if entered_name == "abc" and entered_password == "123":
            display_admin_data()
            admin_login_window.destroy()
        else:
            messagebox.showerror('Invalid Credentials', 'Incorrect username or password')

    admin_login_window = tk.Tk()
    admin_login_window.title("Admin Login")

    ttk.Label(admin_login_window, text="Username:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    ttk.Label(admin_login_window, text="Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")

    username_entry = ttk.Entry(admin_login_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_entry = ttk.Entry(admin_login_window, show="*", width=30)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    login_button = ttk.Button(admin_login_window, text="Login", command=check_credentials)
    login_button.grid(row=2, column=1, pady=10)

def display_admin_data():
    admin_data_window = tk.Tk()
    admin_data_window.title("Admin Data")

    ttk.Label(admin_data_window, text="%-20s%-20s%-20s%-20s" % ('Name', 'Type', 'Price', 'Address')).pack()

    for pet in pets:
        ttk.Label(admin_data_window, text="%-20s%-20s%-20s%-20s" % (pet['Name'], pet['Type'], pet['Price'], pet['Address'])).pack()

def main():
    global root, pets
    pets = []

    root = tk.Tk()
    root.title("Pet Shop Management System")

    # Animal Photos

    images = [
        "C:/Users/prajw/Documents/pythonProject4/logo.jpeg",
        "C:/Users/prajw/Documents/pythonProject4/download.jpeg"
    ]

    image_frames = ttk.Frame(root)
    image_frames.grid(row=0, column=0, columnspan=2, pady=10)

    for i, image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.resize((500, 500))
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(image_frames, image=photo)
        label.photo = photo
        label.grid(row=0, column=i, padx=5)

    # Labels
    ttk.Label(root, text="Pet owner name:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    ttk.Label(root, text="Pet Type:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    ttk.Label(root, text="Pet Price:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    ttk.Label(root, text="owner Address:").grid(row=4, column=0, padx=10, pady=5, sticky="e")

    # Entry widgets
    global pet_name_entry, pet_type_entry, pet_price_entry, pet_address_entry
    pet_name_entry = ttk.Entry(root, width=30)
    pet_name_entry.grid(row=1, column=1, padx=10, pady=5)

    pet_type_entry = ttk.Entry(root, width=30)
    pet_type_entry.grid(row=2, column=1, padx=10, pady=5)

    pet_price_entry = ttk.Entry(root, width=30)
    pet_price_entry.grid(row=3, column=1, padx=10, pady=5)

    pet_address_entry = ttk.Entry(root, width=30)
    pet_address_entry.grid(row=4, column=1, padx=10, pady=5)

    # Buttons
    add_button = ttk.Button(root, text="Add Pet", command=add_pet)
    add_button.grid(row=5, column=1, pady=10)

    clear_button = ttk.Button(root, text="Clear Entries", command=clear_entries)
    clear_button.grid(row=5, column=0, padx=10, pady=10)

    admin_button = ttk.Button(root, text="Admin", command=admin_login)
    admin_button.grid(row=6, column=0, columnspan=2, pady=10)

    # About Us Section
    ttk.Label(root, text="About Us", font=('Helvetica', 16, 'bold')).grid(row=7, column=0, columnspan=2, pady=10)

    about_us_text = (
        "Welcome to our Pet Shop Management System!\n"
        "We are dedicated to providing a wide variety of pets to meet your companionship needs.\n"
        "Our goal is to offer a seamless and enjoyable experience for both pet owners and enthusiasts.\n"
        "Thank you for choosing our pet shop!"
    )

    ttk.Label(root, text=about_us_text, wraplength=500, justify="left").grid(row=8, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
