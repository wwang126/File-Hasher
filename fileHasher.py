import hashlib
import zlib
import glob
import os
import sys

#list of file names in directory
fileNames = []

#list files that are mkv
for filename in glob.glob('*.mkv'):
   fileNames.append(filename)

toWrite = ""
for filename in fileNames:
    print("Reading: ", filename)
    toWrite += str(filename) + "\n"
    fileIn = open(filename,"rb")
    fileBinary = fileIn.read()
    fileIn.close();
    fileHash = 0
    #hash file with crc
    fileHash = zlib.crc32(fileBinary)
    fileHex = format(fileHash, 'x')
    toWrite += "Numerical Hash: "  + str(fileHash) + "\n"
    toWrite += "Hex Hash: " + str(fileHex) + "\n"
print (toWrite)
