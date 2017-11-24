import hashlib
import zlib
import glob
import os
import sys

#file storage
fileNames = []

#list files that are mkv
for filename in glob.glob('*.mkv'):
   fileNames.append(filename)

for filename in fileNames:
    print(filename)

print(fileNames[0])
fileBinary = open(fileNames[0],"rb").read()
fileHash = 0
#hash file with crc
fileHash = zlib.crc32(fileBinary)
#fileBinary.close()
fileHex = hex(fileHash)
print("Numerical Hash: " ,fileHash)
print("Hex Hash: ", fileHex)
