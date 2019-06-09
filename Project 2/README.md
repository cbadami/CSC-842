# Project 2 | Stegcoder | stegcoder.py

## General Information
* Author: Charles Badami
* Date: 6/6/19
* Program Name: Stegcoder
* Description/Purpose: This program is an experiment in rudimentary steganography, i.e. it allows the user to hide a secret message in a jpeg of the user's choosing. The program will also decode any message that it has encoded, given the jpeg in which it was hidden.
* Tested On: Windows 10

## Installation and Usage
First, download the script (stegcoder.py) into the directory of your choice on your Windows 10 machine.

In order to make use of the program, you will need at least one jpeg file to play with. This file should be in the same directory as stegcoder.py and should have either the .jpg or .jpeg extension.

The jpeg file used to test this program is in this repository and is located [here]().

Once the prerequisites above are satisfied, all you have to do is run the script without arguments:
```
python stegcoder.py
```
Using the menu options, the user may both encode and decode messages using different jpeg images.

## Requirements and Design
### Summary of Requirements
* Main Purpose: To encode and/or decode a message to/from a jpeg image file (rudimentary steganography).
* Features:
    * Hides a text message in a jpeg image file, image and message provided by the user.
	* Retrieves a text message from a jpeg file that was hidden by the program itself.
	* Currently supports .jpg or .jpeg only, and messages up to 99 characters long.
	
### Design Specifications
* Language: Python 3.6
* Operating System: Windows 10
* Special Modules Needed: None
* Scripts: stegcoder.py
* Other Files Needed: At least one jpeg image file (see Installation and Usage)
* User Interface: Command line
* Outputs: Text to console, output image files containing encoded messages.

## Video Demonstration

[Video demo link](https://youtu.be/-eh4hX3S47M)
