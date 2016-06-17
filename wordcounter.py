from collections import Counter
from collections import OrderedDict
import string


def read_file(filename):
	with open(filename) as my_file:
		my_list = my_file.readlines()
	return my_list

def strip_invisible(my_list):
	for string in my_list:
		return string.strip()

# remove punctuations and lowercase everything
def clean_file(strip_string):
	clean_string = strip_string.translate(None, string.punctuation).lower()

	return clean_string

def word_counter(clean_string):
	words = clean_string.decode("utf-8-sig").encode("utf-8")
	freqs = dict(Counter(words.split()))
	return freqs	

def write_file(clean_dictionary):
	with open("clean_output.txt", "w") as f:
		for key in sorted(clean_dictionary):
			input_data = key + "-" + str(clean_dictionary[key]) + "\n"
			f.write(input_data)

# def sorted_bykey(clean_dictionary):
# 	sorted_dictionary = sorted(clean_dictionary.key(), key=lambda t: t[0]))
# 	return sorted_dictionary

# def sorted_byvalue(clean_dictionary):
# 	sorted_dictionary = sorted(clean_dictionary.values())
# 	return sorted_dictionary




def main():

	word_list = read_file('LoremIpsum.txt')

	# print len(word_list)

	strip_string = strip_invisible(word_list)
	clean_string = clean_file(strip_string)
	# print clean_string
	clean_dictionary = word_counter(clean_string)
	

	write_file(clean_dictionary)

if __name__ == '__main__':
	main()


# print clean_file(strip_string)
# def clean_file():dd



# def word_counter():
# 	with open('LoremIpsum.txt') as my_file:
#     my_list  = my_file.readlines()