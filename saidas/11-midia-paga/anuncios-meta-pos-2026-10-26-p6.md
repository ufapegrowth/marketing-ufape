# Estrutura de Meta Ads da Pós-graduação, versão 7: parte 6 (seção 13, provas, SUSPENSA, sem alteração nesta versão)

Continuação de `anuncios-meta-pos-2026-10-26-p5.md`. O texto desta parte é o da versão 6, sem nenhuma mudança.

---

## 13. SUSPENSO (decisão 14): montagem das provas de bolsa e do pós-prova

**Estado: suspenso. Não executar.** A decisão 14 do CEO (26/10/2026) manda não produzir peças novas das provas de bolsa nem de Livres, e as encomendas das provas ficam suspensas até nova ordem (gestor-de-midia-pos 12.8; estrategia-de-midia-pos v4, seção 1). O conteúdo abaixo é o da versão 2 deste arquivo, guardado sem apagar e sem mudar o texto. Verba aparece como percentual da verba nova da Pós (VN) e o valor em reais é VN x percentual [CONFIRMAR]. As datas (03/11, 10/11, 26/11, 27/11) e os percentuais valiam na versão 2; se o CEO retomar as provas, tudo volta a passar pelo qa-de-marketing e pela conformidade, com as datas conferidas de novo. Nada desta seção sobe, muda, pausa ou gasta. O pedido de retomada seria novo, com nova ordem do CEO. Cada subseção abaixo repete o aviso "SUSPENSO, NÃO EXECUTAR" no título (recomendação R1 do qa).

**Nota da decisão 20 do CEO (27/10/2026): este texto está desatualizado e não vale.** As provas de bolsa são **presenciais**, em São Paulo e em Goiânia, e toda peça diz o campus e o local da prova da ficha. Onde o texto abaixo diz "online" (regras 13.1, estruturas, anúncios 13.6.1 a 13.6.7, o bloqueio das páginas de Goiânia e a pendência U2 de acesso online), ele foi escrito para a decisão 11 e não pode ser usado. O local de Goiânia é [CONFIRMAR]: as fichas 68640, 68642 e 68644 mostram endereço de São Paulo. **A trava AMP2 (páginas das provas dizerem "online") deixa de existir**, e o texto do AMP2 e do AMP5 na seção 13.10 fica só como histórico. O texto das provas será reescrito pela varredura da vez das provas, se o CEO retomá-las (decisão 14). Nenhuma peça desta seção sobe.

### 13.1 Regras próprias das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 1)

| Regra | Valor nesta montagem | Fonte |
|---|---|---|
| Prova de bolsa | **Superado pela decisão 20: provas presenciais, com o campus e o local da ficha; local de Goiânia [CONFIRMAR].** Texto da versão 2: Online. Toda peça diz o campus da prova (São Paulo ou Goiânia). Sem endereço, sem "presencial", sem documento com foto, sem "sem celular". Data e horário como na ficha: 27/11/2026, das 9h às 13h. Acesso online: [CONFIRMAR, U2] | decisão 11; seção 12.9 |
| Bolsa | Só nas provas e no pós-prova, sempre com a distribuição completa (2 de 50% com monitoria, 4 de 25%, 5 de 10%) e "Bolsa não acumulativa e intransferível". Anúncio de turma não fala de bolsa | criativos-de-anuncio-pos, 1.1 a 1.3; 1.13, 4.1 |
| Crédito e ponte Livres para Pós | Nenhuma menção a crédito, combo ou desconto da ponte | D7 da seção 12.4 |
| Nomes | Campanha = chave + `_<plataforma>_<objetivo>_<público>_<AAAAMM>`; chave = `pos_provas20261127`. Conjunto = nome da campanha + `__` + público. Minúsculas, sem acento | D12 |
| Sobreposição | Sem exclusão de público entre campanhas e sem anúncio que misture ofertas. Registro lado a lado de CPM, alcance e frequência (EA3) | seção 12.6 |

**Divergência resolvida pela seção 12 do cmo (nota para quem monta):** a 1.13 (seção 4.2) usava a área curta na chave (`pos_68615-patclin_...`) e mantinha a UTM antiga das provas (`utm_medium=pago`, `utm_campaign=provas-de-bolsa-2026-11-27`). D11 e D12 mandam o padrão `meta` e `paid_social` também nas provas, porque os anúncios das provas ainda não subiram. A versão 2 seguiu D11 e D12. (Para as turmas, esta versão segue a estratégia v4, que usa a área curta; ver a nota de nomes na seção 1.)

