# QA de marketing: camada 2 da Pós-graduação (A1 a A14)

- **Agente:** qa-de-marketing (departamento 10, Operações de Marketing)
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Revisão:** camada 2, quatro arquivos (sufixo -camada2, regra de nomes da revisão do qa em docs/execucao-2026-10-26.md)
- **Arquivos revisados (inteiros, sem edição):**
  - saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (701 linhas)
  - saidas/05-social-e-comunidade/criador-de-ganchos-pos-2026-10-26.md (628 linhas)
  - saidas/05-social-e-comunidade/autoridade-docente-pos-2026-10-26.md (754 linhas)
  - saidas/06-geracao-de-demanda/iscas-digitais-pos-2026-10-26.md (591 linhas)
- **Entradas lidas:** CLAUDE.md; docs/execucao-2026-10-26.md (decisões 1 a 17); saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 7, 8, 12 e 13: P3, D1, D2, D3, D5, D11, D12, D16, E1 a E4, regra de serviço de 13.3); contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (inteiro); auditorias/conformidade-educacional.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/05-social.md; auditorias/06-geracao-de-demanda.md; fichas em contexto/cursos/pos/ conferidas linha a linha: 707, 68610, 68617, 68606, 68623 (dados principais e local), 657, 382, 68628, 68608, 699 (dados principais), 60 (dados principais), 68632, 289, 68616.
- **Método:** cada arquivo contra o brief da etapa (seção 2.3 e camada 2 do plano do cmo), a voz da marca, as decisões 1 a 17, o catálogo e as fichas; conformidade educacional item por item; auditoria do departamento de cada arquivo; coerência entre os quatro arquivos (mesmas turmas por área, mesmos bloqueios).
- **Status:** rascunho de QA. Nada foi publicado, enviado ou pago. Nenhum arquivo revisado foi alterado: as correções voltam para os agentes donos.

---

## 1. Vereditos

| Arquivo | Veredito | Motivo principal | Obrigatórias | Ajustes |
|---|---|---|---|---|
| mensagens-pos | **CORRIGIR** | Texto-padrão de preço cita a matrícula (R$ 250,00 e R$ 350,00), que a decisão 16 suspende até a U11; turma mínima de 15 em peça que leva a páginas que ainda dizem 20; 679 e 68636 "liberadas" com preço e data, contra o P3 do cmo | 3 | 7 |
| criador-de-ganchos-pos | **CORRIGIR** | 22 ganchos de preço (ângulo CON e o A12-05) usam o texto-padrão com a matrícula (decisão 16), 3 deles entre os recomendados; ganchos TUR com "15" e destino com "20"; 679 e 68636 com data e preço (P3) | 3 | 8 |
| autoridade-docente-pos | **CORRIGIR** | AD-A2-1 promete "6 módulos presenciais de prática hands-on de ecocardiograma" (a ficha de 289 sustenta 4); data de vencimento da 1ª mensalidade errada para 68606 e dada como passada para 68610 e 68608; AD-A14-1 com data de 679 (P3) | 3 | 5 |
| iscas-digitais-pos | **CORRIGIR** | E-mail D6 usa o texto-padrão com matrícula e turma mínima de 15, contra a regra do próprio arquivo e a decisão 16; dias sem campanha diferentes do D1; ponte de 679 e 68636 com data (P3) | 4 | 6 |

Todos os quatro voltam para o agente que os produziu. Nenhum segue para a aprovação humana nesta versão.

---

## 2. Bloqueios transversais (valem para mais de um arquivo)

**T1. Valor da matrícula (decisão 16).** A decisão 16 diz que o site mostra "matrícula R$ 250,00" (e R$ 350,00 em 3 cursos), que a inscrição informada pelo CEO é R$ 260,00, que a diferença fica [CONFIRMAR U11] e que "nenhuma peça cita o valor da inscrição até a resposta". O valor que o catálogo chama de matrícula é esse valor. Como a conformidade exige preço com condições completas, sem esconder a matrícula, a única saída válida até a U11 é **peça sem preço**, com a chamada "Veja parcelas, total e matrícula na página da turma". Atinge: mensagens (regra 3 e tabelas), ganchos (G1 e todos os CON), iscas (e-mail D6). Autoridade-docente já não cita preço: passa.

**T2. Turma mínima de 15 contra páginas que dizem 20.** A decisão 11 fixa 15 também na Pós, mas as fichas de 707, 68610, 68617, 68608, 68628, 68632, 289 e 657 (conferidas) ainda mostram 20 ou "Mínimo 20" na página. Peça com "turma mínima de 15" que leva a uma página com "20" falha o item "página de destino entrega exatamente o que a mensagem prometeu". Regra única proposta (é a da iscas, 1.1 item 7): o número 15 só aparece quando a página da turma já mostrar 15 (hoje 60 e 699); nas demais, a frase sai sem número ("a turma pode não ser formada; compre passagem e hotel só com a turma confirmada") até a Ufape corrigir as páginas (pedido A12 do cmo). Atinge: mensagens, ganchos, regra 7 da autoridade e o e-mail D6 da iscas.

