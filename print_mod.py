#python 3.7 test

from car_class import Car as CAR, ElectricCar

def transfer_list(complete_list, empty_list):
	""" transfers file from one list to another """
	complete_list = complete_list[:]
	while complete_list:
		current_element = complete_list.pop()
		print(f"transfered {current_element}") # pyton 2.6 to 3.6 "transfered {}".format(current_element)
		empty_list.append(current_element)


def show_list(list):
	"""print element from a list """
	for element in list:
		print(element)


full_list = ["veronica", "lol", 1]

empty_list = []

transfer_list(full_list, empty_list)

show_list(empty_list)


my_tesla = ElectricCar("tesla", "model ", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()