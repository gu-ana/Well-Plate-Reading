import pandas as pd

filename = input("Enter filepath (please include the . extension as well):")
fileNameNoExtension = filename.split(".")[0]
found = False
print(filename.split(".")[0])
try:
    with open(filename,'r') as myfile:
        for myline in myfile:
            if myline.find("0:00:00") != -1 and found == False:
                print("time is found")
                found = True
                newFile = open(fileNameNoExtension + "Truncated" + ".txt","w+")
                newFile.write(myline)
            elif found == True:
                newFile.write(myline)
            
except FileNotFoundError:
    print("File not found, please try again")


