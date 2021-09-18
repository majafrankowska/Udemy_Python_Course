#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
# rounding to 2 places: round(1.4444,2) ,2 zaokrągl do dwóch miejsc po przecinku
#round(1.4756,2)

# "Welcome to the tip calculator. "
print("Welcome to the tip calculator. ")

cat = float(input("What was the total bill? $"))


cat1 = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
 

cat2 = int(input("How many people to split the bill? "))

cat3 = float("1." + str(cat1))

cat9 = (cat / cat2) * cat3
cat10 = round(cat9, 2)
print(f"Each person should pay: ${cat10}")


# 1+= cat
# (150.00 / 5) * 1.12 = 33.6 
