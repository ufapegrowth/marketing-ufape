"""Painel de entregáveis: calendário, linha do tempo por turma e leitor do texto de cada peça.

Rodar da raiz do repositório:
    python3 -I ferramentas/entregaveis/painel.py
Lê ferramentas/entregaveis/dados/*.json (esquema em ferramentas/entregaveis/ESQUEMA.md),
embute o texto dos arquivos citados e grava:
  ferramentas/entregaveis/saida/painel-artifact.html (para publicar como página)
  saidas/10-operacoes-de-marketing/painel-de-entregaveis-2026-10-27.html (cópia com doctype)
"""
import glob, json, os, re

HOJE = '2026-10-27'
DADOS = 'ferramentas/entregaveis/dados/'
SAIDA = 'ferramentas/entregaveis/saida/'
COPIA = 'saidas/10-operacoes-de-marketing/painel-de-entregaveis-2026-10-27.html'
BLOCOS = {
    'pos-onda1': 'Pós, turmas de out. e nov. de 2026',
    'workshop': 'Workshop de Neuromonitorização',
    'pos-marco': 'Pós, turmas de março de 2027',
    'pos-abril': 'Pós, turmas de abril de 2027',
    'graduacao': 'Graduação 2027.1',
}
TIPOS = {'post', 'carrossel', 'reels', 'story', 'card_docente', 'video', 'whatsapp', 'email', 'pagina', 'anuncio',
         'campanha_subida', 'campanha_fase', 'campanha_pausa', 'conferencia', 'aprovacao', 'relatorio', 'inicio_turma', 'outro'}
STATUS = {'aguardando_aprovacao', 'em_correcao', 'a_fazer', 'suspenso', 'executado'}

