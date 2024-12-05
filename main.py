from menu import display_menu
from contacts import add_contact, view_contacts, search_contacts, remove_contact
from file_manager import load_contacts, save_contacts

def main():
    contact_list = load_contacts("contacts.csv")
    while True:
        choice = display_menu()
        if choice == "1":
            add_contact(contact_list)
        elif choice == "2":
            view_contacts(contact_list)
        elif choice == "3":
            search_contacts(contact_list)
        elif choice == "4":
            remove_contact(contact_list)
        elif choice == "5":
            save_contacts(contact_list, "contacts.csv")
            print("Contacts saved. Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
