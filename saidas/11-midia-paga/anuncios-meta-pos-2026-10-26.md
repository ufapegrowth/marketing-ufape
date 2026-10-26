# Estrutura de Meta Ads da Pós-graduação: provas de bolsa, pós-prova, turmas de março e de abril (etapa 1.14)

- **Agente:** anuncios-meta (departamento 11 Mídia Paga, por encomenda do gestor-de-midia)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Etapa:** 1.14 da camada 1 do plano do cmo (seção 4), encomenda da seção 7 de saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md e da seção 4 de saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md
- **Status:** rascunho para o qa-de-marketing (auditorias/11-midia-paga.md e auditorias/conformidade-educacional.md) e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda linha de montagem é um pedido para um humano executar no Gerenciador de Anúncios, depois da aprovação.
- **Entradas lidas:**
  - /home/user/marketing-ufape/.claude/agents/anuncios-meta.md
  - /home/user/marketing-ufape/.claude/skills/estrutura-de-campanha-paga/SKILL.md
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 13)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 12 (conciliação da camada 1)
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seções 2 e 3) e as fichas de contexto/cursos/pos/ das 11 turmas de março e abril (só a URL oficial e a coordenação)
  - /home/user/marketing-ufape/docs/visao-de-campanhas-2026-10-26.md
  - /home/user/marketing-ufape/saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (1.13, entrada principal)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (1.11, seções 3, 4, 7, 8 e 9)
  - /home/user/marketing-ufape/saidas/11-midia-paga/analise-de-midia-pos-2026-10-26.md (1.12, seções 0, 5, 9 e 10)
  - /home/user/marketing-ufape/saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-26.md (seções 0 a 4, 6 e 7)
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md
- **Regra de conflito:** as entradas podem estar sendo atualizadas em paralelo com a seção 12 do plano do cmo. Onde houver diferença, vale a seção 12. A numeração do pedido (D13 mídia, D14 UTM e nomes, D15 frase do curso livre) corresponde, no arquivo lido, à seção 12.6 (mídia), a D11 e D12 (UTM e nomes) e a D13 (frase do curso livre). Usei o conteúdo dessas seções.
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web nesta etapa.
- **Dados pessoais:** nenhum. Nenhum aluno, candidato ou lead aparece. Nenhum docente é nomeado aqui: onde o texto prevê docente, fica o campo {docente da ficha}, preenchido com nome e titulação exatamente como na ficha (autorização registrada, decisões 8 e 10).
- **Marcadores:** [CONFIRMAR] é número ou fato que a Ufape ou o gerenciador precisa informar. [CONFIRMAR NO CATÁLOGO] é dado de curso fora do catálogo. [SUPOSIÇÃO] é escolha de desenho ou regra de plataforma sem fonte nos arquivos. [DADO NÃO FORNECIDO] é número de mídia que não existe. Nenhum valor de verba, CPL, CPC, tamanho de público, alcance, leads ou inscritos existe hoje: verba aparece como percentual da verba nova da Pós (VN) e o valor em reais é sempre VN x percentual [CONFIRMAR].

---

## 0. Resumo em cinco linhas

1. Montagem de 1 campanha Meta das provas (3 conjuntos, orçamento no conjunto), 1 campanha de pós-prova (remarketing por turma de destino), 2 campanhas Meta por turma de março (5 turmas) e de abril lote 1 (6 turmas), todas com nome e UTM no padrão D11 e D12 da seção 12.
2. A seção 12 muda três coisas em relação às entradas: as provas são **online**, com o campus (São Paulo ou Goiânia) sempre dito, e nenhum texto cita endereço, "presencial", documento com foto ou celular; a UTM das provas passa a `utm_source=meta` e `utm_medium=paid_social` desde a subida de 03/11; a turma mínima é 15.
3. Os textos dos criativos de 26/10 que dizem "prova presencial" não sobem como estão: este arquivo entrega o texto reescrito de cada conceito (C1, C2, C3, C4 e C6) e o pedido de correção das páginas das provas, que ainda dizem "presencial".
4. Verba só em percentual de VN (seções 3.1 a 3.3 da 1.13); evento de otimização compra nas provas e cadastro ou início de checkout nas turmas, conforme o teste de rastreio de 30/10.
5. Doze pedidos de aprovação (AMP1 a AMP12), cada um com o que, por que, quanto, efeito e como desfazer; nada sobe antes de PP1 (metas) e PP2 (verba).

---

## 1. Regras que valem para toda a montagem

| Regra | Valor nesta montagem | Fonte |
|---|---|---|
| Prova de bolsa | Online. Toda peça diz o campus da prova (São Paulo ou Goiânia). Sem endereço, sem "presencial", sem documento com foto, sem "sem celular". Data e horário como na ficha: 27/11/2026, das 9h às 13h. Acesso online: [CONFIRMAR, U2] | decisão 11; seção 12.9 |
| Turma mínima | 15 alunos, na prova e nas turmas. Só entra no anúncio de turma se a página da turma já disser 15 (algumas páginas ainda dizem 20) [CONFIRMAR por página] | decisão 11; contexto/pos-graduacao.md |
| Certificação | Nenhuma frase de certificação, nenhuma menção ao MEC | briefing; conformidade |
| Urgência | Nenhum "últimas vagas", "vagas limitadas", contador ou "termina hoje". A data da prova é fato e pode aparecer | briefing; conformidade |
| Bolsa | Só nas provas e no pós-prova, sempre com a distribuição completa (2 de 50% com monitoria, 4 de 25%, 5 de 10%) e "Bolsa não acumulativa e intransferível". Anúncio de turma não fala de bolsa | criativos-de-anuncio-pos, 1.1 a 1.3; 1.13, 4.1 |
| Crédito e ponte Livres para Pós | Nenhuma menção a crédito, combo ou desconto da ponte | D7 da seção 12.4 |
| Preço de turma | Sempre com número de parcelas, valor da parcela, total e matrícula, como no catálogo. Nenhum valor com bolsa ou desconto calculado. 341 sem a promoção de 20% até a regra completa (PP7) | catálogo, seção 2; 1.13, 4.1 |
| Nome do curso | Sempre "Pós-graduação em <área>" no texto visível. Marca "Faculdade UFAPE" (homonímia com a universidade federal) | 1.13, 4.1 |
| Quem vê | Nenhum texto afirma ou insinua característica de quem vê. O texto descreve a situação de uso | conformidade, bloco de anúncios |
| Destino | Sempre a página da prova ou da turma, com UTM. Nunca WhatsApp, nunca formulário instantâneo (seção 6) | gestor-de-midia-pos, 3 |
| Nomes | Campanha = chave + `_<plataforma>_<objetivo>_<público>_<AAAAMM>`; chave = `pos_<código>` ou `pos_provas20261127`. Conjunto = nome da campanha + `__` + público. Anúncio = `<código ou conceito>_<formato>_<gancho>_vN`. Minúsculas, sem acento, hífen dentro do bloco, sublinhado entre blocos | D12 |
| UTM | `utm_source=meta`, `utm_medium=paid_social`, `utm_campaign` = nome da campanha, `utm_content` = nome do anúncio, `utm_term` = público. Nenhum dado pessoal | D11 e D12 |
| Campanhas já no ar | 289, 662 e a reta final de 707, 68604, 68606, 698, 68610 e 68608 não são renomeadas; a análise lê por tabela de correspondência | D12, último item |
| Sobreposição | Sem exclusão de público entre campanhas e sem anúncio que misture ofertas. Registro lado a lado de CPM, alcance e frequência (EA3) | seção 12.6 |

**Divergência resolvida pela seção 12 (nota para quem monta):** a 1.13 (seção 4.2) usava a área curta na chave (`pos_68615-patclin_...`) e mantinha a UTM antiga das provas (`utm_medium=pago`, `utm_campaign=provas-de-bolsa-2026-11-27`). D11 e D12 mandam a chave só com o código (`pos_68615_...`) e o padrão `meta` e `paid_social` também nas provas, porque os anúncios das provas ainda não subiram. Este arquivo segue D11 e D12.

---

## 2. Modelo de estrutura (skill estrutura-de-campanha-paga, passo 2)

| Frente | Modelo | Motivo (2 a 3 linhas) |
|---|---|---|
| P1 Provas | Lançamento por fases, em 1 campanha de vendas com 3 conjuntos | Data fixa (27/11) e fases já escritas (40%, 35%, 25%, PP3). Um conjunto por praça e um de remarketing porque São Paulo, Goiânia e visitantes têm tamanhos muito diferentes; com orçamento na campanha, o algoritmo levaria quase tudo para São Paulo (EM5) |
| P2 Pós-prova | Enxuta: 1 campanha de remarketing, 1 conjunto por turma de destino confirmada | Público pequeno (visitantes das páginas da prova e da turma) e janela curta (10 dias úteis) |
| P3 Março e P4 Abril | Lançamento por fases, por turma: 1 campanha de público frio e 1 de remarketing, orçamento na campanha com 1 conjunto | Meta e verba por turma (CPLmax_h); a manutenção de fim de ano desliga só o frio sem mexer no remarketing (EM3) |

