"""Plano de marketing Ufape para a diretoria: uma página em linguagem simples.

Rodar da raiz do repositório, depois do mapa (ferramentas/mapa-mental) e do painel (ferramentas/entregaveis):
    python3 -I ferramentas/plano/plano.py
Lê saidas/09-analytics-e-insights/relatorios-geral-2026-10-27-diretoria.json (texto do relatorios),
os cursos de ferramentas/mapa-mental/saida/mapa-dados.json e as peças de ferramentas/entregaveis/dados/,
e grava ferramentas/plano/saida/plano-artifact.html e saidas/02-estrategia-e-posicionamento/plano-diretoria-2026-10-27.html.
"""
import glob, html, json, os, re

FONTE = 'saidas/09-analytics-e-insights/relatorios-geral-2026-10-27-diretoria.json'
MAPA = 'ferramentas/mapa-mental/saida/mapa-dados.json'
PECAS = 'ferramentas/entregaveis/dados/'
PAINEL = 'https://claude.ai/artifact/9RJcf5McdsLPewFA6kqy8z'
SAIDA = 'ferramentas/plano/saida/'
COPIA = 'saidas/02-estrategia-e-posicionamento/plano-diretoria-2026-10-27.html'
LIMITE = '2027-04-30'
HOJE = '2026-10-27'
CODIGO = re.compile(r'\b(?:OA|OB|OC|OU|PP|AMP|AGP|MP|EVM|AP|AD|AF|DEC|MO|OM|EM|KW|AT)\d+[A-Z]?(?:-[A-Z0-9]+)?\b|\b[GUPRAE]\d{1,2}\b')

d = json.load(open(FONTE, encoding='utf-8'))
mapa = json.load(open(MAPA, encoding='utf-8'))
pecas = [x for f in sorted(glob.glob(PECAS + '*.json')) for x in json.load(open(f, encoding='utf-8'))]

# Conferências do texto: sem travessão, sem código interno nos campos lidos pela diretoria
def textos(o, chave=''):
    if isinstance(o, dict):
        for k, v in o.items():
            if k != 'codigos': yield from textos(v, k)
    elif isinstance(o, list):
        for v in o: yield from textos(v, chave)
    elif isinstance(o, str) and chave not in ('id', 'linha', 'afeta', 'codigo', 'prazo', 'data', 'inicio', 'situacao'):
        yield o
erros = []
for t in textos(d):
    if '—' in t or '–' in t: erros.append('travessão: ' + t[:60])
    if CODIGO.search(t): erros.append('código interno: ' + CODIGO.search(t).group(0) + ' em ' + t[:70])
    if 'saidas/' in t or '.md' in t: erros.append('caminho de arquivo: ' + t[:60])
if erros:
    raise SystemExit('Texto com problema:\n' + '\n'.join(erros[:30]))

# Cursos do recorte, do mapa por curso
LIN = {'pos': 'Pós-graduação', 'graduacao': 'Graduação', 'eventos': 'Eventos', 'livres': 'Cursos Livres'}
KIT = {'aguardando_aprovacao': 'pronto para aprovar', 'a_fazer': 'a fazer', 'inventario_pendente': 'a conferir', 'devolvido': 'em ajuste',
       'revisar_por_mudanca': 'a revisar', 'nao_aplicavel': None, 'aprovado': 'aprovado'}
cursos = []
for j in mapa:
    if j['recorte'] != 'planejar' or j['codigo'] in ('68638', '560') or (j['inicio'] and j['inicio'] > LIMITE):
        continue
    n = j.get('nome_padrao') or ''
    if not n or n.startswith('[CONFIRMAR'): n = j['nome_no_site']
    est = [KIT.get(e['status'], e['status']) for e in j['kit']['entregas']]
    est = [e for e in est if e]
    if est and all(e == 'pronto para aprovar' for e in est): kit = 'Peças prontas para aprovar'
    elif any(e == 'pronto para aprovar' for e in est): kit = 'Parte das peças pronta'
    elif any(e == 'a revisar' for e in est): kit = 'Peças a revisar'
    elif est: kit = 'Peças a fazer'
    else: kit = 'Sem peças neste recorte'
    trav = [re.sub(r'\s+', ' ', CODIGO.sub('', p['descricao'] or '')).replace(' ()', '').strip(' ;,.') for p in j['pendencias'] if 'peca_final' in (p.get('bloqueia') or []) and not p.get('resolvida_em')]
    cursos.append({'l': j['linha'], 'tp': j['tipo'], 'n': n, 'c': '' if j['codigo'] == 'sem-codigo' else j['codigo'], 'i': j['inicio'], 'loc': j['local'],
                   'mod': j['modalidade_normalizada'], 'o': j['onda'], 'kit': kit, 'tr': trav[:6], 'ntr': len(trav)})
