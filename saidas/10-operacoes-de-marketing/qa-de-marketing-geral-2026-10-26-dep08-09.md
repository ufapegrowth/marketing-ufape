# QA de marketing: departamentos 08 (analise-de-funil) e 09 (analise-de-campanha e reconferência do analista-de-dados)

- Agente: qa-de-marketing (10 Operações de Marketing)
- Linha: geral
- Data: 26/10/2026
- Status: rascunho. Nada foi publicado, enviado ou pago. Os arquivos revisados não foram editados.
- Arquivos revisados:
  - /home/user/marketing-ufape/saidas/08-conversao/analise-de-funil-pos-2026-10-26.md (auditoria 08-conversao)
  - /home/user/marketing-ufape/saidas/08-conversao/analise-de-funil-livres-2026-10-26.md (auditoria 08-conversao)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analise-de-campanha-pos-2026-10-26.md (auditoria 09-analytics)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analise-de-campanha-livres-2026-10-26.md (auditoria 09-analytics)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analise-de-campanha-eventos-2026-10-26.md (auditoria 09-analytics)
  - /home/user/marketing-ufape/saidas/09-analytics-e-insights/analista-de-dados-geral-2026-10-26.md (versão 2; só os itens A1 a A4 do QA anterior)
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md, contexto/cursos-livres.md, contexto/eventos.md
  - contexto/catalogo-de-cursos.md (seções 1 a 9, completo)
  - docs/visao-de-campanhas-2026-10-26.md (67 linhas; numeração V1 a V67 igual à do analista: V1 é a linha 9 do arquivo, V67 a linha 75)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (completo, para conferir P1 a P18, A1 a A12, áreas, ondas e prazos)
  - auditorias/08-conversao.md, auditorias/09-analytics.md, auditorias/conformidade-educacional.md
  - saidas/10-operacoes-de-marketing/qa-de-marketing-geral-2026-10-26-dep09-10.md (seção 1, itens A1 a A4)

## Vereditos

| Arquivo | Veredito | Motivo principal |
|---|---|---|
| analise-de-funil-pos-2026-10-26.md | **APROVADO** | Todos os dados de curso conferidos batem com o catálogo; nenhuma taxa inventada; só recomendações |
| analise-de-funil-livres-2026-10-26.md | **CORRIGIR** | 616 descrito como "online gravado, sem data nem vaga", mas o catálogo dá data (05/12/2026) e local "Presencial e Online" (FL1) |
| analise-de-campanha-pos-2026-10-26.md | **CORRIGIR** | "A1 com zero ativas" contradiz o próprio arquivo (586 e 554 ativas) sem a ressalva do recorte (CP1); 68628 e 68632 lidas como "iniciadas, verificar" (CP2); dias "da visão" contra a regra de fonte (CP3) |
| analise-de-campanha-livres-2026-10-26.md | **CORRIGIR** | Nota sobre o analista desatualizada (CL1); janela de 4 a 8 semanas com leituras contraditórias, inclusive "fora da janela" e "dentro da janela" para 68618 (CL2) |
| analise-de-campanha-eventos-2026-10-26.md | **CORRIGIR** | Fonte errada no achado e no fato sobre "sem página": quem marca é o catálogo, não a planilha (CE1) |
| analista-de-dados-geral-2026-10-26.md (A1 a A4) | **APROVADO nos itens A1 a A4** | Os quatro itens foram resolvidos; R1 e R2 também foram atendidos |

Checagens transversais nos seis arquivos: nenhum dado pessoal (nome, telefone, CPF, e-mail de aluno, candidato ou lead); nenhum nome de docente; nenhum travessão nem meia-risca na leitura integral; "últimas vagas" e "vagas limitadas" só aparecem em regra proibitiva ou em pedido de número real; nenhum número de leads, verba, gasto, taxa ou matrícula foi estimado (todos [CONFIRMAR]). As contas derivadas (medianas, percentuais, tetos de receita do workshop) usam só preços do catálogo e contagens da visão e estão declaradas como "não são meta".

---

## 1. analise-de-funil-pos-2026-10-26.md

### 1.1 Recontagem por amostragem (7 itens)

| # | Dado no arquivo (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 22 provas de 27/11/2026 (1.2 e Fatos) | Catálogo, seção 3: 23 linhas com 27/11/2026, menos 68656 (encerrado) = 22 abertas | Sim |
| 2 | 13 provas antigas sem venda (5.2) | Catálogo, seção 3: 691, 687, 689, 695, 682, 681, 684, 680, 688, 694, 685, 690, 693 = 13 | Sim |
| 3 | 707 a 4 dias, 68610 a 33 dias, provas a 32 dias (Fatos) | 26/10 a 30/10 = 4; a 28/11 = 33; a 27/11 = 32 (datas do catálogo) | Sim |
| 4 | 68610 passa do prazo da 1ª mensalidade em 29/10 (hipótese 3) | 28/11/2026 menos 30 dias = 29/10/2026 | Sim |
| 5 | 68646 em 27/11 e 68610 em 28/11 (1.2, fato 3) | Catálogo, seções 2 e 3 | Sim |
| 6 | Felinos, Endoscopia, Nefrologia e Odontologia sem turma futura aberta (1.2, fato 1) | Catálogo: 650, 653, 68612, 68662 e 678 estão "verificar" (iniciadas); nenhuma turma futura aberta nessas áreas; igual ao plano, 2.3 | Sim |
| 7 | 19 ativas, 22 pausadas, 26 sem; 6 ativas em turma iniciada; 73,2% só estáticas (hipótese 10 e Fatos) | Visão: ativas só estático 13 e pausadas só estático 17, 30 de 41 = 73,17%; ativas iniciadas V16 a V20 e V32 = 6 | Sim |