Orçamento: nas provas, no conjunto; nas turmas e no pós-prova, na campanha. Nunca nos dois. Motivo na tabela acima.

---

## 3. Mapa das campanhas (árvore campanha, conjunto, anúncio)

### 3.1 P1 Provas de bolsa (sobe em 03/11, pausa em 27/11)

```
pos_provas20261127_meta_compra_misto18_202611   (objetivo Vendas; orçamento no conjunto)
├── pos_provas20261127_meta_compra_misto18_202611__amplo18-sp
│     anúncios por área liberada (E1 em 03/11; E2 com decisão registrada):
│     c1-bolsas_<área>_e11_numero_v1, c1-bolsas_<área>_e916_numero_v1,
│     c2-entrada_<área>_e11_numero_v1, c2-entrada_<área>_e916_numero_v1,
│     c2-entrada_<área>_vid916_pergunta_v1 (se o vídeo estiver pronto),
│     c6-rotina_<área>_e11_cena_v1, c6-rotina_<área>_e916_cena_v1
├── pos_provas20261127_meta_compra_misto18_202611__amplo18-go
│     mesmos conceitos, com <área>-go (a1-anest-go, a4-cirurgia-go; a2-cardio-go só depois da correção dos links)
│     sobe só com a página de Goiânia dizendo prova online e campus Goiânia (AMP5)
└── pos_provas20261127_meta_compra_misto18_202611__rmk30d
      c4-regra_<área>_car_pergunta_v1 (carrossel "Como funciona")
      estático de remarketing da área (seção 5.6)
```

Em 10/11 (fase 2) entram, por pedido, C3 reescrito (seção 5.4, só com U2 respondido), as iterações do vencedor (uma variável por vez) e as áreas de E5 com destino confirmado. C5 fica travado até A-C2.

| Campo | Valor |
|---|---|
| Objetivo da campanha | Vendas |
| Evento de otimização | Compra (inscrição de R$ 100,00) no pixel e na API de Conversões. Se o teste de 30/10 não mostrar a compra disparando, ou se a 1ª semana não registrar compra com volume, troca única para início de checkout, com aprovação (memorando 3.2; AMP3) |
| Categoria especial de anúncio | Nenhuma [SUPOSIÇÃO: educação não está entre as categorias especiais da Meta; conferir no gerenciador ao criar] |
| Idade | 18 anos ou mais |
| Região | __amplo18-sp: estado de São Paulo. __amplo18-go: Goiás e Distrito Federal. __rmk30d: sem recorte (EM6) |
| Público frio | Amplo, com sugestão de interesses profissionais ligados à medicina veterinária (Advantage+ de público, se a conta usar) [SUPOSIÇÃO de nome do recurso; conferir no gerenciador] |
| Remarketing | Visitantes das páginas de Pós e das provas nos últimos 30 dias (pixel) e quem engajou com o Instagram @ufapevet em 90 dias |
| Exclusões | Compradores da inscrição (evento de compra do pixel nas páginas das provas, 180 dias). Os conjuntos frios excluem __rmk30d. Nenhuma lista de contatos até a base legal [CONFIRMAR] |
| Posicionamentos | Facebook e Instagram: Feed, Stories, Reels e Explorar. Sem Audience Network e sem Messenger [SUPOSIÇÃO de desenho: leitura por posicionamento e controle de onde a marca aparece; se o gerenciador marcar o público como pequeno, voltar aos posicionamentos automáticos com aprovação] |
| Limite de frequência | Em objetivo de Vendas o limite fixo pode não estar disponível [SUPOSIÇÃO de plataforma; conferir]. Controle por leitura diária de frequência e troca de anúncio (EM12) |
| Data de término programada | 26/11/2026, 23h59, nos três conjuntos (pausa de A-C6 confirmada em 23/11) |

### 3.2 P2 Pós-prova (sobe na data do resultado [CONFIRMAR], pausa no fim dos 10 dias úteis)

```
pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM do resultado>   (Vendas; orçamento na campanha)
└── um conjunto por turma de destino confirmada: ...__rmk-prova-<código da turma>
      c5-turma_<área>_e11_resultado_v1 (só depois de A-C2)
      <código da turma>-c2-investimento_e11_numero_v1 (seção 5.8)
```

Observação de nome: a chave `pos_provas20261127-matricula` é a da 1.13 (seção 4.6). D12 não prevê chave para o pós-prova; proponho mantê-la para separar a leitura da inscrição da leitura da matrícula (AMP6).

| Campo | Valor |
|---|---|
| Evento | Compra do produto da turma de destino; se não houver volume, início de checkout |
| Público | Visitantes, em 30 dias, da página da prova da área e da página da turma de destino. É público de visitantes, não de aprovados: o texto vale para quem fez e para quem não fez a prova |
| Exclusões | Compradores da turma de destino (pixel, 180 dias) |
| Texto | Sem prazo de matrícula até U1 e U3 responderem; sem valor com bolsa; com o investimento completo da turma |

### 3.3 P3 Turmas de março (68615, 289 e 333 em 07/12; 657 e 341 em 14/12, só com PP7)

Por turma, duas campanhas (o Google é do anuncios-google):

```
pos_<código>_meta_lead_amplo18-<praça>_202612   (Vendas ou Leads, conforme o evento de EM11; orçamento na campanha)
└── pos_<código>_meta_lead_amplo18-<praça>_202612__amplo18-<praça>
      <código>-c1-rotina_e11_cena_v1, <código>-c1-rotina_e916_cena_v1
      <código>-c3-docente_e11_cena_v1 (docente da ficha, nome e titulação como na ficha)
pos_<código>_meta_lead_rmk30d_202612
└── pos_<código>_meta_lead_rmk30d_202612__rmk30d
      <código>-c2-investimento_e11_numero_v1
      <código>-c4-formato_car_pergunta_v1 (como funciona o semipresencial; 68632 é presencial)
```

Em 21/12 a campanha de frio pausa (manutenção, PP10). Em 04/01 volta como campanha nova `pos_<código>_meta_lead_amplo18-<praça>_202701` se passar na condição de volume (1.13, 3.4). O remarketing segue sem pausa.

| Turma | Campanha de frio | Campanha de remarketing | Região do frio | Fonte do remarketing (30 dias) |
|---|---|---|---|---|
| 68615 | pos_68615_meta_lead_amplo18-sp_202612 | pos_68615_meta_lead_rmk30d_202612 | estado de SP | página de 68615 e da prova 68658; engajamento Instagram 90 dias |
| 289 | pos_289_meta_lead_amplo18-go_202612 | pos_289_meta_lead_rmk30d_202612 | GO e DF | página de 289 e, depois da correção dos links, da prova 68642 |
| 333 | pos_333_meta_lead_amplo18-sp_202612 | pos_333_meta_lead_rmk30d_202612 | estado de SP | página de 333 e da prova 68658 |
| 657 | pos_657_meta_lead_amplo18-sp_202612 | pos_657_meta_lead_rmk30d_202612 | estado de SP | página de 657 |
| 341 | pos_341_meta_lead_amplo18-sp_202612 | pos_341_meta_lead_rmk30d_202612 | estado de SP | página de 341 |

Interesses sugeridos no frio [SUPOSIÇÃO, 1.13 4.4]: medicina veterinária em todas; anestesiologia veterinária em 657; equinos em 341. Exclusões: compradores da turma (180 dias); o frio exclui o remarketing da turma; durante a janela de P2, o remarketing de 68615 e 333 exclui visitantes da prova 68658 (ficam com P2) (EM7).

289 já tem campanha ativa: não é renomeada (D12). A diária atual segue sem aumento até 06/12 e é descontada da parte de 289 em P3 (EM9, R5). Em 07/12, a pessoa do marketing decide se a campanha atual vira a de frio de 289 (mantendo o nome antigo e trocando só a UTM) ou se ela é pausada e as duas campanhas novas sobem. Recomendação: pausar a atual, com exportação, e subir as duas novas, para ter frio e remarketing separados [SUPOSIÇÃO de desenho, AMP7].

### 3.4 P4 Turmas de abril, lote 1 (sobem em 06/01, PP11)

Mesmo desenho de março, com `_202701` e sem manutenção.

