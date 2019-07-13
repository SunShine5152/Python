temp = input('pls input a year:')
year = int(temp)

if ((year%4==0 and year%100 != 0) or year%400==0):
	print('it is run year')
else:
	print('it is not run year')
