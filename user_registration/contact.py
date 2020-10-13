class Contacts():
    """
    Contacts Class
    """
    def __init__(self, name, email, phone):
        """
        Inits Contacts Class
        """
        self.name = name
        self.email = email
        self.phone = phone

    def update(self, name, email, phone):
        """
        Update the existing contact object when name, email or phone modified
        """
        if name is not None and self.name != name:
            self.name = name
        if email is not None and self.email != email:
            self.email = email
        if phone is not None and self.phone != phone:
            self.phone = phone

class ContactsList(list):
    """
    ContactsList: List of Contact objects
    """
    def __init__(self):
        """
        Initializes ContactsList
        """
        super(ContactsList, self).__init__()

    def get_contact_by_email(self, email):
        """
        Search ContactsList by email and return contact object on a successful match
        """
        for contact in self:
            if contact.email == email:
                return contact
        return None

    def get_contact_by_phone(self, phone):
        """
        Search ContactsList by phone and return contact object on a successful match
        """
        for contact in self:
            if contact.phone == phone:
                return contact
        return None

    def get_contact(self, email, phone):
        """
        Checks ContactsList by email and then phone
        & returns contact object if it matches
        """
        contact = None
        if email is not None:
            contact = self.get_contact_by_email(email)
        if contact is None and phone is not None:
            contact = self.get_contact_by_phone(phone)
        return contact

    def print_details(self):
        """
        Print Current contact lists
        """
        print('\nContacts Details')
        print('-'*16)
        for contact in self:
            print(contact.name, contact.email, contact.phone)
