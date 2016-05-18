#code App
# food_price_tuple = ('sushi', 7.50, 'burrito', 8.20, 'cheeseburger', 6.00, 'hot dog', 3.40, 'fried rice', 9.99)


# def convert_tuple_to_dictonary(tuple):
# 	dictionary = {}
# 	evens =[]
# 	index_numbers = range(0,len(food_price_tuple),2)
# 	for item in index_numbers:
# 		dictionary[food_price_tuple[item]] = food_price_tuple[item+1]
# 	return dictionary

# print convert_tuple_to_dictonary(food_price_tuple)

# 	#create an empty dictionary
# 	#identify all the key that are the odds in the tupple
# 	#identify all the values that are the evens in the tupple
# 	#put that pair in the dictionary
# 	#return that dictionary

#Excercise #1.1
# my_name = "faith ng"
# print list(my_name.replace(" ",""))

#exercise #1.2
# string = "1,2,3,4,5"
# print string.split(",")

#exercise 1.3
# string = "One fish two fish red fish blue fish"
# print string.replace(" fish","").split(" ")

#exercise 1.4
string = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quanity:1,price:4.49\n"]



def grocery_bill(list_string):
	bill = []
	for i in list_string:
		item = i.split(",")[0].split(":")[1]
		quantity = float(i.split(",")[1].split(":")[1])
		price = float(i.split(",")[2].split(":")[1])
		bill += [quantity * price]
	return sum(bill) 

print grocery_bill(string)
