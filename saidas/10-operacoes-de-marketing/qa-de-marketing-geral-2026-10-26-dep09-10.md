# QA de marketing: departamentos 09 (analista-de-dados) e 10 (arquiteto-de-fluxos)

- Agente: qa-de-marketing (10 Operações de Marketing)
- Linha: geral
- Data: 26/10/2026
- Status: rascunho. Nada foi publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Arquivos revisados:
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (auditoria 09-analytics)
  - /home/user/marketing-ufape/saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md (auditoria 10-operacoes)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/catalogo-de-cursos.md ("Como usar", resumo e seções 1 a 9)
  - docs/visao-de-campanhas-2026-10-26.md (67 linhas, numeradas V1 a V67 como no analista: V1 é a linha 9 do arquivo, V67 a linha 75)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 8)
  - contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md
  - contexto/cursos/pos/68651-prova-de-bolsa-de-estudos-para-hematologia-veterinaria.md
  - templates/kit-de-lancamento-pos.md
  - conhecimento/INDICE.md
  - .claude/commands/campanha-de-vestibular.md (formato), .claude/skills/matriz-gut/SKILL.md e .claude/agents/relatorios.md (existência)
  - auditorias/09-analytics.md, auditorias/10-operacoes.md, auditorias/conformidade-educacional.md

## Vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| analista-de-dados-geral-2026-10-26.md | **CORRIGIR** | 1 soma errada (43, não 42); o insight "100% das turmas em até 60 dias estão ativas" e a lista "33 dias ou mais" usam a data da visão, não a do catálogo; a linha V67 tem um candidato no catálogo (item sem página) que não foi citado |
| arquiteto-de-fluxos-geral-2026-10-26.md | **CORRIGIR** | contradiz o plano do cmo sobre as bolsas (P10 já resolvido); repete frases ligadas ao MEC em campos de texto do JSON; os exemplos falham na própria conferência C11; tipos de campo não aceitam o marcador "[CONFIRMAR]"; justificativas da ficha 68651 com erro |

Nenhum dos dois tem dado pessoal, travessão, meia-risca ou promessa proibida. Nenhum número de leads, verba ou matrícula foi estimado em nenhum dos dois.

---

## 1. analista-de-dados-geral-2026-10-26.md

### 1.1 Recontagem por amostragem (visão de campanhas e catálogo)

Recontei à mão, linha por linha, 20 contagens. Resultado: 19 batem, 1 não bate.

