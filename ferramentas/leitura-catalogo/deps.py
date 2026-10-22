import os,re,collections,json
root='src'
files=[os.path.join(d,f) for d,_,fs in os.walk(root) for f in fs if f.endswith(('.ts','.tsx'))]
imp=re.compile(r'''(?:from|import)\s*\(?\s*['"](@/[^'"]+|\.{1,2}/[^'"]+)['"]''')
def resolve(base,spec):
    p=spec.replace('@/','src/',1) if spec.startswith('@/') else os.path.normpath(os.path.join(os.path.dirname(base),spec))
    for c in [p,p+'.ts',p+'.tsx',p+'/index.ts',p+'/index.tsx']:
        if os.path.isfile(c): return c
    return None
G={f:[x for x in (resolve(f,m) for m in imp.findall(open(f,errors='ignore').read())) if x] for f in files}
def zone(r):
    n=os.path.basename(r)
    if n.startswith('admin') : return 'admin'
    if n.startswith('portal'): return 'portal'
    if n.startswith('api') or r.startswith('src/routes/api'): return 'api'
    if n in('__root.tsx','README.md'): return 'root'
    return 'site'
routes=[f for f in files if f.startswith('src/routes/')]
use=collections.defaultdict(set)
for r in routes:
    z=zone(r); seen=set(); st=[r]
    while st:
        f=st.pop()
        if f in seen: continue
        seen.add(f); st+=G.get(f,[])
    for f in seen: use[f].add(z)
def grp(f):
    p=f.split('/')
    if p[1]=='modules': return 'modules/'+p[2]
    if p[1] in('routes',): return None
    return '/'.join(p[1:3]) if len(p)>3 else '/'.join(p[1:])
g=collections.defaultdict(set)
for f,zs in use.items():
    k=grp(f)
    if k: g[k]|=zs
for f in files:
    k=grp(f)
    if k and k not in g: g[k]=set()
out=collections.defaultdict(list)
for k,zs in sorted(g.items()):
    out[','.join(sorted(zs - {'root'})) or '(nenhuma rota)'].append(k)
for k,v in sorted(out.items()): print(k,'=>',', '.join(v)); print()
print(collections.Counter(zone(r) for r in routes))
