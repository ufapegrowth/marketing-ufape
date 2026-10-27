## 8. Anúncios responsivos (2 por grupo até o corte; 1 em 662; 1 por grupo na extensão, de cada vez)

### 8.1 Como são montados

Cada turma tem dois textos de anúncio, **A (turma e campus)** e **B (formato e prática)**, copiados nos dois grupos **até o corte**. 13 turmas têm 4 anúncios por campanha; **662 tem só o texto A (2 anúncios, um por grupo) até a ficha ser corrigida** (decisão do qa, G5: A e B de 662 teriam os mesmos títulos e as mesmas descrições). Total até o corte: 54 anúncios. **No dia seguinte ao corte**, cada grupo passa a ter 1 anúncio **-exta**; **no dia do início da turma**, o -exta é pausado e entra 1 anúncio **-extb** por grupo (seção 8.9). Os anúncios da extensão são 56 (14 turmas x 2 grupos x 2 conjuntos): 28 -exta e 28 -extb, **42 liberados para o qa** (26 -exta e 16 -extb) e **14 bloqueados** (2 -exta de 662, bloqueada de vez, e 12 -extb: 333, 68632, 68635, 679, 366 e 662). Entre os 26 -exta liberados, os de 68635, 679 e 366 (6 anúncios) são **liberados pelo gestor-de-midia** (memorando da onda 2, item g) e sobem só depois do qa desta versão e da aprovação do MO6 (M2 do qa onda2c), e os de 333 e 68632 (4 anúncios) são o **texto novo `_v2`** das decisões do cmo, com a versão antiga arquivada até a OU3. Nunca os dois conjuntos ativos juntos.

| Anúncio (nome = utm_content) | Grupo | Texto | Fixações [SUPOSIÇÃO] |
|---|---|---|---|
| rsa-<código>-area-a_v1 | `__area` | A | título da área na posição 1; "Faculdade UFAPE" na posição 3; descrição 1 fixada (a do nome completo) |
| rsa-<código>-area-b_v1 | `__area` | B (não em 662) | igual |
| rsa-<código>-marca-a_v1 | `__marca` | A | "Faculdade UFAPE" na posição 1; título da área na posição 2; descrição 1 fixada |
| rsa-<código>-marca-b_v1 | `__marca` | B (não em 662) | igual |
| rsa-<código>-area-exta_v1 (em 333 e 68632, `rsa-<código>-area-exta_v2`) | `__area` | -exta (seção 8.9), do dia seguinte ao corte até a véspera do início, no lugar dos anúncios do corte | título da área na 1; "Faculdade UFAPE" na 3; descrição 1 (DS1 sem data) na 1; descrição 2 (a regra, ou, em 333 e 68632, a data de início e o formato) na 2 |
| rsa-<código>-marca-exta_v1 (em 333 e 68632, `rsa-<código>-marca-exta_v2`) | `__marca` | -exta (seção 8.9), idem | "Faculdade UFAPE" na 1; título da área na 2; descrição 1 na 1; descrição 2 na 2 |
| rsa-<código>-area-extb_v1 | `__area` | -extb (seção 8.9), do início até a véspera do 3º módulo, no lugar dos -exta | igual ao -exta de `__area` |
| rsa-<código>-marca-extb_v1 | `__marca` | -extb (seção 8.9), idem | igual ao -exta de `__marca` |

Em 662 só existem `rsa-662-area-a_v1` e `rsa-662-marca-a_v1` até o corte; o texto B de 662 só entra em nova versão, com conteúdo liberado pela ficha corrigida. Os -exta e -extb de 662 estão escritos, mas bloqueados (seção 8.9).

Cada texto tem até 12 títulos e 4 descrições (o limite é 15 e 4 [SUPOSIÇÃO de plataforma; conferir no editor]); os anúncios -exta e -extb têm 5 títulos e 2 descrições. Quando o CPL da semana fechada passa do limite da seção 4.5, cada grupo fica só com o texto A [SUPOSIÇÃO de desenho: A é o texto de decisão, com campus e turma]. A descrição de nome completo fica fixada na posição 1 em todos: é ela que garante que "Pós-graduação em <área>" e o campus apareçam juntos.

### 8.2 Títulos que valem para várias turmas (até 30 caracteres)

| Código | Título | Caracteres | Uso |
|---|---|---|---|
| C1 | Faculdade UFAPE | 15 | todos |
| C2 | Pós-graduação veterinária | 25 | todos |
| C3 | Para médicos veterinários | 25 | todos, menos 657 e 662 |
| C3b | Para anestesistas já atuantes | 29 | só 657 (público da página; U10 aberta) |
| C4 | Veja a página da turma | 22 | todos |
| C5 | Veja o cronograma na página | 27 | todos |
| C6 | Calendário dos módulos | 22 | texto B, todos, menos 662 |
| C7 | Docentes listados na página | 27 | texto B, só 68615, 289, 657, 68635, 68636, 68617, 68609 e 366 (nas demais não há peça de autoridade docente, criativos v3) |
| C8 | Teoria online e prática | 23 | texto B, semipresenciais, menos 662 |
| C9 | Módulos presenciais | 19 | texto B, onde não há contagem (68615, 341, 68609) |
| C9b | Aulas presenciais | 17 | texto B, só 68632 |

### 8.3 Campos por turma (contados)

Fórmulas de contagem: "Início em dd/mm/aaaa" tem 20 caracteres; "Turma de março de 2027" e "Turma de abril de 2027" têm 22; "<CH> h de carga horária" tem 22 (500, 360 ou 750); "<N> módulos" tem 10; "<N> módulos presenciais" tem 21; "Campus São Paulo" tem 16 e "Campus Goiânia" tem 14; "Semipresencial" tem 14 e "Presencial" tem 10.

