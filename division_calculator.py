while True:
	first_number = input("\n first_number:")
	if first_number == 'q':
		break
	second_number = input("\n second_number:")
	if second_number == 'q':
		break
	try:
		answer= int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by zero")
	else:
		print(answer)