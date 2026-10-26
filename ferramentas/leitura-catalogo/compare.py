import json,re,datetime,os
M={'jan':1,'fev':2,'mar':3,'abr':4,'mai':5,'may':5,'jun':6,'jul':7,'ago':8,'set':9,'out':10,'nov':11,'dez':12}
def pdate(s,default_year=None):
    s=(s or '').lower()
    m=re.search(r'(\d{1,2})\.(\d{1,2})\.(\d{4})',s)
    if m: return datetime.date(int(m[3]),int(m[2]),int(m[1]))
    m=re.search(r'(\d{1,2})(?:\s*(?:e|,)\s*\d{1,2})*(?:\s*e\s*\d{1,2})?\s*(?:de\s+)?([a-zç]{3})[a-zç]*\s*(?:del|de)?\s*(\d{4})?',s)
    if m and m[2][:3] in M:
        y=int(m[3]) if m[3] else default_year
        if y: return datetime.date(y,M[m[2][:3]],int(m[1]))
    m=re.search(r'([a-zç]{3})[a-zç]*\s*(?:del|de)?\s*(\d{4})',s)
    if m and m[1][:3] in M: return datetime.date(int(m[2]),M[m[1][:3]],1)
    return None
d=json.load(open('cursos.json'))
hoje=datetime.date.fromisoformat(os.environ.get('DATA_LEITURA','2026-10-22'))
for x in d:
    ds=pdate(x.get('inicio'),2026); dw=pdate(x.get('inicio_site'),ds.year if ds else None)
    x['data_planilha']=ds.isoformat() if ds else ''
    x['data_site']=dw.isoformat() if dw else ''
    flags=[]
    if x['url'] and x['aba']!='grad':
        if ds and dw and ds!=dw: flags.append(f"data diverge: planilha {ds:%d/%m/%Y}, site {dw:%d/%m/%Y}")
        if x['aba'] in('pos','livres') and not x.get('inicio_site') and x.get('status_venda')=='a venda': flags.append('site sem data de início')
        if 'XX' in (x.get('inicio_site') or ''): flags.append('site com data em branco (XX)')
        ref=ds or dw  # datas: a planilha é a fonte da verdade
        if ref and ref<hoje and x.get('status_venda')=='a venda' and 'grava' not in (x.get('modalidade') or '').lower(): flags.append(f'turma já começou ({ref:%d/%m/%Y}) e segue à venda')
        if x.get('status_venda')!='a venda': flags.append('página: '+x.get('status_venda',''))
        if x['aba']=='pos' and x.get('turma') and x.get('turma_site') and x['turma'].strip().upper()!=x['turma_site'].strip().upper(): flags.append(f"turma diverge: planilha {x['turma']}, site {x['turma_site']}")
        if 'certificado pelo mec' in (x.get('certificado') or '').lower(): flags.append('usa "CERTIFICADO PELO MEC"')
    x['flags']=flags
json.dump(d,open('cursos.json','w'),ensure_ascii=False,indent=1)
for x in d:
    if x['flags'] and x['aba']!='site': print(x['aba'],'|',(x['nome'] or x['titulo_site'])[:60],'|','; '.join(x['flags']))
print('---- site extras com problema')
for x in d:
    if x['aba']=='site' and [f for f in x['flags'] if 'MEC' not in f]: print((x['titulo_site'])[:60],'|','; '.join(x['flags']))
