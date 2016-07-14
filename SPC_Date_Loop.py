'''
Author:  Adam Dawson
Date Modified:  7/13/2016

Date reader for SPC Storm Reports page.  User inputs a date string, then the function makes sure
the dates are in the correct format and spits out the dates needed.  
'''
def Date_Loop():
    import datetime
    from datetime import datetime, timedelta
    Date_List = []
    while True:
        Start =str(input("Enter the date you would like to begin retrieving reports for(YYMMDD): "))
        End = str(input("Enter the date you would like to stop retrieving reports for(YYMMDD): "))
        ##Exception handling for datetime functions
        try:
            StartDate = datetime.strptime(Start,'%y%m%d').date() ##strptime converts the string in the listed format to a datetime format
            EndDate = datetime.strptime(End,'%y%m%d').date()
            break
        except:
            print("Incorrect Date Format.  Please try again.")

    if StartDate > EndDate: ##want dates to be listed sequentially in order so we can loop over the SPC reports page
        print("Your dates are in the wrong order.  Resorting...")
        Reorder_toEndDate = StartDate
        Reorder_toStartDate = EndDate
        StartDate = Reorder_toStartDate
        EndDate = Reorder_toEndDate
    else:
        print("Dates look OK!")
    
    while StartDate <= EndDate:
        Date_List.append(StartDate.strftime('%y%m%d'))
        StartDate += timedelta(days=1)
        

    return(Date_List)


if __name__ == '__main__':
    Date_Loop()
