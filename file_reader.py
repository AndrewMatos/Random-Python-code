file_path = '/home/andrew/projects/python/pi_digits.txt'
with open(file_path) as file_object:
	#contents = file_object.read()
	lines = file_object.readlines()
	pi_string = ''
	for line in lines:
		pi_string += line.strip()

	birthday = input("Enter your birthday, in the for mmddyy:")

	if birthday in pi_string:
		print("Your birthday appears in PI")
	else:
		print("your birthday does not appear in PI")

#print(contents)


