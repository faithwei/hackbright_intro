def check_prime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def main():
	while (True):
		user_input = raw_input("\nPlease type x if you like to exit.\nPlease enter a number you would like to check: ")
		if user_input.lower() == "x":
			break
		else:
			if check_prime(int(user_input)) == True:
				print "It is a prime number!"
			else:
				print "It is not a prime number."

if __name__ == "__main__":
	main()