### 13.2 Modelo de estrutura das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 2)

| Frente | Modelo | Motivo (2 a 3 linhas) |
|---|---|---|
| P1 Provas | Lançamento por fases, em 1 campanha de vendas com 3 conjuntos | Data fixa (27/11) e fases já escritas (40%, 35%, 25%, PP3). Um conjunto por praça e um de remarketing porque São Paulo, Goiânia e visitantes têm tamanhos muito diferentes; com orçamento na campanha, o algoritmo levaria quase tudo para São Paulo (EM5) |
| P2 Pós-prova | Enxuta: 1 campanha de remarketing, 1 conjunto por turma de destino confirmada | Público pequeno (visitantes das páginas da prova e da turma) e janela curta (10 dias úteis) |

Orçamento: nas provas, no conjunto; no pós-prova, na campanha. Nunca nos dois.

### 13.3 P1 Provas de bolsa [SUSPENSO, NÃO EXECUTAR] (sobe em 03/11, pausa em 27/11)

```
Campanha (objetivo Vendas; orçamento no conjunto):
  pos_provas20261127_meta_compra_misto18_202611
  Conjunto 1:
    - pos_provas20261127_meta_compra_misto18_202611__amplo18-sp
      anúncios por área liberada (E1 em 03/11; E2 com decisão registrada):
      c1-bolsas_<área>_e11_numero_v1, c1-bolsas_<área>_e916_numero_v1,
      c2-entrada_<área>_e11_numero_v1, c2-entrada_<área>_e916_numero_v1,
      c2-entrada_<área>_vid916_pergunta_v1 (se o vídeo estiver pronto),
      c6-rotina_<área>_e11_cena_v1, c6-rotina_<área>_e916_cena_v1
  Conjunto 2:
    - pos_provas20261127_meta_compra_misto18_202611__amplo18-go
      mesmos conceitos, com <área>-go (a1-anest-go, a4-cirurgia-go; a2-cardio-go só depois da correção dos links)
      sobe só com a página de Goiânia dizendo prova online e campus Goiânia (AMP5)
  Conjunto 3:
    - pos_provas20261127_meta_compra_misto18_202611__rmk30d
      c4-regra_<área>_car_pergunta_v1 (carrossel "Como funciona")
      estático de remarketing da área (seção 13.6.6, C6)
```

Em 10/11 (fase 2) entram, por pedido, C3 reescrito (seção 13.6.4, só com U2 respondido), as iterações do vencedor (uma variável por vez) e as áreas de E5 com destino confirmado. C5 fica travado até A-C2.

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

### 13.4 P2 Pós-prova [SUSPENSO, NÃO EXECUTAR] (sobe na data do resultado [CONFIRMAR], pausa no fim dos 10 dias úteis)

```
Campanha (Vendas; orçamento na campanha):
  pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM do resultado>
  Conjuntos:
    - um conjunto por turma de destino confirmada: ...__rmk-prova-<código da turma>
      c5-turma_<área>_e11_resultado_v1 (só depois de A-C2)
      <código da turma>-c2-investimento_e11_numero_v1 (texto da seção 5.8 da versão 2, que continha preço e não foi mantido nesta versão)
```

Observação de nome: a chave `pos_provas20261127-matricula` é a da 1.13 (seção 4.6). D12 não prevê chave para o pós-prova; proponho mantê-la para separar a leitura da inscrição da leitura da matrícula (AMP6).

| Campo | Valor |
|---|---|
| Evento | Compra do produto da turma de destino; se não houver volume, início de checkout |
| Público | Visitantes, em 30 dias, da página da prova da área e da página da turma de destino. É público de visitantes, não de aprovados: o texto vale para quem fez e para quem não fez a prova |
| Exclusões | Compradores da turma de destino (pixel, 180 dias) |
| Texto | Sem prazo de matrícula até U1 e U3 responderem; sem valor com bolsa; com o investimento completo da turma |

### 13.5 Verba das provas e do pós-prova [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 4; percentual de VN, reais = VN x percentual [CONFIRMAR])