**T3. P3 do cmo para 679 e 68636.** O P3 (seção 7 do plano) lista 662, 679, 68641, 68642 e 68636 e manda: "Nenhuma peça com preço ou data desses itens até a correção". Os quatro arquivos tratam 662 corretamente (só nome, campus e data da planilha, decisão 12), mas tratam 679 como "liberada, conferir o link antes de anúncio" e 68636 como "liberada" ou "data [CONFIRMAR com a planilha]", com preço ou data em peça. Até a correção (A12) ou uma liberação expressa do cmo, 679 e 68636 ficam sem preço e sem data de início em peça final.

**T4. Teto e calendário de envio.** A decisão 17 e a seção 13 do plano trocaram o D1 pelo D16 (número igual para a Pós: até 2 WhatsApp e 2 e-mails de campanha por semana, 1 por dia) e acrescentaram E1 (até 1 WhatsApp por semana para quem não engaja), E2 (erro 131049), E3 (descadastro em até 48 h) e E4 (opt-in por categoria). Os dias sem campanha do D1 seguem: 02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço. Ganchos e iscas ainda citam o "teto D1"; a iscas tem o calendário errado.

**T5. Dados de cronograma que a ficha já responde.** Três arquivos deixam [CONFIRMAR] onde a ficha tem o dado, e um afirma além da ficha:
- 68617 tem **2** módulos presenciais: módulo 12 (18 e 19/03/2028: atendimento endocrinológico, anatomia do sistema endócrino, discussão de casos) e módulo 23 (fevereiro de 2029: atendimento endócrino, US abdominal, cirurgia do sistema endócrino, discussão de casos dos alunos).
- 68606 tem 3 presenciais com data ou mês: módulo 6 (17 e 18/04/2027), módulo 13 (27 e 28/11/2027: **endoscopia**, parasitologia ou transplante fecal, prova 2) e módulo 21 (julho de 2028: videocirurgia, cirurgia pancreática e hepatobiliar, colocação de sondas, atendimento clínico, prova 3).
- 289 tem 6 presenciais (módulos 6, 9, 13, 16, 19 e 24): 4 com prática de ecocardiograma (9, 13, 16 e 19), o módulo 6 sem tema na ficha e o 24 com "aula prática e prova final".
- 657 tem 6 presenciais (7, 8, 11, 13, 15 e 18), não só os dois citados.
- 68608: o terceiro presencial é o módulo 22 (agosto de 2028: farmacologia e prova escrita).
- 68610: o módulo 24 presencial traz crioterapia e dermatohistopatologia na prática clínica.

---

## 3. Detalhes por arquivo

### 3.1 mensagens-pos (CORRIGIR)

| # | Tipo | Linha | Problema | Correção |
|---|---|---|---|---|
| M1 | Obrigatória (T1) | 31 (regra 3); tabelas de turmas nas linhas 112 a 114, 155 a 158, 199 e 200, 241 a 244, 284 e 285, 324, 363, 402, 441, 480, 520 a 522, 561, 583, 593, 603, 613, 623 e 633; respostas das linhas 60 e 426 | O texto-padrão de peça inclui "mais matrícula de R$ [matrícula]" (R$ 250,00 ou R$ 350,00), valor suspenso pela decisão 16 até a U11. O arquivo leu só as decisões 1 a 14 (linha 11) | Regra 3 passa a "sem preço em peça até a resposta da U11: a peça leva à página da turma, onde estão parcelas, total e matrícula". As tabelas podem ficar como referência interna, com a nota "não usar em peça até a U11". Na linha 426 (707), a resposta fica "O valor completo está na página da turma", sem o texto-padrão |
| M2 | Obrigatória (T2) | 31, 54 (pilar 3), 62, 649 | "Turma mínima de 15 alunos" em peça, com destino em páginas que ainda dizem 20 | Aplicar a regra única de T2: o 15 só onde a página da turma já mostra 15 (60 e 699); nas demais, frase sem número até a correção das páginas |
| M3 | Obrigatória (T3) | 157 (68636 "liberada"); 583 (679, com preço e data) | Contraria o P3 do cmo (sem preço nem data até a correção) | Coluna "Para peça": "sem preço e sem data de início em peça final até a correção (A12) ou liberação do cmo" |
| M4 | Ajuste | 11 | Entradas citam só as decisões 1 a 14 | Ler e citar as decisões 15 a 17 (preço da inscrição, meta, teto D16) |
| M5 | Ajuste | 348 | "porque o raciocínio endócrino depende dela" é tese pedagógica dita como fato | Marcar [SUPOSIÇÃO] e [REVISÃO DOCENTE], como o criador-de-ganchos já fez no A7-01 |
| M6 | Ajuste | 184 | "A-fast, T-fast, punção guiada e RCP se aprendem com a mão no paciente e no equipamento" mistura as duas turmas (punção guiada é de 68623, bloqueada pelo local) e afirma prática em paciente sem a ficha dizer | Marcar [SUPOSIÇÃO de texto] e citar só os presenciais de 68635 como estão na ficha |
| M7 | Ajuste (T5) | 341, 349, 699 | 68617 com "número exato de módulos presenciais [CONFIRMAR NO CATÁLOGO]" | A ficha traz 2 (módulos 12 e 23); usar o dado |
| M8 | Ajuste (T5) | 302, 310, 695 | 68606: endoscopia prática e datas dos presenciais como [CONFIRMAR]; estágio parafraseado como "nas clínicas e hospitais dos coordenadores" | Usar os módulos 6, 13 e 21 da ficha; citar o estágio literal da página ("Estágios com a cooperação em suas clínicas/hospitais") e manter as regras do estágio [CONFIRMAR] |
| M9 | Ajuste (T5) | 131 | 289: "6 módulos presenciais, com prática hands-on de ecocardiograma" lê como se os 6 fossem de ecocardiograma | "6 módulos presenciais, 4 deles com prática de ecocardiograma" |
| M10 | Ajuste (T5) | 88 | 657: só dois presenciais citados | Escrever "entre os 6 módulos presenciais" |

