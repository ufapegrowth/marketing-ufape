# Fluxos de CRM do kit das 8 turmas de abril de 2027 da Pós-graduação (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609): listas, opt-in, saídas, fila D2, NP2 e UTM (onda 3, lote A)

- **Agente:** arquiteto-de-fluxos (departamento 10, Operações de Marketing), encomenda O10 do plano do CMO da onda 3 (versão 2), lote A
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1 (lote A). O lote B (maio) entra em nova versão do mesmo arquivo, sem mudar o nome (O10, prazo 22/01/2027).
- **Encomenda:** O10 de saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (seção 10, linha O10; seções 7.3 e 7.4; decisão 4 da seção 6; regra 11 e E1 a E22 da seção 2): listas por área das turmas de abril, opt-in S2 e S3, saídas, fila D2 com a data de referência da decisão 4 e até 4 toques da onda 3 por dia sempre de áreas diferentes, conferência com a onda 2 e a newsletter, saída da NP2, supressões previstas por semana (só números) e UTM do CRM. 662 sem lista.
- **Status:** rascunho para o qa-de-marketing (auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC8 (seção 15, no -p3). **Nada é ligado, agendado, enviado ou pago.** Toda ação no CRM é de humano, depois da aprovação. Nenhum arquivo de .claude/commands foi criado: o texto do workflow está na seção 16 (-p3).
- **Entradas lidas (em /home/user/marketing-ufape/):**
  - CLAUDE.md (do orquestrador da squad)
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 11, 14, 16, 17 e 18)
  - contexto/ufape-geral.md e contexto/pos-graduacao.md (inteiros); contexto/catalogo-de-cursos.md (cabeçalho, "Como usar" e seção 2, com as linhas das turmas de março a maio)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda3.md (v2): linhas 1 a 410 (seções 0 a 4.13, início) e 560 a 1013 (fim da seção 5, seções 6 a 11 e listas finais). Não lidas: linhas 411 a 559 (kits de maio das turmas 359 a 60 e início da seção 5), que são do lote B.
  - saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-pos-2026-10-27-onda2.md (meu arquivo da onda 2, inteiro: formato, listas, SA1 a SA10, CC1 a CC12, AF1 a AF7, DEC1 a DEC7)
  - saidas/10-operacoes-de-marketing/qa-de-marketing-pos-2026-10-27-onda2c.md (linhas 1 a 300: vereditos, conferências e F1 a F4) e qa-de-marketing-pos-2026-10-27-onda2c2.md (inteiro)
  - saidas/07-email-whatsapp-relacionamento/newsletter-geral-2026-10-26.md (linhas 1 a 400: seções 0 a 6, com o calendário 3.1 e a fila 3.2)
  - saidas/06-geracao-de-demanda/campanhas-de-nutricao-pos-2026-10-26.md (inteiro: NP1, NP2, NP3, lote de 30/11 e UTM)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-2026-10-27-onda3.md (O7, v1): linhas 1 a 553 (seções 0 a 4.2, com o calendário 0.1 e os blocos fixos 0.2) e 1160 a 1471 (8.4 ao fim, com a seção 10, teto D16 por área e semana). Não lidas: linhas 554 a 1159 (textos dos toques de 366, 68628, 68617, 68636 e início de 68609; só a tabela 0.1 importa para o fluxo).
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (linhas 60 a 149: seções 2.3 e 3, notas GUT dos grupos). As seções 12 e 13 (D1 a D17 e E1 a E4) não foram reabertas: o teto, a fila D2 e as regras E1 a E4 vêm das citações do plano da onda 3, da newsletter, da campanhas-de-nutricao-pos e do meu arquivo da onda 2.
  - templates/documento-de-fluxo.md; .claude/skills/mapear-fluxo/SKILL.md; .claude/skills/matriz-gut/SKILL.md; .claude/agents/arquiteto-de-fluxos.md; auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md
- **Não aberto:** faculdade.ufape.com.br; nenhuma busca na web; as fichas das turmas (os dados de curso vêm do catálogo, do plano e do O7); o plano da Graduação (o calendário da Graduação não estava nas entradas: CF6 da onda 2 segue aberto).
- **Dados pessoais:** nenhum. O arquivo fala de listas, campos do CRM entre colchetes e contagens somadas. Nenhum nome de aluno, candidato ou docente.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape tem. [CONFIRMAR NO CATÁLOGO] é dado de curso fora do catálogo e da ficha. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com a origem. Notas de GUT são avaliação do agente, não medida.

---

## 0. Resumo

1. **O que é:** as regras de CRM para os **55 toques** do kit das 8 turmas de abril (16 e-mails e 39 WhatsApp, mais 1 toque reservado de 68632 sem texto): quem entra em cada lista, quem sai, em que ordem a fila D2 decide, como o 1 por dia e o teto de 2 WhatsApp e 2 e-mails por semana são aplicados contra a onda 2, a onda 1 e a newsletter, quando a NP2 da área sai e qual UTM cada link leva. 662 fica sem lista (OU18).
2. **Sete listas por área, não por curso:** cinco novas (L-A3, L-A4, L-A7, L-A10 e L-A14-679) e duas estendidas da onda 2 (L-A1, com a marca de 68609, e L-A2, com a de 68636). L-A4 junta 68632 e 366. Só A14 é por curso, como no plano.
3. **A conta de calendário fecha.** Os 55 toques (31 dias) passam nos cinco testes da seção 8: nenhum cai nas 37 datas da onda 2, nas 6 da onda 1, nas edições da newsletter nem nos dias sem campanha; todo WhatsApp cai em dia útil; o dia mais cheio é 20/01, com 4 toques de 4 áreas diferentes; nenhum dia repete área. A única coincidência é com a versão de WhatsApp da newsletter, se ela existir (19/02, 05/03 e 30/04): o kit vence.
4. **Contagem conferida com o O7 aprovado:** 55 textos (16 e-mails e 39 WhatsApp) e 14 dias com mais de um toque, iguais à seção 0, item 2, e à seção 10.2 do O7; as notas CF1 e CF2 da seção 10 ficam só como registro.
5. **Fila D2 em ordem de prioridade (DEC1):** o CRM percorre os toques candidatos da semana pela data de referência da decisão 4 (início antes de começar, véspera do 3º módulo depois) e aceita o que cabe em 1 por dia e em 2 e 2 por semana. A nota GUT só desempata data igual: 68628 (60), 68632 (45), 68635 e 366 (36, 68635 na frente pela urgência), 68636 (45) e 68617 (36). Seção 6.
6. **Contato de uma só área:** nenhum toque do lote A é cortado; a única supressão prevista é a newsletter de 04/03 para quem está em A4 (366 e 68632 já dão 2 e-mails). **No pior caso** (contato nas áreas que disputam a semana) o lote A tem até **34 toques cortáveis em 11 semanas**; é limite superior por semana, não soma de um mesmo contato. As combinações de duas áreas que já perdem toque estão na seção 9 (-p2).
7. **Achados que não estavam no plano nem no O7 (seção 10, -p2):** (a) a NP2 das áreas de abril aponta para página de turma em 01/12 e 09/12, antes da conferência de 11/12, contra a regra 13 (DEC5); (b) a UTM da NP2 de dezembro e a UTM do kit de janeiro seriam dois nomes para a mesma turma (DEC6); (c) o pré-início de 68632 em 05/04, última mensagem antes de a regra 8 fechar a lista, cai para quem está em A10 (DEC4, opcional); (d) quem está em A1 e A4 perde o W2 de 68609 em 25/02; (e) o E2 de 68609 em 08/03 cai para quem está em A3 ou A4; (f) a saída da NP2 por área precisa de marca de curso em A14 (DEC7).
8. **Saída da NP2 só onde ainda não saiu:** A10 e A7 em 04/01; A3 em 20/01; A4 e A14 (infectologia) em 22/01. A2 (08/12) e A1 (05/01) já saíram na onda 2; só ligam aqui se a flag da onda 2 não estiver ligada. Seção 11 (-p2).
9. **UTM:** utm_medium=crm, utm_campaign=pos_<código>_<AAAAMM do primeiro envio>, igual em todos os toques da turma, e o toque no utm_content. Seção 12 (-p2).
10. **Toda automação é pedido de aprovação:** AF1 a AF7 e DEC1 a DEC8 (o que, por que, quanto, efeito esperado, como desfazer), mais o OC2 por toque. O fluxo de cada turma (gatilho, condição, ação, saída, como desfazer) está na seção 13 (-p3).
11. **Etapas:** 2 chamadas de agente (este arquiteto e o qa-de-marketing) e 7 etapas de humano; o workflow de reuso (seção 16, -p3) tem 2 etapas.

---

## 1. SIPOC e documento de fluxo

### 1.1 SIPOC (skill .claude/skills/mapear-fluxo/SKILL.md)

| Fornecedores | Entradas | Processo | Saídas | Clientes |
|---|---|---|---|---|
| copy-de-mensagens (O7, lote A) | os 55 toques, datas, horas, templates e utm_content (seções 0.1 e 0.2 do O7) | 1. Definir listas, entrada e saída (arquiteto-de-fluxos) | sete listas (cinco novas e duas estendidas), com filtros de entrada e de saída | Pessoa do marketing (aprova) |
| cmo | plano da onda 3 (regras 1 a 13, E1 a E22, seções 7.3 e 7.4, decisão 4), teto D16, fila D2 | 2. Conferir calendário, fila D2 e teto semana a semana contra a onda 2, a onda 1 e a newsletter (arquiteto-de-fluxos) | conta semanal do pior caso, desempate GUT e supressões previstas (só números) | Quem executa no CRM [CONFIRMAR quem] |
| arquiteto-de-fluxos e qa-de-marketing (onda 2) | listas L-A1 e L-A2, SA1 a SA10, CC1 a CC12, AF1 a AF7 e DEC1 a DEC7, aprovados com ressalvas (onda2c, onda2c2) | 3. Conferência do qa-de-marketing (auditorias 10, 07 e conformidade-educacional) | fila D2, limite diário e teto como regras de CRM | Time de captação (vendas de São Paulo e de Goiânia: recebe quem responde) |
| newsletter | calendário de edições (3.1) e regra de fila (3.2) | 4. Aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC8 | saída da NP2 por área e UTM do CRM | cmo (lê só contagens somadas) |
| campanhas-de-nutricao | NP2 (T1 a T4), lote de 30/11 e regra de saída por área | 5. Montar em rascunho e testar no CRM, sem envio ao público (humano) | registro de supressões por semana, motivo, toque e combinação de áreas, só em contagem | analise-de-campanha e analise-de-midia (relatórios somados) |
| Time de captação e financeiro | opt-in por canal e finalidade, pagamento da 1ª mensalidade, resposta de quem falou com o time [CONFIRMAR campos e ferramenta, P15] | 6. Conferir páginas, links e UTM em 11/12 e reconferir em 04/01 (humano; gestor-de-midia confere) | pedidos de aprovação com plano de desfazer | Candidato com opt-in (recebe mensagem com saída fácil) |
| Ufape (regulação, secretaria, coordenação) | respostas a OU3, OU19, OU20, OU21, OU25, OU29, OU34, U11a e P15 [CONFIRMAR] | 7. Liberar o primeiro envio (04/01) e ler toda segunda (humano e cmo) | painel somado dos indicadores | - |
| gestor-de-midia | conferência das páginas no ar em 11/12 e 04/01 (plano, seção 7.2) | - | - | - |

Toda entrada tem fornecedor e toda saída tem cliente. Todo responsável tem uma etapa (seção 1.2) e toda etapa tem um responsável.

### 1.2 Documento de fluxo (templates/documento-de-fluxo.md)

DOCUMENTO DE FLUXO

**Nome do fluxo:** Listas, opt-in, saídas, fila D2, NP2 e UTM do CRM para o kit de abril de 2027 da Pós (679, 68632, 68635, 366, 68628, 68617, 68636 e 68609)

**Linha de negócio:** Pós-graduação

**Gatilho:** aprovação dos pedidos AF1 a AF7 e das decisões DEC1 a DEC8 (pedido à pessoa do marketing, prevista até 11/12/2026 [SUPOSIÇÃO: junto com a conferência das páginas]) e conferência das páginas de abril em 11/12/2026 (publicação pela Ufape até 10/12). Reconferência curta em 04/01/2027. Primeiro envio previsto: 04/01/2027, 9h (E1 de 68628, 68617 e 68636). Reuso: nova turma ou nova onda que entre na mesma base (workflow da seção 16).

**Etapas (responsável / entrada / saída):**
1. arquiteto-de-fluxos / O7 (lote A), plano da onda 3, meu arquivo da onda 2, newsletter-geral, campanhas-de-nutricao-pos / este arquivo (três partes).
2. qa-de-marketing / este arquivo / revisão (O18c do plano, "onda3c", prevista para 04/12).
3. pessoa do marketing / revisão do qa e pedidos AF1 a AF7 e DEC1 a DEC8 / aprovação ou devolução (prevista até 11/12).
4. quem executa no CRM [CONFIRMAR quem] / aprovação / sete listas em rascunho e toques em modo de teste, sem envio ao público (de 14 a 18/12, antes do recesso de 21/12 a 03/01).
5. time de captação com a pessoa do marketing / listas e regras montadas / teste com contatos internos de teste (lista, SAIR, "pagou sai", fila de dia e de semana, UTM). Envio de teste só para endereços e números internos do time, feito por humano.
6. humano; gestor-de-midia confere / páginas publicadas pela Ufape (OC1-A) / conferência em 11/12 de destino, UTM e política de privacidade no formulário, e reconferência curta em 04/01 antes das 9h.
7. humano no CRM, com o cmo na revisão de segunda-feira / liberação toque a toque (OC2) / envios e leitura somada.

**Etapas de agente:** arquiteto-de-fluxos (etapa 1) e qa-de-marketing (etapa 2). Duas chamadas ao Claude.

**Etapas de aprovação humana:** depois de cada uma das duas etapas de agente (a plataforma pede); depois, uma aprovação por toque (OC2 do plano), a conferência de 11/12, a reconferência de 04/01 e a liberação do primeiro envio. Aprova: a pessoa do marketing que aprovou o plano geral, até a tabela de aprovação de contexto/ufape-geral.md ser preenchida (A9) [CONFIRMAR].

**Checagens de QA e conformidade (qa-de-marketing e auditorias/conformidade-educacional.md):** auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md (seção 17, no -p3). Itens que dependem do documento: opt-in por canal e saída fácil; "réguas têm regras de saída"; "WhatsApp só em horário comercial, com frequência humana e template aprovado quando usar a API"; "nenhum dado pessoal nos arquivos de trabalho".

**Ferramentas usadas (CRM, Chatwoot, n8n, ClickUp, Supabase, GA4, Meta Ads, Google Ads):** CRM e ferramentas de e-mail e de WhatsApp [CONFIRMAR quais, P15 e U11a]; GA4 para ler a UTM [CONFIRMAR]. Nenhuma aplicada pela squad: as regras são texto para quem executa. Sem Supabase nem n8n neste fluxo. Meta Ads e Google Ads: fora (são da mídia).

**Concluído quando:** (1) as sete listas existem em rascunho no CRM com os filtros das seções 2 e 3; (2) os 55 toques estão agendados em modo de teste nas datas da seção 7 e o 56º (68632 em 04/05) não está agendado; (3) o teste de humano confirma, com contatos internos de teste: no máximo 1 mensagem por dia, no máximo 2 WhatsApp e 2 e-mails por semana, a ordem da fila nos casos da seção 9, SAIR e descadastro funcionando, "pagou a 1ª mensalidade sai" funcionando e a UTM de cada link igual à da seção 12; (4) a saída da NP2 acontece nas datas da seção 11; (5) a lista de 68632 fecha às 23h59 de 09/04/2027 enquanto a OU3 estiver aberta; (6) o qa-de-marketing aprovou e a pessoa do marketing aprovou AF1 a AF7 e DEC1 a DEC8. O primeiro envio só ocorre depois do OC2 de cada toque, da conferência de 11/12 e da reconferência de 04/01.

**Data de revisão:** 11/12/2026 (aprovação dos pedidos e conferência das páginas) [SUPOSIÇÃO], 04/01/2027 (reconferência e revisão de ritmo do plano), 22/01/2027 (O10 do lote B, que refaz a conta das semanas com maio) e a cada chegada de OU3, OU19, OU20, OU21, OU25, OU29, U11a ou P15.

---

## 2. As listas por área e turma

Uma lista é um filtro no CRM, não uma planilha de pessoas. Nenhum contato aparece neste arquivo. O tamanho de cada lista é [CONFIRMAR, OC2] e só entra como número somado.