| Turma | Situação hoje | Campanha de frio | Campanha de remarketing | Bloqueio antes de subir |
|---|---|---|---|---|
| 68635 | pausada (reativar) | pos_68635_meta_lead_amplo18-sp_202701 | pos_68635_meta_lead_rmk30d_202701 | meta de PP1 e página sem pendência |
| 68636 | não consta na visão | pos_68636_meta_lead_amplo18-sp_202701 | pos_68636_meta_lead_rmk30d_202701 | data 17/04/2027 só no site: [CONFIRMAR] na planilha |
| 68617 | pausada (reativar) | pos_68617_meta_lead_amplo18-sp_202701 | pos_68617_meta_lead_rmk30d_202701 | peças sem número de turma (diverge entre planilha e site) |
| 68628 | sem campanha | pos_68628_meta_lead_amplo18-sp_202701 | pos_68628_meta_lead_rmk30d_202701 | peças sem número de turma |
| 68609 | sem campanha | pos_68609_meta_lead_amplo18-go_202701 | pos_68609_meta_lead_rmk30d_202701 | remarketing da prova 68640 só depois da página de Goiânia corrigida |
| 68632 | sem campanha | pos_68632_meta_lead_amplo18-go_202701 | pos_68632_meta_lead_rmk30d_202701 | anúncio diz "presencial", nunca "semipresencial" |

As campanhas pausadas de 68635 e 68617 não são renomeadas (D12): a recomendação é deixá-las pausadas e subir as novas no padrão, para não herdar público, verba e nome antigos [SUPOSIÇÃO de desenho; AMP8].

---

## 4. Verba por campanha (percentual de VN; reais = VN x percentual [CONFIRMAR])

Todos os percentuais vêm da 1.13 (seções 3.1 a 3.3). Diária = parte da fase dividida pelos dias da fase.

### 4.1 P1 Provas, Meta, por conjunto e fase

| Fase (dias) | __amplo18-sp | __amplo18-go | __rmk30d | Total Meta da fase | Diária SP / GO / rmk (em VN) |
|---|---|---|---|---|---|
| 1. 03/11 a 09/11 (7) | 5,8800% | 1,2600% | 1,2600% | 8,4000% | 0,8400% / 0,1800% / 0,1800% |
| 2. 10/11 a 19/11 (10) | 4,7775% | 1,1025% | 1,4700% | 7,3500% | 0,4778% / 0,1103% / 0,1470% |
| 3. 20/11 a 26/11 (7) | 2,2500% | 0,4500% | 1,8000% | 4,5000% | 0,3214% / 0,0643% / 0,2571% |
| **Total** | 12,9075% | 2,8125% | 4,5300% | **20,2500%** | |

Enquanto Goiânia estiver bloqueada, a parte de __amplo18-go passa para __amplo18-sp na mesma fase (1.13, 3.1). Área bloqueada não guarda verba. Leads por semana esperados = verba semanal do conjunto dividida pelo CPImax da área [CONFIRMAR em PP1]; sem CPImax, [DADO NÃO FORNECIDO]. Condição de volume da 1.13: VN mínima = 50 x CPImax com 4 conceitos, ou 25 x CPImax na versão enxuta (só C1 e C6).

### 4.2 P2 Pós-prova

5,00% de VN no total, em partes iguais por turma de destino confirmada. Diária = 5% de VN dividido pelos dias corridos da janela [CONFIRMAR data do resultado] e pelo número de turmas de destino.

### 4.3 P3 e P4, por turma e por semana

| Frente e fase | Frio por semana | Remarketing por semana | Diária frio / remarketing |
|---|---|---|---|
| Março, aquecimento 07/12 a 20/12 (com YouTube, PP13) | 0,4200% | 0,1050% | 0,0600% / 0,0150% |
| Março, aquecimento (sem YouTube) | 0,4900% | 0,1225% | 0,0700% / 0,0175% |
| Março, manutenção 21/12 a 03/01 | 0% | 0,1750% | 0% / 0,0250% |
| Março, conversão 04/01 a 24/01 (com YouTube) | 0,5005% | 0,3337% | 0,0715% / 0,0477% |
| Março, conversão (sem YouTube) | 0,5915% | 0,3943% | 0,0845% / 0,0563% |
| Abril lote 1, 06/01 a 24/01 | 0,5158% | 0,1289% | 0,0737% / 0,0184% |

Conta da linha "sem YouTube" (aritmética sobre a 1.13, 3.3): aquecimento 1,225% de VN por turma em 2 semanas, 80/20; conversão 2,9575% em 3 semanas, 60/40. Turma bloqueada deixa a parte em P6. Condição de volume (1.13, 3.4): março, Meta, VN mínima de 152,15 a 285,71 x CPLmax_h; abril, 232,65 x CPLmax_h. Se não fechar, a turma sobe só com remarketing.

---

## 5. Anúncios (entregável padrão por criativo)

Contagem de caracteres: a primeira frase do texto principal aparece entre parênteses, seguida do número de caracteres. Títulos até 40 e descrições até 30 (referência de plataforma [SUPOSIÇÃO]; conferir a prévia no gerenciador). Em Stories e Reels a mensagem está dentro da arte: o texto principal complementa. Quando a primeira frase passa de cerca de 125 caracteres (textos em lista e de investimento), só o começo aparece antes do "ver mais": por isso esses textos põem curso, data e preço logo no início.

Exemplos preenchidos com as duas provas que sobem em 03/11 sem pendência (E1): 68654 Neurologia e 68658 Patologia Clínica. As demais áreas usam o mesmo texto, trocando {nome curto} e {nome completo} pela tabela da seção 4.1 do criativos-de-anuncio-pos e o campus pela praça da prova.

### 5.1 Corpo fixo das provas (substitui BODY_SP e BODY_GO do criativos-de-anuncio-pos)

- **Corpo São Paulo:** "Prova de bolsa do campus São Paulo da Faculdade UFAPE, online, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). São 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Bolsa não acumulativa e intransferível. Regras completas na página da prova."
- **Corpo Goiânia:** igual, com "campus Goiânia". Sem endereço. Sem prazo de matrícula e sem canal do resultado nas provas 68642 e 68644 (as páginas se contradizem, U1).
- **Fica de fora de todo texto das provas:** "presencial", endereço, "documento com foto", "sem celular", "sem relógio", data do resultado, prazo de inscrição, turma de destino (até A-C2).

### 5.2 C1. 11 bolsas por prova (frio, São Paulo e Goiânia)

Nomes: `c1-bolsas_a12-neuro_e11_numero_v1`, `c1-bolsas_a11-patclin_e11_numero_v1` e as versões e916.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | Prova de bolsa de Neurologia: 11 bolsas, de 10% a 50%. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia: 11 bolsas, de 10% a 50%." (54) |
| 2 | Curto, pergunta | Quantas bolsas tem a prova de Patologia Clínica? São 11 por prova. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Quantas bolsas tem a prova de Patologia Clínica?" (48) |
| 3 | Lista de benefícios (longo) | 11 bolsas na prova da Pós-graduação em Neurologia e Neurocirurgia Veterinária. 2 bolsas de 50%, com monitoria. 4 bolsas de 25%. 5 bolsas de 10%. Nota de corte 7,0, com questões de múltipla escolha e dissertativas. Desempate por análise de currículo. + corpo São Paulo | "11 bolsas na prova da Pós-graduação em Neurologia e Neurocirurgia Veterinária." (78) |
| 4 | Objeção primeiro | Não é uma bolsa só: a prova de Patologia Clínica tem 11, de 10% a 50%. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Não é uma bolsa só: a prova de Patologia Clínica tem 11, de 10% a 50%." (70) |
| 5 | Curto, data | Sexta, 27/11: prova de bolsa online de Neurologia, com 11 bolsas. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. Regras na página da prova. | "Sexta, 27/11: prova de bolsa online de Neurologia, com 11 bolsas." (65) |

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova de bolsa: Neurologia" (26) | "Inscrição de R$ 100,00" (22) |
| "11 bolsas por prova" (19) | "Prova online em 27/11" (21) |
| "Bolsas de 10% a 50%, na distribuição" (36) | "Campus São Paulo" (16) |
| "Prova online de bolsa em 27/11" (30) | |
| "Prova de bolsa: Patologia Clínica" (33) | |

O título "Bolsas de 10% a 50%, na distribuição" só vai junto de texto principal que traga a distribuição completa (todos os cinco trazem). Para Goiânia, a descrição "Campus Goiânia" (14).

