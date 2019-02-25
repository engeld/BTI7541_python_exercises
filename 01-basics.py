#
# BasisFunctions/Methods
#
import math

# Develop a function that computes the area of a disc of a given radius.
def calc_disc(radius):
	disc = math.pi * radius ** 2
	print('1. The area of a disc with the radius of ' + str(radius) + ' is ' + str(disc))

# Develop a function that returns the greatest value of a list of positive numbers.
def find_greatest(list_pos_numbers):
	highest_val = 0
	for number in list_pos_numbers[:]:
		if (number > highest_val):
			highest_val = number
	print('2. The highest value in the list is ' + str(highest_val))


# Develop a function that reverse a list of elements.
def reverse_list(the_list):
	list_index = len(the_list)-1
	reversed_list = []

	for i in range(len(the_list)):
		reversed_list.append(the_list[list_index])
		list_index= list_index-1

	print('3. The list of "' + str(the_list) + '" is reversed as "' + str(reversed_list) + '"')

def main():
	#Launcher
	calc_disc(15)

	list_numbers = [1, 4, 21, 16, 29, 19, 20, 31]
	find_greatest(list_numbers)

	the_list_to_reverse = [12, 18, 21, 19, 8, 7, 3, 9]
	reverse_list(the_list_to_reverse)

if __name__ == "__main__":
	main()
