import hashlib
import zlib
import glob
import os
import sys, getopt

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
        fileIn = open(filename,"rb")
        fileBinary = fileIn.read()
        fileIn.close()
        fileHash = 0
        #hash file with crc
        fileHash = zlib.crc32(fileBinary)
        fileHex = format(fileHash, 'x')
        toDisplay += "Numerical Hash: "  + str(fileHash) + "\n"
        toDisplay += "Hex Hash: " + str(fileHex) + "\n"
        toWrite += " " + str(fileHex) + "\n"
    print (toDisplay)

    fileWrite = open("SFVtest.sfv" , "w+")
    fileWrite.write(toWrite)
    fileWrite.close()

def main():
    sfvWriter()

if __name__ == "__main__":
    main()
