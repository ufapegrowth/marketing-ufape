# Casa de mensagens da Pós-graduação, por área de especialidade (A1 a A14)

- Agente: mensagens (departamento 02, Estratégia e Posicionamento), etapa 2.2 da camada 2
- Linha: pos
- Data: 26/10/2026
- Status: rascunho para o qa-de-marketing (auditoria 02-estrategia-e-posicionamento e auditorias/conformidade-educacional.md, aplicadas na seção 18). Nada é publicado, enviado ou pago. Toda peça que sair deste arquivo passa de novo pela conformidade, uma a uma.
- Modelo: templates/casa-de-mensagens.md (mensagem central, elevador, 3 pilares com afirmação, prova e palavras do candidato, objeções, palavras que usamos e evitamos), acrescido do que o pedido exige: mensagens por persona e praça, estágios de consciência, versões curtas e "nunca dizer".
- Entradas lidas:
  - docs/execucao-2026-10-26.md (briefing obrigatório)
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/catalogo-de-cursos.md (seções 2 e 3)
  - templates/casa-de-mensagens.md
  - saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md (entrada principal, variações por área)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md (texto-padrão de preço, seção 2.1; objeções, seção 4)
  - saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md (seções 1 a 6)
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md (seções 1 a 5)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 2.3 e seção 7)
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md (briefing da campanha das provas, seções 0 a 3)
  - auditorias/02-estrategia-e-posicionamento.md e auditorias/conformidade-educacional.md
  - Fichas de turma (prova dos pilares), pelo menos uma por área: contexto/cursos/pos/68609 (A1), 289 (A2), 68635 (A3), 68632 (A4), 68629 (A5), 68606 (A6), 68617 (A7), 68610 (A8), 707 (A9), 68628 (A10), 68608 (A11), 68616 (A12), 68652 (A13, prova, porque não há turma aberta), 341, 679, 382, 699, 60 e 719 (A14)
- Não abri faculdade.ufape.com.br. Nenhuma busca nova na web.
- Dados pessoais: nenhum dado de aluno, candidato ou lead. Docentes aparecem só como coordenação, com nome e titulação exatamente como na ficha, e todos marcados [CONFIRMAR autorização]: nenhum deles entra em peça antes da autorização registrada.
- Voz real de candidato: não existe ainda (persona, seção 0). Toda "palavra do candidato" deste arquivo é hipótese de fala, marcada [SUPOSIÇÃO] com o ID da hipótese da pesquisa-de-persona ou do insights-de-alunos. Não é citação e não vira depoimento.

---

## 0. Como usar este arquivo

### 0.1 Regras duras que valem para todas as seções

1. **Preço só no texto-padrão da oferta** (estrategia-de-oferta, seção 2.1). Neste arquivo, todo preço aparece só dentro de um texto-padrão, nos blocos chamados TP. Nas mensagens, o lugar do preço é marcado com {TP-TURMA:código}, {TP-CURTO:código} ou {TP-PROVA:código}. Quem monta a peça cola o texto-padrão da linha do catálogo, sem arredondar e sem recalcular.
2. **Nenhuma frase de certificação**, nenhuma nota do MEC, nenhuma menção a "reconhecida", "aprovada" ou "certificada" pelo MEC. Texto oficial de certificação: [PREENCHER COM A REGULAÇÃO].
3. **Sem "últimas vagas", "vagas limitadas", "10 primeiros"** ou qualquer urgência sem número real. A única urgência permitida é a data de início ou a data da prova, que são reais.
4. **Sem promessa de emprego, renda, título de especialista, aprovação ou "virar referência".**
5. **Docentes:** só nome e titulação como na ficha, só com autorização registrada [CONFIRMAR autorização]. Sem "renomados", "referência nacional", "maiores especialistas".
6. **Nome do curso:** sempre "Pós-graduação em <área>", mesmo quando o site usa "Pós Graduação" ou "Pós-Graduação" (341, 333, 68629, 719).
7. **Hospital:** a Ufape Clínica só aparece como lugar, quando a ficha disser que a prática é lá, e nunca como "única" ou "o único". Nenhuma das fichas lidas diz que os módulos da Pós acontecem na Ufape Clínica: elas dizem "sede da UFAPE, SP" (68610, 707) ou "Ufape Goiânia" (68609, 289, 68632). Até a Ufape confirmar, a peça fala do local da ficha [CONFIRMAR por curso].
8. **Turma numerada como tradição:** a peça pode dizer "turma IX" como dado do catálogo, sem virar "tradição de X anos" nem "milhares de alunos". O uso como prova está [CONFIRMAR] (contexto/ufape-geral.md). Sem número de turma em 68628, 68617 e 662 (turma diverge, P5). Turma I é curso novo: não é prova de tradição.
9. **Reembolso:** nenhuma peça fala de reembolso até a Ufape dizer o que entra em "valores de inscrição" (estrategia-de-oferta, regra 4). Em 341, o texto da ficha tem sentido oposto: nenhuma peça de 341 fala disso.
10. **1ª mensalidade:** a frase "a 1ª mensalidade é paga até 30 dias antes do início" sai das turmas em que o prazo já venceu (707, 68604, 68606 e, a partir de 29/10/2026, 68610 e 68608). Nelas, a mensagem termina em "Fale com o time para saber como entrar na turma" [SUPOSIÇÃO de texto, a validar com vendas].
11. **Dados que estão só nas fichas** (cronograma, módulos presenciais, coordenação, turma mínima, horários, local da prática) servem como prova dos pilares e levam [CONFIRMAR NO CATÁLOGO] antes de peça final, conforme a regra do catálogo. A página avisa que o cronograma pode mudar; a peça diz "pelo cronograma publicado".
12. **EAD:** não há turma EAD aberta (586 em "verificar"). Nenhuma mensagem promete EAD. A teoria é online; a prática é presencial e não é transmitida (fichas).
13. **Status:** turma em "verificar", "sem venda" ou "encerrado" não recebe chamada para inscrição (650, 653, 664, 666, 665, 677, 701, 586, 554, 68605, 68607, 68612, 68662, 678 e outras).
14. **Anúncio:** nenhum texto afirma ou insinua característica pessoal de quem vê (renda, idade, emprego). "Para quem atende..." passa; "Ganha pouco?" bloqueia.

### 0.2 Textos-padrão de preço (copiados da estrategia-de-oferta, seção 2.1)

- **TP-TURMA (página, WhatsApp, e-mail):** "Investimento: [N]x de R$ [parcela] no cartão ou boleto (total de R$ [total]), mais matrícula de R$ [matrícula]. A 1ª mensalidade é paga até 30 dias antes do início. Turma mínima de [número da ficha] alunos: compre passagem e hotel só depois de a turma ser confirmada."
- **TP-CURTO (anúncio, legenda, card):** "[N]x de R$ [parcela] no cartão ou boleto. Total de R$ [total] + matrícula de R$ [matrícula]."
- **TP-PROVA:** "Prova de bolsa de [especialidade], [São Paulo ou Goiânia], em 27/11/2026, das 9h às 13h, presencial. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Quem é aprovado tem até 10 dias úteis para fazer a matrícula. A bolsa não é acumulativa nem transferível."
- **TP-PROVA-CURTO (versão da campanha, seção 1 do briefing):** "Inscrição de R$ 100,00. 11 bolsas por prova, de 10% a 50%. Prova presencial em 27/11/2026." Sempre acompanhado, na mesma peça (legenda, página ou mensagem seguinte), da distribuição completa: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.

Os valores preenchidos de cada turma estão no bloco "TP da área" de cada seção, copiados do catálogo de 26/10/2026. Conferir a página oficial antes de publicar.

---

## 1. Casa de mensagens da linha (base comum das 14 áreas)

**Linha de negócio e curso:** Pós-graduação, 30 turmas abertas e 22 provas de bolsa de 27/11/2026 (catálogo, seções 2 e 3), em São Paulo e Goiânia.

**Mensagem central (uma frase):** Especialize-se sem parar de atender: prática presencial marcada no cronograma e condições claras antes da matrícula.

(Ajuste em relação ao posicionamento: "condições à vista" virou "condições claras", como pediu a estrategia-de-oferta, para não ser lido como pagamento à vista.)

**Versão de elevador (três frases):**
1. A Pós-graduação da Faculdade UFAPE é semipresencial: teoria online e prática presencial em fins de semana marcados no cronograma de cada turma, cerca de um módulo por mês.
2. Antes de se matricular, você vê o que vai praticar em cada módulo presencial, quem coordena o curso e quanto paga, com parcelas, total e matrícula.
3. Se o valor pesa, existe a prova de bolsa da sua especialidade em 27/11/2026, com 11 bolsas por prova.

| Pilar | Afirmação | Prova | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática no cronograma | Você sabe antes quais fins de semana são presenciais e o que acontece em cada um | Cronograma da ficha de cada turma, com módulos presenciais datados e "Aulas Presenciais e Práticas não serão transmitidas" (todas as fichas lidas) | "Não quero aprender procedimento só pela tela." (posicionamento, segmento P1) |
| 2. Quem ensina e continuidade da área | A coordenação e os professores estão na página do curso, com nome e titulação; muitas áreas já estão na sexta, oitava ou nona turma | Fichas (coordenação e lista de professores); catálogo (turmas VI, VII, VIII, IX) [CONFIRMAR uso da turma como prova] | "Quero aprender com quem atende esse tipo de caso." (H-T16) |
| 3. Cabe na rotina, com condições claras | Um fim de semana por mês, cerca de 2 anos, e você vê parcelas, total, matrícula e turma mínima antes de pagar | contexto/pos-graduacao.md (formato); catálogo (preço); fichas (turma mínima, orientação de passagem) | "Não posso largar o plantão." "E se a turma não abrir?" (H-T4, H-T1 a H-T3) |

**Respostas-padrão às 3 objeções do contexto** (cada área adapta na própria seção):

| Objeção | Resposta na linguagem do candidato | Limite |
|---|---|---|
| Investimento alto | "Você vê a conta inteira antes de decidir: {TP-TURMA:código}. Se quiser pagar menos, a prova de bolsa da sua especialidade tem 11 bolsas por prova: {TP-PROVA-CURTO}." | Nunca "cabe no bolso", "se paga", "ganhe mais", comparação de preço com concorrente, desconto sem regra (341, 359, 352, aluno e ex-aluno) |
| Tempo (um fim de semana por mês, cerca de 2 anos, viagem) | "A teoria é online. Você viaja só nos módulos presenciais, que já estão com data no cronograma da turma. Dá para planejar plantão e viagem com meses de antecedência." | Dizer quando o módulo é de 3 dias (707, 60, alguns de 68616 e 719). Nunca "flexível", "no seu ritmo", "estude quando quiser". Reposição de módulo [CONFIRMAR] |
| Medo de a turma não fechar | "A turma abre com no mínimo [número da ficha] alunos. Por isso a orientação é comprar passagem e hotel só uma semana antes ou quando a turma estiver confirmada." | Sem reembolso na peça até a Ufape definir "valores de inscrição"; data de confirmação [CONFIRMAR]; mínimo 15 ou 20 conforme a ficha. Nunca "turma garantida", "turma confirmada" sem confirmação |

**Mensagens por persona (base):**

| Persona [SUPOSIÇÃO] | Mensagem |
|---|---|
| P1. Clínico de pequenos animais, 1 a 8 anos de formado | "Aprofunde a área que mais aparece na sua rotina sem largar o atendimento: você já sabe quais fins de semana são de prática e o que se faz neles." |
| P2. Quem viaja de outra cidade | "O calendário de módulos presenciais está publicado: você planeja as viagens com antecedência e só compra passagem com a turma confirmada." |
| P3. Recém-formado | "Comece pela prova de bolsa da sua área ou pelas turmas de menor total, e siga trabalhando enquanto estuda." (sem citar renda nem "cabe no bolso") |
| P4. Candidato à prova de bolsa | "Com a inscrição da prova você disputa uma das 11 bolsas da especialidade e decide a matrícula depois do resultado." |

**Praças:** Goiânia (A1, A2, A3, A4): "Pós-graduação com prática presencial em Goiânia" (nunca "a única"). EAD (todas): "Não há turma EAD aberta. A teoria é online e a prática é presencial."

**Estágios de consciência (base):**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Aquele caso que você encaminha toda semana também pode ser seu." |
| Consciente do problema | "Curso curto resolve uma técnica. A especialização organiza a área inteira, módulo a módulo." |
| Consciente da solução | "Teoria online, prática presencial uma vez por mês, com as datas publicadas e a coordenação na página." |
| Pronto para se matricular | "{TP-TURMA:código}. Fale com o time pelo WhatsApp de vendas." |

**Palavras que usamos (linha):** Pós-graduação em <área>; semipresencial; teoria online; módulo presencial; prática; cronograma publicado; um fim de semana por mês; turma <número>; coordenação; parcelas, total e matrícula; turma mínima; prova de bolsa; 11 bolsas; médico veterinário, médica veterinária; caso clínico; rotina.

**Palavras que evitamos (linha):** certificado, reconhecida ou aprovada pelo MEC; nota do MEC; título de especialista (como promessa); garantia; excelência; de ponta; o melhor, a maior, referência nacional; renomados; único, única, pioneira; últimas vagas; vagas limitadas; corra; flexível; no seu ritmo; cabe no bolso; investimento que se paga; aumente sua renda; empregabilidade; EAD (como oferta); Pós em, Pós Graduação (no título).

---

## 2. A1. Anestesiologia e dor (657, 68609, 359; provas 68639 e 68640)

**Linha e cursos (catálogo):** Pós-graduação em Anestesiologia Veterinária, Goiânia, semipresencial, 500 h, turma VIII, início 24/04/2027 (68609). Pós-graduação em Anestesiologia Avançada, São Paulo, semipresencial, 360 h, turma II, 13/03/2027 (657). Pós-graduação em Anestesiologia Locorregional Veterinária, São Paulo, semipresencial, 360 h, turma I, 22/05/2027 (359, "só no site"). Fora de chamada: 68607, 586 (EAD), 554 (verificar).

**Situação e bloqueios:** 657 e 359 têm público com pré-requisito (359 exige residência ou pós em anestesiologia, redação ambígua) [CONFIRMAR]. Desconto de 12% para os 10 primeiros de 359: nunca em peça. Não há turma aberta de Anestesiologia Veterinária em São Paulo: a prova 68639 não aponta destino [CONFIRMAR].

**Mensagem central:** Anestesia com segurança no paciente de rotina, com prática presencial em Goiânia e, para quem já é anestesista, níveis avançado e locorregional em São Paulo.

