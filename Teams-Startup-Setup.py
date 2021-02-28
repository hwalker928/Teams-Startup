# Imports
import datetime
import subprocess
import getpass
import os.path
from shutil import copyfile

# Variables
username = getpass.getuser() # Gets the username of the current Windows User, e.g. Administrator, kevin, steve
startup_path = r'C:\Users\\' + username + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\\teams.py' # Location of startup folder

# Copying + opening
if not os.path.isfile(startup_path): # If the file isn't already in the startup folder (usually first-time run)
    copyfile(__path__, startup_path) # Copy this script to the startup folder
if datetime.datetime.today().weekday() < 5: # If it is monday - friday
    subprocess.call([r'C:\Users\\' + username + r'\AppData\Local\Microsoft\Teams\current\Teams.exe']) # Open Teams
