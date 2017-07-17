# challenge 2
__author__ = 'Kyle Latino'
# Bitmap image tool will accept input path to .bmp and 
# generate a file with the height and width dimensions in pixels.
# 
# 
# height data found in byte23
# width data found in byte19


img = input('Enter path to image:' + '\n') # store path to *.bmp image as string

output = 'imageDataOutput.txt'
print('Image address: ' + img)

try:
	with open(image, 'rb') as img:
		height = img.seek(22)
		width = img.seek(18)
		
		with open(output, 'w+') as out:
			out.write('Image height: ' + height + '\n')
			out.write('Image width: ' + width + '\n')
			
		print('height: ' + height + '\nwidth: ' + width)
		
except :
	print('Unable to open image at location: ' + img)
	