| Turma | Título da área (caracteres) | Título extra (caracteres) | Modalidade, CH, módulos | Início (título) | Turma do mês (título) | Contagem de presenciais (título) |
|---|---|---|---|---|---|---|
| 68615 | Patologia Clínica (17) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | não (a ficha não conta) |
| 289 | Cardiologia Veterinária (23) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 333 | Citopatologia Veterinária (25) | - | Semipresencial, 500 h, 24 | Início em 27/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 657 | Anestesiologia Avançada (23) | - | Semipresencial, 360 h, 18 | Início em 13/03/2027 | Turma de março de 2027 | 6 módulos presenciais |
| 341 | Medicina Interna Equina (23) | - | Semipresencial, 500 h, 24 | Início em 20/03/2027 | Turma de março de 2027 | não (a ficha não conta) |
| 68635 | Clínica Médica e Emergência (27), forma curta por limite | Pequenos Animais (16) | Semipresencial, 750 h, 28 | Início em 10/04/2027 | Turma de abril de 2027 | 9 módulos presenciais |
| 68636 | Pneumologia Veterinária (23) | - | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 6 módulos presenciais |
| 68617 | Endocrinologia (14), forma curta por limite | Pequenos Animais (16) | Semipresencial, 500 h, 24 | Início em 17/04/2027 | Turma de abril de 2027 | 2 módulos presenciais |
| 68628 | Oncologia Veterinária (21) | - | Semipresencial, 500 h, 24 | Início em 10/04/2027 | Turma de abril de 2027 | 8 módulos presenciais |
| 68609 | Anestesiologia Veterinária (26) | - | Semipresencial, 500 h, 26 | Início em 24/04/2027 | Turma de abril de 2027 | não (muitos, fora de ordem na ficha) |
| 68632 | Clínica Cirúrgica (17), forma curta por limite | Cães e Gatos (12) | Presencial, 500 h, 24 | Início em 10/04/2027 | Turma de abril de 2027 | não (toda presencial) |
| 679 | Infectologia Veterinária (24) | - | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 3 módulos presenciais |
| 366 | Reabilitação Veterinária (24), forma curta por limite | Fisioterapia e Fisiatria (24) | Semipresencial, 500 h, 24 | sem data (trava) | sem mês (trava) | 9 módulos presenciais |
| 662 | Ortopedia Veterinária (21) | - | só nome, campus e data | Início em 24/04/2027 | Turma de abril de 2027 | não (662 só com nome, campus e data) |

Fontes: nome, campus, modalidade, CH, turma e data de início, catálogo seção 2 (68636 sem data da planilha; 366 e 662 com a divergência registrada); módulos e presenciais, fichas e criativos v3 (contagem nas fichas, seção 18 e Lista 1 de lá), a conferir na ficha no dia da montagem (S8). A forma curta de 68617 ("Endocrinologia"), 68635, 68632 e 366 só existe porque o nome do catálogo passa de 30 caracteres; o nome completo está na descrição fixada, e sem a fixação (AGP18) as formas curtas saem dos títulos.

### 8.4 Texto A, turma e campus (12 títulos; semipresenciais com data)

Ordem dos títulos: 1 título da área (fixar na posição 1 em `__area`); 2 C1; 3 "Campus <praça>"; 4 C2; 5 "Semipresencial"; 6 "Início em dd/mm/aaaa"; 7 "Turma de <mês> de 2027"; 8 "<CH> h de carga horária"; 9 "<N> módulos"; 10 C3 (657: C3b); 11 C4; 12 título extra da turma (onde houver).

Exceções:
- **68636, 679 e 366 (sem data):** os títulos 6 e 7 saem; entram C5 e, em 68636 e 366, o título "<N> módulos presenciais" no lugar do 9 quando ele couber.
- **68632 (presencial):** o título 5 é "Presencial"; o título extra é "Cães e Gatos"; nenhum título diz "semipresencial".
- **662 (só nome, campus e data):** títulos 1, 2, 3, 4, 6, 7 e 11, e C5 (8 títulos). Nenhum título de modalidade, CH, módulos ou público.

**Descrições do texto A (até 90; 4 por anúncio):**

| # | Descrição | Caracteres | Uso |
|---|---|---|---|
| DS1 | nome completo e campus (tabela 8.6) | 59 a 89 | todos; fixada na posição 1 |
| DC | "Veja turma, campus e cronograma na página da Faculdade UFAPE." | 61 | todos, menos 657 e 662 |
| DC657 | "Para médicos veterinários anestesistas já atuantes. Veja a página da turma." | 75 | só 657 (U10 aberta) |
| DS2 | "Semipresencial, 500 h, 24 módulos. Veja o cronograma na página da turma." | 72 | semipresenciais, menos 662; troca CH e N de cada turma, sem mudar o tamanho |
| DS2p | "Presencial, 500 h, 24 módulos. Veja o cronograma na página da turma." | 68 | só 68632 |
| DT | "A turma pode não ser formada: compre passagem e hotel só depois de a turma ser confirmada." | 90 (no limite; frase aprovada do AP8, sem mudança; contada por script pelo qa) | todos, menos 662; depende do AGP20 |

Montagem: A de 68615 usa DS1, DC, DS2 e DT; A de 657 usa DS1, DC657, DS2 e DT; A de 68632 usa DS1, DC, DS2p e DT; A de 662 usa DS1, D662b e D662c (3 descrições, tabela 8.5). Sem o AGP20, a descrição DT sai e o anúncio segue com 3 descrições.