Regras da prova (11 bolsas: 2 de 50%, 4 de 25%, 5 de 10%; nota 7,0; 2 dias úteis de recurso; 10 dias úteis de matrícula; resultado por WhatsApp ou e-mail; mínimo 15 contra 20) conferidas com contexto/pos-graduacao.md: batem.

### 1.2 Auditoria 08-conversao, item por item

| Item | Resultado | Observação |
|---|---|---|
| Topo da página passa no teste dos 5 segundos | Não se aplica | Desenho de funil, não é página |
| Uma chamada para ação principal por página | Não se aplica | O arquivo só registra o caminho único como hipótese 2 |
| Formulário pede só o necessário | Passa | Os campos propostos no CRM (3.4) são só código, UTM, etapa e motivo somado; nenhum dado pessoal |
| Provas reais e autorizadas | Não se aplica | Nenhuma prova, depoimento ou docente usado |
| Objeções respondidas na página | Não se aplica | Objeções viram hipóteses (6, 7, 8) com dado que confirma e que descarta |
| Testes têm hipóteses escritas | Passa | 10 hipóteses com etapa, evidência, dado que confirma, dado que descarta e prioridade |
| Resultados registrados | Não se aplica nesta rodada | Nenhum teste rodado; nenhum resultado inventado |
| Dados do curso conferidos com o catálogo | Passa (conferido pelo QA) | O arquivo declara que não reabriu o catálogo; o QA conferiu códigos, datas, regras da prova e matrícula, todos iguais (ver FP-R1) |
| Eventos de lead e inscrição rastreados e lead no CRM | Lacuna sinalizada | Hoje [CONFIRMAR]; o arquivo propõe a instrumentação (3.2 a 3.6). Não bloqueia uma saída de desenho |

### 1.3 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | Passa (só códigos e datas citados; conferidos) |
| Status "aberto" ou sem chamada para inscrição | Passa (análise interna, sem chamada) |
| Modalidade clara e correta | Não se aplica (não cita modalidade) |
| Graduação: ato do catálogo | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Passa (nenhuma afirmação; ver FP-R3) |
| Curso livre: não confere diploma | Não se aplica |
| Nota MEC com fonte | Passa (nenhuma nota) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa (nenhum) |
| Comparação com concorrente | Passa ("sem benchmark externo", 5.3) |
| Preço com valor, parcelas e condições | Passa (só matrícula de R$ 250,00 e inscrição de R$ 100,00, iguais ao catálogo) |
| Bolsa e desconto com regra, público e prazo | Passa (regras do contexto; destino e distribuição [CONFIRMAR]) |
| Urgência real | Passa (nenhuma) |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Não se aplica |
| Menores | Não se aplica |
| Formulários com finalidade e política | Não se aplica (não é formulário) |
| WhatsApp e e-mail com consentimento | Passa ("só com aprovação humana e opt-in", cenário B) |
| Nenhum dado pessoal | Passa (só contagens; texto livre não sai do CRM) |
| Políticas Meta e Google | Não se aplica |
| Página de destino entrega o prometido | Não se aplica |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica (não é anúncio) |

### 1.4 Problemas e correções

Nenhum problema bloqueante.

Recomendações (não bloqueiam):
- FP-R1. Cabeçalho, "Não reaberto nesta etapa" (linha 19): incluir contexto/catalogo-de-cursos.md nas entradas e citar o catálogo como fonte das datas nos Fatos (linhas 319 e 320), em vez de só o analise-cro. Os valores já batem.
- FP-R2. Seção 4, pergunta 2 (linha 232): "cada turma da onda 1 ... e as turmas de março de 2027". As turmas de março são da onda 2 (briefing). Escrever "cada turma da onda 1 e, da onda 2, as de março de 2027".
- FP-R3. Hipótese 9 (linha 141): "frase de certificação ligada ao MEC" não repete a frase nem afirma certificação e segue a redação do plano (P2). Para padronizar com o QA anterior (B3), preferir "afirmação de certificação não aprovada (P2)".

**Veredito: APROVADO.** Segue para a aprovação humana.

---

## 2. analise-de-funil-livres-2026-10-26.md

### 2.1 Recontagem por amostragem (7 itens)

| # | Dado no arquivo (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 573: 14/11 no catálogo, 29/11 na visão; 19 dias (1.2, hipótese 3, cenário A) | Catálogo, seção 4; visão, linha 49 (V41); 26/10 a 14/11 = 19 | Sim |
| 2 | 68614: 28/11 e 18/12 (hipótese 3, Fatos) | Catálogo, seção 4; visão, linha 50 (V42) | Sim |
| 3 | 68618: 18/12/2026 e 22/05/2027 (hipótese 3) | Catálogo, seção 4; visão, linha 71 (V63) | Sim |
| 4 | 68665 em 01/11/2026 e 68666 em 25/11/2026 (1.2) | Catálogo, seção 7 | Sim |
| 5 | 4 dos 55 itens do recorte na visão (Fatos; 3.5) | 573, 623, 68614 e 68618 na visão; recorte de Livres: 7 + 1 + 2 + 22 + 13 + 2 + 8 = 55 (catálogo e plano, 2.2) | Sim |
| 6 | Cartão mais caro que à vista em 573, 411 e 713 (hipótese 5) | 573: 10 x 303,00 = 3.030,00 contra 2.350,00; 411: 6 x 98,00 = 588,00 contra 420,00; 713: 10 x 88,00 = 880,00 contra 734,00 | Sim |
| 7 | "13 minicursos contínuos", na linha "Minicurso online de 8 h" (1.2) | Catálogo, seção 5: 13 minicursos abertos, mas 669 tem 6 h; os outros 12 têm 8 h | Parcial (FL-R1) |

