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

def xor(character, keyValue):
	return int(ord(character)) ^ int(keyValue, 16)
			
# fit this function signature!!		
def Crypt(unsignedChar, dataLength, initVal):
	global value
	dat = [] # output data stored here
	value = (initVal) #initialize value for input
	
	for i in range(dataLength):
		nextValue()
		#formatting magic here
		dat.append('\\' + str(hex(xor(unsignedChar[i], extractKey())))[1:]) 
	
	return ''.join(dat)
	
	
	
if __name__ == '__main__':
	
	#print(nextValue(0x10000)) # verify proper implementation of func output. 0x10000 => 0x1DF7615B

	test1 = Crypt('apple', 5, 0x12345678)
	print(test1)
	
	
	test2 = Crypt('\x4c\x88\x9e\xdf\xe8', 5, 0x12345678)
	print(test2)