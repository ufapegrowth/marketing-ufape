# Estrutura de Google Ads da Pós-graduação: Busca das provas de bolsa e das turmas de março e de abril (etapa 1.14)

- **Agente:** anuncios-google (departamento 11 Mídia Paga, por encomenda do gestor-de-midia)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Etapa:** 1.14 da camada 1 do plano do cmo, encomenda da seção 7 de saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md e das seções 4.4 a 4.6 de saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada sobe, muda, pausa ou gasta a partir deste arquivo. Toda linha é pedido para um humano executar no Google Ads.
- **Entradas lidas:**
  - /home/user/marketing-ufape/.claude/agents/anuncios-google.md
  - /home/user/marketing-ufape/.claude/skills/estrutura-de-campanha-paga/SKILL.md
  - /home/user/marketing-ufape/CLAUDE.md
  - /home/user/marketing-ufape/docs/execucao-2026-10-26.md (decisões 1 a 13)
  - /home/user/marketing-ufape/saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 12
  - /home/user/marketing-ufape/contexto/ufape-geral.md e /home/user/marketing-ufape/contexto/pos-graduacao.md
  - /home/user/marketing-ufape/contexto/catalogo-de-cursos.md (seções 2 e 3) e as URLs oficiais das fichas de contexto/cursos/pos/
  - /home/user/marketing-ufape/saidas/11-midia-paga/estrategia-de-midia-pos-2026-10-26.md (1.13)
  - /home/user/marketing-ufape/saidas/11-midia-paga/gestor-de-midia-pos-2026-10-26.md (1.11)
  - /home/user/marketing-ufape/saidas/11-midia-paga/analise-de-midia-pos-2026-10-26.md (1.12)
  - /home/user/marketing-ufape/saidas/11-midia-paga/criativos-de-anuncio-pos-2026-10-26.md (seção 5, Google Busca)
  - /home/user/marketing-ufape/saidas/11-midia-paga/anuncios-meta-pos-2026-10-26.md (mesma etapa; mesmos nomes e regras)
  - /home/user/marketing-ufape/auditorias/conformidade-educacional.md
- **Não lido:** a pesquisa-de-palavras-chave-pos (não estava na lista desta etapa). Toda palavra-chave abaixo é semente [SUPOSIÇÃO], sem volume nem custo por clique: [DADO NÃO FORNECIDO] até a consulta no Planejador de Palavras-chave.
- **Regra de conflito:** onde as entradas divergem da seção 12, vale a seção 12. A numeração do pedido (D13, D14, D15) corresponde, no arquivo lido, à seção 12.6, a D11 e D12 e a D13.
- **Não aberto:** faculdade.ufape.com.br. Nenhuma busca na web.
- **Dados pessoais:** nenhum. Nenhum docente nomeado.
- **Marcadores:** [CONFIRMAR], [CONFIRMAR NO CATÁLOGO], [SUPOSIÇÃO], [DADO NÃO FORNECIDO]. Limites de caracteres do Google (título 30, descrição 90, caminho 15, frase de destaque 25, sitelink 25) são referência de plataforma sem fonte nos arquivos [SUPOSIÇÃO; conferir no editor]. Verba em percentual da verba nova da Pós (VN); reais = VN x percentual [CONFIRMAR].

---

## 0. Resumo em cinco linhas

1. Uma campanha de Busca das provas (`pos_provas20261127_google_compra_busca_202611`), com um grupo por área liberada, e uma campanha de Busca por turma de março (5) e de abril lote 1 (6), cada uma com grupo de área e grupo de marca.
2. Anúncios responsivos com até 15 títulos e 4 descrições, todos contados; a seção 12 troca "Prova presencial em 27/11" por "Prova online em 27/11" e "Prova em São Paulo ou Goiânia" pelo campus do grupo; nenhuma frase de MEC, nenhuma urgência, nenhum "Pós em" visível.
3. Palavras-chave sementes de frase e exata, negativas comuns e cruzadas entre turmas e áreas, sem lance em concorrente.
4. UTM `utm_source=google`, `utm_medium=cpc`, `utm_campaign` = nome da campanha (D11, D12), com marcação automática ligada.
5. Onze pedidos de aprovação (AGP1 a AGP11); nada sobe antes de PP1 e PP2. YouTube de março e Performance Max ficam fora desta montagem.

---

## 1. Regras que valem para toda a montagem