### 2.2 Auditoria 08-conversao, item por item

| Item | Resultado | Observação |
|---|---|---|
| Topo da página passa no teste dos 5 segundos | Não se aplica | Desenho de funil |
| Uma chamada para ação principal por página | Não se aplica | Caminho único tratado como hipótese 4 |
| Formulário pede só o necessário | Passa | Campos propostos sem dado pessoal; boletos por e-mail contados "sem nome nem e-mail do candidato" |
| Provas reais e autorizadas | Não se aplica | Nenhuma prova usada |
| Objeções respondidas na página | Não se aplica | Objeções viram hipóteses 6 e 8 |
| Testes têm hipóteses escritas | Passa | 11 hipóteses com dado que confirma e que descarta |
| Resultados registrados | Não se aplica nesta rodada | Nenhum teste rodado |
| Dados do curso conferidos com o catálogo | **Corrigir** | Datas, preços e códigos batem, exceto a descrição do 616 (FL1) |
| Eventos de lead e inscrição rastreados e lead no CRM | Lacuna sinalizada | Proposta na seção 3; hoje [CONFIRMAR] |

### 2.3 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | **Bloqueia** (FL1: 616 tratado como gravado e sem data) |
| Status "aberto" ou sem chamada para inscrição | Passa (sem chamada) |
| Modalidade clara e correta | **Bloqueia** (FL1: catálogo traz "Presencial e Online", modalidade "On-line", com data) |
| Graduação: ato do catálogo | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Não se aplica (nenhuma menção) |
| Curso livre: não confere diploma | Não se aplica (não é peça; nenhuma afirmação de certificação) |
| Nota MEC com fonte | Passa (nenhuma) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa (nenhum) |
| Comparação com concorrente | Passa ("sem benchmark externo") |
| Preço com valor, parcelas e condições | Passa (cita cartão e à vista sem valores novos) |
| Bolsa e desconto com regra | Não se aplica (cupom citado só como parâmetro) |
| Urgência real | Passa ("vagas restantes só com número real", cenário B) |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Não se aplica |
| Menores | Não se aplica |
| Formulários com finalidade e política | Não se aplica |
| WhatsApp e e-mail com consentimento | Passa ("só com consentimento", "opt-in") |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Não se aplica |
| Página de destino entrega o prometido | Não se aplica |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica |

### 2.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| FL1 | Seção 1.2, linha "Online gravado" (linha 85) | O 616 é citado como referência do formato "online gravado", que o arquivo descreve como "sem data nem vaga; L7 é o primeiro acesso". No catálogo (seção 5), o 616 tem início em 05/12/2026, local "Presencial e Online", modalidade "On-line", 12 h, e o plano (2.2) o conta como "Online com data". A analise-de-campanha de Livres (2.5) trata o mesmo 616 como item com data e janela: os dois arquivos se contradizem | Tirar o 616 da linha "Online gravado" e criar a linha "Online com data: 616 (05/12/2026; Presencial e Online no catálogo)", com L7 = presença ou acesso na data e leitura por dias até a data, como nos presenciais |

Recomendações (não bloqueiam):
- FL-R1. Seção 1.2, linha "Minicurso online de 8 h" (linha 86): escrever "13 minicursos contínuos (12 de 8 h e o 669, de 6 h)". O plano usa a mesma simplificação.
- FL-R2. Seção 5, regra 6 (linha 213): incluir a duplicidade 642 e 712, que a hipótese 10 já cita.
- FL-R3. Cabeçalho (linha 19): incluir contexto/catalogo-de-cursos.md nas entradas; as datas citadas "no catálogo" vieram do analista e batem.

**Veredito: CORRIGIR** (FL1). Volta para o analise-de-funil.

---

## 3. analise-de-campanha-pos-2026-10-26.md

### 3.1 Recontagem por amostragem (8 itens)

