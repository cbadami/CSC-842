#!c:/Program%Files/Python36 python.exe

# Author: Charles Badami
# Date: 6/6/19
# Program/Script Name: stegcoder.py

'''
Description/Purpose: This program is an experiment in rudimentary steganography,
i.e. it allows the user to hide a secret message in a jpeg of the user's
choosing. The program will also decode any message that it has encoded,
given the jpeg in which it was hidden.

'''

#User menu prompt for main program
def menu():
    return input("Enter (1) to encode a message, (2) to decode, (q) to quit: ")


#Count bytes in image file
def imageSize(f):
    inFile = open(f,'rb')
    c = 0
    while 1:
        b = inFile.read(1)
        if not b:
            break
        c += 1
    inFile.close()
    return c


#Algorithm to hide a message in chosen image file
def writeSecret(file, modSecret, start, key):
    
    #Read in image, write out image with steganography
    inFile = open(file,'rb')
    outFile = open("steg_"+file,'wb')
    
    #Beginning of file is identical to original
    front = inFile.read(start)
    outFile.write(front)

    
    for l in modSecret:         
        if (l == '~'):
            outFile.write(inFile.read(1))
            continue
        outFile.write(l.encode('ASCII'))
        inFile.read(1)
    outFile.write(key[0].encode('ASCII'))
    inFile.read(1)
    outFile.write(key[1].encode('ASCII'))
    inFile.read(1)
    end = inFile.read(2)
    outFile.write(end) 
       
    outFile.close()
    inFile.close()
    
    return

#Overall message encoding function 
def encode():
    
    #Get source image file where user wants to hide secret
    fName = input("\nYou chose to encode a message.\nEnter the name of the jpeg file to use: ")
    
    #Check extension, must be jpg or jpeg
    if (fName[-4:].lower() != ".jpg" and fName[-5:] != ".jpeg"):
        print("\nThere seems to be a problem with your file extension. Please try again...")
        return
    
    #Probe file for size in bytes
    try:
        lastByte = imageSize(fName) - 1
    except FileNotFoundError:
        print("\nThere is a problem finding your image file. Please check and try again.")
        return
    
    #Get secret that user wants to hide
    secret = ""
    while (len(secret) < 1 or len(secret) > 99):
        secret = input("Please enter a secret you wish to embed (1-99 characters): ")
    
    #Length of secret (1-99), retrieved later by decoding function (0-99)
    key = len(secret)

    #Pad key if necessary
    if (key < 10):
        key = str("0" + str(key))
    else:
        key = str(key)

    #Obfuscate secret
    modSecret = '~'.join(secret)

    #Calculate location to write into image
    offSet = 2 * len(secret) + 2
    start = lastByte - offSet

    #Read in image, write out image with steganography
    writeSecret(fName, modSecret, start, key)
    
    print("Secret encoded. Output file is steg_" + fName + "\n")
    
    return

#Overall message decoding function
def decode():
       
    #Get source image file containing secret
    fName = input("\nYou chose to decode a message.\nEnter the name of the jpeg file to use: ")
    
    #Check extension, must be jpg or jpeg
    if (fName[-4:].lower() != ".jpg" and fName[-5:] != ".jpeg"):
        print("\nThere seems to be a problem with your file extension. Please try again...")
        return
    
    #Probe file for size in bytes
    try:
        lastByte = imageSize(fName) - 1
    except FileNotFoundError:
        print("\nThere is a problem finding your image file. Please check and try again.")
        return
    
    #Initialize key variable
    k = ''

    #Retrieve length of secret
    f = open(fName, 'rb')
    f.read(lastByte - 3)  
    k = f.read(2)
    
    f.close()
    
    try:
        off = 2 * int(k) + 2
    except ValueError:
        print("Are you sure this image was encoded with this program? Try again...\n")
        return

    #locate and extract message encoded by this program
    f = open(fName, 'rb')
    f.read(lastByte - off)
    s = f.read(2 * int(k) - 1)
    
    f.close()

    #Put message back together
    msg = ""
    for t in range(0, len(s), 2):
        msg += chr(s[t])
        
    print("Decoded message is: " + msg + "\n")

    return   



#main program
print("Welcome to Stegcoder!\n")
choice = menu()

while (choice.lower() != 'q'):
    
    
    if (choice != '1' and choice != '2'):
        print("Please enter a valid choice...\n")
        choice = menu()
        continue
    
    if (choice == '1'):
        encode()     
        
    if (choice == '2'):
        decode()
        
    choice = menu()
    
    
