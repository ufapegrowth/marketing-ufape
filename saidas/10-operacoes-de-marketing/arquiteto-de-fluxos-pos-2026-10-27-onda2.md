# Fluxos de CRM do kit das 5 turmas de março de 2027 da Pós-graduação (657, 341, 289, 68615 e 333): listas, fila D2, saídas, NP2 e UTM

- **Agente:** arquiteto-de-fluxos (departamento 10, Operações de Marketing), encomenda F10 do plano do CMO da onda 2 (versão 2)
- **Linha:** pos
- **Data:** 27/10/2026 (terça-feira)
- **Versão:** 1
- **Encomenda:** F10 de saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (linha F10, regras 1 a 12 e seção 7.3). O plano previa o nome arquiteto-de-fluxos-geral-2026-11-24.md; este arquivo usa o nome pedido na encomenda de 27/10/2026.
- **Status:** rascunho para o qa-de-marketing (auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md) e para a aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC7 (seção 13). **Nada é ligado, agendado, enviado ou pago.** Toda ação no CRM é de humano, depois da aprovação. Nenhum arquivo de .claude/commands foi criado: o texto do workflow está na seção 14.
- **Entradas lidas (em /home/user/marketing-ufape/):**
  - CLAUDE.md (do orquestrador da squad)
  - docs/execucao-2026-10-26.md (decisões 1 a 20; pesam 11, 14, 17 e 18)
  - contexto/ufape-geral.md e contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md (cabeçalho e início da seção 2, para conferir a regra de fonte; as datas das 5 turmas vêm do plano e do F7, que as tiram da seção 2 e das fichas)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-27-onda2.md (v2; seções 1, 2, 4.6, 6, 7, 8, 9, 10)
  - saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md (seção 3 de GUT; seção 12, D1 a D12; seção 13, D16 e E1 a E4)
  - saidas/02-estrategia-e-posicionamento/cmo-pos-2026-10-26.md (seção 6, calendário da onda 1, e 8.2)
  - saidas/07-email-whatsapp-relacionamento/copy-de-mensagens-pos-2026-10-27-onda2.md (F7, inteiro: calendário 0.1, UTM 0.2, seção 7 com o teto por área e os cortes da fila D2)
  - saidas/07-email-whatsapp-relacionamento/newsletter-geral-2026-10-26.md (seções 0 a 5: calendário 3.1 e fila 3.2)
  - saidas/07-email-whatsapp-relacionamento/estrategia-de-relacionamento-pos-2026-10-26.md (seções 3 e 4: segmentos S1 a S12)
  - saidas/06-geracao-de-demanda/campanhas-de-nutricao-pos-2026-10-26.md (seções 0 a 7: NP1, NP2, NP3, calendário do lote e UTM)
  - saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-geral-2026-10-26.md (minha saída anterior: seções 3, 6 e listas finais)
  - templates/documento-de-fluxo.md; .claude/skills/mapear-fluxo/SKILL.md; .claude/skills/matriz-gut/SKILL.md; .claude/agents/arquiteto-de-fluxos.md
  - auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md
- **Não aberto:** faculdade.ufape.com.br; nenhuma busca na web; o arquivo do qa da onda 2; o calendário da Graduação e os planos da onda 3 (A1 com 68609 e 359; A2 com 68636 e 352), que não estavam nas entradas; as fichas das turmas (os dados delas vêm do plano e do F7).
- **Dados pessoais:** nenhum. O arquivo fala de listas, campos do CRM entre colchetes e contagens somadas. Nenhum nome de aluno, candidato ou docente.
- **Marcadores:** [CONFIRMAR] é dado que só a Ufape tem. [SUPOSIÇÃO] é escolha ou hipótese deste agente, com a origem. Notas de GUT são avaliação do agente, não medida.

---

## 0. Resumo

1. **O que é:** as regras de CRM para os 34 toques do kit das 5 turmas de março (10 e-mails e 24 WhatsApp, mais 1 toque reservado de 333 sem texto): quem entra em cada lista, quem sai, em que ordem a fila D2 decide, como o limite de 1 mensagem por dia e o teto de 2 WhatsApp e 2 e-mails por semana são aplicados, quando a NP2 da área sai e qual UTM cada link leva.
2. **Quatro listas, não cinco.** Lista por área, não por curso: L-A1 (657), L-A2 (289), L-A11 (68615 e 333, o mesmo segmento) e L-A14E (341, só o contato com interesse em equinos). Sem a marca de equinos a L-A14E fica vazia e nada de 341 sai pelo CRM (falha fechada).
3. **A conta de calendário fecha.** As 34 datas passam nos quatro testes: nenhum dia com dois toques da onda 2; nenhuma data de newsletter (03/12, 07/01, 14/01, 28/01, 18/02) nem da onda 1 (15/12, 16/12, 06/01, 12/01); nenhum dia sem campanha; todo WhatsApp em dia útil. A única coincidência é 17/12 (edição 3 da newsletter e W1 de 333), que a fila D2 resolve sem exceção codificada.
4. **Desempate pelo GUT, que a F7 deixou comigo:** 341 (80) vence 289 (48) e 68615 (48); entre 289 e 68615 o empate de nota se resolve pela data limite mais próxima (289, 15/05, contra 22/05). Resultado em 08 a 14/03: só o contato que está ao mesmo tempo em A2, A14 e A11 perde um toque, o WhatsApp de acréscimo de 68615 (11/03). **A F7 deixou passar um segundo caso do mesmo empate:** em 11 a 17/01, o contato em A1, A11 e A14 (sem área da onda 1) tem 3 WhatsApp (11, 13 e 15/01); pela mesma regra cai o W2 de 68615 (13/01). Seção 7.4.
5. **Quatro achados que não estavam na F7 nem no plano (seção 8):** (a) se a régua de Livres de 68618 voltar (decisão 14), o contato de A2 que está nela perde E1 e W1 de 289 pela fila D2; (b) a NP2 de equinos precisa do mesmo portão da OU10 que o kit de 341, senão a nutrição apresenta a turma que a regra 10 do plano proíbe; (c) a janela entre 02/12 e 06/12, que a campanhas-de-nutricao-pos dava como "P5 assume" para A2 e A11, ficou sem dono porque o kit só começa em 07/12 e 08/12; (d) a newsletter pode ter versão de WhatsApp no dia seguinte a cada edição, e quatro desses dias (18/12, 08/01, 15/01 e 29/01) caem em toque do kit: o kit vence.
6. **Saída da NP2:** a flag [regua_com_data_ativa_área] liga às 00h05 do dia do primeiro toque do kit da área (A11 em 07/12; A2 em 08/12; A14 equinos em 14/12, ou 15/01 na variante; A1 em 05/01). Seção 9.
7. **UTM:** utm_medium=crm, utm_campaign=pos_<código>_<AAAAMM do primeiro envio>, igual em todos os toques da turma, e o toque no utm_content. Seção 10.
8. **Toda automação é pedido de aprovação:** AF1 a AF7 (o que, por que, quanto, efeito esperado, como desfazer) e DEC1 a DEC7 (decisões de política). O fluxo de cada turma está na seção 11, em tabela de gatilho, condição, ação e saída, com o "como desfazer" em cada uma.
9. **Etapas:** 2 chamadas de agente (este arquiteto e o qa-de-marketing) e 7 etapas de humano; o workflow de reuso (seção 14) tem 2 etapas.

---

## 1. SIPOC e documento de fluxo

### 1.1 SIPOC (skill .claude/skills/mapear-fluxo/SKILL.md)

| Fornecedores | Entradas | Processo | Saídas | Clientes |
|---|---|---|---|---|
| copy-de-mensagens (F7) | os 34 toques, datas, horas, templates e utm_content (seção 0.1 e 0.2 do F7) | 1. Definir listas, entrada e saída (arquiteto-de-fluxos) | quatro listas L-A1, L-A2, L-A11 e L-A14E, com filtros de entrada e de saída | Pessoa do marketing (aprova) |
| cmo | plano da onda 2 (regras 1 a 12, seção 7.3), teto D16, E1 a E4, fila D2, notas GUT | 2. Conferir calendário, fila D2 e teto semana a semana (arquiteto-de-fluxos) | conta semanal do pior caso e o desempate GUT | Quem executa no CRM [CONFIRMAR quem] |
| newsletter | calendário de edições (3.1) e regra de fila (3.2) | 3. Conferência do qa-de-marketing (auditorias 10, 07 e conformidade-educacional) | fila D2, limite diário e teto como regras de CRM | Time de captação (vendas de São Paulo e de Goiânia: recebe quem responde) |
| campanhas-de-nutricao | NP1, NP2, NP3, calendário do lote de 30/11 | 4. Aprovação humana dos pedidos AF1 a AF7 e das decisões DEC1 a DEC7 | saída da NP2 por área e UTM do CRM | cmo (lê só contagens somadas) |
| Time de captação e financeiro | opt-in por canal e finalidade, pagamento da 1ª mensalidade, resposta de quem falou com o time [CONFIRMAR campos e ferramenta, P15] | 5. Montar em rascunho e testar no CRM, sem envio ao público (humano) | registro de supressões por motivo, só em contagem | analise-de-campanha e analise-de-midia (relatórios somados) |
| Ufape (regulação, secretaria, coordenação) | respostas a U10, OU3, OU10, OU11, OU17, U11a, P15 [CONFIRMAR] | 6. Conferir páginas, links e UTM em 04/12 (humano; gestor-de-midia confere) | pedidos de aprovação com plano de desfazer | Candidato com opt-in (recebe mensagem com saída fácil) |
| gestor-de-midia | conferência das páginas no ar em 04/12 (plano, seção 7.2) | 7. Liberar o primeiro envio (07/12) e ler toda segunda (humano e cmo) | painel somado dos indicadores de 13.4 | |

Toda entrada tem fornecedor e toda saída tem cliente. Todo responsável tem uma etapa (seção 1.2) e toda etapa tem um responsável.

### 1.2 Documento de fluxo (templates/documento-de-fluxo.md)

DOCUMENTO DE FLUXO

**Nome do fluxo:** Listas, fila D2, saídas, NP2 e UTM do CRM para o kit de março de 2027 da Pós (657, 341, 289, 68615 e 333)

**Linha de negócio:** Pós-graduação

