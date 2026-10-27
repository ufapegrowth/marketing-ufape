"""Documento final para o cliente: narrativa (relatorios M.2) mais o mapa filtrado até abril de 2027.

Rodar da raiz do repositório, depois de mapa_json.py e mapa_html.py:
    python3 -I ferramentas/mapa-mental/documento_final.py
Grava saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27-documento-final.html
e ferramentas/mapa-mental/saida/documento-final-artifact.html (sem doctype, para publicar como página).
"""
import html, json, re

S = 'ferramentas/mapa-mental/saida/'
NARRATIVA = 'saidas/09-analytics-e-insights/relatorios-geral-2026-10-27.md'
MAPA = S + 'mapa-artifact.html'
LIMITE = '2027-04-30'
PROXIMA_LIVRES = {'68638', '560'}
# Seções da narrativa que ficam fora da página do cliente (roteiro de quem apresenta)
FORA = ('8. Roteiro de apresentação',)


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\w*])\*([^*]+)\*(?![\w*])', r'<em>\1</em>', t)
    t = re.sub(r'(https://[^\s<)]+)', r'<a href="\1" rel="noopener">\1</a>', t)
    t = re.sub(r'\[(SUPOSIÇÃO|CONFIRMAR[^\]]*|DADO NÃO FORNECIDO)\]', r'<span class="mk">[\1]</span>', t)
    return t


