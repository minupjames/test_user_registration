import json
from contact import ContactsList, Contacts
from leads import LeadsList, Leads

class View:
    """
    View Class used for creating Leads and Contacts
    """ 
    def __init__(self):
        """
        Inits View Class
        """
        self.leads_list = LeadsList()
        self.contacts_list = ContactsList()

    def add_contact_to_list(self, initial_contact_data):
        """
        Adding initial contacts to ContactList
        initial_contact_data should be a list of tuples.
        Each tuple should be of the form: (name, email, phone)
        """
        for contact in initial_contact_data:
            contact = Contacts(contact[0], contact[1], contact[2])
            self.contacts_list.append(contact)
        
    def add_leads_to_list(self, initial_leads_data):
        """
        Adding initial leads to LeadsList
        initial_leads_data should be a list of tuples.
        Each tuple should be of the form: (name, email, phone)  
        """
        for lead in initial_leads_data:
            lead = Leads(lead[0],lead[1],lead[2])
            self.leads_list.append(lead)
    
    def validate_input(self, input_json):
        """
        Validates input registrant details
        """
        email = phone = name = None
        try:
            reg_details = json.loads(input_json)
        except Exception as exc:
            raise Exception('Invalid input')
        
        if reg_details is not None:
            registrant = reg_details.get('registrant', None)
            if registrant is not None:
                email = registrant.get('email', None)
                phone = registrant.get('phone', None)
                name = registrant.get('name', None)
            else:
                raise Exception('Invaid input')
        else:
            raise Exception('Invalid input')
            
        if phone is not None:
            if not phone.isnumeric():
                raise Exception("Invalid Phone Number. Shouldn't have brackets, spaces or dashes")
            if len(phone) != 10:
                raise Exception("Invalid Phone Number. It should have 10 digits")
                     
        return name, email, phone

    def add_registrant(self, input_json):
        """
        Validates input and add/update registrant details into contact
        """ 
        name, email, phone = self.validate_input(input_json)
        #Check in ContactList for given email/phone
        contact = self.contacts_list.get_contact(email, phone)
        if contact is None:
            #Check in Leadslist for given email/phone
            lead = self.leads_list.get_lead(email, phone)
            if lead is not None:
                #remove from leads list, delete leads object
                #create new contact and add to contact list
                contact = Contacts(lead.name, lead.email, lead.phone)    
                contact.update(name, email, phone)
                self.leads_list.remove(lead)
                del lead
            else:
                #create new contact and add to contact list
                contact = Contacts(name, phone, email)
            self.contacts_list.append(contact)      
        else:
            #Update Contact if required. 
            contact.update(name, email, phone)
  