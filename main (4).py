# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statement. 

year = 2023

# To get year (integer input)from the user
# year = int(input("Enter a year: "))

# divided by 100 means century year(ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0):
  print("{0} is a leap year".format(year))
  
# not divided by 100 means not century year
# year divided by 4 is leap year
elif (year % 4 == 0):
  print ("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year