| # | Contagem do analista (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 19 ativas, 22 pausadas, 26 sem campanha (seção 0, "Como contei") | Ativas: V16 a V20, V32 a V42, V44, V55, V67 = 19. Pausadas: V11, V15, V23 a V26, V29 a V31, V43, V45 a V48, V52 a V54, V59, V60, V63 a V65 = 22. Sem = 26 | Sim |
| 2 | Faixa "já iniciada": 32 linhas, 6 ativas, 9 pausadas, 17 sem (P1) | V1 a V32 = 32; ativas V16 a V20 e V32 = 6; pausadas V11, V15, V23, V24, V25, V26, V29, V30, V31 = 9; sem = 17 | Sim |
| 3 | Faixas 0 a 30 (4 ativas) e 31 a 60 (6 ativas) (P1) | V33 a V36 = 4 ativas; V37 a V42 = 6 ativas | Sim |
| 4 | Faixa 61 a 180: 14 linhas, 2 ativas, 8 pausadas, 4 sem (P1) | V43 a V56 = 14; ativas V44, V55; pausadas V43, V45 a V48, V52 a V54; sem V49 a V51, V56 | Sim |
| 5 | Faixa acima de 180: 11 linhas, 1 ativa, 5 pausadas, 5 sem (P1) | V57 a V67 = 11; ativa V67; pausadas V59, V60, V63, V64, V65; sem V57, V58, V61, V62, V66 | Sim |
| 6 | 35 não iniciadas: 13 ativas, 13 pausadas, 9 sem (P1) | V33 a V67 = 35; 13, 13 e 9 conferidos | Sim |
| 7 | Só estático: 13 ativas e 17 pausadas, 30 de 41 (73,2%) (P4) | Ativas só estático: V16 a V19, V33, V34, V36, V39 a V42, V44, V67 = 13; pausadas: 17; 30 / 41 = 73,17% | Sim |
| 8 | Sem 5 ângulos: 10 ativas e 16 pausadas, 26 (63,4%) (P4) | Ativas sem 5: V16 a V20, V33, V36, V40, V55, V67 = 10; pausadas com 5: V24, V29, V30, V45, V53, V54 = 6, logo 16 sem | Sim |
| 9 | Sem 5 ângulos ou só estático: 15 e 19, total 34 (82,9%) (P4) | 10 + 5 ativas (V34, V39, V41, V42, V44); 16 + 3 pausadas (V24, V45, V54) | Sim |
| 10 | Com 5 ângulos e vídeo: 4 ativas e 3 pausadas (P4) | Ativas V32, V35, V37, V38; pausadas V29, V30, V53 | Sim |
| 11 | Por linha: Pós 42 (14, 18, 10), Livres 21 (3, 4, 14), Eventos 4 (2, 0, 2) (P5) | Pós: 42 linhas com "Pós" no nome; ativas 14; pausadas 18; sem 10 (V8, V10, V49, V50, V51, V56, V57, V58, V61, V62). Eventos: V28, V36, V66, V67. Livres: 21 | Sim |
| 12 | Medianas dos tickets: 35.400,00; 34.575,00; 33.000,00 (P2) | Preços conferidos um a um na seção 2 do catálogo (27 turmas); ordenação e medianas iguais | Sim |
| 13 | 5 maiores tickets futuros: 657, 352, 707, 341, 68628 (P2) | 48.400,00; 47.880,00; 47.700,00; 43.500,00; 38.940,00 (catálogo). Próximos: 578 e 662 com 37.500,00 | Sim |
| 14 | Tickets das 6 ativas iniciadas (P3) | 650 30.000,00; 68662 35.400,00; 706 14.960,00; 586 14.130,00; 554 27.000,00; 68612 32.520,00 (catálogo) | Sim |
| 15 | 10 datas diferentes entre visão e catálogo (6.4) | Conferidas as 67 linhas: 599, 717, 718, 716, 433, 625, 68668, 573, 68614, 68618. Nenhuma outra diverge | Sim |
| 16 | Recorte: Pós 52, Livres 55, Eventos 3 = 110; constam 34, não constam 76 (P5) | Catálogo: 30 Pós abertas e 22 provas abertas; Livres abertos 2 + 36 + 7 + 10 = 55; plano 2.2. Não constam: 25 + 46 + 5 = 76 (plano, seção 3) | Sim |
| 17 | Tabela por área: totais 13, 13, 8, 76 (P5) | Linha a linha contra o plano, seção 2.3: todas as linhas e colunas somam certo | Sim |
| 18 | Dias até o início por amostra (30/10 = 4; 28/11 = 33; 13/03/2027 = 138) | Conferidos | Sim |
| 19 | Grupos 68665 (6 dias) e 68666 (30 dias), R$ 100,00 (P3) | Catálogo, seção 7 | Sim |
| 20 | "A1, A7, A10, A13 e A14 (42 itens somados: 14 + 10 + 4 + 6 + 9)" (P5, insight) | 14 + 10 + 4 + 6 + 9 = **43** | **Não** |

Nenhum número de leads, verba, gasto ou matrícula foi estimado: todos aparecem como [CONFIRMAR] (seção 0, item 1; seção 3, coluna "Quanto"; seção 5, metas). O ticket é o preço de lista do catálogo, declarado como tal.

