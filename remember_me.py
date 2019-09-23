import json

def get_stored_username(filename):
	""" Get stored username if avaible """
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError: 
		return None 
	else: 
		return username

def store_username(filename):
	""" stores a new username """
	username = input("what is your name? ")
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user(filename):
	"""Greet the user by name."""
	username = get_stored_username(filename)
	if username:
		print(f'welcome back, {username}!')
	else: 
		username = store_username(filename)
		print(f'we will remember you, {username}')


filename = 'username.json'
greet_user(filename)