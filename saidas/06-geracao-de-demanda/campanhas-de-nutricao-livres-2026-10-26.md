# Campanhas de nutrição de Cursos Livres: leads que ainda não estão prontos (27/10/2026 a 24/01/2027)

- **Agente:** campanhas-de-nutricao (departamento 06, Geração de Demanda), etapa 1.28 da camada 1
- **Linha:** livres
- **Data:** 26/10/2026 (segunda-feira)
- **Status:** rascunho para o qa-de-marketing (auditorias/06-geracao-de-demanda.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação da pessoa do marketing. São regras e esboços para o CRM enviar só a quem deu consentimento. A squad não dispara nada. Nada é publicado, enviado ou pago.
- **Escopo:** sequências de nutrição (prioridade 5 da fila D2) para quem deixou contato em Livres e ainda não comprou, e o degrau seguinte de quem já comprou. Não reescreve as réguas com data que já existem: RL1 (kits dos itens com data), RL2 (serviço do presencial), RL3 (grupos novos), RL4 (acesso do online), RL6 (retomada pelo time), RL7 (pagamento não concluído) e a newsletter (RL9).
- **Entradas lidas:**
  - .claude/agents/campanhas-de-nutricao.md (não cita skill; usei .claude/skills/mapear-regua/SKILL.md como apoio de formato)
  - CLAUDE.md
  - docs/execucao-2026-10-26.md (decisões 1 a 13)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md, seção 12 (D1 a D4, D6 a D8, D10 a D13). Ela vale sobre qualquer arquivo ainda não atualizado. Nota de numeração: a encomenda cita "D14 UTM" e "D15 frase do curso livre"; na seção 12 o padrão de UTM é D11 e D12 e a frase do curso livre é D13. Usei os itens pelo conteúdo.
  - contexto/ufape-geral.md, contexto/cursos-livres.md, contexto/catalogo-de-cursos.md (seções 4, 5 e 7)
  - saidas/07-email-whatsapp-relacionamento/estrategia-de-relacionamento-livres-2026-10-26.md (1.26; SL1 a SL12, RL1 a RL10, calendário 7.1 e 8.2)
  - saidas/07-email-whatsapp-relacionamento/estrategia-de-relacionamento-pos-2026-10-26.md (regras herdadas)
  - saidas/07-email-whatsapp-relacionamento/jornada-do-aluno-geral-2026-10-26.md (1.27; passagem 2 e lacunas)
  - saidas/07-email-whatsapp-relacionamento/newsletter-geral-2026-10-26.md (edições 1 a 7)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-2026-10-26.md e copy-de-mensagens-eventos-2026-10-26.md (só os mapas, para a conta do teto)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-livres-2026-10-26.md (apostas 1 a 5)
  - saidas/04-conteudo/estrategia-de-conteudo-livres-2026-10-26.md (1.19; pilares, camada de apoio à decisão, rotação 5.3 e peças L)
  - saidas/06-geracao-de-demanda/campanhas-de-nutricao-pos-2026-10-26.md (arquivo irmão desta etapa, para não repetir dias)
  - Referência de formato: saidas/06-geracao-de-demanda/campanhas-de-nutricao-graduacao-2026-10-26.md (nenhum conteúdo copiado)
  - auditorias/06-geracao-de-demanda.md, auditorias/07-email-e-whatsapp.md, auditorias/conformidade-educacional.md
- **Não abri** faculdade.ufape.com.br. Nenhuma busca na web.
- **Dados pessoais:** nenhum. Só segmentos e campos do CRM entre colchetes.
- **Números:** não existe tamanho de base, número de contatos com opt-in, taxa de abertura, clique, resposta ou venda. Todo número desse tipo é [CONFIRMAR].

---

## 0. Resumo em 5 linhas

1. Três sequências: NL1 boas-vindas e escolha do formato do lead novo (5 toques em 22 dias), NL2 rotação dos contínuos por área pela base (2 toques por área, com 14 dias ou mais entre eles; é o RL5 da 1.26 com datas) e NL3 degrau seguinte de quem já comprou (2 toques, depois da janela de silêncio; é a parte de campanha do RL8).
2. Nutrição é a última da fila D2 e Livres não tem sub-teto próprio (D1): o kit da turma datada da área sempre passa à frente, e a rotação só entra na base a partir de 30/11.
3. A régua de Livres nunca oferece Pós (D6): a nutrição de Livres só marca a área e a compra no CRM; quem convida para a Pós é o P5, pela tabela única de pares.
4. Toda mensagem com preço ou texto longo leva a frase D13: "Curso livre: não confere diploma e não equivale a graduação ou pós-graduação."
5. As lacunas J1 a J4 são da Pós e de serviço; em Livres a lacuna que pesa é J15 (sem registro do primeiro acesso do online, a janela de silêncio conta da compra).

---

## 1. Regras que valem para toda sequência deste arquivo

### 1.1 Teto, fila e calendário (seção 12 do plano do cmo)

| Regra | O que vale | Fonte |
|---|---|---|
| Teto por contato | até 2 WhatsApp e 2 e-mails de campanha por semana somando todas as linhas e a newsletter; no máximo 1 mensagem de campanha por dia em qualquer canal [SUPOSIÇÃO de número, R1]. Livres não tem sub-teto | D1 |
| Fila | 1 serviço; 2 toque principal com data (inclui o kit RL1 da área); 3 data mais próxima e GUT; 4 follow-ups; 5 nutrição (newsletter, NL1, NL2, NL3); 6 reativação | D2 |
| Supressão | toque suprimido não acumula; a sequência segue no toque seguinte, no dia dele | D2 |
| Janela | WhatsApp: dia útil, das 9h às 18h. E-mail: qualquer dia, das 7h às 19h (a squad propõe dia útil para nutrição) [SUPOSIÇÃO] | D1 |
| Dias sem campanha | 02/11; 20 e 21/11; 25/12; 31/12; 01/01; de 21/12 a 03/01 só serviço e manutenção; 26 e 27/11 sem campanha para quem está na campanha das provas | D1 |
| Janela de silêncio | do pedido pago até 2 dias úteis depois do último dia do curso; online e minicurso: 7 dias corridos depois do primeiro acesso, ou da compra enquanto a plataforma não informar o acesso (J15) [SUPOSIÇÃO de prazo]. Durante a janela, o comprador não entra em campanha nova de nenhuma linha | D8 |
| Intervalo de projeto | NL1 com 3 dias ou mais entre toques; NL2 com 14 dias ou mais entre os dois toques da área (no máximo 1 mensagem de contínuo por contato a cada 2 semanas, regra do RL5); NL3 com 14 dias ou mais [SUPOSIÇÃO de desenho] | 1.26 de Livres, RL5 e RL8 |
| Data de entrada | quem deixa contato num período sem campanha entra no primeiro dia permitido [SUPOSIÇÃO] | este arquivo |

### 1.2 Dono único e exclusões

1. **Item com data da área em régua ativa (RL1 ou RL3):** o contato da área sai da nutrição na data do primeiro toque do kit e só volta depois do último. A nutrição nunca repete o convite do kit.
2. **Nenhuma oferta de Pós** em NL1, NL2 ou NL3 (D6, regra 1 da seção 6 da 1.26 de Livres). A compra é registrada em [comprou_livre_código], [comprou_livre_área] e [data_compra_livre]; a passagem para a Pós é do P5, pela tabela única de pares, depois da janela D8. Nenhuma mensagem cita crédito, combo ou desconto da ponte (D7).
3. **Inscrito ou aprovado na prova de bolsa:** sem campanha de Livres até o fim do prazo de matrícula da prova (D10).
4. **Participante do Workshop:** 616 chega a ele só pela RL1, a partir de 30/11 (D9). Os gravados de evento 700 e 202 são da linha Eventos e ficam fora desta rotação (estão no arquivo de Eventos).
5. **Fora de toda nutrição (SL12 e catálogo):** 95 Auxiliar Veterinário (público de auxiliar, só serviço); 347 e 501 em espanhol (até P17); grupos já iniciados 721, 720, 644 e 68663 (até a regra de entrada tardia, PL4) [CONFIRMAR]; grupos duplicados 643 e 713, 642 e 712 (até a Ufape decidir a página); 623 até a correção do site (o tema de endoscopia aponta para 68637, decisão 13); aprimoramentos 639, 640 e 641 e outros itens em "verificar"; 68634 enquanto estiver em "verificar".
6. **Escada interna:** nenhuma mensagem trata dois cursos da mesma área como se um contivesse o outro (458 e 103; 106 e 202; os quatro gravados de felinos) até a Ufape confirmar a sobreposição (1.19, regra 5 do motor).

### 1.3 LGPD, consentimento e saída

- Campanha só com opt-in por canal (WhatsApp e e-mail separados), com data, origem e finalidade aceita [CONFIRMAR campos e base legal com o encarregado de dados, U13 e UR1].
- Comprador de Livres: mensagens do pedido (confirmação, acesso, endereço, véspera, dia, material do pós-curso) são serviço. NL3 é campanha e só vai a quem tem consentimento de campanha registrado; consentimento dado só para o item comprado não basta (jornada, seção 1, regra 1) [SUPOSIÇÃO de regra].
- Checkout com caixa de consentimento própria, desmarcada, separada por canal [CONFIRMAR se o checkout tem].
- Números de grupos de WhatsApp dos grupos de estudos nunca viram lista; nenhuma mensagem de campanha é postada dentro dos grupos (UR8).
- Todo WhatsApp termina com "Responda SAIR para não receber mais mensagens." Todo e-mail tem link de descadastro.
- SAIR ou descadastro tira de toda campanha de todas as linhas no mesmo dia [SUPOSIÇÃO de prazo]; o serviço de pedido já feito continua, se a Ufape confirmar (R7 da 1.26 da Pós).
- Relatório para a squad só somado por sequência, toque, área e código.

### 1.4 Conteúdo (conformidade)

- Dados de curso (nome, modalidade, carga horária, data, preço) só do catálogo do dia; o CRM confere o status "aberto (contínuo)" na data do envio.
- Preço pelo texto-padrão da oferta de Livres: à vista primeiro, depois parcelas no cartão, depois o total no cartão quando for diferente.
- Frase D13 em toda mensagem com preço e em todo e-mail: "Curso livre: não confere diploma e não equivale a graduação ou pós-graduação."
- Sem frase de certificação, selo ou órgão regulador (a página da 68614 e a de Criocirurgia têm a frase: não repetir). Documento de conclusão só com texto da Ufape [PREENCHER COM A REGULAÇÃO].
- Sem "100% prático", "turma reduzida", "últimas vagas", "vagas limitadas" ou prazo que não esteja na ficha. Nenhuma promoção inventada para contínuo.
- Grupos: "R$ 100,00 à vista ou 1x de R$ 100,00", sem dizer o período (U9).
- Docentes e coordenação: nome e titulação só como na ficha; autorização registrada para todos (decisões 8 e 10). Conteúdo clínico com revisão de docente revisor [CONFIRMAR nome].
- Uma chamada para ação por mensagem; um link por WhatsApp.

---

## 2. Mapa da jornada: do lead novo ao comprador e ao degrau seguinte

| Etapa | Sinal no CRM (nome provisório) | Para onde vai | Nutrição deste arquivo? |
|---|---|---|---|
| Lead novo sem área (SL1) | lead_criado em página ou formulário de Livres, com opt-in, sem [área_de_interesse] | NL1 | sim |
| Lead com área, item datado da área em kit (SL2) | [área_de_interesse] de área com RL1 ou RL3 ativo | kit da área | não; NL1 entrega só o T1 |
| Lead com área, sem kit ativo (SL2) | [área_de_interesse] de área sem item datado na semana | NL1 e depois NL2 | sim |
| Falou com o time e não pagou (SL3) | etapa_do_funil = contato sem pedido pago | RL6, pelo time | não |
| Checkout sem pagamento (SL4) | carrinho_abandonado ou boleto pedido e não pago | RL7 (condicional) | não |
| Comprador antes do curso ou do acesso (SL5, SL6, SL7) | pedido pago | RL2, RL3 ou RL4 (serviço) | não |
| Ex-aluno recente (SL8) | curso realizado, acesso online há 30 dias ou mais [SUPOSIÇÃO da 1.26], grupo encerrado | RL8 serviço (material e pesquisa) e depois NL3 | sim, NL3, depois da janela D8 |
| Aluno ou ex-aluno de Pós com interesse em Livres (SL9) | turma de Pós em andamento ou concluída, opt-in de campanha | NL2 da área, só dentro do teto e depois dos programas da Pós da semana | sim, só NL2 |
| Frio (SL11) | 180 dias sem interação [SUPOSIÇÃO da 1.26] | RL10 (reativação, prioridade 6) | não |

**Candidato pronto** = clicou na página de um item duas vezes ou mais [SUPOSIÇÃO], iniciou checkout, pediu o time ou respondeu com pergunta de compra. A nutrição termina aí.

---

## 3. Sequências

### NL1. Boas-vindas e escolha do formato (lead novo)

| Item | Definição |
|---|---|
| Segmento | SL1 e SL2 novos, com opt-in de pelo menos um canal |
| Gatilho de entrada | lead_criado de Livres com opt-in de campanha. De 27/10 a 29/11, contato que também está na campanha das provas ou na base do Workshop recebe só o T1 (D3: a semana dele já está cheia); contato só de Livres recebe a sequência inteira, sempre atrás do kit da área. Lead criado de 21/12 a 03/01 entra em 04/01 |
| Objetivo | o lead informa a área e sabe qual formato é para ele (presencial, gravado, minicurso, grupo) |
| Saída | comprou (vai para o serviço do pedido); iniciou checkout (RL7, se existir); respondeu pedindo o time (time assume, automação pausa 48 h); área ganhou kit com data (sai na data); SAIR, descadastro, bloqueio ou denúncia; fim do T5 (vai para NL2 da área) |
| Toques | 5 em 22 dias: D0 e-mail, D3 WhatsApp, D8 e-mail, D15 WhatsApp, D22 e-mail |

| Toque | Dia e canal | Função | Objetivo e CTA única | Esboço | Conteúdo de apoio (1.19) |
|---|---|---|---|---|---|
| NL1-T1 | D0, e-mail, até 1 h depois do cadastro, dentro da janela | valor | escolher o formato; CTA "Veja qual formato é para você" | Assunto de trabalho: "Curso prático, gravado, minicurso ou grupo: por onde começar". Entrega o que o formulário prometeu, se prometeu. Tabela curta: quanto tempo dura cada formato (minicurso de 8 h; presenciais e gravados com a carga horária do catálogo) e como se paga. Frase D13 | L27 (curso livre, minicurso, grupo e pós) e o tema "quanto tempo dura cada formato" (camada de apoio à decisão). Plano B: hub de presenciais L06 ou página de listagem [CONFIRMAR URL] |
| NL1-T2 | D3, WhatsApp, dia útil, 10h | qualificação | gravar a área; CTA responder | "Oi, [primeiro_nome]. Aqui é da Faculdade UFAPE. Para te mandar só o que serve para a sua rotina: em que área você quer se aprofundar?" Respostas por número com as áreas da seção 2.3 que têm item aberto, mais "outra". Sem link. SAIR no fim. Sem opt-in de WhatsApp, a pergunta vai no T3 por e-mail | nenhum |
| NL1-T3 | D8, e-mail, dia útil, 9h | objeção | responder "vale pagar se há conteúdo gratuito?" e "quanto custa de verdade"; CTA "Leia como escolher" | Assunto de trabalho: "O que um curso livre te dá que o conteúdo gratuito não dá (e o que ele não dá)". Diferença entre aprender por vídeo solto e ter roteiro, carga horária e quem tira dúvida; preço sem susto: à vista, parcelado e total no cartão. Sem desvalorizar o gratuito. Frase D13 | "Hands-on ou gravado: como escolher" (versão curta de L08) e "Preço sem susto" (camada de apoio à decisão) |
| NL1-T4 | D15, WhatsApp, dia útil, 10h | história e prova | mostrar como é por dentro; CTA link da página do item da área | Com área: o roteiro de um item contínuo da área como está na ficha (o que se vê, em quantas horas, quem ensina, com nome e titulação da ficha). Grupo de estudos: como funciona o encontro, a gravação e a regra de reembolso, como na ficha [CONFIRMAR NO CATÁLOGO]. Sem área: o roteiro de um minicurso de 8 h. Um link. SAIR no fim | pilares P1 (técnica para a rotina), P3 (uma hora de minicurso) e P4 (grupo como comunidade); plano de reaproveitamento 5.4 ("o carrossel vira texto de WhatsApp") |
| NL1-T5 | D22, e-mail, dia útil, 9h | oferta | levar à compra do item da área; CTA "Veja o curso de <área>" | Assunto de trabalho: "<nome do curso como no catálogo>: carga horária, formato e preço". Um item contínuo da área, com texto-padrão de preço e frase D13. Se a área tiver item com data em kit, o T5 é suprimido (o kit é o dono). Sem área: hub de minicursos L15 | hub L15 (minicursos); ficha do item |

### NL2. Rotação dos contínuos pela base, por área (é o RL5 da 1.26, com datas)

| Item | Definição |
|---|---|
| Segmento | SL2 da área em foco e SL8 da área (depois de NL3), com opt-in; SL9 da área só dentro do teto e depois dos programas da Pós da semana. Sem área: fica com a newsletter |
| Gatilho de entrada | fim do NL1; lote da base por área nas datas da tabela abaixo, a partir de 30/11 (de 02 a 29/11 a rotação roda só no orgânico, 1.26 de Livres) |
| Objetivo | venda do contínuo da área, com um toque de técnica ou decisão e um de comunidade ou degrau |
| Saída | comprou; respondeu (time assume); área ganhou kit com data; SAIR, descadastro, bloqueio ou denúncia; fim dos 2 toques (volta na próxima passagem da área, com no mínimo 2 semanas) |
| Toques | 2 por área: T1 e-mail (técnica ou decisão) e T2 WhatsApp (comunidade ou degrau), com 14 dias ou mais entre eles |

| Toque | Canal | Função | Esboço | CTA única |
|---|---|---|---|---|
| NL2-T1 | e-mail, dia útil, 9h | valor e oferta | Assunto de trabalho: "Uma decisão de <área> na rotina, em poucas linhas". Um parágrafo de conteúdo da peça-mãe da semana (revisada por docente quando for clínica) e o contínuo da área que aprofunda, com carga horária, formato e texto-padrão de preço. Frase D13 | "Veja o curso" (página do contínuo) |
| NL2-T2 | WhatsApp, dia útil, 10h | prova e comunidade | "Oi, [primeiro_nome]. Em <área>, a Faculdade UFAPE tem <minicurso, gravado ou grupo> com <docente da ficha, nome e titulação>." Uma frase do que o curso cobre, como na ficha. Um link. SAIR no fim | link da página |

**Calendário do lote por área (contas do teto na seção 4)**

| Área (rotação da 1.19, 5.3) | Contínuos que podem aparecer (catálogo, status aberto) | NL2-T1 (e-mail) | NL2-T2 (WhatsApp) | Quem não recebe nesta passagem |
|---|---|---|---|---|
| A1 Anestesia e dor e A13 Felinos (foco de 30/11) | A1: 488, 131, 102, 602, 461. A13: 105, 340, 157, 459 | ter 01/12 | sex 18/12 | contato que também está no NP2 da Pós (01/12 já tem o NP2-T1; desempate D2); quem está no kit de 68618 na semana de 14/12 (T2 suprimido); compradores de 616 na janela D8 |
| A7 Endocrinologia e nefrologia (foco de 07/12) | 103, 104, 542, 458, 454 (642 e 712 fora até a decisão da página) | ter 08/12 | qua 06/01 | - |
| A2 e A3, ventilação (foco de 14/12) | 507 | seg 14/12 | seg 11/01 | inscritos e contatos no kit de 68618 (o kit é o dono do tema na semana) |
| A8 Dermatologia e A9 Oftalmologia (foco de 04/01) | 463, 627, 482 (720 fora: grupo iniciado) | ter 05/01 | ter 19/01 | - |
| A6 Gastroenterologia e A11 Laboratório (foco de 11/01) | 669, 455; 462, 106 (721 fora: grupo iniciado; 202 é de Eventos) | qua 13/01 | qua 27/01 (plano seguinte) | A3 e A11 em kit de 68638 ou no P5 de A11 na mesma semana, pela fila |
| A10 Oncologia e A4 Cirurgia (foco de 18/01) | 465; 469 (68663 fora: grupo iniciado) | qua 20/01 | qua 03/02 (plano seguinte) | - |
| A14 Outras (foco de 25/01) | 541 (95 fora: auxiliar) | ter 26/01 (plano seguinte) | ter 09/02 (plano seguinte, semana de Carnaval: conferir) | - |
| A2, A3, A5 e A12 (focos de novembro, só no orgânico) | A2: 411, 395, 507; A3: 591, 137, 655, 107; A5: 291; A12: 466 | segunda passagem proposta para fevereiro, no plano de 25/01 a 25/04/2027 | idem | A3 a partir de 01/02 é foco do POCUS (kit de 68638 é o dono) |

### NL3. Degrau seguinte de quem já comprou (parte de campanha do RL8)

| Item | Definição |
|---|---|
| Segmento | SL8: comprador de curso livre com consentimento de campanha que cubra outros cursos |
| Gatilho de entrada | presencial: 14 dias corridos depois do último dia do curso, sempre depois do fim da janela D8; online e minicurso: 30 dias depois do primeiro acesso, ou da compra enquanto J15 estiver aberta [SUPOSIÇÃO de prazo, da 1.26] |
| Objetivo | o degrau seguinte na mesma área, dentro de Livres (recompra, M16 do plano de Livres) |
| Saída | comprou de novo; respondeu (time assume); SAIR, descadastro, bloqueio ou denúncia; fim do T2 (vai para NL2 da área) |
| Toques | 2: T1 e-mail, T2 WhatsApp 14 dias depois |
| O que nunca entra | convite para Pós, crédito ou desconto (D6, D7); "como continuação" quando a Ufape não confirmou que um curso aprofunda o outro |

| Toque | Dia e canal | Função | Esboço | Conteúdo de apoio | CTA única |
|---|---|---|---|---|---|
| NL3-T1 | D0 do gatilho, e-mail, dia útil, 9h | valor e oferta | Assunto de trabalho: "Depois do <curso>: um próximo passo em <área>, se fizer sentido". Uma pergunta que costuma aparecer depois do curso (da pesquisa anônima do RL8, somada, quando existir; sem ela, da peça-mãe da área) e o item da mesma área no degrau seguinte, com texto-padrão de preço e frase D13 | artigo da área: L09 (eco ou eletro, A2), L10 (videotoscopia, A5), L12 (hemogasometria e escolha entre 655 e 107, A3), L16 (felinos, A13) | página do item |
| NL3-T2 | D+14, WhatsApp, dia útil, 10h | comunidade | "Oi, [primeiro_nome]. Se surgiu um caso de <área> depois do curso, o grupo de estudos ou o minicurso da área é um jeito de seguir com colegas." Só item aberto e não iniciado. Sem item assim, o toque leva o artigo da área. SAIR no fim | pilar P4 (grupo como comunidade) | um link |

**Datas-alvo dos compradores dos itens com data do trimestre** (o degrau é [SUPOSIÇÃO] e passa por conferência de sobreposição de conteúdo com a Ufape antes do texto final)

| Item (data da planilha) | Fim da janela D8 | NL3-T1 | NL3-T2 | Degrau na mesma área (catálogo) | Choque conhecido |
|---|---|---|---|---|---|
| 573 Hands-On de Ecocardiografia, SP (14/11/2026; a 1.19 cita 14 e 15/11 [CONFIRMAR NO CATÁLOGO]) | 17/11 se terminar em 15/11; 18/11 se terminar em 14/11 | ter 08/12 | ter 05/01 | gravados de A2: 395 ou 507 (411 é ecocardiograma e pode sobrepor [CONFIRMAR]) | P5 lote 1 (289) a partir de 02/12 tem prioridade para o mesmo contato; NL3 suprimido se a semana estiver cheia |
| 68637 Endoscopia Digestiva, SP (28/11/2026) e 68614 Videotoscopia, SP (28/11/2026) | 01/12 | ter 15/12 | ter 12/01 | A5: 291 | nenhum par de Pós (D6) |
| 616 Imersão Avançada em Anestesia Felina, online (05/12/2026) | 08/12 | qua 06/01 | qua 20/01 | A1: 488, 131, 102, 602, 461; A13: 105, 340, 157, 459 | P5 lote 2 (657) a partir de 04/01 para o mesmo contato; pré-requisito de 657 [CONFIRMAR, U10] |
| 68618 Ventilação Mecânica Aplicada à Anestesia, SP (18/12/2026; só com P6 fechada) | 22/12 | qua 06/01 | qua 20/01 | 507 | par 352 só no pré-lançamento de maio |
| Contínuos online e minicursos | 7 dias depois do primeiro acesso ou da compra | 30 dias depois do primeiro acesso ou da compra | 14 dias depois do T1 | item seguinte da área, pela rotação | J15 aberta |

---

## 4. Conta do teto, semana a semana (pior caso)

Pior caso: contato de A1 com opt-in nos dois canais, que está no NP2 da Pós, na base de Livres de A1 e A13 e foi participante do Workshop. Datas dos kits pela 1.26 de Livres (7.1) e pela seção 12 do cmo (D3).

| Semana | Toques com data e follow-ups (já existem) | Nutrição desta linha | E-mail | WhatsApp |
|---|---|---|---|---|
| S1 a S5, 27/10 a 29/11 | provas, Workshop, kits de 573, 68614 e 68637, 68665, 68666, 616 T1 e T2, newsletter edição 1 | só NL1 do lead novo de Livres que está fora das bases das provas e do Workshop; para os demais, só NL1-T1 se o dia estiver livre | cheio (D3) | cheio (D3) |
| S6, 30/11 a 06/12 | 616 T3 (WA 30/11) e T4 (WA 02/12); newsletter edição 2 (e-mail 03/12; WA 04/12) | NL2-T1 de A1 e A13 em 01/12 | NP2-T1 da Pós (01/12) e newsletter (03/12) = 2: NL2-T1 de A1 e A13 suprimido para este contato; sai para quem é só de Livres | 2 (616); newsletter WA suprimida |
| S7, 07 a 13/12 | 68618 T1 (WA 07/12), T2 (e-mail 08/12), T3 (WA 10/12) | NL2-T1 de A7 em 08/12 (outra área); NL3-T1 de 573 em 08/12 (outra área) | 68618 T2 = 1 | 2 (68618); NP2-T2 da Pós suprimido |
| S8, 14 a 20/12 | 68618 T4 (WA 15/12); newsletter edição 3 (e-mail 17/12); serviço de 68618 em 17 e 18/12 | NL2-T1 de ventilação em 14/12 (fora do kit de 68618); NL3-T1 de 68614 e 68637 em 15/12; NL2-T2 de A1 e A13 em 18/12 | NP2-T3 (16/12) e newsletter (17/12) = 2 | 68618 T4 (15/12) e NL2-T2 (18/12) = 2 |
| S9 e S10, 21/12 a 03/01 | só serviço e manutenção (pós-curso de 616 e 68618 é serviço) | nenhuma | - | - |
| S11, 04 a 10/01 | P5 lote 2 da Pós (657) a partir de 04/01; newsletter edição 4 (qui 07/01) | NL2-T1 de A8 e A9 em 05/01; NL3-T1 de 616 e 68618 em 06/01; NL2-T2 de A7 em 06/01; NL3-T2 de 573 em 05/01 | o P5 de 657 vem antes; para este contato NL3-T1 de 616 só sai se sobrar o segundo e-mail | P5 vem antes |
| S12, 11 a 24/01 | 68638 T1 (e-mail 12/01) e T2 (WA 19/01) para A3; newsletter edição 5 (qui 14/01) | NL2-T2 de ventilação em 11/01; NL3-T2 de 68614 e 68637 em 12/01; NL2-T1 de A6 e A11 em 13/01; NL2-T2 de A8 e A9 em 19/01; NL2-T1 de A10 e A4 em 20/01; NL3-T2 de 616 e 68618 em 20/01 | áreas diferentes, cada contato recebe só a da sua área | idem |

Leitura: para quem está em todas as bases, a nutrição de Livres quase sempre perde para os toques com data e para o NP2 da Pós. Isso é o efeito esperado de D2 e D1 sem sub-teto; quem é só de Livres recebe as sequências inteiras.

---

## 5. Lacunas da jornada (1.27)

| Lacuna | É nutrição? | Encaminhamento |
|---|---|---|
| J1 a J4 | não: são da passagem da prova de bolsa para a matrícula na Pós e são serviço (D4) | arquivo da Pós desta etapa, seção 5; copy-de-mensagens e secretaria |
| J15 (online sem registro do primeiro acesso) | não é nutrição, mas trava o início de NL3 no online | até a plataforma informar o acesso (UR5), a janela D8 e o NL3 contam da compra; pedido ao arquiteto-de-fluxos do campo [primeiro_acesso_em] |
| J9 (participante de evento sem segmento) | não nesta linha | arquivo de Eventos desta etapa |

---

## 6. Campos do CRM, templates da Meta e UTM

### 6.1 Campos (nomes provisórios)

| Campo | Uso | Situação |
|---|---|---|
| [opt_in_email], [opt_in_whatsapp], com data, origem e finalidade aceita | entrada em toda sequência | finalidade aceita ainda não é gravada [CONFIRMAR] |
| [área_de_interesse] | NL1-T2, NL2 | existe no desenho |
| [comprou_livre_código], [comprou_livre_área], [data_compra_livre] | NL3 e marcação para o P5 da Pós | 1.26 de Livres, regra 2 [CONFIRMAR] |
| [primeiro_acesso_em] | janela D8 e NL3 do online | **falta** (J15, UR5) |
| [fim_janela_silencio] | exclusão durante D8 | pedido do cmo (12.10) |
| [kit_ativo_área] | saída de NL1 e NL2 quando a área tem item com data | **novo** [SUPOSIÇÃO de nome] |
| [sequencia_nutricao], [toque_nutricao], [data_entrada_nutricao] | controle e supressão | **novo**, igual ao da Pós |

### 6.2 Templates da Meta (se houver API; nomes [SUPOSIÇÃO])

| Template | Categoria provável | Toque | Variáveis | Botões |
|---|---|---|---|---|
| nutri_livres_qual_area_v1 | Marketing | NL1-T2 | {{1}} = [primeiro_nome] | respostas rápidas por área e "SAIR" |
| nutri_livres_por_dentro_v1 | Marketing | NL1-T4 | {{1}} = [primeiro_nome], {{2}} = curso, {{3}} = docente da ficha | URL e "SAIR" |
| nutri_livres_rotacao_area_v1 | Marketing | NL2-T2 | {{1}} = [primeiro_nome], {{2}} = área, {{3}} = curso | URL e "SAIR" |
| nutri_livres_degrau_v1 | Marketing | NL3-T2 | {{1}} = [primeiro_nome], {{2}} = área | URL e "SAIR" |

### 6.3 UTM (D11 e D12)

- utm_source = email ou whatsapp; utm_medium = crm.
- utm_campaign: link para item = `livres_<código>_<AAAAMM do primeiro envio>` (ex.: livres_454_202612); link para guia sem código = `livres_nutricao_<AAAAMM>` [SUPOSIÇÃO de chave; o arquiteto-de-fluxos confirma].
- utm_content = ID do toque: nl1-t3, nl2-a7-t1, nl3-573-t1.
- Minúsculas, sem acento, sem dado pessoal.

---

## 7. Medição (fórmulas; nenhum número existe hoje)

| Métrica | Fórmula | Fonte | Para quê |
|---|---|---|---|
| Qualificação | leads de NL1 com área gravada até D8 ÷ leads que entraram em NL1 | CRM | o NL1-T2 funciona? |
| Venda do contínuo por área | pedidos pagos com utm_content de NL2 ÷ contatos que receberam NL2, por área | loja, CRM | ordem da rotação na revisão de 4 semanas (1.19, regra 2 do motor) |
| Recompra | segundos pedidos com utm_content de NL3 nos 90 dias ÷ compradores que receberam NL3 | loja, CRM | hipótese M16 do plano de Livres |
| Clique por toque | cliques ÷ entregues, por toque e área | ferramenta de e-mail, UTM | qual função move mais |
| Supressão | toques de NL1, NL2 e NL3 suprimidos pela fila ÷ programados | CRM | quanto do teto sobra para Livres |
| Saúde | (SAIR + descadastro + bloqueio + denúncia) ÷ entregues | ferramentas | frequência humana |

Regras: abertura e leitura só como diagnóstico; nenhuma meta de taxa antes de 4 semanas de envio; revisão mensal junto com a Pós (30/11, 28/12 e 25/01); parada pelo gatilho da 1.26 [SUPOSIÇÃO].

---

## 8. Pedidos de aprovação humana

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| NLR1 | Aprovar NL1, NL2 e NL3 como desenho, para o copy-de-mensagens escrever os textos finais | o RL5 e o RL8 da 1.26 não tinham toques nem datas | sem custo de mídia | lead de Livres sem item datado recebe algo útil; recompra medida | desligar as sequências no CRM |
| NLR2 | Aprovar o calendário do lote de NL2 por área (seção 3) | a rotação só pode entrar na base a partir de 30/11 | sem custo; tamanho por área [CONFIRMAR] | contínuos com venda pela base | cancelar o lote da área antes do envio |
| NLR3 | Decidir a regra de entrada tardia dos grupos iniciados (PL4) e a página que fica entre 643 e 713 e entre 642 e 712 | hoje ficam fora da nutrição | sem custo | mais itens na rotação | manter fora |
| NLR4 | Confirmar com a Ufape os degraus da seção 3 (NL3) e a sobreposição de conteúdo entre 411 e 573, 458 e 103, 106 e 202 | escada interna não pode ser inventada | sem custo | degrau honesto | NL3 só com artigo da área |
| NLR5 | Pedir à plataforma do online o registro do primeiro acesso (UR5) | J15 | sem custo | janela D8 e NL3 corretos no online | contar da compra (como está) |
| NLR6 | Submeter os 4 templates da seção 6.2 à Meta (se houver API) | WhatsApp fora da janela de conversa | custo por conversa [CONFIRMAR] | NL1-T2, NL1-T4, NL2-T2 e NL3-T2 enviáveis | desativar o template |

---

## 9. Auditorias

### 9.1 auditorias/06-geracao-de-demanda.md

Briefing: 1.26 de Livres (RL5, RL8), 1.9 e seção 12 do cmo. Metas: sem número [CONFIRMAR], métricas com fórmula. Isca entrega a promessa: NL1-T1 entrega o que o formulário prometeu (lista de iscas [CONFIRMAR]). Toda captura com nutrição em seguida: NL1. Consentimento em todo formulário e checkout: regra escrita, registro real [CONFIRMAR]. Descontos e prazos batem com o catálogo: nenhuma promoção, crédito ou desconto em nutrição.

### 9.2 auditorias/07-email-e-whatsapp.md

Consentimento e saída (1.3); um objetivo por mensagem (seção 3); primeiras linhas sem promessa nem urgência; mensagem pela etapa (seção 2); regras de saída por sequência; medição por envio (seção 7); WhatsApp em dia útil, das 9h às 18h, com template se houver API (1.1 e 6.2).

### 9.3 auditorias/conformidade-educacional.md (o qa-de-marketing repete)

Frase D13 em toda mensagem com preço e em todo e-mail; nenhuma frase de certificação ou selo; preço à vista, parcelado e total; sem "100% prático" nem urgência sem número; nenhum item em "verificar", iniciado ou duplicado; nenhuma oferta de Pós; nenhum dado pessoal; nenhum travessão nem meia-risca.

---

## Próximo passo

1. Pessoa do marketing: aprovar NLR1 a NLR6.
2. Próximo agente sugerido pela instrução deste agente: **copy-de-mensagens**, para escrever NL1, os textos-base de NL2 por área e NL3, no formato de templates/mensagem.md.
3. arquiteto-de-fluxos: campos da seção 6.1, saída por kit ativo da área e a regra de supressão por contato.

---

## Lista 1. Fatos (com fonte)

- Teto somado sem sub-teto de Livres, fila D2, dias sem campanha e conta do pior caso por semana. Fonte: cmo-geral, 12.2 (D1, D2, D3).
- Régua de Livres nunca oferece Pós; tabela única de pares; nenhuma peça cita crédito. Fonte: cmo-geral, 12.4 (D6, D7).
- Janela de silêncio de 2 dias úteis depois do curso e 7 dias no online. Fonte: cmo-geral, 12.5 (D8).
- UTM com utm_medium=crm; frase do curso livre. Fonte: cmo-geral, 12.7 (D11 a D13).
- 616 chega aos participantes do Workshop só pela RL1, a partir de 30/11. Fonte: cmo-geral, D9.
- SL1 a SL12, RL1 a RL10, rotação a partir de 30/11 com no máximo 1 mensagem de contínuo a cada 2 semanas, RL8 a partir de 14 dias, calendário dos kits (7.1) e das semanas (8.2). Fonte: estrategia-de-relacionamento-livres.
- Rotação por área de 02/11/2026 a 27/02/2027, contínuos por área, regras do motor e peças L06, L08, L09, L10, L12, L15, L16 e L27. Fonte: estrategia-de-conteudo-livres, seções 2.4, 4, 5 e 6.
- Datas e status dos itens citados (573, 68614, 68637, 616, 68618, 68638; contínuos por código). Fonte: contexto/catalogo-de-cursos.md, seções 4, 5 e 7, e plano do cmo, 2.3.
- Página 623 sem campanha nova até a correção. Fonte: docs/execucao-2026-10-26.md, decisão 13.
- Autorização de imagem e citação para todos. Fonte: docs/execucao-2026-10-26.md, decisões 8 e 10.
- Edições 2 a 5 da newsletter. Fonte: newsletter-geral, 3.1, e cmo-geral, D4.

## Lista 2. Suposições

- [SUPOSIÇÃO] Número do teto D1 e janela de envio (R1).
- [SUPOSIÇÃO] Prazos da janela D8 e do início do NL3 (14 dias no presencial; 30 dias no online).
- [SUPOSIÇÃO] Número de toques e intervalos de NL1, NL2 e NL3.
- [SUPOSIÇÃO] Degraus por item na tabela do NL3.
- [SUPOSIÇÃO] Critério de "candidato pronto" e regra de entrada no primeiro dia permitido.
- [SUPOSIÇÃO] Regra de que consentimento dado só para o item comprado não leva NL3.
- [SUPOSIÇÃO] Nomes de campos, templates e a chave livres_nutricao_<AAAAMM>.
- [SUPOSIÇÃO] Segunda passagem de A2, A3, A5 e A12 em fevereiro, no plano seguinte.

## Lista 3. Dados que faltam

- [CONFIRMAR] Tamanho da base e de cada segmento e área; contatos com opt-in por canal; taxas de entrega, clique, resposta, descadastro e bloqueio; vendas por item.
- [CONFIRMAR] Registro de opt-in com finalidade aceita; base legal para usar a lista de compradores (U13); caixa de consentimento no checkout.
- [CONFIRMAR] CRM, ferramenta de e-mail e de WhatsApp, API e templates; custo por conversa.
- [CONFIRMAR] Teto D1 e janela (R1 do cmo).
- [CONFIRMAR] Registro do primeiro acesso no online (UR5, J15).
- [CONFIRMAR] Regra de entrada tardia nos grupos (PL4); página que fica entre 643 e 713 e entre 642 e 712; 68637 depois da correção da 623 (U5).
- [CONFIRMAR] Período coberto pelos R$ 100,00 dos grupos (U9); data de 68618 (P6); modalidade de 616; pré-requisito de 657 (U10).
- [CONFIRMAR] Sobreposição de conteúdo entre 411 e 573, 458 e 103, 106 e 202, e entre os gravados de felinos.
- [CONFIRMAR] Nome do docente revisor; URLs e datas de publicação de L06, L08, L09, L10, L12, L15, L16 e L27.
- [CONFIRMAR NO CATÁLOGO] Se 573 tem um ou dois dias (14/11 no catálogo; 14 e 15/11 na 1.19); carga horária de 68638.
- [PREENCHER COM A REGULAÇÃO] Texto do documento de conclusão do curso livre: nenhuma mensagem usa.

## Fontes

Internas: .claude/agents/campanhas-de-nutricao.md; .claude/skills/mapear-regua/SKILL.md; CLAUDE.md; docs/execucao-2026-10-26.md; contexto/ufape-geral.md; contexto/cursos-livres.md; contexto/catalogo-de-cursos.md; saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seções 2.3 e 12); saidas/02-estrategia-e-posicionamento/estrategia-de-marketing-livres-2026-10-26.md; saidas/04-conteudo/estrategia-de-conteudo-livres-2026-10-26.md; saidas/07-email-whatsapp-relacionamento/estrategia-de-relacionamento-livres-2026-10-26.md; estrategia-de-relacionamento-pos-2026-10-26.md; jornada-do-aluno-geral-2026-10-26.md; newsletter-geral-2026-10-26.md; copy-de-mensagens-pos-2026-10-26.md; copy-de-mensagens-eventos-2026-10-26.md; saidas/06-geracao-de-demanda/campanhas-de-nutricao-pos-2026-10-26.md; saidas/06-geracao-de-demanda/campanhas-de-nutricao-graduacao-2026-10-26.md (formato); auditorias/06-geracao-de-demanda.md; auditorias/07-email-e-whatsapp.md; auditorias/conformidade-educacional.md.

Externas: nenhuma. LGPD e regras da WhatsApp Business API citadas só como referência geral, a conferir pelo encarregado de dados e na política vigente da Meta.