### 1.2 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| A1 | Seção 1, pergunta 5, parágrafo "Insight" (linha 191) | Soma errada: "42 itens somados: 14 + 10 + 4 + 6 + 9". A soma é 43 | Trocar "42" por "43" |
| A2 | Seção 1, pergunta 1, "Insight" (linha 58) e "Fatos", 4º item (linha 499) | "100% das turmas em até 60 dias estão ativas" vale só pela data da visão. O catálogo é a fonte única dos dados de curso: por ele, 68618 começa em 18/12/2026 (53 dias) e está **pausada**, e 573 começa em 14/11/2026 (19 dias, faixa de 0 a 30). Pelo catálogo, são 10 ativas de 11 linhas em até 60 dias | Escrever "pela data da visão" na tabela da pergunta 1, no insight e no fato, e acrescentar uma linha ou nota: "pelo catálogo, 68618 (53 dias) entra na faixa de 31 a 60 dias pausada; 10 de 11 ativas (P6 do plano)" |
| A3 | Seção 1, pergunta 4, "Ação" (linha 142) e seção 3, ação 3 (linha 211) | A lista "33 dias ou mais: 68610, 573, 68614 e 623" inclui 573, que tem 19 dias pelo catálogo (14/11/2026); os 34 dias são da visão | Tirar 573 da lista, ou escrever "573 (34 dias pela visão, 19 pelo catálogo) [CONFIRMAR data, P6]" |
| A4 | Seção 6.3, linha V67 (linha 457), e tabelas de cobertura da pergunta 5 (linhas 166 e 177) | O catálogo (seção 9) tem uma linha com o **mesmo nome** de V67: "Paciente Grave Multidiciplinar Foco em casos Clinicos", ONLINE, status "sem página", "só na planilha". O analista cita só o 700 como candidato. Se V67 for essa linha, há campanha **ativa** levando a um item sem página (item "página de destino" da conformidade), e a contagem muda: Eventos no recorte com 1 ativa, A3 com 0 ativa, recorte com 12 ativas e 33 itens na visão | Acrescentar em 6.3 o segundo candidato (linha sem código da seção 9, nome idêntico, sem página) e a consequência acima nas ressalvas da pergunta 5; incluir em "Dados que faltam": "[CONFIRMAR] para onde leva a campanha ativa da linha V67" |

Recomendações (não bloqueiam):
- R1. Pergunta 2, tabela das 5 maiores (linha 83): 341 tem promoção de 20% no catálogo, com texto cortado (P16 do plano). Anotar ao lado do ticket "promoção de 20% [CONFIRMAR regra, P16]".
- R2. Seção 7: os itens não marcados da auditoria 09 deveriam dizer "não se aplica nesta rodada" com o motivo, em vez de ficarem só sem marcação.

### 1.3 Auditoria 09-analytics, item por item

| Item | Resultado | Observação |
|---|---|---|
| Árvore de métricas existe e está atualizada | Passa | Seção 5, por linha, só estrutura, datada de 26/10/2026 |
| Toda métrica tem uma fonte nomeada | Passa | Meta Ads, Google Ads, CRM, GA4, Chatwoot, loja e planilha nomeados em cada ramo |
| Relatórios comparam com as metas | Não se aplica nesta rodada | Não há metas (P11); todas [CONFIRMAR] |
| Metas não batidas com a mesma clareza | Não se aplica nesta rodada | Sem metas |
| Insights terminam com uma ação | Passa | As 5 perguntas e os 3 insights têm ação; a ação da pergunta 4 tem o erro A3 |
| Lacunas de dados sinalizadas | Passa | Seções 0 e 4 e "Dados que faltam"; falta a lacuna de V67 (A4) |
| Backlog revisado todo mês | Não se aplica | Fica com o backlog-de-otimizacao (etapa 1.33) |
| Custo por lead, custo por matrícula, conversão e receita separados por linha | Não se aplica nesta rodada | Sem números; a estrutura está separada por linha (5.1 a 5.4) e nada foi estimado |
| Nenhum dado pessoal nos relatórios | Passa | Nenhum nome, telefone, CPF ou e-mail; o pedido de dados exige só contagens e somas |