**Gatilho:** aprovação do OB2 do plano da onda 2 (pedido à pessoa do marketing em 30/11/2026) e conferência das páginas publicadas em 04/12/2026. Primeiro envio previsto: 07/12/2026, 9h. Reuso: nova turma ou nova onda que entre na mesma base (workflow da seção 14).

**Etapas (responsável / entrada / saída):**
1. arquiteto-de-fluxos / F7, plano da onda 2, cmo-geral (12 e 13), newsletter-geral, campanhas-de-nutricao-pos / este arquivo.
2. qa-de-marketing / este arquivo / revisão (F13, "onda2c", prevista para 26/11).
3. pessoa do marketing / revisão do qa e pedidos AF1 a AF7 e DEC1 a DEC7 / aprovação ou devolução (prevista para 30/11).
4. quem executa no CRM [CONFIRMAR quem] / aprovação / listas em rascunho e toques em modo de teste, sem envio ao público (até 03/12).
5. time de captação com a pessoa do marketing / listas e regras montadas / teste com contatos internos de teste (lista, SAIR, "pagou sai", fila e UTM). Envio de teste só para endereços e números internos do time, feito por humano.
6. humano; gestor-de-midia confere / páginas publicadas pela Ufape (OB1) / conferência em 04/12 de destino, UTM e política de privacidade no formulário.
7. humano no CRM, com o cmo na revisão de segunda-feira / liberação toque a toque / envios e leitura somada.

**Etapas de agente:** arquiteto-de-fluxos (etapa 1) e qa-de-marketing (etapa 2). Duas chamadas ao Claude.

**Etapas de aprovação humana:** depois de cada uma das duas etapas de agente (a plataforma pede); depois, uma aprovação por toque no OB2, a conferência de 04/12 e a liberação do primeiro envio. Aprova: a pessoa do marketing que aprovou o plano geral, até a tabela de aprovação de contexto/ufape-geral.md ser preenchida (A9) [CONFIRMAR].

**Checagens de QA e conformidade (qa-de-marketing e auditorias/conformidade-educacional.md):** auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md (seção 15). Itens que dependem do documento: opt-in por canal e saída fácil; "réguas têm regras de saída"; "WhatsApp só em horário comercial, com frequência humana e template aprovado quando usar a API"; "nenhum dado pessoal nos arquivos de trabalho".

**Ferramentas usadas (CRM, Chatwoot, n8n, ClickUp, Supabase, GA4, Meta Ads, Google Ads):** CRM e ferramentas de e-mail e de WhatsApp [CONFIRMAR quais, P15 e U11a]; GA4 para ler a UTM [CONFIRMAR]. Nenhuma aplicada pela squad: as regras são texto para quem executa. Sem Supabase nem n8n neste fluxo. Meta Ads e Google Ads: fora (são da mídia).

**Concluído quando:** (1) as quatro listas existem em rascunho no CRM com os filtros das seções 3 e 4; (2) os 34 toques estão agendados em modo de teste nas datas da seção 7.1, sem nenhum dia com dois toques da onda 2; (3) o teste de humano confirma, com contatos internos de teste: no máximo 1 mensagem por dia, no máximo 2 WhatsApp e 2 e-mails por semana, SAIR e descadastro funcionando, "pagou a 1ª mensalidade sai" funcionando e a UTM de cada link igual à da seção 10; (4) a saída da NP2 acontece nas datas da seção 9; (5) o qa-de-marketing aprovou e a pessoa do marketing aprovou AF1 a AF7. O primeiro envio só ocorre depois do OB2 de cada toque e da conferência de 04/12.

**Data de revisão:** 30/11/2026 (revisão de segunda-feira, na aprovação do OB2) [SUPOSIÇÃO], e de novo em 04/01/2027 (revisão de ritmo do plano) e a cada chegada de U10, OU3, OU10, OU11 ou OU17.

---

## 2. As listas por turma e área

Uma lista é um filtro no CRM, não uma planilha de pessoas. Nenhum contato aparece neste arquivo. O tamanho de cada lista é [CONFIRMAR, OB2] e só entra como número somado.

| Lista | Área | Turmas que alimenta | Quem pode estar nela (filtro de entrada, seção 3) | Toques (seção 7.1) | utm_campaign |
|---|---|---|---|---|---|
| L-A1 | A1 Anestesiologia e dor | 657, Pós-graduação em Anestesiologia Avançada, turma II, São Paulo, início 13/03/2027 | S2 e S3 com [área_de_interesse]=A1 | 7 (2 e-mails e 5 WhatsApp), de 05/01 a 20/04 | pos_657_202701 |
| L-A2 | A2 Cardiorrespiratório | 289, Pós-graduação em Cardiologia Veterinária, turma II, Goiânia, início 20/03/2027 | S2 e S3 com [área_de_interesse]=A2 | 7, de 08/12 a 27/04 | pos_289_202612 |
| L-A11 | A11 Laboratório | 68615, Pós-graduação em Patologia Clínica, turma VII, São Paulo, início 20/03/2027, e 333, Pós-graduação em Citopatologia Veterinária, turma I, São Paulo, início 27/03/2027 (mesmo segmento, duas marcas de turma na lista) | S2 e S3 com [área_de_interesse]=A11 | 68615: 7, de 07/12 a 05/05. 333: 6, de 09/12 a 16/03 (mais 1 reservado, só com OU3) | pos_68615_202612 e pos_333_202612 |
| L-A14E | A14 Outras (só equinos) | 341, Pós-graduação em Medicina Interna Equina, turma I, São Paulo, início 20/03/2027 | S2 e S3 com [área_de_interesse]=A14 **e** [curso_de_interesse]=equinos ou 341 (campo novo, seção 12) | 7, de 14/12 a 14/04 (variante de janeiro: E1 15/01, W1 18/01, W2 26/01) | pos_341_202612 (variante pos_341_202701) |

Total: 4 × 7 + 6 = 34 toques programados com texto (10 e-mails e 24 WhatsApp; confere com o F7, seção 0.1) e 1 toque de 333 reservado, sem texto e sem agendamento.

Pontos de desenho:

1. **Área, não curso, em A1, A2 e A11.** O plano mede e escreve por área; em cada uma dessas áreas o kit mínimo cobre o segmento inteiro. Em A11 o mesmo contato recebe os dois kits (68615 e 333), como a seção 7.2 do F7 já contou.
2. **A14 é por curso.** A14 junta áreas com 1 a 2 itens (plano geral, seção 2.3, nota); mensagem e palavra-chave rodam por curso. Sem a marca de equinos a lista de 341 fica vazia: é a falha fechada do CLAUDE.md do admin (campo ausente recusa, nunca libera). Se o CRM não tiver o campo, o humano cria a marca com leads que chegaram pela página ou pela campanha de 341 [CONFIRMAR como separar].
3. **Praça.** Contato de 289 de qualquer praça pode estar em L-A2; o texto já diz que o campus é Goiânia. Quem responde vai para o atendimento de vendas de Goiânia [SUPOSIÇÃO: não filtrar por praça; o plano não pede filtro].
4. **Marca de turma na lista.** Cada contato guarda, por turma, o último toque recebido e o motivo de saída (seção 12). É o que permite que "quem pagou 68615 saia de 333" e que a NP2 saia no primeiro toque.

---

## 3. Regra de entrada

Um contato só entra em uma lista, e só recebe um toque, se **todas** as condições abaixo forem verdadeiras no dia do envio. Sem registro, não entra.

| # | Regra | Detalhe | Fonte |
|---|---|---|---|
| EN1 | Opt-in por canal | [opt_in_email]=sim para e-mail e [opt_in_whatsapp]=sim para WhatsApp, cada um com data, origem e finalidade aceita. Opt-in de um canal não vale para o outro. | E4 (cmo-geral, 13.3); estrategia-de-relacionamento-pos, 3.2 |
| EN2 | Opt-in de campanha, não de serviço | O opt-in de serviço (dado na compra) não habilita campanha. | E4 |
| EN3 | Finalidade cobre o kit | A finalidade aceita precisa cobrir "cursos de Pós-graduação da Faculdade UFAPE". Opt-in dado a um item só (por exemplo, uma inscrição em prova) não cobre. | campanhas-de-nutricao-pos, 1.3 |
| EN4 | Segmento | S2 (lead de Pós com área) ou S3 (falou com o time e não pagou) da área da lista, conforme a regra 11 do plano. | estrategia-de-relacionamento-pos, seção 4 |
| EN5 | S3 só sem conversa ativa | Contato S3 com [time_assumiu]=sim, ou que respondeu ao time nas últimas 48 h ([respondeu_em]), não recebe toque automático: a retomada é do time (P4). | F7, seção 0.3; DEC5 |
| EN6 | Fora do kit | S1 (sem área), S4 e S5 (provas, se houver inscritos), S6 (matriculado), S7, S8 (ex-aluno, que segue o P7), S9 (comprador de Livres, que só entra pelo par da tabela D6 do plano geral e depois da janela de silêncio), S10, S11 e S12. | estrategia-de-relacionamento-pos, seção 4; cmo-geral, 12.4 |
| EN7 | Janela de silêncio (D8) | Se hoje for menor ou igual a [fim_janela_silencio], o toque não sai. Régua em curso não é interrompida: vale o contato que já recebeu ao menos 1 toque do kit da turma antes da compra. | cmo-geral, 12.5 |
| EN8 | Entrada tardia | Quem entra na lista depois do primeiro toque recebe só os toques seguintes, sem recuperar os que passaram. O lead novo continua a NP1 (T1, T2 e T3) e passa a elegível ao kit; no dia em que um toque do kit e um da NP1 coincidirem, o kit vence (fila D2). | F7 (toques com data fixa); campanhas-de-nutricao-pos, 1.2 |
| EN9 | Estado da turma no dia | Ver CC4 (seção 5). | contexto/pos-graduacao.md (exceção da decisão 18) |
| EN10 | Página no ar | Ver CC12. | regra 13 do plano |

A lista é gerada às 06h do dia do envio e reconferida 30 minutos antes (às 08h30 para o e-mail de 9h e às 09h30 para o WhatsApp de 10h) [SUPOSIÇÃO: depende de a ferramenta permitir; senão, uma só geração às 06h e SAIR processado até o disparo].

---

## 4. Regras de saída

