# print range(5,1,-1)


#Part 2
# for item in range (1,21):
# 	print item

# for item in range (1,21):
# 	if item == 13:
# 		print "hello"
# 	else:
# 		print item

#Part 3

# 3.a
# fruits = ["apples","oranges","bananas"]

# for item in fruits:
# 	print item

# #3.b
# fruits = ["apples","oranges","bananas"]
# for item in range (len(fruits)):
# 	print fruits[item]

# Part 4

#4.a
# def sum_nums(num):
# 	sum = 0
# 	for item in range(num):
# 		sum = sum + item
# 	return sum

#4.b
# def sum_nums2(num):
# 	sum = 0
# 	if num < 0:
# 		for item in range (0,num-1,-1):
# 			sum = sum + item
# 	else:
# 		for item in range(num+1):
# 			sum = sum + item
# 	return sum

# print sum_nums2(-3) 

#Big challenge

def fizz_buss():
	for item in range (1,101):
		if item%15 == 0:
			print "FizzBuzz"
		elif item%3 == 0:
			print "Fizz"
		elif item%5 == 0:
			print "Buzz"
		else:
			print item

fizz_buss()