**Elevador:**
1. A Pós-graduação em Anestesiologia Veterinária de Goiânia tem 26 módulos e 500 h, com teoria online e módulos presenciais na Ufape Goiânia.
2. Nos presenciais, pelo cronograma publicado, você faz avaliação pré-anestésica, sedação e monitoração em pacientes, intubação e anestesia inalatória, TIVA e ventilação mecânica, e bloqueios locorregionais em modelos anatômicos.
3. Para quem já é anestesista, a Pós-graduação em Anestesiologia Avançada e a Pós-graduação em Anestesiologia Locorregional Veterinária seguem em São Paulo.

| Pilar | Afirmação | Prova (ficha 68609, salvo indicação) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática presencial do protocolo | Os módulos presenciais cobrem o protocolo do começo ao fim | Módulo 5: prática de avaliação pré-anestésica, sedação e monitoração "em pacientes sedados - hands-on"; módulo 8: intubação, indução, anestesia inalatória; módulo 11: TIVA, TCI, ventilação mecânica, hands-on; módulo 14: bloqueio locorregional em modelos anatômicos; módulos 16 e 17: campanha de castração; módulo 21: RECOVER; módulo 23: exóticos e felinos hands-on [CONFIRMAR NO CATÁLOGO; módulo 17 aparece com data fora de ordem] | "Quero segurança no protocolo do paciente de rotina." (gancho da campanha, H-A1.3) |
| 2. Coordenação e continuidade | Coordenação com nome e titulação na página; turma VIII em Goiânia; trilha de níveis na mesma casa | Coordenação: Dr. Alessandro Martins, Dr Rogério Viera Da Silva, Dra. Mayara Travalini de Lima (grafia como na ficha; a lista de professores traz "Dr. Rogério Vieira") [CONFIRMAR autorização e grafia]; 14 professores listados; catálogo: 68609 turma VIII, 657 turma II, 359 turma I | "Fiz a geral; qual é o próximo passo?" (H-A1.2) |
| 3. Cabe na rotina | 500 h em 26 módulos, presencial com horário publicado | Ficha: presencial de sábado das 9h às 18h e domingo das 9h às 13h (módulo 8); local Ufape Goiânia, Av. T-9, Jardim América | "Não posso parar dois anos para residência." (ALT5, posicionamento) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Se a anestesia da rotina ainda depende de um colega volante, os módulos presenciais trabalham exatamente isso: avaliação, sedação, intubação e monitoração." |
| P2 | "Os módulos presenciais de Goiânia estão no cronograma; quem vem do entorno planeja a viagem com antecedência." |
| P3 | "Comece pela prova de bolsa de Anestesiologia em Goiânia e decida a matrícula depois do resultado." |
| P4 | "Prova de bolsa para a Pós-graduação em Anestesiologia Veterinária: em Goiânia e em São Paulo, 27/11/2026." (destino de 68639 [CONFIRMAR]) |
| Já anestesista (657, 359) | "Para quem já atua na anestesia: níveis avançado e locorregional, 360 h cada, em São Paulo." (pré-requisito [CONFIRMAR]) |
| Goiânia | "Pós-graduação em Anestesiologia Veterinária com prática presencial em Goiânia." |
| EAD | "Não há turma EAD aberta em anestesiologia. A teoria é online e a prática é presencial." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantas anestesias da sua semana você conduz sem ajuda?" |
| Consciente do problema | "Insegurança na indução e na monitoração tem nome: falta de prática supervisionada." |
| Consciente da solução | "26 módulos, teoria online e prática presencial em Goiânia: sedação, intubação, TIVA, bloqueios." |
| Pronto | "{TP-TURMA:68609}. Ou faça a prova de bolsa de 27/11 em Goiânia." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "A conta inteira está aqui: {TP-TURMA:68609}. Em Goiânia, a prova de bolsa de Anestesiologia é em 27/11." | 657 e 359 sem desconto em peça; nunca "12% para os 10 primeiros" |
| Tempo | "Um fim de semana por mês; presencial no sábado e no domingo de manhã, com as datas no cronograma." | Vários presenciais da ficha trazem só o mês ("Agosto de 2027"): não inventar o dia |
| Turma não fechar | "A turma abre com no mínimo 20 alunos. Compre passagem só com a turma confirmada." | Sem reembolso na peça |
| "Preciso de residência para a avançada ou a locorregional?" (área) | "A página da locorregional pede formação prévia em anestesiologia; confirme seu caso com o time antes de se matricular." | Pré-requisito [CONFIRMAR]; não afirmar regra de 657 |
| "A prova de São Paulo vale para qual turma?" (área) | "O destino da prova de São Paulo será informado pela Ufape." | Não indicar 657 nem 359 como destino de 68639 |

**Vocabulário (palavras-chave incorporadas):** pós-graduação em anestesiologia veterinária; pós em anestesiologia veterinária em Goiânia; especialização em anestesiologia de cães e gatos; pós-graduação em anestesiologia avançada; anestesiologia locorregional; bloqueios guiados por ultrassom; prova de bolsa de anestesiologia veterinária; "pós em anestesio vet" só em texto corrido e anúncio de busca. Evitamos: título de especialista em anestesiologia (como promessa; o livre 488 é outro produto), "anestesia EAD".

**TP da área (catálogo):** 68609: "30x de R$ 1.081,67 no cartão ou boleto. Total de R$ 32.450,00 + matrícula de R$ 250,00." 657: "30x de R$ 1.613,33 no cartão ou boleto. Total de R$ 48.400,00 + matrícula de R$ 250,00." 359: "26x de R$ 1.673,08 no cartão ou boleto. Total de R$ 43.500,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Anestesiologia Veterinária em Goiânia: sedação, intubação e bloqueios na prática presencial." |
| Post | "Do pré-anestésico ao RECOVER: o que acontece nos módulos presenciais da Pós-graduação em Anestesiologia Veterinária." |
| WhatsApp | "Oi! A turma VIII da Pós-graduação em Anestesiologia Veterinária começa em 24/04/2027, em Goiânia. Quer ver o cronograma dos módulos presenciais?" |
| E-mail (assunto) | "Anestesia na prática: o cronograma da turma VIII em Goiânia" |
| Página (subtítulo) | "500 h, semipresencial, Goiânia. Teoria online e prática presencial com datas publicadas." |

**Nunca dizer nesta área:** "título de especialista garantido"; o apelo emocional da página ("o paciente com dor deve ser tratado") como gatilho de venda; "12% para os 10 primeiros"; destino de 68639; "anestesia EAD" (586 em "verificar"); "Pós em Anestesiologia" no título.

---

## 3. A2. Cardiorrespiratório (289, 698, 68636, 352; provas 68641, 68642, 68659)

**Linha e cursos (catálogo):** Pós-graduação em Cardiologia Veterinária, Goiânia, semipresencial, 500 h, turma II, 20/03/2027 (289). Pós-graduação em Ecocardiografia, São Paulo, semipresencial, 370 h, turma III, 28/11/2026 pela planilha (698). Pós-graduação em Pneumologia Veterinária, São Paulo, semipresencial, 500 h, turma VIII, 17/04/2027 ("só no site", 68636). Pós-graduação em Ventilação Mecânica, São Paulo, semipresencial, 360 h, turma I, 24/05/2027 pela planilha (352).

**Situação e bloqueios:** 698: site mostra 2027 e a planilha 2026 (P4): nenhum anúncio novo antes da correção (pedido A6). 68641 e 68642: links de Cardiologia SP e Goiânia invertidos (P3): nenhuma peça dessas provas antes da correção. 352: desconto "10 primeiros" nunca em peça. Cardiologia XI (68605) está em andamento: só como dado de continuidade, sem chamada.

**Mensagem central:** Do eletrocardiograma ao ecocardiograma com sonda na mão: cardiologia com prática presencial em Goiânia e formação dedicada a eco, pneumologia e ventilação em São Paulo.

**Elevador:**
1. A Pós-graduação em Cardiologia Veterinária de Goiânia tem 24 módulos e 500 h, com teoria online e módulos presenciais na Ufape Goiânia.
2. Pelo cronograma, quatro módulos presenciais são de prática hands-on de ecocardiograma, e o curso vai da radiografia e do ECG às cardiopatias de cães e gatos.
3. Em São Paulo, quem quer só a imagem cardíaca, a pneumologia ou a ventilação mecânica tem formação dedicada a cada tema.

| Pilar | Afirmação | Prova (ficha 289, salvo indicação) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Eco na mão | A prática presencial é centrada no ecocardiograma | Presenciais nos módulos 6, 9 (hands-on ecocardiograma), 13 (prática de ecocardiograma), 16 e 19 (hands-on) e 24 (aula prática e prova final); "apenas os módulos com aulas práticas serão obrigatoriamente presenciais" [CONFIRMAR NO CATÁLOGO] | "O cardiopata eu ainda mando para outro colega." (H-A2.1) |
| 2. Coordenação e continuidade | Coordenação com nome e titulação; área com turma XI em São Paulo e turma II em Goiânia | Coordenação: Msc. Flavia Mazzo [CONFIRMAR autorização]; 14 professores listados; catálogo: 68605 turma XI (em andamento), 289 turma II, 68636 turma VIII [CONFIRMAR uso da turma como prova] | "Quero aprender com quem faz o exame todo dia." (H-T16) |
| 3. Escolha pelo nível | Cardiologia completa, eco, pneumo ou ventilação: cada uma com carga própria | Catálogo: 289 com 500 h, 698 com 370 h, 68636 com 500 h, 352 com 360 h | "Preciso da cardiologia inteira ou só do eco?" (H-A2.3) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Se o eco ainda é terceirizado, a cardiologia de Goiânia tem quatro módulos de prática hands-on de ecocardiograma no cronograma." |
| P2 | "Quem vem de Goiás e estados vizinhos faz a cardiologia em Goiânia, com as datas dos presenciais publicadas." |
| P3 | "Prova de bolsa de Pneumologia em São Paulo, 27/11: decida a matrícula depois do resultado." (Cardiologia só depois de corrigir os links) |
| P4 | "Prova de bolsa para a Pós-graduação em Pneumologia Veterinária em 27/11/2026." |
| UTI e anestesia (352) | "Para quem já está na UTI ou no centro cirúrgico: a Pós-graduação em Ventilação Mecânica é dedicada ao tema, 360 h." [SUPOSIÇÃO de público] |
| Goiânia | "Pós-graduação em Cardiologia Veterinária com prática presencial em Goiânia." |
| EAD | "Não há turma EAD aberta em cardiologia. A teoria é online e o eco é presencial." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quanto do seu exame cardiológico depende de outro serviço?" |
| Consciente do problema | "Interpretar o eco que outro fez não é o mesmo que fazer o seu." |
| Consciente da solução | "Teoria online e hands-on de ecocardiograma presencial em Goiânia, módulo a módulo." |
| Pronto | "{TP-TURMA:289}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "Veja a conta da turma: {TP-TURMA:289}." | Prova de Cardiologia só depois da correção dos links |
| Tempo | "Teoria online; presencial só nos módulos de prática, com datas no cronograma." | Alguns presenciais trazem só o mês: não inventar o dia |
| Turma não fechar | "A turma abre com no mínimo 20 alunos. Compre passagem só com a turma confirmada." | Sem reembolso na peça |
| "Faço cardiologia ou só ecocardiografia?" (área) | "Se você quer o exame, a Pós-graduação em Ecocardiografia é focada nele, com 370 h. Se quer a área inteira, a cardiologia tem 500 h, com eco dentro." | Não comparar carga com concorrente (a da Anclivepa é maior); pré-requisito de 698 [CONFIRMAR NO CATÁLOGO] |
| "Curso hands-on ou pós?" (área) | "O curso livre ensina uma técnica num fim de semana; a pós organiza a área em módulos. Curso livre não confere diploma nem equivale a pós-graduação." | Livre 573 só por link |

**Vocabulário:** pós-graduação em cardiologia veterinária; pós em cardiologia veterinária em Goiânia; pós-graduação em ecocardiografia veterinária; especialização em cardiologia de cães e gatos; pós-graduação em pneumologia veterinária; pós-graduação em ventilação mecânica veterinária; prova de bolsa de pneumologia veterinária; "pós em cardio vet" e "pós em eco vet" só em texto corrido e busca. Evitamos: "atendimento cardiológico de excelência", "opções diagnósticas de ponta" (texto da página 289).

**TP da área:** 289: "30x de R$ 1.180,00 no cartão ou boleto. Total de R$ 35.400,00 + matrícula de R$ 250,00." 698: "18x de R$ 1.498,33 no cartão ou boleto. Total de R$ 26.970,00 + matrícula de R$ 250,00." (só depois da correção da data, A6) 68636: "30x de R$ 1.265,00 no cartão ou boleto. Total de R$ 37.950,00 + matrícula de R$ 250,00." 352: "30x de R$ 1.596,00 no cartão ou boleto. Total de R$ 47.880,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Cardiologia Veterinária em Goiânia: quatro módulos de ecocardiograma hands-on no cronograma." |
| Post | "ECG, radiografia e eco: como a Pós-graduação em Cardiologia Veterinária distribui a prática presencial." |
| WhatsApp | "Oi! A turma II da Pós-graduação em Cardiologia Veterinária começa em 20/03/2027, em Goiânia. Quer receber o cronograma?" |
| E-mail (assunto) | "Cardiologia, eco, pneumo ou ventilação: qual pós é para você" |
| Página (subtítulo) | "500 h, semipresencial, Goiânia. Teoria online e prática de ecocardiograma presencial." |

**Nunca dizer nesta área:** "a única cardiologia de Goiânia"; comparação de carga horária ou duração com a Anclivepa; data de 698 antes da correção do site; "10% para os 10 primeiros" (352); qualquer peça das provas 68641 e 68642 antes da correção dos links.

---

## 4. A3. Emergência, terapia intensiva e clínica médica (68635, 68623; provas 68645, 68660)

**Linha e cursos (catálogo):** Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, São Paulo, semipresencial, 750 h, turma V, 10/04/2027 (68635). Pós-graduação em Terapia Intensiva e Emergência Veterinária, Goiânia, semipresencial, 750 h, turma IV, 22/05/2027 (68623; ficha não lida nesta etapa, a prova de prática vem de 68635). Fora de chamada: 663, 666 (verificar).

**Situação e bloqueios:** a página de 68635 diz "curso com 2 (duas) certificações aprovadas pelo MEC" e "certificado de clínica médica, 375 horas; certificado de emergência, 375 horas": nada disso vai para peça. A prova 68660 (Terapia Intensiva, SP) não tem turma aberta de mesmo nome em SP [CONFIRMAR destino]. Na ficha de 68635 não aparece campo "Vagas": turma mínima [CONFIRMAR].

**Mensagem central:** Do ambulatório ao paciente grave: 750 h com prática presencial de triagem, monitoração, A-fast, T-fast e RCP, para quem não larga o plantão.