### 8.5 Texto B, formato e prática (12 títulos; não existe em 662)

Ordem dos títulos: 1 título da área; 2 C1; 3 "Campus <praça>"; 4 C8; 5 "<N> módulos presenciais" (onde a ficha conta; senão C9); 6 C6; 7 C5; 8 C7 (só onde permitido); 9 "<N> módulos"; 10 "<CH> h de carga horária"; 11 C3 (657: C3b); 12 "Semipresencial".

Exceções:
- **68632:** títulos 4 e 12 saem; entram C9b ("Aulas presenciais") e "Presencial"; "<N> módulos" fica.
- **662:** sem texto B até a ficha ser corrigida (G5). O texto A de 662 usa as descrições DS1, D662b e D662c abaixo.
- **333, 341, 68628 e 679:** sem C7 (sem peça de autoridade docente).

**Descrições do texto B (até 90; 4 por anúncio) e as de 662:**

| # | Descrição | Caracteres | Uso |
|---|---|---|---|
| DS1 | nome completo e campus (tabela 8.6) | 59 a 89 | todos; fixada na posição 1 |
| DF | "Aulas online e módulos presenciais de prática. Cronograma na página da turma." | 77 | semipresenciais, menos 662 |
| DB2 | "Teoria online e prática presencial nos módulos. Veja o calendário na página da turma." | 85 | semipresenciais, menos 662 |
| DS2 | como no texto A | 72 | semipresenciais, menos 662 |
| DP1 | "Presencial em Goiânia, 24 módulos, um por mês. Veja o cronograma na página da turma." | 84 | só 68632 |
| DP2 | "Aulas presenciais não são transmitidas. Cronograma na página da turma." | 70 | só 68632 (a ficha traz a observação; as fichas de 68636 e 68609 não, e lá a frase não entra) |
| DS2p | como no texto A | 68 | só 68632 |
| D662b | "Faculdade UFAPE, campus São Paulo. Veja o cronograma na página da turma." | 72 | só 662 (texto A) |
| D662c | "Turma com início em 24/04/2027 no campus São Paulo. Veja a página da turma." | 75 | só 662 (texto A) |

Montagem: B das semipresenciais usa DS1, DF, DB2 e DS2; B de 68632 usa DS1, DP1, DP2 e DS2p.

### 8.6 Descrição de nome completo (DS1) por turma

Fórmula: 17 caracteres de "Pós-graduação em " mais o nome mais ", campus <praça>." (19 em São Paulo, 17 em Goiânia) e, quando cabe, " Início em dd/mm/aaaa." (22 caracteres, contados com o espaço inicial; o qa corrigiu a fórmula, antes escrita como 23).

| Turma | DS1 | Caracteres |
|---|---|---|
| 68615 | Pós-graduação em Patologia Clínica, campus São Paulo. Início em 20/03/2027. | 75 |
| 289 | Pós-graduação em Cardiologia Veterinária, campus Goiânia. Início em 20/03/2027. | 79 |
| 333 | Pós-graduação em Citopatologia Veterinária, campus São Paulo. Início em 27/03/2027. | 83 |
| 657 | Pós-graduação em Anestesiologia Avançada, campus São Paulo. Início em 13/03/2027. | 81 |
| 341 | Pós-graduação em Medicina Interna Equina, campus São Paulo. Início em 20/03/2027. | 81 |
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, campus São Paulo. | 83 |
| 68636 | Pós-graduação em Pneumologia Veterinária, campus São Paulo. | 59 |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais, campus São Paulo. | 70 |
| 68628 | Pós-graduação em Oncologia Veterinária, campus São Paulo. Início em 10/04/2027. | 79 |
| 68609 | Pós-graduação em Anestesiologia Veterinária, campus Goiânia. Início em 24/04/2027. | 82 |
| 68632 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, campus Goiânia. Início em 10/04/2027. | 89 (forma padrão, R3 do qa; cabe em 90) |
| 679 | Pós-graduação em Infectologia Veterinária, campus São Paulo. | 60 |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, campus São Paulo. | 86 (perto do limite; recontar no editor) |
| 662 | Pós-graduação em Ortopedia Veterinária, campus São Paulo. Início em 24/04/2027. | 79 |

Nomes completos conferidos no catálogo, seção 2: o catálogo escreve "Pós Graduação" em 333 e 341, e as peças usam "Pós-graduação em <área>" (contexto da linha).

### 8.7 Caminho de exibição

"pos-graduacao" (13) e a área sem acento, até 15: "patologia" (9), "cardiologia" (11), "citopatologia" (13), "anestesiologia" (14), "equina" (6), "clinica-medica" (14), "pneumologia" (11), "endocrinologia" (14), "oncologia" (9), "cirurgia" (8), "infectologia" (12), "reabilitacao" (12), "ortopedia" (9).

### 8.8 Checagem dos textos contra as regras

Nenhum texto do corte traz preço, parcela, matrícula, inscrição, bolsa, desconto, MEC, certificado, "últimas vagas", a data do 3º módulo (decisão 18) ou concorrente. "Para médicos veterinários" e "Para anestesistas já atuantes" repetem o público-alvo da página (não descrevem quem vê o anúncio). A frase DT (passagem e hotel) é a aprovada do AP8 do criativos v3 (1.2, r2), sem mudança, com 90 caracteres.

### 8.9 Anúncios da extensão: dois conjuntos em sequência, -exta e -extb (1 por grupo de cada vez)

