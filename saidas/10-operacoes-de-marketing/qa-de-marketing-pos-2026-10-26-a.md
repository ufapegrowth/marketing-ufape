# QA de marketing da Pós-graduação: estratégia de oferta, estratégia de marketing e estratégia de conteúdo

- Agente: qa-de-marketing (departamento 10, Operações de Marketing)
- Linha: pos
- Data: 26/10/2026 (segunda-feira)
- Status: rascunho de revisão. Não edita os arquivos revisados. Nada é publicado, enviado ou pago.
- Entradas lidas:
  - docs/execucao-2026-10-26.md (briefing obrigatório)
  - /home/user/marketing-ufape/CLAUDE.md
  - contexto/ufape-geral.md (voz da marca e regras de aprovação)
  - contexto/pos-graduacao.md (regras da prova de bolsa)
  - contexto/catalogo-de-cursos.md (cabeçalho, seção 2 e seção 3)
  - auditorias/02-estrategia-e-posicionamento.md, auditorias/04-qualidade-de-conteudo.md, auditorias/conformidade-educacional.md
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 1 a 8)
  - templates/kit-de-lancamento-pos.md
  - contexto/cursos/pos/68646-prova-de-bolsa-de-estudos-para-dermatologia-veterinaria.md e contexto/cursos/pos/68652-prova-de-bolsa-de-estudos-para-medicina-de-felinos.md (para conferir as regras da prova)
  - Arquivos revisados, lidos inteiros:
    - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md (516 linhas)
    - saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-pos-2026-10-26.md (477 linhas)
    - saidas/04-conteudo/estrategia-de-conteudo-pos-2026-10-26.md (490 linhas)
- Não abri faculdade.ufape.com.br. Nenhum dado pessoal neste arquivo.

## Resumo dos vereditos

| Arquivo | Auditoria do departamento | Conformidade educacional | Veredito |
|---|---|---|---|
| estrategia-de-oferta-pos-2026-10-26.md | 02: 1 item com falha (preços e condições) | 1 item com falha (dados do curso), 1 com ressalva de marcação | **CORRIGIR** |
| estrategia-de-marketing-pos-2026-10-26.md | 02: 2 itens com ressalva (canais, capacidade) | 1 item com falha (bolsa com regra e destino), 1 com fonte errada | **CORRIGIR** |
| estrategia-de-conteudo-pos-2026-10-26.md | 04: 4 itens com ressalva ou falha | 4 itens com falha | **CORRIGIR** |

Nenhum dos três arquivos tem promessa de emprego, salário, aprovação ou título, frase de certificação, nota do MEC, "últimas vagas", dado pessoal, docente nomeado, travessão ou meia-risca (leitura linha a linha). Os bloqueios vêm de: um dado de preço que não bate com o catálogo, dado tirado só da ficha sem [CONFIRMAR NO CATÁLOGO], provas sem turma de destino dentro da campanha, e inconsistências de calendário, canais e capacidade entre os três arquivos.

Encaminhamento: os três arquivos **voltam para os agentes que os produziram** (estrategia-de-oferta, estrategia-de-marketing e estrategia-de-conteudo), com as listas abaixo. Depois da correção, voltam ao qa-de-marketing antes da aprovação humana.

---

## 1. saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md

### 1.1 Conferência dos dados de curso com o catálogo

| Dado | Resultado |
|---|---|
| 30 turmas abertas (24 em 30x, 3 em 24x, 2 em 18x, 1 em 26x) | confere com o catálogo, seção 2 |
| Código, curso, praça, início, parcelas, total e matrícula das 30 turmas (seção 1.2) | conferidos um a um: todos batem (inclusive 68629 com matrícula de R$ 350,00, 698 com 370 h, 707 com 600 h, 68635 e 68623 com 750 h, 657, 359, 352, 60, 719 e 68629 com 360 h) |
| Nota de centavos (657, 68609, 68629, 359, 719, 698) | contas conferidas; corretas |
| 22 provas abertas, 19 em SP e 3 em Goiânia (68640, 68642, 68644), R$ 100,00 | confere com o catálogo, seção 3; 68656 encerrado |
| Contagem de destino das provas: 10 compatíveis, 8 incertas, 4 sem turma | conferida com o status das turmas no catálogo: correta |
| 586 EAD (18x de R$ 785,00, R$ 14.130,00, matrícula de R$ 350,00, "verificar") | confere |
| Faixa de total na seção 0 | **não confere** (ver problema O1) |
| Regras da prova (11 bolsas: 2 de 50% monitoria, 4 de 25%, 5 de 10%; nota 7,0; 2 dias úteis; 10 dias úteis; não acumulativa e intransferível; desempate por currículo; mínimo 15 x 20 [CONFIRMAR]; destino [CONFIRMAR]) | iguais às de contexto/pos-graduacao.md |
| Horário 9h às 13h, sem celular e relógio, documento com foto | só na ficha 68646, não está no catálogo nem no contexto da linha |
| Propostas PR1 a PR10 | todas marcadas como PROPOSTA, com regra, validade, custo por fórmula e como desfazer; nenhuma apresentada como oferta existente |

### 1.2 auditorias/02-estrategia-e-posicionamento.md, item por item

