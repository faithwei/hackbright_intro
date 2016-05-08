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


# TEST FUNCTIONS
# 1 - add 4 times to your shopping list
add_to_shoppinglist("apple")
add_to_shoppinglist("steak")
add_to_shoppinglist("beef")
add_to_shoppinglist("mustard")

# # 2 - Add an item that is already in the list. what happens?
add_to_shoppinglist("apple")

# # 3 - Remove an item on your list
remove_shoppinglist("apple")

# # 4 - Remove an item that is not in the list. what happens?
remove_shoppinglist("chicken")

# 5 - you've changed your mind on one of your items. you want to substitute it with something else.
replace_item("mustard", "ketchup")





# #solution1
# def add_shopping_list(item):
#     item = item.lower()
#     if item not in shopping_list:
#         shopping_list.append(item)
#         print "Here's your updated list", sorted_shopping_list()
#     else:
#         print "This item %s already exists!" % (item)