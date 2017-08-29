# challenge 2
# written in python 3
__author__ = 'Kyle Latino'
# Bitmap image tool will accept input path to .bmp and
# generate a file with the height and width dimensions in pixels.
#
# .bmp data locations, 2 bytes, little endian
# height data found in bytes 22&23
# width data found in bytes 18&19

import struct
import sys

if(sys.version_info[0] < 3):
	print('\n\nchallenge2.py will run under python 2.7 but the image address must be contained within quotes.\n Recommend running in python 3.\nUse command\'python3 challenge2.py\'\n\n')

image = input('Enter path to image:' + '\n') # store path to *.bmp image as string
#output = image[:len(image)-4] + '_Output.txt'
#print('Image address: ' + image)
print()

try:
	with open(image, 'rb') as img:
		img.seek(18) # location of width value in header
		width = struct.unpack('i', img.read(4))
		widthString = ('width: ' + str(width[0]))

		img.seek(22) # location of height value in header
		height = struct.unpack('i', img.read(4))
		heightString = ('height: ' + str(height[0]))


		#with open(output, 'w+') as out:
			#out.write(heightString + '\n')
			#out.write(widthString + '\n')

		print(heightString + '\n' + widthString + '\n')
except:
	print('Unable to open image at location: ' + img)