O CRM grava o **motivo** de cada saída (campo [kit_saiu_motivo_<código>]); a squad só lê contagem por motivo.

| # | Quem ou o que sai | Regra | Quando age | Fonte |
|---|---|---|---|---|
| SA1 | Quem pagou a 1ª mensalidade da turma | Sai de todos os toques daquela turma, no dia do envio (a lista é reconferida antes do disparo). **Inscrição paga sem 1ª mensalidade não tira** o contato (DEC3), porque o objetivo do toque é concluir a matrícula. | a cada geração de lista | regra 11 do plano; decisão 16 (matrícula de fato = 1ª mensalidade) |
| SA2 | Quem pagou em turma gêmea | Quem paga 68615 sai também de 333, e quem paga 333 sai também de 68615: são alternativas do mesmo segmento e a própria mensagem diz que a escolha depende do trabalho do contato (DEC2). 657, 341 e 289 são independentes. | idem | F7, E2 de 68615 e 333 [SUPOSIÇÃO] |
| SA3 | Turma depois da data limite | A turma sai de toda lista no fim da véspera do 3º módulo (fonte: plano, seção 7.4, "Encerramento"): **341 em 30/04 às 23h59; 289 em 14/05; 657 e 68615 em 21/05**. Se OU6 disser que vale o 1º dia do 3º módulo, a saída passa para 23h59 do 1º dia. Nenhum toque agendado cai depois dessas datas (o último é o pós-início), então o efeito é fechar a lista para qualquer envio manual. | job diário às 00h05 com [data_limite_turma] | decisão 18; plano 7.4; OU6 |
| SA4 | 333 depois de 26/03 sem OU3 | A turma sai de toda lista às **23h59 de 26/03/2027** (sexta-feira da Paixão, véspera do módulo 1 presencial). Com OU3 respondida, a reabertura é novo pedido, com texto novo passando pelo qa (DEC6); sem resposta, a lista não reabre e o toque de 12/05 nunca existe. | job diário | regra 8 do plano |
| SA5 | Descadastro e SAIR | SAIR no WhatsApp ou descadastro no e-mail tira o contato de **toda campanha de todas as linhas**, no mesmo dia na prática e no máximo em **48 h** (E3). Serviço continua [SUPOSIÇÃO já registrada na estrategia-de-relacionamento-pos, 3.1]. O botão "Sair" do template e a palavra SAIR no texto livre valem igual. Resposta com a palavra "parar" ou parecida vai ao humano para registro, no mesmo dia. | tempo real; reconferência antes do envio | E3; estrategia-de-relacionamento-pos, 3.2 |
| SA6 | Quem respondeu (inclui "TURMA") | Sai dos toques automáticos da turma respondida e a conversa passa ao time (vendas de São Paulo; Goiânia no caso de 289). Em A11, a resposta a um toque de 68615 ou de 333 tira o contato dos dois (mesma conversa, mesmo segmento) [SUPOSIÇÃO]. O time decide se devolve à régua (campo [time_assumiu]). | [respondeu_em] | F7, seção 0.3 |
| SA7 | E-mail com devolução permanente ou reclamação de spam | Sai de e-mail de campanha. | tempo real | newsletter-geral, 2.1 |
| SA8 | Turma que deixa de poder receber chamada | Status do catálogo diferente de "aberto" e de "verificar por já ter começado" (CC4), turma cancelada ou adiada: o kit da turma para, e o caso vira serviço da secretaria (S12). | status do dia | conformidade-educacional; decisão 18 |
| SA9 | Contato sem engajamento no WhatsApp (E1) | Sem resposta, clique ou conversa nas últimas 4 mensagens de campanha por WhatsApp: no máximo 1 WhatsApp de campanha por semana. Sem interação em 90 dias: sai do WhatsApp de campanha e fica só no e-mail. | contador [wa_campanha_sem_interacao] | E1 (cmo-geral, 13.3) |
| SA10 | Erro 131049 da Meta | Toque barrado não é reenviado antes de 24 h e não muda de dia: conta como suprimido (E2). Só vale se a Ufape usar a API oficial (U11a). | no envio | E2 |

Saída da automação nunca apaga o contato do CRM nem o histórico: só muda o estado do contato na lista.

---

## 5. Condições comuns de envio (CC1 a CC12)

Toda linha das tabelas da seção 11 diz "CC1 a CC12 e" mais a condição específica. O CRM confere nesta ordem; a primeira que falhar suprime o toque para aquele contato e registra o motivo (somado).

| # | Condição | Falha vira |
|---|---|---|
| CC1 | Opt-in do canal, de campanha e com finalidade (EN1 a EN3) | não entra |
| CC2 | Contato na lista da turma e área, no segmento S2 ou S3 (EN4 a EN6) | não entra |
| CC3 | Nenhum motivo de saída (seção 4) | sai |
| CC4 | Estado da turma permitido hoje: "aberto" no catálogo, ou "verificar" só porque a turma já começou (exceção da decisão 18, em vigor até a véspera do 3º módulo). Qualquer outro estado para o kit da turma. | suprimido; aviso ao cmo |
| CC5 | Dia e horário permitidos: sem campanha em 21/12 a 03/01, 25/12, 31/12, 01/01, 25/01, 08 a 10/02 e 26/03 (as seis últimas datas já estão nas regras 11 do plano). WhatsApp em dia útil das 9h às 18h; e-mail das 7h às 19h. Toque que o CRM não conseguir enviar dentro da janela é suprimido, não vai para o dia seguinte. | suprimido |
| CC6 | Janela de silêncio (EN7) | suprimido |
| CC7 | Limite diário: no máximo 1 mensagem de campanha por contato por dia, em qualquer canal. Serviço não conta. Conversa 1 a 1 do time de vendas não conta. | suprimido |
| CC8 | Teto semanal (segunda a domingo), somando todas as linhas e a newsletter: até 2 WhatsApp e 2 e-mails de campanha; 1 WhatsApp se houver SA9; **contato também na base da Graduação: até 3 por semana somando os canais**, 1 por dia (D16). | suprimido |
| CC9 | Sobreviver à fila D2 (seção 6) quando mais de um toque disputa o dia ou a semana | suprimido; não acumula |
| CC10 | Sem erro 131049 no envio (SA10) | suprimido |
| CC11 | Portões de aprovação do toque: OB2 aprovado para este toque, qa próprio feito e teste de humano da lista, do link e da UTM; portão da turma (OU10 em 341; OU3 em 333) | o toque não é agendado |
| CC12 | Página da turma publicada e conferida em 04/12 (OB1). Nenhum envio sai para página com frase ligada ao MEC antes da troca, salvo decisão humana registrada no OB1 [CONFIRMAR com a regulação]. Toque sem link (pós-início) não depende de CC12, mas depende de a página ter sido corrigida antes, porque a mensagem confirma o que está nela. | o toque não é agendado |

---

## 6. Fila D2, limite de 1 por dia, teto e dias sem campanha

### 6.1 Como o CRM decide (por contato)

1. **Segunda-feira, 06h:** o CRM monta, para cada contato, a lista de toques candidatos da semana inteira (kit, newsletter, régua da onda 1, régua de Livres e NP, o que existir) e aplica CC1 a CC8. Só então ordena o que sobrou pela fila.
2. **Ordem da fila (D2):** (1) serviço de qualquer linha, fora do teto; (2) toque principal de cada campanha com data, onde está o toque do kit; (3) entre toques principais que disputam o mesmo canal na mesma semana, vence o de [data_do_item] mais próxima; empate, vence a maior nota GUT (seção 7.4); (4) follow-ups e reenvios; (5) nutrição (newsletter, NP1, NP2, NP3, rotação dos contínuos); (6) reativação.
3. **[data_do_item]:** data de início da turma se ela ainda não começou; data limite (3º módulo) se já começou [SUPOSIÇÃO: o D2 diz "data mais próxima" e não define o caso da turma iniciada, que existe na onda 1].
4. **Dia:** para cada dia, o toque de maior prioridade fica; os demais daquele dia são suprimidos (limite de 1 por dia, em qualquer canal).
5. **Semana:** dentro de cada canal, ficam os 2 toques de maior prioridade (1 no caso de SA9); os demais são suprimidos.
6. **O suprimido não acumula e não muda de dia** (D2). Se o concorrente sair da lista depois (por exemplo, pagou), o toque suprimido **não volta**.
7. **Nada soma depois do envio:** a checagem diária só remove, nunca acrescenta toque à semana já calculada.
8. **Contagem de supressões** por motivo e por toque, só somada, para o relatório do cmo (seção 12, campo de registro).

### 6.2 O que muda em relação à F7

- **A exceção C5 deixa de ser regra codificada.** O W1 de 333 em 17/12 e a edição 3 da newsletter no mesmo dia se resolvem sozinhos: o limite de 1 por dia mais a prioridade 2 do kit contra a prioridade 5 da newsletter. Se o W1 de 333 for suprimido para aquele contato por outro motivo, o dia fica livre e a newsletter vai. Isso é melhor que "a edição 3 não vai a quem recebe o W1", que deixaria o contato sem os dois.
- **Reenvio para quem não abriu (F7, 1.1 e seguintes) fica de fora desta onda** (DEC4): abertura é estimativa, o W seguinte já faz o papel de follow-up, e cada reenvio é um toque a mais na fila.

---

## 7. Conferência do calendário

### 7.1 Os 34 toques, com dia da semana (e-mail às 9h, WhatsApp às 10h)