### 1.4 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Dados do curso: nome, modalidade, CH, duração e turno batem com o catálogo | Passa (preços e datas conferidos; 586 aparece como EAD, correto) |
| Status "aberto" ou peça sem chamada para inscrição | Passa (análise interna, sem chamada) |
| Modalidade clara e correta | Passa |
| Graduação: ato do catálogo | Não se aplica (Graduação fora da visão) |
| Pós lato sensu sem "reconhecida pelo MEC" | Passa (nenhuma menção ao MEC no arquivo) |
| Curso livre: não confere diploma | Não se aplica (não é peça) |
| Nota MEC com fonte | Passa (nenhuma nota) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa ("maior ticket" é medida do catálogo) |
| Comparação com concorrente | Não se aplica |
| Preço com valor, parcelas e condições | Passa com ressalva: ticket declarado sem matrícula (seção 0, item 3); ver R1 sobre a promoção da 341 |
| Bolsa e desconto com regra | Não se aplica |
| Urgência real | Passa (nenhuma urgência; pede vagas restantes antes de "últimas vagas") |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Não se aplica |
| Menores | Não se aplica |
| Formulários com finalidade e política | Não se aplica |
| WhatsApp e e-mail com consentimento | Não se aplica |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Não se aplica (não é anúncio) |
| Página de destino entrega o que o anúncio promete | Ressalva: ver A4 (possível campanha ativa sem página) |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica (não é anúncio) |

### 1.5 Checagens pedidas

- Travessão ou meia-risca: nenhuma ocorrência na leitura integral.
- Dado pessoal: nenhum.
- Frase ligada ao MEC fora de regra proibitiva: nenhuma. A única menção a certificação (linha 285, "páginas com a frase de certificação") não cita o MEC e é pedido de conferência.

**Veredito: CORRIGIR** (A1 a A4). Volta para o analista-de-dados.

---

## 2. arquiteto-de-fluxos-geral-2026-10-26.md

### 2.1 Conferências pedidas

**Campo de nome de pessoa no esquema:** não há. equipe e evento.palestrantes guardam só contagens; aprovacoes guarda o papel (decidido_por_papel); historico.aplicado_por, kit.entregas.responsavel e arquivos_por_camada.agente guardam nomes de agentes, não de pessoas. Nenhum nome de docente, coordenador ou palestrante aparece no arquivo (conferido contra os 22 nomes da ficha da 707). Passa.

**Origem e regra de vazio por campo:** todas as linhas das tabelas de 1.3 têm as colunas "Origem" e "Se vazio" preenchidas. Há dois defeitos de coerência (B5): a coluna "Tipo" de vários campos não aceita o texto "[CONFIRMAR]" que a coluna "Se vazio" manda escrever, e a regra R1 conflita com os valores próprios de vazio de outros campos.

**Exemplo pos-707 contra catálogo e ficha:**

| Campo | JSON | Catálogo ou ficha | Bate? |
|---|---|---|---|
| catalogo_linha_literal | linha 707 até "planilha e site" | catálogo, seção 2, linha 68 | Sim |
| nome_no_site, nome_padrao, slug | Pós-graduação em Oftalmologia Veterinária; pos-graduacao-em-oftalmologia-veterinaria | catálogo; regra da Pós | Sim |
| local, modalidade, turma, CH | São Paulo; Semipresencial; VII; 600 h | catálogo | Sim |
| inicio, fonte_da_data, dias | 2026-10-30; planilha; 4 | catálogo e ficha ("Início na planilha: 30.10.2026") | Sim |
| preco_texto_site e preco_estruturado | 30x de R$ 1.590,00; R$ 47.700,00; matrícula R$ 250,00 | catálogo (30 x 1.590 = 47.700) | Sim |
| status | aberto | catálogo | Sim |
| modulos, turma_minima, pagina_oficial | 24; 20; URL do produto 707 | ficha (marcados em campos_so_na_ficha) | Sim |
| equipe | 3 coordenadores, 19 docentes | ficha ("Coordenação" com 3; "Professores listados: 19") | Sim |
| status_midia | ativa, estático, sem 5 ângulos, 2026-10-30 | visão, V33 | Sim |
| gut, área, onda | 4, 5, 3 = 60; A9; onda 1 | plano, seções 2.3 e 3 | Sim |
| kit.entregas | 9 entregas com 1, 1, 1, 6, 3, por docente, 4, 2, 1 | templates/kit-de-lancamento-pos.md | Sim (post por docente segue o plano, P13: "1 por docente autorizado") |
| resumo | 8 pendências, bloqueado | 707-p01 a p08; p01 bloqueia peca_final | Sim |

