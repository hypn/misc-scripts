#!/usr/bin/python -u
import sys

# encode and decode functions from https://stackoverflow.com/a/61646764
BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encode_base62(num):
    s = ""
    while num>0:
      num,r = divmod(num,62)
      s = BASE62[r]+s
    return s

def decode_base62(num):
   x,s = 1,0
   for i in range(len(num)-1,-1,-1):
      s = int(BASE62.index(num[i])) *x + s
      x*=62
   return s

# sf15to18 function from https://github.com/mslabina/sf15to18/blob/master/sf15to18.py
def sf15to18 (id):
	if not id:
		raise ValueError('No id given.')
	if not isinstance(id, str):
		raise TypeError('The given id isn\'t a string')
	if len(id) == 18:
		return id
	if len(id) != 15:
		raise ValueError('The given id isn\'t 15 characters long.')

	# Generate three last digits of the id
	for i in range(0,3):
		f = 0

		# For every 5-digit block of the given id
		for j in range(0,5):
			# Assign the j-th chracter of the i-th 5-digit block to c
			c = id[i * 5 + j]

			# Check if c is an uppercase letter
			if c >= 'A' and c <= 'Z':
				# Set a 1 at the character's position in the reversed segment
				f += 1 << j

		# Add the calculated character for the current block to the id
		id += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ012345'[f]

	return id


# Hypn's code:
def generate_ids(salesforce_id, quantity):
	prefix = salesforce_id[0:10]
	num = decode_base62(salesforce_id[10:15])

	if quantity < 0:
		direction = -1
	else:
		direction = 1

	for i in range(quantity * direction):
		next_num = num + ((i + 1) * direction)
		print(sf15to18(prefix + encode_base62(next_num)))

if len(sys.argv) < 3:
	print("Usage:")
	print("  python3 -u " + sys.argv[0] + " {startingId} {amountToGenerateUpOrDown}")
	print("")
	print("Examples:")
	print("  python3 -u " + sys.argv[0] + " 006Do0000028TPmIAM -10")
	print("  python3 -u " + sys.argv[0] + " 006Do0000028TPmIAM 10")
	print("")

else:
	start_id = sys.argv[1]
	quantity = int(sys.argv[2])

	generate_ids(start_id, quantity)