| Item | Resultado do QA | Observação |
|---|---|---|
| O plano tem uma única meta principal | Atendido (herdado) | Herda a meta do cmo: turmas confirmadas com a turma mínima; valor [CONFIRMAR] |
| Persona e curso ou oferta estão nomeados | Atendido | P1 a P4 marcadas [SUPOSIÇÃO]; 30 turmas e 22 provas por código |
| Os 8 canais foram avaliados | Não se aplica (herdado) | A oferta não escolhe canal |
| O posicionamento nomeia a alternativa real | Atendido (herdado) | Responde a curso curto (PR5) e adiar (prova) |
| Todo pilar tem prova | Atendido | Cada componente aponta catálogo ou ficha |
| As regras de voz da marca têm exemplos | Atendido em parte | Texto-padrão com dois exemplos; voz segue [SUPOSIÇÃO] |
| O plano cabe no tempo e na verba | Não se aplica | Custos das propostas só por fórmula |
| Nenhuma oferta, pilar ou resposta promete emprego, aprovação ou salário | Atendido | Seções 2.2, 4 e 7 listam o que não dizer |
| Preços, bolsas e condições vêm do catálogo ou estão marcados | **Falha** | Faixa de total errada na seção 0 (O1); texto-padrão de preço e da prova usa dados só da ficha sem [CONFIRMAR NO CATÁLOGO] (O2, O3); a seção 9.1 afirma que as regras de ficha estão marcadas, o que só vale para parte delas |

### 1.3 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado do QA |
|---|---|---|
| Dados do curso | Nome, modalidade, carga horária, duração e turno batem com o catálogo | **Falha**: seção 0, linha "Maiores obstáculos", diz total de R$ 28.050,00 a R$ 48.400,00 "nas turmas abertas de pequenos animais"; o catálogo tem 68629 (R$ 16.456,00) e 698 (R$ 26.970,00), que são de pequenos animais. Todo o resto bate |
| Dados do curso | Status "aberto" (ou sem chamada para inscrição) | Atendido: só turmas abertas recebem oferta; 698 condicionada à correção do site |
| Dados do curso | Modalidade clara e correta | Atendido: 68632 presencial; nenhuma oferta EAD |
| Regulação | Graduação: ato do catálogo | Não se aplica |
| Regulação | Pós sem "reconhecida pelo MEC" | Atendido |
| Regulação | Curso livre: não confere diploma | Atendido com nota: PR5 (combo) cita livres; se aprovada, toda peça do combo diz que o livre não confere diploma nem equivale à pós |
| Regulação | Nota MEC com fonte | Atendido: nenhuma |
| Promessas | Sem emprego, salário, promoção, aprovação | Atendido |
| Promessas | Empregabilidade com fonte | Não se aplica |
| Promessas | Superlativos com fonte | Atendido: "menor total" e "maior parcela" são contagens internas e não vão para peça como argumento |
| Promessas | Comparação com concorrente | Atendido: Anclivepa, Qualittas e Equalis só em "o que não dizer" |
| Preço (CDC) | Valor, parcelas, condições, matrícula | Atendido com ressalva: o texto-padrão (2.1) é completo, mas leva frases só de ficha sem marcação (O2) |
| Preço (CDC) | Bolsa e desconto com regra, público e validade | Atendido com ressalva: descontos de 341, 359, 352 e aluno e ex-aluno bloqueados; provas sem destino fora da campanha. Falta marcar o horário e as regras no texto-padrão da prova (O3) |
| Preço (CDC) | Urgência real | Atendido: "10 primeiros" fora das peças (PR8) |
| Preço (CDC) | Prouni, Fies, financiamento | Não se aplica |
| Pessoas e dados | Autorização de imagem e voz | Atendido: nenhum docente nomeado |
| Pessoas e dados | Menores | Não se aplica |
| Pessoas e dados | Formulários com finalidade e política | Não se aplica |
| Pessoas e dados | WhatsApp e e-mail com consentimento | Atendido (PR2 com opt-in) |
| Pessoas e dados | Nenhum dado pessoal | Atendido |
| Plataformas | Sem segmentação discriminatória | Não se aplica (sem anúncio) |
| Plataformas | Destino entrega o que o anúncio promete | Ressalva herdada: P2, P3 e P4 do cmo; bloqueio já registrado |
| Anúncios | Sem característica pessoal de quem vê | Atendido |
| Anúncios | Sem escassez falsa | Atendido |
| Anúncios | Sem pessoa pública ou parceria inexistente | Atendido ("parceria de hotel" em "o que não dizer") |
| Anúncios | Sem caixa alta ou pontuação repetida | Não se aplica |
| Anúncios | Destino com dados da Ufape e política | Ressalva herdada (P2) |
| Anúncios | Sem drible da análise | Atendido |

