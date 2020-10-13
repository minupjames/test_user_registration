import json
from registrant import View
from test_data import (initial_contact_data, initial_leads_data,
                       reg1, reg2, reg3)

view = View()
#add initial contact data
view.add_contact_to_list(initial_contact_data)

#add initial lead data
view.add_leads_to_list(initial_leads_data)

#print initial LeadsList
view.leads_list.print_lead_details()
#print initial ContactsList
view.contacts_list.print_details()

# Add/Update regstrant details
view.add_registrant(json.dumps(reg1))
view.add_registrant(json.dumps(reg2))
view.add_registrant(json.dumps(reg3))

view.contacts_list.print_details()

view.leads_list.print_lead_details()


