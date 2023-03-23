import model



def main_menu() -> int:
    print("""    1.Open phonebook file
    2.Save phonebook file
    3.Show all contacts
    4.Add contact
    5.Change contact
    6.Find contact
    7.Delete contact
    8.Exit""")
    choice = input("select menu item: ")
    if choice.isdigit() and 0<int(choice)<= 8:
        return int(choice)
    else:
        print("********************* Enter digit from 1 to 8! ***********************")


def show_contacts(book: list, error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f"{i}. {contact.get('name'):<20}"
                  f"{contact.get('phone'):<20}"
                  f"{contact.get('comment'):<20}")
        return True



def find_contact(book):
    if book:
        result = []
        try_string = input("enter information of contact:")
        for contact in book:
            for field in contact.values():
                if try_string.lower() in field.lower():
                    result.append(contact)
        return result
    else:
        print("************************ phonebook empty or not open ************************")


def add_contact() -> dict:
    name = input("enter name: ")
    phone = input("enter phone number: ")
    comment = input("enter comment: ")
    return {"name": name, "phone": phone, "comment": comment}


def change_contact(book: list[dict], index: int):
    print("if you don't want to change some fields,leave it empty: ")
    contact = add_contact()
    return {"name": contact.get("name") if contact.get("name") else book[index - 1].get("name"),
            "phone": contact.get("phone") if contact.get("phone") else book[index - 1].get("phone"),
            "comment": contact.get("comment") if contact.get("comment") else book[index - 1].get("comment")}



def del_contact(book):
    show_contacts(book, "**************** phonebook empty or not open ********************")
    if book:
        del_index = model.get_number("enter number of removable contact:", f"try again it must be digit from 1 to {len(book)}")
        del_element = book.pop(del_index - 1)
        print(f"************************** contact {del_element.get('name')} succesfully deleted ******************************")
    else:
        print("phonebook empty or not open")