O que passa: nome "Pós-graduação em <área>" em todo título; sem MEC, certificação ou "dupla certificação" (linhas 34, 186, 228, 391, 469); sem urgência (regra 7); descontos fora (regra 5); provas de bolsa só como fato (regra 9); voz do candidato marcada [SUPOSIÇÃO]; docentes com a grafia das fichas conferidas (707, 68610, 68617, 68608, 68628, 382, 289, 657); datas de início iguais ao catálogo; 662, 699, 719, 68623 e 333 com o bloqueio certo.

### 3.2 criador-de-ganchos-pos (CORRIGIR)

| # | Tipo | Linha | Problema | Correção |
|---|---|---|---|---|
| G1 | Obrigatória (T1) | 65 (regra G1); ganchos A1-07, A2-05, A3-04, A3-10, A4-05, A5-06, A6-06, A7-05, A8-06, A9-04, A9-08, A10-05, A11-07, A11-09, A12-06, 341-04, 382-04, 60-04, 679-05, 699-06, 719-04 (linhas 122, 146, 171, 177, 198, 225, 251, 276, 303, 327, 331, 354, 382, 384, 407, 519, 475, 541, 454, 499, 563) e A12-05 (linha 406, "Link da página e G1") | Todos fecham com "matrícula de R$ 250,00" ou "R$ 350,00", suspenso pela decisão 16. O arquivo leu as decisões 1 a 17 e não aplicou a 16 | Marcar os 22 como BLOQUEADO até a U11 ou reescrever o corpo para "parcelas, total e matrícula na página da turma", sem valor. Trocar os recomendados afetados: A1-07 (sugestão: A1-08), A3-04 (sugestão: A3-05) e A11-09 (sugestão: A11-05 ou A11-01) |
| G2 | Obrigatória (T2) | 65 (G1); ganchos TUR e de preço com "turma mínima de 15": A1-06, A2-04, A3-08, A3-10, A4-06, A5-09, A7-09, A10-08, A12-10, 341-10, 382-07, 382-10 | Destino em páginas que ainda dizem 20 | Regra única de T2. 60-07 e 699-10 já seguem a página (15) e passam |
| G3 | Obrigatória (T3) | 136, 138 e A2-05 (68636); 446 e 679-01 a 679-10 (679, com datas; 679-09, 679-01 e 679-04 são recomendados) | Contraria o P3 | 68636 e 679: sem data de início e sem preço em peça final; marcar os ganchos de 679 e o A2-05 como BLOQUEADO para publicação até a correção (A12) ou liberação do cmo |
| G4 | Ajuste (T4) | 54 (0.3) e 597 (Lista 1) | Cita o "teto D1" | Trocar por D16 (seção 13) com E1 a E4 e os dias sem campanha do D1 |
| G5 | Ajuste | 142 (A2-01) | "eletrocardiograma, farmacologia e ecocardiograma nos módulos práticos" de 289: eletrocardiograma e farmacologia estão em módulos online (2, 4, 5 e 7) | "ecocardiograma nos módulos práticos" |
| G6 | Ajuste | 325 (A9-02) | Última data "29/09 e 01/10/2028" | "29 e 30/09 e 01/10/2028" (ficha 707, módulo 24). A contagem de 10 presenciais confere |
| G7 | Ajuste (T5) | 268, 273, 279 | 68617: mês e dia do módulo 12 e número de presenciais como [CONFIRMAR NO CATÁLOGO] | Módulo 12 em 18 e 19/03/2028; 2 presenciais (12 e 23) |
| G8 | Ajuste (T5) | 242, 248, 252, 255 | 68606: demais presenciais e endoscopia como [CONFIRMAR] | Módulos 13 (27 e 28/11/2027, com endoscopia) e 21 (julho de 2028) estão na ficha |
| G9 | Ajuste (T5) | 298 (A8-01) | Conteúdo do módulo 24 de 68610 como [CONFIRMAR NO CATÁLOGO] | Crioterapia e dermatohistopatologia na prática clínica (ficha) |
| G10 | Ajuste (T5) | 380 (A11-05) | Terceiro presencial de 68608 como [CONFIRMAR NO CATÁLOGO] | Módulo 22, agosto de 2028: farmacologia e prova escrita |
| G11 | Ajuste | 529 | Justificativa do 341-02 fala em "equinocultor"; o público da ficha é médico veterinário | "médico veterinário de equinos" |