| Lista | Área | Turmas que alimenta (catálogo) | Quem pode estar nela (filtro de entrada, seção 3) | Toques | Primeiro toque | Atendimento de quem responde |
|---|---|---|---|---|---|---|
| L-A10 (nova) | A10 Oncologia | 68628, Pós-graduação em Oncologia Veterinária, São Paulo, semipresencial, início 10/04/2027 (número da turma fora, P5) | S2 e S3 com [área_de_interesse]=A10 | 7 (2 e-mails e 5 WhatsApp), de 04/01 a 28/04 | seg 04/01, 9h | vendas de São Paulo |
| L-A7 (nova) | A7 Endocrinologia e nefrologia | 68617, Pós-graduação em Endocrinologia de Pequenos Animais, São Paulo, semipresencial, início 17/04/2027 (número da turma fora, P5) | S2 e S3 com [área_de_interesse]=A7 | 7, de 04/01 a 06/05 | seg 04/01, 9h | vendas de São Paulo |
| L-A2 (estendida da onda 2) | A2 Cardiorrespiratório | 68636, Pós-graduação em Pneumologia Veterinária, turma VIII, São Paulo, semipresencial, início 17/04/2027 [CONFIRMAR OU21: data só no site], na lista que já tem 289 | S2 e S3 com [área_de_interesse]=A2 | 7, de 04/01 a 30/04 | seg 04/01, 9h | vendas de São Paulo |
| L-A3 (nova) | A3 Emergência, terapia intensiva e clínica médica | 68635, Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, turma V, São Paulo, semipresencial, início 10/04/2027 | S2 e S3 com [área_de_interesse]=A3 | 7, de 20/01 a 03/05 | qua 20/01, 9h | vendas de São Paulo |
| L-A4 (nova) | A4 Cirurgia, ortopedia e reabilitação | 68632, Pós-graduação em Clínica Cirúrgica de Cães e Gatos, turma V, Goiânia, presencial, início 10/04/2027; e 366, Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, turma I, São Paulo, semipresencial, início 10/04/2027 [CONFIRMAR OU20] (duas marcas de turma na mesma lista) | S2 e S3 com [área_de_interesse]=A4 | 68632: 6 (2 e-mails e 4 WhatsApp), de 22/01 a 05/04, mais 1 reservado em 04/05; 366: 7, de 05/02 a 03/05 | sex 22/01, 9h (68632); sex 05/02, 9h (366) | 68632: vendas de Goiânia; 366: vendas de São Paulo |
| L-A1 (estendida da onda 2) | A1 Anestesiologia e dor | 68609, Pós-graduação em Anestesiologia Veterinária, turma VIII, Goiânia, semipresencial, início 24/04/2027, na lista que já tem 657 | S2 e S3 com [área_de_interesse]=A1 | 7, de 20/01 a 11/05 | qua 20/01, 9h | vendas de Goiânia |
| L-A14-679 (nova, por curso) | A14 Outras (só infectologia) | 679, Pós-graduação em Infectologia Veterinária, turma IV, São Paulo, semipresencial, início 03/04/2027 [CONFIRMAR OU19] | S2 e S3 com [área_de_interesse]=A14 **e** [curso_de_interesse]=infectologia ou 679 (campo da onda 2) | 7, de 22/01 a 26/04 | sex 22/01, 9h | vendas de São Paulo |

Total: 7 + 7 + 7 + 7 + 13 + 7 + 7 = **55 toques programados com texto** (16 e-mails e 39 WhatsApp), mais **1 reservado** (PI de 68632 em 04/05, sem texto e sem agendamento). Pelas tabelas do O7 cada turma tem 7 toques e 68632 tem 6 mais o reservado.

Pontos de desenho:

1. **Área, não curso, onde o plano mede por área.** Em A1, A2, A3, A4, A7 e A10 o kit cobre o segmento inteiro da área. Só A14 é por curso (plano geral, seção 2.3, nota; plano da onda 3, seção 7.3).
2. **A4 é uma lista com duas marcas de turma.** O contato de A4 recebe os toques de 68632 desde 22/01 e os de 366 desde 05/02 (EN8: quem entra depois só recebe os toques seguintes). As respostas vão para vendas de Goiânia (68632) ou de São Paulo (366), conforme o toque respondido.
3. **L-A14-679 e a falha fechada.** Sem a marca [curso_de_interesse] a lista fica vazia e nada de 679 sai pelo CRM (campo ausente recusa, nunca libera). Se o CRM não tiver o campo, o humano cria a marca com os leads que chegaram pela página ou pela campanha de 679 [CONFIRMAR como separar, P15]. DEC7.
4. **Praça.** Contato de qualquer praça pode estar em L-A1 e L-A4; o texto de 68609 e 68632 já diz que o campus é Goiânia. Quem responde vai para vendas de Goiânia [SUPOSIÇÃO: não filtrar por praça; o plano não pede filtro].
5. **Listas estendidas dependem da onda 2.** Se AF1 da onda 2 não for aprovada, esta onda cria L-A1 e L-A2 com o mesmo filtro, sem a marca de 657 e de 289.
6. **Marca de turma por contato.** Cada contato guarda, por turma, o último toque recebido e o motivo de saída (seção 14, no -p3). É o que permite "quem pagou 68632 sai dos toques de 68632" e a saída da NP2 no primeiro toque.
7. **662:** nenhuma lista, nenhuma regra, nenhum toque (espera total, OU18). O gestor-de-midia cuida da campanha que roda hoje (OC8 do plano).

---

## 3. Regra de entrada e opt-in S2 e S3

Um contato só entra em uma lista, e só recebe um toque, se **todas** as condições abaixo forem verdadeiras no dia do envio. Sem registro, não entra. As regras EN1 a EN10 são as da onda 2, aprovadas com ressalvas no onda2c; EN11 e EN12 são novas.

| # | Regra | Detalhe | Fonte |
|---|---|---|---|
| EN1 | Opt-in por canal | [opt_in_email]=sim para e-mail e [opt_in_whatsapp]=sim para WhatsApp, cada um com data, origem e finalidade aceita. Opt-in de um canal não vale para o outro: quem tem só e-mail recebe só os e-mails da turma, e quem tem só WhatsApp recebe só os WhatsApp (o kit mínimo é por turma, não por contato). Sem opt-in em nenhum canal, fora. | E4 (cmo-geral, 13.3); estrategia-de-relacionamento-pos, 3.2 |
| EN2 | Opt-in de campanha, não de serviço | O opt-in de serviço (dado na compra) não habilita campanha. | E4 |
| EN3 | Finalidade cobre o kit | A finalidade aceita precisa cobrir "cursos de Pós-graduação da Faculdade UFAPE". Opt-in dado a um item só (por exemplo, uma inscrição em prova) não cobre. | campanhas-de-nutricao-pos, 1.3 |
| EN4 | Segmento S2 ou S3 da área | **S2:** lead de Pós com [área_de_interesse] igual à área da lista, inclusive quem saiu da NP2 da área no dia do primeiro toque (seção 11, no -p2). **S3:** falou com o time e não pagou. As duas com o opt-in do canal do toque (EN1). | plano da onda 3, regra 11; estrategia-de-relacionamento-pos, seção 4 |
| EN5 | S3 só sem conversa ativa | S3 com [time_assumiu]=sim, ou que respondeu ao time nas últimas 48 h ([respondeu_em]), não recebe toque automático: a retomada é do time (P4). | onda 2, EN5 e DEC5 |
| EN6 | Fora do kit | S1 (sem área), S4 e S5 (provas, se houver inscritos), S6 (matriculado), S7, S8 (ex-aluno, que segue o P7), S9 (comprador de Livres, que só entra pelo par da tabela D6 do plano geral e depois da janela de silêncio), S10, S11 e S12. | estrategia-de-relacionamento-pos, seção 4; cmo-geral, 12.4 |
| EN7 | Janela de silêncio (D8) | Se hoje for menor ou igual a [fim_janela_silencio], o toque não sai. Régua em curso não é interrompida: vale o contato que já recebeu ao menos 1 toque do kit da turma antes da compra. | cmo-geral, 12.5 |
| EN8 | Entrada tardia | Quem entra na lista depois do primeiro toque da turma recebe só os toques seguintes, sem recuperar os que passaram. O lead novo continua a NP1 (T1, T2 e T3); se a área já tem flag de saída da NP2 ligada, ele não entra em NP2 e vai direto à lista da área. No dia em que um toque do kit e um da NP1 coincidirem, o kit vence (fila D2). | O7 (toques com data fixa); campanhas-de-nutricao-pos, 1.2 |
| EN9 | Estado da turma no dia | Ver CC4 (seção 5). | contexto/pos-graduacao.md (exceção da decisão 18) |
| EN10 | Página no ar | Ver CC12. | regra 13 do plano |
| EN11 | Marca de curso em A14 | L-A14-679 só aceita contato com [curso_de_interesse]=infectologia ou 679. Sem a marca, não entra (falha fechada). | plano da onda 3, seção 7.3; DEC7 |
| EN12 | Contato em NP2 da área | No dia do primeiro toque do kit da área o contato sai da NP2 (flag às 00h05) e passa a elegível ao kit; o toque de NP2 pendente é cancelado, mesmo que o primeiro toque do kit seja suprimido para ele. | seção 11 (-p2); onda 2, seção 9 |

A lista é gerada às 06h do dia do envio e reconferida 30 minutos antes (às 08h30 para o e-mail de 9h e às 09h30 para o WhatsApp de 10h) [SUPOSIÇÃO: depende de a ferramenta permitir; senão, uma só geração às 06h e SAIR processado até o disparo].

---

## 4. Regras de saída

O CRM grava o **motivo** de cada saída (campo [kit_saiu_motivo_<código>]); a squad só lê contagem por motivo.

| # | Quem ou o que sai | Regra | Quando age | Fonte |
|---|---|---|---|---|
| SA1 | Quem pagou a 1ª mensalidade da turma | Sai de todos os toques daquela turma, no dia do envio (a lista é reconferida antes do disparo). **Inscrição paga sem 1ª mensalidade não tira** o contato (DEC3 da onda 2, mantida), porque o objetivo do toque é concluir a matrícula. | a cada geração de lista | regra 11 do plano; decisão 16 (matrícula de fato = 1ª mensalidade) |
| SA2 | Quem pagou outra turma da mesma área | Quem paga uma turma de uma área sai dos toques de campanha das outras turmas da mesma área (68632 e 366 em A4; 68609 e 657 em A1; 68636 e 289 em A2): são alternativas do mesmo segmento e a própria frase-ponte diz que a escolha depende do trabalho do contato (E11 do plano). A saída é só dos toques; o contato segue elegível às outras áreas. Se o CRM já trata S6 como "matriculado em qualquer turma de Pós", o efeito já existe. | idem | DEC3 desta onda [SUPOSIÇÃO do agente] |
| SA3 | Turma depois da data limite | A turma sai de toda lista às 23h59 da véspera do 3º módulo (tabela 4.1). Se a OU6 disser que vale o 1º dia do 3º módulo, a saída passa para 23h59 do 1º dia. Nenhum toque agendado cai depois dessas datas (o último é o pós-início), então o efeito é fechar a lista para qualquer envio manual. | job diário às 00h05 com [data_limite_turma] | decisão 18; plano 7.7; OU6 |
| SA4 | 68632 sem OU3 (regra 8) | A turma sai de toda lista às **23h59 de 09/04/2027** (sexta-feira, véspera do início e do módulo 1 presencial). Nenhuma mensagem sobre entrada depois do início existe e o toque reservado de 04/05 nunca é agendado. Com OU3 respondida, a reabertura é novo pedido, com texto novo passando pelo qa e relatório com data nova (DEC6 da onda 2, mantida); a data limite passa a 11/06. | job diário | regra 8 do plano; E22 |
| SA5 | Descadastro e SAIR | SAIR no WhatsApp ou descadastro no e-mail tira o contato de **toda campanha de todas as linhas**, no mesmo dia na prática e no máximo em **48 h** (E3). Serviço continua [SUPOSIÇÃO já registrada na estrategia-de-relacionamento-pos, 3.1]. O botão "Sair" do template e a palavra SAIR no texto livre valem igual. Resposta com "parar" ou parecida vai ao humano para registro, no mesmo dia. **Não se desliga.** | tempo real; reconferência antes do envio | E3; estrategia-de-relacionamento-pos, 3.2 |
| SA6 | Quem respondeu (inclui "TURMA") | Sai dos toques automáticos da turma respondida e a conversa passa ao time (vendas de São Paulo; vendas de Goiânia para 68632 e 68609). Em A4, a resposta a um toque de 68632 não tira o contato de 366, e o contrário também [SUPOSIÇÃO: são turmas e times de venda diferentes]. O time decide se devolve à régua (campo [time_assumiu]). | [respondeu_em] | O7, seção 0.2 |
| SA7 | E-mail com devolução permanente ou reclamação de spam | Sai de e-mail de campanha. | tempo real | newsletter-geral, 2.1 |
| SA8 | Turma que deixa de poder receber chamada | Status do catálogo diferente de "aberto" e de "verificar por já ter começado" (CC4), turma cancelada ou adiada: o kit da turma para, e o caso vira serviço da secretaria (S12). | status do dia | conformidade-educacional; decisão 18 |
| SA9 | Contato sem engajamento no WhatsApp (E1) | Sem resposta, clique ou conversa nas últimas 4 mensagens de campanha por WhatsApp: no máximo 1 WhatsApp de campanha por semana. Sem interação em 90 dias: sai do WhatsApp de campanha e fica só no e-mail. | contador [wa_campanha_sem_interacao] | E1 (cmo-geral, 13.3) |
| SA10 | Erro 131049 da Meta | Toque barrado não é reenviado antes de 24 h e não muda de dia: conta como suprimido (E2). Só vale se a Ufape usar a API oficial (U11a). | no envio | E2 |

Saída da automação nunca apaga o contato do CRM nem o histórico: só muda o estado do contato na lista.

### 4.1 Quando cada lista fecha (SA3 e SA4)

| Turma | Início (catálogo) | 3º módulo (ficha, fonte do plano) | A lista da turma fecha | Último toque agendado |
|---|---|---|---|---|
| 679 | 03/04/2027 [CONFIRMAR OU19] | junho de 2027, dia [CONFIRMAR NO CATÁLOGO, OU25] | 23h59 da véspera do 3º módulo; sem o dia, 23h59 de 31/05/2027 como trava de segurança [SUPOSIÇÃO: falha fechada, antes de qualquer dia de junho] | PI de 26/04 (só com o dia) |
| 68632 | 10/04/2027 | 12 e 13/06/2027 (fora das mensagens, regra 8) | **23h59 de 09/04/2027** enquanto a OU3 estiver aberta; 23h59 de 11/06 com OU3 | pré-início de 05/04 |
| 68635 | 10/04/2027 | junho de 2027, dia [CONFIRMAR NO CATÁLOGO, OU25] | 23h59 da véspera do 3º módulo; sem o dia, 23h59 de 31/05/2027 [SUPOSIÇÃO] | PI de 03/05 (só com o dia) |
| 366 | 10/04/2027 pela planilha; 24/04/2027 no site [CONFIRMAR OU20] | junho de 2027, dia [CONFIRMAR NO CATÁLOGO, OU25] | 23h59 da véspera do 3º módulo; sem o dia, 23h59 de 31/05/2027 [SUPOSIÇÃO] | PI de 03/05 (só com a data e o dia) |
| 68628 | 10/04/2027 | 26 e 27/06/2027 | 23h59 de 25/06/2027 | PI de 28/04 |
| 68617 | 17/04/2027 | 19 e 20/06/2027 | 23h59 de 18/06/2027 | PI de 06/05 |
| 68636 | 17/04/2027 [CONFIRMAR OU21] | 19 e 20/06/2027 | 23h59 de 18/06/2027 | PI de 30/04 |
| 68609 | 24/04/2027 | 26 e 27/06/2027 | 23h59 de 25/06/2027 | PI de 11/05 |

---

## 5. Condições comuns de envio (CC1 a CC12)

Toda linha das tabelas da seção 13 (-p3) diz "CC1 a CC12 e" mais a condição específica. O CRM confere nesta ordem; a primeira que falhar suprime o toque para aquele contato e registra o motivo (somado).

| # | Condição | Falha vira |
|---|---|---|
| CC1 | Opt-in do canal, de campanha e com finalidade (EN1 a EN3) | não entra |
| CC2 | Contato na lista da turma e da área, no segmento S2 ou S3 (EN4 a EN6, EN11) | não entra |
| CC3 | Nenhum motivo de saída (seção 4) | sai |
| CC4 | Estado da turma permitido hoje: "aberto" no catálogo, ou "verificar" só porque a turma já começou (exceção da decisão 18, em vigor até a véspera do 3º módulo). Qualquer outro estado para o kit da turma. | suprimido; aviso ao cmo |
| CC5 | Dia e horário permitidos: sem campanha de 21/12 a 03/01 (inclusive 25/12, 31/12 e 01/01) e nas datas da regra 11 do plano: 25/01, 08 a 10/02, 26/03, 21/04, 27/05 e 09/07. WhatsApp em dia útil das 9h às 18h; e-mail das 7h às 19h. Toque que o CRM não conseguir enviar dentro da janela é suprimido, não vai para o dia seguinte. | suprimido |
| CC6 | Janela de silêncio (EN7) | suprimido |
| CC7 | Limite diário: no máximo 1 mensagem de campanha por contato por dia, em qualquer canal. Serviço não conta. Conversa 1 a 1 do time de vendas não conta. | suprimido |
| CC8 | Teto semanal (segunda a domingo), somando todas as linhas e a newsletter: até 2 WhatsApp e 2 e-mails de campanha; 1 WhatsApp se houver SA9; **contato também na base da Graduação: até 3 por semana somando os canais**, 1 por dia (D16). | suprimido |
| CC9 | Sobreviver à fila D2 (seção 6) quando mais de um toque disputa o dia ou a semana | suprimido; não acumula |
| CC10 | Sem erro 131049 no envio (SA10) | suprimido |
| CC11 | Portões de aprovação do toque: OC2 aprovado para este toque, qa próprio feito e teste de humano da lista, do link e da UTM; portão da turma (OU20 em 366, em todos os toques; OU19 em 679 e OU21 em 68636, só nos pós-inícios, porque os outros toques saem com "abril de 2027"; URL "/v/" em 68617; OU3 em 68632; o dia do 3º módulo nos PI de 679, 68635 e 366) | o toque não é agendado |
| CC12 | Página da turma publicada e conferida em 11/12 e reconferida em 04/01 (OC1-A). Nenhum envio sai para página com frase ligada ao MEC antes da troca, salvo decisão humana registrada no OC1 com a regulação [CONFIRMAR]. Toque sem link (pós-início) não depende de CC12, mas depende de a página ter sido corrigida antes, porque a mensagem confirma o que está nela. | o toque não é agendado |