### 1.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| O1 | Seção 0, linha "Maiores obstáculos (hipótese)" | "Total de R$ 28.050,00 a R$ 48.400,00 nas turmas abertas de pequenos animais" não bate com o catálogo (68629: R$ 16.456,00; 698: R$ 26.970,00) e contradiz a seção 4 e a Lista 1 | Trocar por "Total de R$ 16.456,00 (68629) a R$ 48.400,00 (657) nas turmas abertas de pequenos animais" ou dizer "no padrão 30x, de R$ 28.050,00 a R$ 48.400,00" |
| O2 | Seção 2.1, texto-padrão completo e exemplo de 68610; seção 1.1, linhas "1ª mensalidade", "Turma mínima", "Reembolso" e "Passagem e hotel" | A frase da 1ª mensalidade, a turma mínima de 20 e a orientação de passagem vêm das fichas e do contexto da linha, não do catálogo, e entram no texto que toda peça usa sem [CONFIRMAR NO CATÁLOGO]. A própria seção 1 diz que o que vem só das fichas leva a marcação | Marcar esses três trechos do texto-padrão com [CONFIRMAR NO CATÁLOGO] até subirem para o catálogo (o pedido já está na seção 10) e acrescentar a marcação na coluna "Fonte" das linhas de 1.1 que vêm só de ficha |
| O3 | Seção 2.1, "Texto-padrão da prova de bolsa"; seção 1.4, linhas "Formato" a "Regras da bolsa" | "das 9h às 13h", "presencial", 11 bolsas, nota 7,0 e 10 dias úteis estão no texto pronto para peça sem marcação. O horário só existe na ficha 68646. A ficha 68652 diverge (prazo de 7 dias, resultado no site ou por e-mail, 10 a 20 questões) | Marcar horário e regras com [CONFIRMAR NO CATÁLOGO] no texto-padrão. Registrar que a ficha 68652 diverge do contexto da linha e que a prova fica fora da campanha (já está em 3.2) |
| O4 | Seção 3.1, primeira frase ("a única redução de preço publicada para a Pós hoje") | Contradiz a seção 1.3: a promoção de 20% de 341 está publicada no catálogo, e 359 e 352 têm desconto na ficha | Trocar por "a única redução de preço com regra completa publicada e liberada para peça hoje" |
| O5 | Seção 5, PR5 (pares 68614 com 68610 e 560 com 68628) e seção 7.2, T3 ("560 com 68628") | Pares impossíveis pelo calendário do catálogo: 68614 começa em 28/11/2026, no mesmo dia de 68610; 560 começa em 22/05/2027, depois do início de 68628 (10/04/2027). O livre não pode servir de degrau para uma pós que já começou | Retirar esses dois pares de PR5 e trocar o exemplo de T3 por um par em que o livre acontece antes da pós (ex.: 68638 em 06/03/2027 com 68635 em 10/04/2027; 573 em 14/11/2026 com 698 em 28/11/2026) |
| O6 | Seção 3.2, parágrafo de abertura ("leitura do QA") e Lista 2 ("pela leitura do QA") | Atribuição errada: o qa-de-marketing não produziu essa leitura; ela vem da pesquisa-de-persona, seção 2 | Trocar por "leitura do agente (pesquisa-de-persona, seção 2)" |
| O7 | Seção 1.2, padrão 24x, linha de 60 ("turma mínima de 15 na ficha") e seção 6, A14 | Dado só da ficha, sem [CONFIRMAR NO CATÁLOGO] | Acrescentar [CONFIRMAR NO CATÁLOGO] |
| O8 | Seção 9.1, item "Preços, bolsas e condições" | Autoavaliação diz que tudo o que vem de ficha está marcado; não está (O2, O3, O7) | Refazer o item depois das correções |

**Veredito: CORRIGIR.** O1 é falha de dado de curso (conformidade, item 1); O2 e O3 são falha de marcação da regra de fonte. O4 a O8 são correções leves que entram na mesma volta.

---

## 2. saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-pos-2026-10-26.md

### 2.1 Conferência dos dados de curso com o catálogo

| Dado | Resultado |
|---|---|
| 30 turmas e 22 provas abertas; 6 turmas iniciando no trimestre (707, 68604, 68606, 68610, 68608, 698) | confere |
| 24 turmas de 13/03 a 28/05/2027: 5 em março, 9 em abril, 10 em maio, com os códigos da Lista 1 | confere |
| Vencimentos calculados da 1ª mensalidade (11/02 a 25/02/2027; 04/03 a 25/03/2027) | contas corretas; marcadas [SUPOSIÇÃO] e [CONFIRMAR por ficha] |
| Matrícula de R$ 250,00 ou R$ 350,00 (M1) | confere |
| Lote 1 de abril com prova compatível (68635, 68636, 68617, 68628, 68609, 68632) | confere com a seção 3.2 da oferta |
| Datas do calendário: 26/10/2026 segunda; 02/11 segunda e feriado; 03/11 terça; 20/11 feriado; 27/11 sexta | conferidas no calendário de 2026 |
| Blocos de 34, 28 e 28 dias somando 90 dias (27/10/2026 a 24/01/2027) | conta correta |
| "Provas de bolsa, 9h às 13h" com fonte "catálogo, seção 3" (seção 5.1) | **fonte errada**: o horário não está no catálogo (ver M3) |
| Números de meta, verba, vagas, leads e matrículas | nenhum apresentado como fato: tudo [CONFIRMAR] ou fórmula. Teto de capacidade, meta de 100% de páginas e 1 teste por mês marcados [SUPOSIÇÃO] |
| Regras da prova (seção 1, item 3, e Lista 1) | iguais às de contexto/pos-graduacao.md |

### 2.2 auditorias/02-estrategia-e-posicionamento.md, item por item

| Item | Resultado do QA | Observação |
|---|---|---|
| O plano tem uma única meta principal | Atendido | Turmas de Pós confirmadas com a turma mínima, fórmula e valor [CONFIRMAR] |
| Persona e curso ou oferta estão nomeados | Atendido | P1 e P4; oferta "Pós sem surpresa" e prova; turmas por código |
| Os 8 canais foram avaliados; ativos cabem na capacidade; fora com justificativa | Atendido com ressalva | Os 8 têm motivo e gatilho. Os ajustes de YouTube e LinkedIn em relação ao plano do cmo estão como proposta, mas não batem com a estrategia-de-conteudo (seção 4 deste QA) e precisam de decisão do cmo |
| O posicionamento nomeia a alternativa real | Atendido (herdado) | |
| Todo pilar tem prova | Atendido (herdado) | |
| As regras de voz têm exemplos | Atendido com ressalva (herdado) | |
| O plano cabe no tempo e na verba informados | Pendente de dado, com ressalva a corrigir | Horas e verba não informadas; o teto [SUPOSIÇÃO] está bem desenhado, mas a tabela 5.5 não conta as peças semanais da estrategia-de-conteudo (M5) |
| Nenhuma oferta, pilar ou resposta promete emprego, aprovação ou salário | Atendido | |
| Preços, bolsas e condições do catálogo ou marcados | Atendido com correção | Horário da prova atribuído ao catálogo (M3) |