Ganchos cumpridos pelo corpo (amostra conferida na ficha): A1-02, A1-04, A1-08, A1-09 (657 e 68609); A2-03, A2-09, A2-10 (289); A4-02, A4-04 (68632 e 578); A6-02, A6-03, A6-07, A6-09 (68606); A7-01, A7-03, A7-10 (68617); A8-02, A8-04, A8-07, A8-08, A8-09 (68610: 17 online e 7 presenciais confere); A9-01, A9-06, A9-10 (707); A10-01, A10-03, A10-06, A10-07, A10-09 (68628: 8 presenciais confere); A11-05 (68608); A12-01, A12-02, A12-04, A12-08, A12-09 (68616); 382-01, 382-02, 382-03, 382-07, 382-08 (382: 8 presenciais, de agosto de 2027 a fevereiro de 2029, confere). Nenhum gancho traz caso de paciente, dose ou conduta; o único CAS (A7-07) está BLOQUEADO até haver revisor docente. Sem MEC, certificação, desconto, prova de bolsa ou urgência.

### 3.3 autoridade-docente-pos (CORRIGIR)

| # | Tipo | Linha | Problema | Correção |
|---|---|---|---|---|
| D1 | Obrigatória | 189 e 201 (AD-A2-1) | "com 6 módulos presenciais de prática hands-on de ecocardiograma": a ficha de 289 sustenta 4 (9, 13, 16 e 19); o módulo 6 não tem tema e o 24 é "aula prática e prova final". Promessa de prática além da página de destino | "São 24 módulos e 500 horas, com 6 módulos presenciais, 4 deles de prática de ecocardiograma." |
| D2 | Obrigatória | 353 (68606); 409 (68610); 510 (68608) | 68606: "a 1ª mensalidade venceu em 29/10" está errado; com início em 07/11/2026, ela venceu em 08/10/2026 (30 dias antes, ficha). 68610 e 68608: "venceu em 29/10" e "vencida em 29/10" num arquivo de 26/10 | 68606: "1ª mensalidade vencida (prazo de 08/10/2026)". 68610 e 68608: "a 1ª mensalidade vence em 29/10/2026; a partir daí, só 'Fale com o time'" |
| D3 | Obrigatória (T3) | 595 (AD-A14-1, "início em 03/04/2027") | Data de 679 em post, contra o P3 | Tirar a data até a correção (A12) ou liberação do cmo; o AD-A2-3 (linha 218) já condiciona a data de 68636 e passa |
| D4 | Ajuste (T5) | 386 e 398 (AD-A7-1); 84 | A base mistura os dois presenciais de 68617 num só ("um módulo presencial com atendimento, ultrassom abdominal, cirurgia"); o post diz "um módulo presencial". "Dr. Eric Vieira" aparece também na própria ficha 68617 | "dois módulos presenciais (12 e 23), com atendimento endocrinológico e discussão de casos"; incluir 68617 na lista da linha 84 |
| D5 | Ajuste (T5) | 149 (AD-A1-1) | 657 tem 6 presenciais; o post cita dois como se fossem todos | "Entre os módulos presenciais estão bloqueios locorregionais com prática guiada e hemodinâmica avançada com ventilação mecânica em prática aplicada." |
| D6 | Ajuste | 357 e 359 | A tese cita prática "endoscópica" e o "Não dizer" proíbe endoscopia [CONFIRMAR]; a ficha traz endoscopia no módulo 13 presencial | Alinhar: pode citar endoscopia como tema do módulo 13 presencial, sem prometer volume |
| D7 | Ajuste (T2) | 35 (regra 7) | "Se um post citar, é de 15" | Regra única de T2 (hoje nenhum post cita o número, então nada muda nos textos) |
| D8 | Ajuste (T4) | 708 | "teto de mensagens (D1)" | D16 e E1 a E4 |