- **Chamada:** "Saiba mais". Motivo: o frio ainda não conhece a prova; "Saiba mais" leva à página com as regras, e o botão da página é "COMPRAR".
- **Combinação para o 1º teste (T1 do criativos):** arte `c1-bolsas_<área>_e11_numero_v1` + texto 1 + título "Prova de bolsa: {nome curto}" + descrição "Inscrição de R$ 100,00", contra a combinação de C2 da seção 5.3. Mesmo conjunto, mesma área, mesmo formato.

### 5.3 C2. R$ 100,00 para concorrer (frio)

Nomes: `c2-entrada_<área>_e11_numero_v1`, `_e916_numero_v1`, `_vid916_pergunta_v1`.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | Concorrer a uma bolsa da Pós-graduação em Neurologia e Neurocirurgia Veterinária custa R$ 100,00. É a inscrição na prova online do campus São Paulo, em 27/11/2026: Pix, boleto ou 1x no cartão. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Concorrer a uma bolsa da Pós-graduação em Neurologia e Neurocirurgia Veterinária custa R$ 100,00." (97) |
| 2 | Curto, pergunta | Quanto custa concorrer a uma bolsa de pós-graduação? R$ 100,00. Prova online de Patologia Clínica, campus São Paulo, em 27/11/2026, das 9h às 13h. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Quanto custa concorrer a uma bolsa de pós-graduação?" (52) |
| 3 | Problema, agitação e solução (longo) | O valor total de uma pós-graduação pesa na decisão. A prova de bolsa existe para isso: com a inscrição de R$ 100,00, você concorre a uma das 11 bolsas da prova de Neurologia. São 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. A inscrição é só a entrada na prova: as condições da pós estão na página da turma. + corpo São Paulo | "O valor total de uma pós-graduação pesa na decisão." (51) |
| 4 | Antes, depois e ponte | Hoje: o preço cheio da pós. Depois da prova: a chance de uma bolsa de 10% a 50%. A ponte é a inscrição de R$ 100,00 na prova online de Patologia Clínica, campus São Paulo, em 27/11/2026. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Hoje: o preço cheio da pós." (27) |
| 5 | Curto, número | R$ 100,00 para concorrer a uma das 11 bolsas da prova de Neurologia. Prova online, campus São Paulo, 27/11/2026. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "R$ 100,00 para concorrer a uma das 11 bolsas da prova de Neurologia." (68) |

Cuidado de verdade nos textos 3 e 4: nenhum diz que a bolsa é certa nem que R$ 100,00 é o único custo; "a chance" e "concorre" descrevem o que a inscrição dá. O texto 3 fala do preço da pós de forma geral, sem afirmar a situação financeira de quem lê.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "R$ 100,00 para concorrer" (24) | "11 bolsas por prova" (19) |
| "Inscrição de R$ 100,00 na prova" (31) | "Prova online em 27/11" (21) |
| "Prova de bolsa: Neurologia" (26) | "Bolsas de 10% a 50%" (19) |
| "Bolsa de pós-graduação: R$ 100,00" (33) | |
| "Prova em 27/11: Patologia Clínica" (33) | |

- **Chamada:** "Saiba mais" (mesmo motivo de C1).
- **Combinação para o 1º teste:** `c2-entrada_<área>_e11_numero_v1` + texto 5 + título "R$ 100,00 para concorrer" + descrição "11 bolsas por prova". O vídeo `c2-entrada_<área>_vid916_pergunta_v1` entra com o texto 2 se estiver pronto em 03/11.
- **Vídeo (roteiro da seção 3.8 do criativos):** o quadro de 8 a 14 s muda para "Prova online / Sexta, 27/11/2026, das 9h às 13h / Campus São Paulo" e a locução opcional para "A prova é online, em 27 de novembro, das 9 às 13 horas." Sai "Documento com foto".

### 5.4 C3 reescrito. Prova online, 27/11, das 9h às 13h (fase 2, só com U2 respondido)

O conceito original (logística da prova presencial, local, documento e celular) deixou de ser verdade com a decisão 11. A versão reescrita mantém o ângulo "economia de incerteza", agora sobre o formato online e o campus. Sobe em 10/11 só se a Ufape responder U2 (plataforma, acesso e regras do dia) e a página da prova disser "online". Nomes: `c3-online_<área>_e916_data_v1`, `c3-online_<área>_e11_data_v1`.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto, data | Sexta, 27/11, das 9h às 13h: a prova de bolsa de Neurologia é online. Campus São Paulo. Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Sexta, 27/11, das 9h às 13h: a prova de bolsa de Neurologia é online." (69) |
| 2 | Curto, pergunta | Como é a prova de bolsa de Patologia Clínica? Online, em 27/11/2026, das 9h às 13h. Questões de múltipla escolha e dissertativas. Nota de corte 7,0. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Como é a prova de bolsa de Patologia Clínica?" (45) |
| 3 | Lista (longo) | Prova de bolsa de Neurologia, em 4 pontos. 1. Online, em 27/11/2026, das 9h às 13h. 2. Questões de múltipla escolha e dissertativas. 3. Nota de corte 7,0; desempate por análise de currículo. 4. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Campus São Paulo. Inscrição de R$ 100,00. Como acessar a prova: na página da prova [CONFIRMAR U2]. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia, em 4 pontos." (42) |
| 4 | Objeção primeiro | A prova é online: o campus indica a turma, não o lugar da prova. Prova de bolsa de Patologia Clínica, campus São Paulo, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "A prova é online: o campus indica a turma, não o lugar da prova." (64) |
| 5 | Curto direto | Prova de bolsa online, campus São Paulo: Neurologia, 27/11. Das 9h às 13h. Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Prova de bolsa online, campus São Paulo: Neurologia, 27/11." (59) |

O texto 4 traduz a decisão 11 ("o local não importa, mas a peça diferencia o campus"); a formulação "o campus indica a turma" é leitura deste agente [SUPOSIÇÃO] e vai à Ufape junto com U2 antes de subir.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova online em 27/11" (21) | "Das 9h às 13h" (13) |
| "Prova de bolsa online: Neurologia" (33) | "Campus São Paulo" (16) |
| "Das 9h às 13h, online" (21) | "Inscrição de R$ 100,00" (22) |
| "Como é a prova de bolsa" (23) | |
| "Prova online: Patologia Clínica" (31) | |

- **Chamada:** "Saiba mais".
- **Arte 9:16 (sequência de 3 Stories), troca dos quadros do criativos:** quadro 1 "Prova de bolsa online / Sexta, 27/11/2026 / Das 9h às 13h"; quadro 2 "Múltipla escolha e dissertativas / Nota de corte 7,0"; quadro 3 "Campus São Paulo (ou Goiânia) / Inscrição de R$ 100,00 / 11 bolsas por prova". Sem endereço.

### 5.5 C4. Nota de corte 7,0 e carrossel "Como funciona" (remarketing)

Nomes: `c4-regra_<área>_car_pergunta_v1` (carrossel) e `c4-regra_<área>_e11_pergunta_v2` (iteração de formato, fase 2).

**Troca no carrossel do criativos (seção 3.7):** cartão 3 passa a "2. A prova / 27/11/2026, das 9h às 13h / Online. Campus São Paulo (ou Goiânia)", título do cartão "Prova online em 27/11" (21). Cartão 6 (resultado, recurso, matrícula) continua travado até U1 e U3. Nenhum cartão cita endereço, documento ou celular.

| # | Estrutura | Texto principal | Primeira frase |
|---|---|---|---|
| 1 | Curto, pergunta | Como funciona a prova de bolsa de Neurologia, passo a passo. Inscrição de R$ 100,00, prova online em 27/11/2026, das 9h às 13h, e 11 bolsas por prova. Passe os cartões. Bolsa não acumulativa e intransferível. | "Como funciona a prova de bolsa de Neurologia, passo a passo." (60) |
| 2 | Curto, número | Nota de corte 7,0: é o que a prova de bolsa de Patologia Clínica exige. Mínimo de 70% de acerto. Prova online, campus São Paulo, 27/11/2026. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Nota de corte 7,0: é o que a prova de bolsa de Patologia Clínica exige." (71) |
| 3 | Objeção primeiro (longo) | E se empatar? Na prova de bolsa de Neurologia, o desempate é por análise de currículo. A nota de corte é 7,0 (mínimo de 70% de acerto), em questões de múltipla escolha e dissertativas. Atingir a nota não garante bolsa: a distribuição das 11 bolsas segue as regras da página da prova. + corpo São Paulo | "E se empatar?" (13) |
| 4 | Lista | Prova de bolsa de Patologia Clínica: inscrição de R$ 100,00; prova online em 27/11, das 9h às 13h; nota de corte 7,0; 11 bolsas (2 de 50% com monitoria, 4 de 25%, 5 de 10%). Campus São Paulo. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Patologia Clínica: inscrição de R$ 100,00; prova online em 27/11, das 9h às 13h; nota de corte 7,0; 11 bolsas (2 de 50% com monitoria, 4 de 25%, 5 de 10%)." (173) |
| 5 | Curto direto, remarketing | A prova de bolsa de Neurologia é em 27/11/2026, das 9h às 13h, online. Veja as regras e inscreva-se. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "A prova de bolsa de Neurologia é em 27/11/2026, das 9h às 13h, online." (70) |