Todos os percentuais vêm da 1.13 (seções 3.1 a 3.3). Diária = parte da fase dividida pelos dias da fase.

**P1 Provas, Meta, por conjunto e fase**

| Fase (dias) | __amplo18-sp | __amplo18-go | __rmk30d | Total Meta da fase | Diária SP / GO / rmk (em VN) |
|---|---|---|---|---|---|
| 1. 03/11 a 09/11 (7) | 5,8800% | 1,2600% | 1,2600% | 8,4000% | 0,8400% / 0,1800% / 0,1800% |
| 2. 10/11 a 19/11 (10) | 4,7775% | 1,1025% | 1,4700% | 7,3500% | 0,4778% / 0,1103% / 0,1470% |
| 3. 20/11 a 26/11 (7) | 2,2500% | 0,4500% | 1,8000% | 4,5000% | 0,3214% / 0,0643% / 0,2571% |
| **Total** | 12,9075% | 2,8125% | 4,5300% | **20,2500%** | |

Enquanto Goiânia estiver bloqueada, a parte de __amplo18-go passa para __amplo18-sp na mesma fase (1.13, 3.1). Área bloqueada não guarda verba. Leads por semana esperados = verba semanal do conjunto dividida pelo CPImax da área [CONFIRMAR em PP1]; sem CPImax, [DADO NÃO FORNECIDO]. Condição de volume da 1.13: VN mínima = 50 x CPImax com 4 conceitos, ou 25 x CPImax na versão enxuta (só C1 e C6).

**P2 Pós-prova:** 5,00% de VN no total, em partes iguais por turma de destino confirmada. Diária = 5% de VN dividido pelos dias corridos da janela [CONFIRMAR data do resultado] e pelo número de turmas de destino.

### 13.6 Anúncios das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 5)

Contagem de caracteres: a primeira frase do texto principal aparece entre parênteses, seguida do número de caracteres. Títulos até 40 e descrições até 30 (referência de plataforma [SUPOSIÇÃO]; conferir a prévia no gerenciador). Em Stories e Reels a mensagem está dentro da arte: o texto principal complementa. Quando a primeira frase passa de cerca de 125 caracteres (textos em lista e de investimento), só o começo aparece antes do "ver mais": por isso esses textos põem curso, data e preço logo no início.

Exemplos preenchidos com as duas provas que sobem em 03/11 sem pendência (E1): 68654 Neurologia e 68658 Patologia Clínica. As demais áreas usam o mesmo texto, trocando {nome curto} e {nome completo} pela tabela da seção 4.1 do criativos-de-anuncio-pos e o campus pela praça da prova.

#### 13.6.1 Corpo fixo das provas [SUSPENSO, NÃO EXECUTAR] (texto "online" superado pela decisão 20) (substitui BODY_SP e BODY_GO do criativos-de-anuncio-pos)

- **Corpo São Paulo:** "Prova de bolsa do campus São Paulo da Faculdade UFAPE, online, em 27/11/2026, das 9h às 13h. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). São 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Bolsa não acumulativa e intransferível. Regras completas na página da prova."
- **Corpo Goiânia:** igual, com "campus Goiânia". Sem endereço. Sem prazo de matrícula e sem canal do resultado em nenhuma prova até U1 (12 fichas têm versões contraditórias: 68641, 68642, 68643, 68644, 68645, 68650, 68651, 68652, 68653, 68657, 68659, 68661).
- **Fica de fora de todo texto das provas:** "presencial", endereço, "documento com foto", "sem celular", "sem relógio", data do resultado, prazo de inscrição, turma de destino (até A-C2).

#### 13.6.2 C1. 11 bolsas por prova [SUSPENSO, NÃO EXECUTAR] (frio, São Paulo e Goiânia)

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
- **Combinação para o 1º teste (T1 do criativos):** arte `c1-bolsas_<área>_e11_numero_v1` + texto 1 + título "Prova de bolsa: {nome curto}" + descrição "Inscrição de R$ 100,00", contra a combinação de C2 da seção 13.6.3. Mesmo conjunto, mesma área, mesmo formato.

#### 13.6.3 C2. R$ 100,00 para concorrer [SUSPENSO, NÃO EXECUTAR] (frio)

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
| "Inscrição na prova: R$ 100,00" (29) | |
| "Prova em 27/11: Patologia Clínica" (33) | |

