import sys,json,xml.etree.ElementTree as ET
raw=open(sys.argv[1],'rb').read().decode('utf-8','replace')
root=ET.fromstring(raw)
ids={}
def conv(e):
    if 'IDREF' in e.attrib: return ids.get(e.attrib['IDREF'])
    t=e.tag
    if t=='dict':
        ch=list(e); d={}
        for k,v in zip(ch[::2],ch[1::2]): d[k.text]=conv(v)
        r=d
    elif t=='array': r=[conv(c) for c in e]
    elif t=='integer': r=int(e.text,0) if e.text else 0
    elif t=='true': r=True
    elif t=='false': r=False
    elif t=='data': r='<data>'
    else: r=e.text or ''
    if 'ID' in e.attrib: ids[e.attrib['ID']]=r
    return r
d=conv(root[0])
out=[]
for k in d['_PrelinkInfoDictionary']:
    pers=k.get('IOKitPersonalities') or {}
    out.append({'id':k.get('CFBundleIdentifier'),'version':k.get('CFBundleVersion'),'name':k.get('CFBundleName'),
      'personalities':{n:{x:p.get(x) for x in ('IOClass','IOProviderClass','IONameMatch','IOPropertyMatch','IOUserClass','IOUserServerName','CFBundleIdentifier','compatible') if x in p} for n,p in pers.items()}})
json.dump(out,open(sys.argv[2],'w'),indent=1,default=str)
print(len(out), sum(len(o['personalities']) for o in out))
