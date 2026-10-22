import json,re,hashlib,os,datetime,collections
SITE=os.environ.get('DADOS_DIR','dados')
REPO=os.environ.get('REPO_DIR','../..')
HOJE=datetime.date(2026,10,22)
d=json.load(open(SITE+'/cursos.json'))
def clean(s): return re.sub(r'\s+',' ',(s or '').replace('–','-').replace('—','-')).strip()
def cell(s): return clean(s).replace('|','/')
def pid(u): m=re.search(r'/produto/(\d+)',u or ''); return m.group(1) if m else ''
def slug(s): 
    import unicodedata
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')[:70]
def classify(x):
    t=(x.get('titulo_site') or x.get('nome') or '').lower(); u=x.get('url') or ''
    a=x['aba']
    if a=='grad': return 'graduacao','graduação'
    if a=='bolsa': return 'pos','prova de bolsa'
    if a=='pos': return 'pos','pós-graduação'
    if a=='simposio': return 'livres','simpósio ou congresso'
    if 'teste' in t: return None,None
    if 'simp' in t or 'congresso' in t: return 'livres','simpósio ou congresso'
    if a=='site' and ('pós-gradua' in t or 'pós gradua' in t or 'pos-graduacao' in u): return 'pos','pós-graduação'
    if 'grupo de estudo' in t: return 'livres','grupo de estudos'
    if pid(u) in ('639','640','641'): return 'livres','aprimoramento (Ufape Clínica)'
    if 'simp' in t or 'congresso' in t: return 'livres','simpósio ou congresso'
    mod=(x.get('modalidade') or '').lower()
    if 'espa' in t or 'lima' in t or ' y ' in t: tipo='curso em espanhol'
    elif 'online' in mod.replace('-','').replace(' ','') or 'grava' in mod: tipo='curso online'
    else: tipo='curso presencial'
    return 'livres',tipo
def status(x):
    sv=x.get('status_venda','')
    if not x.get('url'): return 'sem página'
    if sv=='link indisponivel': return 'encerrado (link fora do ar)'
    if sv.startswith('avise'): return 'sem venda (avise-me)'
    ref=x.get('data_site') or x.get('data_planilha')
    mod=(x.get('modalidade') or '').lower()
    if x['aba']=='grad': return 'aberto (vestibular 2027)'
    if ref:
        dt=datetime.date.fromisoformat(ref)
        if dt>=HOJE: return 'aberto'
        if 'grava' in mod or ('online' in mod.replace('-','') and x['aba']=='site'): return 'aberto (contínuo)'
        return 'verificar (turma já iniciada e com venda)'
    if 'online' in mod.replace('-','').replace(' ','') or 'grava' in mod: return 'aberto (contínuo)'
    return 'verificar (sem data no site)'
def preco(x):
    p=[]
    if x.get('parcelado'): p.append(x['parcelado'])
    if x.get('total'): p.append(x['total'])
    if x.get('matricula'): p.append('matrícula '+x['matricula'])
    if x.get('valor_curso_livre'): p.append(x['valor_curso_livre'])
    if x.get('promocao'): p.append('PROMOÇÃO: '+x['promocao'][:120])
    return '; '.join(p) or '[CONFIRMAR NO SITE]'
def mainbody(x):
    fn=SITE+'/html/'+hashlib.md5(x['url'].encode()).hexdigest()+'.txt'
    t=open(fn).read()
    if x['aba']=='grad':
        i=t.find('Perfil do egresso'); t=t[i:] if i>=0 else t
    for end in ['FACULDADE UFAPE\nAv 9','PATROCINADORES E PARCEIROS\n','Documentos para matrícula']:
        j=t.find(end)
        if j>0: t=t[:j]; break
    lines=[clean(l) for l in t.split('\n')]
    out=[];prev=None
    for l in lines:
        if l and l!=prev: out.append(l)
        prev=l
    return '\n'.join(out)
rows=[];skipped=[]
for x in d:
    linha,tipo=classify(x)
    if linha is None or (x['aba']=='simposio' and 'Coagula' in x['nome']): skipped.append(x); continue
    x['linha']=linha;x['tipo']=tipo;x['status']=status(x)
    rows.append(x)
# fichas
fichas=0
for x in rows:
    if not x.get('url'): continue
    nome=clean(x.get('titulo_site') or x['nome'])
    if x['aba']=='grad': nome=clean(x['nome'])
    x['nome_final']=nome
    path=f"contexto/cursos/{x['linha']}/{(pid(x['url'])+'-') if pid(x['url']) else ''}{slug(nome)}.md"
    x['ficha']=path
    os.makedirs(os.path.dirname(REPO+'/'+path),exist_ok=True)
    meta=[('Linha',x['linha']),('Tipo',x['tipo']),('Status em 22/10/2026',x['status']),('Página oficial',x['url']),
          ('Início no site',x.get('inicio_site')),('Início na planilha',x.get('inicio')),('Turma',x.get('turma_site') or x.get('turma')),
          ('Localidade',x.get('localidade_site') or x.get('local')),('Modalidade',x.get('modalidade')),('Carga horária',(x.get('carga_horaria')+' h') if x.get('carga_horaria') else ''),
          ('Módulos',x.get('modulos')),('Preço e condições',preco(x) if x['aba']!='grad' else ''),('Público-alvo',x.get('publico')),('Vagas',x.get('vagas')),
          ('Endereço',x.get('endereco')),('Coordenação',x.get('coordenadores')),('Professores listados',str(x.get('n_professores') or '')),
          ('Certificado (texto do site)',x.get('certificado')),('Alertas',('; '.join(x['flags'])) if x.get('flags') else 'nenhum')]
    body=mainbody(x)
    txt=f"# {nome}\n\nFicha gerada automaticamente a partir da página oficial e da planilha \"DATAS CURSOS E PÓS\" em 22/10/2026. Dados de curso para peças continuam valendo só depois de conferidos em contexto/catalogo-de-cursos.md. Itens em Alertas precisam de confirmação da Ufape.\n\n## Dados principais\n\n"
    txt+='\n'.join(f"- **{k}:** {clean(v)}" for k,v in meta if clean(v))+"\n\n## Texto da página (copiado do site)\n\n"+body+"\n"
    txt=txt.replace('–','-').replace('—','-')
    open(REPO+'/'+path,'w').write(txt); fichas+=1
json.dump(rows,open(SITE+'/rows.json','w'),ensure_ascii=False,indent=1)
json.dump(skipped,open(SITE+'/skipped.json','w'),ensure_ascii=False,indent=1)
print('fichas',fichas,'linhas',collections.Counter((r['linha'],r['tipo']) for r in rows))
print(collections.Counter(r['status'] for r in rows))
