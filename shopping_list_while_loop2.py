"""
Loops Lecture - Shopping list
This project is a shopping list app.
We have a global list that will be our shopping list.
We'll have a menu with options.
The program will keep running until it is closed.
The core logic is in the main() function.
"""

all_lists = {}

#shopping_list = []

def add_list():
    new_list = raw_input("What do you want to call your list? ")
    if new_list.lower() not in all_lists:
        all_lists[new_list] = []
    else: 
        print "That's already a list. "
        print "If you would like to add a list, type 1. "
        print "If you would prefer to return to the main menu, type 2. \n>>>  "
        choice = int(raw_input())
        if choice == 1:
            add_shopping_list()
        else:
            menu_choice()
    return all_lists

def add_item():
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "Here's your updated list", sorted_shopping_list()
    else:
        print "This item %s already exists!" % (item)


def show_all_lists():
    keys = all_lists.keys()
    print keys
    return keys


def sorted_shopping_list(keys):
    print "Which list would you like to see? "   
    print keys
    print "\n\nPlease type the name of the list you would like to see.  "
    key = raw_input()
    print all_lists[key].sort()


def remove_list(keys):
    print "Which list would you like to remove? "
    print keys
    print "\n\nPlease type the name of the list to remove. "
    choice = raw_input()
    if choice in all_lists:
        del all_lists[choice]
    else: 
        print "That list does not exist. "
        print "If you would like to delete a list, type 1. "
        print "IF you would prefer to return to the main menu, type 2. \n>>>  "
        choice = int(raw_input())
        if choice == 1:
            remove_list(keys)
        else: 
            menu_choice()



def remove_item(keys):
    print "Which list would you like to remove an item from? "
    print keys
    print "\n\nPlease type the name of the list to remove an item. "
    choice = raw_input()
    if choice in all_lists:
        print "Which item would you like to remove? "
        print all_lists[choice]
        print "Please type the name of the item you would like to remove. \n>>>  "
        item = raw_input()
        if item in all_lists[choice]:
            all_lists[choice].remove(item)
            print "Item has been removed."
            print all_lists[choice].sort()
        else:
            print "That item is not in the list. "
            print all_lists[choice]
            print "If you would like to delete an item, type 1. "
            print "If you would prefer to return to the main menu, type 2. \n>>>  "
            choice = int(raw_input())
        if choice == 1:
            remove_item(keys)
        else: 
            menu_choice()
    else: 
        print "That list does not exist. "
        print "If you would like to delete an item from a list, type 1. "
        print "If you would prefer to return to the main menu, type 2. \n>>>  "
        choice = int(raw_input())
        if choice == 1:
            remove_item(keys)
        else: 
            menu_choice()


    # item = raw_input("Please enter an item to remove OR type X if done.")
    # item = item.lower()
    # if item in shopping_list:
    #     shopping_list.remove(item)
    #     print "%s has been removed. Here's your updated list" % (item), sorted_shopping_list()
    # else:
    #     print "%s was not on the list." % (item)
    # else: 
    #     print "That item was not on the list. "sho
    #     print "If you would like to delete an item, type 1. "
    #     print "IF you would prefer to return to the main menu, type 2. \n>>>  "
    #     choice = int(raw_input())
    #     if choice == 1:
    #         remove_list(keys)






def menu_choice():
    print "0 - Main Menu"
    print "1 - shoShow all lists."
    print "2 - Show a specific list."
    print "3 - Add a new list."
    print "4 - Add an item to a specific list."
    print "5 - Remove an item from a list."
    print "6 - Remove a list."
    print "7 - Exit."
    choice = int(raw_input("Choose from the menu options."))
    return choice



def main():
    choice = menu_choice()

    keys = show_all_lists()


    while True:
        if choice == 0:
            choice = menu_choice()
        elif choice == 1:
            show_all_lists()
            choice = 0
        elif choice == 2:
            sorted_shopping_list(keys)
            choice = 0 #  prompt with the main menu
        elif choice == 3:
            add_list()
            choice = 0
        elif choice == 4:
            item = raw_input("Please enter an item to add OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            else:
                add_shopping_list(item)
                choice = 0
        elif choice == 5:
            #remove item from specific list
            item = raw_input("Please enter an item to remove OR type X if done.")
            if item.upper() == "X":  # return to main menu
                choice = 0
            else:
                remove_item(item)
                choice = 0
        elif choice == 6:
            remove_list(keys)
            choice = 0
        elif choice == 7:
            break


if __name__ == '__main__':
    main()

