"""Dump every kext's full Info.plist (personalities, libraries, all keys) from prelink XML.

usage: prelink_full.py prelink.xml out.json
"""
import json
import sys
import xml.etree.ElementTree as ET

root = ET.fromstring(open(sys.argv[1], 'rb').read().decode('utf-8', 'replace'))
ids = {}


def conv(e):
    if 'IDREF' in e.attrib:
        return ids.get(e.attrib['IDREF'])
    t = e.tag
    if t == 'dict':
        ch = list(e)
        r = {k.text: conv(v) for k, v in zip(ch[::2], ch[1::2])}
    elif t == 'array':
        r = [conv(c) for c in e]
    elif t == 'integer':
        r = int(e.text, 0) if e.text else 0
    elif t in ('true', 'false'):
        r = t == 'true'
    elif t == 'data':
        r = '<data %d chars>' % len(e.text or '')
    else:
        r = e.text or ''
    if 'ID' in e.attrib:
        ids[e.attrib['ID']] = r
    return r


d = conv(root[0])
json.dump(d['_PrelinkInfoDictionary'], open(sys.argv[2], 'w'), indent=1, default=str)
print(len(d['_PrelinkInfoDictionary']))
