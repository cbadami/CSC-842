#!c:/Program%Files/Python36 python.exe

# Author: Charles Badami
# Date: 7/19/19
# Program Name: PyWake

'''
Description/Purpose: This program, in conjunction with Windows 10 Task Scheduler and Outlook mail client,
sends a notification email to the owner of a workstation upon waking from sleep. This is merely a basic
template and can be modified with different parameters, to include attachments, etc.

'''
#Module that allows control of Outlook
import win32com.client as win32

#Create and send simple email.

mail = win32.Dispatch('outlook.application').CreatItem(0)
mail.To = 'recipient@email.com' #Replace with actual recipient address
mail.Subject = 'PyWake Trigger'
mail.Body = 'Your workstation is awake!'

#Can add modifications, such as adding attachments

mail.Send()