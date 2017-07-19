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
    f1 = hashlib.md5()
    fileBytes = fileDat.read(4096)
    while len(fileBytes) > 0:
        f1.update(fileBytes)
        fileBytes = fileDat.read(4096)
    print(f1.hexdigest())

# start workflow here
# accept input from std in identifying file name
####### commented for testing #######
#inputFileName = input()
inputFileName = 'steg.bmp'

with open(inputFileName, 'rb') as imgFile:
    print('\nsuccessfully opened file: ' + inputFileName + '\n')

    # create output folder with name '<inputFileName>_Output'
    directory = inputFileName[:len(inputFileName)-4] + '_Output' # truncate last 4 chars from inputFileName
    # print(directory)
    if not os.path.exists(directory):
        os.mkdir(directory)

    # repeat till end of file
    fileBytes = imgFile.read(2)
    filePos = 0
    bmpHeader = []
    bmpLength = []
    while fileBytes > 0:
        # scan file for header data... bitmap header (BM / 0x42 0x4D), ignore empty blocks, else unknown
        # store header offset for file_name


        # store length


    # write files from found offsets and lengths


    # get hashes of files
    hashMD5(imgFile)
