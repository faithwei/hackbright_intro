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

def remove_item_shoppinglist():
	item = item.lower()
	if item not in shoppinglist:
		print "%s does not exist on list." % (item)
	else:
		shoppinglist.remove(item)
		print "%s updated shopping list" % (item), sorted_shoppinglist()








# #solution1
# def add_shopping_list(item):
#     item = item.lower()
#     if item not in shopping_list:
#         shopping_list.append(item)
#         print "Here's your updated list", sorted_shopping_list()
#     else:
#         print "This item %s already exists!" % (item)