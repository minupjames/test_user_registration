class Leads():
    """
    Leads Class
    """
    def __init__(self, name, email, phone):
        """
        Inits Leads Class 
        """
        self.name = name
        self.email = email
        self.phone = phone
          
class LeadsList(list):
    """
    LeadsList: List of Leads objects
    """
         
    def __init__(self):
        """
        Initializes LeadsList
        """
        super(LeadsList, self).__init__()   
        
    def get_leads_by_email(self, email):
        """
        Search Leadslist by email and return leads object on a successful match
        """
        for lead in self:
            if lead.email == email:
                return lead
        return None

    def get_leads_by_phone(self, phone):
        """
        Search Leadslist by phone and return leads object on a successful match
        """
        for lead in self:
            if lead.phone == phone:
                return lead
        return None

    def get_lead(self, email, phone):
        """
        Checks Leadslist by email and then phone  
        Return Lead object if it matches.
        """
        lead = None
        if email is not None:
            lead = self.get_leads_by_email(email)
        if lead is None and phone is not None:
            lead = self.get_leads_by_phone(phone)
        return lead
        
    def print_lead_details(self):
        """
        Print Current Lead lists
        """
        print('LeadsList Details')
        for lead in self:
            print(lead.name, lead.email, lead.phone)