O que passa: toda tese leva [PONTO DE VISTA A CONFIRMAR COM O DOCENTE] e nenhuma atribui ao docente fato clínico, dose, número ou resultado; nenhum post cita preço, desconto, bolsa ou certificação; cada post cita só o próprio autor; nome e titulação conferidos nas fichas de 707, 68610, 68617, 68608, 68628, 382, 289 e 657 (inclusive "MSC. Juliana Jorge" na lista de 707, "Dra. Marilu Martins Gioso." com ponto em 382 e "MSc Esp. Juliana V Cirillo" em 68608); autorização de imagem e citação pelas decisões 8 e 10, com o ok do docente para texto em primeira pessoa; encaixe no teto D5 (6 slots de feed já previstos, sem feed em 02/11, 20 e 21/11, 25/12 e 01/01; dias da semana conferidos); UTM no padrão D11 e D12, com linkedin e pos_conteudo marcados [SUPOSIÇÃO]; 662, 699, 719, 68623 e 333 com o bloqueio certo.

### 3.4 iscas-digitais-pos (CORRIGIR)

| # | Tipo | Linha | Problema | Correção |
|---|---|---|---|---|
| I1 | Obrigatória (T1) | 151 (e-mail D6) | "Texto-padrão de preço da estrategia-de-oferta-pos" inclui a matrícula, contra a decisão 16 e contra a própria regra da linha 42 ("Valor da inscrição não é citado até a U11") | E-mail D6 sem preço até a U11: "Veja parcelas, total e matrícula na página da turma" |
| I2 | Obrigatória (T2) | 151 contra 45 | O texto-padrão traz "Turma mínima de 15 alunos" e a regra 1.1, item 7, manda citar 15 só onde a página já diz 15 | O e-mail D6 segue a 1.1, item 7. A regra da iscas é a proposta de regra única (T2) |
| I3 | Obrigatória (T4) | 132 | "dias sem campanha (20 e 21/11; de 25/12 a 03/01 só serviço)" diverge do D1: faltam 02/11 e o período de só serviço começa em 21/12 | "02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço e manutenção" |
| I4 | Obrigatória (T3) | 240 (68636) e 469 (679) | Ponte com data de início | Sem data e sem preço até a correção (A12) ou liberação do cmo; ponte de 679 só depois de conferido o destino |
| I5 | Ajuste (T4) | 103, 130, 509, 554, 579 | Cita o "teto D1" | D16 com E1 a E4. A regra de serviço da 13.3 (mensagem por algo que a pessoa pediu) apoia o e-mail de entrega como serviço; manter a confirmação do encarregado (IR4, NPR5) |
| I6 | Ajuste | 132 contra 143 e 149 | A 1.7 diz que o lead criado de 27/10 a 29/11 recebe só a entrega; a 1.8 manda o WhatsApp no 2º dia e o e-mail no 6º dia sem essa ressalva | Escrever na 1.8 que os toques do 2º e do 6º dia só rodam para lead criado a partir de 30/11, salvo resposta diferente à U-I1 |
| I7 | Ajuste | 350 e 352 (A8, reservada) | "Compare os três formatos de pós em dermatologia" compara com EAD que a Ufape não oferece (comparação implícita com terceiros) e usa "pós em" | "Pós-graduação em Dermatologia Veterinária: o cronograma dos 7 módulos presenciais"; tirar a comparação de formatos |
| I8 | Ajuste | 205, 227, 397, 440 | Títulos com "Pós" como substantivo ("as três Pós-graduações", "as Pós da Ufape") | Subtítulo ou primeira linha com o nome completo de cada turma ("Pós-graduação em <área>") |
| I9 | Ajuste (T5) | 332, 344 (68617); 319 (68606) | Presenciais de 68617 e endoscopia de 68606 como [CONFIRMAR] | Usar a ficha (T5) |
| I10 | Ajuste | 99 | A caixa 1 junta avisos da área e a newsletter. É a mesma categoria (campanha) e cabe na E4 | Manter, mas levar essa leitura ao jurídico junto do IR3 |

LGPD conferida e aprovada no desenho: formulário só com e-mail obrigatório; duas caixas desmarcadas e separadas por canal; finalidade escrita; telefone só com a caixa de WhatsApp; entrega do arquivo sem depender de caixa (marcada [SUPOSIÇÃO] para o jurídico); link da política (URL [CONFIRMAR], bloqueia a publicação até existir); descadastro em um clique e "Responda SAIR" em todo envio; SAIR vale para todas as linhas; nada de CPF, nascimento ou endereço; sem lista comprada; a squad só vê números somados. Aviso de ferramenta de orientação na capa e no rodapé; nenhum título promete vaga, aprovação, título ou resultado.

---

## 4. Conformidade educacional, item por item

Legenda: P = passa; F = falha; N/A = não se aplica.

