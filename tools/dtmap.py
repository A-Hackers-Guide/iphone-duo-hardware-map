import json,sys
dt=json.load(open(sys.argv[1]))['device-tree']; kx=json.load(open(sys.argv[2]))
nodes=[]
def walk(props,path,parent):
    p={k:v for k,v in props.items() if k!='children'}
    comp=p.get('compatible'); comp=comp if isinstance(comp,list) else ([comp] if comp else [])
    nodes.append({'path':path,'parent':parent,'name':path.split('/')[-1],'compatible':comp,'device_type':p.get('device_type'),
      'reg':p.get('reg'),'interrupts':p.get('interrupts'),'interrupt-parent':p.get('interrupt-parent'),
      'props':p})
    for c in props.get('children',[]) or []:
        for n,v in c.items(): walk(v,path+'/'+n,path)
walk(dt,'device-tree',None)
# matching
match={}
for k in kx:
    for pn,pp in k['personalities'].items():
        nm=pp.get('IONameMatch')
        if nm is None: continue
        for s in (nm if isinstance(nm,list) else [nm]):
            match.setdefault(s,[]).append({'kext':k['id'],'class':pp.get('IOClass'),'provider':pp.get('IOProviderClass')})
for n in nodes:
    m=[]
    for s in n['compatible']+[n['name']]:
        m+= [dict(x,matched_on=s) for x in match.get(s,[])]
    n['drivers']=m
json.dump(nodes,open(sys.argv[3],'w'),indent=1,default=str)
print(len(nodes),'nodes', sum(1 for n in nodes if n['drivers']),'with drivers', sum(1 for n in nodes if n['compatible'] and not n['drivers']),'compatible-but-unmatched')