**Limite de carga do plano (não é condição por contato).** O plano da onda 3 permite até 4 toques da onda 3 por dia, sempre de áreas diferentes. O lote A respeita: o dia mais cheio é 20/01 (E1 de 68635 em A3, E1 de 68609 em A1, W1 de 68628 em A10 e W1 de 68636 em A2) e nenhum dia tem duas listas da mesma área. O CRM não bloqueia nada por esse limite; ele registra e **avisa o cmo** se uma remarcação levar um dia a mais de 4 toques ou a duas listas da mesma área.

---

## 6. Fila D2, 1 por dia, teto e data de referência

### 6.1 Como o CRM decide (por contato)

1. **Segunda-feira, 06h:** o CRM monta, para cada contato, a lista de toques candidatos da semana inteira (kit de qualquer onda, régua da onda 1, newsletter, NP1, NP2 e o que existir) e aplica CC1 a CC8. Só então ordena o que sobrou.
2. **Ordem da fila (D2):** (1) serviço de qualquer linha, fora do teto; (2) toque principal de cada campanha com data, onde estão os toques do kit; (3) entre toques principais que disputam a semana, vence o de **data de referência** mais próxima (item 3); empate, vence a maior nota GUT (seção 6.2); empate de nota, a maior urgência (passo 5 da skill matriz-gut); empate ainda, o toque de data de envio mais cedo; (4) follow-ups e reenvios; (5) nutrição (newsletter, NP1, NP2, NP3, rotação dos contínuos); (6) reativação.
3. **Data de referência (decisão 4 do plano da onda 3):** a data de início da turma se ela ainda não começou; a data limite (véspera do 3º módulo) se já começou [SUPOSIÇÃO herdada da onda 2: o D2 diz "data mais próxima" e não define o caso da turma iniciada]. Pós-início sem o dia do 3º módulo (679, 68635 e 366): a referência fica **depois** de qualquer referência com dia de junho, só como posição na fila, nunca como data de peça (DEC2).
4. **Fila em ordem de prioridade (DEC1):** o CRM percorre os candidatos na ordem acima e **aceita** um toque se, entre os já aceitos, (a) o dia está livre (1 por dia em qualquer canal) e (b) o canal ainda não chegou a 2 na semana (1 se SA9; 3 somando canais na base da Graduação). O que não cabe é **suprimido**.
5. **Um concorrente só derruba outro toque se ele mesmo for aceito.** Exemplo: o W1 de 68628 em 20/01 só tira o E1 de 68635 do mesmo dia se couber no teto de WhatsApp do contato; se o contato já tem 657 e 333 na semana, o W1 de 68628 cai e o E1 de 68635 sai. É o que a tabela 7.4 do meu arquivo da onda 2 já fazia (em 14 a 20/12 a edição 3 da newsletter fica para quem perde o W1 de 333) e corrige a redação dos passos 4 e 5 da seção 6.1 daquele arquivo, que lida ao pé da letra cortaria o dia antes do teto e deixaria o contato sem nenhum dos dois toques.
6. **O suprimido não acumula e não muda de dia** (D2). Se o concorrente sair da lista depois (por exemplo, pagou), o toque suprimido **não volta**. A checagem diária só remove, nunca acrescenta toque à semana já calculada.
7. **Contagem de supressões** por motivo (dia, teto semanal, fila), por toque e por combinação de áreas, só somada, para o relatório do cmo (seção 14, no -p3).

### 6.2 Data de referência e nota GUT por turma (skill .claude/skills/matriz-gut/SKILL.md)

O plano geral (cmo-geral, seção 3) dá a mesma nota de grupo (5, 2, 3, total 30) às 9 turmas de abril, o que não desempata. As notas abaixo são avaliação do agente, não medida, e só valem para a fila: desempatam turmas com a mesma data de referência. As da onda 2 ficam como estão (341 = 80; 289 e 68615 = 48; 657 e 333 = 45).

**Escala usada (ancorada nas notas da onda 2).** G acompanha a meta em reais do plano da onda 3 (15 vezes o total do catálogo): 5 se a meta é de R$ 560.000,00 ou mais; 4 de R$ 520.000,00 a R$ 559.999,99; 3 de R$ 490.000,00 a R$ 519.999,99; 2 abaixo de R$ 490.000,00 (confere com a onda 2: R$ 652.500,00 deu 5 e R$ 531.000,00 deu 4). U parte da data de início (03/04 = 5; 10/04 = 4; 17/04 = 3; 24/04 = 2), com mais 1 para 68632 (a janela de mensagens fecha na véspera do início, regra 8) e menos 1 para 366 (data em aberto, P4). T é 4 para turma I (sem histórico, como 341 na onda 2) e 3 para as demais.

| Turma | Início (referência antes) | Véspera do 3º módulo (referência depois) | G | U | T | Nota | Motivo das notas (dado e fonte) |
|---|---|---|---|---|---|---|---|
| 68628 | 10/04/2027 | 25/06/2027 | 5 | 4 | 3 | **60** | meta de R$ 584.100,00 (R$ 38.940,00 x 15), a maior do lote; início 10/04; turma com histórico |
| 68632 | 10/04/2027 | 11/06/2027 (só com OU3) | 3 | 5 | 3 | **45** | meta de R$ 495.000,00; início 10/04 com a janela fechando em 09/04 (regra 8); turma V |
| 68635 | 10/04/2027 | junho, dia [CONFIRMAR OU25] | 3 | 4 | 3 | **36** | meta de R$ 495.000,00; início 10/04; turma V |
| 366 | 10/04/2027 [OU20] | junho, dia [CONFIRMAR OU25] | 3 | 3 | 4 | **36** | meta de R$ 495.000,00; data em aberto (10/04 ou 24/04); turma I sem histórico |
| 68636 | 17/04/2027 [OU21] | 18/06/2027 | 5 | 3 | 3 | **45** | meta de R$ 569.250,00 (R$ 37.950,00 x 15); início 17/04; turma VIII |
| 68617 | 17/04/2027 | 18/06/2027 | 4 | 3 | 3 | **36** | meta de R$ 540.000,00 (R$ 36.000,00 x 15); início 17/04 |
| 679 | 03/04/2027 [OU19] | junho, dia [CONFIRMAR OU25] | 3 | 5 | 3 | **45** | meta de R$ 495.000,00; início 03/04, o mais próximo do lote |
| 68609 | 24/04/2027 | 25/06/2027 | 2 | 2 | 3 | **12** | meta de R$ 486.750,00 (R$ 32.450,00 x 15), a menor do lote; início 24/04 |
| 657 (onda 2) | 13/03/2027 | 21/05/2027 | | | | 45 | nota de grupo da onda 2 |
| 341 (onda 2) | 20/03/2027 | 30/04/2027 | | | | 80 | onda 2 |
| 289 (onda 2) | 20/03/2027 | 14/05/2027 | | | | 48 | onda 2 |
| 68615 (onda 2) | 20/03/2027 | 21/05/2027 | | | | 48 | onda 2 |
| 333 (onda 2) | 27/03/2027 | 28/05/2027 (só com OU3; sem OU3 a turma sai em 26/03) | | | | 45 | onda 2 |

**Ordem resultante dos toques de abril antes do início:** 679 (03/04), 68628 (10/04, nota 60), 68632 (10/04, nota 45), 68635 (10/04, nota 36, urgência 4), 366 (10/04, nota 36, urgência 3), 68636 (17/04, nota 45), 68617 (17/04, nota 36), 68609 (24/04). Todas ficam atrás das turmas da onda 2 antes do início (657 em 13/03; 341, 289 e 68615 em 20/03; 333 em 27/03) e na frente dos pós-inícios da onda 2 (referência de 30/04 em diante). **Depois do início:** 68632 (11/06, só OU3), 68636 (18/06, nota 45), 68617 (18/06, nota 36), 68628 (25/06, nota 60), 68609 (25/06, nota 12), depois 679, 68635 e 366 (junho sem dia, nessa ordem: 45, 36 com urgência 4, 36 com urgência 3).

**Robustez das notas (o que muda e o que não muda):**
1. **OU20.** A nota de 366 depende da data. Com início confirmado em 10/04, U passa a 4 e a nota a 48: 366 passa 68632 (45) e 68635 (36) e a ordem do dia vira 68628, 366, 68632, 68635. Com início em 24/04, a referência de 366 passa a 24/04 e o toque muda de lugar pela data, não pela nota. Nos dois casos é ciclo extra (O7: "se o início for 24/04, ciclo extra"): nova versão deste arquivo, com a conta da seção 9 refeita.
2. **Metas.** Se a meta de uma turma mudar (decisão 16, U8), G muda. A posição de 68628 em primeiro lugar entre as turmas de 10/04 só se inverte se a meta dela cair abaixo de R$ 520.000,00 (G 3, nota 36, atrás de 68632 com 45); enquanto a meta ficar em R$ 520.000,00 ou mais, a ordem não muda (G 4 dá 48).
3. **Empates de data que só aparecem quando dois ou mais toques disputam o mesmo dia ou a mesma semana:** 68628 contra 68632, 68635 e 366 (10/04); 68636 contra 68617 (17/04, e de novo em 18/06 no pós-início); 68628 contra 68609 (25/06, que nunca cai na mesma semana: PI em 28/04 e 11/05). Todos têm desempate escrito.
4. **Pós-inícios sem dia (679, 68635 e 366):** a posição na fila é provisória até a OU25 (DEC2). As únicas semanas em que isso poderia decidir algo são 26/04 a 02/05 (679) e 03 a 09/05 (68635 e 366); a seção 9 mostra que o resultado não depende da posição exata.

---

## 7. Calendário dos 55 toques (e-mail às 9h; WhatsApp às 10h)

### 7.1 Toques por turma (igual à seção 0.1 do O7 e à seção 7.3 do plano, toque a toque)

| Turma (área) | E1 | W1 | W2 | E2 | W3 | Pré-início | Pós-início |
|---|---|---|---|---|---|---|---|
| 68628 (A10) | seg 04/01 | qua 20/01 | sex 05/02 | qua 17/02 | qua 03/03 | seg 05/04 | qua 28/04 |
| 68617 (A7) | seg 04/01 | sex 22/01 | seg 15/02 | qua 24/02 | sex 12/03 | seg 12/04 | qui 06/05 |
| 68636 (A2) | seg 04/01 | qua 20/01 | qua 17/02 | sex 26/02 | seg 15/03 | ter 13/04 | sex 30/04 |
| 68635 (A3) | qua 20/01 | sex 05/02 | sex 19/02 | seg 01/03 | seg 08/03 | ter 06/04 | seg 03/05 (só com o dia do 3º módulo) |
| 68609 (A1) | qua 20/01 | seg 15/02 | qui 25/02 | seg 08/03 | qua 17/03 | seg 19/04 | ter 11/05 |
| 68632 (A4) | sex 22/01 | seg 15/02 | seg 22/02 | qua 03/03 | sex 05/03 | seg 05/04 (sem a frase do 3º módulo) | ter 04/05, reservado sem texto (só OU3) |
| 679 (A14) | sex 22/01 | sex 19/02 | seg 22/02 | qua 24/02 | seg 01/03 | seg 29/03 | seg 26/04 (só com o dia do 3º módulo) |
| 366 (A4) | sex 05/02 | qua 17/02 | qua 24/02 | seg 01/03 | seg 08/03 | qua 07/04 | seg 03/05 (só com a data e o dia) |

Em 68628, 68617, 68636 e 68609 o pós-início é o 4º WhatsApp do kit e o pré-início é o acréscimo; em 679, 68635 e 366 o pré-início é o 4º do kit e o pós-início é o acréscimo condicionado; em 68632 os 4 WhatsApp são todos pré-início e o pós-início fica reservado. Dias da semana conferidos contra 01/01/2027 (sexta-feira), 01/03/2027 (segunda-feira) e 05/04/2027 (segunda-feira).

### 7.2 Os 55 toques por data (31 dias)

| Data | Dia | Toques do dia (turma, área, toque, canal) | Nº |
|---|---|---|---|
| 04/01 | seg | 68628 (A10) E1 e-mail; 68617 (A7) E1 e-mail; 68636 (A2) E1 e-mail | 3 |
| 20/01 | qua | 68635 (A3) E1 e-mail; 68609 (A1) E1 e-mail; 68628 (A10) W1 WhatsApp; 68636 (A2) W1 WhatsApp | 4 |
| 22/01 | sex | 68632 (A4) E1 e-mail; 679 (A14) E1 e-mail; 68617 (A7) W1 WhatsApp | 3 |
| 05/02 | sex | 366 (A4) E1 e-mail; 68635 (A3) W1 WhatsApp; 68628 (A10) W2 WhatsApp | 3 |
| 15/02 | seg | 68632 (A4) W1; 68617 (A7) W2; 68609 (A1) W1, os três WhatsApp | 3 |
| 17/02 | qua | 68628 (A10) E2 e-mail; 366 (A4) W1 WhatsApp; 68636 (A2) W2 WhatsApp | 3 |
| 19/02 | sex | 679 (A14) W1; 68635 (A3) W2, os dois WhatsApp | 2 |
| 22/02 | seg | 68632 (A4) W2; 679 (A14) W2, os dois WhatsApp | 2 |
| 24/02 | qua | 679 (A14) E2 e-mail; 68617 (A7) E2 e-mail; 366 (A4) W2 WhatsApp | 3 |
| 25/02 | qui | 68609 (A1) W2 WhatsApp | 1 |
| 26/02 | sex | 68636 (A2) E2 e-mail | 1 |
| 01/03 | seg | 366 (A4) E2 e-mail; 68635 (A3) E2 e-mail; 679 (A14) W3 WhatsApp | 3 |
| 03/03 | qua | 68632 (A4) E2 e-mail; 68628 (A10) W3 WhatsApp | 2 |
| 05/03 | sex | 68632 (A4) W3 WhatsApp | 1 |
| 08/03 | seg | 68609 (A1) E2 e-mail; 366 (A4) W3 WhatsApp; 68635 (A3) W3 WhatsApp | 3 |
| 12/03 | sex | 68617 (A7) W3 WhatsApp | 1 |
| 15/03 | seg | 68636 (A2) W3 WhatsApp | 1 |
| 17/03 | qua | 68609 (A1) W3 WhatsApp | 1 |
| 29/03 | seg | 679 (A14) pré-início WhatsApp | 1 |
| 05/04 | seg | 68628 (A10) pré-início; 68632 (A4) pré-início, os dois WhatsApp | 2 |
| 06/04 | ter | 68635 (A3) pré-início WhatsApp | 1 |
| 07/04 | qua | 366 (A4) pré-início WhatsApp | 1 |
| 12/04 | seg | 68617 (A7) pré-início WhatsApp | 1 |
| 13/04 | ter | 68636 (A2) pré-início WhatsApp | 1 |
| 19/04 | seg | 68609 (A1) pré-início WhatsApp | 1 |
| 26/04 | seg | 679 (A14) pós-início WhatsApp (só com o dia do 3º módulo) | 1 |
| 28/04 | qua | 68628 (A10) pós-início WhatsApp | 1 |
| 30/04 | sex | 68636 (A2) pós-início WhatsApp | 1 |
| 03/05 | seg | 68635 (A3) pós-início (só com o dia); 366 (A4) pós-início (só com a data e o dia), os dois WhatsApp | 2 |
| 06/05 | qui | 68617 (A7) pós-início WhatsApp | 1 |
| 11/05 | ter | 68609 (A1) pós-início WhatsApp | 1 |
| (04/05 | ter | 68632 (A4) pós-início, reservado, sem texto e sem agendamento) | (1) |

Total: 3 + 4 + 3 + 3 + 3 + 3 + 2 + 2 + 3 + 1 + 1 + 3 + 2 + 1 + 3 + 1 + 1 + 1 + 1 + 2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 2 + 1 + 1 = **55** (16 e-mails e 39 WhatsApp), mais 1 reservado. O dia 04/05 também tem o pré-início de 68616 (A12, lote B), de outra área.

Os dias com mais de um toque do lote A são 14 (04/01, 20/01, 22/01, 05/02, 15/02, 17/02, 19/02, 22/02, 24/02, 01/03, 03/03, 08/03, 05/04 e 03/05); o contato que está em duas ou mais dessas áreas recebe só um deles (fila D2, seção 6).