O texto 4 é uma frase única longa: só os primeiros cerca de 125 caracteres aparecem antes do "ver mais", e eles já trazem inscrição, data e nota. Uso só no estático, não no carrossel.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Como funciona a prova de bolsa" (30) | "Desempate por currículo" (23) |
| "Nota de corte 7,0" (17) | "Inscrição de R$ 100,00" (22) |
| "Prova de bolsa em 27/11" (23) | "Prova online em 27/11" (21) |
| "Regras da prova de bolsa" (24) | |
| "Prova online: Neurologia" (24) | |

- **Chamada:** "Inscreva-se" no remarketing [SUPOSIÇÃO: rótulo disponível na lista de chamadas da Meta; se não houver, "Saiba mais"]. Motivo: quem já visitou a página conhece a prova; a chamada combina com a ação da página (comprar a inscrição).
- **Combinação para o 1º teste (T3 do criativos):** carrossel com o texto 1 + título "Como funciona a prova de bolsa" + descrição "Inscrição de R$ 100,00", contra `c1-bolsas_<área>_e11_numero_v1` com o texto 1 de C1, no conjunto __rmk30d.

### 5.6 C6. Rotina da especialidade (camada de área, frio)

Nomes: `c6-rotina_<área>_e11_cena_v1`, `_e916_cena_v1`, `_e11_numero_v2` (iteração, fase 2). Os ganchos de rotina vêm do criativos (seção 4.2) e são [SUPOSIÇÃO] de tema, não fala de aluno.

| # | Estrutura | Texto principal (Neurologia, 68654) | Primeira frase |
|---|---|---|---|
| 1 | História curta da rotina (gancho B) | O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11. Prova de bolsa para a Pós-graduação em Neurologia e Neurocirurgia Veterinária. + corpo São Paulo | "O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (89) |
| 2 | Curto, número (gancho A) | Neurologia: 11 bolsas por prova, inscrição de R$ 100,00. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Neurologia: 11 bolsas por prova, inscrição de R$ 100,00." (56) |
| 3 | Lista de benefícios | Prova de bolsa de Neurologia: o que você encontra na página. Data e horário (27/11/2026, das 9h às 13h, online). As 11 bolsas e a distribuição (2 de 50% com monitoria, 4 de 25%, 5 de 10%). Nota de corte 7,0 e desempate por currículo. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia: o que você encontra na página." (60) |
| 4 | Curto direto | A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11. Campus São Paulo. Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11." (93) |
| 5 | Pergunta sobre o tema (longo) | Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa? A prova de 27/11 distribui 11 bolsas para a Pós-graduação em Neurologia e Neurocirurgia Veterinária: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. A nota de corte é 7,0. A bolsa não é garantida: a distribuição segue as regras da página. + corpo São Paulo | "Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa?" (67) |

Patologia Clínica (68658): mesmos cinco, com o gancho B "Os exames laboratoriais na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (90) e o nome completo "Pós-graduação em Patologia Clínica Veterinária".

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Prova de bolsa: Neurologia" (26) | "Inscrição de R$ 100,00" (22) |
| "Prova em 27/11: Neurologia" (26) | "11 bolsas por prova" (19) |
| "Prova de bolsa: Patologia Clínica" (33) | "Prova online, campus SP" (23) |
| "Prova em 27/11: Patologia Clínica" (33) | |
| "Neurologia: prova online em 27/11" (33) | |

Nenhum título usa "Pós em" ou abreviação do nome do curso: a regra da 1.13 (4.1) reserva essas formas para palavra-chave.

- **Chamada:** "Saiba mais".
- **Combinação para o 1º teste (T2 do criativos):** `c6-rotina_<área>_e11_cena_v1` + texto 1 + título "Prova de bolsa: {nome curto}" + descrição "Inscrição de R$ 100,00", contra `c1-bolsas_<área>_e11_numero_v1` na mesma área.

### 5.7 C5. A bolsa vale para a turma de {mês} (travado)

Não sobe até A-C2 (destino por prova) e até a página da prova trazer o bloco de destino. Quando liberar, usa o modelo da seção 3.9 do criativos com duas trocas: "A prova é presencial" vira "A prova é online"; "A turma é confirmada quando atinge o número mínimo de alunos" vira "A turma é confirmada com o mínimo de 15 alunos" (decisão 11). Título: "A bolsa vale para a turma de {mês}" (até 37). Chamada: "Saiba mais".

### 5.8 Turmas de março e abril (P3, P4): textos por conceito

Os 3 criativos por turma ainda vão ser produzidos pelo criativos-de-anuncio (prazo 02/12 para março; abril até 30/12). Abaixo, os textos de anúncio com os dados do catálogo, prontos para ligar às artes. Exemplo preenchido com 68615; as demais turmas trocam os campos pela tabela 5.9.

**Frio, conceito c1-rotina (rotina da área) e c3-docente (docente da ficha)**

| # | Estrutura | Texto principal (68615) | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | Pós-graduação em Patologia Clínica, campus São Paulo, com início em 20/03/2027. Semipresencial, 500 h. 30x de R$ 1.180,00 (total de R$ 35.400,00 no cartão ou boleto) e matrícula de R$ 250,00. | "Pós-graduação em Patologia Clínica, campus São Paulo, com início em 20/03/2027." (79) |
| 2 | História curta da rotina | Os exames laboratoriais na rotina da clínica pedem leitura segura. A Pós-graduação em Patologia Clínica da Faculdade UFAPE começa em 20/03/2027, no campus São Paulo, em formato semipresencial, com 500 h. Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. | "Os exames laboratoriais na rotina da clínica pedem leitura segura." (66) |
| 3 | Docente (mensageiro) | Aula com {docente da ficha}, na Pós-graduação em Patologia Clínica. Início em 20/03/2027, campus São Paulo, semipresencial, 500 h. 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. | "Aula com {docente da ficha}, na Pós-graduação em Patologia Clínica." (contar com o nome) |
| 4 | Objeção primeiro (longo) | Semipresencial não quer dizer só online. Na Pós-graduação em Patologia Clínica, as aulas teóricas são online e os módulos práticos são presenciais, no campus São Paulo [CONFIRMAR na ficha da turma o formato mês a mês]. Início em 20/03/2027, 500 h. Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. A turma é confirmada com o mínimo de 15 alunos. | "Semipresencial não quer dizer só online." (40) |
| 5 | Lista | Pós-graduação em Patologia Clínica: início em 20/03/2027; campus São Paulo; semipresencial; 500 h; 30x de R$ 1.180,00 (total de R$ 35.400,00); matrícula de R$ 250,00. | "Pós-graduação em Patologia Clínica: início em 20/03/2027; campus São Paulo; semipresencial; 500 h; 30x de R$ 1.180,00 (total de R$ 35.400,00); matrícula de R$ 250,00." (166) |

O texto 4 só sobe se a página da turma disser 15 alunos e descrever o formato semipresencial como no texto; senão sai a frase da turma mínima e a descrição do formato fica "semipresencial" [CONFIRMAR por página]. A descrição genérica do formato vem de contexto/pos-graduacao.md (formato típico), não do catálogo: por isso o [CONFIRMAR].

**Remarketing, conceito c2-investimento e c4-formato**

| # | Estrutura | Texto principal (68615) | Primeira frase |
|---|---|---|---|
| 1 | Curto direto | O investimento completo da Pós-graduação em Patologia Clínica: 30x de R$ 1.180,00, total de R$ 35.400,00 no cartão ou boleto, e matrícula de R$ 250,00. Início em 20/03/2027, campus São Paulo. | "O investimento completo da Pós-graduação em Patologia Clínica: 30x de R$ 1.180,00, total de R$ 35.400,00 no cartão ou boleto, e matrícula de R$ 250,00." (151) |
| 2 | Curto, pergunta | Quando começa a Pós-graduação em Patologia Clínica? Em 20/03/2027, no campus São Paulo. Semipresencial, 500 h. 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. | "Quando começa a Pós-graduação em Patologia Clínica?" (51) |
| 3 | Como funciona (longo) | Como funciona a Pós-graduação em Patologia Clínica, mês a mês: veja na página o calendário dos módulos e o que é online e o que é presencial. Início em 20/03/2027, campus São Paulo, 500 h. Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. A turma é confirmada com o mínimo de 15 alunos. | "Como funciona a Pós-graduação em Patologia Clínica, mês a mês: veja na página o calendário dos módulos e o que é online e o que é presencial." (141) |
| 4 | Objeção primeiro | A turma é confirmada com o mínimo de 15 alunos, e a Ufape avisa antes do início. Pós-graduação em Patologia Clínica, campus São Paulo, início em 20/03/2027. 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00. | "A turma é confirmada com o mínimo de 15 alunos, e a Ufape avisa antes do início." (80) |
| 5 | Curto, data | 20/03/2027: início da Pós-graduação em Patologia Clínica, campus São Paulo. Semipresencial, 500 h. Matrícula de R$ 250,00 e 30x de R$ 1.180,00 (total de R$ 35.400,00). | "20/03/2027: início da Pós-graduação em Patologia Clínica, campus São Paulo." (75) |