### 2.3 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado do QA |
|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração batem | Atendido, com a fonte do horário da prova a corrigir (M3) |
| Dados do curso | Status "aberto" | Atendido: pede pausa das 6 turmas em "verificar" com campanha ativa |
| Dados do curso | Modalidade clara | Atendido |
| Regulação | Graduação: ato | Não se aplica |
| Regulação | Pós sem "reconhecida pelo MEC" | Atendido (R12 e U4) |
| Regulação | Curso livre não confere diploma | Atendido com nota: seção 6.2, item 6 ("livres como ponte") exige a frase quando virar peça |
| Regulação | Nota MEC | Atendido |
| Promessas | Sem emprego, salário, aprovação | Atendido |
| Promessas | Empregabilidade com fonte | Não se aplica |
| Promessas | Superlativos | Atendido |
| Promessas | Comparação com concorrente | Atendido: Anclivepa só em calendário interno; falta marcar a data de 14/11 (M4) |
| Preço (CDC) | Preço completo | Atendido (herda o texto-padrão da oferta) |
| Preço (CDC) | Bolsa e desconto com regra, público e validade | **Falha**: a aposta 2 e o risco R2 deixam subir "a peça mestre" da campanha única sem dizer que ela exclui as 4 provas sem turma (68652, 68649, 68653, 68655) e as 8 de destino incerto; a oferta (3.2) diz que vender inscrição sem curso de destino fere este item (M1) |
| Preço (CDC) | Urgência real | Atendido |
| Preço (CDC) | Prouni, Fies | Não se aplica |
| Pessoas e dados | Autorização de imagem e voz | Atendido (U9; Reels e vídeo com docente só autorizado) |
| Pessoas e dados | Menores | Não se aplica |
| Pessoas e dados | Formulários | Não se aplica |
| Pessoas e dados | Consentimento em WhatsApp e e-mail | Atendido (canal 1, 6.2, U9, R7) |
| Pessoas e dados | Nenhum dado pessoal | Atendido (só números somados) |
| Plataformas | Sem segmentação discriminatória | Atendido |
| Plataformas | Destino entrega o que promete | Atendido: aposta 1 bloqueia campanha nova para página com pendência |
| Anúncios | Sem característica pessoal | Atendido |
| Anúncios | Sem escassez falsa | Atendido |
| Anúncios | Sem pessoa pública | Atendido |
| Anúncios | Sem caixa alta | Não se aplica |
| Anúncios | Destino com dados da Ufape e política | Atendido (M14) |
| Anúncios | Sem drible | Atendido |

### 2.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| M1 | Seção 3, aposta 2 (coluna "O que fica de fora"), e seção 6.1, R2 | A peça mestre e os envios para a base não excluem de forma explícita as 4 provas sem turma de destino e as 8 incertas, ao contrário da oferta (3.2), que as tira da campanha até a Ufape escrever o destino | Escrever: "A peça mestre, os e-mails e o WhatsApp para a base citam só as provas com destino confirmado pela Ufape. 68652, 68649, 68653 e 68655 ficam fora de toda peça; as 8 incertas entram quando o destino estiver escrito" |
| M2 | Seção 7, U8, prazo "13/11 (PR4, PR9, PR2, PR1)", e seção 5.4, S3, 13/11 | Conflita com a oferta (seção 10: PR4 e PR9 até 29/10/2026, por causa de 68610, 68608 e das peças das provas de 03/11). Decidir PR4 em 13/11 chega depois do início de 707, 68604 e 68606 | Separar: PR4 até 28/10 (junto com U7) e PR9 até 31/10 (junto com U6); PR2 e PR1 podem ficar em 13/11 |
| M3 | Seção 5.1, linha de 27/11 ("9h às 13h", fonte "catálogo, seção 3") | O horário não está no catálogo; vem da ficha 68646 | Fonte: "ficha 68646 [CONFIRMAR NO CATÁLOGO]" |
| M4 | Seção 6.1, R8 ("prova da Anclivepa em 14/11") | Data de concorrente sem fonte nem marcação, diferente da data citada no resto do arquivo (07/11, fim das inscrições) | Indicar a fonte (inteligencia-concorrencia) e marcar [CONFIRMAR no edital oficial], como no restante do arquivo |
| M5 | Seção 5.3 e tabela 5.5 | O teto de 3 lotes por semana não conta o calendário semanal da estrategia-de-conteudo (5 peças por semana no Nível 1, com 20 h em S1 e S2). S1, S11 e S12 já estão "no limite" sem ele | Incluir o lote semanal de conteúdo na tabela 5.5 ou dizer qual frente sai para ele caber; registrar a decisão para a estrategia-de-conteudo |
| M6 | Seção 5.4, S6, 02/12 ("6 posts, 3 criativos, 4 WhatsApp e 2 e-mails por turma (kit mínimo...)") | O kit mínimo de templates/kit-de-lancamento-pos.md também tem 1 roteiro de vídeo curto e 1 post por docente autorizado (além de página, plano dos 8 canais e plano de mídia). "O mínimo nunca diminui" | Listar o kit inteiro ou citar o template sem resumir; o post por docente fica [CONFIRMAR autorização] e não conta como faltante (P13 do cmo) |
| M7 | Seção 1, item 3, e seção 3, aposta 2 ("única redução de preço publicada") | Mesma imprecisão da oferta (O4): a promoção de 341 está publicada | "única redução de preço com regra completa e liberada para peça" |
| M8 | Seção 3, aposta 5, e seção 5.4 (briefings em 11/12, pilar A11 em 23/12 e 08/01, A2 em 15/01, A1 depois) | O conteúdo pilar começa em dezembro por A11 e A2, mas a estrategia-de-conteudo publica guias por área desde novembro (A8, A11) e A1 em 07/12 | Ver a seção 4 deste QA: o cmo decide uma ordem; este arquivo e o de conteúdo passam a citar a mesma |