def md(texto):
    linhas = texto.split('\n')
    out, i = [], 0
    while i < len(linhas):
        l = linhas[i]
        if not l.strip() or l.strip() == '---':
            i += 1; continue
        m = re.match(r'^(#{2,4}) (.*)', l)
        if m:
            n = len(m.group(1)); tit = m.group(2)
            ident = 's-' + re.sub(r'[^a-z0-9]+', '-', tit.lower().encode('ascii', 'ignore').decode()).strip('-')
            out.append(f'<h{n} id="{ident}">{inline(tit)}</h{n}>'); i += 1; continue
        if l.startswith('|'):
            bloco = []
            while i < len(linhas) and linhas[i].startswith('|'):
                bloco.append(linhas[i]); i += 1
            cel = lambda r: [c.strip() for c in r.strip().strip('|').split('|')]
            cab = cel(bloco[0]); corpo = [cel(r) for r in bloco[2:]]
            out.append('<div class="tbl"><table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in cab) + '</tr></thead><tbody>'
                       + ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>' for r in corpo) + '</tbody></table></div>')
            continue
        if re.match(r'^\s*(- |\d+\. )', l):
            bloco = []
            while i < len(linhas) and (re.match(r'^\s*(- |\d+\. )', linhas[i]) or (linhas[i].startswith('  ') and linhas[i].strip())):
                bloco.append(linhas[i]); i += 1
            out.append(lista(bloco)); continue
        par = [l.strip()]; i += 1
        while i < len(linhas) and linhas[i].strip() and not re.match(r'^(#|\||\s*- |\s*\d+\. )', linhas[i]):
            par.append(linhas[i].strip()); i += 1
        out.append(f'<p>{inline(" ".join(par))}</p>')
    return '\n'.join(out)


def lista(bloco):
    ordenada = bool(re.match(r'^\s*\d+\. ', bloco[0]))
    base = len(bloco[0]) - len(bloco[0].lstrip())
    itens, atual = [], None
    for l in bloco:
        ind = len(l) - len(l.lstrip())
        if ind <= base and re.match(r'^\s*(- |\d+\. )', l):
            atual = [re.sub(r'^\s*(- |\d+\. )', '', l), []]; itens.append(atual)
        elif atual is not None:
            atual[1].append(l)
    tag = 'ol' if ordenada else 'ul'
    partes = []
    for txt, filhos in itens:
        sub = lista(filhos) if filhos and re.match(r'^\s*(- |\d+\. )', filhos[0]) else (inline(' '.join(f.strip() for f in filhos)) if filhos else '')
        partes.append(f'<li>{inline(txt)}{sub}</li>')
    return f'<{tag}>' + ''.join(partes) + f'</{tag}>'


# Narrativa: corta o cabeçalho de metadados (até "## Como ler") e as seções de FORA
bruto = open(NARRATIVA, encoding='utf-8').read()
corpo = bruto[bruto.index('## Como ler as situações'):]
secoes = re.split(r'(?m)^(?=## )', corpo)
principais, notas = [], []
for s in secoes:
    if not s.strip():
        continue
    tit = s.split('\n', 1)[0][3:].strip()
    if any(tit.startswith(f) for f in FORA):
        continue
    (notas if tit in ('Fatos (com fonte)', '[SUPOSIÇÃO]', '[CONFIRMAR]', 'Fontes') else principais).append(s)
NAV = [(s.split('\n', 1)[0][3:].strip(), 's-' + re.sub(r'[^a-z0-9]+', '-', s.split('\n', 1)[0][3:].strip().lower().encode('ascii', 'ignore').decode()).strip('-')) for s in principais]
HTML_NARR = md('\n'.join(principais))
HTML_NOTAS = md('\n'.join(notas).replace('## ', '### '))

# Mapa: dados do gerador, filtrados pelo recorte do documento
dados = json.load(open(S + 'mapa-dados.json', encoding='utf-8'))
def no_documento(j):
    if j['recorte'] != 'planejar' or j['codigo'] in PROXIMA_LIVRES:
        return False
    return not (j['inicio'] and j['inicio'] > LIMITE)
proxima = sorted([j for j in dados if j['recorte'] == 'planejar' and not no_documento(j)], key=lambda j: (j['inicio'] or '9999', j['codigo']))
ids = {j['id'] for j in dados if no_documento(j)}
fmt = lambda iso: '/'.join(reversed(iso.split('-'))) if iso else '-'
nome = lambda j: j.get('nome_padrao') or j['nome_no_site']
LIN = {'pos': 'Pós-graduação', 'livres': 'Cursos Livres', 'eventos': 'Eventos', 'graduacao': 'Graduação'}
TAB_PROX = ('<div class="tbl"><table><thead><tr><th>Código</th><th>Turma</th><th>Linha</th><th>Início</th><th>Local</th></tr></thead><tbody>'
            + ''.join(f'<tr><td class="f">{html.escape(j["codigo"])}</td><td>{html.escape(nome(j))}</td><td>{LIN[j["linha"]]}</td><td>{fmt(j["inicio"])}</td><td>{html.escape(j["local"] or "-")}</td></tr>' for j in proxima)
            + '</tbody></table></div>')

mapa = open(MAPA, encoding='utf-8').read()
css_mapa = re.search(r'<style>(.*?)</style>', mapa, re.S).group(1)
script = re.search(r'<script>(.*?)</script>', mapa, re.S).group(1)
corpo_mapa = re.search(r'(<div class="bar">.*?)</div></main>', mapa, re.S).group(1)
corpo_mapa = corpo_mapa.replace('<span>itens no catálogo</span>', '<span>itens neste documento</span>')
corpo_mapa = corpo_mapa.replace('<span>no recorte do plano + Graduação (ramo à parte)</span>', '<span>turmas, provas e eventos até abril de 2027 + Graduação</span>')
assert 'até abril de 2027 + Graduação' in corpo_mapa, 'rótulo do cartão do recorte mudou no mapa'
# O mapa do documento só mostra o recorte; a lista completa continua no mapa de trabalho
script = script.replace('const D=', 'const D_TODOS=', 1)
script = re.sub(r'(const D_TODOS=.*?\]), AREAS=', lambda m: m.group(1) + ', D=D_TODOS.filter(x=>IDS.has(x.id)), AREAS=', script, count=1, flags=re.S)
script = 'const IDS=new Set(' + json.dumps(sorted(ids), ensure_ascii=False) + ');\n' + script
assert 'D=D_TODOS.filter' in script, 'filtro do mapa não entrou no script'

CSS_DOC = r"""
.doc{display:grid;grid-template-columns:minmax(0,1fr);gap:28px}
@media (min-width:1000px){.doc{grid-template-columns:220px minmax(0,1fr)}}
nav.toc{font-size:14px}
@media (min-width:1000px){nav.toc{position:sticky;top:calc(env(safe-area-inset-top,0px) + 16px);align-self:start;max-height:calc(100vh - 32px);overflow:auto}}
nav.toc ol{margin:0;padding:0;list-style:none;display:grid;gap:6px;color:var(--muted)}
nav.toc a{color:var(--ink);text-decoration:none} nav.toc a:hover{color:var(--accent);text-decoration:underline}
article.narr{min-width:0;display:grid;gap:12px;max-width:860px}
article.narr h2{font:700 24px/1.2 var(--f-display);margin:28px 0 2px;text-wrap:balance;scroll-margin-top:16px}
article.narr h2:first-child{margin-top:0}
article.narr h3{font:600 17px/1.3 var(--f-display);margin:14px 0 0;text-wrap:balance;scroll-margin-top:16px}
article.narr p,article.narr li{max-width:72ch}
article.narr ul,article.narr ol{margin:0;padding-left:22px;display:grid;gap:5px}
article.narr td{font-size:13.5px}
article.narr code{font:12.5px var(--f-data);background:var(--accent-soft);padding:1px 5px;border-radius:4px;overflow-wrap:anywhere}
article.narr a{color:var(--accent);overflow-wrap:anywhere}
.mk{font:600 12px/1 var(--f-data);color:var(--wait);white-space:nowrap}
.aviso{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:8px;padding:12px 14px;font-size:14px}
section.bloco{display:grid;gap:14px}
section.bloco>h2{font:700 24px/1.2 var(--f-display);margin:0}
details.notas{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:12px 16px}
details.notas>summary{cursor:pointer;font-weight:600}
details.notas h3{font:600 15px/1.3 var(--f-display);margin:14px 0 4px}
details.notas ul{padding-left:20px;display:grid;gap:4px;font-size:14px}
.bar{position:static}
"""

N_DOC = len(ids)
HTML = f"""<title>Plano de marketing Ufape</title>
<meta name="claude:viewport-fit-sides" content="cover">
<style>{css_mapa}{CSS_DOC}</style>
<header class="top"><div class="wrap">
<span class="eyebrow">Planejamento de marketing · tudo o que começa até abril de 2027 · versão de 27/10/2026</span>
<h1>Plano de marketing Ufape</h1>
<p class="lede">Estratégia e plano de cada curso, turma, prova e evento que começa até abril de 2027, com o que está pronto para aprovar, o que a Ufape precisa decidir e o calendário. Maio de 2027 em diante e os Cursos Livres de 2027 estão na próxima etapa. Nada aqui foi publicado, enviado ou pago.</p>
</div></header>
<main><div class="wrap">
<div class="doc">
<nav class="toc" aria-label="Sumário"><ol>{''.join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for t, i in NAV)}<li><a href="#mapa">Mapa por curso</a></li><li><a href="#proxima-lista">Turmas da próxima etapa</a></li></ol></nav>
<article class="narr">
<p class="aviso">Datas vêm da planilha "DATAS CURSOS E PÓS"; preço e demais dados, do site lido em 26/10/2026. Marcas como <span class="mk">[CONFIRMAR]</span> indicam dado que só a Ufape pode confirmar; <span class="mk">[SUPOSIÇÃO]</span>, uma hipótese ainda não validada. Não há dado pessoal de aluno ou candidato.</p>
{HTML_NARR}
<details class="notas"><summary>Fatos, suposições, dados a confirmar e fontes</summary>{HTML_NOTAS}</details>
</article>
</div>
<section class="bloco" id="mapa"><h2>Mapa por curso</h2>
<p class="lede">{N_DOC} itens do recorte até abril de 2027, por linha e área. Abra um item para ver a onda, o kit mínimo, os canais, as pendências e as aprovações pedidas.</p>
</section>
</div></main>
{corpo_mapa}</div></main>
<main><div class="wrap">
<section class="bloco" id="proxima-lista"><h2>Turmas da próxima etapa</h2>
<p class="lede">{len(proxima)} turmas ficam para a próxima rodada: Pós de maio de 2027 em diante e os Cursos Livres de 2027.</p>
{TAB_PROX}
</section>
</div></main>
<footer><div class="wrap">
<p>Fontes: catálogo de cursos (planilha e site de 26/10/2026), plano geral do cmo, planos das ondas 1, 2 e 3 da Pós, plano da Graduação, planos de mídia e revisões do qa-de-marketing. Um JSON por item em saidas/10-operacoes-de-marketing/cursos/.</p>
</div></footer>
<script>{script}</script>
"""
open(S + 'documento-final-artifact.html', 'w', encoding='utf-8').write(HTML)
completo = ('<!doctype html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            + HTML.split('<header', 1)[0] + '</head>\n<body>\n<header' + HTML.split('<header', 1)[1] + '</body>\n</html>\n')
open('saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-27-documento-final.html', 'w', encoding='utf-8').write(completo)
print('itens no mapa', N_DOC, 'próxima etapa', len(proxima), 'tamanho', len(completo))