| Data | Dia | Toque | Canal | Data | Dia | Toque | Canal |
|---|---|---|---|---|---|---|---|
| 07/12/2026 | seg | E1 68615 | e-mail | 23/02/2027 | ter | W3 333 | WhatsApp |
| 08/12 | ter | E1 289 | e-mail | 02/03 | ter | AC 657 | WhatsApp |
| 09/12 | qua | E1 333 | e-mail | 09/03 | ter | AC 289 | WhatsApp |
| 10/12 | qui | W1 68615 | WhatsApp | 10/03 | qua | AC 341 | WhatsApp |
| 11/12 | sex | W1 289 | WhatsApp | 11/03 | qui | AC 68615 | WhatsApp |
| 14/12 | seg | E1 341 | e-mail | 16/03 | ter | W4 333 | WhatsApp |
| 17/12 | qui | W1 333 | WhatsApp | 14/04 | qua | PI 341 | WhatsApp |
| 18/12 | sex | W1 341 | WhatsApp | 20/04 | ter | PI 657 | WhatsApp |
| 05/01/2027 | ter | E1 657 | e-mail | 27/04 | ter | PI 289 | WhatsApp |
| 08/01 | sex | W2 289 | WhatsApp | 05/05 | qua | PI 68615 | WhatsApp |
| 11/01 | seg | W1 657 | WhatsApp | (12/05 | qua | PI 333, só com OU3, sem texto | WhatsApp) |
| 13/01 | qua | W2 68615 | WhatsApp | 15/01 | sex | W2 341 (padrão) | WhatsApp |
| 19/01 | ter | W2 333 | WhatsApp | 21/01 | qui | W2 657 | WhatsApp |
| 27/01 | qua | E2 289 | e-mail | 29/01 | sex | E2 68615 | e-mail |
| 01/02 | seg | E2 657 | e-mail | 02/02 | ter | E2 341 | e-mail |
| 03/02 | qua | E2 333 | e-mail | 04/02 | qui | W3 657 | WhatsApp |
| 11/02 | qui | W3 289 | WhatsApp | 12/02 | sex | W3 341 | WhatsApp |
| 16/02 | ter | W3 68615 | WhatsApp | | | | |

AC é o WhatsApp da semana anterior ao início (em 333 o equivalente é o W4); PI é o pós-início, com a regra completa da decisão 18. Variante de 341 (OU10 resolvida só depois de 11/12): E1 em 15/01, W1 em 18/01 e W2 em 26/01; o resto não muda. Dias da semana conferidos contra 01/01/2027 (sexta-feira), 28/03/2027 (domingo de Páscoa) e 26/03/2027 (sexta-feira da Paixão).

### 7.2 Os quatro testes por data

| Teste | Regra | Resultado |
|---|---|---|
| T1. Dia único | nenhum dia tem dois toques da onda 2 | passa nas 34 datas e na variante de 341 (15/01, 18/01 e 26/01 também livres) |
| T2. Newsletter | nenhum toque em 03/12, 07/01, 14/01, 28/01 e 18/02 | passa; a única coincidência é 17/12 (W1 de 333 com a edição 3), tratada em 6.2 |
| T3. Onda 1 | nenhum toque em 15/12, 16/12, 06/01 e 12/01 (WhatsApp da onda 1, plano de 26/10, seção 6) | passa nas 34 datas |
| T4. Dias sem campanha e janela | nenhum toque em 21/12 a 03/01, 25/12, 31/12, 01/01, 25/01, 08 a 10/02, 26/03; todo WhatsApp em dia útil e fora de feriado nacional | passa; nenhum feriado nacional cai nas 34 datas (21/04 e 01/05 ficam sem toque; 20/04 é terça-feira) |

### 7.3 Conferência com o calendário da newsletter-geral (seção 3.1)

| Edição | Data e hora | Convive com o kit? | Tratamento |
|---|---|---|---|
| 2 | qui 03/12, 10h | sim, nenhum toque do kit antes de 07/12 | nenhum |
| 3 | qui 17/12, 10h | **choca com o W1 de 333 (A11)** | o kit vence pela fila; sem exceção codificada (6.2) |
| 4 | qui 07/01, 10h | semana de 04 a 10/01: e-mail do kit em 05/01 (657) mais a newsletter = 2 e-mails | cabe |
| 5 | qui 14/01, 10h | semana de 11 a 17/01: newsletter mais, só na variante de 341, o E1 de 15/01 = 2 e-mails | cabe |
| 6 | qui 28/01, 10h | semana de 25 a 31/01: E2 de 289 (27/01), newsletter (28/01) e E2 de 68615 (29/01) = 3 | a newsletter cai para quem está em A2 e A11 (prioridade 5) |
| 7 | qui 18/02, 10h | semana de 15 a 21/02: newsletter e W3 de 68615 em 16/02 | cabe |
| depois de 18/02 | **a newsletter-geral não traz datas** | [CONFIRMAR] | Se a cadência quinzenal em quintas continuar (04/03, 18/03, 01/04, 15/04, 29/04 e 13/05) [SUPOSIÇÃO], nenhuma cai em dia de toque do kit e cada semana fica em 1 e-mail da newsletter mais, no máximo, 1 WhatsApp |

**Versão de WhatsApp da newsletter.** A newsletter-geral só escreveu as edições 1 e 2, ambas com WhatsApp no dia seguinte (19/11 e 04/12). Se as edições 3 a 7 repetirem o desenho (18/12, 08/01, 15/01, 29/01 e 19/02), quatro caem em toque do kit: 18/12 (W1 de 341), 08/01 (W2 de 289), 15/01 (W2 de 341) e 29/01 (E2 de 68615). O kit vence nos quatro, a newsletter por WhatsApp não muda de dia (D2) e o contato daquela área fica sem ela. Pedido de nota para o agente newsletter, sem alterar o arquivo dele (seção 8).

### 7.4 Pior caso semana a semana e o desempate pelo GUT

Pior caso = contato que está, ao mesmo tempo, em todas as áreas que disputam a semana, com opt-in nos dois canais e sem restrição de engajamento. As semanas que não aparecem aqui já cabem em 2 e 2 mesmo no pior caso (conferido contra a seção 7.2 do F7).

| Semana | Candidatos no pior caso | Ficam | Caem | Quem é afetado |
|---|---|---|---|---|
| 07 a 13/12 | e-mails: 07 (68615), 08 (289), 09 (333); WhatsApp: 10 (68615), 11 (289) | E 07, E 08, W 10, W 11 | E1 de 333 (início mais distante, 27/03) | contato em A11 e A2 |
| 14 a 20/12 | WhatsApp: 15 (A9 e A5, onda 1), 16 (A6, onda 1), 17 (333), 18 (341); e-mail: 14 (341), newsletter 17 | os dois WhatsApp da onda 1 (data limite mais próxima: 707 em 18/12, 68604 e 68606 em 23/01); todos os e-mails | W1 de 333 e W1 de 341. Se o contato tem só uma área da onda 1, ficam ela e o W1 de 341 (20/03) e cai o de 333 (27/03) | A11 e A14 com área da onda 1 |
| 11 a 17/01 (a) | WhatsApp: 11 (657), 12 (onda 1), 13 (68615), 15 (341) | W 11 e W 12 | W2 de 68615 e W2 de 341 | A1, A11 e A14 com área da onda 1 |
| 11 a 17/01 (b) **novo** | WhatsApp: 11 (657), 13 (68615), 15 (341), sem área da onda 1 | W 11 e W 15 | **W2 de 68615 (13/01)**, pelo desempate GUT | A1, A11 e A14 |
| 18 a 24/01 (variante de 341) | WhatsApp: 18 (341), 19 (333), 21 (657) | W 18 e W 21 | W2 de 333 (início mais distante) | A14, A11 e A1 |
| 25 a 31/01 | e-mails: 27 (289), 28 (newsletter), 29 (68615) | E 27 e E 29 | newsletter de 28/01 | A2 e A11 |
| 01 a 07/02 | e-mails: 01 (657), 02 (341), 03 (333) | E 01 e E 02 | E2 de 333 | A1, A14 e A11 |
| 08 a 14/03 | WhatsApp: 09 (289), 10 (341), 11 (68615), os três com início em 20/03 | W 09 e W 10 | **AC de 68615 (11/03)**, pelo desempate GUT | A2, A14 e A11 |

Observação sobre 11 a 17/01 (b): a F7 só contou essa semana com um quarto toque (o da onda 1). Sem área da onda 1 o pior caso já tem 3 WhatsApp e cai no mesmo empate de 68615 com 341 (início em 20/03 nos dois).

**Desempate (skill .claude/skills/matriz-gut/SKILL.md).** O plano geral, seção 3, dá a mesma nota de grupo às cinco turmas (5, 3, 3, total 45), o que não desempata. Notas por turma, avaliação do agente, não medida, só para a fila:

| Turma | G | U | T | Total | Motivo das notas (dado e fonte) |
|---|---|---|---|---|---|
| 341 | 5 | 4 | 4 | **80** | G: meta em reais de R$ 652.500,00, a maior das três (plano, seção 1). U: início em 20/03, mesma data das outras duas, e a janela de matrícula depois do início é a mais curta (3º módulo em 01/05, 42 dias depois). T: turma I, sem histórico; o plano a trata como a de menor encaixe de canais [SUPOSIÇÃO do plano], então perder um toque da base pesa mais |
| 289 | 4 | 4 | 3 | **48** | G: meta de R$ 531.000,00 (plano, seção 1). U: início em 20/03; 3º módulo em 15/05, 56 dias depois. T: tem campanha ativa, o que dá leitura de custo, e é turma II |
| 68615 | 4 | 4 | 3 | **48** | G: meta de R$ 531.000,00 (plano, seção 1). U: início em 20/03; 3º módulo em 22/05, 63 dias depois. T: turma VII, a mais antiga das cinco; o contato de A11 ainda recebe o W4 de 333 na semana seguinte |
| 657 e 333 | | | | 45 | nota do grupo (plano geral, seção 3); nunca empatam por data com outra turma de março nas semanas conferidas |

**Regra de desempate para a fila (DEC1):** na ordem 341, 289, 68615. Entre 289 e 68615 as notas empatam (48); desempata a data limite mais próxima, como pede a skill (primeiro urgência, depois esforço) e como o próprio D2 faz com a "data mais próxima": 289 (15/05) vence 68615 (22/05). **Sem OU10 (341 fora), a ordem é 289, 68615.** A mesma ordem vale em 11 a 17/01 e em 08 a 14/03, porque a posição relativa não muda de uma semana para a outra. Efeito prático: só o contato nas três áreas perde um WhatsApp em cada uma das duas semanas, sempre o de 68615; o kit mínimo da turma segue cumprido (o mínimo é por turma, não por contato; F7, 7.3). A semana de 08 a 14/03 e a de abril ainda não conhecem os toques da onda 3 (A1 com 68609 e 359; A2 com 68636 e 352): quem estiver nas duas ondas passa pela mesma fila, e a conferência dessas semanas é do arquiteto na onda 3 [CONFIRMAR].

---

## 8. Conflitos achados e como tratar

