#question 1
# vocabulary_words = {"tuple":"a sequence of immutable objects","dictionary":"unordered collection of key:value pairs that map one thing to another","global scope":"variables defined outside of functions","local scope":"variables inside functions definitions"}


#question 2
# def count_letters(name):
# 	count_alpha = {}
# 	name = name.lower()
# 	for i in name:
# 		if i not in count_alpha:
# 			count_alpha[i] = name.count(i)
# 	return count_alpha


# print count_letters("Victoria Yi Yau")

# question 3
prices = {"banana":4,"apple":2,"orange":1.5,"pear":3}
highest = 0
for key, value in prices.items():
	if value > highest:
		highest = value
print highest



