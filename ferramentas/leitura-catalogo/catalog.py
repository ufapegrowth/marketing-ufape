import os
import json,re,datetime
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'build.py')).read().split('rows=[];skipped=[]')[0])
rows=json.load(open(SITE+'/rows.json'))
def dkey(x): return x.get('data_site') or x.get('data_planilha') or '9999'
def fmt(iso): return datetime.date.fromisoformat(iso).strftime('%d/%m/%Y') if iso else ''
def link(x): return f"[ficha]({x['ficha'].replace('contexto/','')})" if x.get('ficha') else ''
def nm(x): return cell(x.get('nome_final') or x.get('nome'))
L=[]
L.append("""# CATÁLOGO DE CURSOS DA UFAPE

Fonte única de dados de curso para toda a squad. Nenhum agente pode divulgar curso, preço, carga horária, data, modalidade ou certificação que não esteja aqui. Se um dado faltar ou estiver marcado para verificar, o agente escreve [CONFIRMAR NO CATÁLOGO] e não segue com a peça final.

- **Gerado em:** 22/10/2026, a partir da planilha "DATAS CURSOS E PÓS (por data de início)" e da leitura de todas as páginas de produto do site faculdade.ufape.com.br (161 páginas).
- **Responsável pela atualização:** [nome, área]
- **Detalhes de cada curso** (descrição, público, cronograma, coordenação, condições): pasta `contexto/cursos/`, uma ficha por produto, com o texto copiado da página oficial.
- **Problemas encontrados no cruzamento** planilha x site: `docs/auditoria-do-catalogo-2026-10-22.md`.

## Como usar

- **Status "aberto"**: pode ser divulgado com chamada para inscrição.
- **Status "aberto (contínuo)"**: curso online ou gravado, à venda o ano todo.
- **Status "verificar"**: a Ufape precisa confirmar antes de qualquer peça (turma já iniciada ainda à venda, data ausente ou divergente).
- **Status "sem venda (avise-me)"** ou **"encerrado"**: não divulgar com chamada de compra.
- **Preços** são os do site em 22/10/2026. Conferir a página oficial antes de publicar peça com preço.
- **Certificação de pós-graduação:** as páginas do site usam "CERTIFICADO PELO MEC". Até a regulação da Ufape aprovar o texto oficial, nenhuma peça deve usar essa frase. Texto aprovado: [PREENCHER COM A REGULAÇÃO].
- **Graduação:** ato de autorização ou reconhecimento de cada curso: [PREENCHER COM A REGULAÇÃO].

## Resumo

| Linha | Tipo | Produtos | Abertos | A verificar |
|---|---|---|---|---|""")
import collections
c=collections.defaultdict(lambda:[0,0,0])
for x in rows:
    k=(x['linha'],x['tipo']); c[k][0]+=1
    if x['status'].startswith('aberto'): c[k][1]+=1
    if x['status'].startswith('verificar'): c[k][2]+=1
for (l,t),v in sorted(c.items()): L.append(f"| {l} | {t} | {v[0]} | {v[1]} | {v[2]} |")
L.append("""
## 1. Graduação

| Curso | Local | Modalidade | Turno e duração | Carga horária | Investimento (site) | Ato regulatório | Ficha |
|---|---|---|---|---|---|---|---|
| Medicina Veterinária | São Paulo, SP | Presencial | Integral, 4 anos; Noturno, 5 anos | 4.195 h + 75 h de atividades complementares | Integral: de R$ 10.000,00 por R$ 5.000,00/mês (desconto de 50%). Noturno: de R$ 10.000,00 por R$ 4.000,00/mês (desconto de 60%). Regras no Edital de Descontos 2027 | [PREENCHER COM A REGULAÇÃO] | [ficha](cursos/graduacao/graduacao-em-medicina-veterinaria.md) |
| Pedagogia | Goiânia, GO | Presencial | Noturno, 4 anos | 3.440 h | De R$ 1.050,00 por R$ 525,00/mês (desconto de 50%). Regras no Edital de Desconto 2027.1 Goiânia | [PREENCHER COM A REGULAÇÃO] | [ficha](cursos/graduacao/graduacao-em-pedagogia.md) |

Editais publicados no site: Vestibular 2027 (https://faculdade.ufape.com.br/uploads/arquivo/edital-vestibular-2027.pdf), Descontos 2027 (https://faculdade.ufape.com.br/uploads/arquivo/edital-descontos-2027.pdf), Processo Seletivo 2027.1 Goiânia (https://faculdade.ufape.com.br/uploads/arquivo/edital-processo-seletivo-2027-1-goiania.pdf), Desconto de Mensalidade 2027.1 Goiânia (https://faculdade.ufape.com.br/uploads/arquivo/edital-de-desconto-mensalidade-2027-1-goiania.pdf).
""")
def table(title,items,cols):
    L.append(f"## {title}\n")
    hdr={'cod':'Código','curso':'Curso','local':'Local','mod':'Modalidade','ini':'Início','turma':'Turma','ch':'CH','preco':'Preço e condições (site)','status':'Status','ficha':'Ficha','fonte':'Fonte'}
    L.append('| '+' | '.join(hdr[c] for c in cols)+' |'); L.append('|'+'---|'*len(cols))
    for x in sorted(items,key=lambda x:(dkey(x),nm(x))):
        v={'cod':pid(x.get('url')),'curso':nm(x),'local':cell(x.get('localidade_site') or x.get('local') or ''),'mod':cell(x.get('modalidade') or '').capitalize(),
           'ini':fmt(x.get('data_site') or x.get('data_planilha')) or cell(x.get('inicio_site') or x.get('inicio') or ''),'turma':cell(x.get('turma_site') or x.get('turma') or ''),
           'ch':(x.get('carga_horaria')+' h') if x.get('carga_horaria') else '','preco':cell(preco(x)) if x.get('url') else '','status':x['status'],'ficha':link(x),
           'fonte':('só no site' if x['aba']=='site' else ('planilha e site' if x.get('url') else 'só na planilha'))}
        L.append('| '+' | '.join(v[c] for c in cols)+' |')
    L.append('')
pos=[x for x in rows if x['linha']=='pos' and x['tipo']=='pós-graduação']
table('2. Pós-graduação (turmas)',pos,['cod','curso','local','mod','ini','turma','ch','preco','status','fonte','ficha'])
table('3. Provas de bolsa (pós-graduação)',[x for x in rows if x['tipo']=='prova de bolsa'],['cod','curso','local','ini','status','ficha'])
for t,title in [('curso presencial','4. Cursos livres presenciais'),('curso online','5. Cursos livres online e gravados'),('curso em espanhol','6. Cursos em espanhol'),('grupo de estudos','7. Grupos de estudos'),('aprimoramento (Ufape Clínica)','8. Aprimoramento (Ufape Clínica)')]:
    table(title,[x for x in rows if x['tipo']==t],['cod','curso','local','mod','ini','ch','preco','status','fonte','ficha'])
table('9. Simpósios e congressos',[x for x in rows if x['tipo']=='simpósio ou congresso'],['cod','curso','local','ini','preco','status','fonte','ficha'])
out='\n'.join(L).replace('\u2013','-').replace('\u2014','-')
open(REPO+'/contexto/catalogo-de-cursos.md','w').write(out)
print(len(out.splitlines()))
