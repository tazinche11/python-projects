# prob-1: 
# take input directory path from console and returns the files in that path 
# which name ends with one digit and extension will be .txt 
import glob
import os

def searchFile():
    files = glob.glob('../../**/*[0-9].txt', recursive = True)
    print(files)

#searchFile()

# prob-2: 
# Write a code which searches a list of files in the current folder 
# which have 'abc', '123' or 'a1b' in their names.
# How would I use one glob to perform this function? 

def searchFileP2():
    # file_search=glob.glob('./**/(abc|123).*',recursive=True)
    # print(file_search)
    for root, dirs, files in os.walk('.'):
        print("root:", root)
        print("dirs:", dirs)
        print("files: ", files)
        print("===============END==========")

searchFileP2()
