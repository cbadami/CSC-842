#!c:/Program%Files/Python36 python.exe

# Author: Charles Badami
# Date: 6/21/19
# Program Name: Imagepass

'''
Description/Purpose: This program is the first iteration of simple algorithm
that uses an image to generate a pseudo-random, 16-character password, using base64 encoding.
In order to retrieve a forgotten password, the tool uses a simple offset number
and the original image.
'''

import base64
import random

#User menu prompt for main program
def menu():
    return input("\nWould you like to (g)enerate or (r)etrieve a password ((q) to quit)? : ")

#Convert image file to base64 encoding
def convertImg(filename):
    
    #Check extension, must be png
    if (filename[-4:].lower() != ".png"):
        print("\nThere seems to be a problem with your file extension. Please try again...")
        return -1
    
    #Attempt to open file
    try:
        image = open(filename,'rb')
    except FileNotFoundError:
        print("\nThere is a problem finding your image file. Please check and try again.")
        return -1
    
    #Encode file
    txt = base64.b64encode(image.read())
    
    return txt

#Use offset to generate password
def extractPass(txt,offset):
    return txt[offset:offset+16]

##############
#Main program
print("Welcome to ImagePass!")
choice = menu()

while (choice.lower() != 'q'):
    
    if (choice != 'g' and choice != 'r'):
        print("Please enter a valid choice...")
        choice = menu()
        continue
    
    #Password generation option
    if (choice == 'g'):
        file = input("\nPlease enter the filename of the png you would like to use: ")
        
        txt = convertImg(file)
        
        #Error checking
        if (txt == -1):
            choice = menu()
            continue
        
        #Choose random offset
        offset = random.randint(99,199)
        
        pw = extractPass(txt,offset)
        print("\nYour password is " + pw.decode('ASCII') + ", and your offset is " + str(offset) + ".\n")
        print("Please save your offset number and png file in case you need to retrieve your password.")
        print("If your password is not satisfactory, try again with the same or different png...")
        
    #Password retrieval option        
    if (choice == 'r'):
        file = input("Please enter the filename of the png containing your password: ")
        off = int(input("Please enter the offset number of your password: "))
        
        txt = convertImg(file)
        
        #Error checking
        if (txt == -1):
            choice = menu()
            continue
        
        pw = extractPass(txt,off)
        print("\nBased on that information, your password is " + pw.decode('ASCII'))

        
    choice = menu()
    

print("Goodbye!")
