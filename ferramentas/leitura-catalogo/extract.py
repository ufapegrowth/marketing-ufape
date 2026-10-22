import csv,re,html,json,sys,hashlib
rows=list(csv.DictReader(open('planilha.tsv'),delimiter='\t'))
def text(s):
    s=re.sub(r'<script.*?</script>|<style.*?</style>|<!--.*?-->','',s,flags=re.S)
    t=html.unescape(re.sub(r'<[^>]+>','\n',s)); t=re.sub(r'[ \t\xa0]+',' ',t)
    return '\n'.join(l.strip() for l in t.split('\n') if l.strip())
def after(t,label,n=1):
    m=re.search(r'^'+label+r'\s*$\n((?:.*\n){%d})'%n,t,re.M|re.I)
    return ' '.join(m.group(1).split('\n')).strip() if m else ''
out=[]
for r in rows:
    d=dict(r)
    if r['url']:
        s=open('html/'+hashlib.md5(r['url'].encode()).hexdigest()+'.html',errors='ignore').read()
        t=text(s)
        i=t.find('\nHome\n'); body=t[i+6:] if i>0 else t
        mt=re.search(r'<title>(.*?)</title>',s,re.S); d['titulo_site']=re.sub(r'\s+',' ',html.unescape(mt.group(1))).strip() if mt else (body.split('\n')[0] if body else '')
        d['parcelado']=(re.search(r'^\d+x de R\$ ?[\d\.,]+.*$',body,re.M) or [''])[0]
        d['total']=(re.search(r'^R\$ ?[\d\.,]+ .*(?:cart|bolet|vista).*$',body,re.M) or [''])[0]
        m=re.search(r'^Matr[ií]cula\s*\n(R\$ ?[\d\.,]+)',body,re.M); d['matricula']=m.group(1) if m else ''
        m=re.search(r'^Valor\s*\n(R\$ ?[\d\.,]+)\s*\n(.*)$',body,re.M); d['valor_curso_livre']=(m.group(1)+' '+m.group(2)) if m else ''
        m=re.search(r'^PROMO[ÇC][ÃA]O\s*\n((?:.*\n){1,4})',body,re.M); d['promocao']=' '.join(m.group(1).split('\n')).strip() if m else ''
        d['inicio_site']=after(body,'IN[ÍI]CIO')
        d['carga_horaria']=(re.search(r'(\d[\d\.]*) ?horas',body,re.I) or ['',''])[1] if re.search(r'(\d[\d\.]*) ?horas',body,re.I) else ''
        m=re.search(r'(\d+) ?m[óo]dulos',body,re.I); d['modulos']=m.group(1) if m else ''
        d['modalidade']=after(body,'MODALIDADE')
        d['turma_site']=after(body,'Turma')
        d['localidade_site']=after(body,'Localidade')
        d['publico']=after(body,'P[ÚU]BLICO[- ]ALVO')
        d['vagas']=after(body,'VAGAS')
        d['endereco']=after(body,'LOCAL')
        d['certificado']=' | '.join(sorted(set(re.findall(r'^.*CERTIFICAD.*$',body,re.M|re.I))))[:200]
        d['coordenadores']=', '.join(dict.fromkeys(html.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in re.findall(r'products/coordenador/\d+"[^>]*>(.*?)</a>',s,re.S)))
        d['n_professores']=len(set(re.findall(r'products/professor/(\d+)',s)))
        paras=[l for l in body.split('\n') if len(l)>180 and 'Ufape Intercursos' not in l and 'passagens' not in l]
        d['descricao']=paras[0] if paras else ''
        d['esgotado']='sim' if re.search(r'esgotad|indispon[ií]vel|encerrad',body,re.I) else ''
        d['status_venda']='link indisponivel' if 'não está mais disponível' in body else ('avise-me (sem venda)' if 'Avise-me' in body else ('a venda' if 'COMPRAR' in body or 'INSCREVA' in body.upper() else 'indefinido'))
        d['tem_bolsa']='sim' if 'PROVA DE BOLSA' in body.upper() else ''
        open('html/'+hashlib.md5(r['url'].encode()).hexdigest()+'.txt','w').write(body)
    out.append(d)
json.dump(out,open('cursos.json','w'),ensure_ascii=False,indent=1)