**Elevador:**
1. A Pós-graduação em Clínica Médica e Emergência de Pequenos Animais tem 28 módulos e 750 h, com teoria online e módulos presenciais em São Paulo.
2. Pelo cronograma, os presenciais vão da semiologia e do ambulatório clínico à triagem e monitoração do paciente grave, A-fast, T-fast, RCP e trauma.
3. Em Goiânia, a Pós-graduação em Terapia Intensiva e Emergência Veterinária também tem 750 h.

| Pilar | Afirmação | Prova (ficha 68635, salvo indicação) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática do ambulatório à UTI | Os presenciais seguem o caminho do paciente | Presenciais nos módulos 3 (semiologia, patologia clínica), 6 (ECG, hemogasometria), 10 (semiologia neurológica e respiratória, sondagem uretral), 14 (raspado de pele, testes alergênicos), 18 (ambulatório clínico), 21 (exame oral e tratamento periodontal), 24 (triagem e monitoração do paciente grave), 25 (A-fast, T-fast, atendimento de felinos), 28 (RCP, trauma, atendimento clínico) [CONFIRMAR NO CATÁLOGO] | "Travo no paciente grave do plantão." (H-A3.1) |
| 2. Carga horária e continuidade | 750 h em 28 módulos; turma V em SP e IV em Goiânia | Catálogo: 68635 e 68623 com 750 h; coordenação de 68635: Prof. Caio Cavalcanti Balençuela [CONFIRMAR autorização e titulação acadêmica]; 25 professores listados; Terapia Intensiva e Emergência XI (666) em andamento [CONFIRMAR uso como prova] | "Quero ver a clínica inteira, não só um sistema." [SUPOSIÇÃO] |
| 3. Cabe na escala | Um módulo por mês, com as datas dos presenciais publicadas | Cronograma da ficha; módulos de 3 dias em 666 (persona, seção 5.1); horários de 68623 [CONFIRMAR] | "Plantão eu não largo; dá para conciliar?" (H-A3.4) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 plantonista | "Os presenciais estão datados no cronograma: dá para montar a escala com meses de antecedência." |
| P2 | "Em Goiânia, a Pós-graduação em Terapia Intensiva e Emergência Veterinária tem 750 h; para quem vem do entorno, a viagem fica mais curta." |
| P3 | "Prova de bolsa de Clínica Médica e Emergência em 27/11, em São Paulo." |
| P4 | "Prova de bolsa para a Pós-graduação em Clínica Médica e Emergência de Pequenos Animais em 27/11/2026." |
| Goiânia | "Pós-graduação em Terapia Intensiva e Emergência Veterinária com prática presencial em Goiânia." |
| EAD | "Não há turma EAD aberta. Aqui a triagem, o A-fast e a RCP são presenciais." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "O próximo paciente grave chega no seu plantão." |
| Consciente do problema | "Emergência se aprende fazendo, com supervisão, antes de precisar fazer sozinho." |
| Consciente da solução | "750 h, teoria online e presenciais de triagem, monitoração, A-fast, T-fast e RCP." |
| Pronto | "{TP-TURMA:68635}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "A conta da turma de São Paulo: {TP-TURMA:68635}. Prova de bolsa de Clínica Médica e Emergência em 27/11." | Área mais disputada em preço: nunca comparar com EAD de parcela baixa |
| Tempo (principal nesta área) | "Teoria online e presencial uma vez por mês, com data. Você leva o cronograma para a coordenação da escala." | Nunca "flexível"; reposição de módulo [CONFIRMAR] |
| Turma não fechar | "A turma só abre com o número mínimo de alunos; compre passagem só com a turma confirmada." | Número mínimo de 68635 [CONFIRMAR]; sem reembolso |
| "Clínica médica e emergência ou terapia intensiva?" (área) | "A de São Paulo começa no ambulatório e chega ao paciente grave; a de Goiânia é dedicada à terapia intensiva e emergência." | Ementa de 68623 [CONFIRMAR NO CATÁLOGO] |
| "Por que 750 horas?" (área) | "São 28 módulos, do ambulatório à emergência." | Sem "a maior carga"; distribuição de horas [CONFIRMAR NO CATÁLOGO] |

**Vocabulário:** pós-graduação em clínica médica e emergência de pequenos animais; pós em emergência veterinária; pós-graduação em terapia intensiva veterinária; pós em terapia intensiva veterinária em Goiânia; pós de 750 horas; prova de bolsa de clínica médica e emergência veterinária; "pós em UTI veterinária" só em texto corrido. Evitamos: "duas certificações", "certificado de 375 horas", "UTI EAD".

**TP da área:** 68635: "30x de R$ 1.100,00 no cartão ou boleto. Total de R$ 33.000,00 + matrícula de R$ 250,00." 68623: "30x de R$ 1.160,00 no cartão ou boleto. Total de R$ 34.800,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "750 h do ambulatório ao paciente grave: Pós-graduação em Clínica Médica e Emergência de Pequenos Animais." |
| Post | "Triagem, A-fast, T-fast, RCP: o que você pratica nos presenciais da Pós-graduação em Clínica Médica e Emergência." |
| WhatsApp | "Oi! A turma V da Pós-graduação em Clínica Médica e Emergência de Pequenos Animais começa em 10/04/2027. Quer o cronograma para montar sua escala?" |
| E-mail (assunto) | "Plantão e pós no mesmo ano: o cronograma da turma V" |
| Página (subtítulo) | "750 h, semipresencial, São Paulo. Teoria online, prática presencial do ambulatório à emergência." |

**Nunca dizer nesta área:** "duas certificações aprovadas pelo MEC"; "certificado de clínica médica" e "de emergência"; "a maior carga horária"; "estude no seu ritmo"; comparação com EAD de agregador.

---

## 5. A4. Cirurgia, ortopedia e reabilitação (68632, 578, 662, 366; provas 68643, 68644)

**Linha e cursos (catálogo):** Pós-graduação em Clínica Cirúrgica de Cães e Gatos, Goiânia, **presencial**, 500 h, turma V, 10/04/2027 (68632). Pós-graduação em Videocirurgia Veterinária, São Paulo, semipresencial, 500 h, turma IV, 22/05/2027 (578). Pós-graduação em Ortopedia Veterinária, São Paulo, 500 h, 24/04/2027 (662, link trocado, P3). Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, São Paulo, semipresencial, 500 h, turma I, 10/04/2027 (366, data diverge, P4). Fichas de 578, 662 e 366 não lidas nesta etapa.

**Situação e bloqueios:** 68632 é presencial em todos os módulos: a peça nunca diz "semipresencial". 662: sem preço e sem turma em peça até a correção. 68643 (Clínica Cirúrgica, SP) sem turma aberta de mesmo nome em SP [CONFIRMAR destino]. A ficha de 68632 não lista coordenação, só professores [CONFIRMAR coordenação].

**Mensagem central:** Cirurgia de cães e gatos aprendida presencialmente, todo mês, em Goiânia: dos princípios fundamentais aos procedimentos de alta complexidade.

**Elevador:**
1. A Pós-graduação em Clínica Cirúrgica de Cães e Gatos de Goiânia é presencial, com 24 módulos e 500 h, na Ufape Goiânia.
2. O cronograma vai dos acessos cirúrgicos e do trato urinário e digestivo à ortopedia, neurocirurgia, cirurgia torácica e cardiovascular, com simulação de habilidades nas aulas práticas.
3. Em São Paulo, videocirurgia e reabilitação têm formação própria.

| Pilar | Afirmação | Prova (ficha 68632, salvo indicação) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Presencial do começo ao fim | Todos os módulos são presenciais em Goiânia | Catálogo: modalidade presencial; ficha: 24 módulos datados, de 10 e 11/04/2027 a 10 e 11/03/2029; "simulações de habilidades por meio das aulas práticas" [CONFIRMAR NO CATÁLOGO] | "Cirurgia não se aprende por vídeo." (H-A4.1, H-T7) |
| 2. Programa por sistema | Cada mês, um sistema ou uma técnica | Módulos 1 a 24: princípios e acessos, feridas e drenos, urinário, gastrointestinal I e II, reprodutor, ortopedia e osteossíntese, oncológica e reconstrutiva, torácica, videocirurgia e endoscopia, neurocirurgia, cardiovascular, felinos e trauma | "Quero operar com mais segurança na minha clínica." (gancho da campanha) |
| 3. Continuidade e quem ensina | Turma V; professores com titulação na página | Catálogo: turma V; ficha: 6 professores listados com "Dr." e "Dra." [CONFIRMAR autorização]; coordenação [CONFIRMAR] | "Quem vai estar comigo no centro cirúrgico?" [SUPOSIÇÃO] |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Um fim de semana por mês em Goiânia, todos presenciais, um sistema por módulo." |
| P2 | "É presencial todo mês: quem vem de fora planeja 24 viagens, com as datas já publicadas." |
| P3 | "Prova de bolsa de Clínica Cirúrgica em Goiânia, 27/11/2026." |
| P4 | "Prova de bolsa para a Pós-graduação em Clínica Cirúrgica de Cães e Gatos em Goiânia." |
| Reabilitação (366) | "Fisioterapia, fisiatria e reabilitação: turma I em São Paulo." (público [CONFIRMAR]) |
| Goiânia | "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, presencial, em Goiânia." |
| EAD | "Não há turma EAD aberta em cirurgia. Em Goiânia, todos os módulos são presenciais." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Qual cirurgia você ainda encaminha?" |
| Consciente do problema | "Técnica cirúrgica pede repetição presencial, com alguém ao lado." |
| Consciente da solução | "24 módulos presenciais em Goiânia, um sistema por mês." |
| Pronto | "{TP-TURMA:68632}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68632}. Prova de bolsa de Clínica Cirúrgica em Goiânia em 27/11." | 662 sem preço |
| Tempo (mais forte aqui) | "É presencial todo mês, sábado e domingo, com as 24 datas publicadas." | Não suavizar: é presencial integral |
| Turma não fechar | "A turma abre com no mínimo 20 alunos. Compre passagem só com a turma confirmada." | Sem reembolso |
| "Preciso estar em Goiânia todo mês?" (área) | "Sim. Por isso as datas estão publicadas até 2029." | Hospedagem e parceria: não existem no catálogo |
| "Videocirurgia: pós ou curso prático?" (área) | "O curso prático ensina uma técnica; a Pós-graduação em Videocirurgia Veterinária organiza a área em módulos. Curso livre não equivale a pós-graduação." | Livres 99 e 433 em "verificar": sem chamada |

**Vocabulário:** pós-graduação em clínica cirúrgica de cães e gatos; pós em clínica cirúrgica presencial em Goiânia; pós em cirurgia veterinária; especialização em cirurgia de cães e gatos; pós-graduação em videocirurgia veterinária; pós-graduação em fisioterapia veterinária; reabilitação; prova de bolsa de clínica cirúrgica de cães e gatos. Evitamos: "referência nacional em educação", "o curso garante" (texto da página 68632), "semipresencial" para 68632.

**TP da área:** 68632: "30x de R$ 1.100,00 no cartão ou boleto. Total de R$ 33.000,00 + matrícula de R$ 250,00." 578: "30x de R$ 1.250,00 no cartão ou boleto. Total de R$ 37.500,00 + matrícula de R$ 250,00." 366: "30x de R$ 1.100,00 no cartão ou boleto. Total de R$ 33.000,00 + matrícula de R$ 250,00." 662: bloqueado (P3).

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Clínica Cirúrgica de Cães e Gatos, presencial em Goiânia: um sistema por módulo." |
| Post | "Do acesso cirúrgico à neurocirurgia: os 24 módulos presenciais da turma V em Goiânia." |
| WhatsApp | "Oi! A turma V da Pós-graduação em Clínica Cirúrgica de Cães e Gatos começa em 10/04/2027, em Goiânia, e é presencial. Quer as datas dos 24 módulos?" |
| E-mail (assunto) | "24 fins de semana de cirurgia em Goiânia: as datas" |
| Página (subtítulo) | "500 h, presencial, Goiânia. Um sistema por módulo, com datas publicadas até 2029." |

**Nunca dizer nesta área:** "semipresencial" para 68632; "a única pós presencial de Goiânia"; "referência nacional"; preço ou turma de 662; "o curso garante" habilidades.

---

## 6. A5. Diagnóstico por imagem e endoscopia (68604, 68629; provas 68647, 68661, 68649)

**Linha e cursos (catálogo):** Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, São Paulo, semipresencial, 500 h, turma VI, 31/10/2026 (68604, reta final; ficha não lida). Pós-graduação em Ultrassonografia de Pequenos Animais, São Paulo, semipresencial, 360 h, turma III, 22/05/2027 ("só no site", 68629). Fora: 653 Endoscopia e 706 (verificar).

**Situação e bloqueios:** 68604 começa em 5 dias: regra da 1ª mensalidade vencida (usar o fim "Fale com o time para saber como entrar na turma"). 68647 (Imagem) tem turma que começa antes da prova [CONFIRMAR destino]. 68649 (Endoscopia) sem turma: fora da campanha por área.

**Mensagem central:** Ultrassom feito por você, na sua clínica: 360 h com quatro módulos de prática presencial.

**Elevador:**
1. A Pós-graduação em Ultrassonografia de Pequenos Animais tem 18 módulos e 360 h, com teoria online e quatro módulos de prática presencial em São Paulo.
2. O cronograma percorre abdome, tórax, pescoço, olho, músculo-esquelético, Doppler, procedimentos guiados e POCUS na emergência.
3. A prova de bolsa de Ultrassonografia é em 27/11/2026.