**Exemplo pos-68651 contra catálogo e ficha:**

| Campo | JSON | Catálogo ou ficha | Bate? |
|---|---|---|---|
| catalogo_linha_literal | "| 68651 | Prova de Bolsa ... | São Paulo | 27/11/2026 | aberto |" | catálogo, seção 3, linha 120 | Sim |
| inicio, dias | 2026-11-27; 32 | catálogo | Sim |
| fonte_da_data | planilha | a seção 3 do catálogo não tem coluna "Fonte"; o dado vem da ficha | Parcial (B6) |
| preco_texto_site | R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão. | ficha | Sim |
| modalidade | "Presencial" | ficha: "PROVA PRESENCIAL" | Não literal (B6) |
| horario_texto | 9 às 13h | ficha | Sim |
| nota_de_corte_texto | "7.0 (mínimo 70% de acerto)" | ficha: "7.0 (mínimo 70 % de acerto)" | Não literal (B6) |
| carga_horaria null | 500 h da Pós | ficha e catálogo 68608 (500 h) | Sim, como [SUPOSIÇÃO] declarada |
| bolsas_previstas | "[CONFIRMAR]" | ficha: 2 bolsas de 50% (monitoria), 4 de 25%, 5 de 10%; plano P10: "resolvido em 26/10/2026" | **Não** (B1) |
| minimo_para_confirmar_turma | "[CONFIRMAR]", justificado como contradição da ficha | ficha: 15 nas duas menções (não há contradição interna) | Justificativa errada (B2) |
| prazo de matrícula e resultado | "[CONFIRMAR]" | ficha: 10 dias úteis, 10 dias e 7 dias; resultado por e-mail, por telefone (WhatsApp e/ou e-mail) e no site | Sim (divergência real) |
| turma_de_destino | sugestão 68608 [SUPOSIÇÃO] | catálogo: 68608 começa em 28/11/2026 | Sim |
| gut, área | 5, 5, 4 = 100; A11 | plano, seções 2.3 e 3 | Sim |

**Nada vai para o banco agora:** está claro e repetido no resumo (item 5), na abertura da seção 4 ("Este documento não cria tabela, função, migration, rota nem chamada de IA"), no documento de fluxo (Ferramentas) e nos Fatos (item 1). A importação é tratada como pergunta ao ufape-admin, sem criar nada. Passa.