| # | Dado no arquivo (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 42 linhas de Pós: 14 ativas, 18 pausadas, 10 sem (1.1) | Visão linha a linha. Ativas: linhas 24 a 28, 40 a 43, 45 a 47, 52, 63. Pausadas: 23, 31, 32, 37 a 39, 51, 53 a 56, 60 a 62, 67, 68, 72, 73. Sem: 16, 18, 57 a 59, 64 a 66, 69, 70 | Sim |
| 2 | Tabela 1.4: só estático 8 e 13; estático e vídeo 6 e 4; só vídeo 0 e 1; com 5 ângulos 7 e 6; sem 5 ou só estático 10 e 15; pacote completo 4 e 3 | Recontado na visão; percentuais de 32: 65,6; 31,3; 3,1; 40,6; 59,4; 78,1; 21,9 | Sim |
| 3 | 8 ativas não iniciadas: completo 68606, 698, 68608; falta vídeo 68604, 68610, 289; falta ângulos 707 e 662 (1.4) | Visão, linhas 41 a 43, 45 a 47, 52, 63 | Sim |
| 4 | Preços e turmas das 12 pausadas futuras (1.3) e das 6 ativas iniciadas (1.2) | Catálogo, seção 2: 657 II 48.400,00; 68615 VII 35.400,00; 341 I 43.500,00; 333 I 28.050,00; 679 IV 33.000,00; 68635 V 33.000,00; 366 I 33.000,00; 68617 V 36.000,00; 578 IV 37.500,00; 382 I 33.750,00; 352 I 47.880,00; 60 I 29.700,00; 650, 68662, 706, 586, 554, 68612 também batem | Sim |
| 5 | 22 provas, 19 especialidades; 28 itens da onda 1; 78,6% (1.5, 1.6) | 19 especialidades (3 com duas praças); 6 turmas + 22 provas = 28; 22 / 28 = 78,57% | Sim |
| 6 | Turmas da mesma especialidade (tabela 1.5) | Catálogo: 359 (22/05/2027), 68609 GO (24/04/2027), 68632 GO (10/04/2027), 68636 (17/04/2027), 68629 (22/05/2027), 68623 GO (22/05/2027), 68616 (08/05/2027), 68628 (10/04/2027); status de mídia conferido na visão | Sim |
| 7 | Leituras finais 29/11, 30/11 e 07/12 (3.1) | 30/10 + 30 = 29/11; 31/10 + 30 = 30/11; 07/11 + 30 = 07/12 | Sim |
| 8 | Prazos e pendências do plano: A4 em 28/10, provas 29/10 e 03/11, P2 46 páginas, P3, P4, P5, P16 (vários) | Plano do cmo, seções 4, 7 e 8 | Sim |

### 3.2 Auditoria 09-analytics, item por item

| Item | Resultado | Observação |
|---|---|---|
| Árvore de métricas existe e está atualizada | Passa | Usa a árvore da Pós do analista (5.1); o relatório 3.2 segue os mesmos ramos |
| Toda métrica tem fonte nomeada | Passa | Colunas "Onde olhar" (2.1) e "Fonte" (3.2): Meta Ads, Google Ads, CRM, GA4, Chatwoot, loja, catálogo |
| Relatórios comparam com as metas | Não se aplica nesta rodada | Sem metas; o modelo exige realizado contra meta, com versão e data |
| Metas não batidas com a mesma clareza | Não se aplica nesta rodada | O modelo separa leads e matrículas e proíbe trocar a meta depois |
| Insights terminam com uma ação | Passa | H1 a H11 com "como testar"; 4 pedidos de aprovação |
| Lacunas de dados sinalizadas | Passa | "Dados que faltam" com 12 itens |
| Backlog revisado todo mês | Não se aplica | Fica com o backlog-de-otimizacao (1.33) |
| CPL, custo por matrícula, conversão e receita por linha | Não se aplica nesta rodada | Sem números; arquivo só da Pós; nada estimado |
| Nenhum dado pessoal | Passa | |

### 3.3 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | **Bloqueia** (CP2: 68628 e 68632 descritas como iniciadas e "verificar"; no catálogo estão "aberto", 10/04/2027) |
| Status "aberto" ou sem chamada para inscrição | **Bloqueia** pelo mesmo CP2 (status errado atribuído) |
| Modalidade clara e correta | Passa (586 como EAD; praças SP e GO corretas) |
| Graduação: ato do catálogo | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Passa (as menções em 1.7, C3 e R1 são regra proibitiva ou sinalização, sem repetir a frase) |
| Curso livre: não confere diploma | Não se aplica |
| Nota MEC com fonte | Passa (nenhuma) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa ("maior ticket futuro" é medida do catálogo) |
| Comparação com concorrente | Não se aplica |
| Preço com valor, parcelas e condições | Passa (preço total do catálogo; parcelas citadas em 698 e 586 corretas; promoção da 341 marcada [CONFIRMAR], P16) |
| Bolsa e desconto com regra | Passa (regras do contexto; destino [CONFIRMAR]) |
| Urgência real | Passa (nenhuma) |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Não se aplica |
| Menores | Não se aplica |
| Formulários | Não se aplica |
| WhatsApp e e-mail com consentimento | Não se aplica |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Passa (R1 trata destino errado e frase de certificação como falha) |
| Página de destino entrega o prometido | Passa (698, 68662, 662 e 679 sinalizados com R1) |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica (não é anúncio) |

### 3.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| CP1 | Seção 2.5.2, linha 657, coluna "Checar" (linha 258) | "A1 (Anestesiologia e dor, 14 itens) está com zero campanhas ativas" contradiz as tabelas 1.2 e 1.5 do mesmo arquivo, onde 586 (Anestesiologia EAD) e 554 (Dor e Cuidados Paliativos) estão ativas. Os 14 itens são do recorte do plano; 586 e 554 ficam fora dele (turmas iniciadas, "verificar") | Escrever "A1 tem zero campanhas ativas entre os 14 itens do recorte; 586 e 554, fora do recorte por serem turmas iniciadas, seguem ativas (2.3)" |
| CP2 | Seção 2.6 (linha 273) | "68628, 68632 e 677/564 (iniciadas, com status 'verificar')" faz 68628 e 68632 parecerem iniciadas e "verificar". No catálogo, 68628 e 68632 estão "aberto", com início em 10/04/2027; só 677 (11/07/2026) e 564 (18/07/2026) são iniciadas e "verificar" | Escrever "68628 e 68632 (abertas, início em 10/04/2027) e 677 e 564 (iniciadas, status verificar)" |
| CP3 | Seção 0, item 5 (linha 28) e cabeçalho "Início (visão)" da tabela 1.2 (linha 47) | "Dias até o início são os da visão de campanhas" contraria a regra de fonte (datas da planilha, via catálogo) e o analista corrigido, que agora usa a data do catálogo. Nas 42 linhas de Pós as datas da visão e do catálogo coincidem (conferido), então nenhum número muda | Escrever "Dias até o início pela data do catálogo (planilha); nas 42 linhas de Pós a visão traz a mesma data" e trocar o cabeçalho para "Início (catálogo)" |

