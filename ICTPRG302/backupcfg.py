import sys
import pathlib
from pathlib import Path
import smtplib
import shutil
from datetime import datetime
from zoneinfo import ZoneInfo
import logging

Email = ""

###################
#Sets timezone to Melbourne & time stamp variable with YYYYMMDD-HHMMSS format
###################
TimeZone = ZoneInfo("Australia/Melbourne")
TimeStamp = datetime.now(TimeZone).strftime("%Y%m%d-%H%M%S")

###################
#Sets path root to cut down on writing
###################
Root = "/home/ec2-user/environment/ICTPRG302"

###################
#Configures logs' format & location
###################
logging.basicConfig(
    filename='backup.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

###################
#SMTP Emailing Config
###################
smtp = {"enabled": True,
        "sender": "bek.j.jones@gmail.com",          # gmail.com sender
        "recipient": "randerson@sunitafe.edu.au",       # gmail.com recipient
        "server": "smtp.gmail.com",             # SMTP server
        "port": 587,                            # SMTP port
        "user": "bek.j.jones@gmail.com",            # gmail.com user
        "password": "gl0rygl0ry2GOD"}     # gmail.com password

# ORIGINAL email code
#smtp = {"sender": "30028720@students.sunitafe.edu.au",
#        "recipient": "randerson@sunitafe.edu.au",
#        "server": "smtp.elasticemail.com", 
#        "port": 2525, 
#        "user": "30028720@students.sunitafe.edu.au", 
#        "password": "BECA310CB4C1743600B79E1EB5C3C3466EC1"} 

###################
#Defines multiple differnet backup jobs & error hnadling
###################
#.txt file backup
def job1():
    global Email
    global SrcFile
    global DstFile
    SrcFile = Path(f"{Root}/Files/ImportantFile.txt")
    DstFile = Path(f'{Root}/Backups/ImportantFile_{TimeStamp}.txt')
    try:
        pathlib.Path.exists(SrcFile)
        print("File found...")
        shutil.copy2(SrcFile, DstFile)
        print(f"SUCCESS: File {DstFile} has been successfully saved")
        logging.info(f"{DstFile} was successfully backed up")
    except PermissionError as e:
        print(f"ERROR: Insufficient privileges - {e}")
        logging.error(f"{SrcFile} was unable to backup due to insufficient privileges")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup due to insufficient privileges") + '\n'
        ErrorEmail()
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        logging.error(f"{SrcFile} was unable to backup as file/directory could not be found")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup as file/directory could not be found") + '\n'
        ErrorEmail()

#.pdf file backup
def job2():
    global Email
    global SrcFile
    global DstFile
    SrcFile = Path(f"{Root}/Files/ImportantFile.pdf")
    DstFile = Path(f'{Root}/Backups/ImportantFile_{TimeStamp}.pdf')
    try:
        pathlib.Path.exists(SrcFile)
        print("File found...")
        shutil.copy2(SrcFile, DstFile)
        print(f"SUCCESS: File {DstFile} has been successfully saved")
        logging.info(f"{DstFile} was successfully backed up")
    except PermissionError as e:
        print(f"ERROR: Insufficient privileges - {e}")
        logging.error(f"{SrcFile} was unable to backup due to insufficient privileges")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup due to insufficient privileges") + '\n'
        ErrorEmail()
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        logging.error(f"{SrcFile} was unable to backup as file/directory could not be found")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup as file/directory could not be found") + '\n'
        ErrorEmail()
    
#.docx file backup
def job3():
    global Email
    global SrcFile
    global DstFile
    SrcFile = Path(f"{Root}/Files/ImportantFile.docx")
    DstFile = Path(f'{Root}/Backups/ImportantFile_{TimeStamp}.docx')
    try:
        pathlib.Path.exists(SrcFile)
        print("File found...")
        shutil.copy2(SrcFile, DstFile)
        print(f"SUCCESS: File {DstFile} has been successfully saved")
        logging.info(f"{DstFile} was successfully backed up")
    except PermissionError as e:
        print(f"ERROR: Insufficient privileges - {e}")
        logging.error(f"{SrcFile} was unable to backup due to insufficient privileges")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup due to insufficient privileges") + '\n'
        ErrorEmail()
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        logging.error(f"{SrcFile} was unable to backup as file/directory could not be found")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup as file/directory could not be found") + '\n'
        ErrorEmail()

#/Files directory backup
def job4():
    global Email
    global SrcFile
    global DstFile
    SrcFile = Path(f"{Root}/Files/")
    DstFile = Path(f'{Root}/Backups/Files_{TimeStamp}')
    try:
        pathlib.Path.exists(SrcFile)
        print("File found...")
        shutil.copytree(SrcFile, DstFile)
        print(f"SUCCESS: File {DstFile} has been successfully saved")
        logging.info(f"{DstFile} was successfully backed up")
    except FileExistsError as e:
        print(f"ERROR: Directory already exists - {e}")
        logging.error(f"{SrcFile} was unable to backup as file/directory already exists")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup as file/directory already exists") + '\n'
        ErrorEmail()
    except PermissionError as e:
        print(f"ERROR: Insufficient privileges - {e}")
        logging.error(f"{SrcFile} was unable to backup due to insufficient privileges")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup due to insufficient privileges") + '\n'
        ErrorEmail()
    except FileNotFoundError as e:
        print(f"Error: Directory not found - {e}")
        logging.error(f"{SrcFile} was unable to backup as file/directory could not be found")
        Email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] +'\n' + 'Subject: Backup Error\n\n' + (f"FILE BACKUP ERROR: {SrcFile} was unable to backup as file/directory could not be found") + '\n'
        ErrorEmail()
        

def ErrorEmail():
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], Email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: Send email failed: " + str(e), file=sys.stderr)
        logging.error("ERROR: Send email failed: " + str(e), file=sys.stderr)