import os 
from zipfile import ZipFile 
import sys
sys.path.insert(0,'./.history')
from history import SaveHistory

def extractZipFile(fileName):
    SaveHistory(fileName)
    zip = ZipFile(fileName,'r')
    
    print("\nAll files :-")
    zip.printdir()
    zip.extractall()
    foldName = os.path.splitext(fileName)[0]
    print(f"\nSuccessfully Save.\nFolder name :- {foldName}")
    

def allZipFiles():
    allFiles = os.listdir()
    allZipFiles=[]
    
    for allFile in allFiles:
        file = os.path.splitext(allFile)[1]
        
        if file == ".zip":
            allZipFiles.append(allFile)
    
    ind = 1
    print("\nAll Zip file in this folder.")
    for zipFile in allZipFiles:
        print(f"{ind} - {zipFile}")
        ind = ind + 1
    print("\n")
    return allZipFiles    


zipFiles = allZipFiles()

if len(zipFiles)==0:
    print(f"No Zip file found !\nPlease save the zip file in this folder and run code.")
else:
    selectedFile = int(input("Please input the Zip file index no : "))
    
    if selectedFile<=len(zipFiles) :
        print("\nYou have selected :- ")
        print(f"{selectedFile} - {zipFiles[selectedFile-1]}")
        
        extractZipFile(zipFiles[selectedFile-1])
    else:
        print('Please input a valid index.\nRun again.')