pecas, erros = [], []
for p in sorted(glob.glob(DADOS + '*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        if x.get('bloco') not in BLOCOS: erros.append(f"{p}: bloco {x.get('bloco')}")
        if x.get('tipo') not in TIPOS: erros.append(f"{p}: tipo {x.get('tipo')} em {x.get('id')}")
        if x.get('status') not in STATUS: erros.append(f"{p}: status {x.get('status')} em {x.get('id')}")
        for c in ('data', 'data_fim'):
            if x.get(c) and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', x[c]): erros.append(f"{p}: {c} {x[c]} em {x['id']}")
        pecas.append(x)
ids = [x['id'] for x in pecas]
dup = {i for i in ids if ids.count(i) > 1}
if dup: erros.append('ids repetidos: ' + ', '.join(sorted(dup)[:10]))

# Texto dos arquivos citados, para o leitor abrir a peça
textos = {}
for x in pecas:
    a = x.get('arquivo')
    if a and a not in textos:
        if os.path.exists(a):
            textos[a] = open(a, encoding='utf-8').read()
        else:
            erros.append('arquivo não encontrado: ' + a)
for x in pecas:
    a, l = x.get('arquivo'), x.get('linha')
    if a in textos and (not isinstance(l, int) or l < 1 or l > textos[a].count('\n') + 1):
        erros.append(f"linha {l} fora do arquivo em {x['id']}")
if erros:
    raise SystemExit('Dados com problema:\n' + '\n'.join(erros[:40]))

TEXTO = '—–'
for t in list(textos.values()) + [json.dumps(pecas, ensure_ascii=False)]:
    assert not any(c in t for c in TEXTO), 'travessão ou meia-risca nos dados ou nos arquivos'

# Nome de cada turma para a linha do tempo, do mapa por curso
NOMES = {'medicina-veterinaria': 'Medicina Veterinária', 'pedagogia': 'Pedagogia', 'workshop': 'Workshop de Neuromonitorização'}
for j in json.load(open('ferramentas/mapa-mental/saida/mapa-dados.json', encoding='utf-8')):
    n = j.get('nome_padrao') or ''
    if not n or n.startswith('[CONFIRMAR'):
        n = j.get('nome_no_site') or ''
    if j['codigo'] and n:
        NOMES.setdefault(j['codigo'], n.replace('Pós-graduação em ', ''))
CURTO = {'pos-onda1': 'Pós out/nov', 'workshop': 'Workshop', 'pos-marco': 'Pós março', 'pos-abril': 'Pós abril', 'graduacao': 'Graduação'}
DATA = json.dumps({'hoje': HOJE, 'blocos': BLOCOS, 'curto': CURTO, 'nomes': NOMES, 'pecas': pecas, 'arquivos': textos}, ensure_ascii=False, separators=(',', ':'))
DATA = DATA.replace('</', '<\\/')

CSS = r"""
:root{
  /* Layout: cabeçalho com o resumo de hoje, abas (Agora, Calendário, Linha do tempo, Lista) e leitor lateral da peça */
  --bg:#f2f4f1; --surface:#ffffff; --ink:#17231f; --muted:#5a6863; --line:#d5ddd8; --soft:#e7ede9;
  --accent:#1f6b58; --accent-soft:#d9eae3;
  --c-social:#c2552f; --c-msg:#2f62b8; --c-midia:#7b4bb0; --c-site:#1f6b58; --c-marco:#8a6d1d;
  --s-ag:#a86b00; --s-cor:#b3261e; --s-faz:#6c7a75; --s-ok:#2e7d32;
  --f-display:"Bricolage Grotesque","Segoe UI Semibold",system-ui,sans-serif;
  --f-body:"Instrument Sans","Segoe UI",system-ui,sans-serif;
  --f-data:"JetBrains Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0f1513; --surface:#17201d; --ink:#e3ebe7; --muted:#9aa9a3; --line:#2a3833; --soft:#1e2a26;
  --accent:#5cc2a6; --accent-soft:#1c3a32;
  --c-social:#f08a62; --c-msg:#7fa6f0; --c-midia:#b693e6; --c-site:#5cc2a6; --c-marco:#dcbc5a;
  --s-ag:#e3b04b; --s-cor:#ff8a80; --s-faz:#8d9b96; --s-ok:#81c784; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0f1513; --surface:#17201d; --ink:#e3ebe7; --muted:#9aa9a3; --line:#2a3833; --soft:#1e2a26;
  --accent:#5cc2a6; --accent-soft:#1c3a32;
  --c-social:#f08a62; --c-msg:#7fa6f0; --c-midia:#b693e6; --c-site:#5cc2a6; --c-marco:#dcbc5a;
  --s-ag:#e3b04b; --s-cor:#ff8a80; --s-faz:#8d9b96; --s-ok:#81c784; color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none!important}
body{background:var(--bg);color:var(--ink);font:15px/1.5 var(--f-body);margin:0}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:30;background:var(--surface)}
.wrap{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));max-width:1240px;margin:0 auto}
header.top{background:var(--surface);border-bottom:1px solid var(--line)}
header.top .wrap{padding-block:20px 16px;display:grid;gap:14px}
.eyebrow{font:600 12px/1 var(--f-data);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font:700 clamp(24px,3.2vw,32px)/1.1 var(--f-display);margin:4px 0 0;letter-spacing:-.01em;text-wrap:balance}
.lede{color:var(--muted);margin:0;max-width:78ch}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.kpi{border:1px solid var(--line);border-radius:10px;padding:10px 12px;display:grid;gap:2px;background:var(--bg)}
.kpi b{font:700 22px/1.1 var(--f-display);font-variant-numeric:tabular-nums}
.kpi span{font-size:13px;color:var(--muted)}
@media (max-width:720px){nav.tabs{position:static!important}}
nav.tabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--surface);border-bottom:1px solid var(--line)}
nav.tabs .wrap{display:flex;gap:4px;flex-wrap:wrap;padding-block:8px;align-items:center}
nav.tabs a{font-weight:600;text-decoration:none;color:var(--muted);padding:7px 12px;border-radius:8px}
nav.tabs a[aria-current="page"]{background:var(--accent-soft);color:var(--ink)}
nav.tabs a:hover{color:var(--ink)}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto}
.filters select,.filters input{font:inherit;font-size:14px;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:6px 9px;min-width:0}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
main .wrap{padding-block:20px 56px;display:grid;gap:20px}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:13px;color:var(--muted)}
.dot{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px}
.k-social{--k:var(--c-social)} .k-msg{--k:var(--c-msg)} .k-midia{--k:var(--c-midia)} .k-site{--k:var(--c-site)} .k-marco{--k:var(--c-marco)}
h2{font:700 20px/1.2 var(--f-display);margin:0;text-wrap:balance}
h3.grp{font:600 13px/1 var(--f-data);letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:6px 0 0}
.note{font-size:14px;color:var(--muted);max-width:80ch;margin:0}
/* Agora */
.agora{display:grid;gap:18px}
.semana{display:grid;gap:8px}
.semana>header{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.semana>header .meta{color:var(--muted);font-size:13px}
.rows{display:grid;gap:6px}
.row{display:grid;grid-template-columns:92px 1fr auto;gap:4px 12px;align-items:center;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--k);border-radius:8px;padding:9px 12px;cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%}
.row:hover{border-color:var(--k)}
.row .d{font:600 13px/1.2 var(--f-data);font-variant-numeric:tabular-nums;color:var(--muted)}
.row .t{min-width:0}
.row .t b{font-weight:600;display:block;overflow-wrap:anywhere}
.row .t small{color:var(--muted);font-size:13px}
.row .st{display:flex;gap:6px;flex-wrap:wrap;justify-content:flex-end}
.pill{font:600 11px/1 var(--f-data);letter-spacing:.02em;padding:4px 7px;border-radius:999px;white-space:nowrap;border:1px solid currentColor}
.p-aguardando_aprovacao{color:var(--s-ag)} .p-em_correcao{color:var(--s-cor)} .p-a_fazer,.p-suspenso{color:var(--s-faz)} .p-executado{color:var(--s-ok)}
.p-trava{color:var(--s-cor);border-style:dashed}
.p-atraso{color:var(--surface);background:var(--s-cor);border-color:var(--s-cor)}
.empty{color:var(--muted);padding:10px 0}
/* Calendário */
.calnav{display:flex;margin-top:6px;gap:8px;align-items:center;flex-wrap:wrap}
.calnav button{font:inherit;font-weight:600;background:var(--surface);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:6px 12px;cursor:pointer}
.calnav .mes{font:700 20px/1.2 var(--f-display);min-width:190px}
.cal{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:4px}
.cal .wd{font:600 12px/1 var(--f-data);color:var(--muted);text-transform:uppercase;letter-spacing:.05em;padding:4px 6px}
.day{background:var(--surface);border:1px solid var(--line);border-radius:8px;min-height:104px;padding:6px;display:grid;align-content:start;gap:3px;min-width:0}
.day.fora{background:transparent;border-style:dashed;opacity:.55}
.day.hoje{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.day .n{font:600 12px/1 var(--f-data);color:var(--muted);display:flex;justify-content:space-between}
.chip{display:block;width:100%;text-align:left;font:12px/1.25 var(--f-body);color:var(--ink);background:var(--soft);border:0;border-left:3px solid var(--k);border-radius:4px;padding:3px 5px;cursor:pointer;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.chip:hover{background:var(--accent-soft)}
.mais{font:600 12px var(--f-body);background:none;border:0;color:var(--accent);cursor:pointer;text-align:left;padding:2px}
@media (max-width:720px){.cal .wd{font-size:10px;padding:2px}.day{min-height:64px;padding:4px}.chip{font-size:0;height:8px;padding:0;border-left-width:0;background:var(--k)}.day .n{font-size:11px}}
/* Linha do tempo */
#v{min-width:0}
.gantt{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
.gantt svg{display:block}
.gantt text{fill:var(--ink);font:12px var(--f-body)}
.gantt .ax{fill:var(--muted);font:11px var(--f-data)}
.gantt .grid{stroke:var(--line)}
.gantt .hoje{stroke:var(--accent);stroke-width:2}
.gantt .mk{cursor:pointer}
/* Lista */
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
table{border-collapse:collapse;width:100%;font-size:13.5px}
th,td{text-align:left;padding:7px 10px;border-bottom:1px solid var(--line);vertical-align:top}
th{color:var(--muted);font:600 12px var(--f-data);text-transform:uppercase;letter-spacing:.04em;position:sticky;top:0;background:var(--surface)}
tbody tr{cursor:pointer} tbody tr:hover{background:var(--soft)}
td.d{font-family:var(--f-data);white-space:nowrap;font-variant-numeric:tabular-nums}
/* Leitor */
.reader{position:fixed;top:0;right:0;bottom:0;width:min(720px,100%);background:var(--surface);border-left:1px solid var(--line);z-index:40;display:grid;grid-template-rows:auto 1fr;box-shadow:-12px 0 32px rgba(0,0,0,.12)}
.reader>header{padding:calc(14px + env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) 12px 18px;border-bottom:1px solid var(--line);display:grid;gap:8px}
.reader .close{justify-self:end;font:inherit;font-weight:600;background:var(--bg);border:1px solid var(--line);border-radius:8px;padding:5px 12px;cursor:pointer;color:var(--ink)}
.reader h2{font-size:19px}
.reader dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:4px 14px;margin:0;font-size:13px}
.reader dt{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.05em}
.reader dd{margin:0;overflow-wrap:anywhere}
.reader .body{overflow:auto;padding:16px max(16px,env(safe-area-inset-right,0px)) calc(32px + env(safe-area-inset-bottom,0px)) 18px;display:grid;gap:10px;align-content:start}
.reader .acts{display:flex;gap:8px;flex-wrap:wrap}
.reader .acts button{font:inherit;font-size:13px;font-weight:600;background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:5px 10px;cursor:pointer}
.md{font-size:14.5px;display:grid;gap:8px;min-width:0}
.md h1,.md h2,.md h3,.md h4{font-family:var(--f-display);margin:10px 0 0;text-wrap:balance}
.md h1{font-size:20px}.md h2{font-size:18px}.md h3{font-size:16px}.md h4{font-size:15px}
.md p{margin:0;max-width:72ch}
.md blockquote{margin:0;padding:8px 12px;border-left:3px solid var(--accent);background:var(--soft);border-radius:0 6px 6px 0}
.md ul,.md ol{margin:0;padding-left:22px;display:grid;gap:3px}
.md code{font:12.5px var(--f-data);background:var(--soft);padding:1px 4px;border-radius:4px;overflow-wrap:anywhere}
.md .tbl{border-radius:6px}
.md .hl{background:var(--accent-soft);border-radius:6px;box-shadow:0 0 0 6px var(--accent-soft)}
.md .mk{font:600 12px var(--f-data);color:var(--s-ag)}
.shade{position:fixed;inset:0;background:rgba(0,0,0,.28);z-index:35}
@media (prefers-reduced-motion:no-preference){.reader{animation:entra .18s ease-out}@keyframes entra{from{transform:translateX(24px);opacity:.6}to{transform:none;opacity:1}}}
footer .wrap{padding-block:0 32px;color:var(--muted);font-size:13px;display:grid;gap:6px}
"""

JS = r"""
const DADOS=__DATA__;
const HOJE=DADOS.hoje, B=DADOS.blocos, P=DADOS.pecas, ARQ=DADOS.arquivos, NOMES=DADOS.nomes, CURTO=DADOS.curto;
const CAT={post:'social',carrossel:'social',reels:'social',story:'social',card_docente:'social',video:'social',whatsapp:'msg',email:'msg',pagina:'site',anuncio:'midia',campanha_subida:'midia',campanha_fase:'midia',campanha_pausa:'midia',conferencia:'marco',aprovacao:'marco',relatorio:'marco',inicio_turma:'marco',outro:'marco'};
const CATN={social:'Redes sociais e vídeo',msg:'WhatsApp e e-mail',midia:'Mídia paga',site:'Página da turma',marco:'Marcos, aprovações e conferências'};
const TIPON={post:'Post',carrossel:'Carrossel',reels:'Reels',story:'Story',card_docente:'Card de docente',video:'Vídeo',whatsapp:'WhatsApp',email:'E-mail',pagina:'Página',anuncio:'Anúncio',campanha_subida:'Subida de campanha',campanha_fase:'Troca de fase da campanha',campanha_pausa:'Pausa de campanha',conferencia:'Conferência',aprovacao:'Aprovação',relatorio:'Relatório',inicio_turma:'Início da turma',outro:'Marco'};
const STN={aguardando_aprovacao:'aguarda sua aprovação',em_correcao:'em correção',a_fazer:'a fazer',suspenso:'suspenso',executado:'feito'};
const ROT={'medicina-veterinaria':'Med. Vet.',pedagogia:'Pedagogia',workshop:'Workshop'};
const MES=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
const WD=['seg','ter','qua','qui','sex','sáb','dom'];
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const fmt=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7)+'/'+iso.slice(0,4):'-';
const fmtc=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7):'-';
const toD=iso=>new Date(iso+'T12:00:00');
const isoD=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const addD=(iso,n)=>{const d=toD(iso);d.setDate(d.getDate()+n);return isoD(d);};
const segunda=iso=>{const d=toD(iso);const w=(d.getDay()+6)%7;d.setDate(d.getDate()-w);return isoD(d);};
const turmasTxt=x=>x.turmas.join(', ');
const atrasada=x=>x.data&&x.data<HOJE&&x.status!=='executado';

// filtros
const F={bloco:'',cat:'',status:'',q:''};
function fill(){
  $('#f-bloco').innerHTML='<option value="">Todos os blocos</option>'+Object.entries(B).map(([k,v])=>`<option value="${k}">${esc(v)}</option>`).join('');
  $('#f-cat').innerHTML='<option value="">Todos os tipos</option>'+Object.entries(CATN).map(([k,v])=>`<option value="${k}">${esc(v)}</option>`).join('');
  $('#f-status').innerHTML='<option value="">Toda situação</option>'+Object.entries(STN).map(([k,v])=>`<option value="${k}">${esc(v)}</option>`).join('');
}
function pass(x){
  if(F.bloco&&x.bloco!==F.bloco) return false;
  if(F.cat&&CAT[x.tipo]!==F.cat) return false;
  if(F.status&&x.status!==F.status) return false;
  if(F.q){const q=F.q.toLowerCase();if(!(x.titulo.toLowerCase().includes(q)||x.turmas.join(' ').includes(q)||(TIPON[x.tipo]||'').toLowerCase().includes(q))) return false;}
  return true;
}
const sel=()=>P.filter(pass);
const ord=(a,b)=>(a.data||'9999').localeCompare(b.data||'9999')||(a.hora||'').localeCompare(b.hora||'')||a.bloco.localeCompare(b.bloco);
function pills(x){
  const out=[];
  if(atrasada(x)) out.push('<span class="pill p-atraso">data já passou</span>');
  out.push(`<span class="pill p-${x.status}">${esc(STN[x.status])}</span>`);
  if(x.trava&&x.trava.length) out.push(`<span class="pill p-trava" title="${esc(x.trava.join(', '))}">trava ${esc(x.trava.slice(0,3).join(', '))}${x.trava.length>3?' +'+(x.trava.length-3):''}</span>`);
  return out.join('');
}
function row(x){
  const quando=x.data?fmtc(x.data)+(x.data_fim?' a '+fmtc(x.data_fim):'')+(x.hora?' '+x.hora:''):(x.quando||'sem data');
  return `<button class="row k-${CAT[x.tipo]}" data-id="${esc(x.id)}"><span class="d">${esc(quando)}</span><span class="t"><b>${esc(x.titulo)}</b><small>${esc(TIPON[x.tipo])} · ${esc(x.canal)} · ${esc(B[x.bloco])} · ${esc(turmasTxt(x))}</small></span><span class="st">${pills(x)}</span></button>`;
}
// Aba Agora
function vAgora(){
  const xs=sel().sort(ord), seg=segunda(HOJE);
  const grupos=[
    ['Data já passou e ainda não foi aprovada',x=>atrasada(x),'Peças com data anterior a hoje que continuam em rascunho. Precisam de aprovação ou de data nova.'],
    ['Esta semana',x=>x.data&&x.data>=HOJE&&x.data<addD(seg,7),`De ${fmtc(HOJE)} a ${fmtc(addD(seg,6))}`],
    ['Próxima semana',x=>x.data&&x.data>=addD(seg,7)&&x.data<addD(seg,14),`De ${fmtc(addD(seg,7))} a ${fmtc(addD(seg,13))}`],
    ['Daqui a 2 a 4 semanas',x=>x.data&&x.data>=addD(seg,14)&&x.data<addD(seg,35),`De ${fmtc(addD(seg,14))} a ${fmtc(addD(seg,34))}`],
  ];
  const html=grupos.map(([t,f,m])=>{const g=xs.filter(f);return `<section class="semana"><header><h2>${esc(t)}</h2><span class="meta">${esc(m)} · ${g.length} ${g.length===1?'peça':'peças'}</span></header><div class="rows">${g.length?g.map(row).join(''):'<p class="empty">Nada neste período com os filtros atuais.</p>'}</div></section>`;}).join('');
  const depois=xs.filter(x=>x.data&&x.data>=addD(seg,35)).length, sem=xs.filter(x=>!x.data).length;
  $('#v').innerHTML=`<div class="agora">${html}<p class="note">Depois disso: ${depois} peças com data, até abril de 2027 (veja o Calendário e a Linha do tempo). Sem data fixa: ${sem} peças que disparam por evento, como as mensagens que saem após o cadastro (veja a Lista).</p></div>`;
}
// Aba Calendário
let mesAtual=HOJE.slice(0,7);
function vCal(){
  const [y,m]=mesAtual.split('-').map(Number);
  const seg=isoD(new Date(y,m,1,12)).slice(0,7);
  $('#v').innerHTML=`<div class="calnav"><button id="m-prev" aria-label="Mês anterior">‹</button><button id="m-next" aria-label="Próximo mês">›</button><button id="m-hoje">Hoje</button><span class="note">Dois meses por vez. Clique numa peça para ler o texto.</span></div><div id="cal1"></div><div id="cal2"></div><div id="dia"></div>`;
  $('#m-prev').onclick=()=>{mesAtual=isoD(new Date(y,m-2,1,12)).slice(0,7);vCal();};
  $('#m-next').onclick=()=>{mesAtual=isoD(new Date(y,m,1,12)).slice(0,7);vCal();};
  $('#m-hoje').onclick=()=>{mesAtual=HOJE.slice(0,7);vCal();};
  mesCal(mesAtual,'#cal1'); mesCal(seg,'#cal2');
}
function mesCal(mesX,alvo){
  const xs=sel(); const [y,m]=mesX.split('-').map(Number);
  const first=new Date(y,m-1,1,12), ini=new Date(first); ini.setDate(1-((first.getDay()+6)%7));
  const porDia={}; for(const x of xs){ if(!x.data) continue; const fim=x.data_fim&&CAT[x.tipo]!=='midia'?x.data_fim:x.data; (porDia[x.data]=porDia[x.data]||[]).push(x); }
  let cells=WD.map(w=>`<div class="wd">${w}</div>`).join('');
  for(let i=0;i<42;i++){const d=new Date(ini);d.setDate(ini.getDate()+i);const iso=isoD(d);const fora=d.getMonth()!==m-1;
    if(i>=35&&fora&&d.getDate()<=7&&i%7===0) break;
    const list=fora?[]:(porDia[iso]||[]).sort(ord); const max=4;
    cells+=`<div class="day${fora?' fora':''}${iso===HOJE&&!fora?' hoje':''}"><span class="n"><span>${d.getDate()}</span>${list.length?`<span>${list.length}</span>`:''}</span>${list.slice(0,max).map(x=>`<button class="chip k-${CAT[x.tipo]}" data-id="${esc(x.id)}" title="${esc(TIPON[x.tipo]+': '+x.titulo)}">${esc(ROT[x.turmas[0]]||x.turmas[0]||'')} ${esc(TIPON[x.tipo])}</button>`).join('')}${list.length>max?`<button class="mais" data-dia="${iso}">+${list.length-max} no dia</button>`:''}</div>`;}
  const tot=xs.filter(x=>x.data&&x.data.startsWith(mesX)).length;
  $(alvo).innerHTML=`<div class="calnav"><span class="mes">${MES[m-1]} de ${y}</span><span class="note">${tot} peças neste mês</span></div><div class="cal">${cells}</div>`;
  $(alvo).querySelectorAll('.mais').forEach(b=>b.onclick=()=>{const iso=b.dataset.dia;const g=(porDia[iso]||[]).sort(ord);$('#dia').innerHTML=`<section class="semana"><header><h2>${fmt(iso)}</h2><span class="meta">${g.length} peças</span></header><div class="rows">${g.map(row).join('')}</div></section>`;$('#dia').scrollIntoView({block:'start'});});
}
// Aba Linha do tempo
function vGantt(){
  const xs=sel().filter(x=>x.data);
  if(!xs.length){$('#v').innerHTML='<p class="empty">Nada com data com os filtros atuais.</p>';return;}
  const linhas=[]; const vistos={};
  for(const k of Object.keys(B)){ const ts=[...new Set(xs.filter(x=>x.bloco===k).flatMap(x=>x.turmas))].sort(); for(const t of ts){ const key=k+'|'+t; if(!vistos[key]){vistos[key]=1;linhas.push({k,t});} } }
  const d0=toD('2026-10-01'), d1=toD('2027-08-01'); const dias=(d1-d0)/864e5;
  const L=300, W=Math.max(1180,Math.round(dias*5)), R=16, H=26, top=34, h=top+linhas.length*H+12;
  const X=iso=>L+((toD(iso)-d0)/864e5)/dias*(W-L-R);
  let svg=`<svg width="${W}" height="${h}" viewBox="0 0 ${W} ${h}" role="img" aria-label="Linha do tempo das peças por turma">`;
  for(let d=new Date(d0);d<=d1;d.setMonth(d.getMonth()+1)){const iso=isoD(d),x=X(iso);svg+=`<line class="grid" x1="${x}" y1="${top-8}" x2="${x}" y2="${h-6}"/><text class="ax" x="${x+4}" y="${top-14}">${MES[d.getMonth()].slice(0,3)} ${String(d.getFullYear()).slice(2)}</text>`;}
  let blocoAnt='';
  linhas.forEach((ln,i)=>{const y=top+i*H; if(ln.k!==blocoAnt){blocoAnt=ln.k; svg+=`<line class="grid" x1="0" y1="${y}" x2="${W}" y2="${y}"/>`;}
    const nm=(NOMES[ln.t]||'');svg+=`<text class="ax" x="8" y="${y+17}">${esc(CURTO[ln.k])}</text><text x="92" y="${y+17}"><tspan font-weight="600">${esc(ln.t)}</tspan> ${esc(nm.length>26?nm.slice(0,nm.lastIndexOf(' ',26))+' (...)':nm)}<title>${esc(ln.t+' '+nm)}</title></text>`;
    const meus=xs.filter(x=>x.bloco===ln.k&&x.turmas.includes(ln.t));
    for(const x of meus.filter(x=>x.data_fim&&CAT[x.tipo]==='midia')){const a=X(x.data),b=X(x.data_fim);svg+=`<rect class="mk k-${CAT[x.tipo]}" data-id="${esc(x.id)}" x="${a}" y="${y+9}" width="${Math.max(3,b-a)}" height="8" rx="3" style="fill:var(--k);opacity:.35"><title>${esc(TIPON[x.tipo]+' '+fmtc(x.data)+' a '+fmtc(x.data_fim)+': '+x.titulo)}</title></rect>`;}
    for(const x of meus){const cx=X(x.data); if(x.tipo==='inicio_turma'){svg+=`<path class="mk k-marco" data-id="${esc(x.id)}" d="M${cx} ${y+5} l7 8 l-7 8 l-7 -8 z" style="fill:var(--k)"><title>${esc('Início da turma '+fmt(x.data))}</title></path>`;} else if(!(x.data_fim&&CAT[x.tipo]==='midia')){svg+=`<circle class="mk k-${CAT[x.tipo]}" data-id="${esc(x.id)}" cx="${cx}" cy="${y+13}" r="4.5" style="fill:var(--k)${x.status==='executado'?'':';fill-opacity:.85'}"><title>${esc(fmtc(x.data)+' '+TIPON[x.tipo]+': '+x.titulo)}</title></circle>`;}}
  });
  const xh=X(HOJE); svg+=`<line class="hoje" x1="${xh}" y1="${top-8}" x2="${xh}" y2="${h-6}"/><text class="ax" x="${xh+4}" y="${h-8}">hoje</text></svg>`;
  $('#v').innerHTML=`<p class="note">Cada linha é uma turma. Pontos são peças (posts, mensagens, páginas, aprovações), faixas são fases de campanha paga e o losango é o início da turma. Passe o mouse para ver o nome e clique para abrir a peça.</p><div class="gantt">${svg}</div>`;
  const g=$('.gantt'); g.scrollLeft=Math.max(0,xh-L-60);
}
// Aba Lista
function vLista(){
  const xs=sel().sort(ord);
  $('#v').innerHTML=`<p class="note">${xs.length} peças com os filtros atuais. Clique numa linha para ler a peça.</p><div class="tbl"><table><thead><tr><th>Quando</th><th>Peça</th><th>Tipo</th><th>Canal</th><th>Bloco</th><th>Turmas</th><th>Situação</th></tr></thead><tbody>${xs.map(x=>`<tr data-id="${esc(x.id)}"><td class="d">${x.data?fmt(x.data)+(x.hora?' '+esc(x.hora):''):esc(x.quando||'sem data')}</td><td>${esc(x.titulo)}</td><td><span class="dot k-${CAT[x.tipo]}" style="background:var(--k)"></span>${esc(TIPON[x.tipo])}</td><td>${esc(x.canal)}</td><td>${esc(B[x.bloco])}</td><td>${esc(turmasTxt(x))}</td><td>${pills(x)}</td></tr>`).join('')}</tbody></table></div>`;
}
// Leitor: markdown simples com âncora por linha
function inl(t){t=esc(t);t=t.replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>').replace(/(^|[^\w*])\*([^*\n]+)\*(?![\w*])/g,'$1<em>$2</em>').replace(/\[(SUPOSIÇÃO|CONFIRMAR[^\]]*|T|DADO NÃO FORNECIDO|LINK)\]/g,'<span class="mk">[$1]</span>');return t;}
function md(lines,base){
  const out=[];let i=0;const L=lines;
  while(i<L.length){const l=L[i],ln=base+i;
    if(!l.trim()||/^---+\s*$/.test(l)){i++;continue;}
    let m=l.match(/^(#{1,6})\s+(.*)/); if(m){const n=Math.min(4,m[1].length);out.push(`<h${n} data-l="${ln}">${inl(m[2])}</h${n}>`);i++;continue;}
    if(l.trim().startsWith('|')){const st=i;const b=[];while(i<L.length&&L[i].trim().startsWith('|')){b.push(L[i]);i++;}
      const cel=r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim());const sep=b[1]&&/^\s*\|?\s*:?-{2,}/.test(b[1]);
      const head=sep?cel(b[0]):null;const body=(sep?b.slice(2):b);
      out.push(`<div class="tbl"><table>${head?'<thead><tr>'+head.map(c=>`<th>${inl(c)}</th>`).join('')+'</tr></thead>':''}<tbody>${body.map((r,j)=>`<tr data-l="${base+st+(sep?2:0)+j}">${cel(r).map(c=>`<td>${inl(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);continue;}
    if(l.startsWith('>')){const st=i;const b=[];while(i<L.length&&L[i].startsWith('>')){b.push(L[i].replace(/^>\s?/,''));i++;}out.push(`<blockquote data-l="${base+st}">${b.map(inl).join('<br>')}</blockquote>`);continue;}
    if(/^\s*([-*]|\d+\.)\s/.test(l)){const st=i;const b=[];while(i<L.length&&(/^\s*([-*]|\d+\.)\s/.test(L[i])||(/^\s{2,}\S/.test(L[i])))){b.push(L[i]);i++;}
      const ol=/^\s*\d+\./.test(b[0]);out.push(`<${ol?'ol':'ul'} data-l="${base+st}">${b.map((x,j)=>`<li data-l="${base+st+j}" style="margin-left:${Math.floor((x.length-x.trimStart().length)/2)*14}px">${inl(x.trim().replace(/^([-*]|\d+\.)\s/,''))}</li>`).join('')}</${ol?'ol':'ul'}>`);continue;}
    const st=i;const b=[l.trim()];i++;while(i<L.length&&L[i].trim()&&!/^(#|\||>|\s*([-*]|\d+\.)\s)/.test(L[i])){b.push(L[i].trim());i++;}out.push(`<p data-l="${base+st}">${inl(b.join(' '))}</p>`);}
  return out.join('');
}
function trecho(txt,linha){
  const L=txt.split('\n');let a=linha-1;const ini=L[a]||'';
  if(ini.trim().startsWith('|')){let h=a;while(h>0&&L[h-1].trim().startsWith('|'))h--;const head=L.slice(h,Math.min(h+2,a)).filter(x=>x.trim().startsWith('|'));const rows=[...head];if(h+2>a)return{lines:L.slice(h,a+1),base:h+1};return{lines:[...head,L[a]],base:a+1-head.length,tabela:true};}
  const nivel=(ini.match(/^(#+)\s/)||[])[1]; let b=a+1;
  while(b<L.length&&b-a<140){const m=L[b].match(/^(#+)\s/); if(m&&(!nivel||m[1].length<=nivel.length)) break; b++;}
  return{lines:L.slice(a,b),base:a+1};
}
function abrir(id,inteiro){
  const x=P.find(p=>p.id===id); if(!x) return;
  const txt=ARQ[x.arquivo]||''; const t=inteiro?{lines:txt.split('\n'),base:1}:trecho(txt,x.linha);
  $('#r-tit').textContent=x.titulo;
  $('#r-meta').innerHTML=`<div><dt>Quando</dt><dd>${x.data?fmt(x.data)+(x.data_fim?' a '+fmt(x.data_fim):'')+(x.hora?' às '+esc(x.hora):''):esc(x.quando||'sem data')}</dd></div><div><dt>Tipo e canal</dt><dd>${esc(TIPON[x.tipo])} · ${esc(x.canal)}</dd></div><div><dt>Bloco e turmas</dt><dd>${esc(B[x.bloco])} · ${esc(turmasTxt(x))}</dd></div><div><dt>Situação</dt><dd>${pills(x)}</dd></div>${x.trava&&x.trava.length?`<div><dt>Travas</dt><dd>${esc(x.trava.join(', '))}</dd></div>`:''}<div><dt>Arquivo</dt><dd><code>${esc(x.arquivo)}</code>, linha ${x.linha}</dd></div>`;
  $('#r-body').innerHTML=`<div class="acts"><button id="r-alt">${inteiro?'Ver só esta peça':'Ver o arquivo inteiro'}</button></div><div class="md">${md(t.lines,t.base)}</div>`;
  $('#r-alt').onclick=()=>abrir(id,!inteiro);
  $('#reader').hidden=false;$('#shade').hidden=false;
  if(inteiro){const el=[...document.querySelectorAll('#r-body [data-l]')].filter(e=>+e.dataset.l<=x.linha).pop();if(el){el.classList.add('hl');el.scrollIntoView({block:'center'});}}else{$('#r-body').scrollTop=0;}
  $('#r-close').focus();
}
function fechar(){$('#reader').hidden=true;$('#shade').hidden=true;}
// navegação
const VIEWS={agora:vAgora,calendario:vCal,'linha-do-tempo':vGantt,lista:vLista};
function rota(){const h=location.hash.slice(1);const v=VIEWS[h]?h:'agora';document.querySelectorAll('nav.tabs a').forEach(a=>a.setAttribute('aria-current',a.getAttribute('href')==='#'+v?'page':'false'));VIEWS[v]();}
document.addEventListener('click',e=>{const t=e.target.closest('[data-id]');if(t&&!t.closest('#reader')){abrir(t.dataset.id,false);}});
$('#r-close').onclick=fechar;$('#shade').onclick=fechar;document.addEventListener('keydown',e=>{if(e.key==='Escape')fechar();});
fill();
['bloco','cat','status'].forEach(k=>$('#f-'+k).addEventListener('input',e=>{F[k]=e.target.value;rota();}));
$('#f-q').addEventListener('input',e=>{F.q=e.target.value.trim();rota();});
window.addEventListener('hashchange',rota);
// resumo
const comData=P.filter(x=>x.data);
$('#k-total').textContent=P.length;
$('#k-ag').textContent=P.filter(x=>x.status==='aguardando_aprovacao').length;
$('#k-atr').textContent=P.filter(atrasada).length;
const seg0=segunda(HOJE);$('#k-sem').textContent=P.filter(x=>x.data&&x.data>=HOJE&&x.data<addD(seg0,7)).length;
$('#k-30').textContent=P.filter(x=>x.data&&x.data>=HOJE&&x.data<addD(HOJE,30)).length;
$('#k-trava').textContent=P.filter(x=>x.trava&&x.trava.length).length;
$('#k-hoje').textContent=fmt(HOJE);
rota();
"""

HTML = f"""<title>Entregáveis de marketing Ufape</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Instrument+Sans:wght@400;600&family=JetBrains+Mono:wght@500;600&display=swap">
<style>{CSS}</style>
<header class="top"><div class="wrap">
<div><span class="eyebrow">Painel de entregáveis · situação em <span id="k-hoje"></span></span>
<h1>Entregáveis de marketing Ufape</h1></div>
<p class="lede">Cada peça escrita pela squad, com a data em que sai, a turma, a situação e o texto pronto para ler. Tudo está em rascunho: nada foi publicado, enviado ou pago. Cobre tudo o que começa até abril de 2027.</p>
<div class="kpis">
<div class="kpi"><b id="k-total"></b><span>peças no painel</span></div>
<div class="kpi"><b id="k-ag"></b><span>aguardam a sua aprovação</span></div>
<div class="kpi"><b id="k-atr"></b><span>com data que já passou, ainda sem aprovação</span></div>
<div class="kpi"><b id="k-sem"></b><span>saem esta semana</span></div>
<div class="kpi"><b id="k-30"></b><span>saem nos próximos 30 dias</span></div>
<div class="kpi"><b id="k-trava"></b><span>dependem de uma resposta da Ufape (trava)</span></div>
</div>
</div></header>
<nav class="tabs" aria-label="Visões"><div class="wrap">
<a href="#agora">Agora</a><a href="#calendario">Calendário</a><a href="#linha-do-tempo">Linha do tempo</a><a href="#lista">Lista</a>
<div class="filters">
<input id="f-q" type="search" placeholder="Buscar peça ou turma" aria-label="Buscar">
<select id="f-bloco" aria-label="Bloco"></select><select id="f-cat" aria-label="Tipo"></select><select id="f-status" aria-label="Situação"></select>
</div></div></nav>
<main><div class="wrap">
<div class="legend"><span><i class="dot k-social" style="background:var(--k)"></i>Redes sociais e vídeo</span><span><i class="dot k-msg" style="background:var(--k)"></i>WhatsApp e e-mail</span><span><i class="dot k-midia" style="background:var(--k)"></i>Mídia paga</span><span><i class="dot k-site" style="background:var(--k)"></i>Página da turma</span><span><i class="dot k-marco" style="background:var(--k)"></i>Marcos, aprovações e conferências</span></div>
<section id="v" aria-live="polite"></section>
</div></main>
<footer><div class="wrap">
<p>As datas e os textos vêm dos arquivos aprovados pela revisão de qualidade (pasta saidas/). Cada peça mostra o arquivo e a linha de origem. "Trava" é uma resposta ou correção que só a Ufape faz e que segura a peça mesmo depois da aprovação. Não há dado pessoal de aluno ou candidato.</p>
</div></footer>
<div class="shade" id="shade" hidden></div>
<aside class="reader" id="reader" hidden aria-label="Leitor da peça">
<header><button class="close" id="r-close">Fechar</button><h2 id="r-tit"></h2><dl id="r-meta"></dl></header>
<div class="body" id="r-body"></div>
</aside>
<script>{JS.replace('__DATA__', DATA)}</script>
"""
os.makedirs(SAIDA, exist_ok=True)
open(SAIDA + 'painel-artifact.html', 'w', encoding='utf-8').write(HTML)
completo = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HTML.split('<header', 1)[0] + '</head>\n<body>\n<header' + HTML.split('<header', 1)[1] + '</body>\n</html>\n')
open(COPIA, 'w', encoding='utf-8').write(completo)
print('peças', len(pecas), 'arquivos', len(textos), 'tamanho', len(completo))
