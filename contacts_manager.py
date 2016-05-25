from lec14contact import *

contact_Jessica = Contact("jessica", "chuang", "6261234567")
contact_melissa = Contact("melissa","mmmm","4151234567")
contact_faith = Contact("faith","ng","4081234567")

contact_faith.email = "faithwei@gmail.com"
contact_melissa.email = "melissa@hackbright.com"
contact_Jessica.email = "jessica@hackbright.com"

contacts_list = []

contacts_list.append(contact_Jessica)
contacts_list.append(contact_melissa)
contacts_list.append(contact_faith)

for x in contacts_list:
	print x.first_name, x.last_name

contact_Jessica.send_email("How are you doing?")