| # | Conflito | Onde aparece | Tratamento proposto | Quem decide |
|---|---|---|---|---|
| CF1 | **Régua de Livres de 68618 contra 289.** A campanhas-de-nutricao-pos, seção 4, lista 68618 com WhatsApp em 07/12, e-mail em 08/12, WhatsApp em 10/12 e WhatsApp em 15/12, só para A1 e A2 de ventilação e só "com P6 fechada". Se voltar (decisão 14), o contato de A2 nessa régua teria 2 WhatsApp (07 e 10/12) e 1 e-mail (08/12) na semana de 07 a 13/12; o E1 (08/12, mesmo dia) e o W1 (11/12, semana cheia) de 289 caem, porque 68618 (18/12) tem data mais próxima que 289 (20/03). | 07 a 13/12, A2 | Padrão: aceitar a fila (o kit mínimo vale por turma, e o contato recebe E2, W2, W3, AC e PI). Alternativa: o cmo pede à copy de Livres para 68618 não usar 08/12 e 11/12 em A2. Nenhuma exceção manual. | cmo (DEC1 inclui esta decisão se o 68618 voltar) |
| CF2 | **NP2 de equinos apresenta a turma 341.** T1 (cronograma), T2 (quem ensina) e T3 (condições) da NP2 falam da turma de A14 sobre a qual a regra 10 do plano diz "só com a página corrigida ou a promoção retirada (OU10)". | NP2 de A14, 01/12 a 16/12 | DEC7: o contato com [curso_de_interesse]=equinos só recebe NP2 depois de OU10 resolvida; antes disso fica só com a newsletter. Outros A14 (679, 382, 699, 60) seguem a NP2 normal. | cmo |
| CF3 | **Janela de 02/12 a 06/12 para A2 e A11.** A campanhas-de-nutricao-pos supõe que o P5 de A2 e A11 assume em 02/12 e por isso não roda NP2 nessas áreas. O plano da onda 2 deixa nenhum toque de P5 em 02/12 e começa em 07/12 (68615) e 08/12 (289). Resultado: 5 dias sem NP2 e sem kit. | 02 a 06/12 | Aceitar: nenhum toque nesses dias (é menos mensagem, não mais). Nota ao agente campanhas-de-nutricao: o "assume em 02/12" de A2 e A11 passa a 07/12 e 08/12. | cmo |
| CF4 | **Versão de WhatsApp da newsletter nos dias de kit** (18/12, 08/01, 15/01 e 29/01), se existir. | 7.3 | O kit vence; a newsletter não muda de dia por contato. Nota ao agente newsletter para escolher, se quiser, dia livre para a versão de WhatsApp das edições 3 a 7. | newsletter |
| CF5 | **S3 está em dois donos.** A estrategia-de-relacionamento-pos põe S3 (falou com o time e não pagou) na retomada do time (P4), e o plano põe S3 no kit. | todas as listas | EN5 e DEC5: S3 recebe o kit, exceto o contato com [time_assumiu]=sim ou resposta ao time nas últimas 48 h. | pessoa do marketing |
| CF6 | **Contato que também está na base da Graduação** tem teto de 3 por semana somando os canais (D16). O calendário da Graduação não estava nas entradas. | qualquer semana | CC8 aplica o teto menor e a fila resolve. Conferência semana a semana fica [CONFIRMAR] com o plano da Graduação. | arquiteto-de-fluxos, na onda 3 |
| CF7 | **Template da Meta com URL fixa e UTM com mês.** Se um toque escorregar de mês (por exemplo, páginas atrasadas em 04/12), o template já aprovado leva o mês antigo. | 7.2 do plano | DEC6: manter o mês planejado e registrar o desvio na tabela de correspondência (seção 10), para não reenviar o template à aprovação da Meta. | pessoa do marketing |
| CF8 | **Páginas atrasadas.** O plano diz: se a página da turma não estiver no ar em 04/12, a subida e os toques de dezembro dela "passam para janeiro, sem acumular". O plano não dá as datas. | 07 a 18/12 | O toque da turma atrasada não é agendado em dezembro e nenhum toque é antecipado nem empilhado. O arquiteto entrega as datas de janeiro em nova versão, com a conta de 7.4, no mesmo dia em que o atraso for confirmado. Este arquivo não reserva datas de janeiro. | cmo |

---

## 9. Saída da NP2 da área no primeiro toque do kit

A NP2 (campanhas-de-nutricao-pos, seção 3) é nutrição, prioridade 5 da fila. O dono único do convite é o kit: no dia do primeiro toque do kit da área, às **00h05**, o CRM liga a flag [regua_com_data_ativa_área]=sim para todo contato da área e cancela os toques de NP2 pendentes dele. A saída vale **mesmo que o primeiro toque do kit seja suprimido para aquele contato** (fila ou teto), para a nutrição nunca repetir o convite.

| Área | Quem pode estar em NP2 | Primeiro toque do kit | Saída da NP2 | NP2 que ainda acontece antes | Observação |
|---|---|---|---|---|---|
| A11 (68615 e 333) | só leads que chegam depois do início do kit; o lote de 30/11 não roda para A11 | E1 de 68615, seg 07/12, 9h | seg 07/12, 00h05, para as duas turmas | nenhuma do lote | CF3: 02 a 06/12 sem toque |
| A2 (289) | idem | E1 de 289, ter 08/12, 9h | ter 08/12, 00h05 | nenhuma do lote | CF3 |
| A14 equinos (341) | lote de 30/11, **só depois de OU10 resolvida** (CF2) | E1 de 341, seg 14/12, 9h (variante: sex 15/01) | 14/12, 00h05 (variante: 15/01, 00h05) | T1 (01/12), T2 (09/12) e T3 (16/12) só se OU10 estiver resolvida antes do toque; T3 de 16/12 não chega ao contato que já saiu em 14/12 | fora de equinos, A14 segue a NP2 até o P5 do curso dele |
| A1 (657) | lote de 30/11 | E1 de 657, ter 05/01, 9h | ter 05/01, 00h05 (a campanhas-de-nutricao-pos dizia 04/01; não há toque de NP2 entre as duas datas) | T1 (01/12), T2 (09/12) e T3 (16/12) | o T4 de 05/01 não sai para A1 (já é regra da nutrição) |

Contato em mais de uma área sai da NP2 de cada área no dia do primeiro toque do kit daquela área. A flag é por área, não por contato: quem estiver em A1 e A3, por exemplo, sai da NP2 de A1 em 05/01 e segue na de A3 até o P5 dela.

---

## 10. UTM do CRM (regra 12 do plano; D11 e D12)

- utm_source: **email** nos e-mails, **whatsapp** nos WhatsApp. utm_medium: **crm** (único valor aceito para mensagem enviada pelo CRM).
- utm_campaign: **pos_<código>_<AAAAMM do primeiro envio>**, igual em todos os toques da turma. O toque vai no utm_content.
- Tudo em minúsculas, sem acento, hífen dentro do bloco e sublinhado entre blocos. Um link por mensagem. Nenhum dado pessoal na UTM.

| Turma | utm_campaign | utm_content (um por toque) |
|---|---|---|
| 68615 | pos_68615_202612 | e1-68615, w1-68615, w2-68615, e2-68615, w3-68615, ac-68615, pi-68615 (sem link) |
| 289 | pos_289_202612 | e1-289, w1-289, w2-289, e2-289, w3-289, ac-289, pi-289 (sem link) |
| 333 | pos_333_202612 | e1-333, w1-333, w2-333, e2-333, w3-333, w4-333; pi-333 reservado, sem link |
| 341 | pos_341_202612 (variante de janeiro: pos_341_202701) | e1-341, w1-341, w2-341, e2-341, w3-341, ac-341, pi-341 (sem link) |
| 657 | pos_657_202701 | e1-657, w1-657, w2-657, e2-657, w3-657, ac-657, pi-657 (sem link) |

Exemplo de montagem (a URL da página de cada turma é a da seção 0.2 do F7): `<URL da página da turma>?utm_source=whatsapp&utm_medium=crm&utm_campaign=pos_68615_202612&utm_content=w1-68615`.

Regras de apoio:

1. **Mês do primeiro envio.** Vale o mês do primeiro envio **real** de qualquer toque do CRM com link para a página da turma. Como a NP2 de uma turma usa o mesmo padrão (pos_<código>_<AAAAMM>, utm_content np2-...), a regra evita dois nomes para a mesma turma: em 341 nenhum CRM aponta para a página antes de OU10 (CF2), então o primeiro envio é o do kit.
2. **Se o envio escorregar de mês** depois de o template da Meta estar aprovado: manter o nome planejado e registrar o desvio na tabela de correspondência (DEC6). A leitura usa a data do envio, que o CRM guarda.
3. **Toque pós-início não tem link.** O PI pede "responda TURMA"; mede-se por contagem de respostas, sem UTM. O botão do e-mail que leva a wa.me não é rastreado pela UTM [CONFIRMAR P15].
4. **Pago e orgânico não mudam:** pago segue a chave `pos_<código>-<área curta>_<plataforma>_...` ratificada na seção 6 do plano; orgânico usa utm_medium=organic_social e utm_campaign=pos_<código>_<AAAAMM da primeira publicação da turma>.
5. **Teste de humano antes do primeiro envio:** clicar o link de um contato de teste e conferir no GA4 [CONFIRMAR ferramenta] a origem, o meio, a campanha e o conteúdo.

---

## 11. Fluxo de cada turma

Em todas as linhas valem **CC1 a CC12** (seção 5) e as saídas SA1 a SA10 (seção 4). A coluna "Condição" só traz o que é específico do toque. "Saída padrão" quer dizer: quem pagou, respondeu, saiu ou foi suprimido não recebe; o toque suprimido não acumula. Cada tabela termina com "Como desfazer".

### 11.1 68615, Pós-graduação em Patologia Clínica (A11), lista L-A11, utm_campaign pos_68615_202612