No texto 4, "a Ufape avisa antes do início" vem da orientação do contexto da linha (comprar passagem só com a turma confirmada); a forma do aviso é [CONFIRMAR]. Se a Ufape não confirmar, sai o trecho depois da vírgula.

| Títulos (até 40) | Descrições (até 30) |
|---|---|
| "Patologia Clínica, campus SP" (28) | "Início em 20/03/2027" (20) |
| "Início em 20/03/2027" (20) | "Semipresencial, 500 h" (21) |
| "30x de R$ 1.180,00 e matrícula" (30) | "Campus São Paulo" (16) |
| "Patologia Clínica: turma de março" (33) | |
| "Semipresencial no campus São Paulo" (34) | |

- **Chamada:** frio "Saiba mais"; remarketing "Saiba mais" ou "Cadastre-se" se o evento escolhido em EM11 for cadastro [SUPOSIÇÃO: rótulo disponível na Meta]. Motivo: a chamada combina com o evento que a campanha otimiza.
- **Combinação para o 1º teste (aquecimento, só direção):** frio com c1-rotina + texto 2 + título "Patologia Clínica, campus SP" contra c3-docente + texto 3 + mesmo título. O julgamento de conceito fica para a conversão (04/01 em diante), como pede a 1.13 (3.4).

### 5.9 Dados de cada turma para preencher os textos (catálogo, seção 2)

| Código | Nome visível | Campus | Início | Modalidade | Carga | Preço | URL de destino (ficha) | Cuidado |
|---|---|---|---|---|---|---|---|---|
| 68615 | Pós-graduação em Patologia Clínica | São Paulo | 20/03/2027 | Semipresencial | 500 h | 30x de R$ 1.180,00; R$ 35.400,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68615/pos-graduacao-patologia-clinica/sao-paulo | - |
| 289 | Pós-graduação em Cardiologia Veterinária | Goiânia | 20/03/2027 | Semipresencial | 500 h | 30x de R$ 1.180,00; R$ 35.400,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/289/pos-graduacao-em-cardiologia-veterinaria | links das provas de Cardiologia invertidos: remarketing da prova só depois |
| 333 | Pós-graduação em Citopatologia Veterinária | São Paulo | 27/03/2027 | Semipresencial | 500 h | 30x de R$ 935,00; R$ 28.050,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/333/pos-graduacao-em-citopatologia-veterinaria | - |
| 657 | Pós-graduação em Anestesiologia Avançada | São Paulo | 13/03/2027 | Semipresencial | 360 h | 30x de R$ 1.613,33; R$ 48.400,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/657/pos-graduacao-em-anestesiologia-avancada | pré-requisito [CONFIRMAR, U10] escrito na página e no anúncio |
| 341 | Pós-graduação em Medicina Interna Equina | São Paulo | 20/03/2027 | Semipresencial | 500 h | 30x de R$ 1.450,00; R$ 43.500,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/341/pos-graduacao-em-medicina-interna-equina | sem a promoção de 20% (PP7); o catálogo grafa "Pós Graduação": no anúncio, "Pós-graduação em" |
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais | São Paulo | 10/04/2027 | Semipresencial | 750 h | 30x de R$ 1.100,00; R$ 33.000,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68635/pos-graduacao-clinica-medica-e-emergencia-de-pequenos-animais/sao-paulo | - |
| 68636 | Pós-graduação em Pneumologia Veterinária | São Paulo | 17/04/2027 (só no site) | Semipresencial | 500 h | 30x de R$ 1.265,00; R$ 37.950,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68636/pos-graduacao-em-pneumologia-veterinaria | data [CONFIRMAR] na planilha; U6 |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais | São Paulo | 17/04/2027 | Semipresencial | 500 h | 30x de R$ 1.200,00; R$ 36.000,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68617/pos-graduacao-endocrinologia-de-pequenos-animais/v/sao-paulo | sem número de turma |
| 68628 | Pós-graduação em Oncologia Veterinária | São Paulo | 10/04/2027 | Semipresencial | 500 h | 30x de R$ 1.298,00; R$ 38.940,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68628/pos-graduacao-oncologia-veterinaria/sao-paulo | sem número de turma |
| 68609 | Pós-graduação em Anestesiologia Veterinária | Goiânia | 24/04/2027 | Semipresencial | 500 h | 30x de R$ 1.081,67; R$ 32.450,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68609/pos-graduacao-anestesiologia-veterinaria/goiania | - |
| 68632 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos | Goiânia | 10/04/2027 | Presencial | 500 h | 30x de R$ 1.100,00; R$ 33.000,00; matrícula R$ 250,00 | https://faculdade.ufape.com.br/produto/68632/pos-graduacao-clinica-cirurgica-de-caes-e-gatos/goiania | presencial: textos 4 de frio e 3 de remarketing trocam "semipresencial" por "presencial" |

O catálogo grafa 289 como "Semi presencial"; no anúncio, "semipresencial". Totais: o catálogo informa o total "no cartão ou boleto"; o texto repete essa forma.

---

## 6. Formulário instantâneo e mensagem de WhatsApp

Não se aplica nesta rodada. Toda campanha da Pós leva à página da prova ou da turma (gestor-de-midia-pos, seção 3: WhatsApp como destino fora; atendimento instável em 22/10). Formulário instantâneo também fica fora: a coleta de dados aconteceria fora da página, sem a política de privacidade da página na mesma tela [SUPOSIÇÃO de risco], e o CRM recebe a origem pela UTM da página. Se a Ufape quiser formulário instantâneo em março, vira pedido novo, com finalidade e link de privacidade no formulário (conformidade, LGPD).

---

## 7. UTM de cada anúncio

Campo "Parâmetros de URL" do anúncio (não na URL de destino), para não quebrar a URL da página [SUPOSIÇÃO de boa prática de plataforma].

| Campanha | Modelo de parâmetros |
|---|---|
| Provas, frio SP | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127_meta_compra_misto18_202611&utm_content=c1-bolsas_a12-neuro_e11_numero_v1&utm_term=amplo18-sp` |
| Provas, frio GO | idem, com `utm_content=<anúncio>-go` e `utm_term=amplo18-go` |
| Provas, remarketing | idem, com `utm_content=c4-regra_a12-neuro_car_pergunta_v1&utm_term=rmk30d` |
| Pós-prova | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM>&utm_content=<anúncio>&utm_term=rmk-prova-<código da turma>` |
| Turma, frio | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615_meta_lead_amplo18-sp_202612&utm_content=68615-c1-rotina_e11_cena_v1&utm_term=amplo18-sp` |
| Turma, remarketing | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_68615_meta_lead_rmk30d_202612&utm_content=68615-c2-investimento_e11_numero_v1&utm_term=rmk30d` |

Regras: `utm_content` igual ao nome do anúncio no gerenciador; o mesmo criativo em outra área ou praça é outro anúncio, com outro nome. Os parâmetros dinâmicos da Meta (nome da campanha, do conjunto e do anúncio) podem substituir os valores fixos se o arquiteto-de-fluxos preferir [SUPOSIÇÃO de recurso; conferir que o valor final saia em minúsculas e sem acento]. A tabela de correspondência das campanhas antigas é da analise-de-midia (D12).

---

## 8. Protocolo de teste e limites (escritos antes de subir)

Copiados da 1.13 (seção 2.4) e do criativos (seção 6), sem número novo.

