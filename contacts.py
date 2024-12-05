def add_contact(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

   
    if not name.isalpha():
        print("Error: Name must only contain letters.")
        return
    if not phone.isdigit():
        print("Error: Phone number must be numeric.")
        return
    for contact in contact_list:
        if contact["Phone"] == phone:
            print("Error: This phone number already exists.")
            return

    contact_list.append({"Name": name, "Email": email, "Phone": phone, "Address": address})
    print("Contact added successfully!")

def view_contacts(contact_list):
    if not contact_list:
        print("No contacts available.")
        return
    print("\n--- Contact List ---")
    for i, contact in enumerate(contact_list, 1):
        print(f"{i}. {contact['Name']} | {contact['Email']} | {contact['Phone']} | {contact['Address']}")

def search_contacts(contact_list):
    search_term = input("Enter search term (Name, Email, Phone, or Address): ").lower()
    results = [c for c in contact_list if search_term in c["Name"].lower() or
               search_term in c["Email"].lower() or
               search_term in c["Phone"].lower() or
               search_term in c["Address"].lower()]
    if not results:
        print("No matching contacts found.")
    else:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"{contact['Name']} | {contact['Email']} | {contact['Phone']} | {contact['Address']}")

def remove_contact(contact_list):
    phone = input("Enter the phone number of the contact to remove: ")
    for contact in contact_list:
        if contact["Phone"] == phone:
            contact_list.remove(contact)
            print("Contact removed successfully!")
            return
    print("Error: Contact not found.")
