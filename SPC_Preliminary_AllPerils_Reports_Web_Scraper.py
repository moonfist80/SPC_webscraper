'''
Author:  Adam Dawson
Date Modified:  7/13/2016

Gets preliminary filtered hail reports from the
SPC Storm Reports page

Relies on the following packages:
Beautiful Soup
urllib
csv
os
time

Custom Built function:
SPC_Date_Loop.py (this file must be stored wherever
other python packages/scripts are at)
Iterates over the date range provided by the user
and returns a list of dates.
Dates are then iterated over to produce the urls for
each CSV file. 
'''
from bs4 import BeautifulSoup
import urllib.request
import csv
import os
import sys
from SPC_Date_Loop import Date_Loop 
from time import sleep

i = 0
while i==0:
    print('Please input the type of report you would like to receive data for.')
    sleep(1)
    print('Enter ''tornado'' for tornado reports, ''hail'' for hail reports, or ''wind'' for wind reports')
    sleep(1)
    user_report_type = str(input('Enter either tornado, hail, or wind: '))
    if user_report_type == 'tornado':
        print('You have selected tornado reports.')
        report_type = 'torn'
        i += 1
    elif user_report_type == 'hail':
        print('You have selected hail reports.')
        report_type = 'hail'
        i += 1
    elif user_report_type == 'wind':
        print('You have selected wind reports.')
        report_type = 'wind'
        i += 1
    else:
        print('You have entered an invalid format for your reports.  Please try again.')

        
DateList = Date_Loop()
SPC_Base = 'http://www.spc.noaa.gov/climo/reports/'
reports_tag = '_rpts_filtered_' + report_type + '.csv'
header = 'ReportType, Date, Time, Size, Location, County, State, Latitude, Longitude, Comments, \n'



with open('SPC_Reports_Final.csv','w') as FinalTable:
    FinalTable.write(header)


for i in DateList:
    with open('temp_reports.csv','w+') as temp_reports, open('SPC_Reports_Final.csv','a+') as FinalTable:
        Reports_date = str(i)
        website = urllib.request.urlopen(SPC_Base + Reports_date + reports_tag)
        Weather_soup = BeautifulSoup(website, 'lxml').get_text()
        temp_reports.write(Weather_soup)
        
#       Set the cursor at the beginning of 'temp_reports' (our written csv file)
#       for each row in the output, excluding the rows that have the header information
#       write the date followed by each row into the final table.
        temp_reports.seek(0,0)
        for row in temp_reports:
            if not row.startswith('Time'):
                FinalTable.write(report_type + ',' + Reports_date + ',' + row)
##        
        print('Thinking...')
        sleep(4) #Play nice with the SPC servers



#clean up the dummy table
try:
    os.remove('temp_reports.csv')
except:
    raise


print('File is saved wherever your script is saved!')

