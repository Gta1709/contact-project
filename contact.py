# Contact Book Application

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"{name} was added successfully!")

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print("It was removed successfully.")
    else:
        print("Contact not found.")

def search_contact():
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave field blank to keep current value.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print(f"Contact {name} was updated successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        remove_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")