**Veredito: CORRIGIR.** M1 é falha no item "bolsa e desconto com regra, público e validade". M2 a M8 corrigem calendário, fonte e consistência.

---

## 3. saidas/04-conteudo/estrategia-de-conteudo-pos-2026-10-26.md

### 3.1 Conferência dos dados de curso com o catálogo

| Dado | Resultado |
|---|---|
| C09: 68610, 28/11/2026, turma V, semipresencial, 500 h, 30x de R$ 1.000,00, R$ 30.000,00, matrícula de R$ 250,00 | confere |
| C16: 68608, 28/11/2026, turma VIII, 500 h, 30x de R$ 1.180,00, R$ 35.400,00, matrícula de R$ 250,00 | confere |
| Lista 1: 698 (III, 370 h, 18x de R$ 1.498,33, R$ 26.970,00, R$ 250,00), 707, 68604, 68606 e datas de março, abril e maio | conferem |
| 19 turmas em "verificar" (seção 1.2) | confere com o catálogo |
| Dados só da ficha 68610 (7 presenciais, módulos 5 e 9, práticas não transmitidas) | marcados [CONFIRMAR NO CATÁLOGO] |
| "18 docentes" de 68610 (pilar P5) | só da ficha, sem marcação (C8) |
| Nome de 719 (seção 5.3: "Pós-graduação Inteligência Artificial na Saúde") | fora do padrão "Pós-graduação em" (C9) |
| Turma mínima na seção 0 ("turma mínima de 20 alunos") | apresentada como fato; o contexto da linha marca 15 x 20 [CONFIRMAR] (C3) |
| Regras da prova | 11 bolsas, nota 7,0, 2 e 10 dias úteis, não acumulativa e intransferível: iguais ao contexto. A afirmação de "contradição entre as fichas" (seção 2, P3; seção 0, item 6) só se confirma na ficha 68652 (7 dias, resultado no site ou por e-mail); a ficha 68646 segue o contexto (C6) |
| Datas de calendário: 27/11/2026 é sexta (Black Friday); Carnaval em 09/02/2027; dias da semana das peças C01 a C28 | conferidos |
| Esforço de referência | Nível 2 soma 22 h, não 21 h; S4 no Nível 1 soma 10 h, não 12 h (C12) |

### 3.2 auditorias/04-qualidade-de-conteudo.md, item por item

| Item | Resultado do QA | Observação |
|---|---|---|
| O leitor e a mensagem principal ficam claros na introdução | Atendido com ressalva | Leitor (P1) e mensagem claros, mas a seção 0, item 1, diz "meta uma só" e lista duas (turmas confirmadas e inscritos nas provas) (C2) |
| Toda seção tem exemplo ou prova | Atendido | |
| Nenhum parágrafo de enrolação | Atendido | |
| Os fatos têm fonte | Ressalva | "Regras em contradição nas fichas" generalizado para todas as provas sem citar a ficha 68652 (C6); "18 docentes" sem marcação (C8) |
| As regras de voz da marca foram seguidas | **Falha** | A seção 7.5 adota os traços "precisa, próxima, transparente" (estrategia-de-marca, ainda proposta); o guia vigente em contexto/ufape-geral.md diz "técnica, próxima, confiante" [SUPOSIÇÃO] (C10). "Condições à vista" no título da S1 e na seção 0 contraria a regra 5 do texto-padrão da oferta (C11) |
| Uma única chamada para ação clara | Atendido com ressalva | Cada peça tem uma CTA, mas C02 (04/11) e C05 (03/11) apontam para o hub C01, que só sai em 05/11; C27 (28 e 29/11) aponta para o hub de uma prova que já aconteceu (C7) |
| Existe plano de reaproveitamento | Atendido | Seção 6 |
| Nenhuma promessa de emprego, salário ou aprovação | Atendido com ressalva | Nenhuma promessa; mas o pilar P4 se chama "Carreira e título de especialista" e está no pedido de aprovação E1 (C4) |
| Depoimentos e falas reais e autorizados | Atendido | Nenhum depoimento; docentes condicionados à autorização, com plano B |

### 3.3 auditorias/conformidade-educacional.md, item por item