| Item | Provas (P1) | Turmas (P3, P4) e pós-prova (P2) |
|---|---|---|
| Leitura permitida | gasto de pelo menos 1,5 x CPImax da área e 3 dias de dados; nenhuma realocação antes de 06/11 | gasto de pelo menos 1,5 x CPLmax_h e 3 dias |
| Pausa de anúncio | 1,5 a 2 x CPImax sem inscrição; nunca todos os antigos juntos | 1,5 a 2 x CPLmax_h sem lead |
| Promoção à escala | menor custo por inscrito abaixo do CPImax, em 2 leituras seguidas | CPL abaixo do CPLmax_h com volume por vários dias; passos de até 20% da diária |
| Cadência de criativo novo | fase 1 sem criativo novo; fase 2 (10/11) entra C3 e as iterações; reta final sem conceito novo | aquecimento sem julgar conceito; conversão julga; manutenção sem criativo novo |
| Uma mudança por conjunto | no máximo uma por semana; correção de conformidade quando achada | idem |
| Últimos 2 dias | não entram em tendência | idem |
| Sobreposição (A1 e A12 com o Workshop Brasileiro de Neuromonitorização) | de 20/11 a 26/11, se frequência subir e CTR cair por 3 dias seguidos, troca do anúncio mais cansado por ângulo pronto, sem cortar verba antes de 23/11 (EM12); CPM subindo com CTR estável de 03/11 a 18/11 é lido como disputa de leilão (NE4), com registro lado a lado (EA3) | - |

CPImax e CPLmax_h: [CONFIRMAR em PP1]. Sem eles, nenhuma campanha nova sobe (auditoria 11).

---

## 9. Checklists

### 9.1 Checklist de subida (pré-lançamento), por campanha

| # | Item | Quem confere | Provas (03/11) | Turmas (07/12, 14/12, 06/01) |
|---|---|---|---|---|
| S1 | Meta (CPImax ou CPLmax_h) e verba em reais escritas, com aprovador registrado (PP1, PP2) | gestor-de-midia | obrigatório | obrigatório |
| S2 | Pixel e API de Conversões recebendo o evento escolhido na página de destino (teste de 30/10, com compra de R$ 100,00 nas provas) | humano no gerenciador | obrigatório | evento de EM11 testado |
| S3 | Domínio faculdade.ufape.com.br verificado e evento priorizado na configuração de eventos [SUPOSIÇÃO de exigência da conta; conferir] | humano | obrigatório | obrigatório |
| S4 | Evento de otimização certo no conjunto (compra ou início de checkout; cadastro ou início de checkout) | humano | obrigatório | obrigatório |
| S5 | Nome da campanha, do conjunto e do anúncio exatamente como nas seções 3 e 5 | humano; qa | obrigatório | obrigatório |
| S6 | Parâmetros de URL completos (seção 7) e chegada da UTM ao pedido e ao CRM no teste | humano; arquiteto-de-fluxos | obrigatório | obrigatório |
| S7 | Página de destino confere com o anúncio: data, preço, campus; nas provas, diz "online" (AMP2); sem endereço contraditório; Goiânia com o campus certo; Cardiologia com links corrigidos | humano; qa | obrigatório | obrigatório |
| S8 | Página com frase de certificação ligada ao MEC: só com decisão registrada da pessoa do marketing ou com a página corrigida (estado E2) | pessoa do marketing | obrigatório nas 5 provas E2 | conferir em cada turma (12 de 14 ativas e 17 de 18 pausadas têm a frase, 1.12 N4) |
| S9 | Textos e artes aprovados pelo qa-de-marketing com conformidade educacional | qa | obrigatório | obrigatório |
| S10 | Idade 18+, região, exclusões e posicionamentos como na seção 3 | humano | obrigatório | obrigatório |
| S11 | Data de término programada (26/11 nas provas; nenhuma nas turmas, que pausam por pedido) | humano | obrigatório | - |
| S12 | Forma de pagamento da conta ativa e limite de gasto da conta acima da soma das diárias aprovadas [SUPOSIÇÃO de configuração] | humano | obrigatório | obrigatório |
| S13 | Tamanho do público lido no gerenciador e registrado (nenhum número existe hoje) [CONFIRMAR] | humano | obrigatório | obrigatório |
| S14 | Prévia de cada posicionamento conferida (Stories e Reels com a mensagem dentro da arte e sem corte nas zonas de interface) | humano | obrigatório | obrigatório |
| S15 | Registro de quem montou, quem revisou e quem aprovou | humano | obrigatório | obrigatório |

### 9.2 Checklist de pausa

| # | Item |
|---|---|
| P1 | Pausa aprovada antes (A-C6 nas provas, confirmada em 23/11; pedido do gestor nas turmas) |
| P2 | Exportação da campanha, dos conjuntos e dos anúncios antes de pausar (configuração, texto, URL e parâmetros) |
| P3 | Pausar, nunca excluir |
| P4 | Conferir no dia seguinte que o gasto parou (status "inativo" e gasto zero) |
| P5 | Registrar data, hora e motivo da pausa no relatório da semana |
| P6 | Como desfazer: reativar no gerenciador com a configuração exportada; uma reativação conta como mudança da semana no conjunto |

Pausas previstas: provas em 27/11 (término programado em 26/11, 23h59); frio de março em 21/12 (manutenção); pós-prova no fim dos 10 dias úteis [CONFIRMAR]; turmas em 24/01 só por pedido, nunca pela data do trimestre.

---

## 10. Pedidos de aprovação humana (AMP1 a AMP12)

Até a tabela de aprovação de contexto/ufape-geral.md ser preenchida, todos vão à pessoa do marketing que aprovou o plano do cmo. Quem executa: humano no gerenciador. Nada é executado pela squad.

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AMP1 | Estrutura das provas da seção 3.1 (1 campanha, 3 conjuntos, orçamento no conjunto) com nomes e UTM de D11 e D12 desde 03/11, substituindo a UTM antiga do criativos e a exceção de EM2 e PP4 | D12 manda as provas no padrão, porque ainda não subiram | dentro de P1: 20,25% de VN na Meta [CONFIRMAR reais] | relatório das provas somando com as demais linhas | trocar os parâmetros de URL (não reinicia aprendizado [SUPOSIÇÃO]) | 30/10 |
| AMP2 | Textos das provas reescritos (seções 5.1 a 5.6): "online" e campus no lugar de "presencial", endereço, documento e celular; pedido à Ufape para as 22 páginas das provas dizerem "online" antes de 03/11 | decisão 11; a página precisa entregar o que o anúncio diz | sem verba | anúncio e página coerentes | voltar ao texto anterior só se a Ufape revogar a decisão 11 | 30/10 (páginas até 02/11) |
| AMP3 | Evento de otimização das provas: compra; troca única para início de checkout se o teste de 30/10 falhar ou não houver volume na 1ª semana | a compra de R$ 100,00 tem pouco volume por área | sem verba | campanha aprende com um evento que registra | trocar o evento (reinicia aprendizado) | 30/10 |
| AMP4 | Posicionamentos manuais (Feed, Stories, Reels, Explorar), sem Audience Network nem Messenger | leitura por posicionamento e controle de onde a marca aparece | sem verba | menos entrega fora do Instagram e do Facebook | voltar ao automático | 30/10 |
| AMP5 | Conjunto de Goiânia só depois de as páginas 68640, 68642 e 68644 dizerem "online" e "campus Goiânia" (o endereço de São Paulo deixa de ser o bloqueio, pela decisão 11, mas a página ainda diz presencial); Cardiologia só com os links corrigidos | página coerente com o anúncio | 2,8125% de VN no conjunto GO; enquanto bloqueado, vai para SP na mesma fase | entrega em Goiânia sem destino errado | pausar o conjunto | 31/10 |
| AMP6 | Estrutura do pós-prova (seção 3.2) com a chave pos_provas20261127-matricula | separar a leitura de inscrição e de matrícula | 5% de VN | matrículas com bolsa lidas por turma de destino | renomear antes da subida | data do resultado [CONFIRMAR] |
| AMP7 | Estrutura de março (seção 3.3) e decisão sobre a campanha atual de 289 em 07/12 (recomendação: pausar com exportação e subir as duas novas) | frio e remarketing separados por turma; nomes no padrão | dentro de P3 [CONFIRMAR reais] | leitura por turma e manutenção sem mexer no remarketing | reativar a campanha antiga e pausar as novas | 30/11 |
| AMP8 | Estrutura de abril lote 1 (seção 3.4); 68635 e 68617 com campanhas novas, as antigas seguem pausadas | não herdar público, verba e nome antigos | dentro de P4 [CONFIRMAR reais] | 12 campanhas Meta em 06/01, no padrão | reativar as antigas | 30/12 |
| AMP9 | Textos das turmas (seção 5.8) com turma mínima de 15 só onde a página já diz 15 | decisão 11; algumas páginas dizem 20 | sem verba | transparência sobre a turma sem contradizer a página | tirar a frase | 30/11 |
| AMP10 | Registro lado a lado de CPM, alcance e frequência dos conjuntos de A1 e A12 com o Workshop Brasileiro de Neuromonitorização e a 616 (EA3) e regra de fadiga de EM12 | sobreposição de 03/11 a 18/11 (seção 12.6) | sem verba | decisão de 09/11 e 10/11 sem confundir leilão com criativo fraco | não se aplica | 06/11 e 09/11 |
| AMP11 | Parâmetros de URL no campo próprio do anúncio, não na URL | não quebrar a URL da página | sem verba | UTM uniforme | colar na URL | 30/10 |
| AMP12 | C3 reescrito só em 10/11 e só com U2 respondido; C5 só com A-C2 | sem o acesso online confirmado, o texto não pode explicar a prova | dentro de P1 | conceito de logística verdadeiro | não subir | 09/11 |

