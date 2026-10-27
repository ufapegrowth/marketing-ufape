# Gera os JSON por item (esquema versão 1 de arquiteto-de-fluxos-geral-2026-10-26.md) a partir do
# catálogo e das saídas aprovadas. Nenhum número é inventado: dado ausente vira "[CONFIRMAR]" ou null
# com pendência. Roda a partir da raiz do repositório marketing-ufape.
# Versão de 27/10/2026 com as correções B1 a B14 da revisão do qa
# (saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-27-mapa.md, seção 3).
# Pendências e aprovações são lidas das tabelas dos planos e de docs/pendencias-camada-1.md. Onde a fonte é
# texto corrido (e não tabela), há um dicionário curto no script, com o arquivo e a seção de origem.
import re, json, os, sys, datetime, unicodedata

HOJE = '2026-10-27'
CAT = 'contexto/catalogo-de-cursos.md'
PLANO_GERAL = 'saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md'
PL1 = 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md'
PL2 = 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md'
PL3 = 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md'
PLG = 'saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md'
GMG = 'saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md'
B = 'docs/execucao-2026-10-26.md'
PC1 = 'docs/pendencias-camada-1.md'
DIARIO = 'docs/andamento-planejamento.md'
OUT = 'saidas/10-operacoes-de-marketing/cursos'

