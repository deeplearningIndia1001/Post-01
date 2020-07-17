#I.G : @deeplearningindia
from datetime import datetime
Todays_Date = int( datetime.today().strftime ('%d') )
print( datetime.today().strftime ('%d:%m:%Y') )
if Todays_Date%2 ==0:
	New_Post = True
else:
	New_Post = False
print("NEW POST :" , New_Post)
