#hex: 0xFFとkeyのxor
hex = 'a387c69da3879dcaa3879dcaa387c79da3879eced5d2a3879b9ea3879b9ca387'
key = ''
for i in bytes.fromhex(hex):
	key += "{:02x}".format(i ^ 0xFF)
print("key: ", key)

encrypted = '0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d'
xor = lambda p, k: p ^ k

import string
ans = ''
for enc_byte, key_byte in zip(bytes.fromhex(encrypted), bytes.fromhex(key)):
	for i in range(0, 255):
		if xor(i, key_byte) == enc_byte:
			ans += chr(i)
print("ans: ", ans)