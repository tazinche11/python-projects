# prob-1: 
# take input directory path from console and returns the files in that path 
# which name ends with one digit and extension will be .txt 
import glob

def searchFile():
    files = glob.glob('./test-data/*[0-9].txt')
    print(files)

searchFile()