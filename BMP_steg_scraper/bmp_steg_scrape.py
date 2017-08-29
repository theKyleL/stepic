# challenge3
__author__ = 'Kyle Latino'
#
#
# Referenced for creating directories: https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist
#

# imports
import struct
import hashlib
import os

# functions
# get md5 hash of file
def hashMD5(fileDat):
    with open(fileDat, 'rb') as hashFile:
        f1 = hashlib.md5()
        fileBytes = hashFile.read(4096)
        while len(fileBytes) > 0:
            f1.update(fileBytes)
            fileBytes = hashFile.read(4096)
        return (f1.hexdigest())

# create new file from offset and length
def createFile(originFile, offset, length, extension):
    with open(originFile, 'rb') as origin:
        newFileName = directory + os.path.sep + str(offset) + extension
        with open(newFileName, 'wb+') as newImage:
            origin.seek(offset)
            newImage.write(origin.read(length))
        outputFiles.append(os.path.curdir + os.path.sep + newFileName)

# check if currently looking at data from already carved images
def inAlreadyCarvedImg(currentPosition):
    for i in range(bmpCount):
        if currentPosition >= bmpHeaderPos[i] and currentPosition <= bmpHeaderPos[i] + bmpLength[i]:
            lastFileIncurred = i
            return True
    return False

# return the beginning of the next open range
def nextOpenSpace():
    # print('moving to open space')
    return (bmpHeaderPos[lastFileIncurred] + bmpLength[lastFileIncurred])


# start workflow here
# accept input from std in identifying file name
inputFileName = input('Enter file name:\n>')
# inputFileName = 'steg.bmp'
outputFiles = []
bmpHeaderPos = []
bmpLength = []
bmpCount= 0
lastFileIncurred = 0
unknownFilePos = []
unknownFileLength = []

with open(inputFileName, 'rb') as imgFile:
    global directory
    print('\nsuccessfully opened file: ' + inputFileName + '\n')
    # create output folder with name '<inputFileName>_Output'
    directory = inputFileName[:len(inputFileName)-4] + '_Output' # truncate last 4 chars from inputFileName
    # print(directory)
    if not os.path.exists(directory):
        os.mkdir(directory)

    # repeat till end of file
    fileBytes = imgFile.read(1)

    while len(fileBytes) > 0:
        # scan file for header data... bitmap header (BM / 0x42 0x4D), ignore empty blocks, else unknown
        # store header offset for file_name
        if chr(ord(fileBytes)) == 'B' :
            fileBytes = imgFile.read(1)
            if chr(ord(fileBytes)) == 'M' :
                foundHeaderPos = imgFile.tell() - 2
                bmpCount += 1
                # store header position
                bmpHeaderPos.append(foundHeaderPos)
                print('found Bitmap header at: ' + str(foundHeaderPos))
                # store length
                bmpLength.append(struct.unpack('i', imgFile.read(4))[0])

        fileBytes = imgFile.read(1)

    # carving complete for .bmp
    # check non-bmp space for data
    imgFile.seek(0)
    fileBytes = imgFile.read(2)
    #filePos = 1
    while len(fileBytes) > 0:
        if inAlreadyCarvedImg(imgFile.tell()):
            imgFile.seek(nextOpenSpace())
        # look for non-bmp data
        fileBytes = imgFile.read(2)
        if fileBytes != 0x00:
            print('found unknown data at: ' + str(imgFile.tell() - 2))
            # save location of unknown data
            unknownFilePos.append(imgFile.tell() - 2)
            while len(fileBytes) > 0:
                # read until null data found
                fileBytes = imgFile.read(2)
            unknownFileLength.append((imgFile.tell()-2) - unknownFilePos[len(unknownFilePos)-1])


if __name__ == __main__:

  print('\nBitmap offsets: ' + str(bmpHeaderPos) + '\n' + 'Lengths: ' + str(bmpLength) )

  print('\nUnknown file offsets: ' + str(unknownFilePos) + '\n' + 'Lengths: ' +  str(unknownFileLength) + '\n')


  # write files from found offsets and lengths
  print('carving bitmap files\n')
  for i in range(len(bmpHeaderPos)):
    createFile(inputFileName, bmpHeaderPos[i], abs(bmpLength[i]), '.bmp')

  print('carving unknown data\n')
  for i in range(len(unknownFilePos)):
    createFile(inputFileName, unknownFilePos[i], unknownFileLength[i], '.unknown')

  # get hashes of files
  print('finding checksums\n')
  for file in outputFiles:
    print(file + ': ' + hashMD5(file))
  print()
