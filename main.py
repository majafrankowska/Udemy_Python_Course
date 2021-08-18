# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#You have x days, y weeks, and z months left. 
#    There are 365 days in a year, 52 weeks in a year and 12 months in a year. 

days90 = 90 * 365 
weeks90 = 90 * 52 
months90 = 90 * 12 

daysage = int(age) * 365
weeksage = int(age) * 52
monthsage = int(age) * 12 

cat1 = int(days90) - daysage
cat2 = int(weeks90) - weeksage
cat3 = int(months90) - monthsage

print(f"You have {cat1} days, {cat2} weeks, and {cat3} months left. ")

dogage = input("What is your dog's current age? ")

days12 = 12 * 365 
weeks12 = 12 * 52 
months12 = 12 * 12

daysagedog = int(dogage) * 365
weeksagedog = int(dogage) * 52
monthsagedog = int(dogage) * 12 

dog1 = int(days12) - daysagedog
dog2 = int(weeks12) - weeksagedog
dog3 = int(months12) - monthsagedog 

print(f"Your dog has {dog1} days, {dog2} weeks, and {dog3} months left. ")