- **Agente:** arquiteto-de-fluxos (departamento 10), encomenda O10 do plano do CMO da onda 3 (versão 2), lote A
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana. Nada é ligado, agendado, enviado ou pago. Nenhum dado pessoal.
- **Convenções desta parte:** "pior caso" é o contato que está, ao mesmo tempo, em todas as áreas que disputam a semana, com opt-in nos dois canais e sem restrição de engajamento; é limite superior, não estimativa. "Caem" quer dizer suprimidos pela fila em ordem de prioridade da seção 6 (DEC1). Cada concorrente só derruba outro toque se ele mesmo for aceito. O lote B (maio) está só como reserva informativa nas semanas em que ele passa à frente de um toque do lote A (03 a 09/05), pelo plano da onda 3, seção 7.3; o O10 do lote B (22/01/2027) refaz a conta.

---

## 8. Conferência com a onda 2, a onda 1 e a newsletter

### 8.1 Os cinco testes por data

| Teste | Regra | Resultado |
|---|---|---|
| T1. Dia único com a onda 2 | nenhum dos 31 dias do lote A é uma das 37 datas da onda 2 (07, 08, 09, 10, 11, 14, 17 e 18/12; 05, 08, 11, 13, 15, 18, 19, 21, 26, 27 e 29/01; 01, 02, 03, 04, 11, 12, 16 e 23/02; 02, 09, 10, 11 e 16/03; 14, 20 e 27/04; 05 e 12/05), inclusive 15, 18 e 26/01 da variante de 341 | passa nos 31 dias |
| T2. Newsletter | nenhum toque em 07/01, 14/01, 28/01, 18/02 e, pela decisão 10 do plano [SUPOSIÇÃO], 04/03, 18/03, 01/04, 15/04, 29/04 e 13/05 | passa. A versão de WhatsApp da newsletter, se existir no dia seguinte a cada edição (08/01, 15/01, 29/01, 19/02, 05/03, 19/03, 02/04, 16/04, 30/04 e 14/05), coincide com 3 toques do lote A: **19/02** (W1 de 679 e W2 de 68635), **05/03** (W3 de 68632) e **30/04** (PI de 68636). O kit vence; a newsletter por WhatsApp não muda de dia (DEC8) |
| T3. Onda 1 e NP2 | nenhum toque em 01/12, 02/12, 15/12, 16/12, 06/01 e 12/01 (onda 1) nem em 01/12, 09/12, 16/12 e 05/01 (NP2) | passa nos 31 dias; 04/01 e 05/01 ficam em dias separados do W de 06/01 (698, só com OU3) |
| T4. Dias sem campanha e janela | nenhum toque em 21/12 a 03/01, 25/01, 08 a 10/02, 26/03, 21/04, 27/05 e 09/07; todo WhatsApp em dia útil e fora de feriado nacional | passa; os 39 WhatsApp caem em segunda a sexta (conferido contra 01/01/2027, sexta-feira); nenhum feriado nacional cai nos 31 dias (21/04 e 01/05 ficam sem toque; 05/04 e 03/05 são segundas) |
| T5. Carga do plano | até 4 toques da onda 3 por dia, sempre de áreas diferentes | passa: o máximo é 20/01 (4 toques de A3, A1, A10 e A2); 17/02 chega a 4 com o E1 de 68616 (A12, lote B); nenhum dia repete área (A4 tem duas turmas, 68632 e 366, e nenhum dia as junta) |

### 8.2 Contato de uma só área contra a seção 10.1 do O7

Refiz a conta semana a semana com a fila em ordem de prioridade para cada área isolada (A1, A2, A3, A4, A7, A10 e A14), somando os toques da onda 2, da onda 1 e a newsletter. **Confere com a seção 10.1 do O7 em todas as linhas:** nenhum contato de uma só área passa de 2 WhatsApp nem de 2 e-mails por semana nem de 1 mensagem por dia. O único e-mail que passa de 2 é A4 em 01 a 07/03 (E2 de 366 em 01/03, E2 de 68632 em 03/03 e newsletter de 04/03), e a fila corta a newsletter. Três notas sobre o O7, sem alterar o arquivo dele (seção 10):

1. O resumo do O7 diz 55 textos (16 e-mails e 39 WhatsApp), igual à conta das tabelas (já corrigido no O7 aprovado).
2. A seção 10.2 do O7 lista os 14 dias com mais de um toque, iguais aos da seção 7.2 deste arquivo (já corrigido no O7 aprovado).
3. Em A4, na semana de 03 a 09/05, a linha diz "= 1" para o WhatsApp; são até 2 (366 em 03/05 e 68632 em 04/05, este só com OU3 e sem texto). Cabe no teto.

O lote B não muda nenhuma linha de contato de uma só área do lote A: os toques de maio têm referência de 08/05 em diante e ficam atrás de qualquer pré-início de abril na fila.

### 8.3 Conferência com o calendário da newsletter-geral (seção 3.1) e a decisão 10 do plano

| Edição | Data e hora | Semana e toques do lote A | Convive? | Tratamento |
|---|---|---|---|---|
| 4 | qui 07/01, 10h | 04 a 10/01: E de 68628, 68617 e 68636 em 04/01 (e 657 em 05/01, onda 2) | sim, com ressalva | a newsletter cai (5ª da fila) só para quem já recebe 2 e-mails de campanha na semana: **A1 com A10, A2 ou A7** (657 em 05/01 mais um E1 de 04/01). Para quem está em uma área só, cabe |
| 5 | qui 14/01, 10h | 11 a 17/01: nenhum toque do lote A | sim | nenhum |
| 6 | qui 28/01, 10h | 25 a 31/01: nenhum toque do lote A | sim | nenhum |
| 7 | qui 18/02, 10h | 15 a 21/02: E2 de 68628 em 17/02 e 7 WhatsApp do lote A | sim | cabe: 2 e-mails (E2 de 68628 e newsletter) no pior caso. A agenda da edição 7 cita 68632, 366 e 662: nota ao agente newsletter (CF7) |
| 8 (suposta) | qui 04/03, 10h | 01 a 07/03: E2 de 366 (01/03), E2 de 68635 (01/03), E2 de 68632 (03/03) | **sim, corta** | ver 8.4 |
| 9 (suposta) | qui 18/03, 10h | 15 a 21/03: só WhatsApp do lote A (15 e 17/03) | sim | cabe (1 e-mail) |
| 10 (suposta) | qui 01/04, 10h | 29/03 a 04/04: só o WhatsApp de 679 em 29/03 | sim | cabe |
| 11 (suposta) | qui 15/04, 10h | 12 a 18/04: só WhatsApp (12 e 13/04) | sim | cabe |
| 12 (suposta) | qui 29/04, 10h | 26/04 a 02/05: só WhatsApp (26, 28 e 30/04) | sim | cabe |
| 13 (suposta) | qui 13/05, 10h | 10 a 16/05: só o WhatsApp de 68609 em 11/05 | sim | cabe |

A newsletter-geral só escreveu as edições 1 e 2 e deixou 3 a 7 como pauta; depois de 18/02 ela não traz datas. O calendário das edições 8 a 13 é a suposição do plano (decisão 10: quintas quinzenais). Se o calendário real for outro, vale a fila D2: a newsletter é a 5ª e só entra onde sobra teto e dia.

### 8.4 O corte da newsletter de 04/03 para A4

- **Conta (contato só em A4):** e-mails candidatos em 01 a 07/03: E2 de 366 (seg 01/03), E2 de 68632 (qua 03/03) e newsletter (qui 04/03). A fila aceita os dois e-mails do kit (prioridade 2) e a newsletter (prioridade 5) já não cabe no teto de 2 e-mails. **A newsletter de 04/03 cai.** O WhatsApp de 68632 em 05/03 (W3) também vence a versão de WhatsApp da newsletter desse dia, se ela existir.
- **Quem mais perde a newsletter:** A4 com A3 (E2 de 68635 em 01/03 e E2 de 68632 em 03/03; o E2 de 366 já cai no dia 01/03 para o de 68635).
- **Quando a newsletter vai mesmo assim:** sempre que um dos dois e-mails do kit não for aceito para aquele contato (pagou, respondeu, opt-in só de WhatsApp, ou o dia 01/03 ocupado pelo W3 de 679 em A14, ou o dia 03/03 ocupado pelo W3 de 68628 em A10). A fila só conta o que é aceito (DEC1). Exemplo: A4 com A14 recebe E2 de 68632 e newsletter; A4 com A10 recebe E2 de 366 e newsletter.
- **Efeito no kit:** nenhum. O kit mínimo continua inteiro (o mínimo é por turma, não por contato).
- **Dependência:** só existe se a edição de 04/03 existir (SUPOSIÇÃO da decisão 10 do plano). Sem a edição, a conta de A4 em 01 a 07/03 fecha em 2 e-mails.

---

## 9. Pior caso semana a semana e supressões previstas

### 9.1 Pior caso por semana (fila em ordem de prioridade, seção 6)

As semanas sem toque do lote A (11 a 17/01, 25 a 31/01, 08 a 14/02 e 22 a 28/03) e as que cabem sem corte (29/03 a 04/04, 19 a 25/04 e 10 a 16/05) estão só na tabela 9.2.

| Semana | Candidatos no pior caso | Ficam | Caem do lote A | Caem de outras ondas, newsletter e NP2 | Pares de áreas que já perdem toque (2 áreas) |
|---|---|---|---|---|---|
| 04 a 10/01 | E: 04/01 68628 (A10), 68617 (A7), 68636 (A2); 05/01 657 (A1, onda 2); 07/01 newsletter. W: 06/01 698 (A2, onda 1, só OU3); 08/01 289 (A2, onda 2); 08/01 newsletter por WhatsApp; 05/01 NP2-T4 (A3, A4, A14) | E 68628 (04/01) e E 657 (05/01); W 289 (08/01) e, com OU3, 698 (06/01) | **2:** E1 de 68636 e E1 de 68617 | newsletter de 07/01; newsletter por WhatsApp de 08/01; NP2-T4 de 05/01 para quem também está em A1 (o E1 de 657 vence o dia) | (A10, A2): E1 68636. (A10, A7) e (A2, A7): E1 68617 (68636 vence 68617 pela nota 45 contra 36). A newsletter cai para A1 com A10, A2 ou A7 |
| 18 a 24/01 (padrão) | W: 19/01 333 (A11, onda 2); 20/01 68628 (A10), 68636 (A2); 21/01 657 (A1, onda 2); 22/01 68617 (A7). E: 20/01 68635 (A3), 68609 (A1); 22/01 679 (A14), 68632 (A4) | W 657 (21/01) e W 333 (19/01); E 679 (22/01) e E 68635 (20/01) | **5:** W1 68628, W1 68636, W1 68617, E1 68632, E1 68609 | nenhum (333 e 657 ficam à frente) | (A10, A3): E1 68635. (A10, A2) e (A3, A2): W1 68636. (A10, A1), (A3, A1) e (A2, A1): E1 68609. (A14, A4): E1 68632. (A14, A7) e (A4, A7): W1 68617. W1 68628 só cai para A10 com A1 e A11 (3 áreas) |
| 18 a 24/01 (variante de 341, OU10 depois de 11/12) | os mesmos, mais W 18/01 341 (A14 equinos) | W 657 (21/01) e W 341 (18/01); E 679 e E 68635 | **5** (os mesmos) | W2 de 333 (já cai na tabela 7.4 da onda 2) | os mesmos; W1 68628 cai para A10 com duas entre A1, A14 equinos e A11 |
| 01 a 07/02 | E: 01/02 657 (A1), 02/02 341 (A14 equinos), 03/02 333 (A11), 05/02 366 (A4). W: 04/02 657 (A1); 05/02 68635 (A3), 68628 (A10) | E 657 (01/02) e E 341 (02/02); W 657 (04/02) e W 68628 (05/02) | **2:** E1 366 e W1 68635 | E2 de 333 (já cai na tabela 7.4 da onda 2) | (A10, A3): W1 68635. (A10, A4) e (A3, A4): E1 366. 366 também cai para A4 com duas entre A1, A14 equinos e A11 |
| 15 a 21/02 | W: 15/02 68632 (A4), 68617 (A7), 68609 (A1); 16/02 68615 (A11, onda 2); 17/02 366 (A4), 68636 (A2); 19/02 679 (A14), 68635 (A3); 19/02 newsletter por WhatsApp. E: 17/02 68628 (A10); 18/02 newsletter | W 68615 (16/02) e W 679 (19/02); E 68628 (17/02) e newsletter (18/02) | **6:** W1 68632, W2 68617, W1 68609, W1 366, W2 68636, W2 68635 | newsletter por WhatsApp de 19/02 (o W1 de 679 e o W2 de 68635 vencem o dia) | (A4, A7): W2 68617. (A4, A1) e (A7, A1): W1 68609. (A4, A10), (A4, A11), (A4, A14) e (A4, A3): W1 366. (A2, A10) e (A2, A4): W2 68636. (A14, A3): W2 68635. W1 68632 só cai para A4 com A11 e A14 |
| 22 a 28/02 | W: 22/02 68632 (A4), 679 (A14); 23/02 333 (A11, onda 2); 24/02 366 (A4); 25/02 68609 (A1). E: 24/02 679 (A14), 68617 (A7); 26/02 68636 (A2) | W 333 (23/02) e W 679 (22/02); E 679 (24/02) e E 68636 (26/02) | **4:** W2 68632, W2 366, E2 68617, W2 68609 | nenhum | (A4, A14): W2 68632 e W2 366. (A4, A11): W2 366. (A7, A14) e (A7, A4): E2 68617. (A1, A4): W2 68609 |
| 01 a 07/03 | W: 01/03 679 (A14); 02/03 657 (A1, onda 2); 03/03 68628 (A10); 05/03 68632 (A4); 05/03 newsletter por WhatsApp. E: 01/03 366 (A4), 68635 (A3); 03/03 68632 (A4); 04/03 newsletter | W 657 (02/03) e W 679 (01/03); E 68632 (03/03) e newsletter (04/03) | **4:** W3 68628, W3 68632, E2 68635, E2 366 | newsletter por WhatsApp de 05/03 (o W3 de 68632 vence o dia, se ele couber) | (A4, A14) e (A4, A3): E2 366. (A3, A14): E2 68635. (A4, A10): E2 68632. **Contato só em A4: cai a newsletter de 04/03** (8.4). W3 68628 e W3 68632 só caem com três áreas |
| 08 a 14/03 | W: 08/03 366 (A4), 68635 (A3); 09/03 289 (A2, onda 2); 10/03 341 (A14 equinos, onda 2); 11/03 68615 (A11, onda 2); 12/03 68617 (A7). E: 08/03 68609 (A1) | W 341 (10/03) e W 289 (09/03); E 68609 (08/03) | **3:** W3 68635, W3 366, W3 68617 | AC de 68615 (já cai na tabela 7.4 da onda 2) | (A1, A3) e (A1, A4): E2 68609. (A4, A3): W3 366. Os outros caem com duas entre A14 equinos, A2 e A11 |
| 15 a 21/03 | W: 15/03 68636 (A2); 16/03 333 (A11, onda 2); 17/03 68609 (A1). E: 18/03 newsletter | W 333 (16/03) e W 68636 (15/03); newsletter | **1:** W3 68609 | nenhum | nenhum par; cai para A1 com A11 e A2 |
| 05 a 11/04 | W: 05/04 68628 (A10), 68632 (A4); 06/04 68635 (A3); 07/04 366 (A4) | W 68628 (05/04) e W 68635 (06/04) | **2:** pré-início 68632 e pré-início 366 | nenhum | (A4, A10): pré-início 68632 (a última mensagem da turma antes da regra 8; DEC4). (A4, A3): pré-início 366 |
| 12 a 18/04 | W: 12/04 68617 (A7); 13/04 68636 (A2); 14/04 341 PI (A14 equinos, onda 2). E: 15/04 newsletter | W 68636 e W 68617; newsletter | **0** | PI de 341 cai para A14 equinos com A7 e A2 (já na tabela 7.4 do plano) | nenhum |
| 26/04 a 02/05 | W: 26/04 679 PI (A14, só com o dia); 27/04 289 PI (A2, onda 2); 28/04 68628 PI (A10); 30/04 68636 PI (A2); 30/04 newsletter por WhatsApp. E: 29/04 newsletter | W 289 PI (27/04) e W 68636 PI (30/04); newsletter | **2:** PI 68628 e PI 679 | newsletter por WhatsApp de 30/04 (o PI de 68636 vence o dia) | (A10, A2): PI 68628. (A14, A2): PI 679. A ordem exata de 679 em relação a 68628 não muda o resultado (DEC2) |
| 03 a 09/05 | W: 03/05 68635 PI (A3, só com o dia), 366 PI (A4, só com a data e o dia); 04/05 68632 PI (A4, reservado, só OU3); 05/05 68615 PI (A11, onda 2); 06/05 68617 PI (A7). Reserva do lote B (plano 7.3): 03/05 719 pré-início (A14, 719), 04/05 68616 pré-início (A12) | só lote A e onda 2: W 68615 PI (05/05) e, com OU3, W 68632 PI (04/05); sem OU3, W 68615 PI e W 68617 PI | **3** com OU3 (PI 68617, PI 68635, PI 366); **2** sem OU3 (PI 68635 e PI 366) | com o lote B reservado, 719 e 68616 passam à frente e o PI de 68615 cai para quem está em A14 (719) e A12 | (A4, A3): PI 366 (o PI de 68635 vence o dia 03/05). Com o lote B: (A3, A14 719) perde o PI de 68635 |

