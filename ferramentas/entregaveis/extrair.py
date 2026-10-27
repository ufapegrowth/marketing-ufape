"""Separa, no trecho de cada peça, o texto que vai ao público das notas de produção.

Usado por painel.py. A função extrair(linhas) recebe as linhas do trecho da peça
(do começo dela até o próximo título do mesmo nível) e devolve:
  destaques: lista de (rótulo, texto) com gancho, primeira linha, assunto, pré-cabeçalho, chamada
  arte: lista de textos de cada card ou tela da arte
  corpo: lista de parágrafos do texto que vai ao público (as citações "> " do arquivo)
  roteiro: lista de passos de vídeo, quando houver
  notas: o resto do trecho, em markdown, para a seção recolhida de notas de produção
"""
import re

ROTULOS = [
    (r'gancho', 'Gancho'),
    (r'primeira linha', 'Primeira linha'),
    (r'assunto', 'Assunto'),
    (r'pr[ée]-cabe[çc]alho', 'Pré-cabeçalho'),
    (r'texto de pr[ée]-visualiza', 'Pré-visualização'),
    (r'chamada', 'Chamada para ação'),
    (r'cta', 'Chamada para ação'),
    (r'bot[ãa]o', 'Botão'),
    (r't[íi]tulo', 'Título'),
    (r'formato', 'Formato'),
]
ARTE = re.compile(r'^\s*[-*]\s*\**(card|tela|slide|cartão|cart[aã]o)\s*\d+\**\s*[:.]\s*(.*)', re.I)
ROT_LINHA = re.compile(r'^\s*[-*]\s*\*\*([^*]+?)\*\*\s*:?\s*(.*)$')


def limpa(t):
    t = re.sub(r'\s*\((?:A|B|C|D|E|F|G|H|L|M|N|P|R|S|T|U|W)\d+(?:-\d+)?\)\s*$', '', t.strip())
    t = re.sub(r'^"(.*)"$', r'\1', t.strip())
    return t.strip()


def extrair(linhas):
    destaques, arte, corpo, roteiro, notas = [], [], [], [], []
    vistos = set()
    i = 0
    em_arte = False
    par = []
    while i < len(linhas):
        l = linhas[i]
        s = l.strip()
        if s.startswith('>'):
            em_arte = False
            txt = re.sub(r'^>\s?', '', s)
            if txt:
                par.append(txt)
            elif par:
                corpo.append(' '.join(par)); par = []
            i += 1
            continue
        if par:
            corpo.append(' '.join(par)); par = []
        m = ARTE.match(l)
        if m:
            arte.append(limpa(m.group(2)))
            i += 1
            continue
        m = ROT_LINHA.match(l)
        if m:
            rot = m.group(1).strip().rstrip(':').lower()
            val = m.group(2).strip()
            em_arte = rot.startswith('texto da arte') or rot.startswith('telas') or rot.startswith('cards')
            if em_arte and not val:
                i += 1
                continue
            if rot.startswith('roteiro'):
                if val:
                    roteiro.extend([p.strip() for p in re.split(r'\(\d+\)\s*', val) if p.strip()])
                i += 1
                continue
            achou = None
            for pad, nome in ROTULOS:
                if re.match(pad, rot):
                    achou = nome; break
            if achou and val and not rot.startswith(('ganchos alternativos', 'reserva')):
                if achou not in vistos:
                    destaques.append((achou, limpa(val)))
                    vistos.add(achou)
                else:
                    notas.append(l)
                i += 1
                continue
        mg = re.match(r'^\s*[-*]\s*Gancho\s*(\(tela 1\))?\s*:\s*(.*)', l, re.I)
        if mg and 'Gancho' not in vistos:
            destaques.append(('Gancho', limpa(mg.group(2)))); vistos.add('Gancho')
            i += 1
            continue
        mr = re.match(r'^\s*[-*]\s*Roteiro\s*:\s*(.*)', l, re.I)
        if mr:
            roteiro.extend([p.strip() for p in re.split(r'\(\d+\)\s*', mr.group(1)) if p.strip()])
            i += 1
            continue
        notas.append(l)
        i += 1
    if par:
        corpo.append(' '.join(par))
    corpo = [c for c in corpo if c.strip()]
    return {'destaques': destaques, 'arte': arte, 'corpo': corpo, 'roteiro': roteiro, 'notas': '\n'.join(notas).strip()}


def trecho(texto, linha, limite=160):
    """Linhas da peça: do título dela até o próximo título do mesmo nível ou acima."""
    L = texto.split('\n')
    a = max(0, linha - 1)
    ini = L[a] if a < len(L) else ''
    if ini.strip().startswith('|'):
        h = a
        while h > 0 and L[h - 1].strip().startswith('|'):
            h -= 1
        cab = L[h:h + 2] if h + 1 < a else []
        return 'tabela', cab + [L[a]]
    m = re.match(r'^(#+)\s', ini)
    nivel = len(m.group(1)) if m else None
    b = a + 1
    while b < len(L) and b - a < limite:
        mm = re.match(r'^(#+)\s', L[b])
        if mm and (nivel is None or len(mm.group(1)) <= nivel):
            break
        b += 1
    return 'bloco', L[a:b]