def sem_acento(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def slug(s):
    s = sem_acento(s.lower())
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

def data_iso(s):
    m = re.search(r'(\d{2})/(\d{2})/(\d{4})', s or '')
    return f'{m.group(3)}-{m.group(2)}-{m.group(1)}' if m else None

def ler(p):
    return open(p, encoding='utf-8').read()

def trecho(txt, titulo):
    # texto da seção cujo título casa com a expressão "titulo", até o próximo título de nível igual ou maior
    linhas = txt.split('\n'); ini = None; nivel = None
    for i, l in enumerate(linhas):
        m = re.match(r'(#+) ', l)
        if ini is None:
            if m and re.search(titulo, l): ini = i; nivel = len(m.group(1))
        elif m and len(m.group(1)) <= nivel:
            return '\n'.join(linhas[ini:i])
    return '\n'.join(linhas[ini:]) if ini is not None else ''

def tabelas(t):
    # lista de tabelas markdown do trecho; cada tabela é uma lista de dicionários pelo cabeçalho
    out = []; cab = None; rows = None
    for l in t.split('\n'):
        if l.startswith('|'):
            cel = [c.strip() for c in l.strip().strip('|').split('|')]
            if cab is None: cab = cel; rows = []; continue
            if set(l.replace('|', '').strip()) <= set('-: '): continue
            rows.append(dict(zip(cab, cel)))
        elif cab is not None:
            out.append(rows); cab = None
    if cab is not None: out.append(rows)
    return out

def limpa(s, n=240):
    # R9: sem negrito, sem travessão ou meia-risca (U+2014 e U+2013), sem frase de certificação ligada ao órgão regulador, sem urgência falsa por vagas
    s = (s or '').replace('**', '').replace('`', '').replace(chr(0x2014), ', ').replace(chr(0x2013), ', ')
    s = re.sub(r'["“][^"”]*(MEC|Ministério da Educação)[^"”]*["”]', 'a frase de certificação que a squad não repete', s)
    s = re.sub(r'\bligad([ao]s?) ao MEC', r'ligad\1 ao órgão regulador', s)
    s = re.sub(r'\bMEC\b', 'órgão regulador', s)
    s = re.sub(r'(?i)[uú]ltimas\s+vagas', 'urgência por vagas', s)
    s = re.sub(r'\s+', ' ', s).strip()
    if len(s) > n:
        s = s[:n - 1].rsplit(' ', 1)[0].rstrip(' ,;:(') + '…'
    return s

def expande(s):
    # "G10 a G14" vira G10, G11, G12, G13, G14; "OU19 a OU21" idem; códigos soltos ficam como estão
    out = []
    for m in re.finditer(r'\b([A-Z]{1,3})(\d+)(?:\s+a\s+\1(\d+))?\b', s):
        if m.group(3):
            out += [f'{m.group(1)}{k}' for k in range(int(m.group(2)), int(m.group(3)) + 1)]
        else:
            out.append(m.group(1) + m.group(2))
    return out

# ---------- leitura do catálogo ----------
txt = ler(CAT).split('\n')
m_ger = re.search(r'Gerado em[^0-9]*(\d{2}/\d{2}/\d{4})', '\n'.join(txt[:20]))
DATA_CAT = data_iso(m_ger.group(1)) if m_ger else None

secoes = {'2': ('pos', 'pos'), '3': ('pos', 'prova_de_bolsa'), '4': ('livres', 'livre_presencial'),
          '5': ('livres', 'livre_online'), '6': ('livres', 'espanhol'), '7': ('livres', 'grupo_de_estudos'),
          '8': ('livres', 'aprimoramento'), '9': ('eventos', None)}
itens = []
sec = None; cab = None
for l in txt:
    m = re.match(r'## (\d)\. ', l)
    if m: sec = m.group(1); cab = None; continue
    if not l.startswith('|') or sec is None: continue
    cel = [c.strip() for c in l.strip().strip('|').split('|')]
    if cab is None: cab = cel; continue
    if set(l.replace('|', '').strip()) <= set('-: '): continue
    row = dict(zip(cab, cel))
    row['_secao'] = sec; row['_literal'] = l
    if sec in secoes: itens.append(row)
CODIGOS = {re.sub(r'\D', '', r.get('Código', '')) for r in itens} - {''}
def cods(s):
    return [c for c in re.findall(r'\b(\d{2,5})\b', s or '') if c in CODIGOS]

# ---------- plano geral: áreas, ondas, GUT, mídia ----------
P = ler(PLANO_GERAL)
AREAS = {}
NOMES_AREA = {}
for l in P.split('\n'):
    m = re.match(r'\| (A\d+) \| ([^|]+) \| \d+ \|(.*)$', l)
    if m:
        a = m.group(1); NOMES_AREA[a] = m.group(2).strip()
        for cod in re.findall(r'\b(\d{2,5})\b', m.group(3)):
            AREAS.setdefault(cod, a)
        if 'Neuromonitoriza' in m.group(3): AREAS['workshop-neuro'] = a
CONTINUOS = set()
for l in P.split('\n'):
    m = re.match(r'\| (A\d+) \| ([^|]+) \| \d+ \|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', l)
    if m:
        for cod in re.findall(r'\b(\d{2,5})\b', m.group(6)): CONTINUOS.add(cod)

# Itens da seção 2.1 do plano geral (lista numerada)
S21 = {}
for l in trecho(P, r'^### 2\.1 ').split('\n'):
    m = re.match(r'(\d)\. (.*)', l)
    if m: S21[int(m.group(1))] = m.group(2)
INICIADAS_ATIVAS = re.findall(r'\((\d{2,5})\)', S21[2])                      # B1: 2.1 item 2
GRUPOS_INICIADOS = cods(re.search(r'\((\d[^)]*)\)', S21[3]).group(1))          # B7: 2.1 item 3
FORA_COMO_PENDENCIA = set(cods(S21[5]))                                      # B10: 2.1 item 5
for t in tabelas(trecho(P, r'^### 2\.4 ')):                                  # B10: 2.4, linhas "pendência"
    for r in t:
        if r.get('Como aparece no mapa', '').startswith('pendência'): FORA_COMO_PENDENCIA |= set(cods(r.get('Grupo')))
MODALIDADE_DO_EVENTO = cods(S21[7])                                          # B9: 2.1 item 7 (68634)

ONDA1 = set('707 68604 68606 698 68610 68608 573 68614 623 68637 68665 68666'.split())
ONDA2 = set('616 68618 657 341 289 68615 333'.split())
ONDA3 = set('679 68632 68635 366 68628 68617 68636 68609 662 719 68616 68629 359 699 382 68623 578 352 60 68638 560'.split())
ABRIL = '679 68632 68635 366 68628 68617 68636 68609'.split()
MARCO = '657 341 289 68615 333'.split()
MAIO = '719 68616 68629 359 699 382 68623 578 352 60'.split()
ONDA1_POS = '707 68604 68606 698 68610 68608'.split()
POS_ONDA3 = ABRIL + ['662'] + MAIO

GUT = [  # (códigos, g, u, t, motivo)
    ('PROVAS', 5, 5, 4, 'porta de entrada da Pós; prova em 27/11/2026'),
    ('workshop-neuro', 4, 5, 5, 'evento em 20 e 21/11/2026 com campanha ativa'),
    ('698', 4, 5, 4, 'campanha ativa; site com 2027 e planilha com 2026'),
    ('68610 68608', 5, 4, 3, 'início em 28/11/2026; campanhas ativas'),
    ('707 68604 68606', 4, 5, 3, 'reta final e encerramento; campanhas ativas'),
    ('573 68614 623 68637', 3, 5, 3, 'Livres de novembro; datas divergem da visão de campanhas'),
    ('657 341 289 68615 333', 5, 3, 3, 'Pós de março de 2027'),
    ('679 68632 68635 366 68628 68617 68636 68609 662', 5, 2, 3, 'Pós de abril de 2027'),
    ('616 68618', 3, 3, 3, 'Livres de dezembro'),
    ('68665 68666', 2, 5, 2, 'grupos de estudos com início próximo'),
    ('719 68616 68629 359 699 382 68623 578 352 60', 5, 2, 2, 'Pós de maio de 2027'),
    ('CONTINUOS', 3, 2, 2, 'venda contínua, sem data [SUPOSIÇÃO: porta de entrada para a Pós]'),
    ('68638 560', 2, 2, 2, 'Livres de 2027'),
]

MIDIA = {}
for cods_, est in [('707 68604 68606 698 68610 68608 workshop-neuro 573 623 68614', 'ativa'), ('289 700 662', 'ativa'),
                   ('657 341 68615 333 68618 68635 366 68617 382 578 352 60 679', 'pausada'),
                   ('202 68632 68628 68609 719 68616 699 68623', 'sem_campanha')]:
    for c in cods_.split(): MIDIA[c] = est
for c in INICIADAS_ATIVAS: MIDIA[c] = 'ativa'   # B1: plano geral, 2.1 item 2 ("seguem com campanha paga ATIVA")

# ---------- pendências: fontes em tabela ----------
def pend(ref, tipo, desc, marc, campos, bloq, fonte, resolvida=None):
    return {'id': None, 'ref_plano': ref, 'tipo': tipo, 'descricao': limpa(desc), 'marcador': marc, 'campos': list(campos),
            'bloqueia': list(bloq), 'fonte': fonte, 'aberta_em': HOJE, 'resolvida_em': resolvida}

# O que cada código bloqueia, quando a tabela de origem não tem coluna própria.
BLOQ = {
    'P3': ['data', 'preco'],            # plano geral, seção 7, P3: "nenhuma peça com preço ou data desses itens até a correção"
    'P4': ['data', 'peca_final'],       # revisão do qa, B6: divergência de data entre planilha e site bloqueia sempre
    'P5': [],                           # plano geral, seção 7, P5: "peças sem número de turma"
    'P6': ['data'],                     # plano geral, seção 7, P6: "peças sem data até a Ufape confirmar"
    'P7': [],                           # plano geral, seção 7, P7: "o mapa mostra os dois ligados"
    'P8': ['anuncio'],                  # revisão do qa, B1
    'P9': ['peca_final'],               # revisão do qa, B9
    'P16': ['preco', 'peca_final'],     # plano geral, seção 7, P16: "antes de qualquer peça"
    'P17': ['peca_final'],              # plano geral, seção 7, P17: "antes de marcar como pronto"
    'OU3': ['anuncio'],                 # pendencias-camada-1, mídia de março e abril: "mídia parando na véspera do início"
    'OU10': ['peca_final'],             # plano da onda 2, seção 4.2: sem a regra, nenhuma peça de 341 sai
    'U10': ['pagina'],                  # plano da onda 2, seção 8: pré-requisito na página
    'OU18': ['data', 'peca_final', 'anuncio'],  # plano da onda 3, 2.3: espera total
    'OU19': ['data'], 'OU21': ['data'], 'OU22': ['data'],  # plano da onda 3, 2.3: peças com o mês no lugar do dia
    'OU20': ['data', 'peca_final'], 'OU23': ['data', 'peca_final'],  # plano da onda 3, 2.3 (P4): nada sai sem a data
    'OU24': ['preco'],                  # plano da onda 3, 2.3: 359 sem desconto
    'OU25': ['anuncio'],                # pendencias-camada-1, mídia: dia do 3º módulo segura a -extb
    'decisão 13': ['anuncio', 'peca_final'],    # docs/execucao-2026-10-26.md, decisão 13
}
TIPO_REF = {'P3': 'link', 'P4': 'data', 'P5': 'turma', 'P6': 'data', 'P7': 'duplicidade', 'P8': 'outro', 'P16': 'preco_ou_condicao',
            'P17': 'outro', 'OU3': 'data', 'OU10': 'preco_ou_condicao', 'OU17': 'data', 'OU18': 'data', 'OU19': 'data', 'OU20': 'data',
            'OU21': 'data', 'OU22': 'data', 'OU23': 'data', 'OU24': 'preco_ou_condicao', 'OU25': 'data', 'OU12': 'outro', 'OU13': 'divergencia'}
CAMPOS_REF = {'P3': ['pagina_oficial'], 'P4': ['inicio'], 'P5': ['turma'], 'P6': ['inicio', 'status_midia.inicio_na_visao'],
              'OU10': ['condicoes_especiais'], 'OU24': ['condicoes_especiais'], 'OU12': ['equipe.coordenadores_na_ficha'],
              'OU18': ['inicio'], 'OU19': ['inicio'], 'OU20': ['inicio'], 'OU21': ['inicio'], 'OU22': ['inicio'], 'OU23': ['inicio'],
              'OU3': ['kit.entregas[*]']}

POR_ITEM = {}   # código ou chave do item -> lista de pendências vindas das tabelas
def junta(lista, p):
    for q in lista:
        if q['ref_plano'] == p['ref_plano']:
            for k in ('campos', 'bloqueia'):
                for v in p[k]:
                    if v not in q[k]: q[k].append(v)
            if p['descricao'] not in q['descricao']: q['descricao'] = limpa(q['descricao'] + '; ' + p['descricao'])
            if p['fonte'] not in q['fonte']: q['fonte'] = q['fonte'] + '; ' + p['fonte']
            if q['resolvida_em'] and not p['resolvida_em']: q['resolvida_em'] = None
            return
    lista.append(p)
def add(chave, ref, desc, fonte, tipo=None, campos=None, bloq=None, marc='[CONFIRMAR]', resolvida=None):
    junta(POR_ITEM.setdefault(chave, []), pend(ref, tipo or TIPO_REF.get(ref, 'outro'), desc, marc,
                                                 CAMPOS_REF.get(ref, []) if campos is None else campos,
                                                 BLOQ.get(ref, []) if bloq is None else bloq, fonte, resolvida))

# B7: plano geral, seção 7, P3 a P17, para cada código citado em "Itens afetados"
P6_VISAO = {}
for t in tabelas(trecho(P, r'^## 7\. ')):
    for r in t:
        ref = r.get('#', '')
        if not re.fullmatch(r'P\d+', ref) or ref in ('P1', 'P2', 'P11', 'P18'): continue
        # P7 entra junto com os relacionados (mais abaixo), com o par citado na descrição
        alvo = INICIADAS_ATIVAS if ref == 'P8' else [] if ref == 'P7' else cods(r['Itens afetados'])
        for c in alvo:
            desc = r['Pendência'] + '. Tratamento no plano: ' + r['Tratamento no plano']
            res = None
            if ref == 'P4' and c == '698':   # decisão 19 (27/10/2026): 698 segue com 28 e 29/11/2026
                desc += '; na 698 a decisão 19 mantém o início em 28 e 29/11/2026'; res = '2026-10-27'
            if ref == 'P8': desc = 'Decidir pausa ou manutenção da campanha ativa em turma iniciada (A4)'
            add(c, ref, desc, PLANO_GERAL + ', seção 7', campos=['status_midia.campanha'] if ref == 'P8' else None, resolvida=res)
        if ref == 'P6':
            for c, d1, d2 in re.findall(r'(\d{3,5}) \((\d{2}/\d{2}(?:/\d{4})?) x (\d{2}/\d{2}(?:/\d{4})?)\)', r['Itens afetados']):
                P6_VISAO[c] = d2
        if ref == 'P7':
            P7_TXT = r['Itens afetados']
# P7 e 2.1 item 7: relacionados
RELAC = {}
def rel(a, b, relacao, natureza):
    RELAC.setdefault(a, []).append({'id': b, 'relacao': relacao, 'natureza': natureza})
PARES_P7 = []
for parte in re.split(r'[;,]', P7_TXT):
    cs = cods(parte)
    if len(cs) == 2: PARES_P7.append(tuple(cs))
    elif 'Paciente Grave' in parte and len(cs) == 1: PARES_P7.append(('paciente-grave', cs[0]))

# B6: plano da onda 3, tabelas 1.1 e 1.2, coluna "Bloqueio"
TOKEN_REF = [  # plano da onda 3, seção 8: OU25 é o dia do 3º módulo e do módulo 2; OU22 é a data só no site de 68629 e 359
    ('dia do 3º módulo', 'OU25'), ('dia do módulo 2', 'OU25'), ('data sem planilha', 'OU22'),
    ('convite da prova de Especialista', 'convite da prova de Especialista'), ('URL', 'URL "/v/"')]
BLOQ['convite da prova de Especialista'] = ['pagina']   # plano da onda 3, 2.3: "sem o convite da prova de Especialista"
BLOQ['URL "/v/"'] = ['anuncio']                          # plano da onda 3, 2.3: "URL conferida no dia da subida"
T3 = ler(PL3)
for tit, nome_t in ((r'^### 1\.1 ', '1.1'), (r'^### 1\.2 ', '1.2')):
    for t in tabelas(trecho(T3, tit)):
        for r in t:
            c = r.get('Código'); b = (r.get('Bloqueio') or '').replace('*', '')
            if c not in CODIGOS: continue
            for tok in re.split(r'[;,](?![^()]*\))', b):
                tok = tok.strip()
                if not tok or tok == '-': continue
                m = re.match(r'(P\d+|OU\d+)\b', tok)
                ref = m.group(1) if m else next((v for k, v in TOKEN_REF if k in tok), 'onda 3, Bloqueio')
                add(c, ref, f'Bloqueio no plano da onda 3 (tabela {nome_t}): {tok}', PL3 + ', tabela ' + nome_t)

# B6: perguntas por turma das seções 8 dos planos das ondas 2 e 3 (só as linhas com turma citada)
for arq in (PL2, PL3):
    for t in tabelas(trecho(ler(arq), r'^## 8\. ')):
        for r in t:
            ref = re.sub(r'\s*\(.*\)', '', r.get('#', '')).strip()
            if not re.fullmatch(r'O?U\d+', ref): continue
            for c in cods(r.get('Turma')):
                add(c, ref, f'Pergunta {ref} à Ufape ainda sem resposta; afeta: {r.get("Por que importa", "")}', arq + ', seção 8')

# Travas em texto corrido de docs/pendencias-camada-1.md (blocos da onda 2 e do lote A da onda 3)
TRAVAS = [
    # bloco "Onda 2 da Pós", travas: frases de resultado clínico de 657 (regulação) e DACVAA (regulação, até 18/02)
    ('regulação', ['657'], 'regulatorio', 'Convite da prova de Especialista e frases de resultado clínico no cronograma; sigla DACVAA de docente vai à regulação (até 18/02)', ['pagina']),
    # bloco "Onda 2 da Pós", travas: CP1 (cidade no texto) e a página da 68605 disputando a busca de 289
    ('CP1', ['289'], 'outro', 'Cidade no texto da página só com aprovação; página de 68605 à venda disputa a mesma busca', []),
    # bloco "Onda 3 da Pós, lote A", travas: `matriz` corrigida no site em 68628, 68617, 68636 e 68609
    ('matriz', ['68628', '68617', '68636', '68609'], 'outro', 'Campo matriz corrigido no site antes da subida', ['pagina']),
    # bloco "Onda 3 da Pós, lote A", travas: campos titulo e apoio aceitos pela plataforma
    ('plataforma', ABRIL, 'ferramenta', 'Campos titulo e apoio aceitos pela plataforma', ['pagina']),
    # bloco "Onda 3 da Pós, lote A", travas: quem grava os Reels (OU15)
    ('OU15', ABRIL, 'outro', 'Quem grava os Reels e com que custo', []),
]
for ref, alvo, tp, desc, bl in TRAVAS:
    for c in alvo: add(c, ref, desc, PC1, tipo=tp, bloq=bl)

# Pendências específicas que vêm de texto corrido (não de tabela)
ESPECIFICAS = {
    # plano da onda 2, seção 1 ("Páginas"): 68615 diz ter reconhecimento ligado ao órgão regulador e "referência nacional"
    '68615': [('OB1', 'conformidade', 'Página no ar com frase de certificação que a squad não repete e "referência nacional"', [], ['pagina'], PL2)],
    # plano da onda 3, seção 4.8: ficha diz 26 módulos e o cronograma lista 24
    '68609': [('ficha', 'divergencia', 'Ficha diz 26 módulos e o cronograma lista 24', ['modulos'], [], PL3)],
    # docs/execucao-2026-10-26.md, decisão 19
    '698': [('decisão 19', 'data', 'Página ainda mostra 2027; a campanha segue com 28 e 29/11/2026 e a correção do site continua pedida', [], [], B)],
    # decisões do cmo sobre a regra 8 (arquivos próprios)
    '68632': [('regra 8', 'data', 'Módulo presencial antes do 3º: sem OU3, nada pós-início e mídia parando na véspera do início (decisão do cmo)', ['kit.entregas[*]'], ['anuncio'], 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-decisao-68632.md')],
    '359': [('regra 8', 'data', 'Módulo 2 presencial antes do 3º: regra 8 (decisão do cmo); data só no site', ['inicio'], ['anuncio'], 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-decisao-333-359.md')],
    # B2: decisão 13 e diário (a página 623 mostra 01 e 02/08/2026)
    '623': [('decisão 13', 'link', 'Página com data de início errada; nenhuma campanha nova aponta para ela até a correção no site', [], ['anuncio', 'peca_final'], B)],
}
for c in '68640 68642 68644'.split():   # docs/execucao-2026-10-26.md, decisão 20
    ESPECIFICAS.setdefault(c, []).append(('decisão 20', 'outro', 'Prova presencial em Goiânia: a página mostra endereço de São Paulo; local de Goiânia a confirmar', [], ['peca_final'], B))
for c in GRUPOS_INICIADOS:              # B7: plano geral, 2.1 item 3
    ESPECIFICAS.setdefault(c, []).append(('2.1 item 3', 'outro', 'Política de entrada em grupo de estudos já iniciado', [], [], PLANO_GERAL + ', seção 2.1'))

# ---------- perguntas e aprovações de docs/pendencias-camada-1.md ----------
T_PC1 = ler(PC1)
PERG = {}
for t in tabelas(trecho(T_PC1, r'^## 2\. ')):
    for r in t: PERG[r.get('Código')] = r.get('Pergunta', '')
APR_R = []
for t in tabelas(trecho(T_PC1, r'^## 1\. ')):
    for r in t:
        if re.fullmatch(r'R\d+', r.get('Código', '')): APR_R.append(r)

# ---------- aprovações a partir das tabelas de pedidos ----------
def data_arq(p):
    m = re.search(r'(\d{4}-\d{2}-\d{2})', p)
    return m.group(1) if m else HOJE
VERBA_TXT = 'R$ 2.000,00 por turma, decisão 15'
def apr(ref, o_que, por_que, quanto, efeito, desfazer, pedido_em):
    return {'ref': limpa(ref, 120), 'o_que': limpa(o_que, 400), 'por_que': limpa(por_que, 400), 'quanto': limpa(quanto, 400),
            'efeito_esperado': limpa(efeito, 400), 'como_desfazer': limpa(desfazer, 400), 'status': 'pendente',
            'pedido_em': pedido_em, 'decidido_em': None, 'decidido_por_papel': None}
def linhas_pedido(arq, titulo):
    out = []
    for t in tabelas(trecho(ler(arq), titulo)):
        if not t or 'O que' not in t[0] or '#' not in t[0]: continue   # só as tabelas de pedidos
        prev = {}
        for r in t:
            r = dict(r)
            for k, v in r.items():
                if v.startswith('idem') and k in prev: r[k] = prev[k] + v[4:]
            prev = r; out.append(r)
    return out
APROV = {}
def add_apr(alvos, a):
    for c in alvos:
        lst = APROV.setdefault(c, [])
        ja = {t for x in lst for t in x['ref'].split(' e ')}
        novos = [t for t in a['ref'].split(' e ') if t not in ja]   # código que o item já tem não se repete
        if novos: lst.append(dict(a, ref=' e '.join(novos)))

# onda 1 (cmo-pos-2026-10-26.md, seção 8): o pedido vale para a turma com que o texto começa; senão, para as 6
for r in linhas_pedido(PL1, r'^## 8\. '):
    m = re.match(r'(\d{3,5})\b', r['O que'])
    add_apr([m.group(1)] if m and m.group(1) in ONDA1_POS else ONDA1_POS,
            apr(r['#'], r['O que'], r['Por que'], r['Quanto'], r['Efeito esperado'], r['Como desfazer'], data_arq(PL1)))
# onda 2 (seção 9): todas as 5 turmas de março
for r in linhas_pedido(PL2, r'^## 9\. '):
    add_apr(MARCO, apr(r['#'], r['O que'], r['Por que'], r['Quanto'], r['Efeito esperado'], r['Como desfazer'], data_arq(PL2)))
# onda 3 (seção 9): alvo por pedido, pelo texto da coluna "O que" (OC1-A: 8 páginas de abril; OC1-B e OC7: maio;
# OC8: 662; os demais, "kit mínimo das 18 turmas")
ALVO_ONDA3 = {'OC1-A': ABRIL, 'OC1-B': MAIO, 'OC7': MAIO, 'OC8': ['662']}
for r in linhas_pedido(PL3, r'^## 9\. '):
    add_apr(ALVO_ONDA3.get(r['#'], ABRIL + MAIO), apr(r['#'], r['O que'], r['Por que'], r['Quanto'], r['Efeito esperado'], r['Como desfazer'], data_arq(PL3)))
CODS_APR = {x['ref'] for l in APROV.values() for x in l}
# blocos de docs/pendencias-camada-1.md (pedidos que os planos não trazem em tabela própria)
for titulo, alvo in ((r'^## Onda 2 da Pós', MARCO), (r'^## Mídia paga das turmas', MARCO + ABRIL + ['662']), (r'^## Onda 3 da Pós, lote A', ABRIL)):
    for t in tabelas(trecho(T_PC1, titulo)):
        for r in t:
            refs = [x.strip() for x in re.split(r',\s*|\s+e\s+(?=[A-Z])', r['Pedido'])]
            refs = [x for x in refs if x and x not in CODS_APR]   # o que já veio da tabela do plano não se repete
            if not refs: continue
            cs = cods(r['O que aprovar'])
            alvo_r = cs if cs and not (set(cs) & set(alvo)) else alvo
            # no bloco da mídia de março e abril, pedido que só fala de abril vale para as turmas de abril e a 662
            if 'abril' in r['O que aprovar'] and 'março' not in r['O que aprovar'] and set(alvo) > set(ABRIL): alvo_r = ABRIL + ['662']
            midia = '11-midia-paga' in r.get('Arquivo', '') or re.match(r'(AMP|AGP|MO|OM|PP)', refs[0])
            add_apr(alvo_r, apr(' e '.join(refs), r['O que aprovar'], 'conforme o plano da onda (' + r.get('Arquivo', '') + ')',
                                VERBA_TXT if midia else 'conforme o plano da onda', 'conforme o plano da onda', 'conforme o plano da onda', HOJE))
# seção 1 de docs/pendencias-camada-1.md: R2 a R8, para os itens citados (código ou "workshop")
for r in APR_R:
    alvo = cods(r['Pedido'])
    if re.search(r'(?i)workshop', r['Pedido']): alvo = alvo + ['workshop-neuro']
    for c in alvo:
        add_apr([c], apr(r['Código'], r['Pedido'], 'pedido do fechamento da camada 1 (' + PC1 + ', seção 1)',
                         VERBA_TXT if (c in ONDA1_POS + MARCO + POS_ONDA3) and re.search(r'(?i)mídia|verba|anúncio', r['Pedido']) else '[CONFIRMAR]',
                         r.get('Efeito se aprovar', ''), '[CONFIRMAR]', HOJE))
# B1: A4 do plano geral (seção 8) para as 6 turmas iniciadas com campanha ativa
for r in linhas_pedido(PLANO_GERAL, r'^## 8\. '):
    if r['#'] == 'A4':
        add_apr(INICIADAS_ATIVAS, apr('A4', r['O que'], r['Por que'], r['Quanto'], r['Efeito esperado'], r['Como desfazer'], data_arq(PLANO_GERAL)))

# ---------- B14: saídas tiradas de uso pelo diário (27/10, integração do branch) ----------
A_REVISAR = set()
for l in ler(DIARIO).split('\n'):
    m = re.search(r'ficam como rascunho a revisar, sem uso em peça: (.*)', l)
    if m:
        for seg in m.group(1).split(';'):
            for nm in re.split(r',\s*|\s+e\s+', seg.split('(')[0]):
                nm = nm.strip(' |')
                if nm: A_REVISAR.add(nm)
def a_revisar(caminho):
    b = os.path.basename(caminho)
    return any(b in (n + '.md', n + '-2026-10-26.md') for n in A_REVISAR)

# ---------- kit ----------
KEYS_POS = [('pagina', 'Página da turma', 1), ('plano_8_canais', 'Plano dos 8 canais', 1), ('plano_de_midia', 'Plano de mídia', 1),
            ('posts_organicos', 'Posts orgânicos', 6), ('criativos', 'Criativos de anúncio', 3), ('post_por_docente', 'Post por docente', None),
            ('whatsapp', 'Mensagens de WhatsApp', 4), ('email', 'E-mails', 2), ('roteiro_video', 'Roteiro de vídeo curto', 1)]
RESP = {'pagina': ['landing-page', 'seo-on-page'], 'plano_8_canais': ['cmo'], 'plano_de_midia': ['gestor-de-midia'], 'posts_organicos': ['posts-sociais'],
        'criativos': ['criativos-de-anuncio'], 'post_por_docente': ['autoridade-docente'], 'whatsapp': ['copy-de-mensagens'], 'email': ['copy-de-mensagens'],
        'roteiro_video': ['tiktok'], 'mensagem_convite': ['copy-de-mensagens'], 'mensagem_vespera': ['copy-de-mensagens'], 'mensagem_do_dia': ['copy-de-mensagens'],
        'email_convite': ['copy-de-mensagens'], 'criativos_com_utm': ['criativos-de-anuncio'], 'whatsapp_prazos_do_edital': ['copy-de-mensagens'],
        'email_prazos_do_edital': ['copy-de-mensagens'], 'campanha_unica': ['estrategia-de-campanha']}
def entrega(k, nome, q, status='a_fazer', qa='pendente', arquivo=None, regra=None, prazo=None):
    return {'chave': k, 'entrega': nome, 'quantidade_minima': q, 'regra_quantidade': regra, 'autorizados': None, 'responsavel': list(RESP.get(k, [])),
            'prazo': prazo, 'status': status, 'qa': qa, 'arquivo': arquivo, 'secao': None, 'ref_aprovacao': None}
def arquivos_onda(onda):
    d = '2026-10-27-' + onda
    return {'pagina': f'saidas/08-conversao/landing-page-pos-{d}.md', 'plano_8_canais': f'saidas/02-estrategia-e-posicionamento/cmo-pos-{d}.md',
            'plano_de_midia': 'saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md', 'posts_organicos': f'saidas/05-social-e-comunidade/posts-sociais-pos-{d}.md',
            'criativos': 'saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md', 'post_por_docente': f'saidas/05-social-e-comunidade/autoridade-docente-pos-{d}.md',
            'whatsapp': f'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-{d}.md', 'email': f'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-{d}.md',
            'roteiro_video': f'saidas/12-video-e-audio/tiktok-pos-{d}.md'}
COPY_ONDA1 = 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md'
def kit_pos(cod):
    ent = []
    if cod in MARCO: arq = arquivos_onda('onda2'); est = 'aguardando_aprovacao'; qa = 'aprovado'
    elif cod in ABRIL: arq = arquivos_onda('onda3'); est = 'aguardando_aprovacao'; qa = 'aprovado'
    elif cod in MAIO or cod == '662': arq = {}; est = 'a_fazer'; qa = 'pendente'
    elif cod in ONDA1_POS: arq = {}; est = 'inventario_pendente'; qa = 'pendente'
    else: arq = {}; est = 'nao_aplicavel'; qa = 'pendente'
    for k, nome, q in KEYS_POS:
        e = entrega(k, nome, q, est, qa, arq.get(k), '1_por_docente_autorizado' if q is None else None)
        if cod == '662': e['status'] = 'a_fazer'; e['arquivo'] = None
        if cod in MAIO and k in ('plano_8_canais', 'plano_de_midia'):
            e['status'] = 'aguardando_aprovacao'; e['qa'] = 'aprovado'
            e['arquivo'] = PL3 if k == 'plano_8_canais' else 'saidas/11-midia-paga/gestor-de-midia-pos-2026-10-27-onda3.md'
        if cod in ONDA1_POS:
            if k in ('whatsapp', 'email'): e.update(status='aguardando_aprovacao', qa='aprovado', arquivo=COPY_ONDA1)
            if k == 'plano_8_canais': e.update(status='aguardando_aprovacao', qa='aprovado', arquivo=PL1)
            if k == 'plano_de_midia': e.update(status='aguardando_aprovacao', qa='aprovado', arquivo='saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md')
        ent.append(e)
    return ent
# B12: acréscimos e inventário da onda 1 (plano geral, seção 4, "Situação especial da onda 1" e "Prazos da onda 1";
# mesmos 3 acréscimos do exemplo 707 do arquiteto-de-fluxos, seção 1.6)
def acrescimo(k, nome, qtd, resp, prazo, status='a_fazer', qa='pendente', arquivo=None):
    return {'chave': k, 'entrega': nome, 'quantidade': qtd, 'responsavel': resp, 'prazo': prazo, 'status': status, 'qa': qa,
            'arquivo': arquivo, 'secao': None, 'ref_aprovacao': None}
def acrescimos_onda1(cod):
    return [acrescimo('inventario_do_kit', 'Inventário do que já existe do kit, conferido item por item', 1, ['cmo'], '2026-10-28'),
            # reta final: o diário de 27/10 substitui o arquivo de reta final pelo copy-de-mensagens-pos-onda1 v4, aprovado pelo qa
            acrescimo('whatsapp_reta_final', 'Mensagens de reta final, sem urgência por vagas, porque não há número de vagas', None, ['copy-de-mensagens'],
                      '2026-10-28' if cod in ('707', '68604') else None, 'aguardando_aprovacao', 'aprovado', COPY_ONDA1),
            acrescimo('pausa_e_relatorio_final', 'Pedido de pausa das campanhas e relatório final', 2, ['cmo', 'gestor-de-midia'], None)]

# ---------- canais (seção 5 do plano geral; ondas 2 e 3 da Pós pelos planos de onda) ----------
CANAIS_LINHA = {
    'pos': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'teste', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'livres': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'eventos': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'graduacao': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'teste', 'x': 'fora', 'podcast': 'fora'},
}
POS_ONDA23 = {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'fora', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'}
ORDEM_CANAIS = ['instagram', 'facebook', 'tiktok', 'x', 'linkedin', 'youtube', 'podcast', 'whatsapp']
def canais(linha, cod, rec='planejar'):
    if rec != 'planejar':   # B4: fora do recorte, os 8 canais ficam "fora"
        return [{'canal': c, 'estado': 'fora', 'motivo': 'fora do recorte do plano (seção 2.4)', 'natureza': 'proposta_do_cmo'} for c in ORDEM_CANAIS]
    if linha == 'pos' and (cod in MARCO or cod in POS_ONDA3):
        base, fonte = POS_ONDA23, (PL2 if cod in MARCO else PL3) + ', seção 5 (plano da onda)'
    else:
        base, fonte = CANAIS_LINHA[linha], PLANO_GERAL + ', seção 5'
    return [{'canal': c, 'estado': base[c], 'motivo': 'ver ' + fonte, 'natureza': 'proposta_do_cmo'} for c in ORDEM_CANAIS]

# ---------- montagem ----------
def status_norm(s):
    s0 = (s or '').lower()
    if s0.startswith('aberto (contínuo)') or 'contínuo' in s0: return 'aberto (contínuo)'
    if s0.startswith('aberto'): return 'aberto'
    if s0.startswith('verificar'): return 'verificar'
    if s0.startswith('sem venda'): return 'sem venda'
    if s0.startswith('encerrado'): return 'encerrado'
    if s0.startswith('sem página'): return 'sem página'
    return '[CONFIRMAR]'

def modalidade_norm(m, tipo):
    m0 = sem_acento((m or '').lower())
    if tipo == 'prova_de_bolsa': return 'presencial'  # decisão 20 do CEO, 27/10/2026
    if 'semi' in m0: return 'semipresencial'
    if 'grava' in m0: return 'gravacao'
    if 'ead' in m0: return 'ead'
    if 'online' in m0 or 'on-line' in m0 or 'ao vivo' in m0: return 'online'
    if 'presencial' in m0: return 'presencial'
    return '[CONFIRMAR]'

def preco_estr(t):
    # B5: só grava quando parcelas x valor da parcela bate com o total do texto (até R$ 0,01 por parcela)
    m = re.search(r'(\d+)x de R\$ ([\d.]+,\d{2})', t or '')
    tot = re.search(r'R\$ ([\d.]+,\d{2}) (?:no cartão|à vista)', t or '')
    mat = re.search(r'matrícula R\$ ([\d.]+,\d{2})', t or '')
    if not m or not tot: return None
    num = lambda s: float(s.replace('.', '').replace(',', '.'))
    n, v, total = int(m.group(1)), num(m.group(2)), num(tot.group(1))
    if abs(n * v - total) > 0.01 * n + 1e-9: return None
    return {'moeda': 'BRL', 'parcelas': n, 'valor_parcela': v, 'total': total, 'matricula': num(mat.group(1)) if mat else None}

def ficha_path(cel):
    m = re.search(r'\((cursos/[^)]+)\)', cel or '')
    return 'contexto/' + m.group(1) if m else None

def modulos_da_ficha(p):
    if not p or not os.path.exists(p): return None
    m = re.search(r'\*\*Módulos:\*\*\s*(\d+)', ler(p))
    return int(m.group(1)) if m else None

def pagina_da_ficha(p):
    if not p or not os.path.exists(p): return None
    m = re.search(r'https://faculdade\.ufape\.com\.br/\S+', ler(p))
    return m.group(0).rstrip(').,') if m else None

def nome_padrao(nome, tipo):
    if tipo == 'pos':
        return nome if nome.startswith('Pós-graduação em') else '[CONFIRMAR]'
    return nome

def nulos(j, caminhos):
    out = []
    for c in caminhos:
        v = j
        for k in c.split('.'):
            v = v.get(k) if isinstance(v, dict) else None
        if v is None: out.append(c)
    return out

ORDEM = ['versao_schema', 'id', 'revisao', 'revisao_aprovada', 'estado_do_arquivo', 'substituido_por', 'gerado_em', 'atualizado_em', 'fontes',
         'codigo', 'linha', 'linha_origem', 'tipo', 'nome_no_site', 'nome_padrao', 'slug_sugerido', 'aliases', 'pagina_oficial', 'area', 'recorte',
         'motivo_do_recorte', 'onda', 'modo_de_venda', 'grupo_de_campanha', 'gut', 'relacionados', 'local', 'modalidade', 'modalidade_normalizada',
         'turma', 'carga_horaria', 'modulos', 'inicio', 'fonte_da_data', 'dias_ate_inicio', 'fim_das_inscricoes', 'preco_texto_site',
         'preco_estruturado', 'condicoes_especiais', 'status_catalogo', 'status_catalogo_texto', 'vagas', 'equipe', 'prova_de_bolsa', 'graduacao',
         'evento', 'status_midia', 'kit', 'canais', 'arquivos_por_camada', 'metas', 'numeros_agregados', 'pendencias', 'aprovacoes', 'historico', 'resumo']
ORDEM_FONTES = ['catalogo', 'data_catalogo', 'catalogo_linha_literal', 'ficha', 'ficha_editais', 'ficha_lida_em', 'contexto_da_linha',
                'campos_so_na_ficha', 'visao_de_campanhas', 'plano', 'auditorias']
ORDEM_KIT = ['template', 'variacao', 'escopo', 'entregas', 'acrescimos', 'inventario']
def ordena(j):  # R13: chaves na ordem do modelo 1.5
    j['fontes'] = {k: j['fontes'][k] for k in ORDEM_FONTES if k in j['fontes']}
    j['kit'] = {k: j['kit'][k] for k in ORDEM_KIT if k in j['kit']}
    assert set(j) <= set(ORDEM), set(j) - set(ORDEM)
    return {k: j[k] for k in ORDEM if k in j}

def fecha(j, pends):
    # B12: id da pendência = "<codigo>-p01" (itens sem código usam o id do arquivo); B3: resumo calculado
    pre = j['codigo'] if j['codigo'] != 'sem-codigo' else j['id']
    for i, p in enumerate(pends, 1): p['id'] = f'{pre}-p{i:02d}'
    j['pendencias'] = pends
    ab = [p for p in pends if p['resolvida_em'] is None]
    j['resumo'] = {'pendencias_abertas': len(ab), 'bloqueado': any('peca_final' in p['bloqueia'] for p in ab)}
    return ordena(j)

def padroes(j, pends, fonte_kit):
    # B13: pendências padrão que explicam os null por origem vazia nos itens do recorte
    tipo = j['tipo']
    p11 = nulos(j, ['metas.matriculas_alvo', 'metas.cpl_maximo', 'metas.custo_por_matricula_maximo', 'metas.verba',
                    'numeros_agregados.leads', 'numeros_agregados.inscricoes', 'numeros_agregados.matriculas', 'numeros_agregados.verba_gasta',
                    'vagas.vagas_restantes'])
    if tipo not in ('pos', 'prova_de_bolsa', 'graduacao'): p11 += nulos(j, ['vagas.turma_minima', 'vagas.vagas_ofertadas'])
    if j['metas']['fonte'] == '[CONFIRMAR]': p11.append('metas.fonte')
    junta(pends, pend('P11', 'meta_ou_verba', 'Sem metas de custo, números agregados e vagas restantes por turma; nenhuma peça fala em urgência por vagas',
                      '[CONFIRMAR]', p11, ['meta'], PLANO_GERAL + ', seção 7'))
    if tipo == 'pos' and j['vagas']['vagas_ofertadas'] is None:
        junta(pends, pend('OU4', 'meta_ou_verba', 'Vagas totais e restantes da turma ainda não informadas pela Ufape (só números somados)', '[CONFIRMAR]',
                          ['vagas.vagas_ofertadas'], [], PL1 + ', seção 3'))
    if tipo == 'pos' and j['modulos'] is None:
        junta(pends, pend('ficha', 'outro', 'Número de módulos não encontrado na ficha', '[CONFIRMAR]', ['modulos'], [], CAT))
    if j['equipe'] is not None or tipo in ('workshop', 'simposio'):
        cp = nulos(j, ['equipe.coordenadores_na_ficha', 'equipe.docentes_na_ficha', 'equipe.autorizacoes_de_imagem_registradas']) if j['equipe'] else []
        if 'evento' in j: cp += ['evento.palestrantes.' + k for k, v in j['evento']['palestrantes'].items() if v is None]
        cp += [f'kit.entregas[{i}].autorizados' for i, e in enumerate(j['kit']['entregas']) if e['regra_quantidade'] and e['autorizados'] is None]
        if cp:
            junta(pends, pend('P13', 'autorizacao', 'Autorização de imagem e citação registrada pela Ufape para todos (decisões 8 e 10); falta o cmo lançar as contagens da ficha',
                              '[CONFIRMAR autorização]', cp, [], B + ', decisões 8 e 10'))
    cit = {c for p in pends for c in p['campos']}
    if j['fim_das_inscricoes'] is None and j['modo_de_venda'] == 'com_data' and 'fim_das_inscricoes' not in cit:
        # mesmo tratamento do exemplo 707 do arquiteto-de-fluxos (seção 1.6): o catálogo e a ficha não trazem o fim das inscrições
        junta(pends, pend('fim das inscrições', 'data', 'Fim das inscrições não consta no catálogo nem na ficha; sem ele o pedido de pausa fica sem data', '[CONFIRMAR]',
                          ['fim_das_inscricoes'], [], j['fontes']['ficha'] or CAT))
    pr = [f'kit.entregas[{i}].prazo' for i, e in enumerate(j['kit']['entregas']) if e['prazo'] is None]
    pr += [f'kit.acrescimos[{i}].prazo' for i, e in enumerate(j['kit']['acrescimos']) if e['prazo'] is None]
    pr += [f'kit.acrescimos[{i}].quantidade' for i, e in enumerate(j['kit']['acrescimos']) if e['quantidade'] is None]
    if pr:
        junta(pends, pend('prazo do kit', 'kit', 'Prazo de cada entrega ainda não lançado no JSON; vale o calendário do plano da onda', '[CONFIRMAR]', pr, [], fonte_kit))

res = []
for r in itens:
    sec = r['_secao']; linha, tipo = secoes[sec]
    cod = re.sub(r'\D', '', r.get('Código', '')) or 'sem-codigo'
    nome = r.get('Curso', '')
    aliases = []
    if sec == '9':
        tipo = 'workshop' if 'Workshop' in nome else 'simposio'
    if sec == '5' and re.match(r'Mini [Cc]urso', nome): tipo = 'minicurso'           # B12
    if sec == '4' and 'Aprimoramento' in nome: tipo = 'aprimoramento'                 # B12
    linha_origem = 'catalogo'
    if cod in MODALIDADE_DO_EVENTO:   # B9: 68634 é a modalidade transmitida e gravada do workshop (plano geral, 2.1 item 7)
        linha, tipo, linha_origem = 'eventos', 'workshop', 'plano'
    if sec == '9' and cod == 'sem-codigo' and 'Neuromonitoriza' in nome:
        chave = 'workshop-neuro'; ident = 'eventos-workshop-neuromonitorizacao-2026-11-20'
        m = re.search(r'\s*\(na planilha: ([^)]+)\)', nome)
        if m: aliases = [m.group(1).strip()]; nome = nome.replace(m.group(0), '')   # B9: nome da planilha vai para aliases
    elif cod == 'sem-codigo': chave = 'paciente-grave' if 'Paciente Grave' in nome else None; ident = f'{linha}-sem-codigo-{slug(nome)[:60]}'
    else: chave = cod; ident = f'{"livres" if cod in MODALIDADE_DO_EVENTO else linha}-{cod}'   # o id nunca muda (arquiteto, 2.1)
    st = status_norm(r.get('Status')); ini = data_iso(r.get('Início', ''))
    fonte_txt = (r.get('Fonte') or '').lower()
    fonte_data = 'planilha' if 'planilha' in fonte_txt else ('site' if 'site' in fonte_txt else ('pagina_do_evento' if chave == 'workshop-neuro' else 'ausente'))
    if sec == '3' and ini: fonte_data = 'site'
    area = AREAS.get(chave) if chave else None
    no_recorte = area is not None
    if no_recorte and st in ('aberto', 'aberto (contínuo)'): rec = 'planejar'
    elif chave in FORA_COMO_PENDENCIA: rec = 'pendencia'                               # B10
    elif st in ('sem venda', 'encerrado'): rec = 'historico'
    else: rec = 'pendencia'
    if rec == 'planejar':
        onda = 1 if (chave in ONDA1 or tipo == 'prova_de_bolsa' or chave == 'workshop-neuro') else 2 if (chave in ONDA2 or st == 'aberto (contínuo)') else 3 if chave in ONDA3 else None
    else: onda = None
    modo = 'continuo' if st == 'aberto (contínuo)' else 'com_data'
    g = None
    if rec == 'planejar':
        for cods_, gg, uu, tt, mot in GUT:
            alvo = (cods_ == 'PROVAS' and tipo == 'prova_de_bolsa') or (cods_ == 'CONTINUOS' and modo == 'continuo') or (chave in cods_.split())
            if alvo: g = {'g': gg, 'u': uu, 't': tt, 'total': gg * uu * tt, 'motivo': mot, 'natureza': 'avaliacao_do_agente', 'fonte': PLANO_GERAL + ', seção 3'}; break
    fp = ficha_path(r.get('Ficha'))
    preco = r.get('Preço e condições (site)') or r.get('Preço (site)') or ''
    dias = (datetime.date.fromisoformat(ini) - datetime.date.fromisoformat(HOJE)).days if (ini and modo == 'com_data' and rec == 'planejar') else None  # B10
    pends = [pend('P1', 'certificacao', 'Texto oficial de certificação ainda não aprovado pela regulação; nenhuma peça afirma certificação', '[CONFIRMAR]', [], ['certificacao'], PLANO_GERAL + ', seção 7')]
    if tipo == 'pos' and rec == 'planejar':
        pends.append(pend('P2', 'conformidade', 'Página no ar com frase de certificação ligada ao órgão regulador e turma mínima diferente de 15; correção pedida no site', '[CONFIRMAR]', [], ['pagina'], PLANO_GERAL + ', seção 7'))
        pends.append(pend('decisão 16', 'preco_ou_condicao', 'Valor da inscrição (R$ 260,00 informado) diferente da matrícula do site; nenhuma peça cita o valor (U11)', '[CONFIRMAR]', ['preco_estruturado.matricula'], ['preco'], B))
        pends.append(pend('OB1', 'conformidade', 'Endereço da política de privacidade do formulário', '[CONFIRMAR]', [], ['pagina'], 'saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md'))
    if tipo == 'prova_de_bolsa' and rec == 'planejar':   # B4
        pends.append(pend('decisão 14', 'kit', 'Peças das provas suspensas até nova ordem; textos antigos tratam a prova como online e precisam de varredura para presencial (decisão 20)', '[CONFIRMAR]', ['kit.entregas[*]'], ['peca_final'], B))
        for u, campos in (('U1', ['prova_de_bolsa.bolsas_previstas', 'prova_de_bolsa.nota_de_corte_texto', 'prova_de_bolsa.prazo_de_matricula_apos_resultado', 'prova_de_bolsa.divulgacao_do_resultado']),
                          ('U3', ['fim_das_inscricoes', 'prova_de_bolsa.horario_texto']), ('U4', ['prova_de_bolsa.turma_de_destino.codigo'])):
            pends.append(pend(u, 'regra_de_bolsa', PERG.get(u, '[CONFIRMAR]'), '[CONFIRMAR]', campos, [], PC1 + ', seção 2'))
    if linha == 'livres' and rec == 'planejar':
        pends.append(pend('decisão 14', 'kit', 'Cursos Livres ficam por último na ordem de prioridade; kit ainda não produzido', '[CONFIRMAR]', ['kit.entregas[*]'], [], B))
    for ref, tp, desc, campos, bloq, fonte in ESPECIFICAS.get(chave, []):
        junta(pends, pend(ref, tp, desc, '[CONFIRMAR]', campos, bloq, fonte))
    for p in POR_ITEM.get(chave, []):
        junta(pends, dict(p, campos=list(p['campos']), bloqueia=list(p['bloqueia'])))
    if cod in MODALIDADE_DO_EVENTO:   # B9: P9 do plano geral (carga horária do produto 68634 na loja e local "Saiba Mais")
        junta(pends, pend('P9', 'divergencia', 'Modalidade transmitida e gravada do workshop: carga horária de 24 h na loja contra 16 h oficiais, sem data e local "Saiba Mais" no catálogo; correção pedida no site',
                          '[CONFIRMAR]', ['carga_horaria', 'local', 'modalidade_normalizada', 'evento.data_inicio', 'evento.formato', 'evento.horario_texto'], ['peca_final'],
                          PLANO_GERAL + ', seção 7 (P9) e 2.1 item 7'))
    if chave == 'workshop-neuro':     # B9: U9 de docs/pendencias-camada-1.md
        junta(pends, pend('U9', 'data', PERG.get('U9', '[CONFIRMAR]'), '[CONFIRMAR]', ['fim_das_inscricoes', 'evento.cupom', 'condicoes_especiais[0].validade'], [], PC1 + ', seção 2'))
    if not ini and modo == 'com_data' and rec == 'planejar':
        junta(pends, pend('R5', 'data', 'Data de início ausente no catálogo', '[CONFIRMAR]', ['inicio'], ['data'], CAT))
    # ---------- kit ----------
    if tipo == 'pos':
        kit = {'template': 'templates/kit-de-lancamento-pos.md', 'variacao': None, 'escopo': 'item', 'entregas': kit_pos(chave) if rec == 'planejar' else [], 'acrescimos': []}
        if rec == 'planejar' and chave in ONDA1_POS:   # B12
            kit['acrescimos'] = acrescimos_onda1(chave)
            kit['inventario'] = {'situacao': 'pendente', 'prazo': '2026-10-28', 'responsavel': 'cmo'}
    elif tipo == 'prova_de_bolsa':
        kit = {'template': None, 'variacao': None, 'escopo': 'grupo', 'acrescimos': [],
               'entregas': [entrega('campanha_unica', 'Campanha única das provas de 27/11', 1, 'revisar_por_mudanca', 'pendente', 'saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md')] if rec == 'planejar' else []}
    elif chave == 'workshop-neuro':   # B9: as 7 chaves do template na variação workshop (esquema, 1.4)
        POSTS_EV = 'saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md'
        COPY_EV = 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md'
        kit = {'template': 'templates/kit-de-lancamento-evento.md', 'variacao': 'workshop', 'escopo': 'item', 'acrescimos': [], 'entregas': [
            entrega('pagina', 'Página do evento (página própria da Ufape, campanhas apontam para ela)', 1, 'inventario_pendente', 'pendente', fp),
            entrega('posts_organicos', 'Posts orgânicos', 3, 'aguardando_aprovacao', 'aprovado', POSTS_EV),
            entrega('criativos', 'Criativos de anúncio', 2, 'inventario_pendente', 'pendente', 'saidas/11-midia-paga/criativos-de-anuncio-eventos-2026-10-26.md'),
            entrega('mensagem_convite', 'Mensagem de convite', 1, 'aguardando_aprovacao', 'aprovado', COPY_EV),
            entrega('mensagem_vespera', 'Mensagem de véspera', 1, 'aguardando_aprovacao', 'aprovado', COPY_EV),
            entrega('mensagem_do_dia', 'Mensagem do dia', 1, 'aguardando_aprovacao', 'aprovado', COPY_EV),
            entrega('email_convite', 'E-mail de convite', 1, 'aguardando_aprovacao', 'aprovado', COPY_EV)]}
    elif modo == 'continuo':
        kit = {'template': None, 'variacao': None, 'escopo': 'grupo', 'entregas': [], 'acrescimos': []}
    elif linha == 'livres' and rec == 'planejar':
        kit = {'template': 'templates/kit-de-lancamento-livres.md', 'variacao': None, 'escopo': 'item', 'acrescimos': [], 'entregas': [
            entrega(k, n, q) for k, n, q in [('pagina', 'Página', 1), ('plano_8_canais', 'Plano dos 8 canais', 1), ('posts_organicos', 'Posts orgânicos', 4),
                                             ('criativos', 'Criativos', 2), ('whatsapp', 'WhatsApp', 3), ('email', 'E-mail', 1)]]}
    else:
        kit = {'template': None, 'variacao': None, 'escopo': 'item', 'entregas': [], 'acrescimos': []}
    if tipo == 'pos':
        metas = {'matriculas_alvo': 15 if rec == 'planejar' else None, 'cpl_maximo': None, 'custo_por_matricula_maximo': None,
                 'verba': 2000.00 if rec == 'planejar' else None, 'fonte': 'decisões 15 e 16 do briefing'}
    else:
        metas = {'matriculas_alvo': None, 'cpl_maximo': None, 'custo_por_matricula_maximo': None, 'verba': None, 'fonte': '[CONFIRMAR]'}
    # ---------- arquivos por camada (B14: saídas tiradas de uso entram como "devolvido") ----------
    def camada(agente, caminho, secao):
        return {'agente': agente, 'caminho': caminho, 'secao': secao, 'estado': 'devolvido' if a_revisar(caminho) else 'pendente_de_aprovacao',
                'aprovado_em': None, 'ref_aprovacao': None}
    arqs = {'geral': [{'agente': 'cmo', 'caminho': PLANO_GERAL, 'secao': None, 'estado': 'aprovado', 'aprovado_em': '2026-10-26', 'ref_aprovacao': 'plano aprovado pela pessoa do marketing'}],
            'linha': [], 'area': [], 'curso': [camada(e['responsavel'][0], a, chave) for a, e in
                                               {e['arquivo']: e for e in kit['entregas'] if e.get('arquivo') and e['arquivo'].startswith('saidas/')}.items()]}
    for f in sorted(os.listdir('saidas/02-estrategia-e-posicionamento')):
        if f.startswith('cmo-' + linha + '-2026-10-26'): arqs['linha'].append(camada('cmo', 'saidas/02-estrategia-e-posicionamento/' + f, None))
    if area and linha in ('pos', 'livres'):
        arqs['area'].append(camada('mensagens', f'saidas/02-estrategia-e-posicionamento/mensagens-{linha}-2026-10-26.md', area))
    # ---------- motivo do recorte ----------
    if chave in INICIADAS_ATIVAS:
        motivo = 'pendência urgente: turma iniciada com campanha ativa (plano geral, 2.1 item 2)'
    elif chave in FORA_COMO_PENDENCIA:
        motivo = 'pendência: o plano geral põe o item no mapa como pendência (2.1 item 5 e 2.4)'
    elif cod in MODALIDADE_DO_EVENTO:
        motivo = 'pendência: modalidade transmitida e gravada do workshop, sem data no site (plano geral, 2.1 item 7)'
    else:
        motivo = {'planejar': 'à venda e no recorte do plano geral (seção 2)', 'historico': 'sem venda ou encerrado no catálogo', 'pendencia': 'status do catálogo pede verificação ou o item está fora do recorte'}[rec]
    # ---------- relacionados (B2 e B7) ----------
    relac = []
    for a, b2 in PARES_P7:
        if chave == a: relac.append(b2)
        if chave == b2: relac.append(a)
    relac_obj = []
    def id_de(c):
        if c == 'paciente-grave': return 'eventos-sem-codigo-' + slug('Paciente Grave Multidiciplinar Foco em casos Clinicos')[:60]
        rr = next(x for x in itens if re.sub(r'\D', '', x.get('Código', '')) == c)
        ln = secoes[rr['_secao']][0]
        if c in CONTINUOS and rr['_secao'] == '9': ln = 'eventos'
        return f'{"livres" if c in MODALIDADE_DO_EVENTO else ln}-{c}'
    for c in relac:
        relac_obj.append({'id': id_de(c), 'relacao': 'duplicidade_provavel', 'natureza': '[SUPOSIÇÃO]'})
    if relac:
        junta(pends, pend('P7', 'duplicidade', 'Duplicidade provável com ' + ', '.join(o['id'] for o in relac_obj) + '; a Ufape confirma qual página fica à venda',
                          '[CONFIRMAR]', ['relacionados'], [], PLANO_GERAL + ', seção 7'))
    if cod in MODALIDADE_DO_EVENTO:
        relac_obj.append({'id': 'eventos-workshop-neuromonitorizacao-2026-11-20', 'relacao': 'modalidade_do_mesmo_evento', 'natureza': 'dado'})
    if chave == 'workshop-neuro':
        relac_obj += [{'id': 'livres-' + c, 'relacao': 'modalidade_do_mesmo_evento', 'natureza': 'dado'} for c in MODALIDADE_DO_EVENTO]
    # ---------- status de mídia (B7: P6) ----------
    ini_visao = None
    if chave in P6_VISAO:
        dv = P6_VISAO[chave]
        if len(dv) == 5 and ini: dv = dv + '/' + ini[:4]   # sem ano no plano: ano do início (visão de campanhas de 26/10/2026)
        ini_visao = data_iso(dv)
    j = {'versao_schema': 1, 'id': ident, 'revisao': 1, 'revisao_aprovada': 0, 'estado_do_arquivo': 'ativo', 'substituido_por': None,
         'gerado_em': HOJE, 'atualizado_em': HOJE,
         'fontes': {'catalogo': CAT, 'data_catalogo': DATA_CAT, 'catalogo_linha_literal': r['_literal'].split('| [ficha]')[0].rstrip(), 'ficha': fp, 'ficha_lida_em': None,
                    'campos_so_na_ficha': (['modulos'] if modulos_da_ficha(fp) else []) + (['pagina_oficial'] if pagina_da_ficha(fp) else []),
                    'visao_de_campanhas': {'arquivo': 'docs/visao-de-campanhas-2026-10-26.md', 'data': '2026-10-26'}, 'plano': PLANO_GERAL,
                    'auditorias': ['docs/auditoria-do-catalogo-2026-10-26.md']},
         'codigo': cod, 'linha': linha, 'linha_origem': linha_origem, 'tipo': tipo, 'nome_no_site': nome or '[CONFIRMAR]',
         'nome_padrao': 'Workshop Brasileiro de Neuromonitorização' if chave == 'workshop-neuro' else nome_padrao(nome, tipo),   # B9: decisão 7
         'slug_sugerido': slug(nome) if tipo == 'pos' and nome.startswith('Pós-graduação em') else '[CONFIRMAR]', 'aliases': aliases,
         'pagina_oficial': pagina_da_ficha(fp) or ('[CONFIRMAR]' if st.startswith('aberto') else None),
         'area': {'codigo': area or 'sem_area', 'nome': NOMES_AREA.get(area, '[CONFIRMAR]') if area else '[CONFIRMAR]', 'natureza': 'plano_do_cmo'},
         'recorte': rec, 'motivo_do_recorte': motivo,
         'onda': onda, 'modo_de_venda': modo,
         'grupo_de_campanha': 'provas-de-bolsa-2026-11-27' if (tipo == 'prova_de_bolsa' and rec == 'planejar') else (f'sempre-ligado-{area}' if modo == 'continuo' and area and rec == 'planejar' else None),
         'gut': g, 'relacionados': relac_obj,
         'local': r.get('Local') or '[CONFIRMAR]', 'modalidade': r.get('Modalidade') or ('PROVA PRESENCIAL' if tipo == 'prova_de_bolsa' else '[CONFIRMAR]'),
         'modalidade_normalizada': 'online' if cod in MODALIDADE_DO_EVENTO else modalidade_norm(r.get('Modalidade'), tipo),
         'turma': (r.get('Turma') or '[CONFIRMAR]') if tipo == 'pos' else None,
         'carga_horaria': (r.get('CH') or '[CONFIRMAR]') if tipo != 'prova_de_bolsa' else None, 'modulos': modulos_da_ficha(fp) if tipo == 'pos' else None,
         'inicio': ini, 'fonte_da_data': fonte_data if ini else 'ausente', 'dias_ate_inicio': dias, 'fim_das_inscricoes': None,
         'preco_texto_site': preco or '[CONFIRMAR]', 'preco_estruturado': preco_estr(preco), 'condicoes_especiais': [],
         'status_catalogo': st, 'status_catalogo_texto': r.get('Status') or '[CONFIRMAR]',
         'vagas': {'turma_minima': 15 if tipo == 'pos' else None, 'vagas_ofertadas': None, 'vagas_restantes': None},
         'equipe': None if (tipo in ('prova_de_bolsa', 'workshop', 'simposio') or not fp) else {'coordenadores_na_ficha': None, 'docentes_na_ficha': None, 'autorizacoes_de_imagem_registradas': None},
         'status_midia': {'campanha': MIDIA.get(chave, 'nao_consta'), 'formatos': [], 'cinco_angulos': 'nao_consta', 'vinculo_com_a_visao': 'provavel' if chave in MIDIA else 'nenhum',
                          'inicio_na_visao': ini_visao, 'divergencia_de_data': bool(ini_visao and ini_visao != ini), 'fonte': 'docs/visao-de-campanhas-2026-10-26.md', 'lido_em': '2026-10-26'},
         'kit': kit, 'canais': canais(linha, chave, rec), 'arquivos_por_camada': arqs, 'metas': metas,
         'numeros_agregados': {'leads': None, 'inscricoes': None, 'matriculas': None, 'verba_gasta': None, 'lido_em': None},
         'aprovacoes': APROV.get(chave, []) if rec == 'planejar' or chave in INICIADAS_ATIVAS else [],
         'historico': [{'revisao': 1, 'em': HOJE, 'campo': '*', 'de': None, 'para': 'criação', 'motivo': 'versão 1 do mapa, gerada do catálogo e das saídas aprovadas', 'origem': 'gerador do orquestrador sobre o plano do cmo', 'aplicado_por': 'orquestrador'}]}
    if tipo == 'prova_de_bolsa':
        j['prova_de_bolsa'] = {'data_da_prova': ini, 'horario_texto': '[CONFIRMAR]', 'formato': 'presencial', 'local_texto': r.get('Local') or '[CONFIRMAR]',
                               'nota_de_corte_texto': '[CONFIRMAR]', 'turma_de_destino': {'codigo': '[CONFIRMAR]', 'sugestao_do_plano': None, 'natureza_da_sugestao': '[SUPOSIÇÃO]'},
                               'bolsas_previstas': None, 'prazo_de_matricula_apos_resultado': '[CONFIRMAR]', 'divulgacao_do_resultado': '[CONFIRMAR]', 'minimo_para_confirmar_turma': 15}
    if tipo in ('workshop', 'simposio'):
        ev = {'subtipo': tipo, 'data_inicio': ini, 'data_fim': None, 'horario_texto': '[CONFIRMAR]',
              'formato': 'gravado' if modo == 'continuo' else '[CONFIRMAR]', 'modalidades': [], 'carga_horaria_oficial': '[CONFIRMAR]', 'cupom': None,
              'pagina_oficial': pagina_da_ficha(fp) or '[CONFIRMAR]', 'destino_das_campanhas_pagas': '[CONFIRMAR]',
              'palestrantes': {'confirmados_na_ficha': None, 'convidados_a_definir': None, 'autorizacoes_de_imagem_registradas': None}}
        if chave == 'workshop-neuro' or cod in MODALIDADE_DO_EVENTO:
            # decisão 6 (16 h; campanhas para a página neuro-summit) e catálogo, seção 9
            ev.update(carga_horaria_oficial='16 h', destino_das_campanhas_pagas='https://faculdade.ufape.com.br/neuro-summit/')
        if chave == 'workshop-neuro':
            fic = ler(fp) if fp and os.path.exists(fp) else ''
            mh = re.search(r'\*\*Data \(planilha e página\):\*\*[^\n]*?(das \d{2}h às \d{2}h)', fic)
            mc = re.search(r'^(Aluno e ex-aluno UFAPE comprovam[^\n]*)$', fic, re.M)
            mcup = re.search(r'(Aluno e ex-aluno Ufape): (\d+% de desconto) com o cupom (\w+)', preco)
            ev.update(data_fim='2026-11-21', formato='presencial', pagina_oficial='https://faculdade.ufape.com.br/neuro-summit/',
                      horario_texto=mh.group(1) if mh else '[CONFIRMAR]')
            if mcup:   # B9: cópia literal do catálogo (R4)
                ev['cupom'] = {'codigo': mcup.group(3), 'publico': mcup.group(1), 'desconto_texto': mcup.group(2), 'comprovacao_texto': mc.group(1) if mc else '[CONFIRMAR]'}
                j['condicoes_especiais'] = [{'tipo': 'cupom', 'texto': mcup.group(0), 'codigo': mcup.group(3), 'publico': mcup.group(1), 'validade': None}]
            # B9: modalidades do texto do catálogo (seção 9)
            for mm in re.finditer(r'(Presencial|Transmitido \+ gravado) \(([^)]*)\): (R\$ [\d.]+,\d{2})(?: \(produto (\d+)\))?', preco):
                vg = re.search(r'(\d+) vagas', mm.group(2))
                ev['modalidades'].append({'nome': f'{mm.group(1)} ({mm.group(2)})', 'preco_texto_site': mm.group(3), 'vagas': int(vg.group(1)) if vg else None, 'produto': mm.group(4)})
                if vg: j['vagas']['vagas_ofertadas'] = int(vg.group(1))
            j['fontes']['campos_so_na_ficha'] += ['evento.data_fim', 'evento.horario_texto'] + (['evento.cupom.comprovacao_texto'] if mc else [])
            if any(m_['vagas'] is None for m_ in ev['modalidades']):
                junta(pends, pend('U9', 'data', PERG.get('U9', '[CONFIRMAR]'), '[CONFIRMAR]',
                                  [f'evento.modalidades[{i}].vagas' for i, m_ in enumerate(ev['modalidades']) if m_['vagas'] is None], [], PC1 + ', seção 2'))
        j['evento'] = ev
    if rec == 'planejar':
        fonte_kit = (PL1 + ', seção 4') if chave in ONDA1_POS else (PL2 + ', seção 7') if chave in MARCO else (PL3 + ', seção 7') if chave in POS_ONDA3 else (PLANO_GERAL + ', seção 4')
        padroes(j, pends, fonte_kit)
    res.append(fecha(j, pends))

# ---------- Graduação (seção 1 do catálogo; plano próprio) ----------
TG = ler(PLG); TGM = ler(GMG)
G_LINHAS = {r['#']: r for r in linhas_pedido(PLG, r'^## 8\. ')}
MP_LINHAS = {r['#']: r for r in linhas_pedido(GMG, r'^## 7\. ')}
TRAVAS_G = []
for l in ler(DIARIO).split('\n'):
    # diário de 26/10 (qa rodada e) e de 27/10 (qa das campanhas rodada b)
    m = re.search(r'bloqueados pelas pendências ([^.|]*)', l)
    if m: TRAVAS_G += expande(m.group(1))
    m = re.search(r'nada sobe sem ([^|]*)', l)
    if m: TRAVAS_G += expande(m.group(1))
TRAVAS_G = list(dict.fromkeys(TRAVAS_G))
GRAD = [('graduacao-medicina-veterinaria', 'Medicina Veterinária', 'São Paulo, SP'), ('graduacao-pedagogia', 'Pedagogia', 'Goiânia, GO')]
OUTRO_CURSO = {'Medicina Veterinária': 'Pedagogia', 'Pedagogia': 'Medicina Veterinária'}
for ident, nome, local in GRAD:
    row = [l for l in txt if l.startswith('| ' + nome + ' |')]
    lit = row[0].split('| [ficha]')[0].rstrip() if row else '[CONFIRMAR]'
    cel = [c.strip() for c in row[0].strip().strip('|').split('|')] if row else []
    ch = cel[4] if len(cel) > 4 else '[CONFIRMAR]'
    ent = [entrega(k, n, q, 'aguardando_aprovacao', 'aprovado', a)
           for k, n, q, a in [('plano_8_canais', 'Plano dos 8 canais', 1, 'saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md'),
                              ('plano_de_midia', 'Plano de mídia', 1, 'saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md'),
                              ('posts_organicos', 'Posts orgânicos', 6, 'saidas/05-social-e-comunidade/posts-sociais-graduacao-2026-10-26.md'),
                              ('criativos_com_utm', 'Criativos com UTM', 4, 'saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md'),
                              ('whatsapp_prazos_do_edital', 'WhatsApp ligados ao edital', 5, 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md'),
                              ('email_prazos_do_edital', 'E-mails ligados ao edital', 3, 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md'),
                              ('roteiro_video', 'Roteiros de vídeo curto', 2, 'saidas/12-video-e-audio/tiktok-graduacao-2026-10-26.md')]]
    pends = [pend('P1', 'certificacao', 'Reconhecimento do curso: texto da regulação ainda não preenchido no contexto da linha', '[CONFIRMAR]', [], ['certificacao'], 'contexto/graduacao.md'),
             pend('editais', 'divergencia', 'Alertas do texto dos editais (datas e numeração) a confirmar com a Ufape; edital, turnos e LP ainda não copiados para o JSON', '[CONFIRMAR]',
                  ['graduacao.turnos', 'graduacao.edital', 'graduacao.edital_de_desconto', 'graduacao.reconhecimento', 'graduacao.lp.url', 'graduacao.lp.utm.utm_campaign', 'pagina_oficial', 'slug_sugerido'],
                  [], 'contexto/cursos/graduacao/editais-2027-1.md')]
    # B3: uma pendência por trava da Graduação (diário), com o texto do pedido do plano da Graduação ou do gestor-de-midia
    for cg in TRAVAS_G:
        if cg in G_LINHAS:
            oq = G_LINHAS[cg]['O que']
            i1, i2 = oq.find(nome), oq.find(OUTRO_CURSO[nome])
            if i2 >= 0 and (i1 < 0 or i2 < i1): continue   # trava de um curso só: vale para o curso citado primeiro
            pends.append(pend(cg, 'outro', oq, '[CONFIRMAR]', [], ['peca_final'], PLG + ', seção 8'))
        elif cg in MP_LINHAS:
            pends.append(pend(cg, 'meta_ou_verba' if cg in ('MP1', 'MP2') else 'outro', MP_LINHAS[cg]['O que'], '[CONFIRMAR]', [], ['anuncio'], GMG + ', seção 7'))
        elif cg in PERG:
            pends.append(pend(cg, 'meta_ou_verba', PERG[cg], '[CONFIRMAR]', ['metas.matriculas_alvo'], ['meta'], PC1 + ', seção 2'))
    if '[CONFIRMAR' in ch:   # B3 e R4: marcador do catálogo vira pendência; o pedido da Graduação é o G5
        gref = next((k for k, v in G_LINHAS.items() if 'carga horária' in v['O que'] and nome in v['O que']), 'R4')
        pends.append(pend(gref, 'divergencia', G_LINHAS[gref]['O que'] if gref in G_LINHAS else 'Carga horária com marcador no catálogo', '[CONFIRMAR]', ['carga_horaria'], [], PLG + ', seção 8'))
    if 'G4' in G_LINHAS:
        pends.append(pend('G4', 'data', G_LINHAS['G4']['O que'], '[CONFIRMAR]', ['fim_das_inscricoes', 'graduacao.inscricao_ate'], [], PLG + ', seção 8'))
    am = 'AM1 a AM12' if nome == 'Pedagogia' else 'AM1 a AM12 e AG1 a AG11'   # B3: diário, "Pedagogia 100% Meta"
    j = {'versao_schema': 1, 'id': ident, 'revisao': 1, 'revisao_aprovada': 0, 'estado_do_arquivo': 'ativo', 'substituido_por': None, 'gerado_em': HOJE, 'atualizado_em': HOJE,
         'fontes': {'catalogo': CAT, 'data_catalogo': DATA_CAT, 'catalogo_linha_literal': lit, 'ficha': 'contexto/cursos/graduacao/editais-2027-1.md', 'ficha_editais': 'contexto/cursos/graduacao/editais-2027-1.md', 'ficha_lida_em': None, 'campos_so_na_ficha': [],
                    'visao_de_campanhas': {'arquivo': 'docs/visao-de-campanhas-2026-10-26.md', 'data': '2026-10-26'}, 'plano': PLG, 'auditorias': ['docs/auditoria-do-catalogo-2026-10-26.md']},
         'codigo': 'sem-codigo', 'linha': 'graduacao', 'linha_origem': 'catalogo', 'tipo': 'graduacao', 'nome_no_site': nome, 'nome_padrao': nome, 'slug_sugerido': '[CONFIRMAR]', 'aliases': [], 'pagina_oficial': '[CONFIRMAR]',
         'area': {'codigo': 'nao_se_aplica', 'nome': 'Graduação', 'natureza': 'plano_do_cmo'}, 'recorte': 'planejar', 'motivo_do_recorte': 'plano próprio da Graduação (decisão 2)', 'onda': 1, 'modo_de_venda': 'com_data', 'grupo_de_campanha': 'vestibular-2027-1',
         'gut': None, 'relacionados': [], 'local': local, 'modalidade': cel[2] if len(cel) > 2 else '[CONFIRMAR]', 'modalidade_normalizada': 'presencial', 'turma': None,
         'carga_horaria': ch, 'modulos': None, 'inicio': '2027-02-22', 'fonte_da_data': 'edital', 'dias_ate_inicio': (datetime.date(2027, 2, 22) - datetime.date.fromisoformat(HOJE)).days,
         'fim_das_inscricoes': None, 'preco_texto_site': cel[5] if len(cel) > 5 else '[CONFIRMAR]', 'preco_estruturado': None, 'condicoes_especiais': [],
         'status_catalogo': 'aberto', 'status_catalogo_texto': 'inscrições abertas desde 17/08/2026 (edital)', 'vagas': {'turma_minima': 30, 'vagas_ofertadas': None, 'vagas_restantes': None},
         'equipe': None,
         'status_midia': {'campanha': 'nao_consta', 'formatos': [], 'cinco_angulos': 'nao_consta', 'vinculo_com_a_visao': 'nenhum', 'inicio_na_visao': None, 'divergencia_de_data': False, 'fonte': 'docs/visao-de-campanhas-2026-10-26.md', 'lido_em': '2026-10-26'},
         'kit': {'template': 'templates/kit-de-lancamento-graduacao.md', 'variacao': None, 'escopo': 'item', 'entregas': ent, 'acrescimos': []},
         'canais': canais('graduacao', None), 'arquivos_por_camada': {'geral': [], 'linha': [{'agente': 'cmo', 'caminho': PLG, 'secao': None, 'estado': 'pendente_de_aprovacao', 'aprovado_em': None, 'ref_aprovacao': None}], 'area': [], 'curso': []},
         'metas': {'matriculas_alvo': 15, 'cpl_maximo': None, 'custo_por_matricula_maximo': None, 'verba': 2000.00, 'fonte': 'decisões 15 e 16 do briefing'},
         'numeros_agregados': {'leads': None, 'inscricoes': None, 'matriculas': None, 'verba_gasta': None, 'lido_em': None},
         'aprovacoes': [apr(am, 'subir as campanhas ' + ('Meta' if nome == 'Pedagogia' else 'Meta e Google') + ' da Graduação', 'captação do vestibular 2027.1', 'R$ 2.000,00 por curso (decisão 15)', 'inscrições até o início das aulas', 'pausar as campanhas', HOJE)],
         'historico': [{'revisao': 1, 'em': HOJE, 'campo': '*', 'de': None, 'para': 'criação', 'motivo': 'versão 1 do mapa', 'origem': 'gerador do orquestrador sobre o plano do cmo', 'aplicado_por': 'orquestrador'}]}
    j['graduacao'] = {'edital': {'numero': '[CONFIRMAR]', 'titulo': '[CONFIRMAR]', 'url': '[CONFIRMAR]'}, 'edital_de_desconto': {'numero': '[CONFIRMAR]', 'titulo': '[CONFIRMAR]', 'url': '[CONFIRMAR]'},
                      'ato_autorizativo': cel[6] if len(cel) > 6 else '[CONFIRMAR]', 'reconhecimento': '[CONFIRMAR]', 'grau': 'bacharelado' if 'Veterin' in nome else 'licenciatura',
                      'turnos': [], 'formas_de_ingresso': ['redacao', 'enem', 'transferencia_externa', 'diplomado', 'vagas_remanescentes'], 'inscricoes_abertas_desde': '2026-08-17',
                      'inscricao_ate': None, 'inicio_das_aulas': '2027-02-22', 'validade_do_desconto': 'só para o 1º semestre de 2027', 'lp': {'url': '[CONFIRMAR]', 'alterada_pela_squad': False, 'utm': {'gerada_por': 'plataforma', 'parametros': ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'], 'utm_campaign': '[CONFIRMAR]'}}}
    padroes(j, pends, PLG + ', seção 6')
    res.append(fecha(j, pends))

# ---------- gravação ----------
if '--write' in sys.argv:
    os.makedirs(OUT, exist_ok=True)
    for j in res:
        with open(os.path.join(OUT, j['id'] + '.json'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    with open('ferramentas/mapa-mental/saida/mapa-dados.json', 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False)
from collections import Counter
print('itens', len(res))
print('recorte', Counter(j['recorte'] for j in res))
print('linha', Counter(j['linha'] for j in res))
print('recorte sem a Graduação', sum(1 for j in res if j['recorte'] == 'planejar' and j['linha'] != 'graduacao'))
print('onda (planejar, sem a Graduação)', Counter(j['onda'] for j in res if j['recorte'] == 'planejar' and j['linha'] != 'graduacao'))
print('sem área no recorte', [j['id'] for j in res if j['recorte'] == 'planejar' and j['area']['codigo'] == 'sem_area'])
print('ids repetidos', [k for k, v in Counter(j['id'] for j in res).items() if v > 1])
print('bloqueados', sum(j['resumo']['bloqueado'] for j in res))
