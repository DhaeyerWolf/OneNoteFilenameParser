#!/usr/bin/python
import re
import binascii
import sys 

if len(sys.argv) == 1:
    print("Please provide an argument")
    sys.exit()

# Open the file and read in the contents
with open(sys.argv[1], 'rb') as f:
	data = f.read()
# Find all occurrences of the block
start_indexes = [m.start() for m in re.finditer(b'\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00', data)]
# Loop over each occurrence and extract the block, then print it out in hex

i = 0
for start in start_indexes:
	end = data.find(b'\x00\x00\x00\x00\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00', start + 1)
	block = data[start:end]
	if len(block) > 1000 and len(block) < 5000 and not block.count(b'\x00') > 500:
		#print('- {}'.format(block.hex()))
		block = block.hex()
		#print(bytes.fromhex(block).decode('latin-1'))
		readable_chars = bytes([x for x in bytes.fromhex(block) if x in range(32, 127)]).decode('latin-1')
		print('string {}: {}'.format(i,readable_chars))
		i+=1