| Item (auditorias/conformidade-educacional.md) | mensagens | ganchos | autoridade | iscas |
|---|---|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | P (datas e cargas conferidas; 68632 presencial) | P | P | P |
| Curso com status "aberto" ou peça sem chamada | P (turmas em "verificar" fora, regra 10) | P | P | P |
| Modalidade clara e correta | P | P | P | P |
| Graduação: ato regulatório do catálogo | N/A | N/A | N/A | N/A |
| Pós lato sensu sem "reconhecida pelo MEC"; texto de validade aprovado | P (texto oficial não existe: peças sem afirmação) | P | P | P |
| Curso livre deixa claro que não confere diploma | N/A | N/A | N/A | N/A (o minicurso 466 só aparece como limite da aula de A12) |
| Nota MEC só com fonte oficial | P (nenhuma) | P | P | P |
| Sem promessa de emprego, salário, aprovação ou sucesso | P | P | P | P |
| Empregabilidade e satisfação com fonte | N/A | N/A | N/A | N/A |
| Superlativos só com fonte | P (lista "evitar" cobre os textos das fichas) | P | P | P |
| Comparação com concorrente objetiva | P | P | P | P, com ajuste I7 |
| Preço com valor, parcelas e condições completas, sem esconder matrícula | **F** (T1: matrícula suspensa pela decisão 16; condições não verificáveis) | **F** (T1) | P (sem preço) | **F** (T1, e-mail D6) |
| Bolsa e desconto com regra, público e prazo | P (nenhum) | P | P | P |
| Urgência real | P | P | P | P |
| Prouni, Fies ou financiamento | N/A | N/A | N/A | N/A |
| Depoimentos, fotos e vídeos com autorização registrada | P (decisões 8 e 10; nenhum aluno) | P | P | P |
| Menores só com autorização | N/A | N/A | N/A | N/A |
| Formulários com finalidade e política de privacidade | N/A | N/A | N/A | P no desenho; URL [CONFIRMAR] bloqueia publicação |
| WhatsApp e e-mail só com consentimento e saída fácil | N/A | P (só com opt-in; ajuste T4) | N/A | P |
| Nenhum dado pessoal de aluno ou candidato | P | P | P | P |
| Anúncios seguem as políticas da Meta e do Google | P | P | N/A | N/A |
| Página de destino entrega o que a peça promete | **F** (T2: "15" contra página com "20"; T3) | **F** (T2; T3) | **F** (AD-A2-1; T3 no AD-A14-1) | **F** (T2 no e-mail D6; T3 na ponte) |
| Sem característica pessoal de quem vê | P ("Plantonista" é profissão, não característica pessoal) | P | N/A | N/A |
| Sem urgência falsa, contador ou falso botão | P | P | P | P |
| Sem pessoa pública ou parceria inexistente | P | P | P | P |
| Sem caixa alta excessiva ou símbolos | P (nomes em caixa alta só como na ficha; não usar em texto de anúncio) | P, mesma ressalva | P | N/A |
| Página de destino carrega e mostra dados da Ufape | P (662 e 698 sem link; 679 e 68636 pelo T3) | P | P | P |
| Nenhuma sugestão para driblar a análise | P | P | P | P |
| **Resultado** | **Bloqueado** | **Bloqueado** | **Bloqueado** | **Bloqueado** |

Itens bloqueados e o que precisa mudar: seções 2 e 3. Revisado por: qa-de-marketing (agente); revisão humana [CONFIRMAR nome: tabela de aprovação vazia em contexto/ufape-geral.md]. Data: 26/10/2026.

---

## 5. Auditorias de departamento

**auditorias/02-estrategia-e-posicionamento.md (mensagens-pos)**
- Uma meta principal: herdada do plano do cmo (turmas confirmadas); a casa de mensagens não cria meta. P.
- Persona e curso nomeados: por área e por turma, persona [SUPOSIÇÃO]. P.
- 8 canais avaliados: não é escopo da casa de mensagens (fica na camada 1). N/A.
- Alternativa real nomeada: objeções de EAD barato (A3) e de curso curto (base). P.
- Todo pilar tem prova: P, com os ajustes M9 e M10 de precisão.
- Voz com exemplos: lista de palavras e títulos de exemplo. P.
- Cabe no tempo e na verba: N/A nesta etapa.
- Sem promessa de emprego, aprovação ou salário: P.
- Preços e condições do catálogo ou marcados: **F** pela decisão 16 (T1), não pelo catálogo.

**auditorias/05-social.md (criador-de-ganchos-pos e autoridade-docente-pos)**
- Frequência segue o plano: ganchos não agenda (P); autoridade dentro do D5 (P).
- Ideia clara por post: P nos dois.
- Ganchos cumpridos pelo conteúdo: ganchos P na amostra conferida (seção 3.2), com G5 e G6 a corrigir; autoridade **F** no AD-A2-1 (D1).
- Histórias e números reais: ganchos P (contagens conferem; T5 resolve os [CONFIRMAR]); autoridade **F** no AD-A2-1 e nas datas de vencimento (D2).
- Formatado para celular: P.
- Ações de comunidade: N/A (plano).
- Métricas de conversa e lead: P (UTM por peça e por docente).
- Autorização de imagem: P (decisões 8 e 10).
- Dados de curso batem com o catálogo: P nas datas de início e cargas; T3 em 679 e 68636.

