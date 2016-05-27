from contact import*

addressbook = []

def search_contact(first_name,last_name):
	global addressbook
	for index in range(len(addressbook)):
		if addressbook[index].first_name == first_name and addressbook[index].last_name == last_name:
			return addressbook[index]
			break

def add_contact(first_name, last_name, mobile_phone = "", work_phone = "", email ="",twitter_handle =""):
	global addressbook
	
	friend = Contact(first_name, last_name, mobile_phone, work_phone, email, twitter_handle)
	addressbook.append(friend)
	print "Contact %s %s created!" % (first_name, last_name)

def create_contact(first_name, last_name, mobile_phone = "", work_phone = "", email ="",twitter_handle =""):
	friend = search_contact(first_name,last_name)

	if friend != None:
		display_contact(friend)
		user_option = raw_input("This First name and Last name already exist. Would you like to add another one? Type Y for yes or N for no: ")
		if user_option.lower() == "y":
			add_contact(first_name, last_name, mobile_phone, work_phone, email, twitter_handle)
	else:
		add_contact(first_name, last_name, mobile_phone, work_phone, email, twitter_handle)
	
def display_contact(contact_obj):
	print """
		    First name     : %s
		    Last name      : %s
		    Mobile phone   : %s
		    Work phone     : %s
		    Email          : %s
		    Twitter handle : %s
		  """ % (contact_obj.first_name, contact_obj.last_name, contact_obj.mobile_phone, contact_obj.work_phone, contact_obj.email, contact_obj.twitter_handle)

def display_all_contacts():
	global addressbook
	
	for contact in addressbook:
		display_contact(contact)

def update_contact(first_name,last_name):
	global addressbook
	#Raw input for first and last names
	contact_update = search_contact(first_name,last_name)
	
	if contact_update == None:
		print "First name and Last name is not in your Contact List."
	else
		while True:
			update_menu()
			try:
				menu_option = int(raw_input("Select one option: "))
			except ValueError:
				menu_option = None

			if menu_option == 1:
				# Update first name
				new_first_name = raw_input
				if len(new_first_name) > 0:
					contact_update.change_first_name(new_first_name)
				else:
					print "Invalid input"
			elif menu_option == 2:

			elif menu_option == 3:

			elif menu_option == 4:

			elif menu_option == 5:

			elif menu_option == 6:

index
def update_menu():
	print """
			+----------------------------+
			|      Update options        |
			+----------------------------+
			|  1 - First name            |
			|  2 - Last name             |
			|  3 - Mobile phone          |
			|  4 - Work phone    		 |
			|  5 - Email                 |
			|  6 - Twitter handle        |
			+----------------------------+
		  """


def remove_contact(first_name, last_name):
	global addressbook
	# Remove the first instance and exit loop
	# for index in range(len(addressbook)):
	# 	if addressbook[index].first_name == first_name and addressbook[index].last_name == last_name:
	# 		display_contact(addressbook[index])
	# 		user_option = raw_input("Are you sure you want to delete this contact? Type Y for yes or N for no: ")
	# 		if user_option.lower() == "y":
	# 			del addressbook[index]
	# 			break

	# Remove all instances with the same first name and last name
	index = 0
	while True:
		if index < len(addressbook):
			if addressbook[index].first_name == first_name and addressbook[index].last_name == last_name:
				display_contact(addressbook[index])
				user_option = raw_input("Are you sure you want to delete this contact? Type Y for yes or N for no: ")
				if user_option.lower() == "y":
					del addressbook[index]
				else:
					index += 1
			else:
				index += 1
		else:
			break
def show_menu():
	print """
			+----------------------------+
			|      Contact Manager       |
			+----------------------------+
			|  1 - Add Contact           |
			|  2 - Remove Contact        |
			|  3 - Update Contact        |
			|  4 - Display All Contacts  |
			|  5 - Search Contact        |
			|  6 - Exit                  |
			+----------------------------+
		  """

def main():
	global addressbook
    
	while True:
		show_menu()
		try:
			menu_option = int(raw_input("Select one option: "))
		except ValueError:
			menu_option = None

		if menu_option == 1:
			# Add Contact
			create_contact("faith","ng","415-123-4567")
		elif menu_option == 2:
			# Remove Contact
			remove_contact("faith","ng")
		elif menu_option == 3:
			# Update Contact
			print "Not available yet! Come back soon!"
		elif menu_option == 4:
			# Display all contacts
			display_all_contacts()
		elif menu_option == 5:
			# Search Contact
			existing_contact = search_contact("faith","ng")
			print existing_contact.first_name
		elif menu_option == 6:
			print "Thank you for using the Contact Manager!"
			break
		else:
			print "Invalid option! Please select an option from the Menu."

if __name__ == "__main__":
	main()