Recomendações (não bloqueiam):
- CP-R1. Seção 2.5.1, linha 666 (linha 247): a prova 68660 é de São Paulo e a 68623 é de Goiânia. Anotar a diferença de praça, como a tabela 1.5 faz para Cardiologia e Clínica Cirúrgica.
- CP-R2. Seção 1.1 (linha 40): "Pneumologia (código [CONFIRMAR])". Citar os dois candidatos, como o analista faz em 6.3: 670 (10/04/2027, encerrado) ou 68636 (17/04/2027).

**Veredito: CORRIGIR** (CP1 a CP3). Volta para o analise-de-campanha.

---

## 4. analise-de-campanha-livres-2026-10-26.md

### 4.1 Recontagem por amostragem (7 itens)

| # | Dado no arquivo (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 21 linhas de Livres: 3 ativas, 4 pausadas, 14 sem (1.1) | Visão: ativas linhas 48, 49, 50; pausadas 19 (592), 33 (99), 34 (68668), 71 (68618); as outras 14 sem campanha | Sim |
| 2 | 7 campanhas só estáticas; com 5 ângulos 573 e 68614 (1.4) | Visão, linhas 19, 33, 34, 48 a 50, 71 | Sim |
| 3 | Janelas de 4 a 8 semanas (1.3) | 14/11 menos 56 e 28 dias = 19/09 e 17/10; 29/11 = 04/10 e 01/11; 28/11 = 03/10 e 31/10; 18/12 = 23/10 e 20/11; 22/05/2027 = 27/03 e 24/04/2027 | Sim |
| 4 | 45 contínuos = 22 online e gravados + 13 minicursos + 2 espanhol + 8 grupos (2.5) | Catálogo, seções 5, 6 e 7, só "aberto (contínuo)" | Sim |
| 5 | 4 de 55 (7,3%) e 51 (92,7%) (1.1, H1) | 4 / 55 = 7,27%; 51 / 55 = 92,73% | Sim |
| 6 | Diferenças de 15, 20 e 155 dias (H3) | 14/11 a 29/11 = 15; 28/11 a 18/12 = 20; 18/12/2026 a 22/05/2027 = 155 | Sim |
| 7 | Preços e cargas: 573 (28 h, 2.350,00, 10x de 303,00), 623 (12 h, 890,00, 6x de 205,00), 68614 (12 h, 1.250,00, 10x de 175,00), 68618 (17 h, 1.710,00, 1x de 1.800,00), 68668 (48 h, 100,00), 616 (12 h, 990,00) | Catálogo, seções 4, 5 e 7 | Sim |

### 4.2 Auditoria 09-analytics, item por item

| Item | Resultado | Observação |
|---|---|---|
| Árvore de métricas existe e está atualizada | Passa | Usa a árvore de Livres do analista (5.2) |
| Toda métrica tem fonte nomeada | Passa | Meta Ads, Google Ads, GA4, loja, CRM, catálogo |
| Relatórios comparam com as metas | Não se aplica nesta rodada | Sem metas; o modelo exige |
| Metas não batidas com a mesma clareza | Não se aplica nesta rodada | |
| Insights terminam com uma ação | Passa | H1 a H10 com "como testar"; 4 pedidos |
| Lacunas de dados sinalizadas | Passa | |
| Backlog revisado todo mês | Não se aplica | 1.33 |
| CPL, custo por venda, conversão e receita por linha | Não se aplica nesta rodada | Arquivo só de Livres; nada estimado; tetos lógicos declarados como "não são metas" |
| Nenhum dado pessoal | Passa | |

### 4.3 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Nome, modalidade, CH, duração e turno batem com o catálogo | Passa (conferidos em 4.1) |
| Status "aberto" ou sem chamada | Passa (592, 99 e 68668 com status do catálogo; R2 proíbe chamada em curso sem data ou sem venda) |
| Modalidade clara e correta | Passa |
| Graduação: ato do catálogo | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Não se aplica |
| Curso livre: não confere diploma | Passa (seção 0, item 5) |
| Nota MEC com fonte | Passa (nenhuma) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa (nenhum) |
| Comparação com concorrente | Não se aplica |
| Preço com valor, parcelas e condições | Passa (à vista e cartão citados) |
| Bolsa e desconto com regra | Não se aplica |
| Urgência real | Passa (L3, R1 e pedido 4) |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Não se aplica |
| Menores | Não se aplica |
| Formulários | Não se aplica |
| WhatsApp e e-mail com consentimento | Não se aplica |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Passa |
| Página de destino entrega o prometido | Passa (L3 e R1; duplicidade 623 e 68637 sinalizada) |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica |

### 4.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| CL1 | Seção 1.3, parágrafo "Correção de referência" (linha 80) | Diz que o analista cita "V48, 21/10/26" na seção 4.4. A versão 2 do analista (linha 289) já cita "V40, comentário de 21/10/26". A nota afirma um erro que não existe mais e contradiz o arquivo do analista | Remover o parágrafo ou trocar por "Conferido: o analista cita V40, a linha de 623" |
| CL2 | Seção 0, item 3; tabela 1.3; linha 164 (623); linha 171 (68618); 3.1 (linha 198); H8 (linha 258) | A "janela de 4 a 8 semanas" não tem definição única. A tabela e a 3.1 a tratam como o período para ligar a campanha (de 8 a 4 semanas antes), e "se encerra em 5 dias" e "fim da janela de 623 (31/10)" podem ser lidos como data para pausar a 623 a 28 dias do curso. Para 68618, a linha 75 diz "pausada dentro da janela de 8 semanas (que abriu em 23/10)" e a linha 171 diz "a campanha está fora da janela atual". O contexto da linha fala em "campanha curta, de 4 a 8 semanas antes da data" (duração, [SUPOSIÇÃO]) | Definir no item 3 da seção 0: "janela de início: ligar a campanha entre 8 e 4 semanas antes da data; uma vez ligada, ela segue até a data ou até lotar (R6)". Trocar "fim da janela de 623" por "fim da janela de início de 623" (3.1 e H8) e, na linha 171, escrever "se for 18/12/2026, a campanha está pausada dentro da janela de início (23/10 a 20/11)" |

**Veredito: CORRIGIR** (CL1 e CL2). Volta para o analise-de-campanha.

---

## 5. analise-de-campanha-eventos-2026-10-26.md

### 5.1 Recontagem por amostragem (6 itens)

| # | Dado no arquivo (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | 4 linhas de Eventos: 2 ativas, 0 pausadas, 2 sem (1.1) | Visão: V28 (linha 36, sem), V36 (linha 44, ativa), V66 (linha 74, sem), V67 (linha 75, ativa) | Sim |
| 2 | Somas das três linhas batem com o total (1.5; arquivos irmãos) | Ativas 14 + 3 + 2 = 19; pausadas 18 + 4 + 0 = 22; sem 10 + 14 + 2 = 26; só estático 21 + 7 + 2 = 30; sem 5 ou só estático 25 + 7 + 2 = 34 | Sim |
| 3 | Dados do workshop: 16 h, 30 vagas, R$ 1.250,00, R$ 450,00 (68634), cupom de 20%, Av. Tiradentes, 960 (1.2) | Catálogo, seção 9 | Sim |
| 4 | Contas: 30 x 1.250,00 = 37.500,00; 30 x 1.000,00 = 30.000,00; 450,00 com 20% = 360,00 (1.2) | Conferidas | Sim |
| 5 | Dias do calendário até 20/11: 23, 18, 11, 4, 1, -3, -10 (3.1) | Conferidos a partir de 28/10, 02/11, 09/11, 16/11, 19/11, 23/11, 30/11 | Sim |
| 6 | 700: R$ 780,00 ou 10x de R$ 98,00; 202: R$ 285,00 ou 6x de R$ 78,00; nome do JSON "eventos-simposio-neuromonitorizacao-2026-11-20"; área A12 (68654, 68616, 466) | Catálogo, seção 9; plano, 6.2 e 2.3 | Sim |

### 5.2 Auditoria 09-analytics, item por item

| Item | Resultado | Observação |
|---|---|---|
| Árvore de métricas existe e está atualizada | Passa | Usa a árvore de Eventos do analista (5.3) |
| Toda métrica tem fonte nomeada | Passa | Meta Ads, Google Ads, GA4, loja, CRM, catálogo, planilha do kit |
| Relatórios comparam com as metas | Não se aplica nesta rodada | Sem metas; o modelo exige |
| Metas não batidas com a mesma clareza | Não se aplica nesta rodada | |
| Insights terminam com uma ação | Passa | H1 a H10 com "como testar"; 5 pedidos |
| Lacunas de dados sinalizadas | Passa | |
| Backlog revisado todo mês | Não se aplica | 1.33 |
| Custo por inscrição e receita por linha | Não se aplica nesta rodada | Arquivo só de Eventos; nada estimado |
| Nenhum dado pessoal | Passa | Nenhum nome de docente ou palestrante |

### 5.3 Conformidade educacional, item por item

| Bloco e item | Resultado |
|---|---|
| Nome, data, CH e local batem com o catálogo | Passa (nome oficial, 20/11/2026, 16 h, endereço) |
| Status "aberto" ou sem chamada | Passa com ressalva (CE-R2: o 68634 está "verificar" no catálogo) |
| Modalidade clara e correta | Passa (presencial e transmitido separados) |
| Graduação: ato do catálogo | Não se aplica |
| Pós lato sensu sem "reconhecida pelo MEC" | Não se aplica |
| Curso livre ou evento: sem afirmação de certificação | Passa (seção 0, item 5; certificado de participação [CONFIRMAR]) |
| Nota MEC com fonte | Passa (nenhuma) |
| Sem promessa de emprego, salário ou sucesso | Passa |
| Empregabilidade com fonte | Não se aplica |
| Superlativos com fonte | Passa (nenhum) |
| Comparação com concorrente | Não se aplica |
| Preço com valor, parcelas e condições | Passa (iguais ao catálogo) |
| Bolsa e desconto com regra, público e prazo | Passa (cupom com público do catálogo; modalidade e período [CONFIRMAR]) |
| Urgência real | Passa (E10 e R1 exigem número real de vagas restantes) |
| Prouni, Fies | Não se aplica |
| Autorização de imagem e voz | Passa (só docentes confirmados e com autorização [CONFIRMAR]) |
| Menores | Não se aplica |
| Formulários | Não se aplica |
| WhatsApp e e-mail com consentimento | Passa (mensagens de véspera são textos para o CRM; ninguém dispara pela squad) |
| Nenhum dado pessoal | Passa |
| Políticas Meta e Google | Passa |
| Página de destino entrega o prometido | Passa (neuro-summit como destino; risco da V67 sinalizado em H7 e no pedido 3) |
| Bloco "Anúncios (Meta e Google)", 6 itens | Não se aplica |

