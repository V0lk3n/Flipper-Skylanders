#!/usr/bin/env python3

## tnp3xxx.py - Compute a key A
##
## Written in 2016 and 2017 and 2018 by Vitorio Miliano
## Updated to Python 3 in 2022 by Adrian 'vifino' Pistol
##
## To the extent possible under law, the author has dedicated all
## copyright and related and neighboring rights to this software to
## the public domain worldwide.  This software is distributed without
## any warranty.
##
## You should have received a copy of the CC0 Public Domain
## Dedication along with this software.  If not, see
## <http://creativecommons.org/publicdomain/zero/1.0/>.

import re, struct, sys

uidre = re.compile('^[0-9a-f]{8}$', re.IGNORECASE)
magic_nums = [2, 3, 73, 1103, 2017, 560381651, 12868356821]

# Standard MSB CRC pseudocode e.g. https://en.wikipedia.org/w/index.php?title=Computation_of_cyclic_redundancy_checks&oldid=771577830#Bit_ordering_.28endianness.29
# CRC64 ECMA-182 e.g. http://stackoverflow.com/a/29241216
def pseudo_crc48(crc, data):
    POLY = 0x42f0e1eba9ea3693
    MSB = 0x800000000000
    TRIM = 0xffffffffffff
    for x in data:
        crc = crc ^ (x << 40)
        for k in range(0, 8):
            if crc & MSB:
                crc = (crc << 1) ^ POLY
            else:
                crc = crc << 1
            crc = crc & TRIM
    return crc

def calc_keya(uid, sector):
    if sector == 0:
        return format(magic_nums[2] * magic_nums[4] * magic_nums[5], '012x')

    if uidre.match(uid) is None:
        raise ValueError('invalid UID (four hex bytes)')

    if sector < 0 or sector > 15:
        raise ValueError('invalid sector (0-15)')

    PRE = magic_nums[0] * magic_nums[0] * magic_nums[1] * magic_nums[3] * magic_nums[6]
    ints = [b for b in bytes.fromhex(uid)] + [sector]

    key = pseudo_crc48(PRE, ints)

    return struct.pack('<Q', key).hex()[0:12]

if __name__ == '__main__':
    if len(sys.argv) > 1:
        keysa = []
        for sector in range(0, 16):
            keysa.append(calc_keya(sys.argv[1], sector).upper())
        if len(sys.argv) > 2 and sys.argv[2] == '-eml':
            print('0'*20+'\n'+('0'*32+'\n')*3).join(keysa).join([(sys.argv[1]+'0'*24+'\n')+(('0'*32+'\n')*2), '0'*20])
        else:
            print('\n'.join(keysa))
