phone_book = []
path = "book.txt"


def open_file():
    with open(path, "r", encoding="utf8") as file:
        data = file.readlines()
    for item in data:
        item = item.strip().split(";")
        contact ={"name": item[0],
                  "phone" : item[1],
                  "comment" : item[2]}
        phone_book.append(contact)
    print("*********************** file successfully opened **************************")


def get_phone_book():
    return phone_book


def add_contact(contact: dict):
    phone_book.append(contact)
    print("*********************** contact successfully added **************************")


def change_contact(contact: dict, index: int):
    phone_book.pop(index-1)
    phone_book.insert(index-1, contact)
    print(f"**************************** contact was changed *********************************")

def save_file():
    if phone_book:
        with open(path, "w", encoding="utf8") as file:
            for contact in phone_book:
                data = ";".join(v for v in contact.values())
                file.write(data + "\n")
        print("************************ file successfully saved *****************************")
    else:
        print("phonebook empty or not open")

def get_number(message, error_message):
    control = False
    while control == False:
        test = input(message)
        if test.isdigit() == True:
            result = int(test)
            control = True
        else:
            print(error_message)

    return result