### 9.2 Supressões previstas por semana (só números)

"Cortáveis no pior caso" é o limite superior por semana: o máximo de toques do lote A que a fila pode cortar de um contato que está em todas as áreas que disputam a semana. **Não somam entre semanas** para um mesmo contato. "Contato de uma só área" é o caso normal (S2 e S3 da área): nenhum corte do lote A.

| Semana | E do lote A | W do lote A | Total programado | Cortáveis no pior caso (lote A) | Contato de uma só área | Outros cortes previstos |
|---|---|---|---|---|---|---|
| 04 a 10/01 | 3 | 0 | 3 | 2 | 0 | newsletter de 07/01 e de 08/01 por WhatsApp; NP2-T4 de 05/01 |
| 11 a 17/01 | 0 | 0 | 0 | 0 | 0 | nenhum do lote A |
| 18 a 24/01 | 4 | 3 | 7 | 5 | 0 | W2 de 333 na variante de 341 |
| 25 a 31/01 | 0 | 0 | 0 | 0 | 0 | nenhum do lote A |
| 01 a 07/02 | 1 | 2 | 3 | 2 | 0 | E2 de 333 (onda 2) |
| 08 a 14/02 | 0 | 0 | 0 | 0 | 0 | nenhum do lote A |
| 15 a 21/02 | 1 | 7 | 8 | 6 | 0 | newsletter por WhatsApp de 19/02 |
| 22 a 28/02 | 3 | 4 | 7 | 4 | 0 | nenhum |
| 01 a 07/03 | 3 | 3 | 6 | 4 | 0 | newsletter de 04/03 (A4 só, e A4 com A3) e por WhatsApp de 05/03 |
| 08 a 14/03 | 1 | 3 | 4 | 3 | 0 | AC de 68615 (onda 2) |
| 15 a 21/03 | 0 | 2 | 2 | 1 | 0 | nenhum |
| 22 a 28/03 | 0 | 0 | 0 | 0 | 0 | nenhum do lote A (26/03 sem campanha) |
| 29/03 a 04/04 | 0 | 1 | 1 | 0 | 0 | nenhum |
| 05 a 11/04 | 0 | 4 | 4 | 2 | 0 | nenhum |
| 12 a 18/04 | 0 | 2 | 2 | 0 | 0 | PI de 341 (onda 2) |
| 19 a 25/04 | 0 | 1 | 1 | 0 | 0 | nenhum (21/04 sem campanha) |
| 26/04 a 02/05 | 0 | 3 | 3 | 2 | 0 | newsletter por WhatsApp de 30/04 |
| 03 a 09/05 | 0 | 3 (mais 1 reservado) | 3 | 3 com OU3; 2 sem OU3 | 0 | PI de 68615 se o lote B reservado entrar |
| 10 a 16/05 | 0 | 1 | 1 | 0 | 0 | nenhum |
| **Total** | **16** | **39** | **55** | **34** | **0** | |

Leitura: de 55 toques programados, nenhum é cortado para um contato de uma só área; no pior caso de cada semana até 34 podem ser cortados, em 11 semanas, concentrados em 18 a 24/01, 15 a 21/02, 22 a 28/02 e 01 a 07/03 (19 dos 34). **Quantos contatos perdem cada toque** é o tamanho da interseção das listas das áreas envolvidas (por exemplo, quem está em A4 e A14 em 22 a 28/02). Esse número só existe depois do tamanho de cada lista [CONFIRMAR, OC2]; o CRM registra, por semana, motivo (dia, teto semanal ou fila), toque e combinação de áreas, e a squad lê só a contagem (AF7).

---

## 10. Conflitos achados e como tratar

| # | Conflito | Onde aparece | Tratamento proposto | Quem decide |
|---|---|---|---|---|
| CF1 | **Contagem do O7 (resolvido).** O O7 aprovado diz 55 textos (16 e-mails e 39 WhatsApp), igual à conta das tabelas 0.1 (7 textos por turma e 6 em 68632). | O7, seção 0, item 2 | Sem ação | - |
| CF2 | **Dias com mais de um toque no O7 (resolvido).** O O7 aprovado lista os 14 dias na seção 10.2, inclusive 05/02, 19/02 e 03/05. | O7, seção 10.2 | Sem ação; este arquivo traz os mesmos 14 dias (seção 7.2) e a regra de fila para todos | - |
| CF3 | **NP2 aponta para página de turma de abril antes da conferência.** O T1 (01/12, e-mail, "Veja o cronograma da turma") e o T2 (09/12, WhatsApp, link da página da turma) da NP2 saem antes da publicação das páginas de abril (10/12) e da conferência de 11/12. A regra 13 do plano proíbe envio para página com frase ligada ao MEC antes da troca. O T3 (16/12) cai depois da conferência. A mesma questão vale para A1 (T1 em 01/12 antes de 04/12, onda 2). | NP2 de A3, A4, A7, A10 e A14 (infectologia), 01 a 16/12 | DEC5: T1 e T2 saem **sem link** para turma de abril (ou ficam suspensos nessas áreas) e o T3 só com a conferência de 11/12 feita; se a conferência atrasar, o T3 também espera, sem acumular. Nenhuma exceção manual | cmo, com a pessoa do marketing |
| CF4 | **Dois nomes de UTM para a mesma turma.** A NP2 de dezembro com link para a página da turma teria o primeiro envio real em 12/2026 (pos_<código>_202612, como no exemplo da campanhas-de-nutricao-pos, seção 6.3), e o kit do O7 usa pos_<código>_202701 (202702 em 366). | UTM, seção 12 | DEC6: manter os nomes do O7 (os templates da Meta já nascem com ele), usar o mesmo nome nos links da NP2 de dezembro e registrar o desvio na tabela de correspondência (mesma solução da DEC6 da onda 2); a leitura usa a data de envio, que o CRM guarda | pessoa do marketing |
| CF5 | **A14 por curso e a flag da NP2.** A saída da NP2 é por área; em A14 a área junta infectologia, reprodução, geriatria, silvestres e IA na Saúde. Uma flag de A14 inteira em 22/01 tiraria da NP2 quem quer 382, 699 ou 60 antes do kit deles (lote B). | NP2 de A14, 22/01 | DEC7: a flag de A14 é por curso, como a lista (L-A14-679 só para infectologia ou 679). Contato de A14 sem a marca de curso não entra em L-A14-679 e segue na NP2 de A14 até o kit do curso dele. Se o CRM não tiver a marca, vale a falha fechada | cmo |
| CF6 | **Pré-início de 68632 em 05/04 cai para quem está em A10.** É a última mensagem de 68632 antes de a regra 8 fechar a lista (09/04, sem OU3), e o W de pré-início de 68628, de mesma data de início, vence pela nota (60 contra 45). 68628 ainda tem o PI de 28/04. | 05 a 11/04, par (A4, A10) | DEC4 (opcional): o pré-início de 68632 de 05/04 passa à frente do de 68628 só nesse dia. A troca de data do toque é do cmo (plano 7.3). Sem DEC4, vale a nota | cmo |
| CF7 | **Edição 7 da newsletter (18/02) cita 662 e 366.** A agenda do arquivo da newsletter diz "Turmas de abril de A4 (68632 presencial em Goiânia, 366)" e "662 sem preço até a correção do link; 366 sem data (P4)". O plano põe 662 em espera total (OU18) e 366 só sai com OU20. | newsletter-geral, seção 3.1, edição 7 | Nota ao agente newsletter, sem alterar o arquivo dele: a edição 7 não cita 662 e só cita 366 com a data confirmada | cmo |
| CF8 | **Versão de WhatsApp da newsletter nos dias de kit.** Se as edições 3 a 7 repetirem o desenho das edições 1 e 2 (WhatsApp no dia seguinte), 19/02, 05/03 e 30/04 caem em toque do lote A. | T2, seção 8.1 | DEC8: o kit vence; a newsletter por WhatsApp não muda de dia por contato (D2). Nota ao agente newsletter para escolher, se quiser, dia livre | newsletter, com o cmo |
| CF9 | **Portão de data de 366.** Nada de 366 sai antes da OU20 (O7), e o E1 é em 05/02. Se a OU20 disser 24/04, o calendário inteiro de 366 muda. | 366, todos os toques | Verificação às 18h de 03/02 [SUPOSIÇÃO do horário]: com a data de 10/04 confirmada, vale o calendário; aberta ou com 24/04, nenhum toque de 366 é agendado e nada acumula. Com 24/04, ciclo extra: nova versão deste arquivo (e do O7) com a conta da seção 9 refeita | cmo |
| CF10 | **Dependência da onda 2.** L-A1 e L-A2 e as flags de NP2 de A1 (05/01) e A2 (08/12) nascem na onda 2 (AF1 e AF5 de lá). Se a aprovação não vier, esta onda deixa de ter o que estender. | L-A1, L-A2, seção 11 | Se AF1 da onda 2 não estiver aprovada até 11/12, o AF1 desta onda cria L-A1 e L-A2 com o mesmo filtro. Se AF5 da onda 2 não estiver ligada, esta onda liga a flag de A2 em 04/01 e a de A1 em 20/01, no primeiro toque da área | pessoa do marketing |
| CF11 | **Chave do utm_content do pré-início.** A onda 2 usa "ac" (semana anterior ao início) e o O7 usa "pr" (pré-início). | UTM | Mantido o do O7 (pr-<código>); a tabela de correspondência traz os dois nomes. É só leitura, sem efeito no envio | analise-de-midia |
| CF12 | **E2 de 68609 em 08/03 no dia do W3 de 366 e de 68635.** Para quem está em A1 com A3 ou A4, o dia 08/03 tem um toque de turma de 10/04 (referência mais próxima) à frente do E2 de 68609 (24/04), e o E2 cai. | 08/03 | Aceitar a fila: o kit mínimo vale por turma e o contato segue com W1, W2, W3, pré-início e PI de 68609. Nenhuma exceção manual | cmo |

---

## 11. Saída da NP2 da área no primeiro toque do kit

A NP2 (campanhas-de-nutricao-pos, seção 3) é nutrição, prioridade 5 da fila. O dono único do convite é o kit: no dia do primeiro toque do kit da área, às **00h05**, o CRM liga a flag [regua_com_data_ativa_área]=sim para todo contato da área e cancela os toques de NP2 pendentes dele. A saída vale **mesmo que o primeiro toque do kit seja suprimido para aquele contato** (fila ou teto), para a nutrição nunca repetir o convite. Esta onda só liga flag nas áreas que **ainda não saíram na onda 2**.

| Área | Turma (lista) | Primeiro toque do kit | Saída da NP2 | NP2 que ainda acontece antes | Observação |
|---|---|---|---|---|---|
| A10 | 68628 (L-A10) | E1, seg 04/01, 9h | **seg 04/01, 00h05** | T1 (01/12), T2 (09/12) e T3 (16/12), com as travas do CF3; o T4 de 05/01 **não** chega a A10 | só leads do lote de 30/11 e os que chegarem até 03/01 |
| A7 | 68617 (L-A7) | E1, seg 04/01, 9h | **seg 04/01, 00h05** | idem; o T4 de 05/01 não chega a A7 | URL "/v/" conferida antes do E1 (OU29) |
| A3 | 68635 (L-A3) | E1, qua 20/01, 9h | **qua 20/01, 00h05** | T1, T2, T3 e o **T4 de 05/01** (WhatsApp, sem link) | o T4 de 05/01 perde o dia para o E1 de 657 de quem também está em A1 |
| A4 | 68632 e 366 (L-A4) | E1 de 68632, sex 22/01, 9h | **sex 22/01, 00h05**, para as duas turmas (o E1 de 366 em 05/02 não liga outra flag) | T1 a T4 | a flag é por área: vale para 68632 e 366 |
| A14 (infectologia) | 679 (L-A14-679) | E1, sex 22/01, 9h | **sex 22/01, 00h05**, só para [curso_de_interesse]=infectologia ou 679 | T1 a T4 | os demais A14 (382, 699, 60 e 719, lote B) seguem na NP2 até o kit deles (CF5, DEC7). A flag de equinos já saiu na onda 2 (14/12 ou 15/01) |
| A2 | 68636 (L-A2) | E1, seg 04/01, 9h | **nada a ligar**: A2 já saiu na onda 2 (E1 de 289, 08/12) | nenhuma do lote de 30/11 (a NP2 de A2 só roda para leads que chegam depois do kit de 289) | se a flag não estiver ligada em 04/01, o CRM liga às 00h05 desse dia (CF10) |
| A1 | 68609 (L-A1) | E1, qua 20/01, 9h | **nada a ligar**: A1 já saiu na onda 2 (E1 de 657, 05/01) | T1 a T3 do lote de 30/11; o T4 de 05/01 já não chega a A1 (regra da nutrição) | se a flag não estiver ligada em 20/01, o CRM liga às 00h05 desse dia (CF10) |

Contato em mais de uma área sai da NP2 de cada área no dia do primeiro toque do kit daquela área. A flag é por área (por curso em A14), não por contato: quem estiver em A10 e A3, por exemplo, sai da NP2 de A10 em 04/01 e segue na de A3 até 20/01. Lead novo depois do primeiro toque da área entra direto na lista da área (EN8) e não em NP2.

**Efeitos que o plano da onda 3 e a campanhas-de-nutricao-pos não dizem (nota para o cmo):** (a) o T4 de 05/01 não chega a A7 e A10 (a nutrição supõe que ele vai para as áreas "sem P5 nessa semana"; com o kit de 04/01 elas já saíram); (b) a pergunta da nutrição sobre a data do "lote de abril" por área fica respondida: A10 e A7 em 04/01, A3 em 20/01, A4 e A14 em 22/01, de acordo com o plano da onda 3, seção 7.3.

---

## 12. UTM do CRM (regra 12 do plano; D11 e D12)

- utm_source: **email** nos e-mails, **whatsapp** nos WhatsApp. utm_medium: **crm** (único valor aceito para mensagem enviada pelo CRM).
- utm_campaign: **pos_<código>_<AAAAMM do primeiro envio>**, igual em todos os toques da turma. O toque vai no utm_content.
- Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Um link por mensagem. Nenhum dado pessoal na UTM.

| Turma | utm_campaign | utm_content (um por toque) | Nome do template na Meta, se API (U11a) |
|---|---|---|---|
| 68628 | pos_68628_202701 | e1-68628, w1-68628, w2-68628, e2-68628, w3-68628, pr-68628, pi-68628 (sem link) | pos_68628_kit_w1, _w2, _w3, _pr, _pi |
| 68617 | pos_68617_202701 | e1-68617, w1-68617, w2-68617, e2-68617, w3-68617, pr-68617, pi-68617 (sem link) | pos_68617_kit_w1, _w2, _w3, _pr, _pi |
| 68636 | pos_68636_202701 | e1-68636, w1-68636, w2-68636, e2-68636, w3-68636, pr-68636, pi-68636 (sem link) | pos_68636_kit_w1, _w2, _w3, _pr, _pi |
| 68635 | pos_68635_202701 | e1-68635, w1-68635, w2-68635, e2-68635, w3-68635, pr-68635, pi-68635 (sem link) | pos_68635_kit_w1, _w2, _w3, _pr, _pi |
| 68609 | pos_68609_202701 | e1-68609, w1-68609, w2-68609, e2-68609, w3-68609, pr-68609, pi-68609 (sem link) | pos_68609_kit_w1, _w2, _w3, _pr, _pi |
| 68632 | pos_68632_202701 | e1-68632, w1-68632, w2-68632, e2-68632, w3-68632, pr-68632; pi-68632 reservado, sem link e sem agendamento | pos_68632_kit_w1, _w2, _w3, _pr |
| 679 | pos_679_202701 | e1-679, w1-679, w2-679, e2-679, w3-679, pr-679, pi-679 (sem link) | pos_679_kit_w1, _w2, _w3, _pr, _pi |
| 366 | pos_366_202702 (primeiro envio em 05/02) | e1-366, w1-366, w2-366, e2-366, w3-366, pr-366, pi-366 (sem link) | pos_366_kit_w1, _w2, _w3, _pr, _pi |

Exemplo de montagem (a URL da página de cada turma é a da seção 0.2 do O7): `<URL da página da turma>?utm_source=whatsapp&utm_medium=crm&utm_campaign=pos_68628_202701&utm_content=w1-68628`.

Regras de apoio:

