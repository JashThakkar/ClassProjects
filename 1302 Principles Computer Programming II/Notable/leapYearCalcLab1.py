# Leap Year Calculator: Takes an inpute of a year, and outputes if it will be a leap year or not

year = input('Year: ')
digits = False

if int(year[2]) != 0:
    digits = True
  
elif int(year[3]) != 0:
    digits = True

if digits:
    remainder = int(year) % 4
  
    if remainder != 0:
        print(year + " - not a leap year")
      
    elif remainder == 0:
        print(year + ' - leap year')
      
else:
    remainder = int(year) % 400
  
    if remainder == 0:
        print(year + ' - leap year')
      
    elif remainder != 0:
        print(year + " - not a leap year")