Encomenda da estratégia v5 (7.2, item 3), EM16 e a resolução do CC1 pelo orquestrador (criativos ext, seção 2). **Os textos abaixo são os do criativos-de-anuncio (versão 4 do arquivo -ext, seção 3), copiados sem reescrever, com uma troca pedida pelo qa na rodada e (CE1): o título 5 de todo anúncio -exta e -extb é o campus ("Campus São Paulo" ou "Campus Goiânia"), e não mais uma data.** A regra do qa (P1) está cumprida: a regra completa cabe numa única descrição de até 90 caracteres, fixada na posição 2, e nenhum título cita data (EM16). **Em 333 e 68632 a -exta é o texto novo das decisões do cmo (versão 4 do arquivo -ext), sem a regra do 3º módulo; a -exta antiga fica arquivada no fim desta seção.**

**Sequência e troca** (a tabela por turma está na seção 4.6):

1. **Dia seguinte ao corte (troca para a extensão):** o humano **pausa** (nunca remove) os anúncios do corte, que citam a data de início ou o mês da turma sem a regra completa, e ativa o anúncio **-exta** de cada grupo (`rsa-<código>-area-exta_v1` e `rsa-<código>-marca-exta_v1`; em 333 e 68632, `_v2`), só se a turma tiver as condições da seção 4.6. Os -exta e os -extb são criados antes, já pausados, e aprovados pelo qa.
2. **Véspera do início:** último dia do -exta (o -exta nunca fica no ar depois do início); em 333 e 68632, até OU3, é também o último dia da campanha, às 23h59.
3. **Dia do início da turma:** o humano **pausa** os -exta e **ativa** os -extb (`rsa-<código>-area-extb_v1` e `rsa-<código>-marca-extb_v1`), na mesma campanha e no mesmo grupo, sem mudar diária, total, palavras-chave ou negativas (em 68635, 679 e 366, a diária da -extb é a do saldo, seção 4.6). **Nunca os dois pares ativos juntos:** a conferência é ver, no mesmo dia, os -exta pausados e os -extb ativos (ou, onde a -extb está bloqueada, os dois pares pausados). Em sábado, domingo e feriado, a forma de execução é a da seção 4.7.
4. **Véspera do 3º módulo, 23h59:** pausa total (seção 4.6, item 8).
5. Não existe grupo amplo na estrutura, então nenhum grupo é pausado e nenhuma palavra-chave muda (seção 6, nota d).

**Montagem, igual nas duas fases:**
- **Títulos (5):** 1 título da área; 2 "Faculdade UFAPE"; 3 e 4 conforme a fase (abaixo); **5 o campus da turma: "Campus São Paulo" (16) ou "Campus Goiânia" (14; 289, 68609 e 68632)**. Estes 5 títulos **substituem** os títulos herdados do texto A (que não cabem na extensão por citarem "Início em dd/mm/aaaa" ou o mês da turma); títulos herdados só voltam com aprovação do qa.
  - **-exta:** 3 "Matrícula segue aberta" (22); 4 "Aberta até o 3º módulo" (22). **Exceção, -exta nova de 333 e 68632: o título 4 é "Módulo 1 presencial" (19) em 333 e "Turma presencial" (16) em 68632.**
  - **-extb:** 3 "Matrícula até o 3º módulo" (25); 4 "As aulas já começaram" (21).
- **Descrições (2):** descrição 1 = DS1 sem data (tabela abaixo, a mesma nas duas fases), **fixada na posição 1**; descrição 2 = **a regra completa da fase, fixada na posição 2** (tabela por turma), com a data de início e a do 3º módulo (ou o mês da ficha) **só aqui**. **Na -exta nova de 333 e 68632, a descrição 2 traz só a data de início e o formato, sem "3º módulo" e sem a data do 3º módulo (regra 8).** A DC, a DS2 e a DT do corte não entram. A DT não entra em nenhum anúncio da extensão no Google, nem na -exta nem na -extb (no Meta, ela segue na -exta): com as descrições 1 e 2 fixadas, uma 3ª descrição não aparece [SUPOSIÇÃO de plataforma; conferir no editor; RE1 do qa, rodada e].
- **Fixações:** em `__area`, título da área na posição 1 e "Faculdade UFAPE" na 3; em `__marca`, "Faculdade UFAPE" na 1 e título da área na 2; descrição 1 na posição 1 e descrição 2 na posição 2. Os títulos 3, 4 e 5 não são fixados: qualquer combinação deles é verdadeira, e **nenhum título cita data** [SUPOSIÇÃO de plataforma; conferir no editor].
- **Nome e UTM:** `rsa-<código>-<grupo>-exta_v1` e `rsa-<código>-<grupo>-extb_v1` como utm_content (em 333 e 68632, a -exta é `rsa-<código>-<grupo>-exta_v2`); utm_campaign é o da campanha (seção 10).
- **Recursos:** a frase de destaque "Início em dd/mm/aaaa" sai da campanha na extensão, nas duas fases (seção 9).
- **Limite de volume:** 1 anúncio por grupo é o último degrau da escada (seção 4.5).
- **662:** só nome, campus e data da planilha; nenhum texto de modalidade, CH, módulos, público ou docente; sem DT. Os textos estão prontos, com "[DATA]" no lugar do 3º módulo (15 caracteres de uma data de dois dias nas contagens; 5 a menos se for um dia só), e bloqueados.

**Títulos 1 e 5 e descrições 2 por turma** (copiados do criativos ext, seção 3, com o título 5 trocado por CE1; caracteres entre parênteses; os títulos 2, 3 e 4 são os comuns acima, salvo a exceção da -exta de 333 e 68632):