Portão da turma: página publicada e conferida em 04/12 (OB1); OU13 (CEP) é só da página. Se a página atrasar, CF8.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 07/12, 9h | OB2 do E1; página no ar; primeiro toque de A11 | enviar E1 (botão "Ver a turma e as condições", utm_content=e1-68615); ligar a flag de saída da NP2 de A11 às 00h05 | saída padrão; SA2 (pagou 333 também tira) |
| 2 | qui 10/12, 10h | opt-in de WhatsApp; template pos_68615_kit_w1 aprovado na Meta, se API [CONFIRMAR U11a] | enviar W1 (botão URL; utm_content=w1-68615) | saída padrão |
| 3 | qua 13/01, 10h | semana 11 a 17/01: cai pelo GUT no pior caso (b) de 7.4 | enviar W2 (utm_content=w2-68615) | saída padrão |
| 4 | sex 29/01, 9h | semana 25 a 31/01: a newsletter de 28/01 cai para quem também está em A2 | enviar E2 (utm_content=e2-68615) | saída padrão |
| 5 | ter 16/02, 10h | conferido contra newsletter de 18/02 (semana comum) | enviar W3, com a frase de turma mínima sem número | saída padrão |
| 6 | qui 11/03, 10h | semana 08 a 14/03: **cai** para o contato em A2, A14 e A11 ao mesmo tempo (DEC1) | enviar AC ("matrícula aberta até o 3º módulo", sem a data dele) | saída padrão |
| 7 | qua 05/05, 10h | CC4 aceita "verificar por já ter começado"; frase da regra completa com 3º módulo em 22/05/2027 | enviar PI (sem link, "responda TURMA"); resposta vai ao time de São Paulo | resposta tira da automação (SA6); lista fecha às 23h59 de 21/05 (SA3) |

**Como desfazer:** pausar a régua de 68615 no CRM, que cancela os agendamentos pendentes dos toques 2 a 7; limpar a flag da NP2 de A11 (os contatos voltam à NP2 no próximo toque pendente, sem reenvio do que passou); a lista fica arquivada, não apagada. Toque já enviado não volta. SAIR e descadastro nunca são desfeitos.

### 11.2 289, Pós-graduação em Cardiologia Veterinária (A2), lista L-A2, utm_campaign pos_289_202612

Portão da turma: página publicada e conferida em 04/12; PP9 da mídia é de mídia, não do CRM. Nenhum toque cai em 06/01 (dia reservado à 698, se houver OU3). Atendimento: vendas de Goiânia.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | ter 08/12, 9h | OB2 do E1; CF1 se a régua de 68618 existir | enviar E1 (utm_content=e1-289); ligar a flag de saída da NP2 de A2 às 00h05 | saída padrão |
| 2 | sex 11/12, 10h | idem; semana 07 a 13/12 | enviar W1 (utm_content=w1-289) | saída padrão |
| 3 | sex 08/01, 10h | semana 04 a 10/01: cabe com a newsletter de 07/01 e com o W de 06/01 da 698 (só com OU3) | enviar W2 (utm_content=w2-289) | saída padrão |
| 4 | qua 27/01, 9h | semana 25 a 31/01: o E2 fica e a newsletter de 28/01 cai | enviar E2 (utm_content=e2-289) | saída padrão |
| 5 | qui 11/02, 10h | depois do Carnaval e das Cinzas; ficam fora 08 a 10/02 | enviar W3 | saída padrão |
| 6 | ter 09/03, 10h | semana 08 a 14/03: **fica** (vence 68615 por data limite; DEC1) | enviar AC | saída padrão |
| 7 | ter 27/04, 10h | CC4 aceita "verificar por já ter começado"; 3º módulo em 15/05/2027 | enviar PI; resposta vai ao time de Goiânia | SA6; lista fecha às 23h59 de 14/05 (SA3) |

**Como desfazer:** igual a 11.1, com a pausa da régua de 289 e a limpeza da flag de A2.

### 11.3 333, Pós-graduação em Citopatologia Veterinária (A11), lista L-A11, utm_campaign pos_333_202612

Portão da turma: OU3. Sem OU3 nenhuma mensagem depois do início e a turma sai de toda lista às 23h59 de 26/03/2027 (SA4). Sem "coordenação" e sem docente nas mensagens (OU12). OU17 (módulo 1 em 27 e 28/03, sábado de Aleluia e domingo de Páscoa): o W3 e o W4 citam essas datas; se mudarem, ciclo extra.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | qua 09/12, 9h | OB2 do E1; **cai** para o contato em A11 e A2 na semana 07 a 13/12 | enviar E1 (utm_content=e1-333) | saída padrão; SA2 |
| 2 | qui 17/12, 10h | dia da edição 3 da newsletter; kit vence; cai para o contato com 2 WhatsApp da onda 1 na semana | enviar W1 (utm_content=w1-333) | saída padrão |
| 3 | ter 19/01, 10h | semana 18 a 24/01: cai na variante de 341 se o contato também está em A14 e A1 | enviar W2 (utm_content=w2-333) | saída padrão |
| 4 | qua 03/02, 9h | semana 01 a 07/02: **cai** para o contato em A1, A14 e A11 | enviar E2 (utm_content=e2-333) | saída padrão |
| 5 | ter 23/02, 10h | semana comum | enviar W3 (utm_content=w3-333) | saída padrão |
| 6 | ter 16/03, 10h | 4º WhatsApp do kit, **sem** a frase "matrícula aberta até o 3º módulo" enquanto OU3 estiver aberta (desvio 11 do F7) | enviar W4 (utm_content=w4-333) | lista fecha às 23h59 de 26/03 se não houver OU3 (SA4) |
| 7 | qua 12/05, 10h | **só com OU3 respondida**, texto novo aprovado e qa | **não é agendado**; reabertura é novo pedido (DEC6) | sem OU3, nunca existe |

**Como desfazer:** pausar a régua de 333, limpar o marcador de turma 333 em L-A11 (a lista de 68615 não muda) e cancelar o agendamento pendente. Reabertura da lista depois de 26/03 só por pedido novo.

### 11.4 341, Pós-graduação em Medicina Interna Equina (A14, equinos), lista L-A14E, utm_campaign pos_341_202612 (variante pos_341_202701)

Portão da turma: **OU10** (página corrigida ou promoção retirada). Verificação às **18h de 11/12**: resolvida, vale o calendário padrão; aberta, vale a variante (E1 15/01, W1 18/01, W2 26/01); aberta ainda em **08/01**, tudo de 341 fica suspenso e nada acumula (regra 10 do plano) [SUPOSIÇÃO do horário]. OU11 e OU17 (local da prática e módulo 3, marcado "ONLINE PRESENCIAL", em 01 e 02/05/2027, com feriado em 01/05) travam o PI. Sem promoção, sem local da prática e sem "hospital veterinário" em nenhuma mensagem.

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | seg 14/12, 9h (variante: sex 15/01) | OU10 resolvida; marca de equinos | enviar E1 (utm_content=e1-341); ligar a flag de saída da NP2 de equinos às 00h05 | saída padrão |
| 2 | sex 18/12, 10h (variante: seg 18/01) | **cai** pelo pior caso de 14 a 20/12 para quem tem área da onda 1 e A11 | enviar W1 (utm_content=w1-341) | saída padrão |
| 3 | sex 15/01, 10h (variante: ter 26/01) | semana 11 a 17/01: fica pelo GUT no pior caso (b); cai no (a) | enviar W2, com a frase de passagem e hotel só depois da turma confirmada | saída padrão |
| 4 | ter 02/02, 9h | semana 01 a 07/02: fica | enviar E2 | saída padrão |
| 5 | sex 12/02, 10h | depois das Cinzas | enviar W3 | saída padrão |
| 6 | qua 10/03, 10h | semana 08 a 14/03: **fica** (maior nota, DEC1) | enviar AC | saída padrão |
| 7 | qua 14/04, 10h | OU11 e OU17 resolvidas para a data do 3º módulo; CC4 aceita "verificar por já ter começado" | enviar PI (sem link, "responda TURMA") | SA6; lista fecha às 23h59 de 30/04 (SA3) |

**Como desfazer:** pausar a régua de 341 (cancela os agendamentos pendentes), limpar a flag da NP2 de equinos e, se OU10 voltar a abrir, repetir a verificação. Marca [curso_de_interesse] é mantida: ela é filtro, não envio.

### 11.5 657, Pós-graduação em Anestesiologia Avançada (A1), lista L-A1, utm_campaign pos_657_202701

Portão da turma: nenhuma frase de pré-requisito (U10) em nenhuma mensagem, nem "exclusiva", prova ou título de especialista; essas travas são do texto (F7) e do qa, não de CRM. Primeiro toque em 05/01 (NL3: a área de anestesia fica com 68618 até 18/12).

| # | Gatilho | Condição específica | Ação | Saída |
|---|---|---|---|---|
| 1 | ter 05/01, 9h | OB2 do E1; semana 04 a 10/01 com a newsletter de 07/01 | enviar E1 (utm_content=e1-657); ligar a flag de saída da NP2 de A1 às 00h05 | saída padrão |
| 2 | seg 11/01, 10h | semana 11 a 17/01: fica | enviar W1 (utm_content=w1-657) | saída padrão |
| 3 | qui 21/01, 10h | semana 18 a 24/01: fica | enviar W2 | saída padrão |
| 4 | seg 01/02, 9h | semana 01 a 07/02: fica | enviar E2 | saída padrão |
| 5 | qui 04/02, 10h | fica | enviar W3 | saída padrão |
| 6 | ter 02/03, 10h | semana 01 a 07/03: 1 WhatsApp | enviar AC | saída padrão |
| 7 | ter 20/04, 10h | CC4 aceita "verificar por já ter começado"; 3º módulo em 22/05/2027 | enviar PI (sem link) | SA6; lista fecha às 23h59 de 21/05 (SA3) |

**Como desfazer:** pausar a régua de 657, limpar a flag da NP2 de A1 (a NP2-T4 de 05/01 segue excluída para A1 por regra própria).

---

## 12. Campos do CRM

Nomes provisórios [SUPOSIÇÃO]. Nenhum guarda dado pessoal em arquivo da squad; o CRM guarda no contato e a squad lê só contagens.

