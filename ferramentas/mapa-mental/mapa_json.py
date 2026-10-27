# Gera os JSON por item (esquema versão 1 de arquiteto-de-fluxos-geral-2026-10-26.md) a partir do
# catálogo e das saídas aprovadas. Nenhum número é inventado: dado ausente vira "[CONFIRMAR]" ou null
# com pendência. Roda a partir da raiz do repositório marketing-ufape.
import re, json, os, sys, datetime, unicodedata

HOJE = '2026-10-27'
CAT = 'contexto/catalogo-de-cursos.md'
PLANO_GERAL = 'saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md'
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

# ---------- leitura do catálogo ----------
txt = open(CAT, encoding='utf-8').read().split('\n')
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

# ---------- plano geral: áreas, ondas, GUT, mídia ----------
P = open(PLANO_GERAL, encoding='utf-8').read()
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

ONDA1 = set('707 68604 68606 698 68610 68608 573 68614 623 68637 68665 68666'.split())
ONDA2 = set('616 68618 657 341 289 68615 333'.split())
ONDA3 = set('679 68632 68635 366 68628 68617 68636 68609 662 719 68616 68629 359 699 382 68623 578 352 60 68638 560'.split())
ABRIL = '679 68632 68635 366 68628 68617 68636 68609'.split()
MARCO = '657 341 289 68615 333'.split()
MAIO = '719 68616 68629 359 699 382 68623 578 352 60'.split()
ONDA1_POS = '707 68604 68606 698 68610 68608'.split()

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
for cods, est in [('707 68604 68606 698 68610 68608 workshop-neuro 573 623 68614', 'ativa'), ('289 700 662', 'ativa'),
                  ('657 341 68615 333 68618 68635 366 68617 382 578 352 60 679', 'pausada'),
                  ('202 68632 68628 68609 719 68616 699 68623', 'sem_campanha')]:
    for c in cods.split(): MIDIA[c] = est

# ---------- pendências por item (fontes: briefing, planos e revisões do qa) ----------
B = 'docs/execucao-2026-10-26.md'
PL2 = 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md'
PL3 = 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md'
def pend(pid, ref, tipo, desc, marc, campos, bloq, fonte):
    return {'id': pid, 'ref_plano': ref, 'tipo': tipo, 'descricao': desc, 'marcador': marc, 'campos': campos,
            'bloqueia': bloq, 'fonte': fonte, 'aberta_em': HOJE, 'resolvida_em': None}
