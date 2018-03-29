import os
import struct
from ctypes import *
# host to listen on
host = "0.0.0.0"

# our IP header
class IP(Structure):
    _fields_ = [
        ("ihl",     c_ubyte,  4),
        ("version", c_ubyte,  4),
        ("tos",     c_ubyte),
        ("len",     c_ushort),
        ("id",      c_ushort),
        ("offset",  c_ushort),
        ("ttl",     c_ubyte),
        ("protocol_num",    c_byte),
        ("sum",     c_ushort),
        ("src",     c_ulong),
        ("dst",     c_ulong)
    ]