| Regra | Valor | Fonte |
|---|---|---|
| Provas | Online, com o campus do grupo; sem endereço, sem "presencial"; 27/11/2026, das 9h às 13h | decisão 11; seção 12.9 |
| Distribuição das bolsas | Sempre visível com qualquer percentual: a descrição com a distribuição completa fica fixada na posição 1 da descrição (seção 3.4) | criativos-de-anuncio-pos, 3.2 e 5.4 |
| Nome do curso | "Pós-graduação em <área>" por extenso nas descrições; títulos usam o nome da área, nunca "Pós em" nem abreviação; "pós em" só como palavra-chave | 1.13, 4.1 |
| Marca | "Faculdade UFAPE" em todo anúncio (homonímia com a universidade federal) | 1.13, 4.1 |
| Preço de turma | Só em descrição, sempre com parcelas, valor, total e matrícula juntos; nenhum título com preço de turma (um título sozinho mostraria o preço sem as condições) | conformidade; catálogo |
| Turma mínima | 15, só onde a página da turma já disser 15 [CONFIRMAR por página] | decisão 11 |
| Concorrente | Nenhum nome de concorrente em anúncio; nenhum lance em marca de concorrente; o nome pode ser negativa | anuncios-google.md; gestor 3 |
| Políticas | Sem ponto de exclamação no título, sem caixa alta para gritar (UFAPE é sigla), sem símbolos para chamar atenção [SUPOSIÇÃO de política do Google] | criativos, 5.7 |
| Rede | Só Rede de Pesquisa do Google; sem parceiros de pesquisa e sem Display [SUPOSIÇÃO de desenho: Display fora pelo gestor; parceiros sem leitura de qualidade] | gestor 3 |
| Nomes | `<chave>_google_<objetivo>_busca_<AAAAMM>`; grupo = campanha + `__` + grupo; anúncio = `rsa-<código ou área>_<tema>_vN` | D12; 1.13, 4.2 |
| UTM | marcação automática ligada e sufixo de URL final com `utm_source=google&utm_medium=cpc&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term={keyword}` | D11, D12 |

**Divergências resolvidas pela seção 12:** a UTM das provas no criativos (`utm_medium=pago`, `utm_campaign=provas-de-bolsa-2026-11-27`) e na 1.13 (4.3, exceção) passa ao padrão D11 e D12; a chave das turmas fica só com o código (`pos_68615`), sem área curta.

---

## 2. Modelo de estrutura

| Frente | Modelo | Motivo |
|---|---|---|
| P1 Provas | 1 campanha, orçamento na campanha compartilhado entre os grupos de área | Busca por "prova de bolsa" + área tem volume desconhecido e provavelmente baixo por área [SUPOSIÇÃO]; um orçamento único deixa a verba ir para a área que é buscada (1.13, 4.1) |
| P3 e P4 Turmas | 1 campanha por turma, orçamento na campanha, 2 grupos (área e marca) | Meta e verba por turma (CPLmax_h); código no nome; mudança de uma turma não mexe nas outras |

Estratégia de lance [SUPOSIÇÃO de desenho, AGP3]: "Maximizar conversões" com a conversão de compra (provas) ou de cadastro ou início de checkout (turmas, EM11), sem CPA desejado até haver conversões registradas; depois, CPA desejado igual ao CPImax ou ao CPLmax_h, com aprovação. Sem histórico de custo por clique na conta, não há base para lance manual.

---

## 3. P1 Provas de bolsa (sobe em 03/11, pausa em 27/11)

### 3.1 Campanha

| Campo | Valor |
|---|---|
| Nome | pos_provas20261127_google_compra_busca_202611 |
| Objetivo e conversão | Vendas; conversão principal: compra da inscrição de R$ 100,00 (tag do Google na página de confirmação) testada em 30/10 |
| Orçamento | 3,60% de VN na fase 1 (03/11 a 09/11; diária 0,5143%), 3,15% na fase 2 (10/11 a 19/11; diária 0,3150%), 3,00% na fase 3 (20/11 a 26/11; diária 0,4286%); total 9,75% de VN (1.13, 3.1) |
| Localização | estado de São Paulo, Goiás e Distrito Federal, com "presença ou interesse" (EM6) [SUPOSIÇÃO de desenho; ampliação só com procedência do CRM] |
| Idioma | português |
| Programação | todos os dias; término em 26/11/2026 |
| Rotação | otimizar (padrão dos responsivos) |

### 3.2 Grupos e palavras-chave sementes [SUPOSIÇÃO; volume e CPC: DADO NÃO FORNECIDO]

Um grupo por área liberada. Em 03/11: `__a12-neuro` (68654) e `__a11-patclin` (68658). Com decisão registrada sobre a página (E2): `__a2-pneumo` (68659), `__a3-clinmed` (68645), `__a5-ultra` (68661), `__a7-endocrino` (68648), `__a10-onco` (68657). Goiânia, só com a página dizendo online e campus Goiânia: `__a1-anest-go` (68640), `__a4-cirurgia-go` (68644); `__a2-cardio-go` (68642) e `__a2-cardio` (68641) só com os links corrigidos. Destino incerto (E5): só com A-C2. Sem grupo: 68649, 68653, 68652, 68655. Grupo geral só com a página única das provas (A-C9).

| Grupo | Palavra-chave | Correspondência |
|---|---|---|
| __a12-neuro | "prova de bolsa pós-graduação neurologia veterinária" | frase |
| | [prova de bolsa neurologia veterinária] | exata |
| | "bolsa pós-graduação neurologia veterinária" | frase |
| | "bolsa de estudos neurologia veterinária" | frase |
| | "faculdade ufape prova de bolsa neurologia" | frase (marca) |
| __a11-patclin | "prova de bolsa pós-graduação patologia clínica veterinária" | frase |
| | [prova de bolsa patologia clínica veterinária] | exata |
| | "bolsa pós-graduação patologia clínica" | frase |
| | "bolsa de estudos patologia clínica veterinária" | frase |
| | "faculdade ufape prova de bolsa patologia clínica" | frase (marca) |
| demais áreas | mesmo padrão, com o nome da especialidade da tabela 5.5 do criativos | frase e exata |

