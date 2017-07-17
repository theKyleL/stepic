# challenge 1
__author__ = 'Kyle Latino'
# Blum Blum Shub Pseudo Random Number Generator
# 
# Value = (Value^2) % M
# M = 0xE2089EA5
# 

import sys

value = 0x12345678 # initial value
M = 0xE2089EA5 #modulous

# determine the next value for the key stream
def nextValue():
	global M, value
	value = ((value ** 2) % M)
	#return value

#return lowest byte of the value
def extractKey(): # remove (hexKey):
	global value
	#	return(hex(int(hexKey, 16) & 0xff))
	# return hexKey[7:]
	return hex(value)[-2:]

# XOR char value with key
def xor(character, keyValue, isHex):
	#print('xor: ', character, keyValue)
	if isHex:
		return int(int(character, 16) ^ int(keyValue, 16))
	return int(ord(character)) ^ int(keyValue, 16)
			
# format value to match requirements
# e.g. Use '\x##' instead of '0x##'
def printOut(data):
	dat = data
	for i in range()
	print('Output: ' + ''.join(data))
	
# fit this function signature!!		
def Crypt(unsignedChar, dataLength, initVal):
	global value
	dat = [] # output data stored here
	value = (initVal) #initialize value for input
	isHex = False
	
	# check for hex input
	printOut('input: ' + unsignedChar)
	if unsignedChar[:2] == '0x':
		isHex = True
		#print('input was in hex, converting to ascii')
		
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
	
	print()
	
	test2 = Crypt('0x4c0x880x9e0xdf0xe8', 5, 0x12345678)
	