**auditorias/06-geracao-de-demanda.md (iscas-digitais-pos)**
- Briefing escrito: P.
- Metas antes do lançamento: sem número, fórmulas e critério de parada (P como plano; números [CONFIRMAR]).
- Isca entrega a promessa do título: P.
- Captura com nutrição em seguida: P, com o ajuste I6.
- Plano de distribuição por peça: encaminhado a social, distribuição e mídia (P como etapa).
- Regras das comunidades: N/A.
- Revisão no ponto de checagem: esta revisão.
- Consentimento por canal: P no desenho.
- Bolsas, descontos e prazos com o catálogo: P em bolsa e desconto; **F** no preço do e-mail D6 (T1) e nos dias sem campanha (I3).

---

## 6. Coerência entre os quatro arquivos

| Tema | mensagens | ganchos | autoridade | iscas | Situação |
|---|---|---|---|---|---|
| Turmas por área (30 turmas, A1 a A14) | iguais à seção 2.3 | iguais | iguais | iguais (A6, A8, A9 reservadas; A13 em espera) | Coerente |
| 662 só nome, campus e data | sim | sem gancho | sem post | só nome | Coerente |
| 699 retida até a ficha | sim | todos BLOQUEADOS | sem post | retida | Coerente |
| 719 fora do público veterinário | sim | só depois de persona e canal | retido | fora | Coerente |
| 68623 até confirmar o local | sim | A3-01 e A3-09 BLOQUEADOS | AD-A3-2 retido | ponte condicionada | Coerente |
| 333 sem autoridade docente | sim | sem DOC | sem post | sem prova de autoridade | Coerente |
| 698 sem data e sem link (A6) | sim | BLOQUEADO para link | Stories sem link | sem ponte | Coerente |
| 341 sem a promoção | sim | sim | sim | sim | Coerente |
| Provas de bolsa fora (decisão 14) | só como fato | sim | sim | sim | Coerente |
| Matrícula no preço (decisão 16) | cita | cita | não cita | proíbe na regra, cita no e-mail D6 | **Incoerente (T1)** |
| Turma mínima em peça | 15 sempre | 15 sempre | 15 se citar | 15 só onde a página já diz | **Incoerente (T2)** |
| 679 e 68636 (P3) | liberadas | data e preço, com A2-05 e 679-05 em parte bloqueados | 68636 condicionada, 679 com data | ponte com data | **Incoerente com o cmo (T3)** |
| Teto de envio | não trata | D1 | D1 | D1 e calendário errado | **Desatualizado (T4)** |
| 1ª mensalidade vencida (707, 68604, 68606; 68610, 68608 e 698 a partir de 29/10) | correto | correto | data de 68606 errada; 68610 e 68608 no passado | correto | **Corrigir na autoridade (D2)** |
| Presenciais de 68617 e 68606 | [CONFIRMAR] | [CONFIRMAR] | conta 68617 errado | [CONFIRMAR] | **Resolver pela ficha (T5)** |
| Presenciais de 289 | ambíguo | A2-01 inexato | AD-A2-1 exagera | correto | **Corrigir (T5, D1, G5)** |

---

## 7. Encaminhamento

- **Voltam para o agente que produziu:** mensagens (M1 a M3 obrigatórias), criador-de-ganchos (G1 a G3), autoridade-docente (D1 a D3), iscas-digitais (I1 a I4). Os ajustes podem entrar na mesma nova versão. Depois da nova versão, o qa-de-marketing confere só os itens marcados como F.
- **Pedidos ao cmo (não alteram arquivo alheio):**
  1. Adotar a regra única de turma mínima de T2 para toda a squad e incluir a correção das páginas que dizem 20 no pedido A12 à Ufape.
  2. Encomendar à estrategia-de-oferta-pos a suspensão do texto-padrão de preço até a U11 (decisão 16), porque todas as saídas copiam esse texto.
  3. Manter ou liberar 679 e 68636 no P3, por escrito, para os agentes não decidirem cada um à sua maneira.
- **Aprovação humana:** nada segue para a aprovação humana nesta versão. Quem aprova cada tipo de peça continua [CONFIRMAR] (tabela vazia em contexto/ufape-geral.md); até lá, vale a pessoa do marketing (P12 do cmo).

---

## Lista 1. Fatos (com fonte)

