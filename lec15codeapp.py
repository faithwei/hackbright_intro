from urllib2 import urlopen
from json import load

#sf open data source: film location in sf
apiUrl = "https://data.sfgov.org/resource/wwmu-gmzc.json"

#open the apiUrl and assign data to variable
response = urlopen(apiUrl)

json_obj = load(response)

#film title and year 2002

unique_list = [] #global list

#function to search API for specific movies by year
def movie_by_year():
	global unique_list
	#ask user for specific year to search
	year = str(raw_input("For what year would you like to list movies shot in SF? "))#iterates thru json_obj list
	for item in json_obj: 
		#checks value which is the year in the item at key "release_year"
		if item["release_year"] == year: 
			#converts unicode to string or strips u'
			title = str(item["title"]) 
			#sets condition to no include duplicate values at key title
			if title not in unique_list: 
				#adds unique values to "unique_list"
				unique_list.append(title) 
	return unique_list 

print movie_by_year()