**Os 3 primeiros:** AMP2 (sem página coerente, nada das provas sobe), AMP1 e AMP3. **Vão ao cmo:** nenhum muda verba total ou canal; AMP7 e AMP8 vão ao gestor-de-midia.

---

## 11. Notas sobre arquivos de outros agentes (não alterados)

- **criativos-de-anuncio-pos, seções 1.1, 1.4, 3.3 a 3.8, 4.1, 4.2 e 4.3:** "prova presencial", endereço de São Paulo, documento com foto e "sem celular" contrariam a decisão 11 e a seção 12.9; a UTM da seção 1.4 contraria D11 e D12. Os textos reescritos estão na seção 5 deste arquivo; as artes precisam da mesma troca (quadros com "Presencial").
- **criativos-de-anuncio-pos, seção 1.1:** "Turma mínima: não citar número"; a decisão 11 fixou 15.
- **estrategia-de-midia-pos, seções 4.2 e 4.3:** chave com área curta e UTM das provas no padrão antigo; superadas por D12 (seção 1 deste arquivo).
- **estrategia-de-midia-pos, seção 3.1:** o estado E3 de Goiânia dependia do endereço; com a prova online, o bloqueio passa a ser a página dizer "presencial" (AMP5).
- **Páginas das 22 provas (pedido à Ufape, não à squad):** dizem "prova presencial" e trazem endereço; precisam dizer "online" com o campus.

---

## 12. Auditorias

### 12.1 auditorias/11-midia-paga.md (aplicada à montagem)

| Item | Resultado | Observação |
|---|---|---|
| Metas de CPL e custo por matrícula escritas antes de subir | Pendente externo | S1; PP1 |
| Verba dentro do aprovado | Pendente externo | só percentuais de VN |
| Nomenclatura padrão | Atendido no desenho | D12 |
| UTMs completas | Atendido no desenho | seção 7; chegada ao CRM no teste de 30/10 |
| Pixel e API de Conversões | Pendente externo | S2 |
| Criativos aprovados na conformidade | Pendente externo | textos reescritos aqui; artes com troca pedida |
| Públicos sem menores de 18 e sem segmentação discriminatória | Atendido | seção 3 |
| Sem lista de contatos sem base legal | Atendido | só pixel e engajamento |
| Nenhuma alteração sem humano | Atendido | seções 9 e 10 |

### 12.2 auditorias/conformidade-educacional.md (bloco de anúncios e preço)

| Bloco | Resultado | Observação |
|---|---|---|
| Dados de curso do catálogo | Atendido | tabela 5.9; 68636 com [CONFIRMAR] |
| Sem MEC e sem certificação | Atendido | nenhum texto cita |
| Bolsa com regra, público e prazo | Atendido com pendência | distribuição completa e "não acumulativa e intransferível"; prazo de matrícula fora até U1 e U3 |
| Preço com parcelas, valor, total e matrícula | Atendido | seção 5.8 |
| Urgência real | Atendido | só a data da prova |
| Característica pessoal de quem vê | Atendido | nenhum texto afirma situação de quem lê |
| Destino entrega o que o anúncio promete | Pendente externo | páginas das provas dizem "presencial" (AMP2) |
| Sem travessão nem meia-risca | Atendido | conferido por busca dos caracteres |

---

## Lista 1. Fatos (com fonte)

- Provas online, com o campus dito na peça; turma mínima de 15 também na Pós; datas da planilha valem (docs/execucao-2026-10-26.md, decisões 11 e 12; seção 12.1 e 12.9 do plano do cmo).
- Padrão de UTM (`meta`, `paid_social`) e de nomes (chave `pos_<código>`, `pos_provas20261127`) e campanhas antigas sem renomear (seção 12.7, D11 e D12).
- Nenhuma menção a crédito da ponte Livres para Pós (seção 12.4, D7).
- Divisão de P1 por fase e conjunto, de P3 e P4 por turma e semana, condição de volume e limites de revisão (estrategia-de-midia-pos, seções 2.4, 3.1 a 3.4 e 4).
- Canais e destino (página, nunca WhatsApp) (gestor-de-midia-pos, seção 3).
- Inscrição de R$ 100,00, 11 bolsas (2 de 50% com monitoria, 4 de 25%, 5 de 10%), nota de corte 7,0, desempate por currículo, 27/11/2026 das 9h às 13h (catálogo, seção 3; criativos-de-anuncio-pos, 1.1; contexto/pos-graduacao.md).
- Estados E1 a E6 das provas e URLs das páginas (criativos-de-anuncio-pos, seção 4.1).
- Dados das 11 turmas (catálogo, seção 2) e URLs (fichas de contexto/cursos/pos/).
- 12 de 14 ativas e 17 de 18 pausadas levam a página com frase ligada ao MEC (analise-de-midia-pos, N4).
- Sobreposição de público com o Workshop Brasileiro de Neuromonitorização e a 616 de 03/11 a 18/11; EA3 e NE4 (seção 12.6; analise-de-midia-eventos).

## Lista 2. Suposições

- [SUPOSIÇÃO] Educação não é categoria especial de anúncio na Meta.
- [SUPOSIÇÃO] Limite de frequência fixo indisponível no objetivo Vendas; controle por leitura e troca de anúncio.
- [SUPOSIÇÃO] Posicionamentos manuais sem Audience Network e Messenger.
- [SUPOSIÇÃO] Limites de 40 caracteres no título e 30 na descrição como referência de exibição.
- [SUPOSIÇÃO] Rótulos de chamada "Inscreva-se" e "Cadastre-se" disponíveis na lista da Meta.
- [SUPOSIÇÃO] Troca de parâmetros de URL não reinicia o aprendizado.
- [SUPOSIÇÃO] "O campus indica a turma, não o lugar da prova" como leitura da decisão 11 (texto 4 de C3).
- [SUPOSIÇÃO] Formulário instantâneo fora por risco de coleta sem a política de privacidade da página.
- [SUPOSIÇÃO] Ganchos de rotina por área (do criativos) como tema, não como fala de aluno.
- [SUPOSIÇÃO] Pausar a campanha atual de 289 e subir duas novas em 07/12.
- [SUPOSIÇÃO] Domínio verificado e priorização de eventos exigidos pela conta.

## Lista 3. Dados que faltam

- [CONFIRMAR] VN em reais, aprovador e quem executa no gerenciador (PP2); CPImax por área e CPLmax_h por turma (PP1).
- [CONFIRMAR] U2: plataforma, acesso e regras do dia da prova online; páginas das provas atualizadas para "online" com o campus.
- [CONFIRMAR] U1 e U3: prazo de matrícula, canal e data do resultado, fim das inscrições; sem isso, nenhum texto cita prazo.
- [CONFIRMAR] A-C2: turma de destino de cada prova (libera C5 e P2); U4 para as 4 provas sem turma.
- [CONFIRMAR] Correção dos links de Cardiologia (68641 e 68642) e das páginas de Goiânia.
- [CONFIRMAR] Decisão registrada sobre as 5 provas em E2 (página com frase ligada ao MEC).
- [CONFIRMAR] Resultado do teste de rastreio de 30/10 e evento das páginas de turma (EM11).
- [CONFIRMAR] Tamanho dos públicos no gerenciador: [DADO NÃO FORNECIDO] hoje.
- [CONFIRMAR] Base legal para listas de contatos.
- [CONFIRMAR] Turma mínima de 15 em cada página de turma; formato mês a mês de cada turma.
- [CONFIRMAR] Pré-requisito de 657 (U10); regra da promoção de 341; data de 68636 na planilha (U6).
- [CONFIRMAR] Diária atual de 289 e decisão sobre a campanha atual em 07/12.

## Fontes

Internas: as entradas listadas no cabeçalho. Externas: nenhuma. Regras de plataforma sem fonte estão marcadas [SUPOSIÇÃO].

---

**Próximo agente sugerido:** anuncios-google (estrutura de Busca da Pós), depois qa-de-marketing.