cursos.sort(key=lambda c: (list(LIN).index(c['l']) if c['l'] in LIN else 9, c['i'] or '9999', c['n']))

# Peças por linha, do painel
PUB = {'post', 'carrossel', 'reels', 'story', 'card_docente', 'video', 'whatsapp', 'email', 'pagina', 'anuncio'}
por_bloco = {}
for x in pecas:
    if x['tipo'] in PUB and not (x['tipo'] == 'pagina' and not x.get('conteudo')):
        b = por_bloco.setdefault(x['bloco'], {'total': 0, 'prontas': 0})
        b['total'] += 1
        b['prontas'] += x['status'] == 'aguardando_aprovacao'

DATA = json.dumps({'d': d, 'cursos': cursos, 'pecas': por_bloco, 'hoje': HOJE, 'painel': PAINEL}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
assert '—' not in DATA and '–' not in DATA

CSS = r"""
:root{
  /* Layout: largura total; abertura com o resumo e os números; linhas de produto em cartões; decisões por prazo; calendário por mês; cursos em grade filtrável */
  --bg:#eef1ee; --surface:#ffffff; --ink:#16211d; --muted:#56645f; --line:#d3dbd6; --soft:#e5ebe7;
  --accent:#1f6b58; --accent-soft:#d6e9e1; --accent-ink:#ffffff;
  --ok:#1f6b58; --ok-bg:#d6e9e1; --wait:#9a6200; --wait-bg:#fbefd6; --stop:#5f6d68; --stop-bg:#e3e8e5; --risk:#b3261e; --risk-bg:#fbe3e0;
  --f-display:"Bricolage Grotesque","Segoe UI Semibold",system-ui,sans-serif;
  --f-body:"Instrument Sans","Segoe UI",system-ui,sans-serif;
  --f-data:"JetBrains Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0e1412; --surface:#161f1c; --ink:#e4ece8; --muted:#9caba5; --line:#2a3833; --soft:#1d2925;
  --accent:#5cc2a6; --accent-soft:#1b3a31; --accent-ink:#0e1412;
  --ok:#5cc2a6; --ok-bg:#1b3a31; --wait:#f0bd57; --wait-bg:#3a2e12; --stop:#a3b1ab; --stop-bg:#25312d; --risk:#ff8a80; --risk-bg:#3c1f1c; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0e1412; --surface:#161f1c; --ink:#e4ece8; --muted:#9caba5; --line:#2a3833; --soft:#1d2925;
  --accent:#5cc2a6; --accent-soft:#1b3a31; --accent-ink:#0e1412;
  --ok:#5cc2a6; --ok-bg:#1b3a31; --wait:#f0bd57; --wait-bg:#3a2e12; --stop:#a3b1ab; --stop-bg:#25312d; --risk:#ff8a80; --risk-bg:#3c1f1c; color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{background:var(--bg)}
body{color:var(--ink);font:15.5px/1.55 var(--f-body);margin:0}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:30;background:var(--surface)}
.g{padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}
@media (max-width:600px){.g{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
a{color:var(--accent)}
header.top{background:var(--surface);border-bottom:1px solid var(--line)}
header.top .g{padding-block:28px 24px;display:grid;gap:22px}
.eyebrow{font:600 12px/1 var(--f-data);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font:700 clamp(30px,3.6vw,44px)/1.05 var(--f-display);margin:8px 0 0;letter-spacing:-.015em}
.resumo{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin:0;padding:0;list-style:none}
.resumo li{font-size:16.5px;line-height:1.45;padding-left:14px;border-left:3px solid var(--accent)}
.nums{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px}
.num{border:1px solid var(--line);border-radius:12px;padding:14px 16px;background:var(--bg);display:grid;gap:4px}
.num b{font:700 26px/1.05 var(--f-display);font-variant-numeric:tabular-nums}
.num span{font-size:14px;color:var(--muted);line-height:1.35}
.num small{font-size:12.5px;color:var(--muted)}
nav.sec{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--surface);border-bottom:1px solid var(--line)}
@media (max-width:760px){nav.sec{position:static}}
nav.sec .g{display:flex;gap:4px;flex-wrap:wrap;padding-block:10px;align-items:center}
nav.sec a{font-weight:600;text-decoration:none;color:var(--muted);padding:7px 13px;border-radius:999px;font-size:14.5px}
nav.sec a:hover{color:var(--ink);background:var(--soft)}
nav.sec .painel{margin-left:auto;background:var(--ink);color:var(--surface)}
nav.sec .painel:hover{background:var(--ink);color:var(--surface);opacity:.9}
main .g{padding-block:28px 64px;display:grid;gap:44px}
section{display:grid;gap:16px;scroll-margin-top:70px;min-width:0}
h2{font:700 clamp(22px,2.2vw,28px)/1.15 var(--f-display);margin:0;text-wrap:balance}
.sub{color:var(--muted);margin:0;max-width:80ch}
.pill{font:600 12px/1 var(--f-body);padding:5px 9px;border-radius:999px;white-space:nowrap;display:inline-block}
.s-pronto_para_aprovar{color:var(--ok);background:var(--ok-bg)} .s-parcial{color:var(--wait);background:var(--wait-bg)}
.s-em_espera{color:var(--risk);background:var(--risk-bg)} .s-suspenso{color:var(--stop);background:var(--stop-bg)}
/* Linhas */
.linhas{display:grid;grid-template-columns:repeat(auto-fill,minmax(380px,1fr));gap:14px}
@media (max-width:460px){.linhas{grid-template-columns:minmax(0,1fr)}}
.lin{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:18px;display:grid;gap:12px;align-content:start;min-width:0}
.lin header{display:flex;justify-content:space-between;gap:10px;align-items:flex-start;flex-wrap:wrap}
.lin h3{font:700 19px/1.2 var(--f-display);margin:0;text-wrap:balance}
.lin .fr{margin:0;font-size:15.5px}
.lin h4{font:600 12px var(--f-data);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:2px 0 4px}
.lin ul{margin:0;padding-left:18px;display:grid;gap:3px;font-size:14.5px}
.lin .ufape{background:var(--risk-bg);border-radius:10px;padding:10px 12px}
.lin .ufape h4{color:var(--risk)}
.lin .kv{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14px;color:var(--muted)}
.lin .kv b{color:var(--ink)}
.lin details summary{cursor:pointer;font-weight:600;font-size:14.5px}
.lin details ul{margin-top:6px;list-style:none;padding:0}
.lin details li{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid var(--line);padding:4px 0}
.lin details li span:last-child{font:600 12.5px var(--f-data);color:var(--muted);white-space:nowrap}
.lin .pcs{font-size:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.lin .pcs a{font-weight:600}
/* Decisões */
.dec{display:grid;gap:18px}
.grupo{display:grid;gap:8px}
.grupo h3{font:700 17px var(--f-display);margin:0;display:flex;gap:10px;align-items:baseline}
.grupo h3 span{font:600 13px var(--f-body);color:var(--muted)}
.q{display:grid;grid-template-columns:120px minmax(0,1fr) auto;gap:6px 16px;align-items:start;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 16px}
.q.urg{border-left:5px solid var(--risk)}
.q .pz{font:700 15px/1.2 var(--f-display)}
.q .pz small{display:block;font:600 11.5px var(--f-data);color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
.q .tx b{display:block;font-size:15.5px;line-height:1.35}
.q .tx span{color:var(--muted);font-size:14px}
.q .af{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end;max-width:260px}
.tag{font:600 11.5px var(--f-body);padding:4px 8px;border-radius:999px;background:var(--soft);white-space:nowrap}
@media (max-width:700px){.q{grid-template-columns:minmax(0,1fr)}.q .af{justify-content:flex-start;max-width:none}}
/* Calendário */
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:10px;align-items:start}
@media (max-width:1200px){.cal{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:700px){.cal{grid-template-columns:minmax(0,1fr)}}
.mes{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px;display:grid;gap:8px;align-content:start;min-width:0}
.mes h3{font:700 16px var(--f-display);margin:0;padding-bottom:6px;border-bottom:1px solid var(--line);text-transform:capitalize}
.mc{display:grid;grid-template-columns:44px minmax(0,1fr);gap:8px;font-size:14px;line-height:1.35}
.mc b{font:700 13px var(--f-data);font-variant-numeric:tabular-nums}
.mc small{display:block;color:var(--muted);font-size:12.5px}
.mc.hoje b{color:var(--accent)}
/* Aprovações */
.aps{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px}
.ap{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:grid;gap:4px}
.ap b{font-size:14.5px} .ap span{color:var(--muted);font-size:13.5px}
/* Cursos */
.fil{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.fil input,.fil select{font:inherit;font-size:14px;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:8px 13px;min-width:0;max-width:100%}
.fil input{flex:1 1 260px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
@media (max-width:360px){.grid{grid-template-columns:minmax(0,1fr)}}
.cur{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:grid;gap:6px;align-content:start;min-width:0}
.cur .t{display:flex;justify-content:space-between;gap:8px;align-items:baseline}
.cur b{font-size:15px;line-height:1.3;overflow-wrap:anywhere}
.cur .cod{font:600 11.5px var(--f-data);color:var(--muted)}
.cur .m{font-size:13.5px;color:var(--muted)}
.cur .k{font-size:13px;font-weight:600}
.cur .k.ok{color:var(--ok)} .cur .k.wait{color:var(--wait)} .cur .k.stop{color:var(--stop)}
.cur details summary{cursor:pointer;font-size:13.5px;color:var(--risk);font-weight:600}
.cur details ul{margin:6px 0 0;padding-left:18px;font-size:13.5px;display:grid;gap:3px}
.cnt{font-size:14px;color:var(--muted)}
.prox{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}
.prox div{background:var(--surface);border:1px dashed var(--line);border-radius:12px;padding:12px 14px}
.prox b{display:block}
.avisos{margin:0;padding-left:20px;display:grid;gap:4px;color:var(--muted);max-width:90ch}
footer .g{padding-block:0 32px;color:var(--muted);font-size:13px}
"""

JS = r"""
const X=__DATA__, D=X.d, HOJE=X.hoje;
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const MES=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
const dm=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7):'-';
const dma=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7)+'/'+iso.slice(0,4):'-';
const SIT={pronto_para_aprovar:'Pronto para aprovar',parcial:'Em parte pronto',em_espera:'Esperando a Ufape',suspenso:'Suspenso por decisão'};
const NOMEL={};(D.linhas||[]).forEach(l=>NOMEL[l.id]=l.nome);
const ul=a=>(a&&a.length)?`<ul>${a.map(x=>`<li>${esc(x)}</li>`).join('')}</ul>`:'';
// cabeçalho
$('#h-data').textContent=dma(D.data);
$('#resumo').innerHTML=(D.resumo||[]).map(f=>`<li>${esc(f)}</li>`).join('');
$('#nums').innerHTML=(D.numeros||[]).map(n=>`<div class="num"><b>${esc(n.valor)}</b><span>${esc(n.rotulo)}</span>${n.nota?`<small>${esc(n.nota)}</small>`:''}</div>`).join('');
// linhas
$('#linhas').innerHTML=(D.linhas||[]).map(l=>{const pc=X.pecas[l.id];
  return `<article class="lin" id="l-${esc(l.id)}"><header><h3>${esc(l.nome)}</h3><span class="pill s-${esc(l.situacao)}">${esc(SIT[l.situacao]||l.situacao)}</span></header>
  <p class="fr">${esc(l.frase)}</p>
  ${(l.pronto||[]).length?`<div><h4>Pronto</h4>${ul(l.pronto)}</div>`:''}
  ${(l.falta||[]).length?`<div><h4>Falta fazer</h4>${ul(l.falta)}</div>`:''}
  ${(l.depende_da_ufape||[]).length?`<div class="ufape"><h4>Depende da Ufape</h4>${ul(l.depende_da_ufape)}</div>`:''}
  ${(l.verba||l.meta)?`<div class="kv">${l.verba?`<span>Verba: <b>${esc(l.verba)}</b></span>`:''}${l.meta?`<span>Meta: <b>${esc(l.meta)}</b></span>`:''}</div>`:''}
  ${pc?`<div class="pcs"><span><b>${pc.total}</b> peças escritas, <b>${pc.prontas}</b> prontas para aprovar.</span><a href="${X.painel}" target="_blank" rel="noopener">Ver as peças no painel</a></div>`:''}
  ${(l.turmas||[]).length?`<details><summary>${l.turmas.length} ${l.turmas.length===1?'turma':'turmas'} e datas de início</summary><ul>${l.turmas.map(t=>`<li><span>${esc(t.nome)}${t.nota?` <small>(${esc(t.nota)})</small>`:''}</span><span>${t.inicio?dma(t.inicio):'-'}</span></li>`).join('')}</ul></details>`:''}
  </article>`;}).join('');
// decisões
const dec=(D.decisoes||[]).slice().sort((a,b)=>(a.prazo||'9999').localeCompare(b.prazo||'9999'));
const addD=(iso,n)=>{const d=new Date(iso+'T12:00:00');d.setDate(d.getDate()+n);return d.toISOString().slice(0,10);};
const grupos=[['Esta semana',x=>x.prazo&&x.prazo<=addD(HOJE,6),'até '+dm(addD(HOJE,6))],['Em novembro',x=>x.prazo&&x.prazo>addD(HOJE,6)&&x.prazo<='2026-11-30',''],['Dezembro em diante',x=>x.prazo&&x.prazo>'2026-11-30',''],['Sem prazo definido',x=>!x.prazo,'responder assim que possível']];
$('#dec').innerHTML=grupos.map(([t,f,s])=>{const g=dec.filter(f);if(!g.length)return '';return `<div class="grupo"><h3>${esc(t)} <span>${g.length} ${g.length===1?'item':'itens'}${s?' · '+esc(s):''}</span></h3>${g.map(q=>`<div class="q${t==='Esta semana'?' urg':''}"><span class="pz">${esc(q.prazo_texto||(q.prazo?'até '+dm(q.prazo):'sem prazo'))}<small>${q.prazo?dma(q.prazo):''}</small></span><span class="tx"><b>${esc(q.pergunta)}</b><span>${esc(q.por_que)}</span></span><span class="af">${(q.afeta||[]).map(a=>`<span class="tag">${esc(NOMEL[a]||a)}</span>`).join('')}</span></div>`).join('')}</div>`;}).join('');
// calendário
const marcos=(D.marcos||[]).slice().sort((a,b)=>a.data.localeCompare(b.data));
const meses=[];for(let y=2026,m=9;!(y===2027&&m===4);){meses.push([y,m]);m++;if(m===12){m=0;y++;}}
$('#cal').innerHTML=meses.map(([y,m])=>{const k=y+'-'+String(m+1).padStart(2,'0');const g=marcos.filter(x=>x.data.startsWith(k));
  return `<div class="mes"><h3>${MES[m]} ${y}</h3>${g.map(x=>`<div class="mc${x.data===HOJE?' hoje':''}"><b>${dm(x.data)}</b><span>${esc(x.titulo)}<small>${esc(NOMEL[x.linha]||'')}</small></span></div>`).join('')||'<span class="sub">Sem marco principal.</span>'}</div>`;}).join('');
// aprovações
$('#aps').innerHTML=(D.aprovacoes||[]).map(a=>`<div class="ap"><b>${esc(a.o_que)}</b><span>${esc(NOMEL[a.linha]||a.linha)}${a.quando?' · '+esc(a.quando):''}</span></div>`).join('');
// cursos
const LIN={pos:'Pós-graduação',graduacao:'Graduação',eventos:'Eventos',livres:'Cursos Livres'};
const TP={prova_de_bolsa:'Prova de bolsa',minicurso:'Minicurso',aprimoramento:'Aprimoramento',workshop:'Workshop'};
$('#f-l').innerHTML='<option value="">Todas as linhas</option>'+Object.entries(LIN).map(([k,v])=>`<option value="${k}">${v}</option>`).join('');
function cursos(){const q=$('#f-q').value.trim().toLowerCase(),l=$('#f-l').value,so=$('#f-t').checked;
  const xs=X.cursos.filter(c=>(!l||c.l===l)&&(!so||c.ntr)&&(!q||(c.n+' '+c.c+' '+(c.loc||'')).toLowerCase().includes(q)));
  $('#cnt').textContent=`${xs.length} de ${X.cursos.length} cursos, turmas, provas e eventos`;
  $('#grid').innerHTML=xs.map(c=>{const k=/prontas/.test(c.kit)?'ok':/parte|revisar/.test(c.kit)?'wait':'stop';
    return `<div class="cur"><div class="t"><b>${esc(c.n)}</b>${c.c?`<span class="cod">${esc(c.c)}</span>`:''}</div><span class="m">${esc(LIN[c.l]||c.l)}${TP[c.tp]?' · '+TP[c.tp]:''} · ${c.i?'início '+dma(c.i):'sem data fixa'}${c.loc?' · '+esc(c.loc):''}</span><span class="k ${k}">${esc(c.kit)}</span>${c.ntr?`<details><summary>${c.ntr} ${c.ntr===1?'resposta pendente':'respostas pendentes'} da Ufape</summary><ul>${c.tr.map(t=>`<li>${esc(t)}</li>`).join('')}</ul></details>`:''}</div>`;}).join('')||'<p class="sub">Nenhum curso com esses filtros.</p>';}
['#f-q','#f-l','#f-t'].forEach(s=>$(s).addEventListener('input',cursos));cursos();
// próxima etapa e avisos
$('#prox').innerHTML=(D.proxima_etapa||[]).map(p=>`<div><b>${esc(p.titulo)}</b><span class="sub">${esc(p.frase)}</span></div>`).join('');
$('#avisos').innerHTML=(D.avisos||[]).map(a=>`<li>${esc(a)}</li>`).join('');
"""

HTML = f"""<title>Plano de marketing Ufape</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Instrument+Sans:wght@400;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap">
<style>{CSS}</style>
<header class="top"><div class="g">
<div><span class="eyebrow">Situação em <span id="h-data"></span> · tudo o que começa até abril de 2027</span>
<h1>Plano de marketing Ufape</h1></div>
<ul class="resumo" id="resumo"></ul>
<div class="nums" id="nums"></div>
</div></header>
<nav class="sec" aria-label="Seções"><div class="g">
<a href="#linhas-s">Onde estamos</a><a href="#decisoes">O que a Ufape precisa decidir</a><a href="#calendario">Calendário</a><a href="#aprovacoes">Aprovações</a><a href="#cursos">Todos os cursos</a><a href="#proxima">Próxima etapa</a>
<a class="painel" href="{PAINEL}" target="_blank" rel="noopener">Ver as peças</a>
</div></nav>
<main><div class="g">
<section id="linhas-s"><h2>Onde estamos, linha por linha</h2><p class="sub">Cada cartão diz o que está pronto, o que falta e o que depende de uma resposta da Ufape. Nada foi publicado, enviado ou pago.</p><div class="linhas" id="linhas"></div></section>
<section id="decisoes"><h2>O que a Ufape precisa decidir ou responder</h2><p class="sub">Em ordem de prazo. Sem essas respostas, as peças prontas não podem ir ao ar.</p><div class="dec" id="dec"></div></section>
<section id="calendario"><h2>Calendário até abril de 2027</h2><p class="sub">As datas principais de cada mês. O dia a dia de cada peça está no painel de entregáveis.</p><div class="cal" id="cal"></div></section>
<section id="aprovacoes"><h2>O que a pessoa do marketing aprova</h2><div class="aps" id="aps"></div></section>
<section id="cursos"><h2>Todos os cursos deste recorte</h2>
<div class="fil"><input id="f-q" type="search" placeholder="Buscar curso, código ou cidade" aria-label="Buscar curso"><select id="f-l" aria-label="Linha"></select><label for="f-t" class="cnt"><input id="f-t" type="checkbox"> Só os que esperam resposta da Ufape</label><span class="cnt" id="cnt"></span></div>
<div class="grid" id="grid"></div></section>
<section id="proxima"><h2>Próxima etapa</h2><div class="prox" id="prox"></div><h3 class="sub" style="font-weight:600;margin-top:8px">Ainda a confirmar</h3><ul class="avisos" id="avisos"></ul></section>
</div></main>
<footer><div class="g"><p>Feito pela equipe de marketing a partir dos planos aprovados pela revisão de qualidade. Datas da planilha de cursos; preços e demais dados do site, lido em 26/10/2026. Não há dado pessoal de aluno ou candidato.</p></div></footer>
<script>{JS.replace('__DATA__', DATA)}</script>
"""
os.makedirs(SAIDA, exist_ok=True)
open(SAIDA + 'plano-artifact.html', 'w', encoding='utf-8').write(HTML)
completo = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HTML.split('<header', 1)[0] + '</head>\n<body>\n<header' + HTML.split('<header', 1)[1] + '</body>\n</html>\n')
open(COPIA, 'w', encoding='utf-8').write(completo)
print('linhas', len(d.get('linhas', [])), 'decisões', len(d.get('decisoes', [])), 'marcos', len(d.get('marcos', [])), 'cursos', len(cursos), 'tamanho', len(completo))
