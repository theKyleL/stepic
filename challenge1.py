# challenge 1
__author__ = 'Kyle Latino'
# Blum Blum Shub Pseudo Random Number Generator
# 
# Value = (Value^2) % M
# M = 0xE2089EA5
# 

import sys

value = 0x12345678 # initial value will be passed in from function signature
M = 0xE2089EA5 # modulous remains constant in this implementation

# determine the next value for the key stream
def nextValue():
	global M, value
	value = ((value ** 2) % M)

#return lowest byte of the value
def extractKey(): # remove (hexKey):
	global value
	return hex(value)[-2:]

# XOR char value with key
def xor(character, keyValue, isHex):
	if isHex:
		return int(int(('0x' + character[2:]), 16) ^ int(keyValue, 16))
	return int(ord(character)) ^ int(keyValue, 16)
			
# format value to match requirements
# e.g. Use '\x##' instead of '0x##' for input and output of hex values
def alterInputHex(inputHexValue):
	convertedHex = inputHexValue.replace('\\x', '0x')
	return convertedHex

def alterOutputHex(outputHexValue):
	return outputHexValue.replace('0x', '\\x')
	
def printOut(data):
	dat = ''.join(data)
	dat = alterOutputHex(dat)
	print(dat)
	
# fit this function signature!!		
def Crypt(unsignedChar, dataLength, initVal):
	global value
	print((unsignedChar))
	dat = [] # output data stored here
	inputChr = (unsignedChar) # 
	value = (initVal) # initialize value from input
	isHex = False
	
	# check for hex input
	if inputChr[:2] == r'\x': # compare the 'raw' value of the string, ignoring ‘escape’ characters
		isHex = True
		inputValue = alterInputHex(inputChr) # convert input hex value to python native format
		#process hex
		for i in range(dataLength):
			nextValue()
			dat.append(chr(xor(unsignedChar[(4*i):(4*i)+4], extractKey(), isHex)))
	
	else:
		# process chars
		for i in range(dataLength):
			nextValue()
			dat.append(str(hex(xor(unsignedChar[i], extractKey(), isHex))))
	
	printOut(dat)
	
	
if __name__ == '__main__':
	
	#print(nextValue(0x10000)) # verify proper implementation of func output. 0x10000 => 0x1DF7615B

	test1 = Crypt('apple', 5, 0x12345678)
	
	print() # separate tests for readability
	
	test2 = Crypt(r'\x4c\x88\x9e\xdf\xe8', 5, 0x12345678)	
	#
	# NOTE: the use of the 'r' preceeding the input string ensures that the value is passed in its raw format.
	#
	# Without the 'r' it would be necessary to pass an escaped version of the string containing the hex value. 
	# (e.g. '\\x4c\\x88\\x9e\\xdf\\xe8')
	#