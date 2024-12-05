import csv

def load_contacts(filename):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"No existing file found. Starting with an empty contact book.")
        return []

def save_contacts(contact_list, filename):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["Name", "Email", "Phone", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contact_list)