Correspondência ampla fora no começo [SUPOSIÇÃO de desenho: verba pequena, termos amplos gastam fora da intenção]. O relatório de termos de pesquisa é lido em toda revisão (09/11, 16/11, 23/11).

### 3.3 Negativas [SUPOSIÇÃO, a validar pelo relatório de termos]

- **Comuns (lista compartilhada da campanha):** grátis, gratuito, gratuita, pdf, apostila, download, concurso, emprego, vaga de emprego, residência, mestrado, doutorado, sisu, enem, vestibular, universidade federal, pernambuco, agreste, garanhuns, anclivepa (negativa evita aparecer para quem busca o concorrente; nenhum lance nele).
- **Cruzadas entre grupos:** cada grupo nega o nome das especialidades dos outros grupos ativos (ex.: `__a12-neuro` nega "patologia", "pneumologia", "oncologia"; `__a11-patclin` nega "citopatologia", "hematologia", "neurologia"), para que a busca caia no grupo certo.
- **Entre praças:** grupos de São Paulo negam "goiânia"; grupos de Goiânia negam "são paulo".

### 3.4 Anúncio responsivo `rsa-<área>_prova_v1` (um por grupo)

**Títulos compartilhados (13) e de área (2), até 30 caracteres:**

| # | Título | Observação |
|---|---|---|
| S1 | "Prova de bolsa veterinária" (26) | |
| S2 | "Inscrição de R$ 100,00" (22) | |
| S3 | "11 bolsas por prova" (19) | |
| S4 | "Bolsas de 10% a 50%" (19) | só com D2 fixada na descrição 1 |
| S5 | "Prova online em 27/11" (21) | substitui "Prova presencial em 27/11" (decisão 11) |
| S6 | "Prova das 9h às 13h" (19) | horário da ficha; U2 aberta |
| S7 | "Nota de corte 7,0" (17) | |
| S8 | "Faculdade UFAPE" (15) | fixar na posição 3 [SUPOSIÇÃO] |
| S9 | "Pós-graduação veterinária" (25) | |
| S10 | "Bolsas de 50%, 25% e 10%" (24) | só com D2 fixada |
| S11 | "Inscreva-se na prova" (20) | |
| S12 | "Desempate por currículo" (23) | |
| S13 | "Campus São Paulo" (16) | nos grupos de Goiânia: "Campus Goiânia" (14). Substitui "Prova em São Paulo ou Goiânia" |
| A1 | título de área 1 da tabela 5.5 do criativos (ex.: "Prova de bolsa: Neurologia" (26); "Prova 27/11: Patologia Clínica" (30)) | fixar na posição 1 [SUPOSIÇÃO] |
| A2 | título de área 2 (ex.: "Neurologia e Neurocirurgia" (26); "Bolsa em Patologia Clínica" (26)) | |

**Descrições (até 90), 4 por anúncio:**

| # | Descrição | Uso |
|---|---|---|
| D1 | "Prova de bolsa da Faculdade UFAPE: inscrição de R$ 100,00 e 11 bolsas por prova." (80) | todos |
| D2 | "2 bolsas de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0." (68) | todos; fixada na posição 1 da descrição |
| D3 | "Prova online em 27/11/2026, das 9h às 13h, campus São Paulo. Regras na página da prova." (87) | grupos de SP; em Goiânia: "Prova online em 27/11/2026, das 9h às 13h, campus Goiânia. Regras na página da prova." (85) |
| D4 | "Bolsa não acumulativa e intransferível. Resultado por WhatsApp e/ou e-mail." (75) | não nos grupos de 68642, 68644 e 68652 (canal do resultado contraditório, U1) |
| D5 | "Bolsa não acumulativa e intransferível. Inscrição: Pix, boleto ou 1x no cartão." (79) | no lugar de D4 onde D4 não vale |

**Caminho de exibição:** "prova-de-bolsa" (14) / nome da área sem acento, até 15 (ex.: "neurologia" (10); "patologia" (9)).

**URL final:** a página da prova da área (tabela 4.1 do criativos), com o sufixo de UTM da seção 6.

### 3.5 Recursos (extensões)

