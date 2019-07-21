# Project 5 | PyWake

## General Information
* Author: Charles Badami
* Date: 7/19/19
* Program Name: pyWake.py
* Description/Purpose: This program, in conjunction with Windows 10 Task Scheduler and Outlook mail client, sends a notification email to the owner of a workstation upon waking from sleep. This is merely a basic template and can be modified with different parameters, to include attachments, etc.
* Tested On: Windows 10 

## Installation and Usage
First, download the script (pyWake.py) into the directory of your choice on your Windows 10 machine. Note: In order to run the program, you will need to, at minimum, replace the recipient email address with a real value.

Before using the script, you'll also need to install the pypiwin32 package. On Windows 10:
```
1. Open an administrative command prompt.
2. Run the following command: pip install pypiwin32
```

You will also need to satisfy the following tasks for full functionality as originally intended:
```
1. Make sure you are logged into the Outlook desktop application with a valid email address.
2. Create a new task in the Windows Task Scheduler with the following properties:
	a. Add a Trigger to begin the task "On an event." Set Log to "System", Source to "Power-Troubleshooter", and Event ID to 1.
	b. Add an Action with your python.exe path in the Program/script field. Use pyWake.py as an argument, and put the path to that script into the "Start in" field.
	c. Feel free to tweak other settings as you would like.
```

Initially, you may want to Run the task manually to make sure an email is being sent and received. Then, try putting your machine to sleep, then waking from sleep. You should receive a new email alerting you to this event.

## Requirements and Design
### Summary of Requirements
* Main Purpose: This tool is a basic alert by email that notifies a user when the user's workstation wakes from sleep.
* Features:
    * Sends an email automatically to the user when the workstation wakes from sleep.
	* Uses the Outlook desktop client as the source of the email in conjunction with Task Scheduler.
	* Customizable for the ability to add attachments, etc.
	
### Design Specifications
* Language: Python 3.6
* Operating System: Windows 10 with Outlook
* Special Modules Needed: Pypiwin32
* Scripts: pyWake.py
* Other Files Needed: none
* User Interface: Automatic after initial setup
* Outputs: Alert sent to user-selected email address.


## Video Demonstration

[Video demo link](https://youtu.be/N3L1mr0fzps)