### 5.4 Problemas e correções

| # | Local | Problema | Correção proposta |
|---|---|---|---|
| CE1 | Seção 1.3, primeiro achado (linha 88) e Fatos, 7º item (linha 274) | Diz que "a planilha marca essa linha 'sem página'" e dá como fonte "visão e catálogo". A visão de campanhas não tem essa informação. Quem marca a linha "Paciente Grave Multidiciplinar" como "sem página" e "só na planilha" é o catálogo, seção 9, como a própria tabela 1.1 (linha 40) diz | Linha 88: "o catálogo (seção 9) marca essa linha 'sem página', 'só na planilha'". Fato: "A linha 'Paciente Grave Multidiciplinar' tem data de 15/11/2027 e campanha ativa na visão e está 'sem página' no catálogo, seção 9" |

Recomendações (não bloqueiam):
- CE-R1. Seção 1.2, contas (linha 67): "receita líquida da inscrição (R$ 1.250,00 ou R$ 1.000,00...)" usa valores brutos. Escrever "receita bruta da inscrição; a líquida, depois de taxas, é [CONFIRMAR]".
- CE-R2. Seção 1.2: registrar que o produto 68634 está com status "verificar (sem data no site)" no catálogo, além da carga de 24 h (P9).
- CE-R3. Seção 1.2, "Data e local": o briefing fala em "20 e 21/11/2026"; o catálogo dá o início em 20/11/2026. Escrever "início em 20/11/2026 (catálogo); 20 e 21/11 pelo briefing", para alinhar com o analise-de-funil de Livres, que usa "20 e 21/11/2026".

**Veredito: CORRIGIR** (CE1). Volta para o analise-de-campanha.

---

## 6. analista-de-dados-geral-2026-10-26.md (reconferência dos itens A1 a A4)

### 6.1 Situação de cada item

| Item | Pedido do QA anterior | O que a versão 2 traz | Resolvido? |
|---|---|---|---|
| A1 | Trocar "42" por "43" na soma de A1, A7, A10, A13 e A14 | Linha 194: "43 itens somados: 14 + 10 + 4 + 6 + 9"; Fatos, linha 514: "somam 43 itens" | **Sim** |
| A2 | "100% em até 60 dias ativas" valia só pela visão | O arquivo passou a usar a data do catálogo em tudo ("Como contei", linha 34). Pergunta 1 refeita: 0 a 30 dias com 5 linhas e 5 ativas, 31 a 60 com 6 linhas, 5 ativas e 1 pausada (68618); mais de 180 com 10. Insight (linha 61) e fato (linha 510): "10 de 11 ativas" | **Sim** (solução melhor que a proposta: segue a regra de fonte) |
| A3 | Tirar 573 da lista "33 dias ou mais" | Pergunta 4, ação (linha 145) e seção 3, ação 3 (linha 216): lista "68610, 68614 e 623"; 573 fora, com "19 dias pelo catálogo (34 pela visão) [CONFIRMAR data, P6]" | **Sim** |
| A4 | Citar o segundo candidato da V67 e a consequência | 6.3 (linha 466) com as hipóteses 1 e 2; ressalva da pergunta 5 (linha 200) com as contagens alternativas; 6.1 (linha 425); ação 2 (linha 215); 4.4 (linha 290); "Dados que faltam" (linha 534) | **Sim** |

R1 (promoção da 341, linha 86) e R2 (itens da seção 7 com "não se aplica nesta rodada" e o motivo) também foram atendidos.

### 6.2 Recontagem dos números novos ou alterados (6 itens)

| # | Dado (onde) | Recontagem | Bate? |
|---|---|---|---|
| 1 | Faixas pela data do catálogo: 32, 5, 6, 14, 10 = 67 (pergunta 1) | 573 sai de 31 a 60 e entra de 0 a 30; 68618 sai de mais de 180 e entra de 31 a 60; nenhuma linha iniciada muda de faixa (599, 717, 718, 716, 433, 625 e 68668 continuam no passado) | Sim |
| 2 | Ativas por faixa 6, 5, 5, 2, 1; pausadas 9, 0, 1, 8, 4 | Somas 19 e 22 | Sim |
| 3 | 31,6%, 52,6% e 15,8% das 19 ativas (pergunta 1) | 6 / 19, 10 / 19, 3 / 19 | Sim |
| 4 | Cruzamento das 19 ativas (pergunta 4) | 5 + 8 + 4 + 2 = 19; listas conferidas na visão | Sim |
| 5 | Contagens alternativas da V67: 12 ativas, 33 na visão, 77 não constam | 13 menos 1; 34 menos 1; 110 menos 33 | Sim |
| 6 | V26 (68668): -7 pelo catálogo (visão: -25) | 19/10 a 26/10 = 7 | Sim |

### 6.3 Auditorias (só sobre as mudanças)