| Recurso | Conteúdo | Condição |
|---|---|---|
| Frases de destaque (até 25) | "Prova online" (12); "11 bolsas por prova" (19); "Inscrição de R$ 100,00" (22); "Nota de corte 7,0" (17); "Desempate por currículo" (23) | todos os grupos |
| Snippets estruturados | cabeçalho "Cursos" [SUPOSIÇÃO de cabeçalho disponível em português]; valores: especialidades com grupo ativo (ex.: "Neurologia" (10), "Patologia Clínica" (17)) | só especialidades liberadas |
| Sitelinks (até 25) | "Regras da prova" (15); "Como se inscrever" (17) | só com URLs próprias (FAQ ou página única, A-C8 e A-C9) [CONFIRMAR]; sem URL distinta, não sobe |
| Chamada | números de vendas de São Paulo e de Goiânia do contexto geral | só se a Ufape confirmar que atendem ligação [CONFIRMAR]; recomendação: não ativar nesta onda (atendimento instável em 22/10) |
| Formulário de lead | não | coleta fora da página; destino é a página (gestor, 3) |
| Imagem | arte 1:1 de C1 ou C2 sem o quadro "presencial" [SUPOSIÇÃO de recurso disponível na conta] | só depois da troca das artes (AMP2 do anuncios-meta-pos) |

---

## 4. P3 Turmas de março (07/12; 657 e 341 em 14/12, só com PP7) e P4 abril lote 1 (06/01)

### 4.1 Campanhas, orçamento e localização

| Turma | Campanha | Localização (presença ou interesse) | Sobe |
|---|---|---|---|
| 68615 | pos_68615_google_lead_busca_202612 | estado de SP | 07/12 |
| 289 | pos_289_google_lead_busca_202612 | GO e DF | 07/12 |
| 333 | pos_333_google_lead_busca_202612 | estado de SP | 07/12 |
| 657 | pos_657_google_lead_busca_202612 | estado de SP | 14/12, com PP7 |
| 341 | pos_341_google_lead_busca_202612 | estado de SP | 14/12, com PP7 |
| 68635 | pos_68635_google_lead_busca_202701 | estado de SP | 06/01 |
| 68636 | pos_68636_google_lead_busca_202701 | estado de SP | 06/01, com a data conferida na planilha |
| 68617 | pos_68617_google_lead_busca_202701 | estado de SP | 06/01 |
| 68628 | pos_68628_google_lead_busca_202701 | estado de SP | 06/01 |
| 68609 | pos_68609_google_lead_busca_202701 | GO e DF | 06/01 |
| 68632 | pos_68632_google_lead_busca_202701 | GO e DF | 06/01 |

Objetivo "lead": conversão de cadastro, se a página tiver; senão início de checkout (EM11), testada em 30/10. Orçamento por turma (1.13, 3.3): março, 0,2625% de VN por semana no aquecimento (diária 0,0375%), 0,1750% na manutenção de 21/12 a 03/01 (diária 0,0250%; a busca segue na manutenção) e 0,5308% na conversão (diária 0,0758%); abril, 0,2763% por semana (diária 0,0395%). Condição de volume (1.13, 3.4): VN mínima de 188,38 a 380,95 x CPLmax_h em março e 361,90 x CPLmax_h em abril; se não fechar, 1 anúncio responsivo por grupo antes de sair da busca.

### 4.2 Grupos e palavras-chave sementes [SUPOSIÇÃO; volume e CPC: DADO NÃO FORNECIDO]

Dois grupos por campanha: `__area` e `__marca`.

| Turma | __area (frase e exata) | __marca (frase) | Negativas próprias da campanha |
|---|---|---|---|
| 68615 | "pós-graduação em patologia clínica veterinária"; "pós em patologia clínica veterinária"; "especialização patologia clínica veterinária"; [pós patologia clínica veterinária são paulo] | "faculdade ufape patologia clínica" | citopatologia (333), hematologia, goiânia |
| 289 | "pós-graduação em cardiologia veterinária goiânia"; "pós em cardiologia veterinária goiânia"; "especialização cardiologia veterinária goiás" | "faculdade ufape cardiologia goiânia" | ecocardiografia (698), são paulo, pneumologia |
| 333 | "pós-graduação em citopatologia veterinária"; "pós em citopatologia veterinária"; "especialização citopatologia veterinária" | "faculdade ufape citopatologia" | patologia clínica (68615), hematologia, goiânia |
| 657 | "pós-graduação anestesiologia veterinária avançada"; "pós em anestesiologia avançada veterinária" | "faculdade ufape anestesiologia avançada" | locorregional, goiânia; termos de anestesiologia sem "avançada" ficam para 68609 em Goiânia [SUPOSIÇÃO] |
| 341 | "pós-graduação medicina interna equina"; "pós em medicina equina"; "especialização em equinos veterinária" | "faculdade ufape medicina equina" | pequenos animais, cães, gatos |
| 68635 | "pós-graduação clínica médica pequenos animais"; "pós em emergência veterinária"; "especialização clínica médica e emergência veterinária" | "faculdade ufape clínica médica" | terapia intensiva (sem turma em SP), goiânia |
| 68636 | "pós-graduação em pneumologia veterinária"; "pós em pneumologia veterinária" | "faculdade ufape pneumologia" | cardiologia, ventilação mecânica |
| 68617 | "pós-graduação em endocrinologia veterinária"; "pós em endocrinologia pequenos animais" | "faculdade ufape endocrinologia" | nefrologia |
| 68628 | "pós-graduação em oncologia veterinária"; "pós em oncologia veterinária"; "especialização oncologia veterinária" | "faculdade ufape oncologia" | eletroquimioterapia (curso livre 560), goiânia |
| 68609 | "pós-graduação anestesiologia veterinária goiânia"; "pós em anestesiologia veterinária goiás" | "faculdade ufape anestesiologia goiânia" | avançada, locorregional, são paulo |
| 68632 | "pós-graduação clínica cirúrgica cães e gatos goiânia"; "pós presencial goiânia veterinária" (KT17 da pesquisa de palavras-chave, citado pela 1.13); "especialização cirurgia veterinária goiás" | "faculdade ufape cirurgia goiânia" | ortopedia, videocirurgia, são paulo |

