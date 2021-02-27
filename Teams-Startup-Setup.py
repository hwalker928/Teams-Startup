import datetime
import subprocess
import getpass
import os.path
from shutil import copyfile

no = datetime.datetime.today().weekday()
username = getpass.getuser()
path = r'C:\Users\\' + username + r'\AppData\Local\Microsoft\Teams\current\Teams.exe'
startup_path = r'C:\Users\\' + username + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
already_exists_in_startup = os.path.isfile(startup_path + "\\teams.py")
if not already_exists_in_startup:
    copyfile("Teams-Startup-Setup.py", startup_path + "\\teams.py")
if no < 5:
    subprocess.call([path])