1. **Mês do primeiro envio.** Vale o mês do primeiro envio **real** de qualquer toque do CRM com link para a página da turma. A NP2 das áreas de abril tem T3 em 16/12 com link para a página da turma (e T1 e T2 com link, se a DEC5 não for aprovada): o primeiro envio com link seria em 12/2026. **DEC6:** manter o nome planejado pelo O7 (os templates da Meta não voltam à aprovação), usar o mesmo nome nos links da NP2 e registrar o desvio na tabela de correspondência, como a DEC6 da onda 2 já faz com os meses que escorregam. A leitura usa a data de envio.
2. **366 em fevereiro.** O primeiro envio de 366 é em 05/02; por isso 202702. Se a OU20 mudar a data, o nome muda junto com o ciclo extra.
3. **Se o envio escorregar de mês** depois de o template da Meta estar aprovado: manter o nome planejado e registrar o desvio na tabela de correspondência (DEC6 da onda 2).
4. **Toque pós-início não tem link.** O PI pede "responda TURMA"; mede-se por contagem de respostas, sem UTM. O botão do e-mail que leva a wa.me não é rastreado pela UTM [CONFIRMAR P15].
5. **Pago e orgânico não mudam:** pago segue a chave `pos_<código>-<área curta>_<plataforma>_...` ratificada na seção 6 do plano; orgânico usa utm_medium=organic_social e utm_campaign=pos_<código>_<AAAAMM da primeira publicação da turma>.
6. **Teste de humano antes do primeiro envio:** clicar o link de um contato de teste e conferir no GA4 [CONFIRMAR ferramenta] a origem, o meio, a campanha e o conteúdo.

- **Agente:** arquiteto-de-fluxos (departamento 10), encomenda O10 do plano do CMO da onda 3 (versão 2), lote A
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Status:** rascunho para o qa-de-marketing (auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC8 (seção 15). **Nada é ligado, agendado, enviado ou pago.** Toda ação no CRM é de humano, depois da aprovação. Nenhum arquivo de .claude/commands foi criado: o texto do workflow está na seção 16.3.
- **Dados pessoais:** nenhum.

---

## 13. Fluxo de cada turma

Em todas as linhas valem **CC1 a CC12** (seção 5) e as saídas **SA1 a SA10** (seção 4). A coluna "Condição" traz só o que é específico do toque. "Saída padrão" quer dizer: quem pagou, respondeu, saiu ou foi suprimido não recebe; o toque suprimido não acumula. **"Cai se"** lista o que o contato precisa receber (aceito pela fila em ordem de prioridade, seção 6) para este toque ser suprimido: "no dia" é o mesmo dia; "na semana" é 2 toques do mesmo canal aceitos antes dele. **"Nunca cai"** quer dizer que nenhuma combinação do lote A, da onda 2, da onda 1 e da newsletter o derruba (o lote B reservado só passa à frente dos pós-inícios de 03 a 09/05). Os horários são e-mail às 9h e WhatsApp às 10h. A conta completa está nas seções 9 (pior caso) e 6 (ordem da fila). Cada tabela termina com "Como desfazer".

### 13.1 68628, Pós-graduação em Oncologia Veterinária (A10), lista L-A10, utm_campaign pos_68628_202701

Portão da turma: página publicada e conferida em 11/12 e reconferida em 04/01 (CC12); nenhuma peça cita o número da turma (P5). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; reconferência da página antes das 9h; primeiro toque de A10. **Nunca cai** (primeiro da fila no dia e na semana) | enviar E1 (botão "Ver a turma e as condições", utm_content=e1-68628); ligar a flag de saída da NP2 de A10 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | qua 20/01, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 657 em 21/01 (A1) e 333 em 19/01 (A11). Na variante de 341, 2 entre 657, 341 em 18/01 (A14 equinos) e 333 | enviar W1 (utm_content=w1-68628; template pos_68628_kit_w1 aprovado na Meta, se API [CONFIRMAR U11a]) | saída padrão |
| 3 | sex 05/02, 10h | **Nunca cai** (no máximo 1 WhatsApp à frente: 657 em 04/02) | enviar W2 (w2-68628) | saída padrão |
| 4 | qua 17/02, 9h | **Nunca cai** (primeiro e-mail da fila; no dia vence 366 e 68636 pela nota 60); cabe com a newsletter de 18/02 | enviar E2 (e2-68628) | saída padrão |
| 5 | qua 03/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 657 em 02/03 (A1) e 679 em 01/03 (A14) | enviar W3, com a frase de turma mínima sem número (w3-68628) | saída padrão |
| 6 | seg 05/04, 10h | **Nunca cai**, salvo com a DEC4: com ela, cai para quem está em A4 (o pré-início de 68632 do mesmo dia passa à frente) | enviar pré-início (pr-68628; pos_68628_kit_pr) | saída padrão |
| 7 | qua 28/04, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 289 PI em 27/04 e 68636 PI em 30/04 (as duas são de A2: basta estar em A2) | enviar PI, sem link, com a regra completa (3º módulo em 26 e 27/06/2027) e "responda TURMA"; resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 25/06 (SA3) |

**Como desfazer:** pausar a régua de 68628 no CRM, o que cancela os agendamentos pendentes dos toques 2 a 7; limpar a flag da NP2 de A10 (os contatos voltam à NP2 no próximo toque pendente, sem reenvio do que passou); a lista fica arquivada, não apagada. Toque já enviado não volta. SAIR e descadastro nunca são desfeitos.

### 13.2 68617, Pós-graduação em Endocrinologia de Pequenos Animais (A7), lista L-A7, utm_campaign pos_68617_202701

Portão da turma: URL com "/v/" conferida em 11/12, em 04/01 e antes de cada toque com link (OU29); nenhuma peça cita o número da turma (P5). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; URL conferida; primeiro toque de A7. **Cai se** recebe no mesmo dia o E1 de 68628 (A10) ou o E1 de 68636 (A2; nota 45 contra 36) | enviar E1 (e1-68617); ligar a flag de saída da NP2 de A7 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 22/01, 10h | **Cai se**, no dia, recebe o E1 de 679 (A14) ou o E1 de 68632 (A4); ou, na semana, 2 WhatsApp antes entre 657 em 21/01 (A1), 333 em 19/01 (A11), 68628 em 20/01 (A10), 68636 em 20/01 (A2) e, na variante de 341, 341 em 18/01 (A14 equinos) | enviar W1 (w1-68617; template pos_68617_kit_w1) | saída padrão |
| 3 | seg 15/02, 10h | **Cai se**, no dia, recebe o W1 de 68632 (A4); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68635 em 19/02 (A3), 68636 em 17/02 (A2) e 366 em 17/02 (A4) | enviar W2 (w2-68617) | saída padrão |
| 4 | qua 24/02, 9h | **Cai se**, no dia, recebe o E2 de 679 (A14) ou o W2 de 366 (A4, se couber no teto de WhatsApp); ou, na semana, 2 e-mails antes: 679 em 24/02 e 68636 em 26/02 (A14 e A2 juntas) | enviar E2 (e2-68617) | saída padrão |
| 5 | sex 12/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2), 68615 em 11/03 (A11), 68635 em 08/03 (A3) e 366 em 08/03 (A4) | enviar W3 (w3-68617) | saída padrão |
| 6 | seg 12/04, 10h | **Nunca cai** (só o pré-início de 68636, de 13/04, fica à frente); vence o PI de 341 de 14/04 | enviar pré-início (pr-68617) | saída padrão |
| 7 | qui 06/05, 10h | **Cai se**, na semana de 03 a 09/05, recebe antes 2 WhatsApp entre 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e, pela reserva do lote B, 719 pré-início em 03/05 (A14 719) e 68616 pré-início em 04/05 (A12) | enviar PI, sem link, com a regra completa (3º módulo em 19 e 20/06/2027); resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 18/06 (SA3) |

**Como desfazer:** pausar a régua de 68617 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A7; a lista fica arquivada. Se a URL com "/v/" não estiver conferida, o E1 e os toques com link não são agendados e nada acumula.

### 13.3 68636, Pós-graduação em Pneumologia Veterinária, turma VIII (A2), lista L-A2 (estendida), utm_campaign pos_68636_202701

Portão da turma: OU21 (data de 17/04 só no site): todos os toques saem com "abril de 2027" (texto aprovado do O7) até a resposta, menos o PI de 30/04, que só sai com a OU21 (O7, seção 7.7); com data diferente, ciclo extra. A lista L-A2 já existe (289). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 04/01, 9h | OC2 do E1; página conferida. **Cai se** recebe no mesmo dia o E1 de 68628 (A10). Vence o E1 de 68617 pela nota (45 contra 36) | enviar E1 (e1-68636); a flag de saída da NP2 de A2 já está ligada desde 08/12 (onda 2); se não estiver, liga às 00h05 | saída padrão |
| 2 | qua 20/01, 10h | **Cai se**, no dia, recebe o W1 de 68628 (A10) ou o E1 de 68635 (A3), o que couber primeiro na fila; ou, na semana, 2 WhatsApp antes: 657 em 21/01 (A1) e 333 em 19/01 (A11); na variante de 341, 2 entre 657, 341 e 333 | enviar W1 (w1-68636; template pos_68636_kit_w1) | saída padrão |
| 3 | qua 17/02, 10h | **Cai se**, no dia, recebe o E2 de 68628 (A10) ou o W1 de 366 (A4); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68632 em 15/02 (A4) e 68635 em 19/02 (A3) | enviar W2 (w2-68636) | saída padrão |
| 4 | sex 26/02, 9h | **Nunca cai** (só o E2 de 679, de 24/02, fica à frente) | enviar E2 (e2-68636) | saída padrão |
| 5 | seg 15/03, 10h | **Nunca cai** (só o W4 de 333, de 16/03, fica à frente, 1 WhatsApp) | enviar W3 (w3-68636) | saída padrão |
| 6 | ter 13/04, 10h | **Nunca cai** (vence o PI de 341 de 14/04 pela data de início) | enviar pré-início (pr-68636), com "abril de 2027" até a OU21 | saída padrão |
| 7 | sex 30/04, 10h | **Só com a OU21 (O7, seção 7.7): sem a data confirmada, o toque não sai.** **Nunca cai** (no máximo o PI de 289, de 27/04, fica à frente); vence a versão de WhatsApp da newsletter desse dia | enviar PI, sem link, com a regra completa (3º módulo em 19 e 20/06/2027); resposta vai a vendas de São Paulo | SA6; a lista fecha às 23h59 de 18/06 (SA3) |

**Como desfazer:** pausar a régua de 68636 sem mexer em L-A2 nem na régua de 289 (limpar só a marca de turma 68636); a flag da NP2 de A2 é da onda 2 e não muda aqui.

### 13.4 68635, Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, turma V (A3), lista L-A3, utm_campaign pos_68635_202701

Portão da turma: página conferida (a frase de "duas certificações", OU35, é da página); o PI só sai com o dia do 3º módulo (OU25). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | qua 20/01, 9h | OC2 do E1; primeiro toque de A3. **Cai se**, no dia, recebe o W1 de 68628 (A10), desde que ele caiba no teto de WhatsApp. Por teto semanal de e-mail nunca cai | enviar E1 (e1-68635); ligar a flag de saída da NP2 de A3 às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 05/02, 10h | **Cai se**, no dia, recebe o W2 de 68628 (A10) | enviar W1 (w1-68635; template pos_68635_kit_w1) | saída padrão |
| 3 | sex 19/02, 10h | **Cai se**, no dia, recebe o W1 de 679 (A14); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14) e 68632 em 15/02 (A4). Vence a newsletter por WhatsApp desse dia | enviar W2 (w2-68635) | saída padrão |
| 4 | seg 01/03, 9h | **Cai se**, no dia, recebe o W3 de 679 (A14). Por teto semanal de e-mail nunca cai | enviar E2 (e2-68635), com a frase-ponte de A3 sem link para 68623 (E19) | saída padrão |
| 5 | seg 08/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2) e 68615 em 11/03 (A11) | enviar W3 (w3-68635) | saída padrão |
| 6 | ter 06/04, 10h | **Nunca cai** (no máximo 1 WhatsApp à frente, o de 05/04) | enviar pré-início (pr-68635) | saída padrão |
| 7 | seg 03/05, 10h | **Só com o dia do 3º módulo (OU25).** **Cai se**, no dia, recebe o pré-início de 719 (A14 719, lote B reservado); ou, na semana, 2 WhatsApp antes entre 719 em 03/05, 68616 em 04/05 (A12, lote B), 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e 68617 PI em 06/05 (A7) | enviar PI, sem link, com a regra completa e o dia do 3º módulo; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 68635 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A3; a lista fica arquivada.

### 13.5 366, Pós-graduação em Fisioterapia, Fisiatria e Reabilitação Veterinária, turma I (A4), lista L-A4, utm_campaign pos_366_202702

Portão da turma: **OU20.** Nada sai antes da data confirmada; verificação às 18h de 03/02 [SUPOSIÇÃO do horário]: início em 10/04 confirmado, vale o calendário; aberta ou com 24/04, nenhum toque de 366 é agendado e nada acumula (ciclo extra com 24/04). Nenhuma peça diz "coordenação" (OU34). O PI só sai com a data e o dia do 3º módulo (OU25). Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 05/02, 9h | OC2 do E1; OU20 resolvida até 03/02 às 18h. **Cai se**, no dia, recebe o W2 de 68628 (A10) ou o W1 de 68635 (A3; só vale se ele couber); ou, na semana, 2 e-mails antes entre 657 em 01/02 (A1), 341 em 02/02 (A14 equinos) e 333 em 03/02 (A11) | enviar E1 (e1-366); a flag da NP2 de A4 já está ligada desde 22/01 (E1 de 68632) | saída padrão |
| 2 | qua 17/02, 10h | **Cai se**, no dia, recebe o E2 de 68628 (A10); ou, na semana, além do W1 de 68632 de 15/02 (que todo contato de A4 tem à frente), recebe antes 68615 em 16/02 (A11), 679 em 19/02 (A14) ou 68635 em 19/02 (A3) | enviar W1 (w1-366; template pos_366_kit_w1) | saída padrão |
| 3 | qua 24/02, 10h | **Cai se**, no dia, recebe o E2 de 679 (A14); ou, na semana, além do W2 de 68632 de 22/02, recebe antes 333 em 23/02 (A11) | enviar W2 (w2-366) | saída padrão |
| 4 | seg 01/03, 9h | **Cai se**, no dia, recebe o W3 de 679 (A14) ou o E2 de 68635 (A3). Para quem está só em A4, é a newsletter de 04/03 que cai (8.4, no -p2), não este e-mail | enviar E2 (e2-366) | saída padrão |
| 5 | seg 08/03, 10h | **Cai se**, no dia, recebe o W3 de 68635 (A3); ou, na semana, 2 WhatsApp antes entre 341 em 10/03 (A14 equinos), 289 em 09/03 (A2) e 68615 em 11/03 (A11) | enviar W3 (w3-366), com a frase de turma mínima sem número | saída padrão |
| 6 | qua 07/04, 10h | **Cai se** está em A3: o pré-início de 68635 (06/04) soma com o de 68632 ou de 68628 (05/04) e fecha 2 WhatsApp na semana | enviar pré-início (pr-366) | saída padrão |
| 7 | seg 03/05, 10h | **Só com a data e o dia do 3º módulo (OU20 e OU25).** **Cai se**, no dia, recebe o PI de 68635 (A3); ou, na semana, 2 WhatsApp antes entre 719 em 03/05 e 68616 em 04/05 (lote B reservado), 68615 PI em 05/05 (A11), 68632 PI em 04/05 (A4, só com OU3) e 68617 PI em 06/05 (A7) | enviar PI, sem link, com a regra completa; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 366 (cancela os agendamentos pendentes) e limpar só a marca de turma 366 em L-A4 (a régua de 68632 não muda); a flag da NP2 de A4 só é limpa se as duas réguas de A4 forem pausadas. Se a OU20 voltar a abrir, repetir a verificação.

### 13.6 68632, Pós-graduação em Clínica Cirúrgica de Cães e Gatos, turma V, Goiânia, presencial (A4), lista L-A4, utm_campaign pos_68632_202701

Portão da turma: **OU3** (módulo 1 presencial) e regra 8 (E22): nenhuma mensagem fala de entrada depois do início; o pré-início de 05/04 sai sem "matrícula aberta até o 3º módulo"; a data do 3º módulo (12 e 13/06) não aparece. Nenhuma peça diz "coordenação" (OU34). Campus Goiânia no assunto e na primeira linha (E17). Atendimento: vendas de Goiânia.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 22/01, 9h | OC2 do E1; primeiro toque de A4. **Cai se**, no dia, recebe o E1 de 679 (A14). Por teto semanal nunca cai | enviar E1 (e1-68632); ligar a flag de saída da NP2 de A4 às 00h05 (vale para 68632 e 366), mesmo que o E1 seja suprimido | saída padrão |
| 2 | seg 15/02, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp: 68615 em 16/02 (A11) e 679 em 19/02 (A14) | enviar W1 (w1-68632; template pos_68632_kit_w1) | saída padrão |
| 3 | seg 22/02, 10h | **Cai se**, no dia, recebe o W2 de 679 (A14). Por teto semanal só cairia com o W3 de 333 (23/02) e o W2 de 679 juntos, e o de 679 já o derruba | enviar W2 (w2-68632), com a frase de passagem e hotel só depois da turma confirmada | saída padrão |
| 4 | qua 03/03, 9h | **Cai se**, no dia, recebe o W3 de 68628 (A10), que só cabe se o contato não tem antes 657 em 02/03 e 679 em 01/03. Por teto semanal de e-mail nunca cai | enviar E2 (e2-68632); a newsletter de 04/03 cai para quem recebe este e o E2 de 366 (8.4, no -p2) | saída padrão |
| 5 | sex 05/03, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 657 em 02/03 (A1), 679 em 01/03 (A14) e 68628 em 03/03 (A10). Vence a newsletter por WhatsApp desse dia | enviar W3 (w3-68632) | saída padrão |
| 6 | seg 05/04, 10h | **Cai se**, no dia, recebe o pré-início de 68628 (A10; nota 60 contra 45), salvo com a DEC4. É a última mensagem de 68632 | enviar pré-início (pr-68632; pos_68632_kit_pr), sem a frase do 3º módulo | **a lista de 68632 fecha às 23h59 de 09/04 (SA4)** enquanto a OU3 estiver aberta |
| 7 | ter 04/05, 10h | **Não é agendado.** Só com a OU3 respondida, texto novo aprovado e qa; sem a OU3 nunca existe | nenhuma; reabertura é pedido novo (DEC6 da onda 2), com relatório de data nova | sem a OU3, a lista não reabre |

