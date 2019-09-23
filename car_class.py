class Car:
	"""A simple attempt to represent a car."""

	def __init__(self, maker, model, year):
		""" Initialize attributes that describe a car """
		self.maker= maker
		self.model= model
		self.year= year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		""" return a neatly formate descriptive name. """
		long_name = f"{self.year} {self.maker} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statment showing the car's mileage """
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("you can't roll back an odometer!")

my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

class Battery:
	"""A simple attempt to model a battery for an electric car """
	def __init__(self, battery_size = 75):
		"""Initialize the battery attributes """
		self.battery_size = battery_size


	def describe_battery(self):
		""" Print a statemenet describing the battery size. """
		print(f"This cars has a {self.battery_size}-kwh battery")

class ElectricCar(Car):
	""" Represent aspects of a car, specific to electric vehicles. """

	def __init__(self, maker, model, year):
		""" Initialize attributes of the parent class"""
		super().__init__(maker, model, year)
		self.battery = Battery()