| Campo | Onde | Tipo | Uso | Já existe no desenho? |
|---|---|---|---|---|
| [opt_in_email], [opt_in_whatsapp] (com data, origem, finalidade) | contato | sim ou não | EN1 a EN3 | sim (estrategia-de-relacionamento-pos) |
| [área_de_interesse], [praça] | contato | texto | listas | sim |
| [curso_de_interesse] | contato | texto ou etiqueta | L-A14E (equinos ou 341) | **novo** |
| [respondeu_em], [pediu_sair], [matriculou] | contato | data ou sim ou não | SA1, SA5, SA6 | sim |
| [time_assumiu] | contato | sim ou não | EN5, SA6 | **novo** |
| [fim_janela_silencio], [vinculo_ufape] | contato | data, lista | EN7, EN6 | sim (arquiteto-de-fluxos-geral, 6.1) |
| [base_graduacao] | contato | sim ou não | teto de 3 por semana (CC8) | **novo** (ou derivado da etiqueta existente) |
| [regua_com_data_ativa_área] | contato, por área | sim ou não | saída da NP2 | sim (campanhas-de-nutricao-pos, 6.1) |
| [kit_ultimo_toque_<código>] | contato, por turma | texto | EN8, auditoria | **novo** |
| [kit_saiu_motivo_<código>] | contato, por turma | pagou, pagou_gemea, data_limite, sair, descadastro, devolucao, respondeu, turma_parada, engajamento | SA1 a SA10; leitura só somada | **novo** |
| [wa_campanha_sem_interacao] | contato | número | SA9 (E1) | **novo** |
| [data_limite_turma], [estado_da_turma_hoje] | turma | data, texto | SA3, SA4, CC4 | **novo** |
| [nota_gut_fila] | turma | número | desempate da seção 7.4 | **novo** (341 = 80; 289 = 48; 68615 = 48; 657 e 333 = 45) |
| [data_do_item] | turma | data | D2, 6.1 | **novo** |
| registro de supressão | contagem | número por motivo, toque e turma | relatório do cmo e painel de 13.4 | **novo** (só somado) |

---

## 13. Pedidos de aprovação humana e como desfazer cada automação

Quem aprova: a pessoa do marketing que aprovou o plano geral, até a tabela de ufape-geral.md ser preenchida (A9) [CONFIRMAR]. Quem executa no CRM: [CONFIRMAR]. **Nada abaixo está ligado.**

### 13.1 Automações (AF)

| # | O que | Por que | Quanto | Efeito esperado | Como desfazer |
|---|---|---|---|---|---|
| AF1 | Criar L-A1, L-A2, L-A11 e L-A14E em **rascunho**, com os filtros das seções 2 e 3, sem agendar envio | uma regra única de quem recebe cada kit | sem custo de mídia; horas de quem configura [CONFIRMAR]; tamanho de cada lista só somado [CONFIRMAR, OB2] | quatro listas auditáveis, vazias de envio | arquivar a lista (não apaga contato nem histórico) |
| AF2 | Ligar as regras de saída SA1 a SA10 e a reconferência antes do disparo (06h e 30 minutos antes) | o plano manda sair quem pagou, a turma depois da data limite, 333 depois de 26/03 e o descadastro em até 48 h | sem custo de mídia; horas [CONFIRMAR] | ninguém recebe o que já não cabe | desligar regra por regra e voltar ao envio com conferência manual. **SA5 (SAIR e descadastro) não se desliga** |
| AF3 | Ligar a fila D2, o limite de 1 por dia, o teto de 2 e 2 (1 no E1; 3 na base da Graduação), os dias sem campanha e o desempate GUT da seção 7.4 | toda a base da Pós divide o teto; sem fila o CRM aplicaria a ordem de agendamento | sem custo de mídia; horas [CONFIRMAR] | no máximo 1 mensagem por dia e 2 e 2 por semana para o contato, sem exceção manual | desligar a fila e voltar à conferência manual semana a semana (só com decisão do cmo); o teto e o limite diário são suposições do cmo e voltam ao valor anterior só pelo R1 do plano |
| AF4 | Agendar os 34 toques nas datas de 7.1, cada um **só depois do OB2 daquele toque**, do qa próprio e do teste de humano; 341 e 333 com os portões das seções 11.3 e 11.4 | a base é a alavanca mais barata da turma | sem custo de mídia; custo por conversa de marketing do WhatsApp Business se o envio for por API [CONFIRMAR U11a]; o valor precisa vir antes de 07/12 | 10 e-mails e 24 WhatsApp dentro do teto | cancelar o agendamento do toque ou pausar a régua; toque já enviado não volta, por isso cada toque tem aprovação própria |
| AF5 | Ligar a saída da NP2 por área nas datas da seção 9 | dono único do convite | sem custo | a nutrição não repete o convite do kit | limpar a flag [regua_com_data_ativa_área] da área (volta à NP2 no próximo toque pendente, sem reenviar o passado) |
| AF6 | Parametrizar a UTM da seção 10 em links e templates e criar a tabela de correspondência de nomes | atribuição por turma | sem custo | cliques e respostas por toque, só somados | trocar o nome na tabela de correspondência; link já enviado mantém a UTM antiga |
| AF7 | Ligar o registro de supressões por motivo e o painel somado dos indicadores de 13.4 do plano geral | o cmo lê só número somado e precisa saber quantos toques a fila cortou | sem custo de mídia; horas [CONFIRMAR] | relatório de segunda-feira com supressões por motivo | desligar o registro; nenhum dado pessoal sai do CRM |

### 13.2 Decisões de política (DEC)

| # | Decisão proposta | Quem decide | Se não for aprovada |
|---|---|---|---|
| DEC1 | Desempate da fila entre toques com a mesma data de início: 341 (80), 289 (48), 68615 (48, perde para 289 pela data limite). Vale em 11 a 17/01 e em 08 a 14/03. Sem 341, 289 vence 68615. Inclui a escolha do CF1 se a régua de Livres de 68618 voltar. | cmo | a fila fica sem desempate e o CRM decide pela ordem de agendamento, o que não é explicável |
| DEC2 | Pagou 68615 ou 333: sai das duas. Os demais kits são independentes. | pessoa do marketing | cada turma sai só a sua; quem pagou uma continua a receber a gêmea |
| DEC3 | Inscrição paga sem 1ª mensalidade não tira o contato do kit; o time pode marcar [time_assumiu]. | pessoa do marketing, com a Ufape (U11) | quem pagou só a inscrição sai e o time assume a conversa |
| DEC4 | Sem reenvio de e-mail para quem não abriu nesta onda. | cmo | o reenvio entra como follow-up de prioridade 4, em dia livre, em pedido próprio |
| DEC5 | S3 recebe o kit, menos com [time_assumiu]=sim ou resposta ao time nas últimas 48 h. | pessoa do marketing | S3 sai do kit e fica só com o time |
| DEC6 | UTM: se o primeiro envio escorregar de mês depois do template aprovado, manter o nome e registrar o desvio. Reabertura da lista de 333 depois de 26/03 só por pedido novo, com texto novo e qa. | pessoa do marketing | o nome muda e o template volta à aprovação da Meta; sem OU3 a lista de 333 nunca reabre |
| DEC7 | Equinos só entram em NP2 com OU10 resolvida (CF2). | cmo | a NP2 apresenta a turma 341 antes de a regra 10 do plano permitir |

---

## 14. Etapas, cortes e o workflow de reuso

### 14.1 Quantas etapas

| Fluxo | Etapas | Chamadas de agente | Aprovações humanas |
|---|---|---|---|
| Este desenho (F10) | 1 | 1 (arquiteto-de-fluxos) | 1 |
| Conferência do qa (F13, onda2c) | 1 | 1 (qa-de-marketing) | 1 |
| Execução no CRM (etapas 4 a 7 do documento de fluxo) | 4 | 0 (humano) | 4 mais 1 por toque (OB2) |
| Workflow de reuso `/conferir-fila-de-mensagens` (14.3) | 2 | 2 | 2 |

### 14.2 O que foi cortado (nenhum corte muda a entrega)

1. Agente próprio para validar calendário: cortado. A conta está na seção 7 e o qa-de-marketing a confere.
2. Nova rodada de copy-de-mensagens: cortada. Os textos e as datas são os do F7; este arquivo não toca neles.
3. Exceção codificada para 17/12 (C5): cortada. A fila resolve sozinha (6.2).
4. Reenvio para quem não abriu: cortado (DEC4).
5. Lista por curso em A1, A2 e A11: cortada. A área basta; só A14 vira lista de curso.
6. Nota GUT por contato: cortada. A nota é por turma e só desempata data igual.
7. Workflow semanal novo de revisão: cortado. A revisão de segunda-feira do cmo já existe e lê as contagens.
8. Painel novo de acompanhamento: cortado. Usa-se o painel de 13.4 que o analista-de-dados já tem como encomenda.
9. Datas de janeiro de contingência (CF8): não reservadas. Só são calculadas se o atraso acontecer, para não bloquear dias à toa.

### 14.3 Texto do workflow para .claude/commands (não gravado)

Arquivo `.claude/commands/conferir-fila-de-mensagens.md`, para quando entrar uma onda ou turma nova na mesma base (onda 3, por exemplo) ou quando um prazo mudar:

```
---
description: Confere listas, fila D2, limite de 1 por dia, teto semanal, saída da NP2 e UTM de um lote de turmas. Cadeia: arquiteto-de-fluxos -> qa-de-marketing
argument-hint: [linha: pos, livres ou eventos] [caminho do arquivo com os toques do lote] [turmas do lote]
---
Execute o workflow "Conferir a fila de mensagens de um lote".

Leia contexto/ufape-geral.md e o contexto da linha de negócio antes de começar. Linha, arquivo de toques e turmas deste pedido: $ARGUMENTS

Regras: siga o teto D16 e as regras E1 a E4 da seção 13 de saidas/02-estrategia-e-posicionamento/cmo-geral-2026-10-26.md e a fila D2 da seção 12. Dados de curso só de contexto/catalogo-de-cursos.md; o que faltar vira [CONFIRMAR NO CATÁLOGO]. Nenhum dado pessoal. Nada é ligado, agendado, enviado ou pago.

1. Use o agente arquiteto-de-fluxos para produzir as listas por turma e área, as regras de entrada e de saída, a conta semana a semana do pior caso contra os toques já aprovados (inclusive os de saidas/10-operacoes-de-marketing/arquiteto-de-fluxos-pos-2026-10-27-onda2.md e a newsletter), a saída da NP2 e a UTM do CRM, com pedido de aprovação para cada automação (o que, por que, quanto, efeito esperado, como desfazer). Use a skill matriz-gut (.claude/skills/matriz-gut/SKILL.md) só para desempatar toques com a mesma data e a skill mapear-fluxo (.claude/skills/mapear-fluxo/SKILL.md) para o SIPOC. Salve e passe o arquivo para a próxima etapa.
2. Use o agente qa-de-marketing para conferir o arquivo contra os toques aprovados, o teto, a fila e as auditorias, e devolver aprovado ou corrigir. Salve e passe o arquivo para a próxima etapa.
3. Rode a auditoria do departamento (auditorias/10-operacoes.md) e auditorias/conformidade-educacional.md antes de marcar como pronto, e também auditorias/07-email-e-whatsapp.md para as listas e as saídas.

Pare depois de cada etapa, mostre a saída e espere minha aprovação.
Concluído quando: nenhum dia do lote tem dois toques para o mesmo contato, nenhuma semana passa de 2 WhatsApp e 2 e-mails (3 somando canais na base da Graduação), cada empate de data tem desempate escrito, cada automação tem pedido de aprovação com o que desfazer, nenhuma UTM foge de pos_<código>_<AAAAMM> e o lote está aprovado.
```

