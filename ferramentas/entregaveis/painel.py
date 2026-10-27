"""Painel de entregáveis, versão 2: semana, mês, por curso e mídia, com a peça aberta como ela vai ao ar.

Rodar da raiz do repositório:
    python3 -I ferramentas/entregaveis/painel.py
Lê ferramentas/entregaveis/dados/*.json (esquema em ferramentas/entregaveis/ESQUEMA.md, versões 1 e 2),
explica as travas com as pendências e aprovações do mapa por curso e grava:
  ferramentas/entregaveis/saida/painel-artifact.html (para publicar como página)
  saidas/10-operacoes-de-marketing/painel-de-entregaveis-2026-10-27.html (cópia com doctype)
"""
import glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extrair import trecho

HOJE = '2026-10-27'
DADOS = 'ferramentas/entregaveis/dados/'
SAIDA = 'ferramentas/entregaveis/saida/'
COPIA = 'saidas/10-operacoes-de-marketing/painel-de-entregaveis-2026-10-27.html'
MAPA = 'ferramentas/mapa-mental/saida/mapa-dados.json'
BLOCOS = {
    'pos-onda1': 'Pós-graduação: turmas de outubro e novembro de 2026',
    'workshop': 'Workshop Brasileiro de Neuromonitorização',
    'pos-marco': 'Pós-graduação: turmas de março de 2027',
    'pos-abril': 'Pós-graduação: turmas de abril de 2027',
    'graduacao': 'Graduação 2027.1',
}
TIPOS = {'post', 'carrossel', 'reels', 'story', 'card_docente', 'video', 'whatsapp', 'email', 'pagina', 'anuncio',
         'campanha_subida', 'campanha_fase', 'campanha_pausa', 'conferencia', 'aprovacao', 'relatorio', 'inicio_turma', 'outro'}
PUBLICAS = {'post', 'carrossel', 'reels', 'story', 'card_docente', 'video', 'whatsapp', 'email', 'pagina', 'anuncio'}
STATUS = {'aguardando_aprovacao', 'em_correcao', 'a_fazer', 'suspenso', 'executado'}
ID_MAPA = {'medicina-veterinaria': 'graduacao-medicina-veterinaria', 'pedagogia': 'graduacao-pedagogia',
           'workshop': 'eventos-workshop-neuromonitorizacao-2026-11-20'}
CODIGO = re.compile(r'^\s*(?:[A-Z]{1,4}\d*[A-Z]?-?[A-Z]?\d*(?:-\d+)?[a-z]?|\d{3,5}-[A-Z]\d+)(?:\s*\([^)]*\))?\s*:\s*')

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

textos = {}
for x in pecas:
    a = x.get('arquivo')
    if a and a not in textos:
        if os.path.exists(a):
            textos[a] = open(a, encoding='utf-8').read()
        else:
            erros.append('arquivo não encontrado: ' + a)
if erros:
    raise SystemExit('Dados com problema:\n' + '\n'.join(erros[:40]))

# Trecho da peça no arquivo (notas de produção) e título sem código interno
for x in pecas:
    tipo_t, linhas = trecho(textos[x['arquivo']], x['linha'])
    x['_trecho'] = '\n'.join(linhas)
    x['_base'] = x['linha'] if tipo_t == 'bloco' else max(1, x['linha'] - len(linhas) + 1)
    t = x.get('titulo_limpo') or CODIGO.sub('', x['titulo'], count=1)
    x['_titulo'] = t.strip() or x['titulo']
    x['_publica'] = x['tipo'] in PUBLICAS

# Nomes de curso e explicação das travas, do mapa por curso
mapa = json.load(open(MAPA, encoding='utf-8'))
NOMES, EXPL, EXPL_GERAL = {}, {}, {}
def curto(t, n=240):
    t = re.sub(r'\s+', ' ', t or '').strip()
    if len(t) <= n: return t
    c = t[:n]; k = max(c.rfind('. '), c.rfind('; '))
    return (c[:k + 1] if k > 80 else c[:c.rfind(' ')]) + ' (resumo; texto completo no plano)'
for j in mapa:
    chave = j['codigo'] if j['codigo'] != 'sem-codigo' else next((k for k, v in ID_MAPA.items() if v == j['id']), j['id'])
    n = j.get('nome_padrao') or ''
    if not n or n.startswith('[CONFIRMAR'): n = j.get('nome_no_site') or ''
    NOMES[chave] = n
    d = {}
    for pe in j.get('pendencias', []):
        if pe.get('ref_plano'): d.setdefault(pe['ref_plano'], curto(pe.get('descricao')))
    for ap in j.get('aprovacoes', []):
        if ap.get('ref'): d.setdefault(ap['ref'], curto(ap.get('o_que')))
    EXPL[chave] = d
    for k, v in d.items(): EXPL_GERAL.setdefault(k, v)
NOMES['medicina-veterinaria'] = 'Graduação em Medicina Veterinária'
NOMES['pedagogia'] = 'Graduação em Pedagogia'
NOMES['workshop'] = 'Workshop Brasileiro de Neuromonitorização'
for x in pecas:
    ex = []
    for c in x.get('trava') or []:
        txt = next((EXPL.get(t, {}).get(c) for t in x['turmas'] if EXPL.get(t, {}).get(c)), None) or EXPL_GERAL.get(c)
        ex.append([c, txt])
    x['_travas'] = ex

saida = []
for x in pecas:
    saida.append({k: x.get(k) for k in ('id', 'bloco', 'turmas', 'tipo', 'canal', 'data', 'data_fim', 'hora', 'quando', 'status', 'arquivo', 'linha', 'conteudo')}
                 | {'t': x['_titulo'], 'pub': x['_publica'], 'tr': x['_travas'], 'nt': x['_trecho'], 'nb': x['_base']})
for t in list(textos.values()) + [json.dumps(saida, ensure_ascii=False)]:
    assert '—' not in t and '–' not in t, 'travessão ou meia-risca nos dados ou nos arquivos'
