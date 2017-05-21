#Program to calculate Squares of Numbers

#Calculate square from 1 till the user input number
def SquareOfNumbers(n):
	while (n > 100 or n <= 0):
		n = input("Please enter a number between 1-100:")
	print ("The Squares are: ")
	for i in range (1, n+1):
		dict = {i: i**2}
		print (dict)
	return

n = eval(input("Enter a Number (1-100): ")) # n = The user input
SquareOfNumbers(n)
