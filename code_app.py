my_list_formatted = []

with open('class_grades.txt') as my_file:
    my_list  = my_file.readlines()
   

def convert_score_to_letter(score):
    if score >= 90:
    	return "A"
    elif 90>score>=80:
    	return "B"
    elif 80>score>=70:
    	return "C"
    elif 70>score>=60:
    	return "D"
    else:
    	return "F"


def process_file_to_list(my_list):
    for i in my_list:
    	stripped_string = int(i.strip().strip('\xef\xbb\xbf'))
    	my_list_formatted.append(stripped_string)
    return my_list_formatted

def main():
    global my_list_formatted
    for i in process_file_to_list(my_list):
    	graded = convert_score_to_letter(i)

        print i,"is a",graded 

if __name__ == '__main__':
   main()