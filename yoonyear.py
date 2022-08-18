year = input("year : ")
year = int(year)

if (year % 400 == 0)and(year % 100 == 0 and year % 4 ==0):
    print("yoon-yeun")
    
elif (year % 4 == 0 and year % 100 != 0):
    print("yoon-yeun")

else:
    print("pyung-yeun")

