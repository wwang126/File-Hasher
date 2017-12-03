import hashlib
import zlib
import glob
import os
import sys, getopt
import argparse

#takes a fileName and returns it as a hex value
def crc32(fileName):
    try:
        fileIn = open(fileName, "rb")
    except IOError:
        print ("Couldn't read file : ", fileName)
        sys.exit()
    except FileNotFoundError:
        print (fileName, " not found!")
        sys.exit()
    #64kb buffer
    bufferSize = 65536
    with fileIn:
        fileBinary = fileIn.read(bufferSize)
        fileHash = 0
        while len(fileBinary) > 0:
            #hash file with crc
            fileHash = zlib.crc32(fileBinary, fileHash)
            fileBinary = fileIn.read(bufferSize)
    return fileHash


def sfvWriter(outputName):
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
        toDisplay += "CRC32 Hash: " + str(fileHex) + "\n"
        toWrite += " " + str(fileHex) + "\n"
    print (toDisplay)

    fileWrite = open(outputName , "w+")
    fileWrite.write(toWrite)
    fileWrite.close()

#Reads .sfv files
def sfvChecker(sfvName):
    try:
        sfvFile = open(sfvName, "r")
    except FileNotFoundError:
        print("Invalid File Name!")
        sys.exit()
    #If no error read and check
    with sfvFile:
        line = sfvFile.readline()
        while line:
            if(line[0] != ';'):
                print(line)
                fileName = line[0:-10]
                fileHash = line[-9:-1]
                print("File Name: ", fileName)
                print("File Hash: ", fileHash)
                hashChecker(fileName,fileHash)
                line = sfvFile.readline()
            else:
                line = sfvFile.readline()
#Checks if a file matches its CRC32 hash
def hashChecker(fileName,fileHash):
    fileHex = format(crc32(fileName), 'x')
    if(fileHex == fileHash):
        print("\033[0;32mFile is OK!\033[0;0m")
    else:
        print("\033[1;31mFile is not ok.\033[0;0m")

def main():
    #arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', action= 'store',
                        dest= 'outputName',
                        help='Set .sfv output name' )
    parser.add_argument('-i', action= 'store',
                        dest= 'inputName',
                        help='Set .sfv to read' )
    parser.add_argument('-s', '--hash', action='store_true',
                        default=False, dest='hash',
                        help='hash if set' )
    parser.add_argument('-v', '--verify', action='store_true',
                        default=False, dest='verify',
                        help='Verify\'s sfv file is true')
    args = parser.parse_args()
    if(args.hash):
        print("Hashing")
        print(args.outputName)
        sfvWriter(args.outputName)
    if(args.verify):
        print("Verifying: ", args.inputName)
        sfvChecker(args.inputName)
    #sfvWriter()
    #sfvName = args.outputName
    #sfvChecker(sfvName)

if __name__ == "__main__":
    main()
