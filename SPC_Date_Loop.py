import datetime
from datetime import datetime

def MapDate(s):
    year, month, day = map(str, s.split('-'))
    return(year, month, day)


Start =input("Enter the date you would like to begin retrieving reports for(YYYY-MM-DD): ")
#EndDate = input("Enter the date you would like to stop retrieving reports for(YYYY-MM-DD): ")

Testing = MapDate(Start)
print(Testing)

StartDate = datetime.date(datetime.strptime(MapDate(Start),'%Y,%m,%d'))

print(StartDate)

##
##CurrentDate = StartDate
##while CurrentDate < EndDate:
##    Reports_date = CurrentDate
##    print(Reports_date)
##    CurrentDate += 1