| Turma | Título 1 | Título 5 (as duas fases) | -exta, descrição 2 (regra, fixada na posição 2) | -extb, descrição 2 (regra, fixada na posição 2) |
|---|---|---|---|---|
| 68615 | Patologia Clínica (17) | Campus São Paulo (16) | As aulas começam em 20/03/2027. Matrícula aberta até o 3º módulo, em 22 e 23/05/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 22 e 23/05/2027. Fale com o time. (86) |
| 289 | Cardiologia Veterinária (23) | Campus Goiânia (14) | As aulas começam em 20/03/2027. Matrícula aberta até o 3º módulo, em 15 e 16/05/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 15 e 16/05/2027. Fale com o time. (86) |
| 333 (-extb bloqueada por OU3; **-exta nova `_v2`, título 4 "Módulo 1 presencial" (19)**) | Citopatologia Veterinária (25) | Campus São Paulo (16) | **As aulas começam em 27/03/2027. Módulo 1 presencial. Veja datas na página da turma. (83)** | As aulas já começaram. Matrícula até o 3º módulo, em 29 e 30/05/2027. Fale com o time. (86) |
| 657 | Anestesiologia Avançada (23) | Campus São Paulo (16) | As aulas começam em 13/03/2027. Matrícula aberta até o 3º módulo, em 22 e 23/05/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 22 e 23/05/2027. Fale com o time. (86) |
| 341 | Medicina Interna Equina (23) | Campus São Paulo (16) | As aulas começam em 20/03/2027. Matrícula aberta até o 3º módulo, em 01 e 02/05/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 01 e 02/05/2027. Fale com o time. (86) |
| 68635 (**-exta liberada pelo gestor**, item g; -extb bloqueada: dia do 3º módulo) | Clínica Médica e Emergência (27, forma curta por limite) | Campus São Paulo (16) | As aulas começam em 10/04/2027. Matrícula aberta até o 3º módulo, em junho de 2027. (83) | As aulas já começaram. Matrícula até o 3º módulo, em junho de 2027. Fale com o time. (84) |
| 68636 | Pneumologia Veterinária (23) | Campus São Paulo (16) | As aulas começam em abril de 2027. Matrícula aberta até o 3º módulo, em 19 e 20/06/2027. (88) | As aulas já começaram. Matrícula até o 3º módulo, em 19 e 20/06/2027. Fale com o time. (86) |
| 68617 | Endocrinologia (14, forma curta por limite) | Campus São Paulo (16) | As aulas começam em 17/04/2027. Matrícula aberta até o 3º módulo, em 19 e 20/06/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 19 e 20/06/2027. Fale com o time. (86) |
| 68628 | Oncologia Veterinária (21) | Campus São Paulo (16) | As aulas começam em 10/04/2027. Matrícula aberta até o 3º módulo, em 26 e 27/06/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 26 e 27/06/2027. Fale com o time. (86) |
| 68609 | Anestesiologia Veterinária (26) | Campus Goiânia (14) | As aulas começam em 24/04/2027. Matrícula aberta até o 3º módulo, em 26 e 27/06/2027. (85) | As aulas já começaram. Matrícula até o 3º módulo, em 26 e 27/06/2027. Fale com o time. (86) |
| 68632 (-extb bloqueada por OU3; **-exta nova `_v2`, título 4 "Turma presencial" (16)**) | Clínica Cirúrgica (17, forma curta por limite) | Campus Goiânia (14) | **As aulas começam em 10/04/2027. Turma presencial. Veja o cronograma na página da turma. (87)** | As aulas já começaram. Matrícula até o 3º módulo, em 12 e 13/06/2027. Fale com o time. (86) |
| 679 (**-exta liberada pelo gestor**, item g; -extb bloqueada: dia do 3º módulo) | Infectologia Veterinária (24) | Campus São Paulo (16) | As aulas começam em abril de 2027. Matrícula aberta até o 3º módulo, em junho de 2027. (86) | As aulas já começaram. Matrícula até o 3º módulo, em junho de 2027. Fale com o time. (84) |
| 366 (**-exta liberada pelo gestor**, item g; -extb bloqueada: dia do 3º módulo; data de início só depois de P4) | Reabilitação Veterinária (24, forma curta por limite) | Campus São Paulo (16) | As aulas começam em abril de 2027. Matrícula aberta até o 3º módulo, em junho de 2027. (86) | As aulas já começaram. Matrícula até o 3º módulo, em junho de 2027. Fale com o time. (84) |
| 662 (-exta e -extb bloqueadas: ficha de 2026 e sem 3º módulo) | Ortopedia Veterinária (21) | Campus São Paulo (16) | As aulas começam em 24/04/2027. Matrícula aberta até o 3º módulo, em [DATA]. (85, contada com uma data de dois dias no lugar de "[DATA]") | As aulas já começaram. Matrícula até o 3º módulo, em [DATA]. Fale com o time. (86, contada com uma data de dois dias no lugar de "[DATA]") |

**Bloqueios por turma** (criativos ext v4, item g do memorando da onda 2 e decisões do cmo; nada sobe com bloqueio aberto):

| Turma | -exta | -extb |
|---|---|---|
| 68615, 289, 657, 341, 68636, 68617, 68628, 68609 | liberada para o qa (travas gerais e da seção 11) | liberada para o qa |
| 333 | liberada para o qa: **-exta nova `_v2`, sem a regra do 3º módulo**; a antiga fica arquivada até a OU3 | **bloqueada por OU3** (só sobe se OU3 for respondida e a extensão correr até 28/05) |
| 68632 | liberada para o qa: **-exta nova `_v2`, sem a regra do 3º módulo**; a antiga fica arquivada até a OU3 | **bloqueada por OU3** (só sobe se OU3 for respondida e a extensão correr até 11/06) |
| 68635, 679, 366 | **liberada pelo gestor-de-midia (memorando da onda 2, item g; R$ 1,36, R$ 1,29 e R$ 1,36; teto da -exta R$ 39,44, R$ 37,41 e R$ 39,44); sobe só depois do qa desta versão e da aprovação do MO6** | **bloqueada sem o dia do 3º módulo** [CONFIRMAR NO CATÁLOGO]; com o dia, diária pelo saldo (seção 4.6) |
| 662 | **bloqueada** (ficha de 2026, P3, e sem 3º módulo) | **bloqueada** |

