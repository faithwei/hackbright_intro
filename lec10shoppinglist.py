shoppinglist = []

def add_to_shoppinglist(item):
	item = item.lower()
	if item not in shoppinglist:
		shoppinglist.append(item)
		print "Updated shopping list", sorted_shoppinglist()
	else:
		print "%s already exists, please enter another item." %(item)

def sorted_shoppinglist():
	shoppinglist.sort()
	return shoppinglist

def remove_shoppinglist(item):
	item = item.lower()
	if item not in shoppinglist:
		print "%s does not exist on list." % (item)
	else:
		shoppinglist.remove(item)
		print "%s removed from shopping list. Updated shopping list:" % (item), sorted_shoppinglist()

def replace_item(old_item, new_item):
    old_item = old_item.lower()
    new_item = new_item.lower()

    if old_item in shoppinglist:
        item_index = shoppinglist.index(old_item)
        print "%s has replaced %s in the list." % (new_item, old_item)
    else:
        print "%s is not in the list." % (old_item)	


def menu():
	print "0 - Main Menu"
	print "1 - Show shopping list."
	print "2 - Add an item to the shopping list."
	print "3 - Remove an item from the shopping list."
	print "4 - Exit shopping list."
	user_option = int(raw_input("Enter the option number."))
	return user_option

def main():
	user_option = menu()

	while True:
		if user_option == 0:
			user_option = menu()
		elif user_option == 1:
			print sorted_shoppinglist()
			user_option = 0
		elif user_option == 2:
			item = raw_input("Add an item to the shopping list. Type X when done.")
			if item.lower() == "x":
				user_option = 0
			else:
				add_to_shoppinglist(item)
		elif user_option == 3:
			item = raw_input("Remove an item from the shopping list. Type X when done.")
			if item.lower() == "x":
				user_option = 0
			else:
				remove_shoppinglist(item)
		elif user_option == 4:
			break


if __name__ == '__main__':
    main()