| Pilar | Afirmação | Prova (ficha 68629) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática com sonda | Quatro módulos presenciais de prática | Módulos 6 (Prática I), 10 (Prática II), 14 (Prática III) e 17 (Prática IV), presenciais; práticas não transmitidas [CONFIRMAR NO CATÁLOGO] | "Quero fazer o ultrassom aqui, sem terceirizar." (gancho da campanha) |
| 2. Coordenação e continuidade | Coordenação com nome e titulação; turma III | Coordenação: MSC. Luciane Kanayama [CONFIRMAR autorização]; 10 professores listados; catálogo turma III | "Quero aprender com quem lauda todo dia." [SUPOSIÇÃO] |
| 3. Do básico ao POCUS | Programa do aparelho e presets ao intensivismo | Módulo 1 (aparelhagem, presets, bases físicas); módulos 12 (Doppler básico e avançado), 15 (procedimentos guiados), 16 (A-fast, T-fast, Vetblue, POCUS) | "Imagem ou ultrassom, por onde começo?" (H-A5.4) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Se o ultrassom da sua clínica depende de volante, quatro módulos presenciais são de prática." |
| P2 | "São quatro presenciais em São Paulo ao longo do curso; o resto é online." |
| P3 | "É a pós veterinária aberta de menor total no catálogo: {TP-CURTO:68629}. E há prova de bolsa em 27/11." (sem "cabe no bolso"; "menor total" é contagem do catálogo, nunca "a mais barata") |
| P4 | "Prova de bolsa para a Pós-graduação em Ultrassonografia de Pequenos Animais, 27/11/2026." |
| Reta final (68604) | "A turma VI da Pós-graduação em Diagnóstico por Imagem começa em 31/10/2026. Fale com o time para saber como entrar na turma." |
| EAD | "Não há turma EAD aberta. A teoria é online; a prática com o aparelho é presencial." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quanto tempo seu paciente espera pelo ultrassom?" |
| Consciente do problema | "Interpretar o laudo de outro não é o mesmo que fazer o exame." |
| Consciente da solução | "360 h, teoria online e quatro práticas presenciais com sonda." |
| Pronto | "{TP-TURMA:68629}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68629}. Note a matrícula, que nesta turma é diferente das outras." | Matrícula de R$ 350,00 só dentro do TP |
| Tempo | "Quatro módulos presenciais; o resto online, com datas publicadas." | |
| Turma não fechar | "A turma abre com no mínimo 20 alunos. Compre passagem só com a turma confirmada." | Sem reembolso |
| "Preciso de pós para fazer ultrassom na minha clínica?" (área) | "A pós organiza o exame do aparelho ao Doppler e ao POCUS; o que a sua atuação exige é uma decisão sua, com o seu conselho regional." | [REVISÃO REGULAÇÃO]; sem afirmar exigência legal |
| "Imagem ou ultrassonografia?" (área) | "A de ultrassonografia é focada no ultrassom; a de diagnóstico por imagem é mais ampla." | Ementa de 68604 [CONFIRMAR NO CATÁLOGO] |

**Vocabulário:** pós-graduação em ultrassonografia veterinária; pós em ultrassonografia de pequenos animais; pós em ultrassom veterinário; pós-graduação em diagnóstico por imagem veterinária; especialização em radiologia veterinária (só com radiologia na ementa [CONFIRMAR]); prova de bolsa de ultrassonografia veterinária; "pós em USG vet" só em busca. Evitamos: "a mais barata", "conteúdo da graduação deveras superficial" (texto da página), "endoscopia" como oferta.

**TP da área:** 68629: "24x de R$ 685,67 no cartão ou boleto. Total de R$ 16.456,00 + matrícula de R$ 350,00." 68604: "30x de R$ 1.000,00 no cartão ou boleto. Total de R$ 30.000,00 + matrícula de R$ 250,00." (sem a frase da 1ª mensalidade)

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Ultrassonografia de Pequenos Animais: quatro módulos de prática presencial com o aparelho." |
| Post | "Do preset ao POCUS: o caminho dos 18 módulos da Pós-graduação em Ultrassonografia de Pequenos Animais." |
| WhatsApp | "Oi! A turma III da Pós-graduação em Ultrassonografia de Pequenos Animais começa em 22/05/2027. Quer ver as datas das quatro práticas?" |
| E-mail (assunto) | "Ultrassom na sua clínica: o cronograma da turma III" |
| Página (subtítulo) | "360 h, semipresencial, São Paulo. Teoria online e quatro práticas presenciais." |

**Nunca dizer nesta área:** "a pós mais barata"; "precisa de pós para fazer ultrassom"; "últimos dias" para 68604 (só a data de início); prova de Endoscopia como caminho para alguma turma.

---

## 7. A6. Gastroenterologia (68606; prova 68650)

**Linha e curso (catálogo):** Pós-graduação em Gastroenterologia Veterinária, São Paulo, semipresencial, 500 h, turma IX, 07/11/2026 (68606).

**Situação e bloqueios:** reta final (12 dias): 1ª mensalidade vencida. A prova 68650 é depois do início da turma: não vender a prova como caminho para 68606 [CONFIRMAR destino]. Não juntar a reta final e a prova na mesma peça.

**Mensagem central:** O paciente digestivo de ponta a ponta, com prática presencial de cirurgia, endoscopia e videocirurgia: a turma IX começa em 07/11/2026.

**Elevador:**
1. A Pós-graduação em Gastroenterologia Veterinária tem 24 módulos e 500 h, com teoria online e três módulos práticos presenciais em São Paulo.
2. Nos presenciais, pelo cronograma, há anatomia prática e cirurgia esofágica, gástrica e intestinal, endoscopia, videocirurgia e cirurgia pancreática e hepatobiliar, além de atendimento clínico.
3. Entre os módulos, a página prevê um grupo de discussão de casos entre alunos e coordenação.

| Pilar | Afirmação | Prova (ficha 68606) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática que o digestivo pede | Cirurgia, endoscopia e videocirurgia nos presenciais | Módulo 6 (anatomia prática, cirurgia esofágica, gástrica e intestinal, parasitologia ou transplante fecal); módulo 13 (endoscopia); módulo 21 (videocirurgia, cirurgia pancreática e hepatobiliar, sondas, atendimento clínico) [CONFIRMAR NO CATÁLOGO] | "O paciente que vomita e volta todo mês." (gancho da campanha) |
| 2. Coordenação, turma IX e discussão de casos | A área está na nona turma; coordenação na página | Catálogo: turma IX; coordenação: Esp. Maria Carolina Pappalardo [CONFIRMAR autorização]; 38 nomes na lista; "grupo para discussão de casos entre os alunos e os coordenadores" (texto da página) [CONFIRMAR uso da turma como prova] | "Quero alguém para discutir o caso difícil." [SUPOSIÇÃO] |
| 3. Da semiologia à oncologia | Programa completo do trato digestivo | Módulos de semiologia, laboratório, imagem, esôfago, estômago, intestino, pâncreas, fígado, emergências, endócrino, oncologia | "Sei o básico, mas não fecho o diagnóstico." (H-T16) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Começa em 07/11/2026: 24 módulos sobre o paciente digestivo, com prática presencial." |
| P2 | "São três módulos práticos presenciais em São Paulo; o resto é online." |
| P3 | "Se a turma IX ficou próxima demais, a prova de bolsa de Gastroenterologia de 27/11 tem destino a confirmar pela Ufape." |
| P4 | "Prova de bolsa para a Pós-graduação em Gastroenterologia Veterinária, 27/11/2026 (destino [CONFIRMAR])." |
| EAD | "Não há turma EAD aberta. Cirurgia e endoscopia são presenciais." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantos vômitos crônicos passaram pela sua agenda este mês?" |
| Consciente do problema | "Enteropatia, pancreatite, hepatopatia: o digestivo pede raciocínio de especialista." |
| Consciente da solução | "500 h, teoria online, prática de endoscopia e cirurgia." |
| Pronto | "A turma IX começa em 07/11/2026. {TP-CURTO:68606}. Fale com o time para saber como entrar na turma." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-CURTO:68606}. Fale com o time para saber como entrar na turma." | Sem a frase da 1ª mensalidade; sem prova como desconto para esta turma |
| Tempo | "Um fim de semana por mês; três presenciais ao longo de dois anos." | |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso |
| "Posso entrar agora?" (área) | "O time explica como fica a entrada a esta altura." | Regra de entrada tardia [CONFIRMAR] (PR4) |
| "Tem endoscopia e estágio?" (área) | "Há endoscopia num dos presenciais, pelo cronograma." | "Estágios com a cooperação em suas clínicas" [CONFIRMAR] antes de usar |

**Vocabulário:** pós-graduação em gastroenterologia veterinária; pós em gastroenterologia veterinária de pequenos animais em São Paulo; especialização em gastroenterologia de cães e gatos; prova de bolsa de gastroenterologia veterinária; "pós em gastro vet" só em busca. Evitamos: "especialidade emergente e carente de profissionais", "coordenadores referências nacionais" (texto da página).

**TP da área:** 68606: "30x de R$ 1.180,00 no cartão ou boleto. Total de R$ 35.400,00 + matrícula de R$ 250,00." (sem a frase da 1ª mensalidade)

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Gastroenterologia Veterinária, turma IX: começa em 07/11/2026, com endoscopia e cirurgia na prática." |
| Post | "Esôfago, estômago, intestino, pâncreas e fígado em 24 módulos." |
| WhatsApp | "Oi! A turma IX da Pós-graduação em Gastroenterologia Veterinária começa em 07/11/2026. Quer saber como entrar na turma?" |
| E-mail (assunto) | "Turma IX de Gastroenterologia: começa em 07/11" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Três módulos práticos presenciais." |

**Nunca dizer nesta área:** "especialidade carente de profissionais"; "referências nacionais"; "últimas vagas"; "faça a prova e entre com bolsa nesta turma".

---

## 8. A7. Endocrinologia e nefrologia (68617; provas 68648, 68653)

**Linha e curso (catálogo):** Pós-graduação em Endocrinologia de Pequenos Animais, São Paulo, semipresencial, 500 h, 17/04/2027 (68617; turma diverge entre planilha e site, P5: sem número de turma). Fora: 68612 Nefrologia (verificar). Prova 68653 sem turma (D4).

**Mensagem central:** Diabetes, Cushing e tireoide com acompanhamento de longo prazo: endocrinologia de cães e gatos com atendimento endocrinológico presencial.

**Elevador:**
1. A Pós-graduação em Endocrinologia de Pequenos Animais tem 24 módulos e 500 h, com teoria online e dois módulos presenciais em São Paulo.
2. Os presenciais, pelo cronograma, têm atendimento endocrinológico, anatomia do sistema endócrino, ultrassom abdominal, cirurgia do sistema endócrino e discussão de casos clínicos dos alunos.
3. O programa passa por Cushing, hipoadrenocorticismo, diabetes em cães e gatos, tireoide, insulinoma e emergências endócrinas.

| Pilar | Afirmação | Prova (ficha 68617) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Atendimento endócrino na prática | Dois presenciais com atendimento e casos | Módulo 12 (atendimento endocrinológico, anatomia, discussão de casos); módulo 23 (atendimento endócrino, US abdominal, cirurgia do sistema endócrino, casos dos alunos) [CONFIRMAR NO CATÁLOGO; módulo 17 aparece com data fora de ordem] | "Endócrino é acompanhamento longo; quero conduzir sem medo." (gancho da campanha) |
| 2. Coordenação | Coordenação com nome e titulação | DR. Eric Vieira Januário [CONFIRMAR autorização]; 22 professores listados; sem número de turma (P5) | "Quero aprender com quem atende endócrino toda semana." [SUPOSIÇÃO] |
| 3. Discussão de casos ao longo do curso | Casos discutidos em vários módulos | Módulos 8, 9, 10, 13, 14 e 20 com discussão de casos | "Rede de contatos e currículo mais forte." (H-A7.1; sem prometer) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Diabético instável, Cushing que não fecha: o curso trabalha esses casos módulo a módulo." |
| P2 | "Dois módulos presenciais em São Paulo; o resto é online." |
| P3 | "Prova de bolsa de Endocrinologia em 27/11/2026." |
| P4 | "Prova de bolsa para a Pós-graduação em Endocrinologia de Pequenos Animais." |
| EAD | "Não há turma EAD aberta. O atendimento endocrinológico é presencial." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantos pacientes crônicos você acompanha sem protocolo próprio?" |
| Consciente do problema | "Endocrinopata exige ajuste fino por anos; o tutor volta toda semana." |
| Consciente da solução | "500 h sobre o paciente endócrino, com atendimento presencial e discussão de casos." |
| Pronto | "{TP-TURMA:68617}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68617}. Prova de bolsa de Endocrinologia em 27/11." | |
| Tempo | "Só dois módulos presenciais em São Paulo; o resto é online, um fim de semana por mês." | |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso; sem número da turma |
| "E nefrologia?" (área) | "A prova de Nefrologia e Urologia de 27/11 tem destino a confirmar pela Ufape." | 68653 fora de anúncio por área (D4) |

**Vocabulário:** pós-graduação em endocrinologia de pequenos animais; pós em endocrinologia veterinária; especialização em endocrinologia de cães e gatos; diabetes e tireoide em cães e gatos; prova de bolsa de endocrinologia veterinária; "pós em endócrino vet" só em busca. Evitamos: "instituição reconhecida e respeitada", "profissionais renomados", "amplia suas oportunidades profissionais" (texto da página), número de turma.

**TP da área:** 68617: "30x de R$ 1.200,00 no cartão ou boleto. Total de R$ 36.000,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Endocrinologia de Pequenos Animais: diabetes, Cushing e tireoide com atendimento presencial." |
| Post | "Cushing, hipoadreno, diabetes, tireoide: o que cada módulo trabalha." |
| WhatsApp | "Oi! A Pós-graduação em Endocrinologia de Pequenos Animais começa em 17/04/2027. Quer ver o cronograma?" |
| E-mail (assunto) | "O paciente endócrino, módulo a módulo" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Atendimento endocrinológico presencial e discussão de casos." |

**Nunca dizer nesta área:** número da turma; "renomados"; "agrega valor ao seu currículo e amplia oportunidades"; destino da prova de Nefrologia.

---

## 9. A8. Dermatologia (68610; prova 68646)

**Linha e curso (catálogo):** Pós-graduação em Dermatologia Veterinária, São Paulo, semipresencial, 500 h, turma V, 28/11/2026 (68610).

**Situação e bloqueios:** a 1ª mensalidade vence em 29/10/2026 (conta da estrategia-de-oferta); depois disso, sem a frase. A prova 68646 é em 27/11, um dia antes do início (D2): nenhuma peça da prova cita a turma de 28/11, e nenhuma peça da turma sugere esperar a prova [CONFIRMAR decisão A-C2]. Coordenação na ficha: "UFAPE" (sem pessoa).

**Mensagem central:** A dermatite que volta todo mês, tratada módulo a módulo: sete presenciais com atendimento de casos clínicos, citologia, testes alérgicos e otoscopia.

**Elevador:**
1. A Pós-graduação em Dermatologia Veterinária tem 24 módulos e 500 h, com teoria online e sete módulos presenciais na sede da Faculdade UFAPE em São Paulo.
2. Pelo cronograma, os presenciais têm coleta e citologia, atendimento de casos clínicos, dermatoscopia, testes alérgicos, otoscopia e videotoendoscopia, feridas e crioterapia.
3. A turma V começa em 28/11/2026.