Totais: 26 -exta e 16 -extb liberados (42); 2 -exta (662, dois grupos) e 12 -extb bloqueados (14). Dos 26 -exta liberados, 6 (68635, 679 e 366) dependem da aprovação do MO6 depois do qa desta versão e 4 (333 e 68632) são o texto novo `_v2`.

**DS1 sem data (descrição 1, fixada na posição 1, igual em -exta e -extb; é a DS1 da tabela 8.6 menos " Início em dd/mm/aaaa.", 22 caracteres; contagens recontadas pelo qa na rodada d):**

| Turma | DS1 sem data | Caracteres |
|---|---|---|
| 68615 | Pós-graduação em Patologia Clínica, campus São Paulo. | 53 |
| 289 | Pós-graduação em Cardiologia Veterinária, campus Goiânia. | 57 |
| 333 | Pós-graduação em Citopatologia Veterinária, campus São Paulo. | 61 |
| 657 | Pós-graduação em Anestesiologia Avançada, campus São Paulo. | 59 |
| 341 | Pós-graduação em Medicina Interna Equina, campus São Paulo. | 59 |
| 68635 | Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, campus São Paulo. | 83 (a DS1 do corte já é sem data) |
| 68636 | Pós-graduação em Pneumologia Veterinária, campus São Paulo. | 59 (idem) |
| 68617 | Pós-graduação em Endocrinologia de Pequenos Animais, campus São Paulo. | 70 (idem) |
| 68628 | Pós-graduação em Oncologia Veterinária, campus São Paulo. | 57 |
| 68609 | Pós-graduação em Anestesiologia Veterinária, campus Goiânia. | 60 |
| 68632 | Pós-graduação em Clínica Cirúrgica de Cães e Gatos, campus Goiânia. | 67 |
| 679 | Pós-graduação em Infectologia Veterinária, campus São Paulo. | 60 (idem) |
| 366 | Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, campus São Paulo. | 86 (idem; perto do limite) |
| 662 | Pós-graduação em Ortopedia Veterinária, campus São Paulo. | 57 |

**Pontos de atenção de contagem:** maior título 27 (título 1 de 68635), com o título 5 trocado pelo campus (16 ou 14); maior descrição 2, 88 (68636, -exta); maior DS1, 86 (366). A -exta nova de 333 (título 4 de 19, descrição 2 de 83) e de 68632 (título 4 de 16, descrição 2 de 87) fica dentro desses máximos. Recontar no editor antes de subir (S9).

**-exta antiga de 333 e de 68632 (versão da rodada f, arquivada; só depois da OU3; não sobe enquanto a OU3 estiver aberta; texto copiado do criativos ext v4, sem alteração).** Com a OU3 respondida, o cmo decide em ciclo extra se ela volta e se a -extb sobe. Nomes `rsa-333-area-exta_v1`, `rsa-333-marca-exta_v1`, `rsa-68632-area-exta_v1` e `rsa-68632-marca-exta_v1`, sem uso.

- 333: títulos 1 "Citopatologia Veterinária" (25) | 2 "Faculdade UFAPE" (15) | 3 "Matrícula segue aberta" (22) | 4 "Aberta até o 3º módulo" (22) | 5 "Campus São Paulo" (16); descrição 1, fixada (61): "Pós-graduação em Citopatologia Veterinária, campus São Paulo."; descrição 2 (85): "As aulas começam em 27/03/2027. Matrícula aberta até o 3º módulo, em 29 e 30/05/2027."
- 68632: títulos 1 "Clínica Cirúrgica" (17, forma curta por limite) | 2 "Faculdade UFAPE" (15) | 3 "Matrícula segue aberta" (22) | 4 "Aberta até o 3º módulo" (22) | 5 "Campus Goiânia" (14); descrição 1, fixada (67): "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, campus Goiânia."; descrição 2 (85): "As aulas começam em 10/04/2027. Matrícula aberta até o 3º módulo, em 12 e 13/06/2027."

---

## 9. Recursos (extensões)

Nenhum recurso mostra preço, parcela, matrícula ou valor de inscrição (decisão 16).

| Recurso | Conteúdo | Condição |
|---|---|---|
| Frases de destaque (até 25) | "Faculdade UFAPE" (15); "Campus São Paulo" (16) ou "Campus Goiânia" (14); "Semipresencial" (14) ou "Presencial" (10); "Início em dd/mm/aaaa" (20, onde há data); "<CH> h de carga horária" (22, menos 662); "Módulos presenciais" (19, ou "Aulas presenciais" (17) em 68632); "Cronograma na página" (20); "Corpo docente na página" (23, só onde C7 vale) | todas as campanhas; 662 só com marca, campus, data e cronograma; **na extensão (-exta e -extb), "Início em dd/mm/aaaa" sai (cita a data sem a regra completa, EM16) e as demais ficam** |
| Snippet estruturado | cabeçalho "Cursos" [SUPOSIÇÃO de cabeçalho disponível em português]; de 3 a 10 valores de até 25 caracteres [SUPOSIÇÃO de plataforma; conferir no editor] | só onde o programa está na ficha; nas demais, sem snippet [CONFIRMAR na ficha] |
| Sitelinks (até 25) | "Calendário dos módulos" (22); "Corpo docente" (13); "Como funciona" (13); "Todas as pós-graduações" (23) | só com URL distinta da página da turma e aceita pelo editor [CONFIRMAR]; sem URL própria, não sobe (o anúncio vale sem sitelink) |
| Chamada | não | atendimento instável em 22/10 e destino é a página, nunca WhatsApp |
| Formulário de lead | não | a coleta é na página da turma |
| Imagem e preço | não | decisão 16 |