### 2.2 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| B1 | Seção 1.3, linha prova_de_bolsa.bolsas_previstas (linha 161); seção 1.7, primeiro marcador (linha 481); JSON 68651, bolsas_previstas (linha 547); pendência 68651-p02 (linha 597); Suposição 3 (linha 1105); Dados que faltam 5 (linha 1123) | Contradiz o plano aprovado. O arquivo diz que regras e percentuais ficam vazios "(plano, P10)", mas o plano, P10, diz "resolvido em 26/10/2026 pelas páginas das provas (2 bolsas de 50%, 4 de 25%, 5 de 10%, nota de corte 7,0)". Só a turma de destino segue vazia | Mudar o tipo de bolsas_previstas para lista de objetos (quantidade, percentual_texto) copiada da ficha, com o caminho em campos_so_na_ficha; refazer 68651-p02 para tratar só da turma de destino e das provas sem turma futura; tirar a Suposição 3 e ajustar o item 5 de "Dados que faltam". Conferir os percentuais também em contexto/pos-graduacao.md, que o plano cita |
| B2 | Seção 1.7, primeiro marcador (linha 481) e Fatos, item 7 (linha 1089) | Dois erros de leitura da ficha 68651: (a) o mínimo para confirmar a turma é 15 nas duas menções, então não há contradição interna; a divergência é com a turma mínima de 20 da Pós; (b) o resultado é divulgado por três vias (e-mail; telefone, WhatsApp e/ou e-mail; site), e o fato cita só e-mail e site | (a) Reescrever: "o mínimo da ficha (15) diverge da turma mínima da Pós (20)"; pela R6, copiar 15 e abrir pendência do tipo divergencia, ou declarar por que fica "[CONFIRMAR]". (b) Corrigir o fato 7 com as três vias |
| B3 | JSON 707, pendência 707-p02 (linha 457); JSON 68651, pendência 68651-p05 (linha 600); seção 1.7, terceiro marcador (linha 483) | Frases ligadas ao MEC fora de regra proibitiva, dentro de campos de texto do JSON que o HTML mostra ao cliente: "bloco CERTIFICAÇÃO DO MEC" e "reconhecido pelo Ministério da Educação". Não afirmam certificação, mas repetem a frase que o briefing manda não escrever, e a própria C10 diz "em nenhum campo de texto" | Reescrever as duas pendências sem repetir a frase, por exemplo: "A página oficial traz afirmação de certificação não aprovada pela regulação (auditoria de 26/10, seção 9; P2). Não repetir; anúncio que leve à página é sinalizado." Na linha 483, dizer "uma afirmação de certificação não aprovada". Ampliar C10 e 4.3, item 5, para as variantes ("do MEC", "pelo MEC", "Ministério da Educação"), com a única exceção do ato regulatório da Graduação copiado do catálogo |
| B4 | Seção 3.9, conferência C11 (linha 984), contra os exemplos 1.6 e 1.7 | Os próprios exemplos falham na C11 ("todo [CONFIRMAR] ou [SUPOSIÇÃO] tem pendência"). No 707 há "[CONFIRMAR]" sem pendência em vagas.vagas_ofertadas, nos prazos de 8 entregas e em arquivos_por_camada.geral.ref_aprovacao. No 68651, em slug_sugerido, fim_das_inscricoes, vagas.turma_minima e quantidade_minima de 3 entregas | Ou acrescentar as pendências nos exemplos, ou reescrever a C11 dizendo quais campos exigem pendência (por exemplo, só classes C, N e P) e que prazos e refs de aprovação ficam fora |
| B5 | Seção 1.1, R1 (linha 43), e seção 1.3, coluna "Tipo" | (a) A coluna "Tipo" não aceita o texto que a coluna "Se vazio" manda escrever: modulos ("inteiro ou null"), gut ("objeto ou null"), equipe.* (inteiro), prova_de_bolsa.data_da_prova, graduacao.inscricoes_abertas_desde, graduacao.inicio_das_aulas e evento.data_inicio ("data"), kit.entregas.quantidade_minima (inteiro). Pela 4.3, a plataforma recusaria esses arquivos. (b) A R1 diz que todo vazio é "[CONFIRMAR]", mas vários campos têm vazio próprio (sem_area, sem-codigo, nao_consta, ausente, 0, lista vazia). (c) C1 (linha 974) pede "contagem igual à do catálogo mais a Graduação", mas os 184 do catálogo já incluem os 2 da Graduação | (a) Acrescentar "ou marcador [CONFIRMAR]" ao tipo desses campos. (b) Acrescentar à R1: "salvo quando a coluna Se vazio define outro valor". (c) Trocar por "contagem igual ao total do catálogo (184, Graduação incluída)" |
| B6 | JSON 68651 (linhas 499 a 551) | Cópias que a R4 exige literais e não são: nota_de_corte_texto ("70%" no lugar de "70 %"); modalidade "Presencial" (a ficha diz "PROVA PRESENCIAL"); fonte_da_data "planilha" tem como origem a "coluna Fonte do catálogo", que não existe na seção 3 (o dado vem da ficha) | Copiar "7.0 (mínimo 70 % de acerto)"; copiar a modalidade como na ficha ou definir que, na prova, a modalidade vem de prova_de_bolsa.formato; incluir "fonte_da_data" em campos_so_na_ficha ou ajustar a origem do campo para "catálogo ou ficha" |

