#!/usr/bin/env python2

import sys
import struct
import base64
import datetime

MAGIC = 0x8BADF00D
VERSION = 1
SECTION_ASCII = hex(0x1)
SECTION_UTF8 = hex(0x2)
SECTION_WORDS = hex(0x3)
SECTION_DWORDS = hex(0x4)
SECTION_DOUBLES = hex(0x5)
SECTION_COORD = hex(0x6)
SECTION_REFERENCE = hex(0x7)
SECTION_PNG = hex(0x8)
SECTION_GIF87 = hex(0x9)
SECTION_GIF89 = hex(0xA)

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# Some constants. You shouldn't need to change these.


if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])
timestamp = datetime.datetime.utcfromtimestamp(int(struct.unpack("<L", data[8:12])[0])).isoformat()
author = ''.join(struct.unpack("<8s", data[12:20]))
section_count = int(struct.unpack("<L", data[20:24])[0])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

print("TIMESTAMP: %s" % timestamp)
print("AUTHOR: %s" % author)
print("SECTION COUNT: %d" % section_count)


print("-------- BODY --------")

offset = 24
for section in range(1,section_count+1):
    stype = hex(struct.unpack("<L", data[offset : offset+4])[0])
    slen = int(struct.unpack("<L", data[offset+4 : offset+8])[0])
    offset += 8

    print("SECTION: " + str(section))
    print("TYPE: " + stype)
    print("LENGTH: " + str(slen))

    if stype == SECTION_ASCII:
        tmp = "<" + str(slen)+ "s"
        value = struct.unpack(tmp, data[offset:offset+slen])[0]
        print("VALUE: " + value)

    elif stype == SECTION_UTF8:
        tmp = "<" + str(slen)+ "s"
        value = struct.unpack(tmp, data[offset:offset+slen]).decode('utf-8')[0]
        print("VALUE: " + value)

    elif stype == SECTION_WORDS:
        words = slen / 4
        value = struct.unpack(("<%s" % 'L'*words), data[offset:offset+slen])[0]
        print("VALUE: %s" % value)

    elif stype == SECTION_DWORDS:
        dwords = slen / 8
        value = struct.unpack(("<%s" % 'Q'*dwords), data[offset:offset+slen])[0]
        print("VALUE: %s" % value)

    elif stype == SECTION_DOUBLES:
        doubles = slen / 8
        value = struct.unpack(("<%s" % 'd'*doubles), data[offset:offset+slen])[0]
        print("VALUE: %s" % value)

    elif stype == SECTION_COORD:
        value = struct.unpack("<dd", data[offset:offset+slen]),
        print("COORDINATES: %s" % value)


    elif stype == SECTION_PNG:
        signature = [137, 80, 78, 71, 13, 10, 26, 10]
        value = struct.unpack('<' + ("%s" % 'B'*slen), data[offset:offset+slen])
        myImage = open("myImage.png", "wb")
        myImage.write(bytearray(signature + list(value)))
    

    

    print(70*"-")
    offset += slen