| Bloco | Item | Resultado do QA |
|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração batem | **Falha**: turma mínima de 20 como fato (C3); nome de 719 fora do padrão (C9). Os dados de 68610, 68608 e 698 batem |
| Dados do curso | Status "aberto" | Atendido |
| Dados do curso | Modalidade clara | Atendido (68632 presencial; EAD sem turma aberta) |
| Regulação | Graduação: ato | Não se aplica (Enem e Graduação só como calendário) |
| Regulação | Pós sem "reconhecida pelo MEC" | Atendido (7.2; C22 não repete a frase da ficha 68652) |
| Regulação | Curso livre não confere diploma | Atendido (7.2, item 4) |
| Regulação | Nota MEC | Atendido |
| Promessas | Sem emprego, salário, aprovação | **Falha leve**: o pilar P4 "Carreira e título de especialista", mesmo bloqueado, nomeia carreira e título como tema de pilar e vai para aprovação em E1; a oferta (2.2) lista "título de especialista" em "o que não dizer" (C4) |
| Promessas | Empregabilidade com fonte | Não se aplica |
| Promessas | Superlativos | Atendido (7.4, item 8) |
| Promessas | Comparação com concorrente | Atendido (7.4, item 3; 5.3) |
| Preço (CDC) | Preço completo | Atendido (C09, C16, C18, T8) |
| Preço (CDC) | Bolsa e desconto com regra, público e validade | **Falha**: C01 (hub), C02, C05 e C06 cobrem "todas, 22 provas", tirando só 68656, 68641 e 68642. As 4 provas sem turma (68652, 68649, 68653, 68655) e as 8 de destino incerto continuam no hub e nos envios (C1) |
| Preço (CDC) | Urgência real | Atendido; J4 ("faltam 6 semanas") deve trazer a data exata do início |
| Preço (CDC) | Prouni, Fies | Não se aplica |
| Pessoas e dados | Autorização de imagem e voz | Atendido (C26, C27 condicionadas) |
| Pessoas e dados | Menores | Atendido (7.3, item 5) |
| Pessoas e dados | Formulários com finalidade e política | Atendido (M2 da seção 8) |
| Pessoas e dados | Consentimento | Atendido (só opt-in em todos os envios) |
| Pessoas e dados | Nenhum dado pessoal | Atendido |
| Plataformas | Sem segmentação discriminatória | Não se aplica |
| Plataformas | Destino entrega o que promete | **Falha**: C02 e C05 levam a um hub ainda não publicado; C27 leva ao hub de prova encerrada (C7) |
| Anúncios | Sem característica pessoal | Atendido (7.4, item 10) |
| Anúncios | Sem escassez falsa | Atendido |
| Anúncios | Sem pessoa pública | Atendido |
| Anúncios | Sem caixa alta | Atendido (7.5, item 6) |
| Anúncios | Destino com dados da Ufape e política | Ressalva herdada (46 páginas com a frase do MEC, P2) |
| Anúncios | Sem drible | Atendido |

### 3.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| C1 | Seção 4, C01 (coluna "Pilar e área": "todas as áreas (22 provas)"), C02, C05, C06, C19, C21, C23 a C25 | O hub e os envios incluem as 4 provas sem turma e as 8 incertas; a oferta (3.2) e o cmo (P10) as tiram da campanha até haver destino | No hub e nos envios, só provas com destino confirmado; as 4 sem turma ficam fora de toda peça (C22 já está condicional); as 8 incertas entram quando o destino estiver escrito |
| C2 | Seção 0, item 1 | "Meta a servir (uma só)" lista duas metas | Meta: turmas confirmadas com a turma mínima. Inscritos nas provas viram métrica de apoio (M8 da estrategia-de-marketing) |
| C3 | Seção 0, item 1 ("turma mínima de 20 alunos") | Apresentado como fato; contexto, oferta e marketing marcam 15 x 20 [CONFIRMAR] | "turma mínima (20 nas páginas das turmas, 15 nas páginas das provas: [CONFIRMAR])", como já está na seção 7.4, item 5 |
| C4 | Seção 0, item 3; seção 2, pilar P4; seção 10, E1; seção 5.2, J3 | Pilar "Carreira e título de especialista" vai para aprovação com nome que remete a carreira e título | Renomear para "O que a pós lato sensu é e o que ela não é" e tirar P4 da aprovação de E1 até a regulação liberar o texto (E9). J3 continua bloqueado |
| C5 | Seção 4, S3: C19 (sex 20/11, WhatsApp da prova) e C18 (sex 20/11, e-mail) | A estrategia-de-marketing (S4 e R8) proíbe mensagem das provas para a base em 20 e 21/11 (workshop e feriado); 20/11 é feriado nacional | Mover C19 para qui 19/11 ou seg 23/11 e C18 para qui 19/11 |
| C6 | Seção 0, item 6; seção 2, P3; seção 4, C01; seção 10, E4; Lista 3 | "Regras da prova em contradição nas fichas (canal do resultado, 10 ou 7 dias)" sem dizer que a divergência está na ficha 68652; o contexto da linha diz que as 22 páginas seguem a mesma regra, e a 68646 confirma | Citar a ficha 68652 como origem da divergência; para as demais provas, usar as regras de contexto/pos-graduacao.md. Registrar como nota para o contexto (não editar) |
| C7 | Seção 4: C02 (qua 04/11) e C05 (ter 03/11) antes de C01 (qui 05/11); C27 com CTA "link do hub" | Peças levam a um destino que ainda não existe; C27 leva ao hub de prova já realizada | Publicar C01 até 03/11 ou mover C02 e C05 para depois de 05/11. Em C27, CTA para a página da área ou da próxima turma aberta |
| C8 | Seção 2, P5 ("68610 com 18") | Contagem de docentes só da ficha, sem marcação | Acrescentar [CONFIRMAR NO CATÁLOGO] |
| C9 | Seção 5.3, terceiro item | "Pós-graduação Inteligência Artificial na Saúde" fora do padrão de nome da linha | "Pós-graduação em Inteligência Artificial na Saúde" |
| C10 | Seção 7.5, item 5 | Traços de voz diferentes do guia de marca vigente (contexto/ufape-geral.md: técnica, próxima, confiante) | Usar os traços do guia vigente; citar os da estrategia-de-marca como proposta pendente de aprovação |
| C11 | Seção 0, itens 2 e 4; título da S1 ("condições à vista") | A oferta (2.1, regra 5) pede "condições claras" nas peças de preço, porque "à vista" pode ser lido como pagamento à vista, que não existe na Pós | Trocar por "condições claras" nos títulos e temas; manter a citação literal do posicionamento só onde ela for citação |
| C12 | Seção 3.3 (Nível 2 = 21 h) e quadro de volume (S4 = 12 h no Nível 1) e Lista 2 | Contas erradas: 16 + 4 + 1 + 1 = 22 h; S4 no Nível 1 (C21 M + C23, C24, C25) = 10 h | Corrigir para 22 h e 10 h (15 h a 17 h com N2) |
| C13 | Seção 3.1 (YouTube "Ativo leve"; LinkedIn "visão de fevereiro") e seção 5.2, F4 | Diverge da estrategia-de-marketing (YouTube fora no bloco 1 e teste condicionado a partir de 30/11; decisão sobre LinkedIn em 08/01) | Alinhar com a estrategia-de-marketing, ou registrar a diferença como pedido ao cmo |
| C14 | Seção 8.2, item 4 ("toda segunda-feira (02/11, ...)") | 02/11 é feriado; a estrategia-de-marketing move a revisão para terça, 03/11 | Trocar 02/11 por 03/11 |
| C15 | Seção 4, dependências ("Regras da prova e destino das provas: 03/11") e S0.2 ("resposta até 03/11") | A estrategia-de-marketing (U6, R2) e o gestor-de-midia (D7) pedem até 31/10; as peças das provas são entregues em 03/11 | Prazo de 31/10 |
| C16 | Cabeçalho, "Entradas lidas" | Não leu a estrategia-de-oferta nem a estrategia-de-marketing da Pós, que vêm antes na cadeia (1.8 e 1.9). É a origem de C1, C5, C11, C13, C14 e C15 | Ler as duas e alinhar calendário, canais, ordem de áreas e regras de oferta |

