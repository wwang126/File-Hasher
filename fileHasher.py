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
fileHash = zlib.crc32(fileBinary)
#hash file with crc
print(fileHash)
fileHash.close()