- Auditoria 09-analytics: sem mudança de resultado em relação ao QA anterior; "Lacunas de dados sinalizadas" agora passa sem ressalva (V67 incluída).
- Conformidade educacional: o item "Página de destino entrega o prometido" deixa de ter ressalva, porque a V67 está sinalizada como risco e pedida à Ufape. Demais itens como no QA anterior (passa ou não se aplica).
- Checagens: nenhum travessão, meia-risca, dado pessoal ou frase ligada ao MEC nas partes alteradas.

**Veredito: APROVADO nos itens A1 a A4.** Segue para a aprovação humana.

---

## 7. Contradições entre os arquivos

| # | Arquivos | Contradição | Tratamento |
|---|---|---|---|
| X1 | analise-de-funil-livres (1.2) e analise-de-campanha-livres (2.5) | 616 "online gravado, sem data" num e item com data e janela no outro | FL1 |
| X2 | analise-de-campanha-livres (1.3, linha 80) e analista-de-dados (4.4) | Nota diz que o analista cita V48; o analista cita V40 | CL1 |
| X3 | analise-de-campanha-pos (0.5) e analista-de-dados (seção 0) | Dias "da visão" contra dias "pelo catálogo" (sem efeito nos números da Pós) | CP3 |
| X4 | analise-de-funil-livres (cabeçalho) e analise-de-campanha-eventos (1.2) | "20 e 21/11/2026" contra "20/11/2026" | Não é erro (início no catálogo, duração no briefing); recomendação CE-R3 |

Nenhuma contradição nos totais: as três análises de campanha somam 67 linhas, 19 ativas, 22 pausadas, 26 sem campanha, 30 só estáticas e 34 sem 5 ângulos ou só estáticas, iguais ao analista.

---

## Fatos (com fonte)

- A visão tem 42 linhas de Pós (14 ativas, 18 pausadas, 10 sem), 21 de Livres (3, 4, 14) e 4 de Eventos (2, 0, 2) (docs/visao-de-campanhas-2026-10-26.md, recontagem linha a linha).
- Nas 42 linhas de Pós, a data da visão é igual à do catálogo; as 10 divergências são todas de Livres (catálogo, seções 2 e 4; visão).
- O 616 tem início em 05/12/2026, local "Presencial e Online", modalidade "On-line", 12 h e R$ 990,00 à vista (catálogo, seção 5); o plano o conta como "Online com data" (cmo, 2.2).
- 68628 e 68632 estão "aberto", com início em 10/04/2027; 677 e 564 estão "verificar (turma já iniciada e com venda)" (catálogo, seção 2).
- 586 (Anestesiologia EAD) e 554 (Dor e Cuidados Paliativos) estão com campanha ativa e fora do recorte do plano (visão, linhas 27 e 28; cmo, 2.1 e 2.4).
- A linha "Paciente Grave Multidiciplinar Foco em casos Clinicos" está "sem página" e "só na planilha" no catálogo, seção 9; a visão não tem essa informação.
- O analista-de-dados, versão 2, cita "V40, comentário de 21/10/26" na seção 4.4 (analista, linha 289).
- O catálogo tem 13 minicursos contínuos; 12 de 8 h e o 669 de 6 h (catálogo, seção 5).
- As 22 provas de 27/11/2026 estão abertas; a 68656 está encerrada; 13 provas antigas estão sem venda (catálogo, seção 3).
- Prazos do plano: decisão A4 em 28/10; plano das provas em 29/10; peças das provas e de 68614, 623 e 68637 em 03/11; peças de 573 em 30/10; kit leve dos grupos em 28/10 e 06/11 (cmo, seção 4).

## Suposições

- [SUPOSIÇÃO] A numeração V1 a V67 começa na linha 9 do arquivo da visão, como no analista e no QA anterior.
- [SUPOSIÇÃO] A janela de 4 a 8 semanas do contexto de Livres descreve a duração da campanha (começa entre 8 e 4 semanas antes e vai até a data); a correção CL2 pede só que o arquivo escolha uma definição e a use em todo lugar.
- [SUPOSIÇÃO] As frases "frase de certificação ligada ao MEC" usadas nos arquivos de Pós descrevem a pendência P2 sem repetir a frase do site e por isso não bloqueiam.
- [SUPOSIÇÃO] Os dados citados a partir do analise-cro e dos insights (por exemplo, "??" na página de 68610, 120 dias de acesso do 411, 17 de 23 aulas do 713) foram tirados das fichas; o QA não abriu esses arquivos nem as fichas.

## Dados que faltam

- [CONFIRMAR] Data única de 573, 68614 e 68618 (P6) e a página que fica à venda entre 623 e 68637 (P7).
- [CONFIRMAR] Para onde leva a campanha ativa da V67: produto 700 ou a linha "Paciente Grave" sem página.
- [CONFIRMAR] Turma de destino de cada prova de bolsa e qual mínimo vale (15 ou 20).
- [CONFIRMAR] Se o cupom SIMPNEUROMONIT vale para o transmitido (68634) e o status de venda do 68634 ("verificar" no catálogo).
- [CONFIRMAR] Definição da janela de campanha dos Livres presenciais (contexto marcado como [SUPOSIÇÃO]).
- [CONFIRMAR] Todos os números de funil e de campanha (leads, verba, gasto, inscrições, matrículas, vagas restantes): nenhum existe hoje.
- [CONFIRMAR] Quem aprova cada tipo de peça (contexto/ufape-geral.md, tabela vazia; P12). Até lá, a aprovação vai à pessoa do marketing que fez o pedido.
- Não conferido nesta revisão: fichas de curso e as saídas analise-cro-pos, analise-cro-livres e insights-de-alunos-pos, usadas como evidência pelos funis.