DATA = json.dumps({'hoje': HOJE, 'blocos': BLOCOS, 'nomes': NOMES, 'pecas': saida, 'arquivos': textos},
                  ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

CSS = r"""
:root{
  /* Layout: largura total; cabeçalho com o resumo, abas Semana, Mês, Por curso e Mídia; a peça abre numa janela grande, como vai ao ar */
  --bg:#eef1ee; --surface:#ffffff; --ink:#16211d; --muted:#56645f; --line:#d3dbd6; --soft:#e5ebe7;
  --accent:#1f6b58; --accent-soft:#d6e9e1; --accent-ink:#ffffff;
  --c-social:#c4532c; --c-msg:#2a5fb8; --c-midia:#7a49b0; --c-site:#1f6b58; --c-marco:#8a6a14;
  --s-ag:#9a6200; --s-ag-bg:#fbefd6; --s-cor:#b3261e; --s-cor-bg:#fbe3e0; --s-faz:#5f6d68; --s-faz-bg:#e8ecea; --s-ok:#2e7d32;
  --wa-bg:#e7ddd3; --wa-bub:#ffffff; --wa-me:#d9fdd3;
  --f-display:"Bricolage Grotesque","Segoe UI Semibold",system-ui,sans-serif;
  --f-body:"Instrument Sans","Segoe UI",system-ui,sans-serif;
  --f-data:"JetBrains Mono",ui-monospace,Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#0e1412; --surface:#161f1c; --ink:#e4ece8; --muted:#9caba5; --line:#2a3833; --soft:#1d2925;
  --accent:#5cc2a6; --accent-soft:#1b3a31; --accent-ink:#0e1412;
  --c-social:#f28a62; --c-msg:#80a8f2; --c-midia:#b896e8; --c-site:#5cc2a6; --c-marco:#dcbc5a;
  --s-ag:#f0bd57; --s-ag-bg:#3a2e12; --s-cor:#ff8a80; --s-cor-bg:#3c1f1c; --s-faz:#a3b1ab; --s-faz-bg:#25312d; --s-ok:#81c784;
  --wa-bg:#0b141a; --wa-bub:#1f2c33; --wa-me:#005c4b; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#0e1412; --surface:#161f1c; --ink:#e4ece8; --muted:#9caba5; --line:#2a3833; --soft:#1d2925;
  --accent:#5cc2a6; --accent-soft:#1b3a31; --accent-ink:#0e1412;
  --c-social:#f28a62; --c-msg:#80a8f2; --c-midia:#b896e8; --c-site:#5cc2a6; --c-marco:#dcbc5a;
  --s-ag:#f0bd57; --s-ag-bg:#3a2e12; --s-cor:#ff8a80; --s-cor-bg:#3c1f1c; --s-faz:#a3b1ab; --s-faz-bg:#25312d; --s-ok:#81c784;
  --wa-bg:#0b141a; --wa-bub:#1f2c33; --wa-me:#005c4b; color-scheme:dark}
*{box-sizing:border-box}
[hidden]{display:none!important}
html,body{background:var(--bg)}
body{color:var(--ink);font:15px/1.5 var(--f-body);margin:0}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);z-index:30;background:var(--surface)}
.g{padding-left:max(24px,env(safe-area-inset-left,0px));padding-right:max(24px,env(safe-area-inset-right,0px))}
@media (max-width:600px){.g{padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
button{font:inherit;color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
header.top{background:var(--surface);border-bottom:1px solid var(--line)}
header.top .g{padding-block:22px 18px;display:grid;gap:16px;grid-template-columns:minmax(0,1.1fr) minmax(0,1.4fr);align-items:end}
@media (max-width:1000px){header.top .g{grid-template-columns:minmax(0,1fr)}}
.eyebrow{font:600 12px/1 var(--f-data);letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}
h1{font:700 clamp(26px,3vw,36px)/1.08 var(--f-display);margin:6px 0 8px;letter-spacing:-.01em;text-wrap:balance}
.lede{color:var(--muted);margin:0;max-width:62ch;font-size:15.5px}
.kpis{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px}
@media (max-width:700px){.kpis{grid-template-columns:repeat(2,minmax(0,1fr))}}
.kpi{border:1px solid var(--line);border-radius:12px;padding:12px 14px;display:grid;gap:4px;background:var(--bg);text-align:left;cursor:pointer}
.kpi:hover{border-color:var(--accent)}
.kpi b{font:700 28px/1 var(--f-display);font-variant-numeric:tabular-nums}
.kpi span{font-size:13.5px;color:var(--muted);line-height:1.3}
nav.tabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--surface);border-bottom:1px solid var(--line)}
@media (max-width:760px){nav.tabs{position:static}}
nav.tabs .g{display:flex;gap:6px 14px;flex-wrap:wrap;padding-block:10px;align-items:center}
.tablist{display:flex;gap:4px;flex-wrap:wrap}
.tablist a{font-weight:600;text-decoration:none;color:var(--muted);padding:8px 14px;border-radius:999px;font-size:15px}
.tablist a[aria-current="page"]{background:var(--ink);color:var(--surface)}
.tablist a:hover{color:var(--ink)}
.tablist a[aria-current="page"]:hover{color:var(--surface)}
.filters{display:flex;gap:8px;flex-wrap:wrap;margin-left:auto;align-items:center;min-width:0;max-width:100%}
@media (max-width:760px){.filters{margin-left:0;width:100%}.filters select,.filters input{flex:1 1 100%}}
.filters select,.filters input{font:inherit;font-size:14px;color:var(--ink);background:var(--bg);border:1px solid var(--line);border-radius:999px;padding:7px 12px;min-width:0;max-width:100%}
.filters label{display:flex;gap:6px;align-items:center;font-size:14px;color:var(--ink)}
main .g{padding-block:20px 64px;display:grid;gap:18px}
#v{min-width:0;display:grid;gap:18px}
.legend{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:13.5px;color:var(--muted)}
.sw{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:6px;vertical-align:-1px;background:var(--k)}
.k-social{--k:var(--c-social)} .k-msg{--k:var(--c-msg)} .k-midia{--k:var(--c-midia)} .k-site{--k:var(--c-site)} .k-marco{--k:var(--c-marco)}
h2{font:700 22px/1.15 var(--f-display);margin:0;text-wrap:balance}
.note{font-size:14px;color:var(--muted);margin:0;max-width:90ch}
.bar{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar .nav{display:flex;gap:6px}
.btn{font-weight:600;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 14px;cursor:pointer;font-size:14px}
.btn:hover{border-color:var(--ink)}
.btn.pri{background:var(--ink);color:var(--surface);border-color:var(--ink)}
/* Semana */
.week{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:10px;align-items:start}
@media (max-width:1100px){.week{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media (max-width:760px){.week{grid-template-columns:minmax(0,1fr)}}
.col{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:10px;display:grid;gap:8px;align-content:start;min-height:160px;min-width:0}
.col.hoje{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.col.vazio{background:transparent;border-style:dashed}
.col>header{display:flex;justify-content:space-between;align-items:baseline;gap:6px;padding:2px 4px 4px;border-bottom:1px solid var(--line)}
.col>header b{font:700 15px/1.2 var(--f-display)}
.col>header span{font:600 12px var(--f-data);color:var(--muted)}
.col .tag-hoje{font:700 11px var(--f-data);color:var(--accent);text-transform:uppercase;letter-spacing:.06em}
.card{display:grid;gap:5px;text-align:left;background:var(--bg);border:1px solid var(--line);border-top:4px solid var(--k);border-radius:10px;padding:9px 10px;cursor:pointer;min-width:0;width:100%}
.card:hover{border-color:var(--k);background:var(--surface)}
.card .ch{font:600 11.5px/1.2 var(--f-data);color:var(--k);text-transform:uppercase;letter-spacing:.04em}
.card .cur{font-size:12.5px;color:var(--muted);line-height:1.3;overflow-wrap:anywhere}
.card .tt{font-weight:600;font-size:14px;line-height:1.3;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;overflow-wrap:anywhere}
.card .st{display:flex;gap:5px;flex-wrap:wrap}
.pill{font:600 11.5px/1 var(--f-body);padding:4px 8px;border-radius:999px;white-space:nowrap}
.p-aguardando_aprovacao{color:var(--s-ag);background:var(--s-ag-bg)} .p-em_correcao{color:var(--s-cor);background:var(--s-cor-bg)}
.p-a_fazer,.p-suspenso{color:var(--s-faz);background:var(--s-faz-bg)} .p-executado{color:var(--s-ok);background:var(--s-faz-bg)}
.p-trava{color:var(--s-cor);background:transparent;border:1px dashed var(--s-cor)}
.ops{background:var(--surface);border:1px solid var(--line);border-radius:14px}
.ops>summary{cursor:pointer;padding:12px 16px;font-weight:600;list-style:none;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.ops>summary::-webkit-details-marker{display:none}
.ops>summary::before{content:"+";font:700 16px var(--f-data);color:var(--muted);width:14px}
.ops[open]>summary::before{content:"-"}
.ops .meta{color:var(--muted);font-weight:400;font-size:14px}
.oplist{display:grid;gap:4px;padding:0 12px 12px}
.op{display:grid;grid-template-columns:110px 1fr auto;gap:4px 12px;align-items:center;text-align:left;background:none;border:0;border-radius:8px;padding:7px 8px;cursor:pointer;width:100%}
.op:hover{background:var(--soft)}
.op .d{font:600 12.5px var(--f-data);color:var(--muted);font-variant-numeric:tabular-nums}
.op .x{min-width:0;overflow-wrap:anywhere}
.op .x small{display:block;color:var(--muted);font-size:12.5px}
@media (max-width:600px){.op{grid-template-columns:1fr}}
/* Mês */
.month{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}
.month .wd{font:600 12px/1 var(--f-data);color:var(--muted);text-transform:uppercase;letter-spacing:.06em;padding:4px 6px}
.day{background:var(--surface);border:1px solid var(--line);border-radius:10px;min-height:120px;padding:7px;display:grid;align-content:start;gap:4px;min-width:0;text-align:left;cursor:pointer}
.day:hover{border-color:var(--ink)}
.day.fora{background:transparent;border-style:dashed;opacity:.5;cursor:default}
.day.hoje{border-color:var(--accent);box-shadow:inset 0 0 0 1px var(--accent)}
.day .n{font:700 14px/1 var(--f-display);display:flex;justify-content:space-between;align-items:baseline}
.day .n small{font:600 11.5px var(--f-data);color:var(--muted)}
.day .ln{font-size:12.5px;line-height:1.25;border-left:3px solid var(--k);padding-left:6px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.day .mais{font-size:12px;color:var(--accent);font-weight:600}
@media (max-width:760px){.month .wd{font-size:10px;padding:2px}.day{min-height:56px;padding:4px}.day .ln{font-size:0;height:6px;border-left:0;background:var(--k);border-radius:2px;padding:0}.day .mais{display:none}}
/* Por curso */
.curso{display:grid;grid-template-columns:320px minmax(0,1fr);gap:18px;align-items:start}
@media (max-width:900px){.curso{grid-template-columns:minmax(0,1fr)}}
.clist{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:8px;display:grid;gap:2px;position:sticky;top:76px;max-height:calc(100vh - 96px);overflow:auto}
@media (max-width:900px){.clist{position:static;max-height:none}}
.clist h3{font:600 12px var(--f-data);text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:10px 8px 4px}
.clist button{display:flex;justify-content:space-between;gap:8px;text-align:left;background:none;border:0;border-radius:8px;padding:7px 8px;cursor:pointer;font-size:14px}
.clist button:hover{background:var(--soft)}
.clist button[aria-pressed="true"]{background:var(--ink);color:var(--surface)}
.clist button span:last-child{font:600 12px var(--f-data);opacity:.75}
.feed{display:grid;gap:12px;min-width:0}
.feed .mes{font:700 16px var(--f-display);margin-top:8px;color:var(--muted)}
.item{display:grid;grid-template-columns:86px minmax(0,1fr) auto;gap:14px;align-items:start;background:var(--surface);border:1px solid var(--line);border-left:5px solid var(--k);border-radius:12px;padding:12px 14px;cursor:pointer;text-align:left;width:100%}
.item:hover{border-color:var(--k)}
.item .d{font:700 15px/1.15 var(--f-display);font-variant-numeric:tabular-nums}
.item .d small{display:block;font:600 11.5px var(--f-data);color:var(--muted);text-transform:uppercase}
.item .x{min-width:0;display:grid;gap:3px}
.item .ch{font:600 11.5px var(--f-data);color:var(--k);text-transform:uppercase;letter-spacing:.04em}
.item .tt{font-weight:600;font-size:15px;line-height:1.3;overflow-wrap:anywhere}
.item .pv{color:var(--muted);font-size:14px;line-height:1.4;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.item .st{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end}
@media (max-width:640px){.item{grid-template-columns:64px minmax(0,1fr)}.item .st{grid-column:2;justify-content:flex-start}}
/* Mídia */
.gantt{max-width:100%;overflow-x:auto;border:1px solid var(--line);border-radius:14px;background:var(--surface)}
.gantt svg{display:block}
.gantt text{fill:var(--ink);font:12.5px var(--f-body)}
.gantt .ax{fill:var(--muted);font:11px var(--f-data)}
.gantt .grid{stroke:var(--line)}
.gantt .hoje{stroke:var(--accent);stroke-width:2}
.gantt .mk{cursor:pointer}
/* Janela da peça */
.modal{position:fixed;inset:0;z-index:50;display:grid;place-items:center;padding:max(16px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(16px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));background:rgba(10,16,14,.55)}
.sheet{background:var(--surface);border-radius:18px;width:min(1240px,100%);max-height:100%;display:grid;grid-template-rows:auto minmax(0,1fr);overflow:hidden;box-shadow:0 24px 64px rgba(0,0,0,.3)}
.sheet>header{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:14px 18px;border-bottom:1px solid var(--line);flex-wrap:wrap}
.sheet>header .nav{display:flex;gap:6px}
.sheet .crumb{font:600 12px var(--f-data);text-transform:uppercase;letter-spacing:.06em;color:var(--k)}
.sheet .in{overflow:auto;display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:0}
@media (max-width:900px){.sheet .in{grid-template-columns:minmax(0,1fr)}}
.stage{padding:24px;display:grid;gap:16px;align-content:start;background:var(--bg);min-width:0}
.stage h2{font-size:24px}
.side{padding:20px;border-left:1px solid var(--line);display:grid;gap:14px;align-content:start;min-width:0}
@media (max-width:900px){.side{border-left:0;border-top:1px solid var(--line)}}
.side dl{margin:0;display:grid;gap:10px}
.side dt{font:600 11.5px var(--f-data);text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.side dd{margin:2px 0 0;overflow-wrap:anywhere}
.side .trv{display:grid;gap:8px}
.side .trv div{border:1px dashed var(--s-cor);border-radius:10px;padding:8px 10px;font-size:13.5px}
.side .trv b{color:var(--s-cor);font-family:var(--f-data);font-size:12px}
.side details{border-top:1px solid var(--line);padding-top:10px}
.side summary{cursor:pointer;font-weight:600}
/* Mockups */
.mock{background:var(--surface);border:1px solid var(--line);border-radius:16px;overflow:hidden;max-width:960px;width:100%}
.mock .hd{display:flex;gap:10px;align-items:center;padding:10px 14px;border-bottom:1px solid var(--line)}
.av{width:32px;height:32px;border-radius:50%;background:var(--accent);color:var(--accent-ink);display:grid;place-items:center;font:700 12px var(--f-display)}
.mock .hd b{font-size:14px} .mock .hd small{display:block;color:var(--muted);font-size:12px}
.slides{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(220px,1fr);gap:10px;overflow-x:auto;padding:12px;background:var(--soft)}
.slide{aspect-ratio:4/5;max-width:100%;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px;display:grid;align-content:space-between;gap:8px}
.slide.v{aspect-ratio:9/16}
.slide .num{font:600 11px var(--f-data);color:var(--muted)}
.slide p{margin:0;font:600 17px/1.3 var(--f-display);text-wrap:balance;overflow-wrap:anywhere}
.slide .sub{display:block;font-size:13px;color:var(--muted);line-height:1.35}
.slide{align-content:start}.slide .num{margin-bottom:auto}
.cap{padding:14px 16px;display:grid;gap:8px;font-size:15px}
.cap p{margin:0;max-width:70ch}
.cap .lead{font-weight:700}
.wa{background:var(--wa-bg);padding:18px;display:grid;gap:8px;justify-items:start}
.bub{background:var(--wa-bub);border-radius:4px 14px 14px 14px;padding:10px 12px;max-width:min(520px,100%);display:grid;gap:6px;box-shadow:0 1px 1px rgba(0,0,0,.12);font-size:15px}
.bub p{margin:0;overflow-wrap:anywhere}
.bub .lead{font-weight:700}
.bub .tm{justify-self:end;font:11px var(--f-data);color:var(--muted)}
.lk{color:var(--c-msg);text-decoration:underline;font-weight:600}
.mail .meta{padding:12px 16px;border-bottom:1px solid var(--line);display:grid;gap:4px;font-size:14px}
.mail .meta b{font-size:17px;font-family:var(--f-display)}
.mail .meta span{color:var(--muted)}
.mail .body{padding:16px 18px;display:grid;gap:10px;font-size:15px}
.mail .body p{margin:0;max-width:66ch}
.cta{justify-self:start;background:var(--accent);color:var(--accent-ink);font-weight:700;border-radius:8px;padding:10px 16px}
.brw .url{padding:8px 14px;background:var(--soft);font:12.5px var(--f-data);color:var(--muted);border-bottom:1px solid var(--line)}
.brw .body{padding:20px;display:grid;gap:10px}
.brw .body h3{font:700 22px/1.2 var(--f-display);margin:0}
.brw .body p{margin:0;max-width:70ch}
.ad .tag{font:600 11.5px var(--f-data);color:var(--muted)}
.scenes{display:grid;gap:8px;padding:14px 16px;counter-reset:c}
.scenes li{list-style:none;display:grid;grid-template-columns:28px 1fr;gap:8px}
.scenes li::before{counter-increment:c;content:counter(c);font:700 13px var(--f-data);color:var(--surface);background:var(--k);border-radius:6px;display:grid;place-items:center;height:24px}
.var{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:10px 14px;display:grid;gap:6px;max-width:760px;font-size:14px}
.var b{font:600 12px var(--f-data);text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.mk2{font:600 12px var(--f-data);color:var(--s-ag);background:var(--s-ag-bg);border-radius:4px;padding:0 4px}
.empty{color:var(--muted);padding:18px;background:var(--surface);border:1px dashed var(--line);border-radius:12px}
.md{font-size:14px;display:grid;gap:8px;min-width:0}
.md h1,.md h2,.md h3,.md h4{font-family:var(--f-display);margin:8px 0 0;font-size:15px}
.md p{margin:0} .md ul,.md ol{margin:0;padding-left:20px;display:grid;gap:3px}
.md blockquote{margin:0;padding:6px 10px;border-left:3px solid var(--accent);background:var(--soft);border-radius:0 6px 6px 0}
.md code{font:12px var(--f-data);background:var(--soft);padding:1px 4px;border-radius:4px;overflow-wrap:anywhere}
.md .tbl{overflow-x:auto} .md table{border-collapse:collapse;font-size:12.5px} .md th,.md td{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left;vertical-align:top}
.md .hl{background:var(--accent-soft)}
.full{max-height:60vh;overflow:auto;border:1px solid var(--line);border-radius:10px;padding:12px;background:var(--bg)}
footer .g{padding-block:0 32px;color:var(--muted);font-size:13px}
"""

JS = r"""
const DADOS=__DATA__;
const HOJE=DADOS.hoje,B=DADOS.blocos,P=DADOS.pecas,ARQ=DADOS.arquivos,NOMES=DADOS.nomes;
const CAT={post:'social',carrossel:'social',reels:'social',story:'social',card_docente:'social',video:'social',whatsapp:'msg',email:'msg',pagina:'site',anuncio:'midia',campanha_subida:'midia',campanha_fase:'midia',campanha_pausa:'midia',conferencia:'marco',aprovacao:'marco',relatorio:'marco',inicio_turma:'marco',outro:'marco'};
const CATN={social:'Redes sociais e vídeo',msg:'WhatsApp e e-mail',site:'Página da turma',midia:'Anúncios e campanhas pagas',marco:'Aprovações, conferências e marcos'};
const TIPON={post:'Post',carrossel:'Carrossel',reels:'Reels',story:'Stories',card_docente:'Cards de docentes',video:'Vídeo',whatsapp:'WhatsApp',email:'E-mail',pagina:'Página da turma',anuncio:'Anúncio',campanha_subida:'Campanha entra no ar',campanha_fase:'Fase da campanha',campanha_pausa:'Campanha pausa',conferencia:'Conferência',aprovacao:'Aprovação',relatorio:'Relatório',inicio_turma:'Início das aulas',outro:'Marco'};
const CANAL={instagram:'Instagram',facebook:'Facebook',tiktok:'TikTok',youtube:'YouTube',linkedin:'LinkedIn',x:'X',whatsapp:'WhatsApp',email:'E-mail',site:'Site',meta_ads:'Meta (Instagram e Facebook)',google_ads:'Google',crm:'CRM',interno:'Equipe'};
const STN={aguardando_aprovacao:'Pronta para aprovar',em_correcao:'Em ajuste',a_fazer:'A produzir',suspenso:'Em espera',executado:'Feita'};
const STD={aguardando_aprovacao:'Escrita e aprovada pela revisão de qualidade. Falta a sua aprovação para sair.',em_correcao:'Voltou da revisão de qualidade com ajustes a fazer.',a_fazer:'Ainda não foi escrita ou ainda vai acontecer.',suspenso:'Parada até uma resposta da Ufape.',executado:'Já foi feita.'};
const MES=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'];
const WD=['Segunda','Terça','Quarta','Quinta','Sexta','Sábado','Domingo'];
const $=s=>document.querySelector(s);
const esc=s=>String(s??'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const toD=iso=>new Date(iso+'T12:00:00');
const isoD=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const addD=(iso,n)=>{const d=toD(iso);d.setDate(d.getDate()+n);return isoD(d);};
const segunda=iso=>{const d=toD(iso);d.setDate(d.getDate()-((d.getDay()+6)%7));return isoD(d);};
const dm=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7):'-';
const dma=iso=>iso?iso.slice(8,10)+'/'+iso.slice(5,7)+'/'+iso.slice(0,4):'-';
const wdn=iso=>WD[(toD(iso).getDay()+6)%7];
const curso=x=>x.turmas.length>1?(x.turmas.length+' turmas'):(NOMES[x.turmas[0]]||x.turmas[0]);
const cursoCurto=t=>(NOMES[t]||t).replace(/^Pós-graduação em /,'').replace(/^Graduação em /,'');
const canal=x=>CANAL[x.canal]||x.canal;
const rotulo=x=>{const c=canal(x),t=TIPON[x.tipo];return (c===t||(x.tipo==='pagina'&&x.canal==='site'))?t:c+' · '+t;};
const quando=x=>x.data?dma(x.data)+(x.data_fim&&x.data_fim!==x.data?' a '+dma(x.data_fim):'')+(x.hora?', '+x.hora:''):(x.quando||'Sem data fixa');
// filtros
const F={bloco:'',cat:'',trava:false,q:''};
function pass(x){
  if(F.bloco&&x.bloco!==F.bloco) return false;
  if(F.cat&&CAT[x.tipo]!==F.cat) return false;
  if(F.trava&&!(x.tr&&x.tr.length)) return false;
  if(F.q){const q=F.q.toLowerCase();const h=(x.t+' '+x.turmas.map(t=>t+' '+(NOMES[t]||'')).join(' ')+' '+TIPON[x.tipo]+' '+canal(x)).toLowerCase();if(!h.includes(q)) return false;}
  return true;}
const ord=(a,b)=>(a.data||'9999').localeCompare(b.data||'9999')||(a.hora||'').localeCompare(b.hora||'')||a.bloco.localeCompare(b.bloco)||a.t.localeCompare(b.t);
const pubs=()=>P.filter(x=>x.pub&&pass(x)).sort(ord);
const ops=()=>P.filter(x=>!x.pub&&pass(x)).sort(ord);
function pills(x){return `<span class="pill p-${x.status}">${esc(STN[x.status])}</span>`+(x.tr&&x.tr.length?'<span class="pill p-trava">Depende da Ufape</span>':'');}
function card(x){return `<button class="card k-${CAT[x.tipo]}" data-id="${esc(x.id)}"><span class="ch">${esc(rotulo(x))}${x.hora?' · '+esc(x.hora):''}</span><span class="tt">${esc(x.t)}</span><span class="cur">${esc(x.turmas.map(cursoCurto).join(', '))}</span><span class="st">${pills(x)}</span></button>`;}
function opRow(x){return `<button class="op" data-id="${esc(x.id)}"><span class="d">${esc(x.data?wdn(x.data).slice(0,3)+' '+dm(x.data):(x.quando||'sem data'))}</span><span class="x">${esc(x.t)}<small>${esc(TIPON[x.tipo])} · ${esc(x.turmas.map(cursoCurto).join(', '))}</small></span><span>${pills(x)}</span></button>`;}
// Semana
let semana=segunda(HOJE);
function vSemana(){
  const fim=addD(semana,6), xs=pubs().filter(x=>x.data&&x.data>=semana&&x.data<=fim), os=ops().filter(x=>x.data&&x.data>=semana&&x.data<=fim);
  let cols='';
  for(let i=0;i<7;i++){const d=addD(semana,i), g=xs.filter(x=>x.data===d);
    cols+=`<section class="col${d===HOJE?' hoje':''}${g.length?'':' vazio'}" aria-label="${wdn(d)} ${dm(d)}"><header><b>${wdn(d)} ${dm(d)}</b>${d===HOJE?'<span class="tag-hoje">hoje</span>':`<span>${g.length||''}</span>`}</header>${g.map(card).join('')||'<span class="note">Nenhuma peça.</span>'}</section>`;}
  const rot=`${dm(semana)} a ${dma(fim)}`;
  $('#v').innerHTML=`<div class="bar"><h2>Semana de ${rot}</h2><div class="nav"><button class="btn" id="s-prev">‹ Anterior</button><button class="btn${semana===segunda(HOJE)?' pri':''}" id="s-hoje">Esta semana</button><button class="btn" id="s-next">Próxima ›</button></div><span class="note">${xs.length} peças vão ao público nesta semana.</span></div>
  <div class="week">${cols}</div>
  <details class="ops"${os.length&&!xs.length?' open':''}><summary>Bastidores da semana <span class="meta">${os.length} itens: campanhas pagas, aprovações, conferências e relatórios</span></summary><div class="oplist">${os.map(opRow).join('')||'<p class="note">Nada nesta semana.</p>'}</div></details>`;
  $('#s-prev').onclick=()=>{semana=addD(semana,-7);vSemana();};
  $('#s-next').onclick=()=>{semana=addD(semana,7);vSemana();};
  $('#s-hoje').onclick=()=>{semana=segunda(HOJE);vSemana();};
}
// Mês
let mes=HOJE.slice(0,7);
function vMes(){
  const [y,m]=mes.split('-').map(Number), first=new Date(y,m-1,1,12), ini=new Date(first); ini.setDate(1-((first.getDay()+6)%7));
  const xs=pubs().filter(x=>x.data&&x.data.startsWith(mes)); const porDia={}; xs.forEach(x=>(porDia[x.data]=porDia[x.data]||[]).push(x));
  let cells=WD.map(w=>`<div class="wd">${w.slice(0,3)}</div>`).join('');
  for(let i=0;i<42;i++){const d=new Date(ini);d.setDate(ini.getDate()+i);const iso=isoD(d),fora=d.getMonth()!==m-1;
    if(i%7===0&&i>=28&&fora) break;
    const g=fora?[]:(porDia[iso]||[]);
    cells+=fora?`<div class="day fora"><span class="n">${d.getDate()}</span></div>`:`<button class="day${iso===HOJE?' hoje':''}" data-sem="${segunda(iso)}"><span class="n">${d.getDate()}${g.length?`<small>${g.length}</small>`:''}</span>${g.slice(0,4).map(x=>`<span class="ln k-${CAT[x.tipo]}">${esc(TIPON[x.tipo])}: ${esc(x.turmas.map(cursoCurto).join(', '))}</span>`).join('')}${g.length>4?`<span class="mais">+${g.length-4} peças</span>`:''}</button>`;}
  $('#v').innerHTML=`<div class="bar"><h2>${MES[m-1][0].toUpperCase()+MES[m-1].slice(1)} de ${y}</h2><div class="nav"><button class="btn" id="m-prev">‹ Anterior</button><button class="btn${mes===HOJE.slice(0,7)?' pri':''}" id="m-hoje">Este mês</button><button class="btn" id="m-next">Próximo ›</button></div><span class="note">${xs.length} peças neste mês. Clique num dia para ver a semana com as peças.</span></div><div class="month">${cells}</div>`;
  $('#m-prev').onclick=()=>{mes=isoD(new Date(y,m-2,1,12)).slice(0,7);vMes();};
  $('#m-next').onclick=()=>{mes=isoD(new Date(y,m,1,12)).slice(0,7);vMes();};
  $('#m-hoje').onclick=()=>{mes=HOJE.slice(0,7);vMes();};
  document.querySelectorAll('.day[data-sem]').forEach(b=>b.onclick=()=>{semana=b.dataset.sem;location.hash='semana';});
}
// Por curso
let cursoSel=null;
function vCurso(){
  const todos=P.filter(x=>x.pub&&pass(x));
  const grupos={}; for(const x of todos) for(const t of x.turmas){const k=x.bloco;(grupos[k]=grupos[k]||{});(grupos[k][t]=grupos[k][t]||0);grupos[k][t]++;}
  const chaves=Object.keys(B).filter(k=>grupos[k]);
  if(!cursoSel||!chaves.some(k=>grupos[k][cursoSel.split('|')[1]]&&cursoSel.split('|')[0]===k)){const k=chaves[0];cursoSel=k?k+'|'+Object.keys(grupos[k]).sort((a,b)=>cursoCurto(a).localeCompare(cursoCurto(b)))[0]:null;}
  const lista=chaves.map(k=>`<h3>${esc(B[k])}</h3>`+Object.keys(grupos[k]).sort((a,b)=>cursoCurto(a).localeCompare(cursoCurto(b))).map(t=>`<button data-cur="${esc(k+'|'+t)}" aria-pressed="${cursoSel===k+'|'+t}"><span>${esc(cursoCurto(t))}</span><span>${grupos[k][t]}</span></button>`).join('')).join('');
  let feed='<p class="empty">Nenhuma peça com os filtros atuais.</p>';
  if(cursoSel){const [k,t]=cursoSel.split('|');const xs=todos.filter(x=>x.bloco===k&&x.turmas.includes(t)).sort(ord);let mesAnt='';
    feed=`<div class="bar"><h2>${esc(NOMES[t]||t)}</h2><span class="note">${esc(B[k])} · ${xs.length} peças, da primeira à última, com um trecho do texto.</span></div>`+xs.map(x=>{const mm=x.data?x.data.slice(0,7):'sem';let h='';if(mm!==mesAnt){mesAnt=mm;h=`<div class="mes">${mm==='sem'?'Sem data fixa (saem por evento)':MES[+mm.slice(5,7)-1]+' de '+mm.slice(0,4)}</div>`;}
      return h+`<button class="item k-${CAT[x.tipo]}" data-id="${esc(x.id)}"><span class="d">${x.data?dm(x.data):'-'}<small>${x.data?wdn(x.data).slice(0,3):''}</small></span><span class="x"><span class="ch">${esc(rotulo(x))}</span><span class="tt">${esc(x.t)}</span><span class="pv">${esc(previa(x))}</span></span><span class="st">${pills(x)}</span></button>`;}).join('');}
  $('#v').innerHTML=`<div class="curso"><nav class="clist" aria-label="Cursos">${lista}</nav><div class="feed">${feed}</div></div>`;
  document.querySelectorAll('[data-cur]').forEach(b=>b.onclick=()=>{cursoSel=b.dataset.cur;vCurso();window.scrollTo({top:$('#v').offsetTop-70});});
}
function previa(x){const c=x.conteudo;if(!c) return x.quando&&!x.data?x.quando:'';const p=(c.corpo&&c.corpo[0])||(c.arte&&c.arte[0])||(c.roteiro&&c.roteiro[0])||'';return p.replace(/\s+/g,' ');}
// Mídia e bastidores
function vMidia(){
  const xs=P.filter(x=>pass(x)&&x.data&&(!x.pub||x.tipo==='pagina'));
  const linhas=[];const vistos={};
  for(const k of Object.keys(B)){const ts=[...new Set(xs.filter(x=>x.bloco===k).flatMap(x=>x.turmas))].sort((a,b)=>cursoCurto(a).localeCompare(cursoCurto(b)));for(const t of ts){if(!vistos[k+t]){vistos[k+t]=1;linhas.push({k,t});}}}
  const d0=toD('2026-10-01'),d1=toD('2027-08-01'),dias=(d1-d0)/864e5,L=330,W=Math.max(1300,Math.round(dias*5.2)),R=16,H=30,top=40,h=top+linhas.length*H+16;
  const X=iso=>L+((toD(iso)-d0)/864e5)/dias*(W-L-R);
  let svg=`<svg width="${W}" height="${h}" viewBox="0 0 ${W} ${h}" role="img" aria-label="Campanhas pagas e marcos por turma">`;
  for(let d=new Date(d0);d<=d1;d.setMonth(d.getMonth()+1)){const x=X(isoD(d));svg+=`<line class="grid" x1="${x}" y1="${top-10}" x2="${x}" y2="${h-8}"/><text class="ax" x="${x+5}" y="${top-16}">${MES[d.getMonth()].slice(0,3)} ${d.getFullYear()}</text>`;}
  let ant='';linhas.forEach((ln,i)=>{const y=top+i*H;if(ln.k!==ant){ant=ln.k;svg+=`<line class="grid" x1="0" y1="${y}" x2="${W}" y2="${y}"/><text class="ax" x="10" y="${y+12}">${esc(B[ln.k].replace('Pós-graduação: ','Pós: '))}</text>`;}
    const nm=cursoCurto(ln.t);svg+=`<text x="10" y="${y+24}" font-weight="600">${esc(nm.length>40?nm.slice(0,nm.lastIndexOf(' ',40)):nm)}<title>${esc(NOMES[ln.t]||ln.t)}</title></text>`;
    const meus=xs.filter(x=>x.bloco===ln.k&&x.turmas.includes(ln.t));
    for(const x of meus.filter(x=>x.data_fim&&CAT[x.tipo]==='midia')){const a=X(x.data),b=X(x.data_fim);svg+=`<rect class="mk k-midia" data-id="${esc(x.id)}" x="${a}" y="${y+14}" width="${Math.max(3,b-a)}" height="10" rx="4" style="fill:var(--k);opacity:.4"><title>${esc(dm(x.data)+' a '+dm(x.data_fim)+': '+x.t)}</title></rect>`;}
    for(const x of meus){if(x.data_fim&&CAT[x.tipo]==='midia') continue;const cx=X(x.data);
      if(x.tipo==='inicio_turma') svg+=`<path class="mk k-marco" data-id="${esc(x.id)}" d="M${cx} ${y+10} l8 9 l-8 9 l-8 -9 z" style="fill:var(--k)"><title>${esc('Início das aulas: '+dma(x.data))}</title></path>`;
      else svg+=`<circle class="mk k-${CAT[x.tipo]}" data-id="${esc(x.id)}" cx="${cx}" cy="${y+19}" r="5" style="fill:var(--k)"><title>${esc(dm(x.data)+' '+TIPON[x.tipo]+': '+x.t)}</title></circle>`;}});
  const xh=X(HOJE);svg+=`<line class="hoje" x1="${xh}" y1="${top-10}" x2="${xh}" y2="${h-8}"/><text class="ax" x="${xh+5}" y="${h-10}">hoje</text></svg>`;
  $('#v').innerHTML=`<div class="bar"><h2>Campanhas pagas e bastidores, por turma</h2></div><p class="note">Faixas roxas são as fases das campanhas pagas, do início ao fim. Pontos são aprovações, conferências, relatórios e a publicação da página. O losango é o início das aulas. Passe o mouse para ver o nome e clique para abrir os detalhes.</p><div class="gantt">${svg}</div>`;
  const g=$('.gantt');g.scrollLeft=Math.max(0,xh-L-80);
}
// Janela da peça: a peça como vai ao ar
function txt(s){s=esc(s);return s.replace(/\[(LINK|link[^\]]*)\]/g,'<span class="lk">link da página</span>').replace(/\[(nome|primeiro_nome)\]/gi,'<span class="mk2">nome</span>').replace(/\[(T|SUPOSIÇÃO|CONFIRMAR[^\]]*|DADO NÃO FORNECIDO)\]/g,'<span class="mk2" title="Marca de conteúdo condicionado">[$1]</span>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');}
const ps=a=>(a||[]).map(p=>`<p>${txt(p)}</p>`).join('');
const arteTxt=a=>{const s=String(a||'').replace(/^(Tela|Card|Slide|Cart[aã]o)\s*\d+\s*[:.]\s*/i,'');const p=s.split(/\s+\|\s+/);return `<p>${txt(p[0].replace(/^"|"$/g,''))}</p>`+p.slice(1).map(z=>`<small class="sub">${txt(z.replace(/^"|"$/g,''))}</small>`).join('');};
function dest(c,rot){const d=(c.destaque||[]).find(d=>d.rotulo.toLowerCase().startsWith(rot));return d?d.texto:null;}
function mock(x){
  const c=x.conteudo;
  if(!c) return `<div class="empty">${x.pub?'O texto desta peça ainda não está disponível no painel. Abra as notas de produção ao lado para ver o que o arquivo traz.':'Este item é dos bastidores: não vai ao público. Os detalhes estão ao lado e nas notas de produção.'}</div>`;
  const prof=`<div class="hd"><span class="av">UF</span><div><b>Faculdade Ufape</b><small>${esc(canal(x))}</small></div></div>`;
  const lead=(c.destaque||[]).filter(d=>!/^(assunto|pré|pre)/i.test(d.rotulo));
  const chamada=c.chamada?`<span class="cta">${txt(c.chamada)}</span>`:'';
  let h='';
  if(x.tipo==='whatsapp'){const pl=dest(c,'primeira')||dest(c,'gancho');h=`<div class="mock"><div class="hd"><span class="av">UF</span><div><b>Faculdade Ufape</b><small>WhatsApp${x.hora?' · '+esc(x.hora):''}</small></div></div><div class="wa"><div class="bub">${pl?`<p class="lead">${txt(pl)}</p>`:''}${ps(c.corpo)}${chamada}<span class="tm">${esc(x.hora||'')}</span></div></div></div>`;}
  else if(x.tipo==='email'){const as=dest(c,'assunto'),pre=dest(c,'pré')||dest(c,'pre');h=`<div class="mock mail"><div class="meta"><span>De: Faculdade Ufape</span><b>${txt(as||x.t)}</b>${pre?`<span>${txt(pre)}</span>`:''}</div><div class="body">${ps(c.corpo)}${chamada}</div></div>`;}
  else if(x.tipo==='pagina'){h=`<div class="mock brw"><div class="url">faculdade.ufape.com.br / página da turma</div><div class="body">${lead.length?`<h3>${txt(lead[0].texto)}</h3>`:''}${ps(c.corpo)}${(c.arte||[]).length?`<ul>${c.arte.map(a=>`<li>${txt(a)}</li>`).join('')}</ul>`:''}${chamada}</div></div>`;}
  else if(x.tipo==='anuncio'){h=`<div class="mock ad">${prof.replace('</small>',' · <span class="tag">Patrocinado</span></small>')}${(c.arte||[]).length?`<div class="slides">${c.arte.map((a,i)=>`<div class="slide"><span class="num">${i+1}/${c.arte.length}</span>${arteTxt(a)}</div>`).join('')}</div>`:''}<div class="cap">${lead.map(d=>`<p class="lead">${txt(d.texto)}</p>`).join('')}${ps(c.corpo)}${chamada}</div></div>`;}
  else if(x.tipo==='video'||x.tipo==='reels'){h=`<div class="mock">${prof}${(c.arte||[]).length?`<div class="slides">${c.arte.map((a,i)=>`<div class="slide v"><span class="num">tela ${i+1}</span>${arteTxt(a)}</div>`).join('')}</div>`:''}${(c.roteiro||[]).length?`<ol class="scenes k-social">${c.roteiro.map(r=>`<li><span>${txt(r)}</span></li>`).join('')}</ol>`:''}<div class="cap">${lead.map(d=>`<p class="lead">${txt(d.texto)}</p>`).join('')}${ps(c.corpo)}${chamada}</div></div>`;}
  else {const v=x.tipo==='story';h=`<div class="mock">${prof}${(c.arte||[]).length?`<div class="slides">${c.arte.map((a,i)=>`<div class="slide${v?' v':''}"><span class="num">${x.tipo==='card_docente'?'card':v?'tela':'card'} ${i+1}/${c.arte.length}</span>${arteTxt(a)}</div>`).join('')}</div>`:''}${(c.roteiro||[]).length?`<ol class="scenes k-social">${c.roteiro.map(r=>`<li><span>${txt(r)}</span></li>`).join('')}</ol>`:''}${(lead.length||(c.corpo||[]).length||chamada)?`<div class="cap">${lead.map(d=>`<p class="lead">${txt(d.texto)}</p>`).join('')}${ps(c.corpo)}${chamada}</div>`:''}</div>`;}
  if((c.variantes||[]).length) h+=`<div class="var"><b>Outras versões para teste</b>${c.variantes.map(v=>`<div><strong>${esc(v.rotulo)}:</strong> ${txt(v.texto)}</div>`).join('')}</div>`;
  if(c.observacao) h+=`<p class="note">${txt(c.observacao)}</p>`;
  return h;}
function inl(t){t=esc(t);return t.replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');}
function md(lines,base){const out=[];let i=0;const L=lines;
  while(i<L.length){const l=L[i];if(!l.trim()||/^---+\s*$/.test(l)){i++;continue;}
    let m=l.match(/^(#{1,6})\s+(.*)/);if(m){out.push(`<h4 data-l="${base+i}">${inl(m[2])}</h4>`);i++;continue;}
    if(l.trim().startsWith('|')){const st=i,b=[];while(i<L.length&&L[i].trim().startsWith('|')){b.push(L[i]);i++;}const cel=r=>r.trim().replace(/^\||\|$/g,'').split('|').map(c=>c.trim());const sep=b[1]&&/^\s*\|?\s*:?-{2,}/.test(b[1]);
      out.push(`<div class="tbl"><table>${sep?'<thead><tr>'+cel(b[0]).map(c=>`<th>${inl(c)}</th>`).join('')+'</tr></thead>':''}<tbody>${(sep?b.slice(2):b).map((r,j)=>`<tr data-l="${base+st+(sep?2:0)+j}">${cel(r).map(c=>`<td>${inl(c)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`);continue;}
    if(l.startsWith('>')){const st=i,b=[];while(i<L.length&&L[i].startsWith('>')){b.push(L[i].replace(/^>\s?/,''));i++;}out.push(`<blockquote data-l="${base+st}">${b.map(inl).join('<br>')}</blockquote>`);continue;}
    if(/^\s*([-*]|\d+\.)\s/.test(l)){const st=i,b=[];while(i<L.length&&(/^\s*([-*]|\d+\.)\s/.test(L[i])||/^\s{2,}\S/.test(L[i]))){b.push(L[i]);i++;}out.push(`<ul data-l="${base+st}">${b.map((x,j)=>`<li data-l="${base+st+j}">${inl(x.trim().replace(/^([-*]|\d+\.)\s/,''))}</li>`).join('')}</ul>`);continue;}
    const st=i,b=[l.trim()];i++;while(i<L.length&&L[i].trim()&&!/^(#|\||>|\s*([-*]|\d+\.)\s)/.test(L[i])){b.push(L[i].trim());i++;}out.push(`<p data-l="${base+st}">${inl(b.join(' '))}</p>`);}
  return out.join('');}
let lista=[],pos=-1;
function abrir(id,ctx){
  const x=P.find(p=>p.id===id);if(!x) return;
  if(ctx){lista=ctx;} pos=lista.indexOf(id);
  const k=CAT[x.tipo];
  $('#m-crumb').className='crumb k-'+k;$('#m-crumb').textContent=rotulo(x);
  $('#m-prev').disabled=pos<=0;$('#m-next').disabled=pos<0||pos>=lista.length-1;
  $('#m-stage').innerHTML=`<h2>${esc(x.t)}</h2>${mock(x)}`;
  const trv=(x.tr||[]).length?`<div><dt>O que precisa da Ufape antes de sair</dt><dd class="trv">${x.tr.map(([c,e])=>`<div><b>${esc(c)}</b><br>${esc(e||'Resposta ou correção pedida no plano da onda.')}</div>`).join('')}</dd></div>`:'';
  $('#m-side').innerHTML=`<dl><div><dt>Quando sai</dt><dd>${x.data?esc(wdn(x.data))+', ':''}${esc(quando(x))}</dd></div><div><dt>Curso</dt><dd>${esc(x.turmas.map(t=>NOMES[t]||t).join('; '))}</dd></div><div><dt>Onde</dt><dd>${esc(canal(x))}</dd></div><div><dt>Situação</dt><dd>${pills(x)}<br><span class="note">${esc(STD[x.status])}</span></dd></div>${trv}</dl>
  <details><summary>Notas de produção</summary><p class="note">Testes, contagem de caracteres, links de rastreio e conferências, como estão no arquivo.</p><div class="md">${md(x.nt.split('\n'),x.nb)}</div></details>
  <details id="m-full"><summary>Arquivo original</summary><p class="note"><code>${esc(x.arquivo)}</code>, linha ${x.linha}</p><div class="full md"></div></details>`;
  $('#m-full').addEventListener('toggle',e=>{if(!e.target.open) return;const box=e.target.querySelector('.full');if(!box.innerHTML){box.innerHTML=md((ARQ[x.arquivo]||'').split('\n'),1);const el=[...box.querySelectorAll('[data-l]')].filter(z=>+z.dataset.l<=x.linha).pop();if(el){el.classList.add('hl');el.scrollIntoView({block:'center'});}}});
  $('#modal').hidden=false;document.body.style.overflow='hidden';$('#m-close').focus();$('.sheet .in').scrollTop=0;
}
function fechar(){$('#modal').hidden=true;document.body.style.overflow='';}
// navegação
const VIEWS={semana:vSemana,mes:vMes,curso:vCurso,midia:vMidia};
function rota(){const h=location.hash.slice(1);const v=VIEWS[h]?h:'semana';document.querySelectorAll('.tablist a').forEach(a=>a.setAttribute('aria-current',a.getAttribute('href')==='#'+v?'page':'false'));VIEWS[v]();}
document.addEventListener('click',e=>{const t=e.target.closest('[data-id]');if(t&&!t.closest('#modal')){const ctx=[...document.querySelectorAll('#v [data-id]')].map(z=>z.dataset.id);abrir(t.dataset.id,[...new Set(ctx)]);}});
$('#m-close').onclick=fechar;$('#modal').addEventListener('click',e=>{if(e.target.id==='modal')fechar();});
$('#m-prev').onclick=()=>{if(pos>0)abrir(lista[pos-1]);};$('#m-next').onclick=()=>{if(pos<lista.length-1)abrir(lista[pos+1]);};
document.addEventListener('keydown',e=>{if($('#modal').hidden) return;if(e.key==='Escape')fechar();if(e.key==='ArrowRight')$('#m-next').click();if(e.key==='ArrowLeft')$('#m-prev').click();});
$('#f-bloco').innerHTML='<option value="">Todos os cursos</option>'+Object.entries(B).map(([k,v])=>`<option value="${k}">${esc(v)}</option>`).join('');
$('#f-cat').innerHTML='<option value="">Todos os canais</option>'+['social','msg','site','midia','marco'].map(k=>`<option value="${k}">${esc(CATN[k])}</option>`).join('');
$('#f-bloco').oninput=e=>{F.bloco=e.target.value;cursoSel=null;rota();};$('#f-cat').oninput=e=>{F.cat=e.target.value;rota();};
$('#f-trava').oninput=e=>{F.trava=e.target.checked;rota();};$('#f-q').oninput=e=>{F.q=e.target.value.trim();rota();};
window.addEventListener('hashchange',rota);
// resumo
const PUB=P.filter(x=>x.pub),s0=segunda(HOJE);
$('#k-ap').textContent=PUB.filter(x=>x.status==='aguardando_aprovacao').length;
$('#k-sem').textContent=PUB.filter(x=>x.data&&x.data>=s0&&x.data<=addD(s0,6)).length;
$('#k-30').textContent=PUB.filter(x=>x.data&&x.data>=HOJE&&x.data<addD(HOJE,30)).length;
$('#k-tr').textContent=PUB.filter(x=>x.tr&&x.tr.length).length;
$('#k-tot').textContent=PUB.length;$('#k-hoje').textContent=dma(HOJE);
document.querySelectorAll('.kpi').forEach(b=>b.onclick=()=>{const a=b.dataset.acao;if(a==='trava'){$('#f-trava').checked=true;F.trava=true;}semana=segunda(HOJE);location.hash=a==='mes'?'mes':'semana';rota();});
rota();
"""

HTML = f"""<title>Entregáveis de marketing Ufape</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Instrument+Sans:wght@400;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap">
<style>{CSS}</style>
<header class="top"><div class="g">
<div><span class="eyebrow">Situação em <span id="k-hoje"></span> · tudo o que começa até abril de 2027</span>
<h1>Entregáveis de marketing Ufape</h1>
<p class="lede">As <b id="k-tot"></b> peças que vão ao público, no dia em que saem. Clique numa peça para ver como ela vai aparecer no Instagram, no WhatsApp ou no e-mail. Nada foi publicado, enviado ou pago.</p></div>
<div class="kpis">
<button class="kpi" data-acao="semana"><b id="k-sem"></b><span>saem nesta semana</span></button>
<button class="kpi" data-acao="mes"><b id="k-30"></b><span>saem nos próximos 30 dias</span></button>
<button class="kpi" data-acao="semana"><b id="k-ap"></b><span>estão prontas e esperam a sua aprovação</span></button>
<button class="kpi" data-acao="trava"><b id="k-tr"></b><span>dependem de uma resposta da Ufape para sair</span></button>
</div>
</div></header>
<nav class="tabs" aria-label="Visões"><div class="g">
<div class="tablist"><a href="#semana">Semana</a><a href="#mes">Mês</a><a href="#curso">Por curso</a><a href="#midia">Campanhas e bastidores</a></div>
<div class="filters">
<input id="f-q" type="search" placeholder="Buscar curso ou assunto" aria-label="Buscar">
<select id="f-bloco" aria-label="Cursos"></select><select id="f-cat" aria-label="Canais"></select>
<label for="f-trava"><input id="f-trava" type="checkbox"> Só o que depende da Ufape</label>
</div></div></nav>
<main><div class="g">
<div class="legend"><span><i class="sw k-social"></i>Redes sociais e vídeo</span><span><i class="sw k-msg"></i>WhatsApp e e-mail</span><span><i class="sw k-site"></i>Página da turma</span><span><i class="sw k-midia"></i>Anúncios e campanhas pagas</span><span><i class="sw k-marco"></i>Aprovações, conferências e marcos</span></div>
<section id="v" aria-live="polite"></section>
</div></main>
<footer><div class="g"><p>Os textos e as datas vêm dos arquivos aprovados pela revisão de qualidade da squad. "Depende da Ufape" quer dizer que a peça espera uma resposta ou uma correção que só a Ufape pode fazer, mesmo depois da sua aprovação. Não há dado pessoal de aluno ou candidato.</p></div></footer>
<div class="modal" id="modal" hidden role="dialog" aria-modal="true" aria-labelledby="m-crumb">
<div class="sheet"><header><span id="m-crumb" class="crumb"></span><div class="nav"><button class="btn" id="m-prev">‹ Anterior</button><button class="btn" id="m-next">Próxima ›</button><button class="btn pri" id="m-close">Fechar</button></div></header>
<div class="in"><div class="stage" id="m-stage"></div><aside class="side" id="m-side"></aside></div></div>
</div>
<script>{JS.replace('__DATA__', DATA)}</script>
"""
os.makedirs(SAIDA, exist_ok=True)
open(SAIDA + 'painel-artifact.html', 'w', encoding='utf-8').write(HTML)
completo = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HTML.split('<header', 1)[0] + '</head>\n<body>\n<header' + HTML.split('<header', 1)[1] + '</body>\n</html>\n')
open(COPIA, 'w', encoding='utf-8').write(completo)
com = sum(1 for x in pecas if x['_publica'] and x.get('conteudo'))
print('peças', len(pecas), 'públicas', sum(1 for x in pecas if x['_publica']), 'com texto', com, 'tamanho', len(completo))