**Negativas comuns de todas as campanhas de turma:** grátis, gratuito, pdf, apostila, download, concurso, emprego, vaga de emprego, residência, mestrado, doutorado, ead grátis, universidade federal, pernambuco, agreste, garanhuns, enem, vestibular, sisu, curso livre, curso online gravado [SUPOSIÇÃO; "curso livre" e "gravado" evitam disputar com Livres, sobreposição R6 da 1.9]. "Prova de bolsa" vira negativa nas campanhas de turma de 03/11 a 26/11 [SUPOSIÇÃO de desenho, para a busca da prova cair na campanha das provas]; não se aplica depois (as turmas sobem em dezembro e janeiro).

### 4.3 Anúncio responsivo `rsa-<código>_turma_v1` (2 por grupo de área; 1 no grupo de marca)

Exemplo completo: 68615. Os demais trocam os campos pela tabela 4.4.

**Títulos (até 30):**

| # | Título | Observação |
|---|---|---|
| 1 | "Patologia Clínica Veterinária" (29) | título de área, fixar na posição 1 [SUPOSIÇÃO] |
| 2 | "Patologia Clínica em SP" (23) | título de área 2 |
| 3 | "Faculdade UFAPE" (15) | fixar na posição 3 [SUPOSIÇÃO] |
| 4 | "Pós-graduação veterinária" (25) | |
| 5 | "Campus São Paulo" (16) | |
| 6 | "Início em 20/03/2027" (20) | |
| 7 | "Turma de março de 2027" (22) | |
| 8 | "Semipresencial" (14) | 68632: "Presencial" (10) |
| 9 | "500 h de carga horária" (22) | |
| 10 | "Matrícula de R$ 250,00" (22) | condição da matrícula, sem parcela; o preço completo fica na descrição fixada |
| 11 | "Veja o calendário dos módulos" (29) | |
| 12 | "Turma mínima de 15 alunos" (25) | só se a página disser 15 |
| 13 | "Inscreva-se na página" (21) | |
| 14 | "Módulos práticos presenciais" (28) | só se a ficha da turma descrever o formato assim [CONFIRMAR]; 68632 fora |
| 15 | "Coordenação na página do curso" (30) | |

**Descrições (até 90):**

| # | Descrição | Uso |
|---|---|---|
| DT1 | "Pós-graduação em Patologia Clínica, campus São Paulo. Início em 20/03/2027." (75) | todos |
| DT2 | "Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00." (82) | todos; fixada na posição 2 da descrição, para o preço aparecer sempre completo |
| DT3 | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) | todos |
| DT4 | "A turma é confirmada com o mínimo de 15 alunos. Saiba como funciona na página da turma." (87) | só se a página disser 15; senão "Aulas e módulos explicados mês a mês na página da turma." (56) |

Nenhum título traz parcela, porque o Google pode mostrar o título sem a descrição com o total e a matrícula. A matrícula sozinha (título 10) é condição completa do item "matrícula" e não esconde parcela [SUPOSIÇÃO de leitura da conformidade; se o qa discordar, sai].

**Caminho:** "pos-graduacao" (13) / "patologia" (9).

### 4.4 Campos por turma (contados)

