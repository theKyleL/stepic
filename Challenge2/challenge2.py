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

if(sys.version_info[0] < 3):
	print('\n\nchallenge1.py will run under python 2.7 but the image address must be contained within quotes.\n Recommend running in python 3.\nUse command\'python3 challenge2.py\'\n\n')

image = input('Enter path to image:' + '\n') # store path to *.bmp image as string
output = 'imageDataOutput.txt'
print('Image address: ' + image)

try:
	with open(image, 'rb') as img:
		img.seek(18)
		width = struct.unpack('i', img.read(4))
		widthString = ('width: ' + str(width[0]))

		img.seek(22)
		height = struct.unpack('i', img.read(4))
		heightString = ('height: ' + str(height[0]))


		with open(output, 'w+') as out:
			out.write(heightString + '\n')
			out.write(widthString + '\n')

			print(heightString + '\n' + widthString)
except:
	print('Unable to open image at location: ' + img)
