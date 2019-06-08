# Project 1 | Trilocater | trilocate.py

## General Information
* Author: Charles Badami
* Date: 5/23/19
* Program Name: trilocate.py
* Description/Purpose: This program reads in a file of comma-separated records, representing triangulation data from three cellular base stations (longitude, latitude, radius to target device based on signal strength) measured at a certain point in time. The program then calculates and displays the approximate latitude and longitude of the target device, as well as an approximate address.
* Tested On: Windows 10

## Installation and Usage
First, download the script (trilocate.py) into the directory of your choice on your Windows 10 machine.

Before using the script, you'll need to install the GeoPy module. On Windows 10:
```
1. Open an administrative command prompt.
2. Run the following command: pip install geopy
```

In addition, the script will attempt to open a file named "bsdata.txt". This file should be in the same directory as trilocate.py and contain records of comma-separated base station data, in the following format:

Note: lon=longitude in degrees, lat=latitude in degrees, r=distance (radius) to target in meters 
```
[lon of bs1],[lat of bs1],[r of bs1],[lon of bs2],[lat of bs2],[r of bs2],[lon of bs3],[lat of bs3],[r of bs3]
```
The data file used to test this program is in this repository and is located [here](https://github.com/cbadami/CSC-842/blob/master/Project%201/bsdata.txt).

Once the prerequisites above are satisfied, all you have to do is run the script without arguments:
```
python trilocate.py
```

## Requirements and Design
### Summary of Requirements
* Main Purpose: To automate the triangulation of a mobile device location, given three cell tower coordinates and distances to target.
* Features:
    * Reads data from a text file provided by the user (bsdata.txt).
	* Calculates approximate geographical coordinates of target mobile device by circular triangulation.
	* Converts geographical coordinates into approximate land address.
	
### Design Specifications
* Language: Python 3.6
* Operating System: Windows 10
* Special Modules Needed: GeoPy (Geolocation API)
* Scripts: trilocate.py
* Other Files Needed: bsdata.txt (see Installation and Usage)
* User Interface: Command line
* Outputs: Text to console

## Video Demonstration

[Video demo link](https://www.youtube.com/watch?v=bdBh8goW8VM&feature=youtu.be)
