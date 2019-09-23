def count_words(filename):
	"""Count the approximate numbers of words in a file """
	try: 
		with  open(filename, encoding = 'utf-8') as f:
			contents = f.read()
	except FileNotFoundError:	
		#for passing the error silently without and continue the code
		#pass 
		print(f"Sorry, the file {filename} does not exist.")
	else:
		#count the approximate number of words in the file
		words = contents.split(" ")
		num_words = len(words)
		print(f"The file {filename} has about {num_words} words.")

filenames = ['programming.txt', "alice.txt"]
for filename in filenames:
	count_words(filename)