| Turma | Título de área 1 | Título de área 2 | DT1 | DT2 | DT3 |
|---|---|---|---|---|---|
| 68615 | "Patologia Clínica Veterinária" (29) | "Patologia Clínica em SP" (23) | "Pós-graduação em Patologia Clínica, campus São Paulo. Início em 20/03/2027." (75) | "Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 289 | "Cardiologia Veterinária" (23) | "Cardiologia em Goiânia" (22) | "Pós-graduação em Cardiologia Veterinária, campus Goiânia. Início em 20/03/2027." (79) | "Investimento: 30x de R$ 1.180,00 (total de R$ 35.400,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 333 | "Citopatologia Veterinária" (25) | "Citopatologia em São Paulo" (26) | "Pós-graduação em Citopatologia Veterinária, campus São Paulo. Início em 27/03/2027." (83) | "Investimento: 30x de R$ 935,00 (total de R$ 28.050,00) e matrícula de R$ 250,00." (80) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 657 | "Anestesiologia Avançada" (23) | "Anestesiologia Avançada em SP" (29) | "Pós-graduação em Anestesiologia Avançada, campus São Paulo. Início em 13/03/2027." (81) | "Investimento: 30x de R$ 1.613,33 (total de R$ 48.400,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 360 h. Pré-requisito na página do curso." (56) |
| 341 | "Medicina Interna Equina" (23) | "Medicina Equina em São Paulo" (28) | "Pós-graduação em Medicina Interna Equina, campus São Paulo. Início em 20/03/2027." (81) | "Investimento: 30x de R$ 1.450,00 (total de R$ 43.500,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 68635 | "Clínica Médica e Emergência" (27) | "Emergência de Pequenos Animais" (30) | "Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, campus São Paulo." (83) | "Investimento: 30x de R$ 1.100,00 (total de R$ 33.000,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 750 h. Início em 10/04/2027. Veja o calendário dos módulos na página." (85) |
| 68636 | "Pneumologia Veterinária" (23) | "Pneumologia em São Paulo" (24) | "Pós-graduação em Pneumologia Veterinária, campus São Paulo. Início em 17/04/2027." (81) | "Investimento: 30x de R$ 1.265,00 (total de R$ 37.950,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 68617 | "Endocrinologia Veterinária" (26) | "Endocrinologia em São Paulo" (27) | "Pós-graduação em Endocrinologia de Pequenos Animais, campus São Paulo." (70) | "Investimento: 30x de R$ 1.200,00 (total de R$ 36.000,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Início em 17/04/2027. Veja o calendário dos módulos na página." (85) |
| 68628 | "Oncologia Veterinária" (21) | "Oncologia em São Paulo" (22) | "Pós-graduação em Oncologia Veterinária, campus São Paulo. Início em 10/04/2027." (79) | "Investimento: 30x de R$ 1.298,00 (total de R$ 38.940,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 68609 | "Anestesiologia Veterinária" (26) | "Anestesiologia em Goiânia" (25) | "Pós-graduação em Anestesiologia Veterinária, campus Goiânia. Início em 24/04/2027." (82) | "Investimento: 30x de R$ 1.081,67 (total de R$ 32.450,00) e matrícula de R$ 250,00." (82) | "Semipresencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (80) |
| 68632 | "Clínica Cirúrgica Cães e Gatos" (30) | "Cirurgia de Cães e Gatos em GO" (30) | "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, campus Goiânia. Início 10/04/2027." (86) | "Investimento: 30x de R$ 1.100,00 (total de R$ 33.000,00) e matrícula de R$ 250,00." (82) | "Presencial, 500 h. Faculdade UFAPE. Veja o calendário dos módulos na página." (76) |

Títulos 6, 7 e 9 trocam a data, o mês e a carga de cada turma (catálogo, seção 2). 657: o DT3 cita o pré-requisito só depois de ele estar escrito na página (PP7, U10). 341: nenhum texto cita a promoção de 20% até a regra completa (PP7). 68617 e 68628: nenhum texto cita número de turma. 68636: data [CONFIRMAR] na planilha antes de subir.

**URL final:** a página da turma (tabela 5.9 do anuncios-meta-pos), com o sufixo da seção 6.

### 4.5 Recursos das turmas

| Recurso | Conteúdo | Condição |
|---|---|---|
| Frases de destaque | "Faculdade UFAPE" (15); "Campus São Paulo" (16) ou "Campus Goiânia" (14); "Semipresencial" (14) ou "Presencial" (10); "Matrícula de R$ 250,00" (22); "Início em <data>" (até 20) | todas |
| Snippet estruturado | cabeçalho "Cursos" [SUPOSIÇÃO]; valores: módulos ou disciplinas da ficha da turma, até 25 caracteres cada [CONFIRMAR na ficha] | só com o programa da ficha |
| Sitelinks | "Calendário dos módulos", "Coordenação", "Investimento" (até 25) | só se a página tiver âncoras ou URLs próprias [CONFIRMAR]; sem URL distinta, não sobe |
| Chamada e formulário de lead | não | mesmo motivo das provas |

### 4.6 Fora desta montagem

- **YouTube de março** (`pos_marco27_youtube_visualizacao_rmk30d_202612`, exceção EM1): só com PP13 (2 vídeos aprovados, quem grave, condição de volume). A estrutura é montada quando PP13 for aprovado; neste arquivo não há anúncio de vídeo.
- **Performance Max e Display:** fora (gestor, seção 3).
- **Campanhas ativas da Pós no Google:** a visão de campanhas não separa canal; se houver busca ativa de 289, 662 ou das turmas da reta final, ela não é renomeada (D12) e não recebe as palavras-chave das campanhas novas [CONFIRMAR na exportação, A1 da 1.12].

---

## 5. Protocolo de leitura

| Item | Provas | Turmas |
|---|---|---|
| Leitura | custo por inscrito por grupo, com 3 dias e gasto de 1,5 x CPImax; relatório de termos em toda revisão | CPL por grupo; termos |
| Pausa de anúncio | 1,5 a 2 x CPImax sem inscrição | 1,5 a 2 x CPLmax_h sem lead |
| Teste T8 do criativos | fixar S2 ou S3 na posição 2, dentro do mesmo grupo, de 03/11 a 16/11; leitura pelo relatório de recursos e custo por inscrito somado | - |
| Lance | troca para CPA desejado só com conversões registradas e com aprovação | idem |
| Mudanças | uma por campanha por semana; negativa nova a partir do relatório de termos não conta como mudança de estrutura [SUPOSIÇÃO de desenho] | idem |

---

## 6. UTM e rastreio

- Marcação automática (gclid) ligada na conta [CONFIRMAR].
- Sufixo de URL final no nível do anúncio: `utm_source=google&utm_medium=cpc&utm_campaign=<nome da campanha>&utm_content=<nome do anúncio>&utm_term={keyword}`.
- Exemplo das provas: `utm_source=google&utm_medium=cpc&utm_campaign=pos_provas20261127_google_compra_busca_202611&utm_content=rsa-a12-neuro_prova_v1&utm_term={keyword}`.
- Exemplo de turma: `utm_source=google&utm_medium=cpc&utm_campaign=pos_68615_google_lead_busca_202612&utm_content=rsa-68615_turma_v1&utm_term={keyword}`.
- Conversões: compra da inscrição (provas) e cadastro ou início de checkout (turmas), com a tag do Google testada em 30/10; importação de matrícula do CRM só com o padrão do arquiteto-de-fluxos (P15) [CONFIRMAR].

---

## 7. Checklists

### 7.1 Subida

| # | Item |
|---|---|
| S1 | Meta (CPImax ou CPLmax_h) e verba em reais escritas, com aprovador (PP1, PP2) |
| S2 | Tag do Google e conversão certa disparando na página de destino (teste de 30/10); marcação automática ligada |
| S3 | Rede só de Pesquisa; parceiros e Display desligados |
| S4 | Localização com "presença ou interesse" e idioma português |
| S5 | Nomes de campanha, grupo e anúncio e sufixo de UTM como nas seções 3, 4 e 6 |
| S6 | Página de destino coerente: provas dizendo "online" e o campus (AMP2 do anuncios-meta-pos); Goiânia e Cardiologia corrigidas; páginas E2 com decisão registrada sobre a frase ligada ao MEC |
| S7 | Títulos e descrições aprovados pelo qa (conformidade); D2 fixada na descrição 1 das provas; DT2 fixada na descrição 2 das turmas |
| S8 | Negativas comuns, cruzadas e de praça aplicadas antes do primeiro dia |
| S9 | Recursos só com URL própria (sitelinks) e números confirmados (chamada) |
| S10 | Término programado em 26/11 nas provas; turmas sem término automático |
| S11 | Registro de quem montou, revisou e aprovou |

### 7.2 Pausa

Exportar a campanha (grupos, palavras-chave, anúncios, recursos); pausar, nunca remover; conferir gasto zero no dia seguinte; registrar data, hora e motivo; desfazer reativando. Pausas: provas em 27/11; turmas só por pedido; a busca de março segue na manutenção de fim de ano.

---

## 8. Pedidos de aprovação humana (AGP1 a AGP11)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer | Prazo |
|---|---|---|---|---|---|---|
| AGP1 | Campanha das provas da seção 3, com nomes e UTM D11 e D12 | D12; provas ainda não subiram | 9,75% de VN [CONFIRMAR reais] | busca de prova por área com origem lida | trocar o sufixo | 30/10 |
| AGP2 | Títulos e descrições das provas com "online" e campus (S5, S13, D3) | decisão 11 | sem verba | anúncio coerente com a decisão | voltar ao texto anterior só se a decisão mudar | 30/10 |
| AGP3 | Lance "Maximizar conversões" sem CPA desejado no começo | sem histórico de CPC | sem verba nova | aprendizado sem teto errado | lance manual | 30/10 |
| AGP4 | Só Rede de Pesquisa, sem parceiros | controle de qualidade do tráfego | sem verba | gasto só no Google | ligar parceiros | 30/10 |
| AGP5 | Fixações: área na posição 1, "Faculdade UFAPE" na 3; D2 na descrição 1 (provas); DT2 na descrição 2 (turmas) | relevância, marca e preço sempre completo | sem verba | conformidade de preço e bolsa | soltar as fixações | 30/10 |
| AGP6 | Negativas comuns, cruzadas, de praça e "prova de bolsa" nas turmas | evitar disputa interna e termo errado | sem verba | menos gasto fora da intenção | retirar | 30/10 (provas); 30/11 (turmas) |
| AGP7 | Campanhas de março da seção 4 | P3 | 12,3375% de VN no Google em P3 [CONFIRMAR reais] | leads de busca por turma | pausar | 30/11 |
| AGP8 | Campanhas de abril lote 1 da seção 4 | P4 | 0,75% de VN por turma (6 turmas) | demanda de abril | pausar | 30/12 |
| AGP9 | Recursos: frases de destaque e snippets já; sitelinks só com URLs próprias; sem chamada e sem formulário nesta onda | URL distinta e atendimento instável | sem verba | anúncio mais completo sem destino falso | ativar depois | 30/10 |
| AGP10 | Grupos de Goiânia só com a página dizendo online e campus Goiânia; Cardiologia só com os links corrigidos | destino coerente | dentro de P1 | nenhum clique para página errada | pausar os grupos | 31/10 |
| AGP11 | Turma mínima de 15 em título e descrição só onde a página da turma já diz 15 | decisão 11; páginas com 20 | sem verba | transparência sem contradição | tirar o título | 30/11 |

**Os 3 primeiros:** AGP2, AGP1 e AGP5.

---

## 9. Notas sobre arquivos de outros agentes (não alterados)

- **criativos-de-anuncio-pos, seção 5:** S5 "Prova presencial em 27/11", S13 "Prova em São Paulo ou Goiânia", D3 com "presencial", a frase de destaque "Prova presencial" e a UTM `utm_medium=pago` contrariam a decisão 11 e D11; trocas na seção 3.4 e 3.5 deste arquivo. A D2 do criativos ("Bolsas de 50% (monitoria), 25% e 10%") não mostra a quantidade de cada bolsa; a D2 deste arquivo traz a distribuição completa.
- **estrategia-de-midia-pos, 4.3:** exceção de UTM das provas superada por D12.

---

## 10. Auditorias

| Auditoria | Item | Resultado |
|---|---|---|
| 11-midia-paga | metas e verba antes de subir | pendente externo |
| 11-midia-paga | volume e CPC só com fonte | atendido: [DADO NÃO FORNECIDO], nenhum número inventado |
| 11-midia-paga | sem marca de concorrente no anúncio | atendido |
| 11-midia-paga | nomenclatura, UTM, conversão | atendido no desenho; teste em 30/10 |
| conformidade | sem MEC, sem certificação | atendido |
| conformidade | preço com parcelas, total e matrícula | atendido (DT2 fixada) |
| conformidade | bolsa com distribuição completa | atendido (D2 fixada) |
| conformidade | urgência real | atendido |
| conformidade | destino entrega o que o anúncio diz | pendente externo (páginas das provas) |
| conformidade | sem travessão nem meia-risca | atendido (busca dos caracteres) |

---

## Lista 1. Fatos (com fonte)

- Provas online com o campus; turma mínima de 15; datas da planilha (decisões 11 e 12; seção 12.9).
- UTM `google` e `cpc`; chaves `pos_<código>` e `pos_provas20261127` (D11, D12).
- Google com 30% das provas nas fases 1 e 2 e 40% na fase 3; Google em P3 e P4 por turma e semana (gestor-de-midia-pos, 4.2 e 4.3; estrategia-de-midia-pos, 3.1 e 3.3).
- Performance Max e Display fora; YouTube só com PP13 (gestor-de-midia-pos, seção 3).
- Fatos das provas (R$ 100,00, 11 bolsas, distribuição, nota de corte, desempate) e títulos de área contados (criativos-de-anuncio-pos, 1.1 e 5.5).
- Dados das 11 turmas (catálogo, seção 2).
- Negativas cruzadas propostas e termo KT17 (estrategia-de-midia-pos, 4.4 e 4.5).

## Lista 2. Suposições

- [SUPOSIÇÃO] Todas as palavras-chave são sementes, sem volume.
- [SUPOSIÇÃO] Limites de caracteres e recursos (cabeçalho "Cursos", imagem) do Google, sem fonte nos arquivos.
- [SUPOSIÇÃO] Correspondência só de frase e exata no começo; Rede de Pesquisa sem parceiros.
- [SUPOSIÇÃO] Lance "Maximizar conversões" sem CPA desejado no começo.
- [SUPOSIÇÃO] Fixações de título e descrição.
- [SUPOSIÇÃO] "Prova de bolsa" como negativa nas campanhas de turma durante a campanha das provas.
- [SUPOSIÇÃO] Título "Matrícula de R$ 250,00" sozinho não esconde condição.
- [SUPOSIÇÃO] Negativa nova não conta como mudança de estrutura.

## Lista 3. Dados que faltam

- [CONFIRMAR] VN em reais, CPImax e CPLmax_h, aprovador (PP1, PP2).
- [DADO NÃO FORNECIDO] Volume de busca e CPC de toda palavra-chave (Planejador de Palavras-chave).
- [CONFIRMAR] Teste da tag e da conversão em 30/10; marcação automática ligada.
- [CONFIRMAR] U2 (acesso à prova online) e páginas das provas dizendo "online".
- [CONFIRMAR] Correção das páginas de Goiânia e dos links de Cardiologia; A-C2 (destinos); decisão sobre as páginas E2.
- [CONFIRMAR] URLs próprias para sitelinks (A-C8, A-C9); números que atendem ligação.
- [CONFIRMAR] Turma mínima de 15 em cada página; formato mês a mês; pré-requisito de 657; regra da promoção de 341; data de 68636 na planilha.
- [CONFIRMAR] Campanhas de busca já ativas da Pós (exportação A1 da 1.12).

## Fontes

Internas: as entradas do cabeçalho. Externas: nenhuma. Regras de plataforma sem fonte marcadas [SUPOSIÇÃO].

---

**Próximo agente sugerido:** qa-de-marketing.