**Veredito: CORRIGIR.** C1, C3, C4 e C7 são falhas na conformidade educacional; C10 é falha no item de voz da auditoria 04. O resto entra na mesma volta.

---

## 4. Consistência entre os três arquivos, com o plano do cmo e com o guia de marca

| Tema | Oferta | Marketing | Conteúdo | Plano do cmo e guia | Situação e correção |
|---|---|---|---|---|---|
| Meta | herda a do cmo | turmas confirmadas (uma só) | duas metas na seção 0 | uma meta (seção 1) | Conteúdo corrige (C2) |
| Turma mínima | 15 x 20 [CONFIRMAR] | 15 x 20 [CONFIRMAR]; usa 20 como [SUPOSIÇÃO] conservadora | 20 como fato na seção 0 | 20 (contexto) e 15 na prova (P10) | Conteúdo corrige (C3) |
| Ondas | ondas 1 a 3 iguais ao briefing | iguais | iguais | iguais | Consistente. Nota: o kit de março (lote 1 em 02/12, lote 2 em 09/12) fica depois da janela da onda 2 (07/11 a 27/11); o cmo confirma se aceita ou antecipa |
| Apostas | prova como entrada; reta final sem urgência; propostas PR | 5 apostas | pilares P3 e P2 em novembro servem às apostas 2 e 3 | | Consistente nas apostas 1 a 4. Aposta 5 (conteúdo pilar, "2 áreas no trimestre", A11 e A2 a partir de dezembro) não bate com o conteúdo (peça longa toda semana desde 05/11; guias de A8 e A11 em novembro; A1 em 07/12) nem com o cmo (conteudo-longo "depois"). O pedido E2 do conteúdo resolve só se o cmo aprovar. Correção: o cmo decide a ordem e o volume; marketing (M8) e conteúdo passam a citar a mesma |
| Provas sem destino | 4 fora; 8 só com destino | "D4 sem anúncio por área"; peça mestre sem exclusão explícita | hub com 20 provas | P10: destino [CONFIRMAR] | Marketing (M1) e conteúdo (C1) alinham à oferta |
| Prazo das decisões de oferta | PR4 e PR9 até 29/10 | U8: 13/11 | não cita | prazos da onda 1 em 28/10 a 03/11 | Marketing corrige (M2) |
| Prazo de regras e destino das provas | antes das peças de 03/11 | 31/10 (U6, D7) | 03/11 | peças das provas em 03/11 | Conteúdo corrige (C15) |
| Canais | não se aplica | 3 ativos; YouTube teste condicionado no bloco 2; LinkedIn só no bloco 3, decisão em 08/01 | YouTube "ativo leve"; LinkedIn "visão de fevereiro" | YouTube ativo leve; LinkedIn teste na onda 3 | O ajuste do marketing é proposta ao cmo. Até o cmo decidir, conteúdo cita a proposta do marketing como pendente (C13) |
| Revisão semanal | não se aplica | 03/11 (feriado em 02/11) | 02/11 | revisão de segunda-feira | Conteúdo corrige (C14) |
| 20 e 21/11 | não se aplica | sem mensagem das provas | C18 e C19 em 20/11 | workshop é da linha Eventos | Conteúdo corrige (C5) |
| Capacidade | não se aplica | teto de 3 lotes por semana | 5 peças por semana (16 h a 20 h) | horas do time [CONFIRMAR] | O teto não conta o conteúdo: marketing corrige (M5); conteúdo cita o teto |
| Kit mínimo de Pós | não se aplica | resumo sem vídeo curto e post por docente | não se aplica | template completo, mínimo nunca diminui | Marketing corrige (M6) |
| "Redução de preço publicada" | "única" (3.1) e, ao mesmo tempo, 341 em 1.3 | "única" | não usa | P16 (341) | Oferta (O4) e marketing (M7) corrigem |
| "Condições à vista" | pede "condições claras" | cita o posicionamento literalmente | usa em títulos | | Conteúdo corrige (C11); a citação literal no marketing é aceitável |
| Título de especialista | "o que não dizer" | não usa | pilar P4 | P1 (texto de certificação vazio) | Conteúdo corrige (C4) |
| Voz da marca | voz [SUPOSIÇÃO] | herda o posicionamento | traços da estrategia-de-marca | ufape-geral.md: técnica, próxima, confiante [SUPOSIÇÃO] | Conteúdo corrige (C10) |
| Destino das provas (10, 8, 4) | 10, 8, 4 | 10, 8, 4 | as 4 sem turma iguais | P10 | Consistente |
| Regras da prova | iguais ao contexto | iguais ao contexto | iguais, mais a divergência da 68652 sem citar a ficha | P10 | Conteúdo corrige (C6). Nota para o contexto da linha (não editada aqui): a ficha 68652 diverge da regra "iguais em todas" |
| Frase do MEC no site | 26 das 30 turmas (P2) | 46 páginas | 46 páginas | P2: 46 páginas, 26 das 30 turmas | Consistente (recortes diferentes do mesmo número) |
| A14 | "Outras" | chamada de "Equinos" na ordem das áreas | "outras" | "Outras especialidades" | Leve: o marketing pode dizer "A14 (341, equinos)" |

