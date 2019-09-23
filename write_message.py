filename = 'programming.txt'

# open(filename, 'w') as file_object:
#	file_object.write('i love programming. \n')
with open(filename, 'a') as file_object:
	file_object.write('I also love finding meaning in large data sets. \n')
	file_object.write('i love creating apps that can run in a browser. \n')