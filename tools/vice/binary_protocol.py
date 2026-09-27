#!/usr/bin/env python3
"""Small VICE binary-monitor protocol core for C64Scene.

Protocol integers are little-endian. This module deliberately contains no
socket/process policy so packet encoding can be unit-tested independently.
"""
import struct

STX=0x02
API_VERSION=0x02
CMD_CHECKPOINT_SET=0x12
CMD_CHECKPOINT_DELETE=0x13
CMD_CHECKPOINT_LIST=0x14

def request(command, request_id, body=b""):
    # STX, API version, body length, request id, command
    return struct.pack("<BBIIB",STX,API_VERSION,len(body),request_id,command)+body

def checkpoint_set(request_id,start,end=None,stop=True,enabled=True,
                   operation=0x04,temporary=False,memspace=0x00):
    if end is None: end=start
    body=struct.pack("<HHBBBBB",start,end,int(stop),int(enabled),
                     operation,int(temporary),memspace)
    return request(CMD_CHECKPOINT_SET,request_id,body)

def checkpoint_delete(request_id,number):
    return request(CMD_CHECKPOINT_DELETE,request_id,struct.pack("<I",number))

def checkpoint_list(request_id):
    return request(CMD_CHECKPOINT_LIST,request_id)
