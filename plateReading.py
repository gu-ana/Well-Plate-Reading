# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:54:37 2019

@author: Ana
"""

import pandas as pd
import numpy as np
import csv
#filename = input("Enter filepath (please include the . extension as well):")
filename = r"C:\Users\Ana\Documents\Imaging\lamp angptl2 test 2(copy).txt"
fileNameNoExtension = filename.split(".")[0]
found = False
firstTime= False
print(filename.split(".")[0])

try:
    with open(filename,'r') as myfile:
        for myline in myfile:
            if found == True:
                newFile.write(myline)
            elif myline.find("Time") != -1 and firstTime == False:
                firstTime = True
            elif myline.find("Time") != -1 and firstTime == True:
                found = True
                newPath = fileNameNoExtension + "Truncated" + ".txt"
                newFile = open(newPath,"w+")
                newFile.write(myline)
            
                
    newFile.close()
    
except FileNotFoundError:
    print("File not found, please try again")
    
#data = np.loadtxt(newPath,delimiter = '\t', dtype = str)
#print(data)

numberOfWells = input("Enter set of wells. Use commas to separate the wells: ").split(',')
totalWells = list(['Time'] + numberOfWells)
print(totalWells)
def yes_or_no(totalWells):
    check = str(input("More well sets? (Y/N):")).lower().strip()
    try:
        if check == 'y':
            numberOfWells = input("Enter set of wells. Use commas to separate the wells: ").split(',')
            totalWells = np.append(totalWells,list(['Time']+numberOfWells))
            print(totalWells) #well duh, but the system thinks every individual character is [0][0] index.
            return yes_or_no(totalWells)
        elif check == 'n':
            return
        else:
            print('Invalid Input')
            return yes_or_no(totalWells)
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return yes_or_no(totalWells)

yes_or_no(totalWells)

data = pd.read_csv(newPath,delimiter = '\t',usecols = totalWells,nrows = 31)


#print(data)

dataMean = data.mean(axis = 1)
print(dataMean)