Este workflow tem 2 etapas: 2 chamadas ao Claude e 2 aprovações humanas, mais a auditoria. Cita só agentes, skills e auditorias que existem.

---

## 15. Auditorias

**auditorias/10-operacoes.md**
- [ ] conhecimento/INDICE.md está atualizado: **não feito por este agente** (a encomenda manda editar só este arquivo); o orquestrador atualiza.
- [x] Todo workflow cita só agentes, skills e auditorias que existem (arquiteto-de-fluxos, qa-de-marketing, matriz-gut, mapear-fluxo, auditorias 10, 07 e conformidade-educacional).
- [x] Todo workflow termina com auditoria e critério de pronto conferível (14.3 e "Concluído quando" de 1.2).
- [x] Aprovação humana antes de publicar, enviar ou pagar (AF1 a AF7, DEC1 a DEC7, OB2 por toque).
- [x] Acesso mínimo: a squad escreve texto; o CRM é de humano.
- [x] Nenhuma chave em arquivo de texto.
- [x] Documento com data de revisão (30/11/2026).
- [ ] Toda peça pública passou por qa-de-marketing e por conformidade-educacional: este arquivo não é peça pública; vai ao qa (F13, onda2c).
- [x] Dados de curso batem com o catálogo: nome, turma, campus e datas citados vêm do plano v2 e do F7, que os tiram do catálogo, seção 2 e das fichas; nenhum preço, bolsa ou ato regulatório neste arquivo.

**auditorias/07-email-e-whatsapp.md**
- [x] Consentimento e descadastro funcionando: EN1 a EN3, SA5; teste de humano antes do primeiro envio.
- [x] Cada mensagem tem um objetivo: herdado do F7.
- [x] Segmentos recebem mensagens da etapa da jornada: S2 e S3 da área; S6, S8 e S9 fora.
- [x] Réguas têm regras de saída: seção 4.
- [ ] Resultados registrados para cada envio: registro de supressões (AF7) e UTM (seção 10); depende do CRM [CONFIRMAR P15].
- [ ] Cliques, respostas e conversões medidos: UTM e contagem de respostas "TURMA"; o PI não tem clique.
- [x] WhatsApp em horário comercial, com frequência humana: CC5, CC7 e CC8; template da Meta só se a Ufape usar API (U11a).

**auditorias/conformidade-educacional.md**
- [x] Nenhuma peça nova: o arquivo não tem texto de mensagem nem de página.
- [x] Sem frase ligada ao MEC, sem preço, sem bolsa, sem "últimas vagas", sem nota de curso: nada disso aparece.
- [x] WhatsApp e e-mail só com consentimento e saída fácil.
- [x] Nenhum dado pessoal em peça ou arquivo de trabalho.
- [ ] Página de destino entrega o que a mensagem promete: pendente de OB1; trava no CC12.
- [ ] Formulários com finalidade e política de privacidade: pendente externo, conferido em 04/12.

**Resultado:** pronto para o qa-de-marketing. A execução depende de OB2 por toque, OB1, AF1 a AF7, DEC1 a DEC7 e das respostas U10, OU3, OU10, OU11, OU17, U11a e P15. Busca de travessão e meia-risca: feita pelo agente na escrita; a conferência por busca é do orquestrador.

**Próximo agente sugerido:** qa-de-marketing (F13, revisão "onda2c": fluxos, com auditorias/10-operacoes.md, auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md).

---

## Fatos (com fonte)

- Os 5 kits, o calendário de 34 toques e o reservado de 333, os horários (e-mail 9h, WhatsApp 10h), os IDs de utm_content, a variante de 341, 333 sem texto depois do início e 657 a partir de 05/01: F7 (copy-de-mensagens-pos-2026-10-27-onda2.md, seções 0 e 7.1) e plano da onda 2, seção 7.3 e regras 7 a 12.
- Início, turma, campus e 3º módulo das 5 turmas: plano da onda 2, seção 1 (que cita o catálogo, seção 2, e as fichas). Datas de encerramento das listas: plano, seção 7.4.
- Teto D16 (2 WhatsApp e 2 e-mails por semana; 1 por dia; contato nas duas bases com o teto menor, de 3 por semana somando canais); regras E1 a E4; fila D2 e D3: cmo-geral, seções 12.2 e 13.3. Padrão de UTM D11 e D12: cmo-geral, 12.7.
- Janela de silêncio D8 e ex-aluno D10: cmo-geral, 12.5; campos do CRM: arquiteto-de-fluxos-geral-2026-10-26.md, 6.1.
- Segmentos S1 a S12 e a fila: estrategia-de-relacionamento-pos-2026-10-26.md, seção 4. S3 é "lead que falou com o time e não pagou".
- NP1, NP2, NP3, o lote de 30/11, as datas T1 (01/12), T2 (09/12), T3 (16/12) e T4 (05/01), a lista de áreas em que NP2 roda e os campos: campanhas-de-nutricao-pos-2026-10-26.md, seções 3, 4 e 6. A régua de 68618: seção 4, semanas S7 e S8.
- Edições da newsletter em 03/12, 17/12, 07/01, 14/01, 28/01 e 18/02 e o WhatsApp de 19/11 e 04/12: newsletter-geral-2026-10-26.md, seções 3.1 e 4 a 5.
- Toques da onda 1 em 15/12, 16/12, 06/01 e 12/01: cmo-pos-2026-10-26.md, seção 6 e 8.2.
- Nota de grupo GUT 45 (5, 3, 3) para as cinco turmas: cmo-geral, seção 3. Metas em reais de R$ 652.500,00 (341) e R$ 531.000,00 (289 e 68615): plano da onda 2, seção 1.
- Decisões 11, 14, 17 e 18: docs/execucao-2026-10-26.md. Desempate da skill matriz-gut: ".claude/skills/matriz-gut/SKILL.md", passo 5.
- Calendário: 01/01/2027 é sexta-feira; 08 e 09/02/2027 são Carnaval; 10/02 é Cinzas; 26/03/2027 é sexta-feira da Paixão; 28/03/2027 é domingo de Páscoa; 25/01 é feriado municipal de São Paulo (plano da onda 2, regra 11 e fatos).
- As ferramentas de agente do arquiteto-de-fluxos são Read e Write: ele não executa no CRM (.claude/agents/arquiteto-de-fluxos.md).

## [SUPOSIÇÃO]

- As notas GUT por turma (341 em 80; 289 e 68615 em 48), a leitura "data limite mais próxima" como desempate entre 289 e 68615, e a ordem 341, 289, 68615 nas duas semanas (DEC1).
- [data_do_item] igual à data limite quando a turma já começou.
- Pagou 68615 ou 333, sai das duas (DEC2); quem responde a um toque de A11 sai dos dois kits (SA6).
- Inscrição paga sem 1ª mensalidade não tira o contato (DEC3); S3 recebe o kit salvo [time_assumiu] (DEC5).
- Não filtrar L-A2 por praça.
- Geração da lista às 06h e reconferência 30 minutos antes (depende da ferramenta); horário de verificação da OU10 em 11/12 às 18h.
- Horários de job (00h05) para a saída por data limite e para a flag da NP2.
- Cadência quinzenal em quintas da newsletter depois de 18/02 e versão de WhatsApp no dia seguinte a cada edição.
- Nomes provisórios dos campos do CRM da seção 12.
- Resposta com "parar" ou parecida vai a humano para registro.
- Que a flag da NP2 liga mesmo com o primeiro toque do kit suprimido.
- Os prazos de 48 h e de 24 h dependem da ferramenta; a regra de E3 é o limite máximo.

## [CONFIRMAR]

- **U10** (pré-requisito de 657), **OU3** (reposição dos módulos; 333 depois do início), **OU10** (promoção de 341), **OU11** (local da prática e formato do módulo 3 de 341), **OU17** (datas de 333 e 341 em feriado), **OU6** (3º módulo: véspera ou 1º dia), **OU13** (CEP de 68615), **U11** (valor da inscrição, para distinguir inscrição de 1ª mensalidade em DEC3), **U11a** (API oficial do WhatsApp e templates), **P15** (ferramenta de CRM, e-mail e WhatsApp, e rastreio de wa.me).
- Contatos com opt-in por área e canal e o tamanho de cada lista (OB2); campo de finalidade aceita; existência da marca de equinos ou de [curso_de_interesse]; como o CRM marca conversa ativa com o time.
- Quem executa no CRM, quem aprova cada tipo de peça (A9) e o custo por conversa de marketing, se houver API.
- Datas da newsletter depois de 18/02 e existência de WhatsApp nas edições 3 a 7; calendário da Graduação (CF6); toques da onda 3 de A1 e A2 em março e abril; se a régua de Livres de 68618 volta (CF1) e o que é "P6" na campanhas-de-nutricao-pos.
- Se a Ufape quer a flag de saída da NP2 em A2 e A11 desde 02/12 (como a campanhas-de-nutricao-pos supunha) ou só em 07 e 08/12 (como o plano da onda 2 manda).
- Tabela de correspondência entre nomes de campanha antigos e novos (analise-de-midia) para os desvios de mês (DEC6).
- Se a página pode sair com frase ligada ao MEC antes da troca (regulação, regra 13 do plano).