- A inscrição da Pós custa R$ 260,00 segundo o CEO; o site mostra "matrícula R$ 250,00" e R$ 350,00 em 3 cursos; nenhuma peça cita esse valor até a U11: docs/execucao-2026-10-26.md, decisão 16.
- Turma mínima de 15 alunos também na Pós: decisão 11. Páginas que ainda dizem 20 ou "Mínimo 20": fichas 707, 68610, 68617, 68608, 68628, 68632, 289 e 657 (conferidas); 60 e 699 dizem 15.
- P3: nenhuma peça com preço ou data de 662, 679, 68641, 68642 e 68636 até a correção: cmo-geral, seção 7.
- D16 e E1 a E4 substituem o número do D1; dias sem campanha do D1 (02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço): cmo-geral, seções 12.2 e 13.3.
- D5: sem feed da Pós em 02/11, 20 e 21/11, 25/12 e 01/01; até 10 por semana e 2 por dia: cmo-geral, seção 12.3.
- D12: utm_campaign começa por <linha>_<código>, minúsculas, hífen dentro do bloco e sublinhado entre blocos: cmo-geral, seção 12.7.
- 289: presenciais nos módulos 6, 9, 13, 16, 19 e 24; prática de ecocardiograma em 9, 13, 16 e 19: ficha 289.
- 68617: presenciais nos módulos 12 (18 e 19/03/2028) e 23 (fevereiro de 2029); "Dr. Eric Vieira" consta na mesma ficha: ficha 68617.
- 68606: início em 07/11/2026; presenciais nos módulos 6, 13 (com endoscopia) e 21: ficha 68606. 1ª mensalidade até 30 dias antes do início: mesma ficha.
- 657: presenciais nos módulos 7, 8, 11, 13, 15 e 18: ficha 657.
- 707: 10 presenciais (4, 6, 8, 11, 14, 17, 19, 21, 22 e 24); último em 29 e 30/09 e 01/10/2028; horários de sexta, sábado e domingo: ficha 707.
- 68610: 7 presenciais (5, 9, 14, 18, 21, 22 e 24); módulo 24 com crioterapia e dermatohistopatologia: ficha 68610.
- 68628: 8 presenciais (5, 7, 9, 12, 15, 17, 20 e 24): ficha 68628.
- 68608: terceiro presencial no módulo 22 (farmacologia e prova escrita): ficha 68608.
- 382: 8 presenciais (4, 6, 9, 12, 15, 17, 20 e 22): ficha 382.
- 68623: localidade Goiânia e "Aulas Práticas (Presenciais) - Unidade São Paulo" na mesma página: ficha 68623.
- 26/10/2026 é segunda-feira; 11/12 sexta; 18/11 quarta; 17/12 quinta; 30/12 quarta; 08/01/2027 sexta; 14/01/2027 quinta: calendário.

## Lista 2. Suposições

- [SUPOSIÇÃO] Leitura de que a "matrícula" do catálogo e a "inscrição" da decisão 16 são a mesma taxa (a decisão compara os dois valores e pede [CONFIRMAR U11]).
- [SUPOSIÇÃO] A regra única de turma mínima proposta em T2 (citar 15 só onde a página já mostra 15) é a forma de cumprir a decisão 11 sem falhar o item de página de destino; a decisão final é do cmo.
- [SUPOSIÇÃO] Ganchos substitutos sugeridos para os recomendados bloqueados (A1-08, A3-05, A11-05 ou A11-01).
- [SUPOSIÇÃO] A caixa 1 da iscas, que junta avisos da área e newsletter, cabe na E4 por serem da mesma categoria (campanha); a leitura vai ao jurídico.

## Lista 3. Dados que faltam ([CONFIRMAR])

- [CONFIRMAR U11] Valor da inscrição da Pós (R$ 260,00 informado contra R$ 250,00 e R$ 350,00 no site): destrava todo preço em peça.
- [CONFIRMAR] Correção das páginas da Pós que ainda dizem turma mínima de 20 (pedido A12).
- [CONFIRMAR] Correção dos links de 679 e 68636 ou liberação expressa do cmo (P3, U6).
- [CONFIRMAR] Local dos módulos presenciais de 68623 e da prática com cavalos de 341.
- [CONFIRMAR] Revisor docente nomeado da Pós e prazo; quem aprova cada tipo de peça (tabela de ufape-geral.md).
- [CONFIRMAR] URL da política de privacidade, base legal e textos das caixas (IR3 da iscas).
- [CONFIRMAR] Regra de entrada tardia (PR4) para 707, 68604, 68606, 68610, 68608 e 698; data em que cada turma é confirmada.
- [CONFIRMAR U-I1] Se a régua das provas roda depois da decisão 14 (define os toques de novembro do lead de isca).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação da Pós.

## Fontes

CLAUDE.md; docs/execucao-2026-10-26.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 7, 8, 12 e 13); contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md; auditorias/conformidade-educacional.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/05-social.md; auditorias/06-geracao-de-demanda.md; fichas contexto/cursos/pos/707, 68610, 68617, 68606, 68623, 657, 382, 68628, 68608, 699, 60, 68632, 289 e 68616; os quatro arquivos revisados.