Recomendações (não bloqueiam):
- R3. Seção 1.3, area.codigo (linha 116): a Graduação aparece em "sem_area" e em "nao_se_aplica". Deixar só "nao_se_aplica" para a Graduação.
- R4. Seção 1.4, nomes das áreas (linha 236): A11 aparece como "Laboratório", mas o exemplo 68651 usa o nome completo da seção 2.3 do plano. Usar sempre o nome do plano.
- R5. Seção 2.2 (linhas 765 e 769): "eventos-workshop-neuromonitorizacao-2026-11-20.json" não segue a própria regra do slug (que daria "workshop-brasileiro-de-neuromonitorizacao-veterinaria-anestesia"). Declarar a exceção junto com a decisão pendente (Dados que faltam 10).
- R6. Kit de Pós: o template diz "1 por docente da ficha"; o exemplo usa "1 por docente autorizado", como decidiu o plano (P13). Deixar a referência ao P13 escrita na linha de 1.4, para não parecer que o mínimo diminuiu.

### 2.3 Auditoria 10-operacoes, item por item

| Item | Resultado | Observação |
|---|---|---|
| conhecimento/INDICE.md está atualizado | Pendente, não bloqueia esta saída | O índice não tem a pasta cursos/ nem o fluxo; o briefing proíbe editar arquivo alheio nesta rodada e o arquivo propõe o registro (2.4). Registrar depois da aprovação |
| Workflow cita só agentes, skills e auditorias que existem | Passa | relatorios, cmo, qa-de-marketing, skill matriz-gut e as 3 auditorias existem |
| Workflow termina com auditoria e critério de pronto conferível | Passa | Os dois textos de 3.9 terminam com auditoria e "Concluído quando" |
| Aprovação humana antes de publicar | Passa | "Pare depois de cada etapa"; mudança de recorte, GUT e pausa viram pedido |
| Acesso às ferramentas é o mínimo necessário | Passa | Só arquivos; nenhuma ferramenta externa no fluxo |
| Nenhuma chave em arquivo de texto | Passa | |
| Documentos têm data de revisão | Passa | 02/11/2026, marcada [SUPOSIÇÃO] |
| Toda peça pública passou por qa e conformidade | Não se aplica | Desenho interno; este arquivo é o QA |
| Dados de curso batem com o catálogo | Corrigir | 707 bate em tudo; 68651 tem B1 e B6 |

### 2.4 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Dados do curso batem com o catálogo | Passa com ressalva (B1 e B6 na prova 68651; Graduação e workshop batem com o catálogo nos campos conferidos) |
| Status "aberto" ou sem chamada | Passa (R14: só aberto entra em "planejar") |
| Modalidade clara e correta | Passa (tabela de equivalência em 1.4) |
| Graduação: ato do catálogo | Passa ("Portaria SERES/MEC nº 162, de 13/03/2025 (D.O.U. 21/03/2025), conforme o Edital 002/2026", igual ao catálogo) |
| Pós lato sensu sem "reconhecida pelo MEC" | Passa no mérito (nada afirma certificação); ajuste de redação em B3 |
| Curso livre: não confere diploma | Não se aplica (o esquema não tem campo de certificação) |
| Nota MEC com fonte | Passa (nenhuma nota) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa (o superlativo da página 68651 não é copiado) |
| Comparação com concorrente | Não se aplica |
| Preço com valor, parcelas e condições | Passa (cópia literal, matrícula incluída) |
| Bolsa e desconto com regra | Passa (cupom com validade [CONFIRMAR]; bolsas, ver B1) |
| Urgência real | Passa (vagas_restantes sempre [CONFIRMAR]; R9 proíbe "últimas vagas") |
| Prouni, Fies | Passa (nenhuma menção) |
| Autorização de imagem e voz | Passa (só contagens; [CONFIRMAR autorização]) |
| Menores | Passa (sem campo de pessoa; risco 8 da seção 5) |
| Formulários | Não se aplica |
| WhatsApp e e-mail com consentimento | Passa ("só com opt-in" nos canais) |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Não se aplica |
| Página de destino | Passa (pendências 707-p02 e 68651-p05 sinalizam anúncio que leva a página com frase de certificação) |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica (não é anúncio) |