ESPECIFICAS = {
    '333': [('regra 8', 'data', 'Como o aluno que entra depois do início repõe o módulo 1 presencial (OU3); sem resposta, nada pós-início e mídia parando na véspera do início', ['kit.entregas[*]'], ['anuncio'], PL2),
            ('OU12', 'outro', 'Quem coordena a turma (a ficha lista só uma professora)', ['equipe.coordenadores_na_ficha'], [], PL2),
            ('OU17', 'data', 'Módulo 1 cai no fim de semana da Páscoa (27 e 28/03/2027)', ['inicio'], [], PL2)],
    '341': [('OU10', 'preco_ou_condicao', 'Promoção da página: corrigir ou retirar; sem isso nenhuma peça de 341 sai', ['condicoes_especiais'], ['peca_final'], PL2),
            ('OU11', 'outro', 'Local da prática e formato do módulo 3; 3º módulo em 01/05/2027, feriado (OU17)', [], [], PL2)],
    '657': [('U10', 'outro', 'Pré-requisito de entrada não está na ficha', [], ['pagina'], PL2),
            ('regulação', 'regulatorio', 'Convite da prova de Especialista e frases de resultado clínico no cronograma; sigla DACVAA de docente', [], ['pagina'], PL2)],
    '289': [('CP1', 'outro', 'Cidade no texto da página só com aprovação; página de 68605 à venda disputa a mesma busca', [], [], 'saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2a.md')],
    '68615': [('OB1', 'conformidade', 'Página no ar diz que o curso tem reconhecimento ligado ao órgão regulador e "referência nacional"', [], ['pagina'], PL2)],
    '679': [('OU19', 'data', 'Data de início a confirmar; linha da planilha aponta para a página de 679', ['inicio'], ['data', 'peca_final'], PL3),
            ('OU25', 'data', 'Dia do 3º módulo não está na ficha (só o mês)', [], ['anuncio'], PL3)],
    '366': [('OU20', 'data', 'Data de início diverge entre planilha e site', ['inicio'], ['data', 'peca_final'], PL3),
            ('OU25', 'data', 'Dia do 3º módulo não está na ficha (só o mês)', [], ['anuncio'], PL3)],
    '68636': [('OU21', 'data', 'Data de início sem linha própria na planilha', ['inicio'], ['data', 'peca_final'], PL3)],
    '68635': [('OU25', 'data', 'Dia do 3º módulo não está na ficha (só o mês)', [], ['anuncio'], PL3)],
    '68632': [('regra 8', 'data', 'Módulo presencial antes do 3º: sem OU3, nada pós-início e mídia parando na véspera do início (decisão do cmo)', ['kit.entregas[*]'], ['anuncio'], 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-decisao-68632.md')],
    '68628': [('P5', 'turma', 'Turma diferente entre planilha e site; peças sem número de turma', ['turma'], [], PLANO_GERAL)],
    '68617': [('P5', 'turma', 'Turma diferente entre planilha e site; peças sem número de turma', ['turma'], [], PLANO_GERAL)],
    '68609': [('ficha', 'divergencia', 'Ficha diz 26 módulos e o cronograma lista 24', ['modulos'], [], PL3)],
    '662': [('OU18', 'data', 'Turma de 2027 sem data confiável (24/04/2027 coincide com o módulo 9 da turma IV); campanha atual com pedido de pausa', ['inicio'], ['data', 'peca_final', 'anuncio'], PL3)],
    '698': [('decisão 19', 'data', 'Página ainda mostra 2027; a campanha segue com 28 e 29/11/2026 e a correção do site continua pedida', [], [], B)],
    '359': [('regra 8', 'data', 'Módulo 2 presencial antes do 3º: regra 8 (decisão do cmo); data só no site', ['inicio'], ['anuncio'], 'saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-decisao-333-359.md')],
}
for c in '68616 578 352'.split():
    ESPECIFICAS.setdefault(c, []).append(('regra 8', 'data', 'Módulo 1 ou 2 presencial: sem OU3, nada pós-início', [], ['anuncio'], PL3))
for c in '68640 68642 68644'.split():
    ESPECIFICAS.setdefault(c, []).append(('decisão 20', 'outro', 'Prova presencial em Goiânia: a página mostra endereço de São Paulo; local de Goiânia a confirmar', [], ['peca_final'], B))

# ---------- kit ----------
KEYS_POS = [('pagina', 'Página da turma', 1), ('plano_8_canais', 'Plano dos 8 canais', 1), ('plano_de_midia', 'Plano de mídia', 1),
            ('posts_organicos', 'Posts orgânicos', 6), ('criativos', 'Criativos de anúncio', 3), ('post_por_docente', 'Post por docente', None),
            ('whatsapp', 'Mensagens de WhatsApp', 4), ('email', 'E-mails', 2), ('roteiro_video', 'Roteiro de vídeo curto', 1)]
RESP = {'pagina': 'landing-page', 'plano_8_canais': 'cmo', 'plano_de_midia': 'gestor-de-midia', 'posts_organicos': 'posts-sociais',
        'criativos': 'criativos-de-anuncio', 'post_por_docente': 'autoridade-docente', 'whatsapp': 'copy-de-mensagens', 'email': 'copy-de-mensagens',
        'roteiro_video': 'tiktok'}
def arquivos_onda(onda):
    d = '2026-10-27-' + onda
    return {'pagina': f'saidas/08-conversao/landing-page-pos-{d}.md', 'plano_8_canais': f'saidas/02-estrategia-e-posicionamento/cmo-pos-{d}.md',
            'plano_de_midia': 'saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md', 'posts_organicos': f'saidas/05-social-e-comunidade/posts-sociais-pos-{d}.md',
            'criativos': 'saidas/11-midia-paga/criativos-de-anuncio-pos-turmas-2026-10-26.md', 'post_por_docente': f'saidas/05-social-e-comunidade/autoridade-docente-pos-{d}.md',
            'whatsapp': f'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-{d}.md', 'email': f'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-{d}.md',
            'roteiro_video': f'saidas/12-video-e-audio/tiktok-pos-{d}.md'}
def kit_pos(cod):
    ent = []
    if cod in MARCO: arq = arquivos_onda('onda2'); est = 'aguardando_aprovacao'; qa = 'aprovado'
    elif cod in ABRIL: arq = arquivos_onda('onda3'); est = 'aguardando_aprovacao'; qa = 'aprovado'
    elif cod in MAIO or cod == '662': arq = {}; est = 'a_fazer'; qa = 'pendente'
    elif cod in ONDA1_POS: arq = {}; est = 'inventario_pendente'; qa = 'pendente'
    else: arq = {}; est = 'nao_aplicavel'; qa = 'pendente'
    for k, nome, q in KEYS_POS:
        e = {'chave': k, 'entrega': nome, 'quantidade_minima': q, 'regra_quantidade': '1_por_docente_autorizado' if q is None else None,
             'autorizados': None, 'responsavel': RESP[k], 'prazo': None, 'status': est, 'qa': qa, 'arquivo': arq.get(k)}
        if cod == '662': e['status'] = 'a_fazer'; e['arquivo'] = None
        if cod in MAIO and k in ('plano_8_canais', 'plano_de_midia'):
            e['status'] = 'aguardando_aprovacao'; e['qa'] = 'aprovado'
            e['arquivo'] = PL3 if k == 'plano_8_canais' else 'saidas/11-midia-paga/gestor-de-midia-pos-2026-10-27-onda3.md'
        if cod in ONDA1_POS:
            if k in ('whatsapp', 'email'): e.update(status='aguardando_aprovacao', qa='aprovado', arquivo='saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-onda1-2026-10-26.md')
            if k == 'plano_8_canais': e.update(status='aguardando_aprovacao', qa='aprovado', arquivo='saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md')
            if k == 'plano_de_midia': e.update(status='aguardando_aprovacao', qa='aprovado', arquivo='saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md')
        ent.append(e)
    return ent

# ---------- canais (seção 5 do plano geral; ondas 2 e 3 da Pós pelos planos de onda) ----------
CANAIS_LINHA = {
    'pos': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'teste', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'livres': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'eventos': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'},
    'graduacao': {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'ativo', 'tiktok': 'teste', 'x': 'fora', 'podcast': 'fora'},
}
POS_ONDA23 = {'instagram': 'ativo', 'facebook': 'ativo', 'whatsapp': 'ativo', 'linkedin': 'fora', 'youtube': 'fora', 'tiktok': 'fora', 'x': 'fora', 'podcast': 'fora'}
def canais(linha, cod):
    if linha == 'pos' and (cod in MARCO or cod in ABRIL or cod in MAIO):
        base, fonte = POS_ONDA23, (PL2 if cod in MARCO else PL3)
        nat = 'plano_da_onda'
    else:
        base, fonte, nat = CANAIS_LINHA[linha], PLANO_GERAL + ', seção 5', 'proposta_do_cmo'
    return [{'canal': c, 'estado': base[c], 'motivo': 'ver ' + fonte, 'natureza': nat} for c in ['instagram', 'facebook', 'tiktok', 'x', 'linkedin', 'youtube', 'podcast', 'whatsapp']]

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
    m = re.search(r'(\d+)x de R\$ ([\d.]+,\d{2})', t or '')
    tot = re.search(r'R\$ ([\d.]+,\d{2}) (?:no cartão|à vista)', t or '')
    mat = re.search(r'matrícula R\$ ([\d.]+,\d{2})', t or '')
    if not m: return None
    num = lambda s: float(s.replace('.', '').replace(',', '.'))
    return {'moeda': 'BRL', 'parcelas': int(m.group(1)), 'valor_parcela': num(m.group(2)), 'total': num(tot.group(1)) if tot else None,
            'matricula': num(mat.group(1)) if mat else None}

def ficha_path(cel):
    m = re.search(r'\((cursos/[^)]+)\)', cel or '')
    return 'contexto/' + m.group(1) if m else None

def modulos_da_ficha(p):
    if not p or not os.path.exists(p): return None
    m = re.search(r'\*\*Módulos:\*\*\s*(\d+)', open(p, encoding='utf-8').read())
    return int(m.group(1)) if m else None

def pagina_da_ficha(p):
    if not p or not os.path.exists(p): return None
    m = re.search(r'https://faculdade\.ufape\.com\.br/\S+', open(p, encoding='utf-8').read())
    return m.group(0).rstrip(').,') if m else None

def nome_padrao(nome, tipo):
    if tipo == 'pos':
        return nome if nome.startswith('Pós-graduação em') else '[CONFIRMAR]'
    return nome

res = []
for r in itens:
    sec = r['_secao']; linha, tipo = secoes[sec]
    cod = re.sub(r'\D', '', r.get('Código', '')) or 'sem-codigo'
    nome = r.get('Curso', '')
    if sec == '9':
        tipo = 'workshop' if 'Workshop' in nome else 'simposio'
    if cod == 'sem-codigo' and 'Neuromonitoriza' in nome: chave = 'workshop-neuro'; ident = 'eventos-workshop-neuromonitorizacao-2026-11-20'
    elif cod == 'sem-codigo': chave = None; ident = f'{linha}-sem-codigo-{slug(nome)[:60]}'
    else: chave = cod; ident = f'{linha}-{cod}'
    st = status_norm(r.get('Status')); ini = data_iso(r.get('Início', ''))
    fonte_txt = (r.get('Fonte') or '').lower()
    fonte_data = 'planilha' if 'planilha' in fonte_txt else ('site' if 'site' in fonte_txt else ('pagina_do_evento' if chave == 'workshop-neuro' else 'ausente'))
    if sec == '3' and ini: fonte_data = 'site'
    area = AREAS.get(chave) if chave else None
    no_recorte = area is not None
    if no_recorte and st in ('aberto', 'aberto (contínuo)'): rec = 'planejar'
    elif st in ('sem venda', 'encerrado'): rec = 'historico'
    else: rec = 'pendencia'
    if rec == 'planejar':
        onda = 1 if (chave in ONDA1 or tipo == 'prova_de_bolsa' or chave == 'workshop-neuro') else 2 if (chave in ONDA2 or st == 'aberto (contínuo)') else 3 if chave in ONDA3 else None
    else: onda = None
    modo = 'continuo' if st == 'aberto (contínuo)' else 'com_data'
    g = None
    if rec == 'planejar':
        for cods, gg, uu, tt, mot in GUT:
            alvo = (cods == 'PROVAS' and tipo == 'prova_de_bolsa') or (cods == 'CONTINUOS' and modo == 'continuo') or (chave in cods.split())
            if alvo: g = {'g': gg, 'u': uu, 't': tt, 'total': gg * uu * tt, 'motivo': mot, 'natureza': 'avaliacao_do_agente', 'fonte': PLANO_GERAL + ', seção 3'}; break
    fp = ficha_path(r.get('Ficha'))
    preco = r.get('Preço e condições (site)') or r.get('Preço (site)') or ''
    dias = (datetime.date.fromisoformat(ini) - datetime.date.fromisoformat(HOJE)).days if (ini and modo == 'com_data') else None
    pends = [pend('P1', 'P1', 'certificacao', 'Texto oficial de certificação ainda não aprovado pela regulação; nenhuma peça afirma certificação', '[CONFIRMAR]', [], ['certificacao'], PLANO_GERAL + ', seção 7')]
    if tipo == 'pos' and rec == 'planejar':
        pends.append(pend('P2', 'P2', 'conformidade', 'Página no ar com frase de certificação ligada ao órgão regulador e turma mínima diferente de 15; correção pedida no site', '[CONFIRMAR]', [], ['pagina'], PLANO_GERAL + ', seção 7'))
        pends.append(pend('U11', 'decisão 16', 'preco_ou_condicao', 'Valor da inscrição (R$ 260,00 informado) diferente da matrícula do site; nenhuma peça cita o valor', '[CONFIRMAR]', ['preco_estruturado.matricula'], ['preco'], B))
        pends.append(pend('privacidade', 'OB1', 'conformidade', 'Endereço da política de privacidade do formulário', '[CONFIRMAR]', [], ['pagina'], 'saidas/08-conversao/otimizador-de-cta-pos-2026-10-27-onda2.md'))
    if tipo == 'prova_de_bolsa':
        pends.append(pend('decisão 14', 'decisão 14', 'kit', 'Peças das provas suspensas até nova ordem; textos antigos tratam a prova como online e precisam de varredura para presencial (decisão 20)', '[CONFIRMAR]', ['kit.entregas[*]'], ['peca_final'], B))
    if linha == 'livres' and rec == 'planejar':
        pends.append(pend('decisão 14', 'decisão 14', 'kit', 'Cursos Livres ficam por último na ordem de prioridade; kit ainda não produzido', '[CONFIRMAR]', ['kit.entregas[*]'], [], B))
    for i, (ref, tp, desc, campos, bloq, fonte) in enumerate(ESPECIFICAS.get(chave, []), 1):
        pends.append(pend(f'E{i}', ref, tp, desc, '[CONFIRMAR]', campos, bloq, fonte))
    if not ini and modo == 'com_data' and rec == 'planejar':
        pends.append(pend('data', 'R5', 'data', 'Data de início ausente no catálogo', '[CONFIRMAR]', ['inicio'], ['data'], CAT))
    if tipo == 'pos':
        kit = {'template': 'templates/kit-de-lancamento-pos.md', 'variacao': None, 'escopo': 'item', 'entregas': kit_pos(chave) if rec == 'planejar' else [], 'acrescimos': []}
    elif tipo == 'prova_de_bolsa':
        kit = {'template': None, 'variacao': None, 'escopo': 'grupo', 'entregas': [{'chave': 'campanha_unica', 'entrega': 'Campanha única das provas de 27/11', 'quantidade_minima': 1, 'regra_quantidade': None, 'autorizados': None, 'responsavel': 'estrategia-de-campanha', 'prazo': None, 'status': 'revisar_por_mudanca', 'qa': 'pendente', 'arquivo': 'saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md'}], 'acrescimos': []}
    elif chave == 'workshop-neuro':
        kit = {'template': 'templates/kit-de-lancamento-evento.md', 'variacao': 'workshop', 'escopo': 'item', 'acrescimos': [], 'entregas': [
            {'chave': 'posts_organicos', 'entrega': 'Posts orgânicos', 'quantidade_minima': 3, 'regra_quantidade': None, 'autorizados': None, 'responsavel': 'posts-sociais', 'prazo': None, 'status': 'devolvido', 'qa': 'corrigir', 'arquivo': 'saidas/05-social-e-comunidade/posts-sociais-eventos-2026-10-26.md'},
            {'chave': 'criativos', 'entrega': 'Criativos de anúncio', 'quantidade_minima': 2, 'regra_quantidade': None, 'autorizados': None, 'responsavel': 'criativos-de-anuncio', 'prazo': None, 'status': 'inventario_pendente', 'qa': 'pendente', 'arquivo': 'saidas/11-midia-paga/criativos-de-anuncio-eventos-2026-10-26.md'},
            {'chave': 'mensagem_convite', 'entrega': 'Mensagens (convite, véspera, dia) e e-mail convite', 'quantidade_minima': 4, 'regra_quantidade': None, 'autorizados': None, 'responsavel': 'copy-de-mensagens', 'prazo': None, 'status': 'devolvido', 'qa': 'corrigir', 'arquivo': 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-eventos-2026-10-26.md'},
            {'chave': 'pagina', 'entrega': 'Página do evento (página própria da Ufape, campanhas apontam para ela)', 'quantidade_minima': 1, 'regra_quantidade': None, 'autorizados': None, 'responsavel': 'landing-page', 'prazo': None, 'status': 'nao_aplicavel', 'qa': 'pendente', 'arquivo': None}]}
    elif modo == 'continuo':
        kit = {'template': None, 'variacao': None, 'escopo': 'grupo', 'entregas': [], 'acrescimos': []}
    elif linha == 'livres':
        kit = {'template': 'templates/kit-de-lancamento-livres.md', 'variacao': None, 'escopo': 'item', 'acrescimos': [], 'entregas': [
            {'chave': k, 'entrega': n, 'quantidade_minima': q, 'regra_quantidade': None, 'autorizados': None, 'responsavel': rp, 'prazo': None, 'status': 'a_fazer', 'qa': 'pendente', 'arquivo': None}
            for k, n, q, rp in [('pagina', 'Página', 1, 'landing-page'), ('plano_8_canais', 'Plano dos 8 canais', 1, 'cmo'), ('posts_organicos', 'Posts orgânicos', 4, 'posts-sociais'), ('criativos', 'Criativos', 2, 'criativos-de-anuncio'), ('whatsapp', 'WhatsApp', 3, 'copy-de-mensagens'), ('email', 'E-mail', 1, 'copy-de-mensagens')]]} if rec == 'planejar' else {'template': None, 'variacao': None, 'escopo': 'item', 'entregas': [], 'acrescimos': []}
    else:
        kit = {'template': None, 'variacao': None, 'escopo': 'item', 'entregas': [], 'acrescimos': []}
    metas = {'matriculas_alvo': 15 if (tipo == 'pos' and rec == 'planejar') else None, 'cpl_maximo': None, 'custo_por_matricula_maximo': None,
             'verba': 2000.00 if (tipo == 'pos' and rec == 'planejar') else None, 'fonte': 'decisões 15 e 16 do briefing' if tipo == 'pos' else '[CONFIRMAR]'}
    arqs = {'geral': [{'agente': 'cmo', 'caminho': PLANO_GERAL, 'secao': None, 'estado': 'aprovado', 'aprovado_em': '2026-10-26', 'ref_aprovacao': 'plano aprovado pela pessoa do marketing'}],
            'linha': [], 'area': [], 'curso': [{'agente': e['responsavel'], 'caminho': e['arquivo'], 'secao': chave, 'estado': 'pendente_de_aprovacao' if e['qa'] == 'aprovado' else ('devolvido' if e['qa'] == 'corrigir' else 'pendente_de_aprovacao'), 'aprovado_em': None, 'ref_aprovacao': None} for e in kit['entregas'] if e.get('arquivo')]}
    for f in sorted(os.listdir('saidas/02-estrategia-e-posicionamento')):
        if f.startswith('cmo-' + linha + '-2026-10-26'): arqs['linha'].append({'agente': 'cmo', 'caminho': 'saidas/02-estrategia-e-posicionamento/' + f, 'secao': None, 'estado': 'pendente_de_aprovacao', 'aprovado_em': None, 'ref_aprovacao': None})
    if area and linha in ('pos', 'livres'):
        arqs['area'].append({'agente': 'mensagens', 'caminho': f'saidas/02-estrategia-e-posicionamento/mensagens-{linha}-2026-10-26.md', 'secao': area, 'estado': 'pendente_de_aprovacao', 'aprovado_em': None, 'ref_aprovacao': None})
    aprov = []
    if chave in MARCO: aprov = [{'ref': x, 'o_que': y, 'por_que': 'kit mínimo da onda 2', 'quanto': 'sem verba nova', 'efeito_esperado': 'turma pronta para a subida de 07/12', 'como_desfazer': 'despublicar ou pausar', 'status': 'pendente', 'pedido_em': HOJE, 'decidido_em': None, 'decidido_por_papel': None} for x, y in [('OB1', 'publicar a página e corrigir o site'), ('OB2', 'enviar as mensagens'), ('OB3', 'publicar posts e cards de docente'), ('AMP13 a AMP25 e AGP12 a AGP25', 'subir a mídia paga')]]
    if chave in ABRIL: aprov = [{'ref': x, 'o_que': y, 'por_que': 'kit mínimo da onda 3', 'quanto': 'sem verba nova', 'efeito_esperado': 'turma pronta para a subida de abril', 'como_desfazer': 'despublicar ou pausar', 'status': 'pendente', 'pedido_em': HOJE, 'decidido_em': None, 'decidido_por_papel': None} for x, y in [('OC1-A', 'publicar a página e corrigir o site'), ('OC2', 'enviar as mensagens'), ('OC3', 'publicar cards de docente'), ('OC4', 'publicar posts e Reels'), ('AMP13 a AMP25 e AGP12 a AGP25', 'subir a mídia paga')]]
    j = {'versao_schema': 1, 'id': ident, 'revisao': 1, 'revisao_aprovada': 0, 'estado_do_arquivo': 'ativo', 'substituido_por': None,
         'gerado_em': HOJE, 'atualizado_em': HOJE,
         'fontes': {'catalogo': CAT, 'data_catalogo': DATA_CAT, 'catalogo_linha_literal': r['_literal'].split('| [ficha]')[0].rstrip(), 'ficha': fp, 'ficha_lida_em': None,
                    'campos_so_na_ficha': (['modulos'] if modulos_da_ficha(fp) else []) + (['pagina_oficial'] if pagina_da_ficha(fp) else []),
                    'visao_de_campanhas': {'arquivo': 'docs/visao-de-campanhas-2026-10-26.md', 'data': '2026-10-26'}, 'plano': PLANO_GERAL,
                    'auditorias': ['docs/auditoria-do-catalogo-2026-10-26.md']},
         'codigo': cod, 'linha': linha, 'linha_origem': 'catalogo', 'tipo': tipo, 'nome_no_site': nome or '[CONFIRMAR]', 'nome_padrao': nome_padrao(nome, tipo),
         'slug_sugerido': slug(nome) if tipo == 'pos' and nome.startswith('Pós-graduação em') else '[CONFIRMAR]', 'aliases': [],
         'pagina_oficial': pagina_da_ficha(fp) or ('[CONFIRMAR]' if st.startswith('aberto') else None),
         'area': {'codigo': area or 'sem_area', 'nome': NOMES_AREA.get(area, '[CONFIRMAR]') if area else '[CONFIRMAR]', 'natureza': 'plano_do_cmo'},
         'recorte': rec, 'motivo_do_recorte': {'planejar': 'à venda e no recorte do plano geral (seção 2)', 'historico': 'sem venda ou encerrado no catálogo', 'pendencia': 'status do catálogo pede verificação ou o item está fora do recorte'}[rec],
         'onda': onda, 'modo_de_venda': modo, 'grupo_de_campanha': 'provas-de-bolsa-2026-11-27' if tipo == 'prova_de_bolsa' else (f'sempre-ligado-{area}' if modo == 'continuo' and area else None),
         'gut': g, 'relacionados': [],
         'local': r.get('Local') or '[CONFIRMAR]', 'modalidade': r.get('Modalidade') or ('PROVA PRESENCIAL' if tipo == 'prova_de_bolsa' else '[CONFIRMAR]'),
         'modalidade_normalizada': modalidade_norm(r.get('Modalidade'), tipo), 'turma': (r.get('Turma') or '[CONFIRMAR]') if tipo == 'pos' else None,
         'carga_horaria': (r.get('CH') or '[CONFIRMAR]') if tipo != 'prova_de_bolsa' else None, 'modulos': modulos_da_ficha(fp) if tipo == 'pos' else None,
         'inicio': ini, 'fonte_da_data': fonte_data if ini else 'ausente', 'dias_ate_inicio': dias, 'fim_das_inscricoes': None,
         'preco_texto_site': preco or '[CONFIRMAR]', 'preco_estruturado': preco_estr(preco), 'condicoes_especiais': [],
         'status_catalogo': st, 'status_catalogo_texto': r.get('Status') or '[CONFIRMAR]',
         'vagas': {'turma_minima': 15 if tipo == 'pos' else None, 'vagas_ofertadas': None, 'vagas_restantes': None},
         'equipe': {'coordenadores_na_ficha': None, 'docentes_na_ficha': None, 'autorizacoes_de_imagem_registradas': None},
         'status_midia': {'campanha': MIDIA.get(chave, 'nao_consta'), 'formatos': [], 'cinco_angulos': 'nao_consta', 'vinculo_com_a_visao': 'provavel' if chave in MIDIA else 'nenhum',
                          'inicio_na_visao': None, 'divergencia_de_data': False, 'fonte': 'docs/visao-de-campanhas-2026-10-26.md', 'lido_em': '2026-10-26'},
         'kit': kit, 'canais': canais(linha, chave), 'arquivos_por_camada': arqs, 'metas': metas,
         'numeros_agregados': {'leads': None, 'inscricoes': None, 'matriculas': None, 'verba_gasta': None, 'lido_em': None},
         'pendencias': pends, 'aprovacoes': aprov,
         'historico': [{'revisao': 1, 'em': HOJE, 'campo': '*', 'de': None, 'para': 'criação', 'motivo': 'versão 1 do mapa, gerada do catálogo e das saídas aprovadas', 'origem': 'gerador do orquestrador sobre o plano do cmo', 'aplicado_por': 'orquestrador'}]}
    if tipo == 'prova_de_bolsa':
        j['prova_de_bolsa'] = {'data_da_prova': ini, 'horario_texto': '[CONFIRMAR]', 'formato': 'presencial', 'local_texto': r.get('Local') or '[CONFIRMAR]',
                               'nota_de_corte_texto': '[CONFIRMAR]', 'turma_de_destino': {'codigo': '[CONFIRMAR]', 'sugestao_do_plano': None, 'natureza_da_sugestao': '[SUPOSIÇÃO]'},
                               'bolsas_previstas': None, 'prazo_de_matricula_apos_resultado': '[CONFIRMAR]', 'divulgacao_do_resultado': '[CONFIRMAR]', 'minimo_para_confirmar_turma': 15}
    if tipo in ('workshop', 'simposio'):
        j['evento'] = {'subtipo': tipo, 'data_inicio': ini, 'data_fim': '2026-11-21' if chave == 'workshop-neuro' else None, 'horario_texto': '[CONFIRMAR]',
                       'formato': 'presencial' if chave == 'workshop-neuro' else ('gravado' if modo == 'continuo' else '[CONFIRMAR]'), 'modalidades': [], 'carga_horaria_oficial': '16 h' if chave == 'workshop-neuro' else '[CONFIRMAR]',
                       'cupom': {'codigo': 'SIMPNEUROMONIT', 'publico': 'aluno e ex-aluno', 'desconto_texto': '[CONFIRMAR]', 'comprovacao_texto': '[CONFIRMAR]'} if chave == 'workshop-neuro' else None,
                       'pagina_oficial': 'https://faculdade.ufape.com.br/neuro-summit/' if chave == 'workshop-neuro' else '[CONFIRMAR]',
                       'destino_das_campanhas_pagas': 'https://faculdade.ufape.com.br/neuro-summit/' if chave == 'workshop-neuro' else '[CONFIRMAR]',
                       'palestrantes': {'confirmados_na_ficha': None, 'convidados_a_definir': None, 'autorizacoes_de_imagem_registradas': None}}
    ab = [p for p in pends if p['resolvida_em'] is None]
    j['resumo'] = {'pendencias_abertas': len(ab), 'bloqueado': any('peca_final' in p['bloqueia'] for p in ab)}
    res.append(j)

# Graduação (seção 1 do catálogo; plano próprio)
GRAD = [('graduacao-medicina-veterinaria', 'Medicina Veterinária', 'São Paulo, SP'), ('graduacao-pedagogia', 'Pedagogia', 'Goiânia, GO')]
for ident, nome, local in GRAD:
    row = [l for l in txt if l.startswith('| ' + nome + ' |')]
    lit = row[0].split('| [ficha]')[0].rstrip() if row else '[CONFIRMAR]'
    cel = [c.strip() for c in row[0].strip().strip('|').split('|')] if row else []
    ent = [{'chave': k, 'entrega': n, 'quantidade_minima': q, 'regra_quantidade': None, 'autorizados': None, 'responsavel': rp, 'prazo': None, 'status': 'aguardando_aprovacao', 'qa': 'aprovado', 'arquivo': a}
           for k, n, q, rp, a in [('plano_8_canais', 'Plano dos 8 canais', 1, 'cmo', 'saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md'),
                                  ('plano_de_midia', 'Plano de mídia', 1, 'gestor-de-midia', 'saidas/11-midia-paga/gestor-de-midia-graduacao-2026-10-26.md'),
                                  ('posts_organicos', 'Posts orgânicos', 6, 'posts-sociais', 'saidas/05-social-e-comunidade/posts-sociais-graduacao-2026-10-26.md'),
                                  ('criativos_com_utm', 'Criativos com UTM', 4, 'criativos-de-anuncio', 'saidas/11-midia-paga/criativos-de-anuncio-graduacao-2026-10-26.md'),
                                  ('whatsapp_prazos_do_edital', 'WhatsApp ligados ao edital', 5, 'copy-de-mensagens', 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md'),
                                  ('email_prazos_do_edital', 'E-mails ligados ao edital', 3, 'copy-de-mensagens', 'saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-graduacao-2026-10-26.md'),
                                  ('roteiro_video', 'Roteiros de vídeo curto', 2, 'tiktok', 'saidas/12-video-e-audio/tiktok-graduacao-2026-10-26.md')]]
    j = {'versao_schema': 1, 'id': ident, 'revisao': 1, 'revisao_aprovada': 0, 'estado_do_arquivo': 'ativo', 'substituido_por': None, 'gerado_em': HOJE, 'atualizado_em': HOJE,
         'fontes': {'catalogo': CAT, 'data_catalogo': DATA_CAT, 'catalogo_linha_literal': lit, 'ficha': 'contexto/cursos/graduacao/editais-2027-1.md', 'ficha_editais': 'contexto/cursos/graduacao/editais-2027-1.md', 'ficha_lida_em': None, 'campos_so_na_ficha': [],
                    'visao_de_campanhas': {'arquivo': 'docs/visao-de-campanhas-2026-10-26.md', 'data': '2026-10-26'}, 'plano': 'saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md', 'auditorias': ['docs/auditoria-do-catalogo-2026-10-26.md']},
         'codigo': 'sem-codigo', 'linha': 'graduacao', 'linha_origem': 'catalogo', 'tipo': 'graduacao', 'nome_no_site': nome, 'nome_padrao': nome, 'slug_sugerido': '[CONFIRMAR]', 'aliases': [], 'pagina_oficial': '[CONFIRMAR]',
         'area': {'codigo': 'nao_se_aplica', 'nome': 'Graduação', 'natureza': 'plano_do_cmo'}, 'recorte': 'planejar', 'motivo_do_recorte': 'plano próprio da Graduação (decisão 2)', 'onda': 1, 'modo_de_venda': 'com_data', 'grupo_de_campanha': 'vestibular-2027-1',
         'gut': None, 'relacionados': [], 'local': local, 'modalidade': cel[2] if len(cel) > 2 else '[CONFIRMAR]', 'modalidade_normalizada': 'presencial', 'turma': None,
         'carga_horaria': cel[4] if len(cel) > 4 else '[CONFIRMAR]', 'modulos': None, 'inicio': '2027-02-22', 'fonte_da_data': 'edital', 'dias_ate_inicio': (datetime.date(2027, 2, 22) - datetime.date.fromisoformat(HOJE)).days,
         'fim_das_inscricoes': None, 'preco_texto_site': cel[5] if len(cel) > 5 else '[CONFIRMAR]', 'preco_estruturado': None, 'condicoes_especiais': [],
         'status_catalogo': 'aberto', 'status_catalogo_texto': 'inscrições abertas desde 17/08/2026 (edital)', 'vagas': {'turma_minima': 30, 'vagas_ofertadas': None, 'vagas_restantes': None},
         'equipe': {'coordenadores_na_ficha': None, 'docentes_na_ficha': None, 'autorizacoes_de_imagem_registradas': None},
         'status_midia': {'campanha': 'nao_consta', 'formatos': [], 'cinco_angulos': 'nao_consta', 'vinculo_com_a_visao': 'nenhum', 'inicio_na_visao': None, 'divergencia_de_data': False, 'fonte': 'docs/visao-de-campanhas-2026-10-26.md', 'lido_em': '2026-10-26'},
         'kit': {'template': 'templates/kit-de-lancamento-graduacao.md', 'variacao': None, 'escopo': 'item', 'entregas': ent, 'acrescimos': []},
         'canais': canais('graduacao', None), 'arquivos_por_camada': {'geral': [], 'linha': [{'agente': 'cmo', 'caminho': 'saidas/02-estrategia-e-posicionamento/cmo-graduacao-2026-10-26.md', 'secao': None, 'estado': 'pendente_de_aprovacao', 'aprovado_em': None, 'ref_aprovacao': None}], 'area': [], 'curso': []},
         'metas': {'matriculas_alvo': 15, 'cpl_maximo': None, 'custo_por_matricula_maximo': None, 'verba': 2000.00, 'fonte': 'decisões 15 e 16 do briefing'},
         'numeros_agregados': {'leads': None, 'inscricoes': None, 'matriculas': None, 'verba_gasta': None, 'lido_em': None},
         'pendencias': [pend('P1', 'P1', 'certificacao', 'Reconhecimento do curso: texto da regulação ainda não preenchido no contexto da linha', '[CONFIRMAR]', [], ['certificacao'], 'contexto/graduacao.md'),
                        pend('edital', 'editais', 'divergencia', 'Alertas do texto dos editais (datas e numeração) a confirmar com a Ufape', '[CONFIRMAR]', [], [], 'contexto/cursos/graduacao/editais-2027-1.md')],
         'aprovacoes': [{'ref': 'AM1 a AM12 e AG1 a AG11', 'o_que': 'subir as campanhas Meta e Google da Graduação', 'por_que': 'captação do vestibular 2027.1', 'quanto': 'R$ 2.000,00 por curso (decisão 15)', 'efeito_esperado': 'inscrições até o início das aulas', 'como_desfazer': 'pausar as campanhas', 'status': 'pendente', 'pedido_em': HOJE, 'decidido_em': None, 'decidido_por_papel': None}],
         'historico': [{'revisao': 1, 'em': HOJE, 'campo': '*', 'de': None, 'para': 'criação', 'motivo': 'versão 1 do mapa', 'origem': 'gerador do orquestrador sobre o plano do cmo', 'aplicado_por': 'orquestrador'}]}
    j['graduacao'] = {'edital': {'numero': '[CONFIRMAR]', 'titulo': '[CONFIRMAR]', 'url': '[CONFIRMAR]'}, 'edital_de_desconto': {'numero': '[CONFIRMAR]', 'titulo': '[CONFIRMAR]', 'url': '[CONFIRMAR]'},
                      'ato_autorizativo': cel[6] if len(cel) > 6 else '[CONFIRMAR]', 'reconhecimento': '[CONFIRMAR]', 'grau': 'bacharelado' if 'Veterin' in nome else 'licenciatura',
                      'turnos': [], 'formas_de_ingresso': ['redacao', 'enem', 'transferencia_externa', 'diplomado', 'vagas_remanescentes'], 'inscricoes_abertas_desde': '2026-08-17',
                      'inscricao_ate': None, 'inicio_das_aulas': '2027-02-22', 'validade_do_desconto': 'só para o 1º semestre de 2027', 'lp': {'url': '[CONFIRMAR]', 'alterada_pela_squad': False, 'utm': {'gerada_por': 'plataforma', 'parametros': ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term'], 'utm_campaign': '[CONFIRMAR]'}}}
    j['resumo'] = {'pendencias_abertas': 2, 'bloqueado': False}
    res.append(j)

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
print('onda (planejar)', Counter(j['onda'] for j in res if j['recorte'] == 'planejar'))
print('sem área no recorte', [j['id'] for j in res if j['recorte'] == 'planejar' and j['area']['codigo'] == 'sem_area'])
print('ids repetidos', [k for k, v in Counter(j['id'] for j in res).items() if v > 1])
print('bloqueados', sum(j['resumo']['bloqueado'] for j in res))