| Pilar | Afirmação | Prova (ficha 68610) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Sete presenciais com caso clínico | Prática do exame ao laudo | Presenciais nos módulos 5, 9, 14, 18, 21, 22 e 24; "Atendimento de Casos Clínicos" em 5 e 9; coleta, colorações e laudos de citopatologia (5); testes alérgicos (14); otoscopia e videotoendoscopia (18); práticas na sede da UFAPE, SP, não transmitidas [CONFIRMAR NO CATÁLOGO] | "Dermatite que volta todo mês e otite que não fecha." (H-A8.1) |
| 2. Quem ensina | 18 professores com titulação na página | Ficha: 18 nomes com Dr., Dra., MSc. e Esp.; coordenação registrada como "UFAPE" [CONFIRMAR coordenação nominal e autorização]; turma V [CONFIRMAR uso como prova] | "Quero aprender com quem atende pele toda semana." [SUPOSIÇÃO] |
| 3. Formato com datas até 2028 | Datas de todos os 24 módulos publicadas | Cronograma de 28 e 29/11/2026 a 28 e 29/10/2028; avaliação por prova mensal online de 5 questões | "Preciso saber os fins de semana para avisar a clínica." (H-T4) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Sete fins de semana presenciais em dois anos, com atendimento de casos e citologia: as datas já estão publicadas." |
| P2 | "Você sabe hoje os sete fins de semana em que precisa estar em São Paulo." |
| P3 | "Turma V, 500 h: veja a conta inteira antes de decidir." |
| P4 | "Prova de bolsa para a Pós-graduação em Dermatologia Veterinária em 27/11/2026; o destino da bolsa será informado pela Ufape." |
| EAD | "Não há turma EAD aberta. As práticas presenciais não são transmitidas." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantas consultas da sua semana são de pele?" |
| Consciente do problema | "Prurido que volta é diagnóstico incompleto, não tutor difícil." |
| Consciente da solução | "500 h, sete presenciais com casos clínicos, citologia e testes alérgicos." |
| Pronto | "Turma V em 28/11/2026. {TP-TURMA:68610}." (até 29/10; depois, TP sem a frase da 1ª mensalidade) |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68610}." | Após 29/10/2026, sem a frase da 1ª mensalidade e com "Fale com o time para saber como entrar na turma" |
| Tempo | "Sete presenciais em dois anos; o resto online, com datas publicadas." | |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso |
| "Espero a prova de bolsa para entrar?" (área) | "A prova é em 27/11 e a turma começa em 28/11. O time explica o que vale para cada caso." | Decisão A-C2 [CONFIRMAR]; nunca sugerir esperar |
| "EAD ou semipresencial?" (área) | "Aqui a teoria é online e a prática de pele, ouvido e citologia é presencial." | Sem comparar preço com EAD |

**Vocabulário:** pós-graduação em dermatologia veterinária; pós em dermatologia veterinária semipresencial em São Paulo; especialização em dermatologia de cães e gatos; duração e carga horária; prova de bolsa de dermatologia veterinária; "pós em derma vet" só em busca. Evitamos: "excelência", "reconhecida pelo MEC" (texto da página).

**TP da área:** 68610: "30x de R$ 1.000,00 no cartão ou boleto. Total de R$ 30.000,00 + matrícula de R$ 250,00." Completo até 29/10/2026: exemplo preenchido da estrategia-de-oferta, seção 2.1.

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Dermatologia Veterinária: sete presenciais com atendimento de casos e citologia. Turma V em 28/11." |
| Post | "Citologia, testes alérgicos, videotoscopia: os sete presenciais da turma V." |
| WhatsApp | "Oi! A turma V da Pós-graduação em Dermatologia Veterinária começa em 28/11/2026. Quer as datas dos sete presenciais?" |
| E-mail (assunto) | "Os sete fins de semana de prática da Dermatologia" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Sete módulos presenciais com casos clínicos." |

**Nunca dizer nesta área:** "reconhecida pelo MEC"; "faça a prova e entre com bolsa na turma de 28/11"; "últimas vagas"; coordenador nominal (a ficha não traz).

---

## 10. A9. Oftalmologia (707)

**Linha e curso (catálogo):** Pós-graduação em Oftalmologia Veterinária, São Paulo, semipresencial, 600 h, turma VII, 30/10/2026 (707).

**Situação e bloqueios:** reta final (4 dias); 1ª mensalidade vencida. Sem prova de bolsa (68656 fora do ar): nenhuma peça fala de bolsa nesta área. Maior parcela do padrão 30x: a objeção de preço é a mais forte.

**Mensagem central:** Clínica e microcirurgia ocular com microscópio individual por aluno e atendimentos reais supervisionados: a turma VII começa em 30/10/2026.

**Elevador:**
1. A Pós-graduação em Oftalmologia Veterinária tem 24 módulos de três dias e 600 h, com teoria online ao vivo e gravada.
2. Os presenciais acontecem na sede da Faculdade UFAPE em São Paulo, com microscópio individual para cada aluno, supervisão de professores e monitores e atendimentos clínicos reais em mutirões supervisionados.
3. A turma VII começa em 30/10/2026.

| Pilar | Afirmação | Prova (ficha 707) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Microscópio individual e casos reais | Prática de microcirurgia e atendimento | "Cada aluno conta com um microscópio individual, além de supervisão constante de professores e monitores"; "atendimentos clínicos reais, em mutirões supervisionados"; presenciais nos módulos 4, 6, 8, 11, 14, 17, 19, 21, 22 e 24 [CONFIRMAR NO CATÁLOGO] | "É muito dinheiro; o que justifica?" (H-A9.2) |
| 2. Coordenação e turma VII | Três coordenadoras com titulação; sétima turma | Coordenação: Dra. Andrea Barbosa, Dra. Angélica Safatle, Dra. Juliana Jorge (a lista final traz "MSC. Juliana Jorge": [CONFIRMAR titulação e autorização]); 19 nomes; turma VII [CONFIRMAR uso como prova] | "Quero ver quem opera." [SUPOSIÇÃO] |
| 3. 600 h em módulos de três dias | Carga e horário publicados | Catálogo: 600 h; ficha: sexta das 14h às 20h, sábado das 8h às 17h30, domingo das 8h às 12h | "Três dias por mês?" (H-A9.3) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 experiente | "Se o olho é a parte da clínica que você mais encaminha, a turma VII começa em 30/10/2026." |
| P2 | "Teoria online ao vivo e gravada; presencial em módulos de sexta a domingo, com horário publicado." |
| P3 | Sem mensagem própria: sem prova de bolsa na área e com a maior parcela do padrão 30x. Encaminhar ao time. |
| P4 | Não se aplica (sem prova). |
| EAD | "Não há turma EAD aberta. Microcirurgia é presencial, no microscópio." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Úlcera de córnea que não fecha: você conduz ou encaminha?" |
| Consciente do problema | "Oftalmologia exige mão no microscópio, não só teoria." |
| Consciente da solução | "600 h, microscópio individual nos presenciais, atendimentos reais supervisionados." |
| Pronto | "Turma VII em 30/10/2026. {TP-CURTO:707}. Fale com o time para saber como entrar na turma." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento (mais forte) | "{TP-CURTO:707}. No valor estão 600 h e os presenciais com microscópio individual por aluno." | Sem bolsa, sem desconto; nunca comparar com EAD |
| Tempo | "Módulos de sexta à tarde a domingo de manhã, com horário publicado." | Dizer que são três dias |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso |
| "Posso entrar agora?" (área) | "Fale com o time para saber como entrar na turma." | Regra de entrada tardia [CONFIRMAR] |
| "Pós ou curso de microcirurgia?" (área) | "O curso livre treina uma técnica; a pós cobre clínica e cirurgia ocular em 24 módulos." | Livres de microcirurgia sem data: sem chamada |

**Vocabulário:** pós-graduação em oftalmologia veterinária; pós em oftalmologia veterinária presencial em São Paulo (dito como "semipresencial com prática presencial"); especialização em oftalmologia de cães e gatos; pós em oftalmologia veterinária 600 horas; "pós em oftalmo vet" só em busca. Evitamos: "infraestrutura completa e moderna", "referências nacionais e internacionais" (texto da página), "prova de bolsa de oftalmologia".

**TP da área:** 707: "30x de R$ 1.590,00 no cartão ou boleto. Total de R$ 47.700,00 + matrícula de R$ 250,00." (sem a frase da 1ª mensalidade)

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Oftalmologia Veterinária: microscópio individual nos presenciais. Turma VII em 30/10/2026." |
| Post | "Como funciona um presencial de oftalmologia: microscópio por aluno e atendimento supervisionado." |
| WhatsApp | "Oi! A turma VII da Pós-graduação em Oftalmologia Veterinária começa em 30/10/2026. Quer saber como entrar na turma?" |
| E-mail (assunto) | "Turma VII de Oftalmologia: começa em 30/10" |
| Página (subtítulo) | "600 h, semipresencial, São Paulo. Microscópio individual e atendimentos reais supervisionados." |

**Nunca dizer nesta área:** prova de bolsa; "infraestrutura completa e moderna"; "referências internacionais"; "últimas vagas"; "título de especialista" ou CBOV.

---

## 11. A10. Oncologia (68628; prova 68657)

**Linha e curso (catálogo):** Pós-graduação em Oncologia Veterinária, São Paulo, semipresencial, 500 h, 10/04/2027 (68628; turma diverge, P5: sem número).

**Mensagem central:** O paciente oncológico conduzido com protocolo e biossegurança: quimioterapia, eletroquimioterapia, cirurgia e radioterapia na prática presencial.

**Elevador:**
1. A Pós-graduação em Oncologia Veterinária tem 24 módulos e 500 h, com teoria online e módulos presenciais em São Paulo.
2. Pelo cronograma, os presenciais têm quimioterapia com biossegurança, eletroquimioterapia e crioterapia, cirurgia oncológica e reconstrutiva, radioterapia com visita e discussão de casos.
3. A prova de bolsa de Oncologia é em 27/11/2026.

| Pilar | Afirmação | Prova (ficha 68628) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Tratamento na prática | Cada modalidade de tratamento tem presencial | Módulo 5 (quimioterapia e biossegurança), 7 (eletroquimioterapia, crioterapia), 9 (cirurgia oncológica e reconstrutiva), 15 (radioterapia com visita), 17 e 20 (casos clínicos) [CONFIRMAR NO CATÁLOGO] | "Quimioterapia: preciso de estrutura na clínica?" (H-A10.2) |
| 2. Coordenação | Coordenação com nome e titulação | ESP. Juliana Vieira Cirillo (também "MSc Esp. Juliana V Cirillo" na lista: [CONFIRMAR titulação e autorização]); 36 nomes listados; sem número de turma | "Quero discutir caso com quem trata câncer todo dia." [SUPOSIÇÃO] |
| 3. Do diagnóstico ao paliativo | Programa completo | Diagnóstico (imagem, patologia, molecular), neoplasias por sistema, cuidado paliativo e dor, psico-oncologia, nutrição | "Conduzir com protocolo e segurança." (gancho da campanha) |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Biossegurança e protocolo de quimioterapia na prática presencial, antes de aplicar na sua clínica." |
| P2 | "Presenciais em São Paulo distribuídos ao longo do curso, com mês publicado." |
| P3 | "Prova de bolsa de Oncologia em 27/11/2026." |
| P4 | "Prova de bolsa para a Pós-graduação em Oncologia Veterinária." |
| EAD | "Não há turma EAD aberta. Quimioterapia e cirurgia oncológica são presenciais." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantos dos seus pacientes idosos chegaram com um nódulo este mês?" |
| Consciente do problema | "Indicar quimioterapia sem dominar a biossegurança é risco para você e para a equipe." |
| Consciente da solução | "500 h, presenciais de quimioterapia, eletroquimioterapia, cirurgia e radioterapia." |
| Pronto | "{TP-TURMA:68628}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68628}. Prova de bolsa de Oncologia em 27/11." | |
| Tempo | "Um fim de semana por mês; os presenciais têm mês publicado." | Data exata de alguns presenciais [CONFIRMAR] |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso; sem número de turma |
| "Pós ou curso de eletroquimioterapia?" (área) | "O curso livre foca uma técnica; a pós cobre a oncologia inteira, com eletroquimioterapia num dos presenciais." | Livre 560 só por link |

**Vocabulário:** pós-graduação em oncologia veterinária; pós em oncologia veterinária de pequenos animais em São Paulo; especialização em oncologia de cães e gatos; biossegurança em quimioterapia; prova de bolsa de oncologia veterinária; "pós em onco vet" só em busca. Evitamos: "referência nacional em educação", "o curso garante".

**TP da área:** 68628: "30x de R$ 1.298,00 no cartão ou boleto. Total de R$ 38.940,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Oncologia Veterinária: quimioterapia com biossegurança na prática presencial." |
| Post | "Quimio, eletroquimio, cirurgia, radioterapia: um presencial para cada tratamento." |
| WhatsApp | "Oi! A Pós-graduação em Oncologia Veterinária começa em 10/04/2027. Quer ver o cronograma dos presenciais?" |
| E-mail (assunto) | "Oncologia na prática: o que acontece em cada presencial" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Tratamento oncológico na prática presencial." |

**Nunca dizer nesta área:** número da turma; "referência nacional"; número de casos de câncer sem fonte; promessa de cura ou resultado clínico.

---

## 12. A11. Laboratório (68608, 68615, 333; provas 68651, 68658)

**Linha e cursos (catálogo):** Pós-graduação em Hematologia Veterinária, São Paulo, semipresencial, 500 h, turma VIII, 28/11/2026 (68608). Pós-graduação em Patologia Clínica, São Paulo, semipresencial, 500 h, turma VII, 20/03/2027 (68615; ficha não lida). Pós-graduação em Citopatologia Veterinária, São Paulo, semipresencial, 500 h, turma I, 27/03/2027 (333; ficha não lida; o posicionamento registra 1 professor e coordenação "UFAPE": prova de docente fraca).

**Situação e bloqueios:** 68608 com 1ª mensalidade vencendo em 29/10/2026. Prova 68651 um dia antes da turma (D2): mesma regra da A8.

**Mensagem central:** Fechar o caso sem depender só do laboratório: mielograma, coagulograma e medicina transfusional na prática presencial.

**Elevador:**
1. A Pós-graduação em Hematologia Veterinária tem 24 módulos e 500 h, com teoria online e três módulos presenciais em São Paulo.
2. Pelo cronograma, nos presenciais você faz coagulograma, coleta de mielograma e coleta e processamento de hemocomponentes.
3. A área tem ainda Patologia Clínica (turma VII) e Citopatologia (turma I), em 2027.

