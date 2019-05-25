#!c:/Program%Files/Python36 python.exe

# Author: Charles Badami
# Date: 5/23/19
# Program Name: trilocate.py
'''
Description/Purpose: This program reads in a file of comma-separated records,
representing triangulation data from three cellular base stations
(longitude, latitude, radius to target device based on signal strength)
measured at a certain point in time. The program then calculates and
displays the approximate latitude and longitude of the target device,
as well as an approximate address.
'''

from geopy.geocoders import Nominatim
import math

#Convert geographical coordinates to flat cartesian
def convertToXandY(lon, lat):
    x = lon * (math.pi/180) * 6378137
    y = lat * (math.pi/180) * 6378137
    return (x,y)

#Compute the intersection of three base station signals
def circIntersect(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    x1, y1 = convertToXandY(x1,y1)
    x2, y2 = convertToXandY(x2,y2)
    x3, y3 = convertToXandY(x3,y3)
    
    yA = (x2-x3) * ((x2*x2 - x1*x1) + (y2*y2 - y1*y1) + (r1*r1 - r2*r2))
    yB = (x1-x2) * ((x3*x3 - x2*x2) + (y3*y3 - y2*y2) + (r2*r2 - r3*r3))
    yC = 2 * ((y1-y2)*(x2-x3) - (y2-y3)*(x1-x2))
    y = -1*((yA-yB)/yC)
    
    xA = (y2-y3) * ((y2*y2 - y1*y1) + (x2*x2 - x1*x1) + (r1*r1 - r2*r2))
    xB = (y1-y2) * ((y3*y3 - y2*y2) + (x3*x3 - x2*x2) + (r2*r2 - r3*r3))
    xC = 2 * ((x1-x2)*(y2-y3) - (x2-x3)*(y1-y2))
    x = -1*((xA-xB)/xC)
    
    lat = y/((math.pi/180)*6378137)
    lon = x/((math.pi/180)*6378137)
    
    return (lat, lon)

#Begin main program

#Default data file path
try:
    dataFile = open("bsdata.txt","r")
except FileNotFoundError:
    print("There is a problem finding your data file. Please check and try again.")
    quit()

#Loop through records in file, give user option to quit
for line in dataFile:
    next = input("\nTriangulate next record? ")
    
    #Exit loop if user does not want to continue
    if (next.lower() != 'y'):
        dataFile.close()
        break
    
    #Convert data from strings to floats
    data = line.split(',')
    data = [float(i) for i in data]
    
    
    latResult, lonResult = circIntersect(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8])

    print ("target latitude="+str(latResult)+" target longitude="+str(lonResult))
    
    if (not(-90<latResult<90) or not(-180<lonResult<180)):
        print("Sorry, one or both coordinates out of range, check your data.")
        break
    
    #GeoPy usage to translate coordinates
    geolocator = Nominatim(user_agent="trilocate.py")
    location = geolocator.reverse(str(latResult)+", "+str(lonResult))
    print(location.address)

print("\nAll finished, goodbye!")
    
    