**Como desfazer:** pausar a régua de 68632 (cancela os agendamentos pendentes dos toques 2 a 6) e limpar só a marca de turma 68632 em L-A4 (a régua de 366 não muda); a flag da NP2 de A4 só é limpa se as duas réguas de A4 forem pausadas. A reabertura da lista depois de 09/04 só por pedido novo.

### 13.7 679, Pós-graduação em Infectologia Veterinária, turma IV (A14, infectologia), lista L-A14-679, utm_campaign pos_679_202701

Portão da turma: **OU19** (data de 03/04): todos os toques saem com "abril de 2027" (texto aprovado do O7) até a resposta; marca de curso (EN11, DEC7); o PI só sai com o dia do 3º módulo (OU25) e a data confirmada. A linha de campanha "Citopatologia 03/04" da visão de campanhas é da mídia (gestor), não do CRM. Atendimento: vendas de São Paulo.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | sex 22/01, 9h | OC2 do E1; [curso_de_interesse]=infectologia ou 679; primeiro toque do curso. **Nunca cai** (primeiro da fila no dia e na semana) | enviar E1 (e1-679); ligar a flag de saída da NP2 de A14 para infectologia às 00h05, mesmo que o E1 seja suprimido | saída padrão |
| 2 | sex 19/02, 10h | **Nunca cai** (no máximo o W de 68615, de 16/02, fica à frente); vence a newsletter por WhatsApp desse dia | enviar W1 (w1-679; template pos_679_kit_w1) | saída padrão |
| 3 | seg 22/02, 10h | **Nunca cai** (no máximo o W de 333, de 23/02, fica à frente) | enviar W2 (w2-679) | saída padrão |
| 4 | qua 24/02, 9h | **Nunca cai** (primeiro e-mail da fila no dia e na semana) | enviar E2 (e2-679) | saída padrão |
| 5 | seg 01/03, 10h | **Nunca cai** (no máximo o AC de 657, de 02/03, fica à frente) | enviar W3 (w3-679), com a frase de turma mínima sem número | saída padrão |
| 6 | seg 29/03, 10h | **Nunca cai**; mesmo com A14 numa lista só e os toques de 699, 719 e 382 do lote B, 679 vence pela data de início | enviar pré-início (pr-679), com "abril de 2027" até a OU19 | saída padrão |
| 7 | seg 26/04, 10h | **Só com o dia do 3º módulo (OU25) e a OU19.** **Cai se** está em A2 (289 PI em 27/04 e 68636 PI em 30/04 ficam à frente) | enviar PI, sem link, com a regra completa e o dia do 3º módulo; resposta vai a vendas de São Paulo | SA6; a lista fecha na véspera do 3º módulo (SA3); sem o dia, o toque não sai |

**Como desfazer:** pausar a régua de 679 (cancela os agendamentos pendentes dos toques 2 a 7); limpar a flag da NP2 de A14 para infectologia (a de equinos é da onda 2 e não muda); a marca [curso_de_interesse] é mantida: ela é filtro, não envio.

### 13.8 68609, Pós-graduação em Anestesiologia Veterinária, turma VIII, Goiânia (A1), lista L-A1 (estendida), utm_campaign pos_68609_202701

Portão da turma: o convite da prova de Especialista que a página traz é item do OC1-A (nenhuma peça o repete); L-A1 já existe (657). Atendimento: vendas de Goiânia.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | qua 20/01, 9h | OC2 do E1. **Cai se**, no dia, recebe o W1 de 68628 (A10), o E1 de 68635 (A3) ou o W1 de 68636 (A2), cada um quando couber. Por teto semanal de e-mail nunca cai sem um desses | enviar E1 (e1-68609); a flag de saída da NP2 de A1 já está ligada desde 05/01 (E1 de 657); se não estiver, liga às 00h05 | saída padrão |
| 2 | seg 15/02, 10h | **Cai se**, no dia, recebe o W1 de 68632 (A4) ou o W2 de 68617 (A7); ou, na semana, 2 WhatsApp antes entre 68615 em 16/02 (A11), 679 em 19/02 (A14), 68635 em 19/02 (A3) e 68636 em 17/02 (A2) | enviar W1 (w1-68609; template pos_68609_kit_w1) | saída padrão |
| 3 | qui 25/02, 10h | **Cai se**, na semana, recebe antes 2 WhatsApp entre 333 em 23/02 (A11), 679 em 22/02 (A14), 68632 em 22/02 (A4) e 366 em 24/02 (A4). A4 sozinha já traz 2 | enviar W2 (w2-68609) | saída padrão |
| 4 | seg 08/03, 9h | **Cai se**, no dia, recebe o W3 de 68635 (A3) ou o W3 de 366 (A4), o que couber. Por teto semanal nunca cai | enviar E2 (e2-68609); os nomes de 657 e 359 entram sem link (E19) | saída padrão |
| 5 | qua 17/03, 10h | **Cai se**, na semana, recebe antes 333 em 16/03 (A11) e 68636 em 15/03 (A2) | enviar W3 (w3-68609) | saída padrão |
| 6 | seg 19/04, 10h | **Nunca cai** (vence o PI de 657 de 20/04: referência de 24/04 contra 21/05) | enviar pré-início (pr-68609) | saída padrão |
| 7 | ter 11/05, 10h | **Nunca cai** (no máximo o PI de 333, de 12/05, só com OU3, fica à frente) | enviar PI, sem link, com a regra completa (3º módulo em 26 e 27/06/2027); resposta vai a vendas de Goiânia | SA6; a lista fecha às 23h59 de 25/06 (SA3) |

**Como desfazer:** pausar a régua de 68609 e limpar só a marca de turma 68609 em L-A1 (a régua de 657 não muda); a flag da NP2 de A1 é da onda 2 e não muda aqui.

---

## 14. Campos do CRM

Nomes provisórios [SUPOSIÇÃO]. Nenhum guarda dado pessoal em arquivo da squad; o CRM guarda no contato e a squad lê só contagens. **Esta onda não cria campo novo**: reaproveita os da onda 2 (seção 12 do arquivo dela) e acrescenta valores.

| Campo | Onde | Tipo | Uso | Situação e valores desta onda |
|---|---|---|---|---|
| [opt_in_email], [opt_in_whatsapp] (com data, origem, finalidade) | contato | sim ou não | EN1 a EN3 | existe no desenho |
| [área_de_interesse], [praça] | contato | texto | listas | existe; valores A1, A2, A3, A4, A7, A10 e A14 |
| [curso_de_interesse] | contato | texto ou etiqueta | L-A14-679 (infectologia ou 679) e L-A14E (equinos ou 341) | novo na onda 2; esta onda acrescenta o valor "infectologia" |
| [respondeu_em], [pediu_sair], [matriculou] | contato | data ou sim ou não | SA1, SA5, SA6 | existe |
| [time_assumiu] | contato | sim ou não | EN5, SA6 | novo na onda 2 |
| [fim_janela_silencio], [vinculo_ufape] | contato | data, lista | EN7, EN6 | existe |
| [base_graduacao] | contato | sim ou não | teto de 3 por semana (CC8) | novo na onda 2 |
| [regua_com_data_ativa_área] | contato, por área (por curso em A14) | sim ou não | EN12, seção 11 (-p2) | existe; esta onda liga A10, A7, A3, A4 e A14 infectologia |
| [kit_ultimo_toque_<código>] | contato, por turma | texto | EN8, auditoria | novo na onda 2; códigos 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609 |
| [kit_saiu_motivo_<código>] | contato, por turma | pagou, pagou_mesma_area, data_limite, regra8, sair, descadastro, devolucao, respondeu, turma_parada, engajamento | SA1 a SA10; leitura só somada | novo na onda 2; esta onda troca "pagou_gemea" por "pagou_mesma_area" (DEC3) e acrescenta "regra8" (SA4) |
| [wa_campanha_sem_interacao] | contato | número | SA9 (E1) | novo na onda 2 |
| [data_limite_turma], [estado_da_turma_hoje] | turma | data, texto | SA3, SA4, CC4 | valores: 68628 e 68609, 25/06/2027; 68617 e 68636, 18/06/2027; 68632, 09/04/2027 (11/06 com OU3); 679, 68635 e 366, 31/05/2027 até a OU25 (trava de segurança) |
| [nota_gut_fila] | turma | número | desempate da seção 6.2 | valores: 68628 = 60; 68632, 68636 e 679 = 45; 68635 e 366 = 36 (desempate por urgência: 68635 = 4, 366 = 3); 68617 = 36; 68609 = 12 |
| [data_do_item] | turma | data | D2, seção 6.1 | início antes de começar; véspera do 3º módulo depois; PI sem dia fica depois de qualquer dia de junho (DEC2) |
| registro de supressão | contagem | número por semana, motivo (dia, teto semanal, fila), toque e combinação de áreas | relatório do cmo e painel somado | novo na onda 2; esta onda acrescenta semana e combinação de áreas, para a tabela 9.2 |

---

## 15. Pedidos de aprovação humana e como desfazer cada automação

Quem aprova: a pessoa do marketing que aprovou o plano geral, até a tabela de ufape-geral.md ser preenchida (A9) [CONFIRMAR]. Quem executa no CRM: [CONFIRMAR]. **Nada abaixo está ligado.** O envio de cada toque continua sendo o OC2 do plano da onda 3, uma aprovação por toque.

### 15.1 Automações (AF)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AF1 | Criar L-A3, L-A4, L-A7, L-A10 e L-A14-679 e estender L-A1 e L-A2 com as marcas de 68609 e de 68636, em **rascunho**, com os filtros das seções 2 e 3, sem agendar envio | uma regra única de quem recebe cada kit | sem custo de mídia; horas de quem configura [CONFIRMAR]; tamanho de cada lista só somado [CONFIRMAR, OC2] | sete listas auditáveis, sem envio | arquivar a lista nova (não apaga contato nem histórico); nas estendidas, remover só a marca de turma (a lista da onda 2 não muda) |
| AF2 | Ligar as regras de saída SA1 a SA10 para as 8 turmas, a regra 8 de 68632 (a lista fecha às 23h59 de 09/04 sem OU3), a trava de 31/05 para 679, 68635 e 366 e a reconferência antes do disparo (06h e 30 minutos antes) | o plano manda sair quem pagou, a turma depois da data limite, 68632 na véspera do início e o descadastro em até 48 h | sem custo de mídia; horas [CONFIRMAR] | ninguém recebe o que já não cabe | desligar regra por regra e voltar ao envio com conferência manual. **SA5 (SAIR e descadastro) não se desliga** |
| AF3 | Ligar a fila em ordem de prioridade da seção 6 (data de referência da decisão 4, nota GUT só para empate), o 1 por dia, o teto de 2 e 2 (1 no E1; 3 na base da Graduação), os dias sem campanha e o aviso ao cmo quando um dia passar de 4 toques da onda 3 ou repetir área | toda a base da Pós divide o teto; sem fila o CRM aplicaria a ordem de agendamento | sem custo de mídia; horas [CONFIRMAR] | no máximo 1 mensagem por dia e 2 e 2 por semana para o contato, sem exceção manual | desligar a fila e voltar à conferência manual semana a semana (só com decisão do cmo); o teto e o limite diário são suposições do cmo e voltam ao valor anterior só pelo R1 do plano |
| AF4 | Agendar os 55 toques nas datas da seção 7 (o 56º, PI de 68632 em 04/05, **não** é agendado), cada um **só depois do OC2 daquele toque**, do qa próprio e do teste de humano; 366 com o portão OU20 (verificação em 03/02, 18h), 679, 68635 e 366 no PI só com o dia do 3º módulo, o PI de 68636 só com a OU21, 679 e 68636 com "abril de 2027" até a OU19 e a OU21 | a base é a alavanca mais barata da turma | sem custo de mídia; custo por conversa de marketing do WhatsApp Business se o envio for por API [CONFIRMAR U11a]; o valor precisa vir antes de 04/01 | 16 e-mails e 39 WhatsApp dentro do teto | cancelar o agendamento do toque ou pausar a régua; toque já enviado não volta, por isso cada toque tem aprovação própria |
| AF5 | Ligar a saída da NP2 nas datas da seção 11 (-p2): A10 e A7 em 04/01, A3 em 20/01, A4 e A14 infectologia em 22/01; e, só se a flag da onda 2 não estiver ligada, A2 em 04/01 e A1 em 20/01 | dono único do convite | sem custo | a nutrição não repete o convite do kit | limpar a flag [regua_com_data_ativa_área] da área (volta à NP2 no próximo toque pendente, sem reenviar o passado) |
| AF6 | Parametrizar a UTM da seção 12 (-p2) em links e templates e registrar na tabela de correspondência o desvio da NP2 de dezembro e os dois nomes do utm_content do pré-início ("ac" e "pr") | atribuição por turma | sem custo | cliques e respostas por toque, só somados | trocar o nome na tabela de correspondência; link já enviado mantém a UTM antiga |
| AF7 | Ligar o registro de supressões por semana, motivo, toque e combinação de áreas e o relatório de segunda-feira com a tabela 9.2 (-p2) | o cmo lê só número somado e precisa saber quantos toques a fila cortou | sem custo de mídia; horas [CONFIRMAR] | relatório de segunda-feira com supressões por semana e motivo | desligar o registro; nenhum dado pessoal sai do CRM |

### 15.2 Decisões de política (DEC)

| # | Decisão proposta | Quem decide | Se não for aprovada |
|---|---|---|---|
| DEC1 | **Fila em ordem de prioridade:** o CRM aceita os toques candidatos na ordem da D2 e recusa o que fecharia o dia ou o teto da semana; um concorrente só derruba outro se ele mesmo for aceito. Mesmo resultado da tabela 7.4 da onda 2 (em 14 a 20/12 a newsletter fica para quem perde o W1 de 333). | cmo | o CRM corta o dia e depois a semana, o que deixa o contato sem nenhum dos dois toques onde bastava cortar um (20/01 e 01/03 desta onda, 17/12 da onda 2) |
| DEC2 | **Notas GUT por turma e posição dos pós-inícios sem dia:** 68628 = 60; 68632, 68636 e 679 = 45; 68635 e 366 = 36 (68635 na frente pela urgência); 68617 = 36; 68609 = 12. PI de 679, 68635 e 366 ficam depois de qualquer referência com dia de junho até a OU25. Vale só para empate de data de referência. | cmo | a fila fica sem desempate e o CRM decide pela ordem de agendamento, o que não é explicável |
| DEC3 | **Pagou uma turma, sai das outras turmas da mesma área** (68632 e 366; 68609 e 657; 68636 e 289). Só dos toques; o contato segue elegível a outras áreas. Se o CRM já trata S6 como matriculado em qualquer turma, só confirma. | pessoa do marketing | cada turma sai só a sua e o contato que pagou uma turma continua a receber os toques das outras da área |
| DEC4 | **Opcional: o pré-início de 68632 de 05/04 passa à frente do de 68628 só nesse dia.** É a última mensagem de 68632 antes de a regra 8 fechar a lista; 68628 ainda tem o PI de 28/04. Muda quem perde o toque para quem está em A10 e A4. | cmo | vale a nota: quem está em A10 e A4 perde o pré-início de 68632 |
| DEC5 | **NP2 e página de abril antes de 11/12:** o T1 (01/12) e o T2 (09/12) da NP2 de A3, A4, A7, A10 e A14 infectologia saem sem link para a turma de abril (ou ficam suspensos nessas áreas) e o T3 (16/12) só depois da conferência de 11/12. Sem acúmulo se a conferência atrasar. | cmo, com a pessoa do marketing | a NP2 aponta para páginas com "CERTIFICADO PELO MEC", contra a regra 13, salvo decisão humana registrada no OC1 com a regulação |
| DEC6 | **UTM:** manter os nomes do O7 (202701; 202702 em 366), usar o mesmo nome nos links da NP2 de dezembro e registrar o desvio na tabela de correspondência | pessoa do marketing | o nome muda para 202612 nos links de dezembro e os templates da Meta voltam à aprovação |
| DEC7 | **A14 por curso:** lista e flag de NP2 de A14 por [curso_de_interesse] (L-A14-679 só para infectologia ou 679); sem a marca, o contato não entra | cmo | A14 numa lista só: 679 vence todos os A14 do lote B pela data, mas a flag de A14 em 22/01 tiraria da NP2 quem quer 382, 699 ou 60 antes do kit deles |
| DEC8 | **Newsletter por WhatsApp nos dias de kit (19/02, 05/03 e 30/04):** o kit vence e a versão da newsletter não muda de dia. Nota ao agente newsletter, sem alterar o arquivo dele, com a edição 7 sem 662 e só com 366 se a data estiver confirmada (CF7) | newsletter, com o cmo | a newsletter por WhatsApp concorre com o kit e pela fila perde o dia do mesmo jeito (prioridade 5) |