| Pilar | Afirmação | Prova (ficha 68608) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Coleta e processamento na prática | Três presenciais com procedimento | Módulo 6 (coagulograma: TP, TTPA, TSMO, tromboelastograma; coleta de mielograma); módulo 13 (medicina transfusional: coleta e processamento, triagem de doadores); módulo 22 (farmacologia, prova escrita) [CONFIRMAR NO CATÁLOGO] | "Dependo do laboratório ou do colega para fechar o caso." (H-A11.2) |
| 2. Coordenação e continuidade | Coordenação com nome e titulação; turmas VIII e VII | Coordenação de 68608: ESP. Mariana Aldemundo Pereira di Vincenzo [CONFIRMAR autorização]; 14 nomes; catálogo: 68608 VIII, 68615 VII [CONFIRMAR uso como prova] | "É para clínico ou só para laboratório?" (H-A11.3) |
| 3. Do hemograma ao paciente crítico | Programa aplicado à clínica | Módulos de patologia clínica, imunomediadas, infecciosas, anemias, coagulopatias, hematologia felina, paciente crítico e cirúrgico | "Quero interpretar o hemograma com segurança." [SUPOSIÇÃO] |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Mielograma, coagulograma e transfusão: os três presenciais trazem o laboratório para a sua decisão clínica." |
| P2 | "Três presenciais em São Paulo; o resto online." |
| P3 | "Citopatologia é turma I e tem a menor parcela do padrão 30x no catálogo: {TP-CURTO:333}." |
| P4 | "Prova de bolsa para a Pós-graduação em Patologia Clínica em 27/11/2026." (68651 só com decisão A-C2) |
| Laboratório | "Para quem trabalha em laboratório ou quer levar o laboratório para a clínica." (público de 68608 [CONFIRMAR]) |
| EAD | "Não há turma EAD aberta. Coleta e processamento são presenciais." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Quantos hemogramas você assina por semana sem discutir?" |
| Consciente do problema | "Anemia sem causa definida é caso aberto." |
| Consciente da solução | "500 h, presenciais de mielograma, coagulograma e transfusão." |
| Pronto | "Turma VIII em 28/11/2026. {TP-TURMA:68608}." (até 29/10; depois, sem a frase da 1ª mensalidade) |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68608}. Patologia Clínica tem prova de bolsa em 27/11." | |
| Tempo | "Três presenciais em dois anos." | |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso |
| "Hematologia, patologia clínica ou citopatologia?" (área) | "Hematologia foca o sangue e a medula; patologia clínica, os exames da rotina; citopatologia, a citologia." | Ementas de 68615 e 333 [CONFIRMAR NO CATÁLOGO] |

**Vocabulário:** pós-graduação em hematologia veterinária; pós-graduação em patologia clínica veterinária; pós-graduação em citopatologia veterinária; pós em análises clínicas veterinárias [SUPOSIÇÃO de público]; prova de bolsa de hematologia veterinária; prova de bolsa de patologia clínica veterinária; "pós em hemato vet" só em busca. Evitamos: "o curso garante", autoridade docente em 333 antes de corrigir a ficha.

**TP da área:** 68608: "30x de R$ 1.180,00 no cartão ou boleto. Total de R$ 35.400,00 + matrícula de R$ 250,00." 68615: "30x de R$ 1.180,00 no cartão ou boleto. Total de R$ 35.400,00 + matrícula de R$ 250,00." 333: "30x de R$ 935,00 no cartão ou boleto. Total de R$ 28.050,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Hematologia Veterinária: mielograma, coagulograma e transfusão na prática. Turma VIII em 28/11." |
| Post | "Do hemograma à transfusão: os três presenciais da Hematologia." |
| WhatsApp | "Oi! A turma VIII da Pós-graduação em Hematologia Veterinária começa em 28/11/2026. Quer o cronograma?" |
| E-mail (assunto) | "Hematologia, patologia clínica ou citopatologia: qual pós escolher" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Três módulos presenciais de coleta e processamento." |

**Nunca dizer nesta área:** "faça a prova de Hematologia e entre na turma de 28/11"; autoridade docente de 333; "para clínico e laboratório" sem a ficha dizer.

---

## 13. A12. Neurologia (68616; prova 68654)

**Linha e curso (catálogo):** Pós-graduação em Neurologia e Neurocirurgia Veterinária, São Paulo, semipresencial, 500 h, turma IX, 08/05/2027 (68616). Fora: 677 e 701 (verificar).

**Situação e bloqueios:** o Workshop de Neuromonitorização (20 e 21/11, linha Eventos) fala com público próximo: não juntar as duas ofertas na mesma peça; o cupom SIMPNEUROMONIT não vale para a Pós. A ficha não traz público-alvo [CONFIRMAR NO CATÁLOGO].

**Mensagem central:** Do exame neurológico à neurocirurgia da coluna: presenciais em sequência clínica, terminando com quatro módulos de neurocirurgia.

**Elevador:**
1. A Pós-graduação em Neurologia e Neurocirurgia Veterinária tem 24 módulos e 500 h, com teoria online e presenciais em São Paulo.
2. Pelo cronograma, os presenciais vão da neuroanatomia e do exame neurológico à coleta de líquido cerebroespinhal, video-otoscopia e neurocirurgia da coluna cervical, toracolombar e lombossacra e do crânio.
3. A turma IX começa em 08/05/2027.

| Pilar | Afirmação | Prova (ficha 68616) | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Do exame à neurocirurgia | Presenciais em sequência clínica | Presenciais nos módulos 2, 5, 9, 10, 13, 17, 20, 21, 22, 23 e 24; coleta de LCE e biópsias (9); semiologia e localização de lesões (10); neurocirurgia cervical, toracolombar, lombossacra e do crânio (21 a 24) [CONFIRMAR NO CATÁLOGO] | "Paciente neurológico eu encaminho." (H-A12.1) |
| 2. Coordenação e turma IX | Coordenação com nome e titulação; nona turma | Dra. Carolina Gonçalves Dias Lima [CONFIRMAR autorização]; 15 nomes; catálogo turma IX [CONFIRMAR uso como prova] | "Preciso ter experiência?" (H-A12.3) |
| 3. Avaliação no presencial | Avaliações presenciais a cada bloco | Seis avaliações presenciais às sextas às 14h (módulos 5, 9, 13, 17, 20, 24); presenciais de sexta a domingo em vários módulos | "Quero saber se estou aprendendo de fato." [SUPOSIÇÃO] |

**Persona e praça:**

| Para quem | Mensagem |
|---|---|
| P1 | "Localizar a lesão antes de pedir a ressonância: semiologia neurológica presencial no cronograma." |
| P2 | "Alguns presenciais são de sexta a domingo; as datas estão no cronograma." |
| P3 | "Prova de bolsa de Neurologia em 27/11/2026." |
| P4 | "Prova de bolsa para a Pós-graduação em Neurologia e Neurocirurgia Veterinária." |
| EAD | "Não há turma EAD aberta. Neurocirurgia é presencial." |

**Estágios de consciência:**

| Estágio | Mensagem |
|---|---|
| Inconsciente | "Convulsão, paresia, hérnia de disco: quantos você conduz até o fim?" |
| Consciente do problema | "Exame neurológico bem feito muda o pedido de exame e a conversa com o tutor." |
| Consciente da solução | "500 h, do exame neurológico à neurocirurgia da coluna, com presenciais." |
| Pronto | "{TP-TURMA:68616}." |

**Objeções:**

| Objeção | Resposta | Limite |
|---|---|---|
| Investimento | "{TP-TURMA:68616}. Prova de bolsa de Neurologia em 27/11." | Sem cupom do workshop |
| Tempo | "Presenciais de sábado e domingo, alguns de sexta a domingo, com datas no cronograma." | Dizer os três dias |
| Turma não fechar | "A turma abre com no mínimo 20 alunos; compre passagem só com a turma confirmada." | Sem reembolso |
| "Neurologia ou neurocirurgia?" (área) | "Esta pós começa pela neurologia clínica e termina com quatro módulos de neurocirurgia." | 677 sem chamada |

**Vocabulário:** pós-graduação em neurologia e neurocirurgia veterinária; pós em neurologia veterinária em São Paulo; especialização em neurologia de cães e gatos; prova de bolsa de neurologia veterinária; "pós em neuro vet" só em busca. Evitamos: "referência nacional em educação", "o curso garante".

**TP da área:** 68616: "30x de R$ 1.192,40 no cartão ou boleto. Total de R$ 35.772,00 + matrícula de R$ 250,00."

**Versões curtas:**

| Formato | Texto |
|---|---|
| Anúncio | "Pós-graduação em Neurologia e Neurocirurgia Veterinária: do exame neurológico à cirurgia de coluna." |
| Post | "Os quatro módulos finais de neurocirurgia da turma IX." |
| WhatsApp | "Oi! A turma IX da Pós-graduação em Neurologia e Neurocirurgia Veterinária começa em 08/05/2027. Quer o cronograma?" |
| E-mail (assunto) | "Turma IX de Neurologia: do exame à neurocirurgia" |
| Página (subtítulo) | "500 h, semipresencial, São Paulo. Presenciais do exame neurológico à neurocirurgia." |

**Nunca dizer nesta área:** cupom SIMPNEUROMONIT para a Pós; workshop e pós na mesma peça; 677 e 701 com chamada; "referência nacional".

---

## 14. A13. Medicina felina (prova 68652; sem turma aberta)

**Situação:** nenhuma turma aberta (650 em "verificar"). A prova 68652 está em D4 (sem turma de destino) [CONFIRMAR destino]. A página da prova traz frase ligada ao MEC e regras contraditórias (resultado por e-mail, WhatsApp ou site; matrícula em 7 ou 10 dias). **Não há posicionamento de venda de pós em Felinos até existir turma aberta** (posicionamento, seção 3.1).

**Mensagem central (só para conteúdo e para quando houver destino):** Medicina felina estudada pelo que o gato tem de próprio: conteúdo da prova e bibliografia publicados.

**Elevador:**
1. A prova de bolsa de Medicina de Felinos de 27/11/2026 traz o conteúdo cobrado e a bibliografia sugerida na página.
2. Os temas vão de cat friendly practice e farmacologia felina a doenças infecciosas, renais, endócrinas, respiratórias e cardiomiopatias.
3. O destino da bolsa será informado pela Ufape antes de qualquer divulgação paga.

