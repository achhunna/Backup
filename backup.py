''' Script to copy file into Backup/ folder with timestamp on filename (C) 2015 Achhunna Mali'''
# Hosted on GitHub https://github.com/achhunna/Backup

import os
import shutil
from datetime import datetime

# Define timestamp format
timeStamp = "%b%d%Y_%I%M%S %p"
timeStampStr = datetime.now().strftime(timeStamp)


# Define network location path
locationPath = "//rws-filer1/GMO_finance/Database/"

# Define file copying function
def copyFile(old_file_name, new_file_name, folderName):
        src_dir= os.curdir
        dst_dir= os.path.join(os.curdir , folderName)
        src_file = os.path.join(src_dir, old_file_name)
        shutil.copy2(src_file,dst_dir)
        
        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)
		
# Declare filename and folder variable
fullFileName = "Feeder.xlsx"
folder = "Backup"

# Split extension
periodLoc = fullFileName.find(".")
fileName = fullFileName[:periodLoc]
extension = fullFileName[periodLoc:]

# Create timestamp filename
timeStampName = fileName + "_" + timeStampStr + extension

# Change directory
os.chdir(locationPath)

# Copy timestamp file into folder
try:
		copyFile(fullFileName, timeStampName, folder)
		print("Done!")
except Err:
		print("Error:" + Err)