---

## 16. Etapas, cortes e o workflow de reuso

### 16.1 Quantas etapas

| Fluxo | Etapas | Chamadas de agente | Aprovações humanas |
|---|---|---|---|
| Este desenho (O10, lote A) | 1 | 1 (arquiteto-de-fluxos) | 1 |
| Conferência do qa (O18c, "onda3c") | 1 | 1 (qa-de-marketing) | 1 |
| Execução no CRM (etapas 4 a 7 do documento de fluxo) | 4 | 0 (humano) | 4 mais 1 por toque (OC2) |
| Nova versão com o lote B (O10, 22/01/2027) | 1 | 1 | 1 |
| Workflow de reuso `/conferir-fila-de-mensagens` (16.3) | 2 | 2 | 2 |

### 16.2 O que foi cortado (nenhum corte muda a entrega)

1. Agente próprio para validar calendário: cortado. A conta está nas seções 7 a 9 e o qa-de-marketing a confere.
2. Nova rodada de copy-de-mensagens: cortada. Os textos e as datas são os do O7; este arquivo não toca neles. As duas correções de contagem (CF1 e CF2) vão como nota.
3. Reenvio de e-mail para quem não abriu: cortado (DEC4 da onda 2 mantida). Cada reenvio seria um toque a mais na fila.
4. Lista por curso em A1, A2, A3, A4, A7 e A10: cortada. A área basta; só A14 vira lista de curso.
5. Lista própria para 68632 e para 366: cortada. A4 é uma lista com duas marcas de turma.
6. Exceção codificada para 20/01, 01/03 ou 17/02: cortada. A fila em ordem de prioridade resolve sozinha.
7. Nota GUT por contato: cortada. A nota é por turma e só desempata data de referência igual.
8. Painel novo de acompanhamento: cortado. Usa-se o painel somado que o analista-de-dados já tem como encomenda (13.4 do plano geral).
9. Datas de contingência para página atrasada: não reservadas. Se o atraso acontecer, o arquiteto entrega nova versão com a conta da seção 9 refeita (como o CF8 da onda 2), para não bloquear dias à toa.
10. Lista, regra e toque para 662: nenhum (espera total, OU18).
11. Workflow semanal novo de revisão: cortado. A revisão de segunda-feira do cmo já existe e lê as contagens.

### 16.3 Texto do workflow para .claude/commands (não gravado)

Arquivo `.claude/commands/conferir-fila-de-mensagens.md`, versão revisada do texto proposto na onda 2 (fila em ordem de prioridade, conferência contra ondas anteriores e supressões por semana). Serve para a onda 3, lote B, e para qualquer onda ou turma nova na mesma base:

```
---
description: Confere listas, opt-in, saídas, fila D2, limite de 1 por dia, teto semanal, saída da NP2 e UTM de um lote de turmas contra as ondas já aprovadas e a newsletter. Cadeia: arquiteto-de-fluxos, qa-de-marketing
argument-hint: [linha: pos, livres ou eventos] [caminho do arquivo com os toques do lote] [turmas do lote] [arquivos de fluxos das ondas anteriores]
---
Execute o workflow "Conferir a fila de mensagens de um lote".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha, arquivo de toques, turmas e arquivos de fluxos anteriores deste pedido: $ARGUMENTS

Regras: siga o teto D16 e as regras E1 a E4 da seção 13 de saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md e a fila D2 da seção 12, com a data de referência da decisão do plano da onda (início antes de começar, véspera do 3º módulo depois). Dados de curso só de contexto/catalogo-de-cursos.md; o que faltar vira [CONFIRMAR NO CATÁLOGO]. Nenhum dado pessoal. Nada é ligado, agendado, enviado ou pago. Nunca use travessão.

1. Use o agente arquiteto-de-fluxos para produzir as listas por área, o opt-in S2 e S3, as regras de saída, a fila D2 aplicada em ordem de prioridade, a conta semana a semana do pior caso contra os toques das ondas anteriores e a newsletter, a saída da NP2 só nas áreas que ainda não saíram, as supressões previstas por semana (só números), a UTM do CRM, o fluxo de cada turma e os pedidos de aprovação (o que, por que, quanto, efeito esperado, como desfazer). Use a skill matriz-gut (.claude/skills/matriz-gut/SKILL.md) só para desempatar toques com a mesma data de referência e a skill mapear-fluxo (.claude/skills/mapear-fluxo/SKILL.md) para o SIPOC. Salve e passe o arquivo para a próxima etapa.
2. Use o agente qa-de-marketing para conferir o arquivo contra os toques aprovados, as datas e os dias da semana, o teto, a fila e as supressões, e devolver aprovado ou as correções numeradas. Salve e passe o arquivo para a próxima etapa.
3. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto.
4. Rode também auditorias/07-email-e-whatsapp.md nas listas e nas saídas.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: nenhum dia do lote tem dois toques para o mesmo contato, nenhuma semana passa de 2 WhatsApp e 2 e-mails (3 somando canais na base da Graduação), todo empate de data de referência tem desempate escrito, toda supressão prevista tem número por semana, toda automação tem pedido de aprovação com o que desfazer, nenhuma UTM foge de pos_<código>_<AAAAMM> e o lote está aprovado pelo qa-de-marketing e pela pessoa do marketing.
```

Este workflow tem **2 etapas de agente**: 2 chamadas ao Claude e 2 aprovações humanas, mais as auditorias. Cita só agentes, skills e auditorias que existem no repositório (arquiteto-de-fluxos, qa-de-marketing, matriz-gut, mapear-fluxo, auditorias 10-operacoes, 07-email-e-whatsapp e conformidade-educacional).

---

## 17. Auditorias

**auditorias/10-operacoes.md**
- [ ] conhecimento/INDICE.md está atualizado: **não feito por este agente** (a encomenda manda editar só este arquivo, que agora são três partes); o orquestrador atualiza.
- [x] Todo workflow cita só agentes, skills e auditorias que existem (arquiteto-de-fluxos, qa-de-marketing, matriz-gut, mapear-fluxo, auditorias 10-operacoes, 07-email-e-whatsapp e conformidade-educacional).
- [x] Todo workflow termina com auditoria e critério de pronto conferível (16.3 e "Concluído quando" da seção 1.2).
- [x] Aprovação humana antes de publicar, enviar ou pagar (AF1 a AF7, DEC1 a DEC8, OC2 por toque).
- [x] Acesso mínimo: a squad escreve texto; o CRM é de humano.
- [x] Nenhuma chave em arquivo de texto.
- [x] Documento com data de revisão (11/12/2026, 04/01/2027 e 22/01/2027).
- [ ] Toda peça pública passou por qa-de-marketing e por conformidade-educacional: este arquivo não é peça pública; vai ao qa (O18c, "onda3c").
- [x] Dados de curso batem com o catálogo: nome, turma, campus, modalidade e início citados vêm do catálogo (seção 2) e do plano; nenhum preço, bolsa ou ato regulatório neste arquivo. As metas em reais da seção 6.2 são o total do catálogo multiplicado por 15 (decisão 16).

**auditorias/07-email-e-whatsapp.md**
- [x] Consentimento e descadastro funcionando: EN1 a EN3, SA5; teste de humano antes do primeiro envio.
- [x] Cada mensagem tem um objetivo: herdado do O7.
- [x] Assuntos e primeiras linhas honestos: do O7; não tocados aqui.
- [x] Segmentos recebem mensagens da etapa da jornada: S2 e S3 da área; S6, S8 e S9 fora (EN6).
- [x] Réguas têm regras de saída: seção 4 e saídas por turma da seção 13.
- [ ] Resultados registrados para cada envio: registro de supressões (AF7) e UTM (seção 12); depende do CRM [CONFIRMAR P15].
- [ ] Cliques, respostas e conversões medidos: UTM e contagem de respostas "TURMA"; o PI não tem clique.
- [x] WhatsApp em horário comercial, com frequência humana e template da Meta quando usar a API: CC5, CC7, CC8; template só se a Ufape usar API (U11a).

**auditorias/conformidade-educacional.md**
- [x] Nenhuma peça nova: o arquivo não tem texto de mensagem nem de página.
- [x] Sem frase ligada ao MEC, sem preço, sem bolsa, sem "últimas vagas", sem nota de curso, sem promessa: nada disso aparece. A frase "CERTIFICADO PELO MEC" só aparece entre aspas como o que a página de origem traz e que bloqueia o envio (DEC5).
- [x] WhatsApp e e-mail só com consentimento e saída fácil (EN1 a EN3, SA5).
- [x] Nenhum dado pessoal em peça ou arquivo de trabalho.
- [x] Status "aberto" (ou "verificar" só por já ter começado, decisão 18): CC4.
- [x] Regra 8 de 68632 (nada sobre entrada depois do início, lista fecha em 09/04 sem OU3): SA4 e 13.6.
- [ ] Página de destino entrega o que a mensagem promete: pendente do OC1-A; trava no CC12 e na DEC5.
- [ ] Formulários com finalidade e política de privacidade: pendente externo, conferido em 11/12 e 04/01.

**Resultado:** pronto para o qa-de-marketing (O18c). A execução depende do OC2 por toque, do OC1-A, de AF1 a AF7, de DEC1 a DEC8 e das respostas de OU3, OU19, OU20, OU21, OU25, OU29, U11a e P15. Busca de travessão e meia-risca: feita pelo agente na escrita; a conferência por busca é do orquestrador.

**Próximo agente sugerido:** qa-de-marketing (O18c, revisão "onda3c": fluxos, com auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md).

---

## Fatos (com fonte)

- Os 55 toques do lote A (16 e-mails e 39 WhatsApp), mais 1 reservado de 68632, as datas, os horários (e-mail 9h, WhatsApp 10h), os templates, os IDs de utm_content e a regra de que 679, 68635 e 366 dependem do dia do 3º módulo: O7 (copy-de-mensagens-pos-2026-10-27-onda3.md, seções 0.1, 0.2 e 2) e plano do CMO da onda 3, seção 7.3. A contagem de 55 e os 14 dias com mais de um toque conferem com o O7 (seção 0, item 2, e seção 10.2) e com a seção 7.2 deste arquivo.
- Início, turma, campus, modalidade e status "aberto" das 8 turmas: contexto/catalogo-de-cursos.md, seção 2 (linhas de 679, 68632, 68635, 366, 68628, 68617, 68636 e 68609). Totais do catálogo usados nas metas: R$ 33.000,00 (679, 68632, 68635 e 366), R$ 38.940,00 (68628), R$ 36.000,00 (68617), R$ 37.950,00 (68636) e R$ 32.450,00 (68609).
- 3º módulo e fechamento das listas (26 e 27/06 em 68628 e 68609; 19 e 20/06 em 68617 e 68636; 12 e 13/06 em 68632; junho sem dia em 679, 68635 e 366): plano da onda 3, seções 1.1 e 4.1 a 4.9; O7, seção 0.1. Regra 8 e mídia de 68632 até 09/04: plano, seção 2.1 (regra 8) e 4.2.
- Teto de 2 WhatsApp e 2 e-mails por semana somando linhas, 1 por dia, janela, dias sem campanha, regras E1 a E4 e fila D2 com a newsletter em 5º: plano da onda 3, regra 11; newsletter-geral, seção 3.2; docs/execucao-2026-10-26.md, decisão 17.
- Data de referência (início antes, véspera do 3º módulo depois): plano da onda 3, seção 6, decisão 4; resultado da fila em cada semana de 7.4 do plano (que este arquivo confere).
- Datas da onda 2 (37), onda 1 (6) e das edições da newsletter: plano da onda 3, seção 7.3; arquiteto-de-fluxos-pos-2026-10-27-onda2.md, seção 7.1; newsletter-geral, seção 3.1. NP2 (T1 em 01/12, T2 em 09/12, T3 em 16/12 e T4 em 05/01): campanhas-de-nutricao-pos, seção 4. Saída da NP2 por área nas datas de 04/01, 20/01 e 22/01: plano da onda 3, seção 7.3, regra "Saída da NP2".
- Notas de grupo GUT 30 (5, 2, 3) das turmas de abril: cmo-geral, seção 3. Notas da onda 2 (341 = 80; 289 e 68615 = 48; 657 e 333 = 45): meu arquivo da onda 2, seção 7.4. Desempate (urgência, depois menor esforço): skill matriz-gut, passo 5.
- Metas em reais por turma de abril: plano da onda 3, seção 1 (15 vezes o total do catálogo; decisão 16).
- Decisões 11, 14, 16, 17 e 18: docs/execucao-2026-10-26.md. Pós-início: matrícula até o 3º módulo (decisão 18).
- Calendário: 01/01/2027 é sexta-feira; 08 e 09/02 são Carnaval; 10/02 é Cinzas; 26/03 é sexta-feira da Paixão; 28/03 é domingo de Páscoa; 21/04 é quarta-feira (Tiradentes); 01/05 é sábado; 04/01, 15/02, 22/02, 01/03, 08/03, 15/03, 29/03, 05/04, 12/04, 19/04, 26/04 e 03/05 são segundas-feiras.
- As ferramentas do agente arquiteto-de-fluxos são Read e Write: ele não executa no CRM (.claude/agents/arquiteto-de-fluxos.md).

## [SUPOSIÇÃO]

- As notas GUT por turma e a escala (G pela meta em reais, U pela data de início com ajustes para 68632 e 366, T pela turma I) (seção 6.2), ancoradas nas notas da onda 2.
- [data_do_item] igual à data limite quando a turma já começou (herdada da onda 2); posição dos pós-inícios sem dia (679, 68635 e 366) depois de qualquer dia de junho, como posição na fila, nunca como data de peça.
- Trava de segurança de 31/05/2027 para o fechamento das listas de 679, 68635 e 366 até a OU25.
- Fila em ordem de prioridade (DEC1) como leitura correta da D2 e do resultado já aprovado da tabela 7.4 da onda 2.
- Pagou uma turma, sai das outras da mesma área (DEC3); resposta a um toque de uma turma de A4 só tira a turma respondida.
- Não filtrar L-A1 e L-A4 por praça.
- A14 com lista e flag de NP2 por curso (DEC7).
- "Pior caso" como o contato que está em todas as áreas que disputam a semana, com opt-in nos dois canais.
- Geração da lista às 06h e reconferência 30 minutos antes; horário de verificação da OU20 às 18h de 03/02; aprovação dos pedidos até 11/12; testes de 14 a 18/12.
- Horários de job (00h05) para a saída por data limite e para a flag da NP2.
- Edições da newsletter depois de 18/02 em quintas quinzenais (decisão 10 do plano) e versão de WhatsApp no dia seguinte a cada edição.
- Nomes provisórios dos campos do CRM da seção 14.
- Resposta com "parar" ou parecida vai a humano para registro; a flag da NP2 liga mesmo com o primeiro toque do kit suprimido.
- Os prazos de 48 h e de 24 h dependem da ferramenta; a regra de E3 é o limite máximo.
- Que o CRM pode tratar S6 como "matriculado em qualquer turma de Pós" (efeito da DEC3).

## [CONFIRMAR]

- **OU3** (reposição dos módulos presenciais; 68632 depois do início), **OU6** (3º módulo: véspera ou 1º dia), **OU19** (data de 679 e linha "Citopatologia 03/04"), **OU20** (início de 366: 10/04 ou 24/04), **OU21** (data de 68636), **OU25** (dia do 3º módulo de 679, 68635 e 366), **OU29** (URL "/v/" e turma de 68617), **OU34** (quem representa 68632 e 366), **U11** (valor da inscrição, para distinguir inscrição de 1ª mensalidade na SA1), **U11a** (API oficial do WhatsApp e templates), **P15** (ferramenta de CRM, e-mail e WhatsApp, e rastreio de wa.me), **OU18** (662, que fica sem lista).
- Contatos com opt-in por área e canal e o tamanho de cada lista (OC2); campo de finalidade aceita; existência da marca [curso_de_interesse]; como o CRM marca conversa ativa com o time; se o CRM trata S6 como matriculado em qualquer turma.
- Se as flags de NP2 de A1 (05/01) e A2 (08/12) da onda 2 foram ligadas (CF10); se AF1 da onda 2 foi aprovada (L-A1 e L-A2).
- Quem executa no CRM, quem aprova cada tipo de peça (A9) e o custo por conversa de marketing, se houver API.
- Datas da newsletter depois de 18/02 e existência de WhatsApp nas edições 3 a 7; calendário da Graduação (CF6 da onda 2).
- Decisão humana sobre a NP2 com link para página de abril antes de 11/12 (DEC5) e sobre página com frase ligada ao MEC (regra 13, OC1 com a regulação).
- Tabela de correspondência entre nomes de campanha (analise-de-midia) para os desvios de mês (DEC6).
- Toques do lote B (O10 de 22/01/2027), que refaz a conta das semanas de 03 a 09/05 e seguintes.