- **Chamada:** "Saiba mais" (mesmo motivo de C1).
- **Combinação para o 1º teste:** `c2-entrada_<área>_e11_numero_v1` + texto 5 + título "R$ 100,00 para concorrer" + descrição "11 bolsas por prova". O vídeo `c2-entrada_<área>_vid916_pergunta_v1` entra com o texto 2 se estiver pronto em 03/11.
- **Vídeo (roteiro da seção 3.8 do criativos):** o quadro de 8 a 14 s muda para "Prova online / Sexta, 27/11/2026, das 9h às 13h / Campus São Paulo" e a locução opcional para "A prova é online, em 27 de novembro, das 9 às 13 horas." Sai "Documento com foto".

#### 13.6.4 C3 reescrito [SUSPENSO, NÃO EXECUTAR]. Prova online, 27/11, das 9h às 13h (fase 2, só com U2 respondido) (superado pela decisão 20: provas presenciais)

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

#### 13.6.5 C4 [SUSPENSO, NÃO EXECUTAR]. Nota de corte 7,0 e carrossel "Como funciona" (remarketing)

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

#### 13.6.6 C6 [SUSPENSO, NÃO EXECUTAR]. Rotina da especialidade (camada de área, frio)

Nomes: `c6-rotina_<área>_e11_cena_v1`, `_e916_cena_v1`, `_e11_numero_v2` (iteração, fase 2). Os ganchos de rotina vêm do criativos (seção 4.2) e são [SUPOSIÇÃO] de tema, não fala de aluno.

| # | Estrutura | Texto principal (Neurologia, 68654) | Primeira frase |
|---|---|---|---|
| 1 | História curta da rotina (gancho B) | O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11. Prova de bolsa para a Pós-graduação em Neurologia e Neurocirurgia Veterinária. + corpo São Paulo | "O paciente neurológico na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (89) |
| 2 | Curto, número (gancho A) | Neurologia: 11 bolsas por prova, inscrição de R$ 100,00. Prova online, campus São Paulo, em 27/11/2026, das 9h às 13h. 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "Neurologia: 11 bolsas por prova, inscrição de R$ 100,00." (56) |
| 3 | Lista de benefícios | Prova de bolsa de Neurologia: o que você encontra na página. Data e horário (27/11/2026, das 9h às 13h, online). As 11 bolsas e a distribuição (2 de 50% com monitoria, 4 de 25%, 5 de 10%). Nota de corte 7,0 e desempate por currículo. Campus São Paulo. Inscrição de R$ 100,00. Bolsa não acumulativa e intransferível. | "Prova de bolsa de Neurologia: o que você encontra na página." (60) |
| 4 | Curto direto | A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11. Campus São Paulo. Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Bolsa não acumulativa e intransferível. | "A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem prova de bolsa online em 27/11." (93) |
| 5 | Pergunta sobre o tema (longo) | Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa? A prova de 27/11 distribui 11 bolsas para a Pós-graduação em Neurologia e Neurocirurgia Veterinária: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. A nota de corte é 7,0. A bolsa não é garantida: a distribuição segue as regras da página. + corpo São Paulo | "Neurologia e neurocirurgia na rotina: dá para aprofundar com bolsa?" (67) |

Patologia Clínica (68658): mesmos cinco, com o gancho B "Os exames laboratoriais na rotina da clínica: a especialidade tem prova de bolsa em 27/11." (90) e o nome completo como na seção 2 do catálogo, "Pós-graduação em Patologia Clínica" (turma 68615), ou o nome da prova como na seção 3 ("prova de bolsa de Patologia Clínica Veterinária") até A-C2 dizer a turma de destino. Nunca "Pós-graduação em Patologia Clínica Veterinária", que não existe no catálogo (AMP-Q2).

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

#### 13.6.7 C5 [SUSPENSO, NÃO EXECUTAR]. A bolsa vale para a turma de {mês} (travado)

Não sobe até A-C2 (destino por prova) e até a página da prova trazer o bloco de destino. Quando liberar, usa o modelo da seção 3.9 do criativos com duas trocas: "A prova é presencial" vira "A prova é online"; "A turma é confirmada quando atinge o número mínimo de alunos" vira "A turma é confirmada com o mínimo de 15 alunos" (decisão 11). Título: "A bolsa vale para a turma de {mês}" (até 37). Chamada: "Saiba mais".