Valores de snippet (módulos da ficha como estão nas peças aprovadas do criativos v3):

| Turma | Valores (caracteres) |
|---|---|
| 68615 | Hemostasia (10); Hemoparasitoses (15); Mielograma (10); Automação do hemograma (22) |
| 289 | Eletrocardiograma (17); Taquiarritmias (14); Bradiarritmias (14); Ecocardiografia (15) |
| 333 | Citologia básica (16); Imunocitopatologia (18); Leitura de lâminas (18); Derrames cavitários (19); Mielograma (10) |
| 657 | Hemodinâmica avançada (21); Ventilação mecânica (19); Bloqueios locorregionais (24) |
| 68628 | Imunoterapia (12); Eletroquimioterapia (19); Biossegurança (13) |
| 68609 | Avaliação pré-anestésica (24); Monitoração (11); Anestesia inalatória (20) |
| 366 | Hidroterapia (12); Cinesioterapia (14); Recursos eletrofísicos (22); Terapias manuais (16) |
| 341, 68635, 68636, 68617, 68632, 679, 662 | sem snippet até o programa da ficha ser conferido [CONFIRMAR] |

---

## 10. UTM, rastreio e conversões

- **Marcação automática** (gclid) ligada na conta [CONFIRMAR].
- **Sufixo de URL final**, no nível do anúncio: `utm_source=google&utm_medium=cpc&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term={keyword}` (D11 e D12). Minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Nenhum dado pessoal em UTM. A chave com área curta e o nome do anúncio esperam a ratificação do cmo (seção 1, nota sobre o D12).
- **Exemplo (68615, `__area`, texto A):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68615-patclin_google_lead_busca_202612&utm_content=rsa-68615-area-a_v1&utm_term={keyword}`.
- **Exemplo (68632, `__marca`, texto B):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68632-cirurgia-go_google_lead_busca_202701&utm_content=rsa-68632-marca-b_v1&utm_term={keyword}`.
- **Exemplo da extensão, antes do início (68615, `__area`, anúncio -exta):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68615-patclin_google_lead_busca_202612&utm_content=rsa-68615-area-exta_v1&utm_term={keyword}`.
- **Exemplo da extensão, a partir do início (68615, `__marca`, anúncio -extb):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_68615-patclin_google_lead_busca_202612&utm_content=rsa-68615-marca-extb_v1&utm_term={keyword}`.
- **Exemplo da -exta nova (333, `__area`, `_v2`; só a -exta nova enquanto a OU3 estiver aberta; a `_v1` arquivada não é usada):** `utm_source=google&utm_medium=cpc&utm_campaign=pos_333-citopato_google_lead_busca_202612&utm_content=rsa-333-area-exta_v2&utm_term={keyword}`. Em 68632, `utm_content=rsa-68632-area-exta_v2` e `rsa-68632-marca-exta_v2`, com `utm_campaign=pos_68632-cirurgia-go_google_lead_busca_202701`.
- A extensão não cria campanha nova: o utm_campaign é o mesmo e só o utm_content leva o sufixo -exta ou -extb [SUPOSIÇÃO de desenho, estratégia 4.2; origem: manter o histórico e a leitura por turma]. A analise-de-midia lê a extensão pelo padrão `rsa-<código>-<grupo>-ext[ab]_v[12]` e compara as duas fases pela mesma diária (em 68635, 679 e 366 a diária da -extb é a do saldo; em 333 e 68632 a -exta `_v2` é a única).
- **Anúncios já no ar** (289 e 662, se tiverem busca) não são renomeados; a análise lê por tabela de correspondência (D12). A busca atual de 662, se existir, entra na pausa do OM2 (seção 4.3).
- **Conversões:**

| Conversão | Papel | Onde é medida | Observação |
|---|---|---|---|
| Lead (cadastro; ou início de checkout) | primária, entra no lance | tag do Google na página da turma | teste de 30/10 (EA4); evento que a página registra [CONFIRMAR] |
| Inscrição paga | secundária, só leitura [SUPOSIÇÃO de plataforma; conferir no editor] | loja ou CRM | importação de conversão offline só com o padrão do arquiteto-de-fluxos (P15) e a base legal [CONFIRMAR]; valor da inscrição fora dos textos até U11 |
| 1ª mensalidade paga (matrícula de fato) | secundária, só leitura [SUPOSIÇÃO de plataforma; conferir no editor] | CRM e financeiro | idem |

Os dois pagamentos são lidos por turma e somados no CRM (só números somados, nenhum dado pessoal). Com a decisão 18 (matrícula até o 3º módulo), a 1ª mensalidade é contada até a véspera do 3º módulo e o custo por matrícula é lido depois do corte e de novo depois do fim da extensão (estratégia 2.5) [CONFIRMAR com o gestor a janela de leitura].

---

## 11. Travas de subida (nada sobe com trava aberta)

