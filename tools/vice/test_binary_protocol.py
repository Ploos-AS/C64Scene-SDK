#!/usr/bin/env python3
import struct
from binary_protocol import *

p=checkpoint_set(0x11223344,0x2345)
assert p[0]==0x02
assert p[1]==0x02
assert struct.unpack_from("<I",p,2)[0]==9
assert struct.unpack_from("<I",p,6)[0]==0x11223344
assert p[10]==0x12
body=p[11:]
assert struct.unpack_from("<H",body,0)[0]==0x2345
assert struct.unpack_from("<H",body,2)[0]==0x2345
assert body[4:]==bytes([1,1,4,0,0])

d=checkpoint_delete(7,0x12345678)
assert d[10]==0x13 and struct.unpack_from("<I",d,11)[0]==0x12345678
l=checkpoint_list(8)
assert l[10]==0x14 and len(l)==11
print("binary protocol packet tests: PASS")