### 13.7 UTM das provas e do pós-prova [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 7)

Campo "Parâmetros de URL" do anúncio (não na URL de destino), para não quebrar a URL da página [SUPOSIÇÃO de boa prática de plataforma].

| Campanha | Modelo de parâmetros |
|---|---|
| Provas, frio SP | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127_meta_compra_misto18_202611&utm_content=c1-bolsas_a12-neuro_e11_numero_v1&utm_term=amplo18-sp` |
| Provas, frio GO | idem, com `utm_content=<anúncio>-go` e `utm_term=amplo18-go` |
| Provas, remarketing | idem, com `utm_content=c4-regra_a12-neuro_car_pergunta_v1&utm_term=rmk30d` |
| Pós-prova | `utm_source=meta&utm_medium=paid_social&utm_campaign=pos_provas20261127-matricula_meta_compra_rmk-prova_<AAAAMM>&utm_content=<anúncio>&utm_term=rmk-prova-<código da turma>` |

### 13.8 Protocolo de teste das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 8, coluna das provas)

| Item | Provas (P1) |
|---|---|
| Leitura permitida | gasto de pelo menos 1,5 x CPImax da área e 3 dias de dados; nenhuma realocação antes de 06/11 |
| Pausa de anúncio | 1,5 a 2 x CPImax sem inscrição; nunca todos os antigos juntos |
| Promoção à escala | menor custo por inscrito abaixo do CPImax, em 2 leituras seguidas |
| Cadência de criativo novo | fase 1 sem criativo novo; fase 2 (10/11) entra C3 e as iterações; reta final sem conceito novo |
| Uma mudança por conjunto | no máximo uma por semana; correção de conformidade quando achada |
| Últimos 2 dias | não entram em tendência |
| Sobreposição (A1 e A12 com o Workshop Brasileiro de Neuromonitorização) | de 20/11 a 26/11, se frequência subir e CTR cair por 3 dias seguidos, troca do anúncio mais cansado por ângulo pronto, sem cortar verba antes de 23/11 (EM12); CPM subindo com CTR estável de 03/11 a 18/11 é lido como disputa de leilão (NE4), com registro lado a lado (EA3) |

CPImax: [CONFIRMAR em PP1]. Sem ele, nenhuma campanha das provas sobe.

### 13.9 Itens do checklist próprios das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, seção 9)

| # | Item | Provas (03/11) |
|---|---|---|
| S2 | Pixel e API de Conversões recebendo o evento escolhido na página de destino (teste de 30/10, com compra de R$ 100,00 nas provas) | obrigatório |
| S4 | Evento de otimização certo no conjunto (compra ou início de checkout) | obrigatório |
| S7 | Página de destino confere com o anúncio: nas provas, diz "online" (AMP2, sem efeito pela decisão 20); sem endereço contraditório; Goiânia com o campus certo; Cardiologia com links corrigidos | obrigatório |
| S8 | Página com frase de certificação ligada ao MEC: só com decisão registrada da pessoa do marketing ou com a página corrigida (estado E2) | obrigatório nas 5 provas E2 |
| S11 | Data de término programada (26/11 nas provas) | obrigatório |
| P1 (pausa) | Pausa aprovada antes (A-C6 nas provas, confirmada em 23/11). Pausas previstas: provas em 27/11 (término programado em 26/11, 23h59); pós-prova no fim dos 10 dias úteis [CONFIRMAR] | obrigatório |

### 13.10 Pedidos das provas [SUSPENSO, NÃO EXECUTAR] (versão 2, AMP1 a AMP6, AMP10 e AMP12), todos suspensos

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AMP1 | Estrutura das provas da seção 13.3 (1 campanha, 3 conjuntos, orçamento no conjunto) com nomes e UTM de D11 e D12 desde 03/11, substituindo a UTM antiga do criativos e a exceção de EM2 e PP4 | D12 manda as provas no padrão, porque ainda não subiram | dentro de P1: 20,25% de VN na Meta [CONFIRMAR reais] | relatório das provas somando com as demais linhas | trocar os parâmetros de URL (não reinicia aprendizado [SUPOSIÇÃO]) | 30/10 |
| AMP2 (deixa de existir, decisão 20) | Textos das provas reescritos (seções 13.6.1 a 13.6.6): "online" e campus no lugar de "presencial", endereço, documento e celular; pedido à Ufape para as 22 páginas das provas dizerem "online" antes de 03/11 | decisão 11; a página precisa entregar o que o anúncio diz | sem verba | anúncio e página coerentes | voltar ao texto anterior só se a Ufape revogar a decisão 11 | 30/10 (páginas até 02/11) |
| AMP3 | Evento de otimização das provas: compra; troca única para início de checkout se o teste de 30/10 falhar ou não houver volume na 1ª semana | a compra de R$ 100,00 tem pouco volume por área | sem verba | campanha aprende com um evento que registra | trocar o evento (reinicia aprendizado) | 30/10 |
| AMP4 | Posicionamentos manuais (Feed, Stories, Reels, Explorar), sem Audience Network nem Messenger | leitura por posicionamento e controle de onde a marca aparece | sem verba | menos entrega fora do Instagram e do Facebook | voltar ao automático | 30/10 |
| AMP5 | Conjunto de Goiânia só depois de as páginas 68640, 68642 e 68644 dizerem "online" e "campus Goiânia" (o endereço de São Paulo deixa de ser o bloqueio, pela decisão 11, mas a página ainda diz presencial); Cardiologia só com os links corrigidos | página coerente com o anúncio | 2,8125% de VN no conjunto GO; enquanto bloqueado, vai para SP na mesma fase | entrega em Goiânia sem destino errado | pausar o conjunto | 31/10 |
| AMP6 | Estrutura do pós-prova (seção 13.4) com a chave pos_provas20261127-matricula | separar a leitura de inscrição e de matrícula | 5% de VN | matrículas com bolsa lidas por turma de destino | renomear antes da subida | data do resultado [CONFIRMAR] |
| AMP10 | Registro lado a lado de CPM, alcance e frequência dos conjuntos de A1 e A12 com o Workshop Brasileiro de Neuromonitorização e a 616 (EA3) e regra de fadiga de EM12 | sobreposição de 03/11 a 18/11 (seção 12.6) | sem verba | decisão de 09/11 e 10/11 sem confundir leilão com criativo fraco | não se aplica | 06/11 e 09/11 |
| AMP12 | C3 reescrito só em 10/11 e só com U2 respondido; C5 só com A-C2 | sem o acesso online confirmado, o texto não pode explicar a prova | dentro de P1 | conceito de logística verdadeiro | não subir | 09/11 |

(AMP7, AMP8, AMP9 e AMP11 da versão 2 eram das turmas e do campo de UTM; foram substituídos pelos pedidos AMP13 a AMP25 e pela seção 6.3.)

### 13.11 Pendências e suposições próprias das provas [SUSPENSO, NÃO EXECUTAR] (versão 2)

- [CONFIRMAR] U2: plataforma, acesso e regras do dia da prova online; páginas das provas atualizadas para "online" com o campus. (Sem efeito pela decisão 20: as provas são presenciais; local de Goiânia [CONFIRMAR].)
- [CONFIRMAR] U1 e U3: prazo de matrícula, canal e data do resultado, fim das inscrições; sem isso, nenhum texto cita prazo.
- [CONFIRMAR] A-C2: turma de destino de cada prova (libera C5 e P2); U4 para as 4 provas sem turma.
- [CONFIRMAR] Correção dos links de Cardiologia (68641 e 68642) e das páginas de Goiânia.
- [CONFIRMAR] Decisão registrada sobre as 5 provas em E2 (página com frase ligada ao MEC).
- [CONFIRMAR] VN em reais, aprovador e quem executa no gerenciador (PP2); CPImax por área (PP1).
- [SUPOSIÇÃO] Limite de frequência fixo indisponível no objetivo Vendas; posicionamentos manuais; limites de 40 caracteres no título e 30 na descrição como referência de exibição; rótulos "Inscreva-se" e "Cadastre-se" disponíveis na lista da Meta; troca de parâmetros de URL não reinicia o aprendizado; "o campus indica a turma, não o lugar da prova" como leitura da decisão 11 (texto 4 de C3); ganchos de rotina por área (do criativos) como tema, não como fala de aluno.

---

**Continua em `anuncios-meta-pos-2026-10-26-p7.md` (seção 14, "Mudanças desta versão", listas e fontes).**
