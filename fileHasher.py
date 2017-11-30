import hashlib
import zlib
import glob
import os
import sys, getopt

#takes a fileName and returns it as a hex value
def crc32(fileName):
    bufferSize = 65536
    with open(fileName, "rb") as fileIn:
        fileBinary = fileIn.read(bufferSize)
        fileHash = 0
        while len(fileBinary) > 0:
            #hash file with crc
            fileHash = zlib.crc32(fileBinary, fileHash)
            fileBinary = fileIn.read(bufferSize)
        return fileHash

def sfvWriter():
    #list of file names in directory
    fileNames = []

    #list files that are mkv
    for filename in glob.glob('*.mkv'):
       fileNames.append(filename)

    toDisplay = ""
    toWrite = ";SFV Test\n"
    for filename in fileNames:
        print("Reading: ", filename)
        toDisplay += str(filename) + "\n"
        toWrite += str(filename)
        fileHex = format(crc32(filename), 'x')
        toDisplay += "Numerical Hash: "  + str(fileHash) + "\n"
        toDisplay += "Hex Hash: " + str(fileHex) + "\n"
        toWrite += " " + str(fileHex) + "\n"
    print (toDisplay)

    fileWrite = open("SFVtest.sfv" , "w+")
    fileWrite.write(toWrite)
    fileWrite.close()

#Reads .sfv files
def sfvChecker(sfvName):
    sfvFile = open(sfvName, "r")
    line = sfvFile.readline()
    while line:
        print(line)
        fileName = line[0:-10]
        fileHash = line[-9:-1]
        print("File Name: ", fileName)
        print("File Hash: ", fileHash)
        hashChecker(fileName,fileHash)
        line = sfvFile.readline()
#Checks if a file matches its CRC32 hash
def hashChecker(fileName,fileHash):
    fileHex = format(crc32(fileName), 'x')
    print("Comparing: ", fileHex , " and " , fileHash)
    if(fileHex == fileHash):
        print("\033[0;32mFile is OK!\033[0;0m")
    else:
        print("\033[1;31mFile is not ok.\033[0;0m")

def main():
    #sfvWriter()
    sfvName = "SFVtest.sfv"
    sfvChecker(sfvName)

if __name__ == "__main__":
    main()
