# challenge3
__author__ = 'Kyle Latino'
#
#
# Used stackoverflow to learn how to create directories: https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
#
# imports
import struct
import hashlib
import os

# functions
# get md5 hash of each file
def hashMD5(fileDat):
    with open(fileDat, 'r') as hashFile:
        f1 = hashlib.md5()
        fileBytes = hashFile.read(4096)
        while len(fileBytes) > 0:
            f1.update(fileBytes)
            fileBytes = hashFile.read(4096)
            print(f1.hexdigest())

# create new bitmap file from offset and length
def createBMP(originFile, offset, length):
    with open(originFile, 'rb') as origin:
        newFileName = directory + str(offset) + '.bmp'
        with open(newFileName, 'wb+') as newImage:
            origin.seek(offset)
            newImage.write(origin.read(length))

        outputFiles.append(newFileName)

# start workflow here
# accept input from std in identifying file name
####### commented for testing #######
#inputFileName = input()
inputFileName = 'steg.bmp'
outputFiles = []
bmpHeaderPos = []
bmpLength = []

with open(inputFileName, 'rb') as imgFile:
    print('\nsuccessfully opened file: ' + inputFileName + '\n')

    # create output folder with name '<inputFileName>_Output'
    directory = inputFileName[:len(inputFileName)-4] + '_Output' # truncate last 4 chars from inputFileName
    # print(directory)
    if not os.path.exists(directory):
        os.mkdir(directory)

    # repeat till end of file
    fileBytes = imgFile.read(1)
    filePos = 0
    # bmpHeader = []
    # bmpLength = []
    while len(fileBytes) > 0:
        # scan file for header data... bitmap header (BM / 0x42 0x4D), ignore empty blocks, else unknown
        # store header offset for file_name
        #print(chr(ord(fileBytes)))
        #input('Press enter\n') # wait for user input... debugging
        if chr(ord(fileBytes)) == 'B' :
            fileBytes = imgFile.read(1)
            if chr(ord(fileBytes)) == 'M' :
                foundHeaderPos = imgFile.tell() - 2
                # store header position
                bmpHeaderPos.append(foundHeaderPos)
                print('found Bitmap header at: ' + str(foundHeaderPos))
                # store length
                bmpLength.append(struct.unpack('i', imgFile.read(4))[0])

        if filePos % 10000 == 0:
            print(bmpHeaderPos)
            print(bmpLength)

        fileBytes = imgFile.read(1)
        filePos = imgFile.tell()

print(str(bmpHeaderPos) + '\n' + str(bmpLength))


# write files from found offsets and lengths
print('\ncarving bitmap files')
for i in range(len(bmpHeaderPos)):
    createBMP(inputFileName, bmpHeaderPos[i], abs(bmpLength[i]))

# get hashes of files
print('\nfinding checksums')
for file in outputFiles:
    hashMD5(file)
