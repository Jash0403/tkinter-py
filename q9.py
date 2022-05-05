print("List of months: January, February, March, April, May, June, July, August, September, October, November, December : ")
month=input("Enter Month : ")
if month == "February":
	print("Nunber of days: 28/29 days")
elif month in ("April", "June", "September", "November"):
	print("Number of days: 30 days")
elif month in ("January", "March", "May", "July", "August", "October", "December"):
	print("Number of days: 31 day")
else:
	print("Month Name Wrong")