| Pilar | Afirmação | Prova | Palavras do candidato [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Conteúdo publicado | Você sabe o que estudar | Ficha 68652: lista de conteúdo e 5 obras de bibliografia sugerida | "O que cai na prova?" (H-PB1) |
| 2. Regras da bolsa | Mesmas 11 bolsas das outras provas | Ficha: 2 de 50% (monitoria), 4 de 25%, 5 de 10%; nota de corte 7,0 | "Vale pagar a inscrição?" (H-PB3) |
| 3. Destino transparente | A bolsa só é divulgada com turma de destino | Estratégia de campanha, D4 | "Fiz a prova, e a turma?" (persona, seção 5.1, linha A13) |

**Persona e praça:** P1 com foco felino e P4: só conteúdo (artigo-guia de estudo, se a Ufape aprovar a isca) até o destino. Sem praça Goiânia. EAD: "Não há turma EAD aberta."

**Estágios:** Inconsciente: "O gato não é um cão pequeno." Consciente do problema: "Farmacologia felina tem idiossincrasias que mudam a dose." Consciente da solução e Pronto: bloqueados até haver turma.

**Objeções:** investimento, tempo e turma: sem resposta de venda até haver turma. "A bolsa vale para qual turma?": "O destino será informado pela Ufape." Nunca indicar 650.

**Vocabulário:** prova de bolsa de medicina de felinos; o que cai na prova de bolsa de medicina felina; bibliografia; especialização em felinos (só conteúdo). Evitamos: "cat friendly" como selo, "área sem concorrência", "a pós de felinos mais completa".

**TP da área:** nenhum de turma. TP-PROVA só depois do destino.

**Versões curtas (só conteúdo):** Post: "Cat friendly, FIV, FeLV, PIF, DTUIF: os temas que a prova de Medicina de Felinos cobra." Os demais formatos ficam bloqueados.

**Nunca dizer nesta área:** "inscreva-se" com anúncio pago por área; "reconhecida pelo MEC"; prazo de matrícula ou canal de resultado da página de Felinos; "única" ou "mais completa".

---

## 15. A14. Outras especialidades (por curso)

Regra: cada subseção é uma casa de mensagens curta de um curso. Nenhum desses cursos tem prova de bolsa aberta, salvo Odontologia (68655, sem turma, D4).

### 15.1 Pós-graduação em Medicina Interna Equina (341)

**Catálogo:** São Paulo, semipresencial, 500 h, turma I, 20/03/2027. **Bloqueios:** promoção de 20% com texto cortado (P16): nunca em peça; texto de reembolso com sentido oposto: nada sobre reembolso; a ficha cita segundo local em Indaiatuba, SP, e "equipamento hospital veterinário" [CONFIRMAR local da prática].

**Mensagem central:** Medicina interna equina com prática presencial na maioria dos temas, do paciente crítico ao neonato.

**Elevador:** 1. São 24 módulos e 500 h, com teoria online e módulos online e presenciais. 2. Pelo cronograma, há prática do paciente crítico, cirurgia, cardiologia, respiratório, digestivo, locomotor, UTI neonatal, podologia e odontologia equina. 3. A turma I começa em 20/03/2027.

| Pilar | Afirmação | Prova (ficha 341) | Palavras [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática por sistema | Módulos com parte presencial em quase todos os sistemas | Módulos 3 a 8, 12, 13, 16 a 19 e 22 marcados online e presencial; módulo 24 com estágio obrigatório [CONFIRMAR NO CATÁLOGO] | "Onde são as práticas com cavalos?" (H-A14.3) |
| 2. Coordenação | Nome e titulação | Esp. Maria Augusta Berlingieri [CONFIRMAR autorização]; 9 nomes | "Saí da faculdade com pouca prática em equinos." (H-A14.1) |
| 3. Do campo ao hospital | Neonato a campo e UTI neonatal | Módulos 11 e 12 | [SUPOSIÇÃO] |

**Persona:** veterinário de equinos que viaja (perto de P2): "Datas publicadas até 2029 para planejar as viagens." EAD: sem turma EAD. **Objeções:** investimento: "{TP-TURMA:341}" sem desconto; tempo: "um fim de semana por mês"; turma: "mínimo de 20 alunos; passagem só com a turma confirmada"; área, "Onde é a prática?": "O time informa o local de cada módulo" [CONFIRMAR]. **Estágios:** Inconsciente: "Cólica de madrugada: você conduz ou encaminha?" Problema: "A graduação dá poucas horas de medicina interna equina." Solução: "24 módulos com prática na maioria dos temas." Pronto: "{TP-TURMA:341}." **Vocabulário:** pós-graduação em medicina interna equina; pós em medicina equina; especialização em clínica de equinos. **TP:** "30x de R$ 1.450,00 no cartão ou boleto. Total de R$ 43.500,00 + matrícula de R$ 250,00." **Curtas:** Anúncio: "Pós-graduação em Medicina Interna Equina: prática do paciente crítico ao neonato." Post: "Podologia, UTI neonatal, cólica: o cronograma da turma I." WhatsApp: "Oi! A turma I da Pós-graduação em Medicina Interna Equina começa em 20/03/2027. Quer o cronograma?" E-mail: "Medicina equina, módulo a módulo." Página: "500 h, semipresencial, São Paulo. Prática presencial na maioria dos temas." **Nunca dizer:** "20% de desconto"; "possibilidade de bolsas"; "formados inseguros e sem diferencial" (texto da página); reembolso.

### 15.2 Pós-graduação em Infectologia Veterinária (679)

**Catálogo:** São Paulo, semipresencial, 500 h, turma IV, 03/04/2027. **Bloqueio:** o link da planilha ("Citopatologia 03/04") aponta para esta página (P3) [CONFIRMAR]; a página diz "única pós-graduação semipresencial em infectologia veterinária do mundo" e fala em empregabilidade: nada disso vai para peça. As considerações da ficha não trazem a orientação de passagem.

**Mensagem central:** Doença infecciosa na rotina clínica, do diagnóstico à vacinação, com prática laboratorial presencial.

**Elevador:** 1. 24 módulos, 500 h, teoria online. 2. Presenciais de prática laboratorial (coleta, armazenamento e envio de amostras), zoonoses com coleta para exame de raiva e controle de infecção hospitalar. 3. Turma IV em 03/04/2027.

| Pilar | Afirmação | Prova (ficha 679) | Palavras [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Laboratório na prática | Três presenciais | Módulos 3, 13 e 22 [CONFIRMAR NO CATÁLOGO] | "Coletei, mas a amostra chegou ruim." |
| 2. Coordenação e turma IV | Nome como na ficha | Ricardo L. S. Gonzalez (sem titulação na ficha) [CONFIRMAR titulação e autorização]; 6 nomes | [SUPOSIÇÃO] |
| 3. Infecção por sistema | Módulos por órgão | Módulos 14 a 21 | [SUPOSIÇÃO] |

**Persona:** P1: "Antibioticoterapia, sepse e zoonoses tratadas em módulos próprios." EAD: sem turma EAD. **Objeções:** investimento: "{TP-TURMA:679}" (sem a frase de passagem até a Ufape confirmar que vale para esta turma); tempo: três presenciais; turma: "mínima de 20 alunos" (ficha). **Estágios:** Inconsciente: "Qual foi o último antibiótico que você escolheu sem cultura?" Problema: "Infecção mal conduzida volta, e às vezes resistente." Solução: "500 h, do diagnóstico à vacinação, com prática de laboratório." Pronto: "{TP-TURMA:679}." **Vocabulário:** pós-graduação em infectologia veterinária; especialização em infectologia de cães e gatos; doenças infecciosas. **TP:** "30x de R$ 1.100,00 no cartão ou boleto. Total de R$ 33.000,00 + matrícula de R$ 250,00." (só depois de corrigir o link, P3) **Curtas:** Anúncio: "Pós-graduação em Infectologia Veterinária: do diagnóstico à vacinação." Post: "Antibioticoterapia, sepse, zoonoses: o programa em 24 módulos." WhatsApp: "Oi! A turma IV da Pós-graduação em Infectologia Veterinária começa em 03/04/2027. Quer o cronograma?" E-mail: "Infectologia na rotina, módulo a módulo." Página: "500 h, semipresencial, São Paulo. Prática laboratorial presencial." **Nunca dizer:** "única do mundo"; "melhoria da empregabilidade".

### 15.3 Pós-graduação em Obstetrícia, Neonatologia e Biotecnologias da Reprodução em Cães e Gatos (382)

**Catálogo:** São Paulo, semipresencial, 500 h, turma I, 22/05/2027. A ficha não traz público-alvo nem turma mínima [CONFIRMAR].

**Mensagem central:** Reprodução de cães e gatos com prática presencial de inseminação, andrologia, ultrassom reprodutivo, obstetrícia e neonatologia.

**Elevador:** 1. 24 módulos, 500 h, teoria online. 2. Oito presenciais, pelo cronograma: exame ginecológico e inseminação por endoscopia, exame andrológico e criopreservação de sêmen, ultrassonografia reprodutiva, cirurgia, obstetrícia, neonatologia, manejo de canis e gatis e inseminação intrauterina cirúrgica. 3. Turma I em 22/05/2027.

| Pilar | Afirmação | Prova (ficha 382) | Palavras [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática reprodutiva | Oito presenciais | Módulos 4, 6, 9, 12, 15, 17, 20 e 22 presenciais [CONFIRMAR NO CATÁLOGO] | "Quero fazer inseminação com segurança." |
| 2. Coordenação | Nome e titulação | ESP. Patricia Salla, Dra. Marilu Martins Gioso [CONFIRMAR autorização] | [SUPOSIÇÃO] |
| 3. Do embrião ao neonato | Ciclo completo | Módulos 1 e 14 a 17 | [SUPOSIÇÃO] |

**Persona:** P1: "Da inseminação ao neonato, com oito presenciais." EAD: sem turma EAD. **Objeções:** investimento: "{TP-TURMA:382}" sem número de turma mínima até confirmar; tempo: oito presenciais; turma: "a turma só abre com o número mínimo de alunos" [CONFIRMAR número]. **Estágios:** Inconsciente: "Quantas cesarianas de emergência você atendeu este ano?" Problema: "Neonato crítico pede protocolo próprio." Solução: "500 h, oito presenciais de reprodução." Pronto: "{TP-TURMA:382}." **Vocabulário:** pós-graduação em reprodução de cães e gatos; obstetrícia veterinária; neonatologia veterinária. **TP:** "30x de R$ 1.125,00 no cartão ou boleto. Total de R$ 33.750,00 + matrícula de R$ 250,00." **Curtas:** Anúncio: "Reprodução de cães e gatos na prática: inseminação, andrologia, obstetrícia." Post: "Do exame andrológico ao neonato: os oito presenciais." WhatsApp: "Oi! A turma I começa em 22/05/2027. Quer o cronograma?" E-mail: "Reprodução de cães e gatos, módulo a módulo." Página: "500 h, semipresencial, São Paulo. Oito módulos presenciais." **Nunca dizer:** público de criadores sem a ficha dizer; turma mínima sem número confirmado.

### 15.4 Pós-graduação em Geriatria Veterinária (699)

**Catálogo:** São Paulo, semipresencial, 500 h, turma I, 22/05/2027. **Bloqueio:** a ficha aceita "estudantes a partir do último ano" e ao mesmo tempo exige diploma; lotação mínimo 15 e máximo 40; módulos 11 e 19 com datas fora de ordem: **nenhuma peça antes da correção** [CONFIRMAR NO CATÁLOGO].

**Mensagem central (para quando a ficha for corrigida):** O paciente idoso visto inteiro: dor, cognição, nutrição, doença crônica e cuidado paliativo numa especialização dedicada.

**Pilares:** 1. Programa dedicado ao idoso (20 módulos: síndromes geriátricas, disfunção cognitiva, dor, paliativos, nutrição; ficha). 2. Coordenação: Prof. Caio Cavalcanti Balençuela [CONFIRMAR titulação e autorização]; 32 nomes. 3. Presenciais nos módulos 6 (fisioterapia, avaliação funcional) e 20 (exame clínico geriátrico, escalas de dor) e aulas a cada 15 dias à noite [CONFIRMAR]. **Objeções e versões curtas:** suspensas até a correção. **TP:** "24x de R$ 1.375,00 no cartão ou boleto. Total de R$ 33.000,00 + matrícula de R$ 250,00." **Nunca dizer:** "escassez de formação especializada no país"; "estudantes podem se matricular"; "única" ou "primeira".

### 15.5 Pós-graduação em Medicina de Silvestres (60)

**Catálogo:** São Paulo, semipresencial, 360 h, turma I, 28/05/2027. Turma mínima de 15 (ficha).

**Mensagem central:** Peixes, anfíbios, répteis, aves e mamíferos silvestres: 18 módulos por grupo, com quatro práticas presenciais.

**Elevador:** 1. 18 módulos, 360 h, módulos de sexta a domingo. 2. Presenciais de prática nos módulos 3, 8, 13 e 18. 3. Turma I em 28/05/2027.

| Pilar | Afirmação | Prova (ficha 60) | Palavras [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Prática por grupo | Quatro presenciais | Módulos 3, 8, 13, 18 [CONFIRMAR NO CATÁLOGO] | "Atendo exótico, mas aprendi sozinho." |
| 2. Coordenação | Nome como na ficha | Carolina Nery (sem titulação na ficha) [CONFIRMAR titulação e autorização]; 10 nomes | [SUPOSIÇÃO] |
| 3. Horário publicado | Sexta 14h às 20h, sábado 8h às 18h, domingo 8h às 13h | Ficha | "Sexta à tarde dá?" |

**Persona:** veterinário de exóticos: "Um grupo animal por bloco, com prática presencial." EAD: sem turma EAD. **Objeções:** investimento: "{TP-TURMA:60}" com "turma mínima de 15 alunos"; tempo: três dias por módulo; turma: "compre passagem só com a turma confirmada". **Estágios:** Inconsciente: "Chegou um réptil na sua clínica: e agora?" Problema: "Silvestres quase não aparecem na graduação." Solução: "360 h, quatro práticas presenciais." Pronto: "{TP-TURMA:60}." **TP:** "24x de R$ 1.237,50 no cartão ou boleto. Total de R$ 29.700,00 + matrícula de R$ 250,00." **Curtas:** Anúncio: "Pós-graduação em Medicina de Silvestres: um grupo animal por bloco, com prática presencial." Post: "Peixes, anfíbios, répteis, aves e mamíferos: os 18 módulos." WhatsApp: "Oi! A turma I da Pós-graduação em Medicina de Silvestres começa em 28/05/2027. Quer o cronograma?" E-mail: "Silvestres, grupo a grupo." Página: "360 h, semipresencial, São Paulo. Quatro práticas presenciais." **Nunca dizer:** "R$ 77,3 bilhões"; "maior diversidade biológica do mundo"; número de espécies da página.

### 15.6 Pós-graduação em Inteligência Artificial na Saúde (719)

**Catálogo:** São Paulo, semipresencial, 360 h, turma I, 08/05/2027. Público da ficha: médicos, enfermeiros, gestores de saúde, profissionais de TI e engenheiros clínicos. **Fora das personas P1 a P4.** Posicionamento próprio pendente (cmo e Ufape) [CONFIRMAR]; ato regulatório [CONFIRMAR NO CATÁLOGO]. Coordenação: Prof. Ricardo Bontempo [CONFIRMAR autorização]. Requisito: notebook com i3, Windows e 8 GB (ficha). **Nenhuma mensagem de venda nesta rodada.** TP de referência: "18x de R$ 666,67 no cartão ou boleto. Total de R$ 12.000,00 + matrícula de R$ 250,00." **Nunca dizer:** "alinhado às normas do MEC"; ligação com veterinária.

### 15.7 Odontologia (prova 68655)

D4: sem turma aberta (68662 e 678 em "verificar"). Só aparece na lista da peça mestre das provas, se a Ufape confirmar que segue à venda. Nenhuma outra mensagem.

---

## 16. Provas de bolsa de 27/11/2026: mensagem geral e variação por área

Coerente com saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md (campanha única, camadas mestre, área e turma; destinos D1 a D4).

### 16.1 Casa de mensagens da prova

**Mensagem central (a da campanha):** "Faça a prova de bolsa da Pós-graduação na sua especialidade. Inscrição de R$ 100,00 e 11 bolsas por prova, de 10% a 50%. Prova presencial em 27 de novembro."

**Elevador:**
1. Em 27/11/2026 há 22 provas de bolsa da Pós-graduação, em 19 especialidades: todas em São Paulo e três delas (Anestesiologia, Cardiologia e Clínica Cirúrgica) também em Goiânia.
2. Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%, com nota de corte 7,0.
3. Você decide a matrícula depois do resultado, em até 10 dias úteis.

| Pilar | Afirmação | Prova | Palavras [SUPOSIÇÃO] |
|---|---|---|---|
| 1. Custo baixo para tentar | Inscrição pequena diante da pós | Catálogo, seção 3 (TP-PROVA) | "Vale pagar para tentar?" (H-PB3) |
| 2. Bolsas contadas | 11 por prova, com percentuais publicados | Páginas das provas; contexto/pos-graduacao.md [CONFIRMAR NO CATÁLOGO] | "Quantas bolsas tem?" (H-PB3) |
| 3. Regras claras | Nota de corte, recurso, prazo de matrícula, não acumulativa | Páginas das provas | "E depois do resultado?" (H-PB7) |

**Objeções da prova:**

| Objeção | Resposta | Limite |
|---|---|---|
| "Pago e posso não ganhar nada" | "São 11 bolsas por prova e a nota de corte é 7,0. {TP-PROVA-CURTO}" | Nunca chance de aprovação; nunca "garanta sua bolsa" |
| "A bolsa vale para qual turma?" | Só com destino confirmado: "A bolsa vale para a turma [código], início em [data]." Antes: "O destino será informado pela Ufape." | Camada turma bloqueada até a confirmação |
| "É online?" | "Não. É presencial, das 9h às 13h, em São Paulo ou Goiânia." | Endereço de Goiânia [CONFIRMAR] (página 68640 mostra SP) |
| "Somo com outro desconto?" | "A bolsa não é acumulativa." | |
| "Quanto fica a parcela com bolsa?" | "O time mostra a conta da turma de destino." | Base de cálculo [CONFIRMAR]; nenhuma conta em peça |

**Estágios:** Inconsciente: "A pós da sua área tem prova de bolsa." Problema: "O valor da pós pesa? A prova é o primeiro passo." Solução: "11 bolsas por prova, de 10% a 50%." Pronto: "{TP-PROVA:código}. Inscreva-se na prova."

**Persona e praça:** P4 é o público principal; P1, P2 e P3 recebem a camada mestre. Goiânia: anúncios segmentados citam só 68640, 68642 (depois da correção dos links) e 68644. EAD: "A prova é presencial; não há versão online."

**Versões curtas (mestre):** Anúncio: "Prova de bolsa da Pós-graduação em 27/11: 11 bolsas por prova, de 10% a 50%." Post: "Como funciona a prova de bolsa: 11 bolsas, nota 7,0, matrícula em até 10 dias úteis." WhatsApp: "Oi! Em 27/11 tem prova de bolsa da Pós-graduação na sua especialidade. Quer as regras?" E-mail (assunto): "Prova de bolsa em 27/11: as regras inteiras." Página (bloco citável): texto da pesquisa-de-palavras-chave, seção 5.1, depois de [CONFIRMAR NO CATÁLOGO] as regras.

**Nunca dizer (prova):** "bolsa de 50%" ou "bolsas de até 50%" sem a distribuição; "garanta sua bolsa"; "últimas bolsas"; número de inscritos; comparação com a Anclivepa em peça pública; "antes que acabe" em referência ao concorrente; turma ou data de destino sem confirmação; frase de certificação; data de resultado ou prazo final de inscrição (não existem).

### 16.2 Variação por área

Nome em peça: "Prova de bolsa para a Pós-graduação em <área>". Gancho: hipótese da persona [SUPOSIÇÃO].

| Área | Provas e destino (campanha 3.2) | Gancho | Mensagem de área | Bloqueio |
|---|---|---|---|---|
| A1 | 68640 Goiânia (D1, 68609); 68639 SP (D3) | Segurança no protocolo anestésico | "Prova de bolsa para a Pós-graduação em Anestesiologia Veterinária em Goiânia, 27/11." | 68639 sem turma; endereço de Goiânia [CONFIRMAR] |
| A2 | 68659 (D1, 68636); 68642 (D1, 289); 68641 (D3) | O cardiopata que vai para outro colega | "Prova de bolsa para a Pós-graduação em Pneumologia Veterinária, 27/11." | 68641 e 68642 só depois de corrigir os links |
| A3 | 68645 (D1, 68635); 68660 (D3) | O paciente crítico no plantão | "Prova de bolsa para a Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, 27/11." | 68660 sem destino em SP |
| A4 | 68644 Goiânia (D1, 68632); 68643 SP (D3) | Operar com segurança na própria clínica | "Prova de bolsa para a Pós-graduação em Clínica Cirúrgica de Cães e Gatos em Goiânia." | 68643 sem destino; 662 não é destino |
| A5 | 68661 (D1, 68629); 68647 (D2); 68649 (D4) | Fazer o exame na própria clínica | "Prova de bolsa para a Pós-graduação em Ultrassonografia de Pequenos Animais, 27/11." | 68649 só na lista mestre |
| A6 | 68650 (D2) | O quadro digestivo recorrente | Só camada mestre até o destino | Não ligar à turma 68606 |
| A7 | 68648 (D1, 68617); 68653 (D4) | O endócrino de longo prazo | "Prova de bolsa para a Pós-graduação em Endocrinologia de Pequenos Animais." | 68653 só na lista mestre |
| A8 | 68646 (D2) | A dermatite que volta | Só camada mestre até a decisão A-C2 | Não citar a turma de 28/11 |
| A9 | nenhuma (68656 fora do ar) | - | - | Fora da campanha |
| A10 | 68657 (D1, 68628) | Protocolo e segurança no oncológico | "Prova de bolsa para a Pós-graduação em Oncologia Veterinária." | Sem número de turma |
| A11 | 68658 (D1, 68615); 68651 (D2) | Fechar o caso sem depender do laboratório | "Prova de bolsa para a Pós-graduação em Patologia Clínica." | 68651 sem citar a turma de 28/11 |
| A12 | 68654 (D1, 68616) | O neurológico que hoje é encaminhado | "Prova de bolsa para a Pós-graduação em Neurologia e Neurocirurgia Veterinária." | Não juntar com o workshop |
| A13 | 68652 (D4) | - | Só lista mestre | Página com frase do MEC e regras contraditórias |
| A14 | 68655 Odontologia (D4) | - | Só lista mestre | Sem turma |

A camada turma ("A bolsa vale para a turma [código], início em [data]", seguida de {TP-TURMA:código}) só entra em qualquer área depois da confirmação do destino pela Ufape.

---

## 17. Estágios de consciência: resumo de uso

Cada seção de área traz a sua tabela de estágios. O que muda de um estágio para outro:

| Estágio | Uso | Canal típico [SUPOSIÇÃO] |
|---|---|---|
| Inconsciente | Pergunta sobre a rotina, sem curso nem preço | Post orgânico, Reels |
| Consciente do problema | Nomeia a dificuldade clínica, sem prometer resultado | Post, artigo, anúncio de alcance |
| Consciente da solução | Formato, prática e carga do curso | Anúncio, página, e-mail |
| Pronto para se matricular | TP completo e contato | WhatsApp com opt-in, página, remarketing |

---

## 18. Auditorias

### 18.1 auditorias/02-estrategia-e-posicionamento.md (aplicada por este agente)

| Item | Resultado | Observação |
|---|---|---|
| O plano tem uma única meta principal | Não se aplica (herdado) | Meta do plano do cmo: turmas de Pós confirmadas com a turma mínima até o início; quantidade-alvo [CONFIRMAR] |
| Persona e curso ou oferta estão nomeados | Atendido | P1 a P4 em cada área; código do catálogo em cada curso e prova |
| Os 8 canais foram avaliados | Não se aplica (herdado) | Vale a seção 5 do plano do cmo e a seção 4 da campanha das provas; aqui só os formatos curtos |
| O posicionamento nomeia a alternativa real | Atendido | Curso curto (A2, A4, A5, A9, A10), residência (A1), EAD (todas), adiar (prova de bolsa) |
| Todo pilar tem prova | Atendido, com pendências | Cada pilar cita a ficha ou o catálogo. Dados só das fichas marcados [CONFIRMAR NO CATÁLOGO]. Pilar de coordenação depende de [CONFIRMAR autorização]. A8 e A4 sem coordenação nominal na ficha. A13 e 699 sem pilar de venda |
| As regras de voz têm exemplos | Atendido | Versões curtas por área e "nunca dizer" com o texto atual das páginas como contraexemplo |
| Cabe no tempo e na verba | Não se aplica | Sem verba nesta etapa |
| Nenhuma promessa de emprego, aprovação ou salário | Atendido | Nenhuma mensagem promete resultado; textos de página com "empregabilidade" (679) e "oportunidades" (68617) listados como proibidos |
| Preços, bolsas e condições do catálogo ou marcados | Atendido | Preço só nos TP, copiados do catálogo; regras da bolsa da campanha e do contexto, com [CONFIRMAR NO CATÁLOGO]; descontos de 341, 359 e 352 fora |

### 18.2 auditorias/conformidade-educacional.md

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga, duração batem com o catálogo | Atendido. Nomes no padrão "Pós-graduação em"; 68632 presencial; 707 com 600 h; 68635 e 68623 com 750 h; 68629, 657, 359, 352, 60 e 719 com 360 h; 698 com 370 h |
| Dados do curso | Só turma "aberta" recebe chamada | Atendido. Turmas em "verificar" sem chamada; 699 e 719 sem mensagem de venda; 662 sem preço |
| Dados do curso | Modalidade clara | Atendido. Nenhuma mensagem de EAD como oferta |
| Regulação | Pós sem "reconhecida pelo MEC" | Atendido. Textos de página com MEC listados em "nunca dizer" (68610, 68635, 68632, 68628, 68616, 68652, 719) |
| Regulação | Nota MEC | Atendido. Nenhuma |
| Promessas | Sem emprego, salário, aprovação | Atendido |
| Promessas | Superlativos com fonte | Atendido. "Menor total" e "menor parcela" são contagens do catálogo, sem "a mais barata" em peça |
| Promessas | Comparação com concorrente | Atendido. Nenhuma peça cita concorrente |
| Preço (CDC) | Valor, parcelas e condições completas | Atendido pelos TP; frase da 1ª mensalidade retirada onde venceu |
| Preço (CDC) | Bolsa com regra, público e validade | Atendido em parte. Regras da bolsa completas; destino, base de cálculo e requisito de inscrição [CONFIRMAR]. Provas D4 fora de anúncio por área |
| Preço (CDC) | Urgência real | Atendido. Só datas de início e de prova |
| Pessoas e dados | Autorização de imagem | Pendente. Coordenações nomeadas como prova interna, todas [CONFIRMAR autorização]: nenhuma entra em peça sem autorização registrada |
| Pessoas e dados | Nenhum dado pessoal de aluno ou candidato | Atendido |
| Pessoas e dados | WhatsApp e e-mail com consentimento | Atendido. Versões de WhatsApp e e-mail são para a base com opt-in |
| Plataformas | Página de destino entrega o que a mensagem promete | Ressalva. 26 das 30 páginas têm frase ligada ao MEC (P2); 698, 68641, 68642, 662 e 679 com data ou link errado (P3, P4); página 68640 com endereço de SP. Anúncio para essas páginas segue o bloqueio do plano do cmo |
| Anúncios | Sem característica pessoal de quem vê | Atendido. P3 aparece como "turma de menor total", nunca "você que ganha pouco" |
| Anúncios | Sem escassez falsa, caixa alta excessiva | Atendido |

**Resultado:** aprovado como rascunho de mensagens para o qa-de-marketing. Bloqueado para peça final: qualquer peça com docente (autorização), qualquer peça com dado só das fichas antes de [CONFIRMAR NO CATÁLOGO], A13, 699, 719, 662, 698 (data), provas 68641 e 68642 (links), camada turma das provas (destino), frase de reembolso em todas as áreas.

Conferência de forma: sem travessão e sem meia-risca neste arquivo; nenhum dado pessoal; nenhum número fora do catálogo, das fichas ou das saídas citadas.

---

## 19. Próximo passo

- Próximo agente sugerido: **estrategia-de-conteudo**, usando as tabelas de estágio de consciência e o vocabulário de cada área. Na camada 2, o criador-de-ganchos (2.3) e os criativos-de-anuncio (2.4) partem das versões curtas e da seção 16; o autoridade-docente (2.5) só com as autorizações.
- Pedidos à Ufape (sem custo, sem publicação): autorização de nome e titulação de cada coordenação citada; grafia e titulação divergentes (68609, 707, 68628, 679, 60, 699); coordenação nominal de 68610 e 68632; turma mínima de 68635 e 382; local da prática de 341; correção da ficha de 699; destino das provas; endereço da prova de Goiânia; o que entra em "valores de inscrição"; uso da numeração de turma como prova.
- Notas para outros arquivos (este agente não edita arquivo alheio): posicionamento-pos, seção 2.1: trocar "condições à vista" por "condições claras" (já sinalizado pela estrategia-de-oferta). Ficha 68632 sem coordenação; ficha 679 sem orientação de passagem e reembolso; ficha 382 sem público e sem turma mínima.

---

## Lista 1. Fatos com fonte

- Catálogo, seção 2 (26/10/2026): modalidade, carga horária, turma, início e preço de 707, 68604, 68606, 68610, 698, 68608, 657, 341, 289, 68615, 333, 679, 68632, 68635, 366, 68628, 68617, 68636, 68609, 662, 719, 68616, 68629, 359, 699, 382, 68623, 578, 352 e 60, usados só nos TP e nas linhas de curso.
- Catálogo, seção 3: 22 provas abertas em 27/11/2026, em 19 especialidades (3 com prova também em Goiânia), inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão); 68656 fora do ar.
- contexto/pos-graduacao.md e páginas das provas: 11 bolsas (2 de 50% monitoria, 4 de 25%, 5 de 10%), nota 7,0, 2 dias úteis de recurso, 10 dias úteis de matrícula, não acumulativa, intransferível.
- Fichas: coordenação, número de módulos, módulos presenciais e conteúdo citados em cada pilar (68609, 289, 68635, 68632, 68629, 68606, 68617, 68610, 707, 68628, 68608, 68616, 68652, 341, 679, 382, 699, 60, 719); turma mínima de 20 nas fichas de turma, 15 em 60 e na prova 68652, 15 a 40 em 699; horários de 707, 60, 68609 e 699; microscópio individual e mutirões supervisionados em 707; locais "sede da UFAPE, SP" e "Ufape Goiânia".
- Textos de página proibidos citados em "nunca dizer": frases ligadas ao MEC (68610, 68635, 68632, 68628, 68616, 68652, 719), "única do mundo" e "empregabilidade" (679), "carente de profissionais" (68606), "renomados" (68617), "R$ 77,3 bilhões" (60), promoção de 20% (341), desconto dos 10 primeiros (359, 352).
- estrategia-de-oferta: textos-padrão, vencimento da 1ª mensalidade de 68610 e 68608 em 29/10/2026, regras de uso.
- estrategia-de-campanha: mensagem central da prova, camadas, destinos D1 a D4, ganchos.
- pesquisa-de-palavras-chave: termos e perguntas por área.
- plano do cmo: áreas A1 a A14 e pendências P1 a P16.

## Lista 2. Suposições

- [SUPOSIÇÃO] Todas as "palavras do candidato" (hipóteses de fala de P1 a P4, com IDs H-*), sem voz real.
- [SUPOSIÇÃO] Personas P1 a P4 e o público de 352, 366, 382, 657 e 359.
- [SUPOSIÇÃO] Ganchos por área (herdados da campanha).
- [SUPOSIÇÃO] Texto "Fale com o time para saber como entrar na turma".
- [SUPOSIÇÃO] Canais típicos por estágio de consciência.
- [SUPOSIÇÃO] Que o público de Goiás e estados vizinhos prefira Goiânia.
- [SUPOSIÇÃO] Que a mensagem de "condições claras" reduza o medo de pagar antes de saber.

## Lista 3. Dados que faltam

- [CONFIRMAR autorização] Nome e titulação de todas as coordenações citadas; titulação divergente em 68609 (Viera e Vieira), 707 (Dra. e MSC. Juliana Jorge), 68628 (ESP. e MSc Esp.), 679 e 60 (sem titulação), 68635, 699 e 719 ("Prof.").
- [CONFIRMAR] Coordenação nominal de 68610 e 68632.
- [CONFIRMAR NO CATÁLOGO] Cronogramas, módulos presenciais, horários e turma mínima (só nas fichas); módulos com data fora de ordem em 68609, 68617 e 699.
- [CONFIRMAR] Turma mínima de 68635, 382 e 719; regra de 15 ou 20 nas provas.
- [CONFIRMAR] Uso da numeração de turma como prova; turma de 68628, 68617 e 662 (P5).
- [CONFIRMAR] Local da prática por curso (sede, Ufape Goiânia, Ufape Clínica, Indaiatuba em 341).
- [CONFIRMAR] O que entra em "valores de inscrição"; data de confirmação da turma; regra de reposição de módulo; regra de entrada tardia (707, 68604, 68606, 68610, 68608).
- [CONFIRMAR] Destino das 22 provas, base de cálculo da bolsa, aprovado sem bolsa, data do resultado, prazo de inscrição, endereço em Goiânia, requisito de inscrição.
- [CONFIRMAR] Pré-requisitos de 657, 359 e 698; público de 68608, 366, 382 e 68616.
- [CONFIRMAR] Correções do site: 698 (data), 68641 e 68642 (links), 662 e 679 (links), ficha de 699.
- [PREENCHER COM A REGULAÇÃO] Texto de certificação da Pós; ato regulatório de 719.
- [CONFIRMAR] Posicionamento próprio de 719.
- Fichas não lidas nesta etapa: 68604, 698, 68636, 352, 657, 359, 68623, 578, 662, 366, 68615, 333 e as provas além de 68652; as mensagens desses cursos usam só o catálogo e as saídas anteriores.

## Fontes

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (seções 2 e 3); templates/casa-de-mensagens.md; contexto/cursos/pos/ (68609, 289, 68635, 68632, 68629, 68606, 68617, 68610, 707, 68628, 68608, 68616, 68652, 341, 679, 382, 699, 60, 719); saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md; saidas/03-seo-e-busca/pesquisa-de-palavras-chave-pos-2026-10-26.md; saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md; saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md; auditorias/02-estrategia-e-posicionamento.md; auditorias/conformidade-educacional.md.

Externas: nenhuma nesta etapa.
