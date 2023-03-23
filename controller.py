import model
import view



def start():
    while True:
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
            case 2:
                model.save_file()
            case 3:
                view.show_contacts(pb, "********************* phonebook empty or not open ***********************")
            case 4:
                contact = view.add_contact()
                model.add_contact(contact)
            case 5:
                if view.show_contacts(pb, "********************* phonebook empty or not open *************************"):
                    index = model.get_number("Enter number of change contact:", f"try again it must be digit from 1 to {len(pb)}")
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)

            case 6:
                result = view.find_contact(pb)
                view.show_contacts(result, "********************* contacts not found *************************")
            case 7:
                view.del_contact(pb)
            case 8:
                print("goodbye!")
                return