---

## 5. Notas para outros arquivos (este agente não os edita)

- contexto/pos-graduacao.md: a frase "regras iguais em todas" não vale para a ficha 68652 (prazo de matrícula de 7 dias na seção REGRAS, resultado no site ou por e-mail, 10 a 20 questões). Pedir confirmação à Ufape.
- contexto/catalogo-de-cursos.md: subir horário da prova, regras das bolsas, regra da 1ª mensalidade, turma mínima e orientação de passagem (o pedido já está na seção 10 da oferta).
- saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md: decidir YouTube e LinkedIn (proposta do marketing), a ordem das áreas e o volume do conteúdo longo (aposta 5 do marketing e E2 do conteúdo).

---

## Lista 1. Fatos (com fonte)

- 30 turmas de Pós abertas, com códigos, datas, parcelas, totais e matrículas (catálogo, seção 2, 26/10/2026).
- 22 provas de bolsa abertas em 27/11/2026, R$ 100,00; 68656 encerrada; 3 em Goiânia (catálogo, seção 3).
- 68629: 24x de R$ 685,67, total de R$ 16.456,00, matrícula de R$ 350,00; 698: 18x de R$ 1.498,33, total de R$ 26.970,00 (catálogo, seção 2).
- 68614 começa em 28/11/2026; 560 em 22/05/2027; 68638 em 06/03/2027; 573 em 14/11/2026 (catálogo, seção 4). 68610 começa em 28/11/2026; 68628 em 10/04/2027; 68635 em 10/04/2027 (catálogo, seção 2).
- Regras da prova: 11 bolsas (2 de 50% monitoria, 4 de 25%, 5 de 10%), nota 7,0, 2 dias úteis de recurso, 10 dias úteis para matrícula, não acumulativa e intransferível, desempate por currículo, mínimo 15 x 20 [CONFIRMAR], destino [CONFIRMAR] (contexto/pos-graduacao.md).
- Horário de 9h às 13h, prova presencial (ficha 68646). Prazo de matrícula de 7 dias e resultado no site na seção REGRAS da ficha 68652, que também diz 10 dias úteis em outro trecho.
- Kit mínimo de Pós: página, plano dos 8 canais, plano de mídia, 6 posts, 3 criativos, 1 post por docente autorizado, 4 WhatsApp, 2 e-mails, 1 roteiro de vídeo curto (templates/kit-de-lancamento-pos.md).
- Voz da marca vigente: técnica, próxima, confiante [SUPOSIÇÃO] (contexto/ufape-geral.md).
- Canais da Pós no plano do cmo: Instagram, Facebook (inventário), WhatsApp ativos; YouTube ativo leve; LinkedIn em teste na onda 3; TikTok, X e podcast fora (cmo, seção 5).
- Calendário: 26/10/2026 é segunda; 02/11/2026 é segunda e feriado; 20/11/2026 é feriado; 27/11/2026 é sexta; terça de Carnaval em 09/02/2027 (calendário oficial, conferido pelo QA).

## Lista 2. Suposições

- [SUPOSIÇÃO] A leitura de "pequenos animais" na seção 0 da oferta inclui 68629 e 698, porque ambas são de cães e gatos pelo nome e pela área (A5 e A2 do cmo).
- [SUPOSIÇÃO] O prazo de 31/10 para regras e destino das provas vale para o conteúdo, porque é o prazo da estrategia-de-marketing e do gestor-de-midia para as peças de 03/11.
- [SUPOSIÇÃO] Os pares de PR5 propostos como troca (68638 com 68635; 573 com 698) são possíveis pelo calendário; a decisão de pareamento é da Ufape.

## Lista 3. Dados que faltam

- [CONFIRMAR NO CATÁLOGO] Horário, local e regras da prova; regra da 1ª mensalidade; turma mínima (15 ou 20); orientação de passagem; número de docentes por turma.
- [CONFIRMAR] Turma de destino de cada prova; divergência da ficha 68652 (7 ou 10 dias; canal do resultado).
- [CONFIRMAR] Decisão do cmo sobre YouTube, LinkedIn, ordem das áreas e volume de conteúdo longo.
- [CONFIRMAR] Horas do time por semana (teto real de capacidade).
- [CONFIRMAR] Quem aprova cada tipo de peça (tabela vazia em contexto/ufape-geral.md).
- [CONFIRMAR no edital oficial] Datas da prova da Anclivepa-SP (07/11 e 14/11).
- [PREENCHER COM A REGULAÇÃO] Texto de certificação da Pós.

## Fontes

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (cabeçalho e seções 2, 3 e 4); contexto/cursos/pos/68646-prova-de-bolsa-de-estudos-para-dermatologia-veterinaria.md; contexto/cursos/pos/68652-prova-de-bolsa-de-estudos-para-medicina-de-felinos.md; templates/kit-de-lancamento-pos.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/04-qualidade-de-conteudo.md; auditorias/conformidade-educacional.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-pos-2026-10-26.md; saidas/04-conteudo/estrategia-de-conteudo-pos-2026-10-26.md.

Externas: nenhuma.
