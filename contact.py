class Contact(object):
	def __init__(self, first_name, last_name, mobile_phone = "", work_phone = "", email ="",twitter_handle =""):
		self.first_name = first_name
		self.last_name = last_name
		self.mobile_phone = mobile_phone
		self.email = email
		self.twitter_handle = twitter_handle
		self.work_phone = work_phone
	
	def change_first_name(self,first_name):
		self.first_name = first_name

	def change_last_name(self,last_name):
		self.last_name = last_name

	def change_mobile_phone(self,mobile_phone):
		self.mobile_phone = mobile_phone

	def change_work_phone(self,work_phone):
		self.work_phone = work_phone	

	def change_email(self, email):
		self.email = email

	def change_twiiter(self, twitter_handle):
		self.twitter_handle = twitter_handle

	def send_email(self,message):
		if self.email == "":
			print "Please add the email first."
		elif message == "":
			print "Please write a message."
		else:
			print "To: %s - %s" % (self.email,message)

	def send_twitter(self,message):
		if self.twitter_handle == "":
			print "Please add the twitter handle first."
		elif message == "":
			print "Please write a message."
		else:
			print "Tweet: %s" % (message)