### 2.5 Checagens pedidas

- Travessão ou meia-risca: nenhuma ocorrência na leitura integral. O "->" da descrição dos workflows segue o formato dos workflows existentes (campanha-de-vestibular.md).
- Dado pessoal: nenhum. Os tratamentos (Dr., Dra., Prof.) aparecem só no texto da regra C9.
- Frase ligada ao MEC fora de regra proibitiva: 2 ocorrências em campos de JSON (707-p02 e 68651-p05) e 1 no texto explicativo de 1.7 (B3). As demais menções (R9, C10, 4.3, A7 e o ato da Graduação) estão em regra proibitiva, em pedido de correção ou são o ato regulatório do catálogo.

**Veredito: CORRIGIR** (B1 a B6). Volta para o arquiteto-de-fluxos.

---

## Fatos (com fonte)

- A visão tem 67 linhas: 19 ativas, 22 pausadas e 26 sem campanha (docs/visao-de-campanhas-2026-10-26.md, recontagem linha a linha).
- 68618 começa em 18/12/2026 no catálogo e 22/05/2027 na visão, com campanha pausada; 573 começa em 14/11/2026 no catálogo e 29/11/2026 na visão (catálogo, seção 4; visão, V41 e V63).
- O catálogo tem a linha "Paciente Grave Multidiciplinar Foco em casos Clinicos", ONLINE, "sem página", "só na planilha" (catálogo, seção 9).
- A1 + A7 + A10 + A13 + A14 = 14 + 10 + 4 + 6 + 9 = 43 itens (plano do cmo, seção 2.3).
- O plano dá P10 como resolvido em 26/10/2026, com 2 bolsas de 50%, 4 de 25% e 5 de 10% e nota de corte 7,0 (saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 7).
- A ficha 68651 traz o mínimo de 15 alunos nas duas menções, prazos de matrícula de 10 dias úteis, 10 dias e 7 dias, e resultado por e-mail, por telefone (WhatsApp e/ou e-mail) e no site (ficha 68651).
- Os dados da 707 no exemplo batem com o catálogo e a ficha (catálogo, seção 2; ficha 707).
- O ato da Medicina Veterinária no exemplo é igual ao do catálogo (catálogo, seção 1).

## Suposições

- [SUPOSIÇÃO] A numeração V1 a V67 do analista começa na linha 9 do arquivo da visão; a recontagem usou a mesma numeração.
- [SUPOSIÇÃO] As frases das pendências 707-p02 e 68651-p05 aparecem no mapa HTML apresentado ao cliente, porque o HTML desenha o nó "Pendências" (arquiteto, seção 3.7).
- [SUPOSIÇÃO] Os percentuais de bolsa citados pelo plano em P10 estão também em contexto/pos-graduacao.md (arquivo não lido nesta revisão).

## Dados que faltam

- [CONFIRMAR] Para onde leva a campanha ativa da linha V67 da visão: produto 700 ou a linha "Paciente Grave" sem página.
- [CONFIRMAR] Data única de 573, 68614 e 68618 (P6 do plano).
- [CONFIRMAR] Percentuais de bolsa em contexto/pos-graduacao.md, para o arquiteto copiar em bolsas_previstas.
- [CONFIRMAR] Dados do workshop no exemplo do arquiteto (5 palestrantes, horário e endereço) e os campos da Graduação vindos da ficha de editais: não conferidos contra as fichas nesta revisão, porque o pedido limitou a conferência aos exemplos 707 e 68651.
- [CONFIRMAR] Quem aprova cada tipo de peça (contexto/ufape-geral.md, tabela vazia; P12). Até lá, a aprovação vai à pessoa do marketing que fez o pedido.