| Turma | Trava | Quem resolve | O que fica valendo até lá |
|---|---|---|---|
| Todas | Teste de rastreio de 30/10 (lead disparando na página, UTM chegando ao CRM); aprovação de PP16, EM4, EM11 e EM13 a EM16 | Ufape e humano | nada sobe |
| **As 14 páginas com a frase "CERTIFICADO PELO MEC" (P2/A7)** | a página ainda publica a frase (46 páginas no site); a squad não a repete | Ufape (regulação) ou a pessoa do marketing | **a campanha da turma só sobe com decisão registrada da pessoa do marketing ou com a página corrigida (igual ao S8 do anuncios-meta)** |
| 679 | **P3:** link da planilha trocado (a linha "Citopatologia 03/04" aponta para 679); sem data e sem preço em peça final | Ufape (correção) e pessoa do marketing com ciência do cmo (liberação; pedido A12) | campanha pronta e pausada, sem data nos textos |
| 68636 | **P3:** data só no site (planilha sem data, U6); sem data e sem preço em peça final | Ufape e pessoa do marketing com ciência do cmo (A12) | sem data nos textos |
| 662 | **P3 e OU18:** a página mostra início em 15/08/2026, cronograma de 2026, turma IV e preço de outra turma; **campanha atual (a Busca, se houver) pausada pelo OM2 até a OU18** (seção 4.3); o limite de R$ 500,00 e o teto de R$ 2.000,00 prevalecendo valem só se a campanha atual voltar a rodar; estrutura nova só com a OU18 respondida, ficha de 2027 e link corrigido | Ufape e pessoa do marketing com ciência do cmo | só nome, campus e data da planilha (24/04/2027); 1 anúncio por grupo; nenhum texto de modalidade, CH, módulos, público ou docente |
| 366 | **P4:** data diverge (planilha 10/04/2027, site 24/04/2027); sobe só com a data conferida na página | Ufape | sem data nos textos |
| 657 | **U10:** pré-requisito formal ainda não escrito na página; **PP7:** desbloqueio de 657 e 341, data alvo 14/12 [SUPOSIÇÃO] | Ufape; pessoa do marketing e cmo | o texto usa só o público da ficha ("anestesistas já atuantes"); se U10 trouxer pré-requisito formal, o texto muda em nova versão |
| 341 | **PP7**; **PR7:** regra da promoção de 20% (nenhum texto cita promoção ou desconto); local da prática com cavalos [CONFIRMAR] | Ufape; pessoa do marketing e cmo | sem promoção, sem local da prática, sem contagem de presenciais |
| 68617 | **URL:** a ficha termina em "/v/" (turma V; planilha VII); conferir se o destino é a turma da planilha; sem número de turma em peça | Ufape | sem número de turma |
| 68628 | **P5:** turma diverge (planilha VI, site VII); sem número de turma em peça | Ufape | sem número de turma |
| 289 | Teto de R$ 2.000,00; limite de R$ 500,00 da campanha atual até 06/12; diárias recalculadas em 30/11; excedente sobre R$ 425,00 sai da manutenção | analise-de-midia e gestor | seção 4.3 |
| 68615 e 333 | **PP6:** motivo da pausa anterior conhecido, meta escrita, criativos aprovados e página sem pendência | gestor e qa | - |
| 68632 | Nunca "semipresencial" | - | texto e negativa já cuidam disso |
| **Extensão, todas** | só sobe se a turma não tiver 15 matrículas nem lotado [CONFIRMAR vagas]; os textos -exta e -extb (criativos ext v4 com CE1) precisam ser aprovados pelo qa; OU6 (véspera) [CONFIRMAR]; **a troca de -exta para -extb é pedido humano no dia do início, nunca com os dois pares ativos; em sábado, domingo e feriado, plano A, B ou C da seção 4.7 (plano A testado até 15/01; plantão nomeado pela Ufape [CONFIRMAR nomes])** | gestor; qa; Ufape | os anúncios do corte são pausados e a campanha não gasta além do corte; nada de extensão sem texto aprovado |
| **333 e 68632 (extensão)** | módulo 1 presencial: a extensão para na véspera dele (26/03 e 09/04) até OU3, às 23h59; **só a -exta nova (`_v2`, sem "Matrícula aberta até o 3º módulo" e sem a data do 3º módulo) roda, a -exta antiga fica arquivada e a -extb fica bloqueada**; 26/03 é a sexta da Paixão (término programado antes do feriado, MO5, ou plano C) | Ufape (OU3); cmo (com OU3, decide se a antiga volta e se a -extb sobe) | pausa total em 26/03 e 09/04 |
| **68635, 679 e 366 (extensão)** | **a -exta está liberada pelo gestor-de-midia (memorando da onda 2, item g; diária R$ 1,36, R$ 1,29 e R$ 1,36; teto da -exta R$ 39,44, R$ 37,41 e R$ 39,44), depois do qa desta versão e da aprovação do MO6; a -extb fica bloqueada sem o dia do 3º módulo** (regra do saldo, seção 4.6); sem o dia, a -exta para às 23h59 da véspera do início (09/04, 02/04 e 09/04) e o saldo não é gasto; 679 só com P3 resolvida e 366 só com P4 resolvida | Ufape (data) e gestor | até o fim da -exta; o texto da -extb fica pronto e pausado |
| **662 (extensão)** | **-exta e -extb bloqueadas:** ficha de 2026 (P3) e sem 3º módulo; os R$ 150,00 não são gastos; em 662, 4.3 define o valor; campanha atual pausada pelo OM2 | Ufape (ficha e data) e gestor | só até o corte, e só depois da OU18 |

Também seguem [CONFIRMAR]: páginas que dizem turma mínima de 20 (a decisão 11 fixa 15; nenhum texto cita o número); política de privacidade e finalidade do formulário em cada página.

---

