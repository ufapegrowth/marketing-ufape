# Copy de mensagens: régua de e-mail e WhatsApp das provas de bolsa da Pós-graduação de 27/11/2026

- **Agente:** copy-de-mensagens (departamento 07, E-mail, WhatsApp e Relacionamento), camada 3, onda 1
- **Linha:** pos
- **Data:** 26/10/2026 (segunda-feira)
- **Status:** rascunho para o qa-de-marketing e para a aprovação humana (A-C7 da estratégia de campanha). A squad não dispara nada: são textos para o CRM enviar, só para contatos com opt-in. Nada é publicado, enviado ou pago.
- **Entradas lidas:**
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md (item prova de bolsa)
  - contexto/catalogo-de-cursos.md (seções 2 e 3; leitura da seção 1 e do início do arquivo)
  - contexto/cursos/pos/68639-prova-de-bolsa-de-estudos-para-anestesiologia-veterinaria.md (modelo da página da prova: documento com foto, sem celular e relógio, endereço de São Paulo, bolsas)
  - templates/mensagem.md
  - .claude/skills/assuntos-de-email/SKILL.md
  - .claude/skills/mapear-regua/SKILL.md
  - saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md (entrada principal: oferta, destino D1 a D4, calendário, regras de canal)
  - saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md (persona P4)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md (voz: precisa, próxima, transparente)
  - auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md
- **Dados pessoais:** nenhum. Os textos usam campos entre colchetes que o CRM preenche. Docentes não são nomeados. Nenhum aprovado de edição anterior é citado.
- **Não abri** faculdade.ufape.com.br. O texto da página vem da ficha da prova 68639 e das fichas já lidas pelo agente de estratégia.

---

## 0. Resumo

1. A régua tem 20 mensagens em 5 etapas: convite, lembretes, confirmação de inscrição, véspera e dia da prova, pós-prova. Mais 17 respostas prontas para o time de vendas.
2. Cada mensagem tem um único objetivo e uma única chamada para ação, declarados no bloco dela.
3. Todo texto usa só: inscrição de R$ 100,00, prova presencial em 27/11/2026 das 9h às 13h, 11 bolsas por prova (2 de 50% com monitoria, 4 de 25%, 5 de 10%), nota de corte 7,0, resultado por WhatsApp ou e-mail, 2 dias úteis para recurso, 10 dias úteis para matrícula, bolsa não acumulativa e intransferível, desempate por análise de currículo.
4. O destino de cada prova (para qual turma a bolsa vale) não está em nenhuma página. Nenhuma mensagem de convite cita turma. O bloco de turma existe, mas só é liberado depois da resposta da Ufape (A-C2). Das 22 provas, 10 estão em D1 (destino provável), 4 em D2, 4 em D3 e 4 em D4 sem turma aberta: [CONFIRMAR destino] (seção 5).
5. Bloqueios que seguram envio: local da prova em Goiânia (a página 68640 mostra o endereço de São Paulo), links de Cardiologia invertidos, regras de Felinos contraditórias, data do resultado, prazo de inscrição, regra do aprovado sem bolsa.
6. Não há comparação com outra instituição, escassez, frase de certificação, percentual de aprovação nem valor de curso com bolsa calculado.

---

## 1. Regras desta régua

**Quem recebe**
- WhatsApp: só contato com opt-in registrado no CRM (campo [opt_in_whatsapp] igual a sim) [CONFIRMAR o nome do campo e onde o consentimento fica guardado].
- E-mail: só contato com consentimento de e-mail registrado e sem descadastro [CONFIRMAR ferramenta].
- Base de leads e ex-alunos: a segmentação é por [segmento] (lead ou ex_aluno) e por [área_de_interesse], se o CRM tiver. Sem área de interesse, o contato recebe a versão mestre.
- Quem já se inscreveu na prova sai da régua de convite e entra na régua de serviço (confirmação, véspera, dia, resultado).

**Quando envia**
- WhatsApp só em dia útil, das 9h às 18h [SUPOSIÇÃO de janela comercial, a Ufape confirma]. Fora dela, o envio espera abrir.
- Cadência de campanha por contato: no máximo 2 WhatsApp e 2 e-mails por semana, somando todas as campanhas da Ufape [SUPOSIÇÃO de limite, vem da estratégia de campanha, seção 4.3]. Mensagens de serviço ao inscrito não contam.
- Sem mensagem das provas em 20/11 e 21/11 (Workshop de Neuromonitorização, linha Eventos). Sem envio em 02/11 (feriado) [SUPOSIÇÃO de efeito].
- Antes de cada envio, o CRM confere o status "aberto" da prova no catálogo. Prova que deixou de estar aberta sai da lista da mensagem.
- Uma mensagem por área, não duas: a versão por área substitui a mestre para quem tem área de interesse.

**Como sai**
- WhatsApp: "responda SAIR" no texto e botão de resposta rápida "Sair" no template. Quem responde SAIR sai de toda mensagem de campanha.
- E-mail: link de descadastro e link da política de privacidade no rodapé.

**Regras de saída da régua:** inscreveu na prova; respondeu (a automação para e o time de vendas assume); pediu para sair; bloqueou ou denunciou (suspender); prova deixou de estar aberta; matriculou (sai de tudo).

**Link e UTM:** no máximo um link por mensagem. UTM: utm_source (whatsapp ou email), utm_medium=base, utm_campaign=provas-de-bolsa-2026-11-27, utm_content=<id da mensagem>-<área>-<código da prova> [SUPOSIÇÃO de padrão, o arquiteto-de-fluxos confere].

**O que se mede (além de abertura e leitura):** cliques, respostas, inscrições concluídas por mensagem, comparecimento por prova e matrículas com bolsa. Números somados por prova, sem dado pessoal.

**Idioma e tom:** português do Brasil, de colega para colega, frases curtas, sem assumir que o leitor é homem, sem emoji, sem caixa alta para gritar.

---

## 2. Mapa da régua (skill mapear-regua)

Gatilho: contato com opt-in na base de leads e ex-alunos. Objetivo final: inscrição na prova e, depois, matrícula com bolsa dentro do prazo.

| ID | Data e hora | Canal | Quem recebe | Função (objetivo único) |
|---|---|---|---|---|
| M2 | ter 03/11, 10h | E-mail | Base sem área de interesse | Levar à página das provas e à inscrição |
| M4 | ter 03/11, 10h | E-mail | Base com área de interesse liberada | Levar à página da prova da área |
| M1 | qua 04/11, 10h | WhatsApp | Base sem área de interesse | Fazer o contato dizer a especialidade para receber o link |
| M3 | qua 04/11, 10h | WhatsApp | Base com área de interesse liberada | Levar à página da prova da área |
| M6 | qui 05/11, 10h | E-mail | Quem não abriu M2 ou M4 e não se inscreveu | Lembrete: levar à inscrição |
| M5 | sex 06/11, 10h | WhatsApp | Quem não respondeu a M1 ou M3 e não se inscreveu | Lembrete: levar à inscrição |
| M7 | ter 10/11, 10h | E-mail | Base que não se inscreveu | Tirar as dúvidas e levar à inscrição |
| M8 | seg 23/11, 10h | E-mail | Base que não se inscreveu | Reta final: levar à inscrição |
| M9 | ter 24/11, 10h | WhatsApp | Base que não se inscreveu | Reta final: levar à inscrição |
| M10 | na hora do pagamento | E-mail | Inscrito | Confirmar a inscrição com as regras |
| M11 | na hora do pagamento (WhatsApp na próxima janela comercial) | WhatsApp | Inscrito com opt-in | Confirmar a inscrição com as regras |
| M12 | qui 26/11, 10h | E-mail | Inscrito | Véspera: confirmar presença |
| M13 | qui 26/11, 14h | WhatsApp | Inscrito com opt-in | Véspera: confirmar presença |
| M14 | sex 27/11, 7h | E-mail | Inscrito | Dia da prova: horário, local e regras |
| M15 | sex 27/11, 8h (só se a janela permitir) | WhatsApp | Inscrito com opt-in | Dia da prova: horário, local e regras |
| M16 e M17 | dia da divulgação do resultado [CONFIRMAR data] | WhatsApp e e-mail | Aprovado com bolsa | Levar à conversa de matrícula dentro do prazo |
| M18 | dia da divulgação [CONFIRMAR regra antes de usar] | WhatsApp e e-mail | Aprovado sem bolsa | Levar à conversa sobre as condições da turma |
| M19 | dia da divulgação | WhatsApp e e-mail | Quem não atingiu a nota de corte | Oferecer a conversa sobre as condições normais da turma, sem pressão |
| M20 | dia útil seguinte à prova [CONFIRMAR política de ausência] | WhatsApp e e-mail | Inscrito que não compareceu | Oferecer a conversa sobre as condições normais da turma, sem cobrança |

Semana de 03 a 07/11: 2 e-mails e 2 WhatsApp por contato (dentro do limite). Semana de 09 a 13/11: 1 e-mail (M7) mais o reenvio de 12/11. Semana de 23 a 27/11: 2 e-mails (M8 e reenvio de 25/11) e 1 WhatsApp (M9), fora as mensagens de serviço.

**Etiquetas e campos no CRM e no Chatwoot:** [segmento] (lead ou ex_aluno); [opt_in_whatsapp] e [opt_in_email] com data do consentimento; [área_de_interesse]; [praça]; [inscrito_prova_código]; [presença_confirmada]; [resultado] (aprovado_com_bolsa, aprovado_sem_bolsa, nao_atingiu, ausente); [matriculou]; [pediu_sair]. Nenhum desses campos entra em arquivo da squad com dado de pessoa.

### Campos que o CRM preenche

| Campo | O que é | Regra |
|---|---|---|
| [nome] | Primeiro nome do contato | Se vazio, usar "olá" sem nome |
| [área] | Nome da especialidade no padrão da linha (ver seção 5) | Só prova com status "aberto" e liberada na seção 5 |
| [praça] | São Paulo ou Goiânia | Da prova |
| [endereço_da_prova] | São Paulo: Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100. Goiânia: [CONFIRMAR] | Não preencher para Goiânia até a Ufape confirmar |
| [link_mestre] | Página que reúne as provas | [CONFIRMAR se existe]. Sem ela, M2 e M8 usam o link do WhatsApp de vendas |
| [link_da_prova] | Página da prova da área, com UTM | Um link por mensagem |
| [lista_das_especialidades_liberadas] | Lista das áreas liberadas na seção 5 | Montada pelo CRM no dia do envio |
| [nota] | Nota do inscrito | Só nas mensagens de resultado |
| [percentual_da_bolsa] | 50% (monitoria), 25% ou 10% | Só em M16 e M17 |
| [data_limite_recurso] e [data_limite_matrícula] | 2 dias úteis e 10 dias úteis após a divulgação | Calculadas pela Ufape [CONFIRMAR calendário de dias úteis] |
| [turma_de_destino] e [condição_da_turma] | Turma, início e condição completa do catálogo | Só depois da resposta A-C2 |
| [canal_de_recurso] | Como pedir recurso | [CONFIRMAR] |
| [link_vendas] | WhatsApp de vendas: São Paulo (11) 91366-9290, Goiânia (62) 9420-1847 | Contatos oficiais de contexto/ufape-geral.md |

---

## 3. Mensagens

Toda mensagem segue templates/mensagem.md. Em todas, "Linha de negócio e curso" é Pós-graduação, provas de bolsa de 27/11/2026 (campanha única das provas). A primeira linha ou o assunto "A" e "B" são os dois escolhidos para teste; as outras três ficam como reserva. Cada lista foi escrita para variar entre benefício, curiosidade, pergunta e direto, sem urgência falsa.

Frase padrão de oferta usada nos textos, igual à da campanha: "Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0."

### 3.1 Convite à base de leads e ex-alunos

#### M1. WhatsApp, convite mestre

- **Canal:** WhatsApp
- **Objetivo (único):** fazer o contato responder com a especialidade que quer, para o time enviar o link da prova.
- **Segmento:** base de leads e ex-alunos com opt-in, sem área de interesse registrada e que ainda não se inscreveu.
- **Primeira linha A (teste):** [nome], quantas bolsas tem cada prova? São 11.
- **Primeira linha B (teste):** [nome], qual especialidade você quer? Tem prova de bolsa em 27/11.
- Reserva: [nome], as provas de bolsa da Pós-graduação são em 27/11.
- Reserva: Oi, [nome]. A prova de bolsa da Ufape custa R$ 100,00 para fazer.
- Reserva: [nome], as inscrições das provas de bolsa da Pós-graduação estão abertas.
- **Gancho:** o número de bolsas e o custo de entrada.
- **Corpo (texto do template):**

> Oi, [nome], aqui é da Faculdade UFAPE. [abertura_segmento]
>
> As provas de bolsa da Pós-graduação são em 27/11 (sexta), das 9h às 13h, presenciais em São Paulo ou em Goiânia, conforme a especialidade.
>
> Inscrição de R$ 100,00. 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0.
>
> Qual especialidade você quer? Responda com o nome dela e eu envio o link da prova.
>
> Para não receber mais mensagens, responda SAIR.

  [abertura_segmento]: lead, vazio. Ex-aluno: "Você já estudou com a gente."
- **Chamada para ação:** responder com a especialidade.
- **Resposta pronta do time quando o contato responde (janela de 24 h, sem template):** "Obrigado, [nome]. Esta é a página da prova de [área]: [link_da_prova]. Ela mostra data, local, regras e a inscrição. Se tiver dúvida, pergunte por aqui."
- **Follow-up (quem não respondeu):** M5, sexta 06/11.
- **Data e horário:** qua 04/11, 10h.
- **Opt-in de WhatsApp confirmado:** envio só para [opt_in_whatsapp] igual a sim. Sem registro, não envia.
- **Template aprovado pela Meta:** nome sugerido pb_convite_mestre_v1 [SUPOSIÇÃO de nome]; categoria marketing; variáveis {{1}} nome, {{2}} abertura do segmento (duas versões do template, uma para lead e outra para ex-aluno, se a Meta não aceitar variável vazia); botão de resposta rápida "Sair". Submissão e aprovação pendentes.
- **Forma de sair:** "responda SAIR" no texto e botão "Sair".

#### M2. E-mail, convite mestre

- **Canal:** e-mail
- **Objetivo (único):** levar o contato à página das provas para escolher a especialidade e se inscrever.
- **Segmento:** base de leads e ex-alunos com consentimento, sem área de interesse registrada, que ainda não se inscreveu.
- **Assunto A (teste):** 11 bolsas por prova na Pós-graduação, com inscrição de R$ 100,00
- **Assunto B (teste):** [nome], a prova de bolsa da Pós-graduação é em 27/11
- Reserva: Prova de bolsa em 27/11: como funciona, em 6 pontos
- Reserva: Quanto custa tentar uma bolsa na Pós-graduação da Ufape
- Reserva: [nome], qual especialidade você quer fazer?
- **Texto de pré-visualização:** Prova presencial em 27/11, das 9h às 13h, em São Paulo ou Goiânia, conforme a especialidade.
- **Gancho:** a prova de bolsa como forma de conhecer o valor antes de decidir a matrícula.
- **Corpo:**

> Olá, [nome],
>
> [abertura_segmento_email]
>
> A Faculdade UFAPE aplica provas de bolsa para a Pós-graduação em 27 de novembro, sexta-feira, uma prova por especialidade.
>
> Escolher uma pós envolve decidir antes de saber quanto você pagaria. A prova de bolsa ajuda nessa decisão: você faz a prova e, se atingir a nota de corte e receber uma das bolsas, tem até 10 dias úteis para fazer a matrícula com ela.
>
> Como funciona:
> - Inscrição: R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão.
> - Prova presencial em 27/11/2026, das 9h às 13h, com questões de múltipla escolha e dissertativas, em São Paulo ou em Goiânia, conforme a especialidade.
> - 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.
> - Nota de corte 7,0 (mínimo de 70% de acerto). Em caso de empate, análise de currículo.
> - Resultado por WhatsApp ou e-mail. Depois dele, 2 dias úteis para recurso e 10 dias úteis para a matrícula.
> - A bolsa não é acumulativa e é intransferível.
>
> Especialidades com prova aberta: [lista_das_especialidades_liberadas].
>
> Todas essas regras estão na página de cada prova.
>
> [Botão] Ver as provas e me inscrever: [link_mestre]
>
> Equipe de relacionamento, Faculdade UFAPE

  [abertura_segmento_email]: lead, vazio. Ex-aluno: "Você já passou pela Ufape. Se pensa em outra especialidade, a prova de bolsa é uma das formas de entrar. A bolsa da prova não é acumulativa com outras condições."
- **Chamada para ação:** "Ver as provas e me inscrever" (um botão, um link).
- **Follow-up (quem não abriu):** M6, quinta 05/11.
- **Data e horário:** ter 03/11, 10h.
- **Opt-in:** consentimento de e-mail registrado.
- **Template Meta:** não se aplica.
- **Forma de sair:** link de descadastro e política de privacidade no rodapé, com o endereço da Faculdade UFAPE (Av. 9 de Julho, 3939, São Paulo, SP).

#### M3. WhatsApp, convite por área

- **Canal:** WhatsApp
- **Objetivo (único):** levar o contato à página da prova da especialidade de interesse dele.
- **Segmento:** base com opt-in e [área_de_interesse] registrada em uma área liberada da seção 5, que ainda não se inscreveu. Goiânia só depois de o local ser corrigido.
- **Primeira linha A (teste):** Oi, [nome]. A prova de bolsa de [área] custa R$ 100,00 e tem 11 bolsas.
- **Primeira linha B (teste):** [nome], você quer [área]? A prova de bolsa é em 27/11.
- Reserva: [nome], tem prova de bolsa para a Pós-graduação em [área] em 27/11.
- Reserva: [nome], a Pós-graduação em [área] tem prova de bolsa na sexta, 27/11.
- Reserva: [nome], uma pergunta sobre [área]: já viu a prova de bolsa?
- **Gancho:** a prova da própria especialidade da pessoa.
- **Corpo (texto do template):**

> Oi, [nome], aqui é da Faculdade UFAPE. [abertura_segmento] Você se interessou por [área] com a gente, por isso escrevo.
>
> A prova de bolsa para a Pós-graduação em [área] é em 27/11 (sexta), das 9h às 13h, presencial em [praça].
>
> Inscrição de R$ 100,00. 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0.
>
> Regras e inscrição: [link_da_prova]
>
> Para não receber mais mensagens, responda SAIR.

  A frase "Você se interessou por [área] com a gente" só entra se o CRM registrar o interesse [SUPOSIÇÃO de que a segmentação por interesse existe]. Sem registro, usar M1.
- **Chamada para ação:** abrir o link da prova.
- **Follow-up (quem não respondeu nem clicou):** M5, sexta 06/11.
- **Data e horário:** qua 04/11, 10h.
- **Opt-in de WhatsApp confirmado:** só [opt_in_whatsapp] igual a sim.
- **Template aprovado pela Meta:** pb_convite_area_lead_v1 e pb_convite_area_exaluno_v1 [SUPOSIÇÃO de nomes]; categoria marketing; variáveis {{1}} nome, {{2}} área, {{3}} praça, e botão de URL com sufixo dinâmico {{4}} (link da prova com UTM); botão "Sair". Submissão e aprovação pendentes.
- **Forma de sair:** "responda SAIR" e botão "Sair".

#### M4. E-mail, convite por área

- **Canal:** e-mail
- **Objetivo (único):** levar o contato à página da prova da área de interesse e à inscrição.
- **Segmento:** base com consentimento e [área_de_interesse] em uma área liberada da seção 5.
- **Assunto A (teste):** Prova de bolsa para a Pós-graduação em [área]: 11 bolsas, inscrição de R$ 100,00
- **Assunto B (teste):** [nome], a prova de bolsa de [área] é em 27/11
- Reserva: [área]: como funciona a prova de bolsa da Ufape
- Reserva: Quer se aprofundar em [área]? Tem prova de bolsa em 27/11
- Reserva: Prova de bolsa de [área]: quantas bolsas e qual a nota de corte
- **Texto de pré-visualização:** Prova presencial em [praça], em 27/11, das 9h às 13h. Regras completas na página.
- **Gancho:** [frase_da_área] (hipótese por área, seção 5).
- **Corpo:**

> Olá, [nome],
>
> [abertura_segmento_email] [frase_da_área]
>
> A Faculdade UFAPE aplica a prova de bolsa para a Pós-graduação em [área] em 27 de novembro, sexta-feira, das 9h às 13h, presencial em [praça].
>
> - Inscrição: R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão.
> - 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.
> - Nota de corte 7,0 (mínimo de 70% de acerto). Em caso de empate, análise de currículo.
> - Questões de múltipla escolha e dissertativas.
> - Resultado por WhatsApp ou e-mail, 2 dias úteis para recurso e 10 dias úteis para a matrícula.
> - A bolsa não é acumulativa e é intransferível.
> - Local: [endereço_da_prova].
>
> [bloco_da_turma, só depois de A-C2: "A bolsa vale para a [turma_de_destino]. [condição_da_turma]"]
>
> [Botão] Inscrever-me na prova: [link_da_prova]
>
> Equipe de relacionamento, Faculdade UFAPE

  [condição_da_turma], quando liberada, traz sempre número de parcelas, valor da parcela, total e matrícula, como estão no catálogo (seção 5 e seção 6, resposta 6). Nunca valor com bolsa aplicada.
- **Chamada para ação:** "Inscrever-me na prova" (rótulo sugerido pela análise de conversão).
- **Follow-up (quem não abriu):** M6, quinta 05/11, com o assunto reserva "Quer se aprofundar em [área]? Tem prova de bolsa em 27/11".
- **Data e horário:** ter 03/11, 10h.
- **Opt-in:** consentimento de e-mail registrado.
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro e política de privacidade no rodapé.

### 3.2 Lembretes: antes de 07/11 e na reta final (20 a 26/11)

#### M6. E-mail, lembrete de 05/11 (reenvio para quem não abriu)

- **Canal:** e-mail
- **Objetivo (único):** levar quem não abriu o convite à inscrição.
- **Segmento:** quem recebeu M2 ou M4, não abriu e não se inscreveu.
- **Assunto A (teste):** [nome], quantas bolsas tem cada prova? São 11
- **Assunto B (teste):** Prova de bolsa da Pós-graduação: o que você precisa saber em 1 minuto
- Reserva: A inscrição na prova de bolsa custa R$ 100,00
- Reserva: [nome], sexta, 27/11, tem prova de bolsa
- Reserva: Como funciona a prova de bolsa de [área]
- **Texto de pré-visualização:** 2 bolsas de 50% (monitoria), 4 de 25% e 5 de 10% em cada prova.
- **Gancho:** a pergunta que mais pesa: quantas bolsas.
- **Corpo:**

> Olá, [nome],
>
> Enviei um e-mail na terça sobre as provas de bolsa da Pós-graduação e quero garantir que ele chegou até você. Os pontos principais:
>
> - Prova presencial em 27/11, sexta, das 9h às 13h.
> - Inscrição de R$ 100,00.
> - 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.
> - Nota de corte 7,0.
>
> [Botão] Ver a prova e me inscrever: [link_da_prova ou link_mestre]
>
> Equipe de relacionamento, Faculdade UFAPE

  Nota para o QA: a palavra "garantir" refere-se ao recebimento do e-mail, não a bolsa ou resultado. Se o QA preferir, trocar por "confirmar que ele chegou".
- **Chamada para ação:** "Ver a prova e me inscrever".
- **Follow-up:** nenhum (último toque do e-mail antes de M7).
- **Data e horário:** qui 05/11, 10h.
- **Opt-in:** consentimento de e-mail.
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.

#### M5. WhatsApp, lembrete de 06/11 (para quem não respondeu)

- **Canal:** WhatsApp
- **Objetivo (único):** levar quem não respondeu à página da prova.
- **Segmento:** quem recebeu M1 ou M3, não respondeu, não clicou e não se inscreveu.
- **Primeira linha A (teste):** [nome], sexta, 27/11, tem prova de bolsa da Pós-graduação.
- **Primeira linha B (teste):** [nome], ficou alguma dúvida sobre a prova de bolsa?
- Reserva: [nome], 11 bolsas por prova, inscrição de R$ 100,00.
- Reserva: Oi, [nome]. Posso te passar o link da prova de [área]?
- Reserva: [nome], a prova de bolsa de [área] é em 27/11.
- **Gancho:** retomar a conversa sem repetir tudo.
- **Corpo (texto do template):**

> Oi, [nome], é da Faculdade UFAPE de novo. Passando para lembrar da prova de bolsa da Pós-graduação: 27/11 (sexta), das 9h às 13h, com inscrição de R$ 100,00 e 11 bolsas por prova.
>
> Regras e inscrição: [link_da_prova ou link_vendas]
>
> Para não receber mais mensagens, responda SAIR.
- **Chamada para ação:** abrir o link.
- **Follow-up:** nenhum nesta etapa. Quem responde vai para o time de vendas; quem não responde recebe M9 em 24/11.
- **Data e horário:** sex 06/11, 10h.
- **Opt-in de WhatsApp confirmado:** só [opt_in_whatsapp] igual a sim.
- **Template aprovado pela Meta:** pb_lembrete_v1 [SUPOSIÇÃO de nome]; categoria marketing; variáveis {{1}} nome e botão de URL dinâmico {{2}}; botão "Sair". Submissão pendente.
- **Forma de sair:** "responda SAIR" e botão "Sair".

#### M7. E-mail, como funciona e dúvidas (10/11)

- **Canal:** e-mail
- **Objetivo (único):** responder às dúvidas mais comuns e levar à inscrição.
- **Segmento:** base com consentimento que ainda não se inscreveu.
- **Assunto A (teste):** [nome], 5 dúvidas sobre a prova de bolsa, respondidas
- **Assunto B (teste):** Quantas bolsas, qual a nota de corte e o que levar na prova
- Reserva: Prova de bolsa da Pós-graduação: como funciona, passo a passo
- Reserva: O que acontece depois da prova de bolsa
- Reserva: A prova é online? Dá para acumular a bolsa? Respostas
- **Texto de pré-visualização:** Passo a passo, da inscrição à matrícula, e as dúvidas mais comuns.
- **Gancho:** a dúvida comum que trava a inscrição.
- **Corpo:**

> Olá, [nome],
>
> Estas são as dúvidas mais comuns sobre a prova de bolsa da Pós-graduação.
>
> **Como funciona, em ordem**
> 1. Você se inscreve na prova da sua especialidade (R$ 100,00 à vista, no Pix ou boleto, ou 1x no cartão).
> 2. Faz a prova presencial em 27/11, das 9h às 13h.
> 3. Recebe o resultado por WhatsApp ou e-mail.
> 4. Tem 2 dias úteis para recurso.
> 5. Se for contemplado com bolsa, tem até 10 dias úteis para a matrícula.
>
> **Quantas bolsas há?** 11 por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.
>
> **Qual a nota de corte?** 7,0, o que equivale a 70% de acerto. Em caso de empate, análise de currículo.
>
> **A prova é online?** Não. É presencial, em São Paulo ou em Goiânia, conforme a especialidade.
>
> **Posso acumular a bolsa com outra condição?** Não. A bolsa não é acumulativa e é intransferível.
>
> **O que levo?** Documento com foto. Celular e relógio não são permitidos no dia da prova.
>
> [Botão] Escolher a minha prova: [link_mestre]
>
> Equipe de relacionamento, Faculdade UFAPE

  Perguntas sobre "para qual turma a bolsa vale" e "quanto custa a pós" não entram neste e-mail até a Ufape responder o destino (A-C2). Quando entrarem, usar a resposta 3 e a resposta 6 da seção 6, com condição completa.
- **Chamada para ação:** "Escolher a minha prova".
- **Follow-up (quem não abriu):** qui 12/11, 10h. Assunto: "[nome], 11 bolsas por prova, inscrição de R$ 100,00". Texto: "Olá, [nome]. Resumo da prova de bolsa da Pós-graduação: 27/11, das 9h às 13h, presencial, nota de corte 7,0. Regras e inscrição: [link_mestre]".
- **Data e horário:** ter 10/11, 10h.
- **Opt-in:** consentimento de e-mail.
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.

#### M8. E-mail, reta final (23/11)

- **Canal:** e-mail
- **Objetivo (único):** levar quem ainda não se inscreveu à inscrição, só com fatos da data.
- **Segmento:** base com consentimento que não se inscreveu. Só envia se a inscrição estiver aberta no catálogo no dia do envio. Se a Ufape informar prazo de inscrição, a data real entra no texto; sem ele, o texto não diz "inscrições até" [CONFIRMAR prazo].
- **Assunto A (teste):** A prova de bolsa da Pós-graduação é na sexta, 27/11
- **Assunto B (teste):** [nome], a prova de bolsa de [área] é na sexta
- Reserva: Prova de bolsa na sexta: horário, local e regras
- Reserva: Prova de bolsa em 27/11: R$ 100,00 e 11 bolsas por prova
- Reserva: [nome], sexta é a prova de bolsa. Veja as regras antes
- **Texto de pré-visualização:** Das 9h às 13h, presencial. Documento com foto, sem celular e relógio.
- **Gancho:** a data real da prova e o que levar.
- **Corpo:**

> Olá, [nome],
>
> A prova de bolsa para a Pós-graduação [em [área]] é na sexta-feira, 27 de novembro, das 9h às 13h, presencial em [praça].
>
> Se você ainda não se inscreveu, a inscrição é feita pela página da prova: R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão.
>
> O que vale saber:
> - 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%.
> - Nota de corte 7,0 (70% de acerto).
> - Leve documento com foto. Celular e relógio não são permitidos.
> - Resultado por WhatsApp ou e-mail, 2 dias úteis para recurso e 10 dias úteis para a matrícula.
>
> [Botão] Fazer a inscrição: [link_da_prova ou link_mestre]
>
> Equipe de relacionamento, Faculdade UFAPE

- **Chamada para ação:** "Fazer a inscrição".
- **Follow-up (quem não abriu):** qua 25/11, 10h. Assunto: "Prova de bolsa na sexta: horário, local e regras". Texto de duas linhas com data, horário, inscrição de R$ 100,00 e o link.
- **Data e horário:** seg 23/11, 10h (nenhuma mensagem de prova em 20 e 21/11).
- **Opt-in:** consentimento de e-mail.
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.

#### M9. WhatsApp, reta final (24/11)

- **Canal:** WhatsApp
- **Objetivo (único):** levar quem não se inscreveu à página da prova.
- **Segmento:** base com opt-in que não se inscreveu e não pediu para sair. Só envia com a inscrição aberta no catálogo.
- **Primeira linha A (teste):** [nome], a prova de bolsa de [área] é na sexta, 27/11.
- **Primeira linha B (teste):** [nome], alguma dúvida sobre a prova de bolsa de [área]?
- Reserva: [nome], sexta, das 9h às 13h: prova de bolsa da Pós-graduação.
- Reserva: [nome], posso te ajudar com a inscrição na prova de [área]?
- Reserva: [nome], 11 bolsas por prova, inscrição de R$ 100,00, sexta, 27/11.
- **Gancho:** a data real e a oferta de ajuda.
- **Corpo (texto do template):**

> Oi, [nome], é da Faculdade UFAPE. A prova de bolsa para a Pós-graduação em [área] é na sexta, 27/11, das 9h às 13h, presencial em [praça].
>
> Inscrição de R$ 100,00. 11 bolsas por prova, nota de corte 7,0. Leve documento com foto; celular e relógio não são permitidos.
>
> Regras e inscrição: [link_da_prova]
>
> Para não receber mais mensagens, responda SAIR.
- **Chamada para ação:** abrir o link.
- **Follow-up:** nenhum. Quem responde vai para o time de vendas.
- **Data e horário:** ter 24/11, 10h.
- **Opt-in de WhatsApp confirmado:** só [opt_in_whatsapp] igual a sim.
- **Template aprovado pela Meta:** pb_reta_final_v1 [SUPOSIÇÃO de nome]; categoria marketing; variáveis {{1}} nome, {{2}} área, {{3}} praça, botão de URL dinâmico {{4}}; botão "Sair". Submissão pendente.
- **Forma de sair:** "responda SAIR" e botão "Sair".

### 3.3 Confirmação de inscrição, com as regras

#### M10. E-mail, confirmação de inscrição

- **Canal:** e-mail (mensagem de serviço, não conta na cadência)
- **Objetivo (único):** confirmar a inscrição e deixar claras as regras do dia da prova.
- **Segmento:** inscrito com pagamento confirmado.
- **Assunto A (teste):** Inscrição confirmada: prova de bolsa de [área], 27/11
- **Assunto B (teste):** [nome], sua inscrição na prova de bolsa está confirmada
- Reserva: Prova de bolsa de [área]: horário, local e o que levar
- Reserva: Tudo certo com a sua inscrição. Veja as regras da prova
- Reserva: Sua inscrição na prova de [área] foi recebida
- **Texto de pré-visualização:** 27/11, das 9h às 13h. Leve documento com foto.
- **Gancho:** a confirmação com tudo o que a pessoa precisa no dia.
- **Corpo:**

> Olá, [nome],
>
> Recebemos a sua inscrição na prova de bolsa para a Pós-graduação em [área]. Guarde estas informações.
>
> - Data: sexta-feira, 27 de novembro de 2026.
> - Horário: das 9h às 13h.
> - Local: [endereço_da_prova].
> - Leve documento com foto.
> - Celular e relógio não são permitidos no dia da prova.
> - A prova tem questões de múltipla escolha e dissertativas. Nota de corte 7,0 (70% de acerto).
> - O resultado sai por WhatsApp ou e-mail. Depois dele, 2 dias úteis para recurso e 10 dias úteis para a matrícula, se houver bolsa.
> - A bolsa não é acumulativa e é intransferível.
>
> Se algum dado estiver errado, responda este e-mail com a correção.
>
> Equipe de relacionamento, Faculdade UFAPE
>
> Dúvidas sobre a prova: secretaria, (11) 97492-8443 (WhatsApp) ou duvidas@intercursos.com.br, de segunda a sexta, das 9h às 18h.

- **Chamada para ação:** responder com a correção, se algum dado estiver errado. Os contatos da secretaria no rodapé são informação institucional.
- **Follow-up:** M12 (véspera). Nenhum reenvio.
- **Data e horário:** imediato após o pagamento confirmado.
- **Opt-in:** consentimento de e-mail ou relação de serviço registrada [CONFIRMAR base legal com a Ufape].
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé (vale para mensagens de campanha; a de serviço segue a regra da Ufape [CONFIRMAR]).
- **Bloqueio:** prova de Goiânia só com [endereço_da_prova] confirmado. Prova de Felinos fora da régua.

#### M11. WhatsApp, confirmação de inscrição

- **Canal:** WhatsApp (mensagem de serviço)
- **Objetivo (único):** confirmar a inscrição e as regras do dia da prova.
- **Segmento:** inscrito com opt-in de WhatsApp.
- **Primeira linha A (teste):** [nome], sua inscrição na prova de bolsa de [área] está confirmada.
- **Primeira linha B (teste):** Oi, [nome]. Recebemos sua inscrição na prova de [área].
- Reserva: [nome], prova de bolsa em 27/11, das 9h às 13h. Inscrição confirmada.
- Reserva: [nome], tudo certo com sua inscrição. Veja o que levar.
- Reserva: [nome], guarde estas informações da prova de [área].
- **Gancho:** a pessoa acabou de pagar e quer saber se deu certo.
- **Corpo (texto do template):**

> Oi, [nome], aqui é da Faculdade UFAPE. Sua inscrição na prova de bolsa para a Pós-graduação em [área] está confirmada.
>
> Sexta, 27/11, das 9h às 13h.
> Local: [endereço_da_prova].
> Leve documento com foto. Celular e relógio não são permitidos.
>
> O resultado sai por WhatsApp ou e-mail. Depois dele, 2 dias úteis para recurso e 10 dias úteis para a matrícula, se houver bolsa.
>
> Se algum dado estiver errado, responda esta mensagem.
- **Chamada para ação:** responder se algum dado estiver errado.
- **Follow-up:** M13 (véspera).
- **Data e horário:** logo após o pagamento, dentro da janela comercial. Pagamento fora da janela: o e-mail M10 vai na hora e este WhatsApp espera abrir.
- **Opt-in de WhatsApp confirmado:** [opt_in_whatsapp] igual a sim. Inscrito sem opt-in recebe só o e-mail.
- **Template aprovado pela Meta:** pb_confirmacao_inscricao_v1 [SUPOSIÇÃO de nome]; categoria de utilidade, a Meta decide a classificação; variáveis {{1}} nome, {{2}} área, {{3}} endereço da prova. Submissão pendente.
- **Forma de sair:** "responda SAIR para parar de receber mensagens que não sejam sobre a sua prova" [CONFIRMAR com a Ufape o alcance da saída em mensagem de serviço].
- **Bloqueio:** mesmo de M10.

### 3.4 Véspera e dia da prova

#### M12. E-mail, véspera

- **Canal:** e-mail (serviço)
- **Objetivo (único):** fazer o inscrito confirmar presença.
- **Segmento:** inscrito.
- **Assunto A (teste):** [nome], amanhã é a prova de bolsa de [área]
- **Assunto B (teste):** Prova de bolsa amanhã: horário, local e o que levar
- Reserva: Amanhã, das 9h às 13h: prova de bolsa
- Reserva: [nome], confirme sua presença na prova de amanhã
- Reserva: Checklist da prova de bolsa de amanhã
- **Texto de pré-visualização:** Das 9h às 13h. Documento com foto, sem celular e relógio.
- **Gancho:** a lista do que levar, na véspera.
- **Corpo:**

> Olá, [nome],
>
> Amanhã, sexta-feira, 27/11, é a sua prova de bolsa para a Pós-graduação em [área].
>
> - Horário: das 9h às 13h.
> - Local: [endereço_da_prova].
> - Leve documento com foto.
> - Celular e relógio não são permitidos no dia da prova.
> - Planeje a chegada com folga.
>
> Para confirmarmos sua presença, responda este e-mail com a palavra SIM.
>
> Boa prova.
>
> Equipe de relacionamento, Faculdade UFAPE

- **Chamada para ação:** responder SIM.
- **Follow-up:** M14 (dia da prova).
- **Data e horário:** qui 26/11, 10h.
- **Opt-in:** consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.
- Nota: a hora limite de entrada no local não está publicada [CONFIRMAR tolerância de atraso]. O texto não inventa horário de chegada.

#### M13. WhatsApp, véspera

- **Canal:** WhatsApp (serviço)
- **Objetivo (único):** fazer o inscrito confirmar presença.
- **Segmento:** inscrito com opt-in de WhatsApp.
- **Primeira linha A (teste):** [nome], amanhã é a sua prova de bolsa, das 9h às 13h.
- **Primeira linha B (teste):** [nome], você vai à prova de bolsa de amanhã?
- Reserva: [nome], prova de bolsa amanhã. Veja o que levar.
- Reserva: Oi, [nome]. Lembrete da prova de [área]: amanhã, 27/11.
- Reserva: [nome], checklist da prova de amanhã.
- **Gancho:** lembrete útil, com pergunta simples.
- **Corpo (texto do template):**

> Oi, [nome], aqui é da Faculdade UFAPE. Amanhã, sexta, 27/11, é a sua prova de bolsa para a Pós-graduação em [área].
>
> Das 9h às 13h, em [endereço_da_prova].
> Leve documento com foto. Celular e relógio não são permitidos.
>
> Você vai? Responda SIM para confirmar.
- **Chamada para ação:** responder SIM.
- **Follow-up:** M15 (dia da prova). Quem responde NÃO ou pergunta sobre ausência vai para o time de vendas, sem promessa de reembolso (resposta 11 da seção 6).
- **Data e horário:** qui 26/11, 14h.
- **Opt-in de WhatsApp confirmado:** [opt_in_whatsapp] igual a sim.
- **Template aprovado pela Meta:** pb_vespera_v1 [SUPOSIÇÃO de nome]; categoria de utilidade (a Meta decide); variáveis {{1}} nome, {{2}} área, {{3}} endereço; botão de resposta rápida "Sim, vou". Submissão pendente.
- **Forma de sair:** "responda SAIR" para parar de receber mensagens de campanha [CONFIRMAR alcance].

#### M14. E-mail, dia da prova

- **Canal:** e-mail (serviço)
- **Objetivo (único):** lembrar horário, local e regras no dia.
- **Segmento:** inscrito.
- **Assunto A (teste):** Hoje é a prova de bolsa: das 9h às 13h
- **Assunto B (teste):** [nome], boa prova hoje
- Reserva: Prova de bolsa de [área] hoje, 27/11
- Reserva: Hoje, das 9h às 13h: documento com foto e sem celular
- Reserva: [nome], hoje é o dia. Local e regras
- **Texto de pré-visualização:** Local, horário e o que levar.
- **Gancho:** o essencial, em poucas linhas, antes de sair de casa.
- **Corpo:**

> Olá, [nome],
>
> Hoje é a prova de bolsa para a Pós-graduação em [área].
>
> - Das 9h às 13h.
> - Local: [endereço_da_prova].
> - Documento com foto.
> - Celular e relógio não são permitidos.
>
> Se algo impedir a sua chegada, responda este e-mail agora.
>
> Boa prova.
>
> Equipe de relacionamento, Faculdade UFAPE

- **Chamada para ação:** responder se algo impedir a chegada.
- **Follow-up:** nenhum.
- **Data e horário:** sex 27/11, 7h [CONFIRMAR horário de envio].
- **Opt-in:** consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.

#### M15. WhatsApp, dia da prova

- **Canal:** WhatsApp (serviço)
- **Objetivo (único):** lembrar horário, local e regras no dia.
- **Segmento:** inscrito com opt-in. Só envia se a Ufape aprovar janela de WhatsApp a partir das 8h; sem essa aprovação, o dia da prova fica só no e-mail M14 e a véspera M13 cobre o WhatsApp [SUPOSIÇÃO de conflito com o horário comercial das 9h].
- **Primeira linha A (teste):** [nome], hoje é a prova de bolsa. Das 9h às 13h.
- **Primeira linha B (teste):** Boa prova hoje, [nome].
- Reserva: [nome], prova de bolsa hoje. Documento com foto.
- Reserva: [nome], hoje, em [endereço_da_prova], das 9h às 13h.
- Reserva: [nome], lembrete rápido da prova de hoje.
- **Gancho:** o essencial do dia.
- **Corpo (texto do template):**

> Oi, [nome], hoje é a sua prova de bolsa para a Pós-graduação em [área].
>
> Das 9h às 13h, em [endereço_da_prova]. Documento com foto. Celular e relógio não são permitidos.
>
> Se algo impedir a sua chegada, responda esta mensagem. Boa prova.
- **Chamada para ação:** responder se algo impedir a chegada.
- **Follow-up:** nenhum.
- **Data e horário:** sex 27/11, 8h, com a condição acima.
- **Opt-in de WhatsApp confirmado:** [opt_in_whatsapp] igual a sim.
- **Template aprovado pela Meta:** pb_dia_prova_v1 [SUPOSIÇÃO de nome]; categoria de utilidade (a Meta decide); variáveis {{1}} nome, {{2}} área, {{3}} endereço. Submissão pendente.
- **Forma de sair:** "responda SAIR" [CONFIRMAR alcance].

### 3.5 Pós-prova

Regras comuns de M16 a M20: a data da divulgação do resultado, o canal do recurso e o calendário de dias úteis são da Ufape [CONFIRMAR]. A Ufape informa o resultado, o texto só o comunica. As mensagens nunca citam valor com bolsa aplicada; o time de vendas informa, com todas as condições. Nenhuma promete vaga, matrícula, aprovação futura ou emprego. [turma_de_destino] só entra depois de A-C2; antes, a frase alternativa é "O time de matrícula confirma com você a turma de destino na conversa".

Assuntos do e-mail de resultado (a família serve para M17, M18, M19 e M20; o assunto não revela o resultado para não expor a pessoa em notificação). Como a abertura é de alta intenção, não precisa de teste A e B; os dois primeiros ficam como padrão e reserva.

- **Assunto A:** [nome], o resultado da prova de bolsa de [área] está disponível
- **Assunto B:** Resultado da prova de bolsa da Pós-graduação em [área]
- Reserva: [nome], seu resultado e os próximos passos
- Reserva: Prova de bolsa de [área]: resultado e prazos
- Reserva: [nome], leia o resultado da sua prova de bolsa

#### M16. WhatsApp, resultado: aprovado com bolsa

- **Canal:** WhatsApp (serviço)
- **Objetivo (único):** levar o aprovado com bolsa à conversa de matrícula dentro do prazo.
- **Segmento:** [resultado] igual a aprovado_com_bolsa.
- **Primeira linha A (teste):** [nome], o resultado da prova de bolsa de [área] está disponível.
- **Primeira linha B (teste):** [nome], saiu o resultado da sua prova de [área].
- Reserva: [nome], resultado da prova de bolsa e prazos de matrícula.
- Reserva: Oi, [nome]. Seu resultado da prova de [área] chegou.
- Reserva: [nome], leia o resultado da sua prova de bolsa.
- **Gancho:** o resultado e o prazo.
- **Corpo (texto do template):**

> Oi, [nome], aqui é da Faculdade UFAPE. O resultado da sua prova de bolsa para a Pós-graduação em [área] saiu.
>
> Sua nota: [nota]. Bolsa: [percentual_da_bolsa].
>
> Prazos: 2 dias úteis para recurso (até [data_limite_recurso]) e 10 dias úteis para a matrícula com a bolsa (até [data_limite_matrícula]). A bolsa não é acumulativa e é intransferível.
>
> [Turma: [turma_de_destino], ou, sem destino confirmado: O time de matrícula confirma com você a turma de destino na conversa.]
>
> O time de matrícula explica as condições completas e o valor com a bolsa aplicada. Fale com ele aqui: [link_vendas]
- **Chamada para ação:** falar com o time de matrícula (um link).
- **Follow-up:** no 7º dia útil do prazo, para quem não matriculou: "[nome], o prazo da matrícula com bolsa termina em [data_limite_matrícula]. O time de matrícula está por aqui para as suas dúvidas: [link_vendas]." A data é real e vem do calendário da Ufape.
- **Data e horário:** dia da divulgação [CONFIRMAR], em horário comercial.
- **Opt-in de WhatsApp confirmado:** [opt_in_whatsapp] igual a sim. Sem opt-in, só e-mail (M17).
- **Template aprovado pela Meta:** pb_resultado_com_bolsa_v1 [SUPOSIÇÃO de nome]; categoria de utilidade (a Meta decide); variáveis {{1}} nome, {{2}} área, {{3}} nota, {{4}} percentual, {{5}} data limite do recurso, {{6}} data limite da matrícula, botão de URL dinâmico {{7}} para o WhatsApp de vendas. Submissão pendente.
- **Forma de sair:** "responda SAIR" [CONFIRMAR alcance].

#### M17. E-mail, resultado: aprovado com bolsa

- **Canal:** e-mail (serviço)
- **Objetivo (único):** levar o aprovado com bolsa à conversa de matrícula dentro do prazo.
- **Segmento:** [resultado] igual a aprovado_com_bolsa.
- **Assunto A e B:** família de assuntos do início da seção 3.5.
- **Texto de pré-visualização:** Resultado, prazos de recurso e de matrícula.
- **Gancho:** o resultado e o prazo.
- **Corpo:**

> Olá, [nome],
>
> O resultado da sua prova de bolsa para a Pós-graduação em [área] saiu.
>
> - Sua nota: [nota].
> - Bolsa: [percentual_da_bolsa].
> - Recurso: até [data_limite_recurso] (2 dias úteis após a divulgação). Como pedir: [canal_de_recurso].
> - Matrícula com a bolsa: até [data_limite_matrícula] (10 dias úteis após a divulgação).
> - A bolsa não é acumulativa e é intransferível.
>
> [Turma: [turma_de_destino], com [condição_da_turma], ou, sem destino confirmado: O time de matrícula confirma com você a turma de destino na conversa.]
>
> O time de matrícula explica as condições completas e o valor com a bolsa aplicada.
>
> [Botão] Falar com o time de matrícula: [link_vendas]
>
> Equipe de relacionamento, Faculdade UFAPE

- **Chamada para ação:** "Falar com o time de matrícula".
- **Follow-up:** no 7º dia útil do prazo, a mesma lógica de M16, por e-mail, com o assunto "Matrícula com bolsa: o prazo termina em [data_limite_matrícula]".
- **Data e horário:** dia da divulgação [CONFIRMAR].
- **Opt-in:** consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** não se aplica.
- **Forma de sair:** descadastro no rodapé.

#### M18. WhatsApp e e-mail, resultado: aprovado sem bolsa (bloqueado até a regra)

- **Canal:** WhatsApp e e-mail (serviço)
- **Objetivo (único):** levar o contato à conversa sobre as condições da turma.
- **Segmento:** [resultado] igual a aprovado_sem_bolsa (atingiu a nota de corte e não recebeu uma das 11 bolsas).
- **Bloqueio:** não enviar até a Ufape responder: critério de distribuição das 11 bolsas, se o aprovado sem bolsa pode se matricular e em que condição, e se há lista de espera [CONFIRMAR]. Os blocos entre colchetes são preenchidos com a regra oficial, sem improviso.
- **Primeira linha A (teste):** [nome], o resultado da prova de bolsa de [área] está disponível.
- **Primeira linha B (teste):** [nome], saiu o resultado da sua prova de [área].
- Reserva: [nome], seu resultado e os próximos passos.
- Reserva: Oi, [nome]. Resultado da prova de bolsa de [área].
- Reserva: [nome], leia o resultado da sua prova.
- **Corpo (WhatsApp e e-mail, mesmo texto):**

> Oi, [nome], aqui é da Faculdade UFAPE. O resultado da sua prova de bolsa para a Pós-graduação em [área] saiu.
>
> Sua nota: [nota]. Você atingiu a nota de corte de 7,0. [regra_oficial_da_distribuição_das_bolsas].
>
> Prazo de recurso: 2 dias úteis após a divulgação, até [data_limite_recurso]. Como pedir: [canal_de_recurso].
>
> [regra_oficial_para_aprovado_sem_bolsa: se pode matricular, com que condição e até quando]
>
> Se quiser conhecer as condições da turma, o time de vendas explica por aqui: [link_vendas]
- **Chamada para ação:** falar com o time de vendas.
- **Follow-up:** nenhum automático. Quem responde vai para o time de vendas.
- **Data e horário:** dia da divulgação [CONFIRMAR].
- **Opt-in:** WhatsApp só com [opt_in_whatsapp] igual a sim; e-mail com consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** pb_resultado_sem_bolsa_v1 [SUPOSIÇÃO de nome]; utilidade (a Meta decide); variáveis {{1}} nome, {{2}} área, {{3}} nota, {{4}} data limite do recurso e dois blocos de regra preenchidos pela Ufape (ou um template por regra aprovada). Submissão só depois da regra.
- **Forma de sair:** "responda SAIR" no WhatsApp; descadastro no e-mail.

#### M19. WhatsApp e e-mail, resultado: não atingiu a nota de corte

- **Canal:** WhatsApp e e-mail (serviço)
- **Objetivo (único):** oferecer a conversa sobre as condições normais da turma, sem pressão.
- **Segmento:** [resultado] igual a nao_atingiu.
- **Primeira linha A (teste):** [nome], o resultado da prova de bolsa de [área] está disponível.
- **Primeira linha B (teste):** [nome], obrigado por fazer a prova de bolsa de [área].
- Reserva: [nome], seu resultado e os próximos passos.
- Reserva: Oi, [nome]. Resultado da prova de [área].
- Reserva: [nome], leia o resultado da sua prova.
- **Gancho:** respeito ao esforço, informação clara e sem pressão.
- **Corpo (WhatsApp e e-mail, mesmo texto):**

> Oi, [nome], aqui é da Faculdade UFAPE. Obrigado por fazer a prova de bolsa para a Pós-graduação em [área].
>
> Sua nota foi [nota], abaixo da nota de corte de 7,0, então não houve bolsa desta vez. Se quiser pedir recurso, o prazo é de 2 dias úteis após a divulgação, até [data_limite_recurso]. Como pedir: [canal_de_recurso].
>
> A Pós-graduação em [área] segue com as condições normais da turma, sem pressa de decisão. Se quiser conhecê-las, responda TURMA e o time de vendas conversa com você.
- **Chamada para ação:** responder TURMA (conversa com vendas, sem link).
- **Follow-up:** nenhum. Sem insistência: quem não responde sai da régua.
- **Data e horário:** dia da divulgação [CONFIRMAR].
- **Opt-in:** WhatsApp só com [opt_in_whatsapp] igual a sim; e-mail com consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** pb_resultado_nao_atingiu_v1 [SUPOSIÇÃO de nome]; utilidade (a Meta decide); variáveis {{1}} nome, {{2}} área, {{3}} nota, {{4}} data limite do recurso, {{5}} canal do recurso; botão de resposta rápida "Turma". Submissão pendente.
- **Forma de sair:** "responda SAIR" no WhatsApp; descadastro no e-mail.
- Nota: a frase "sem pressa de decisão" só vale se a turma de destino tiver data de matrícula que permita; se a turma estiver perto de fechar, o time ajusta na conversa com data real [CONFIRMAR].

#### M20. WhatsApp e e-mail, ausente

- **Canal:** WhatsApp e e-mail (serviço)
- **Objetivo (único):** oferecer a conversa sobre as condições normais da turma, sem cobrança.
- **Segmento:** [resultado] igual a ausente (inscrito que não compareceu).
- **Bloqueio:** a política de ausência, de reembolso da inscrição e de nova prova não está publicada [CONFIRMAR]. O texto não promete devolução nem nova chance.
- **Primeira linha A (teste):** [nome], sentimos sua falta na prova de bolsa de [área].
- **Primeira linha B (teste):** [nome], sobre a prova de bolsa de [área] de ontem.
- Reserva: [nome], uma mensagem sobre a sua inscrição na prova.
- Reserva: Oi, [nome]. Registramos que você não pôde fazer a prova.
- Reserva: [nome], se ainda quer a Pós-graduação em [área], vale conversar.
- **Corpo (WhatsApp e e-mail, mesmo texto):**

> Oi, [nome], aqui é da Faculdade UFAPE. Registramos que você não compareceu à prova de bolsa para a Pós-graduação em [área]. Imprevistos acontecem.
>
> Se a Pós-graduação em [área] ainda faz sentido para você, o time de vendas explica as condições normais da turma, sem compromisso. Responda TURMA e ele conversa com você.
>
> [regra_oficial_de_ausência, se a Ufape aprovar um texto]
- **Chamada para ação:** responder TURMA.
- **Follow-up:** nenhum.
- **Data e horário:** primeiro dia útil depois da prova (seg 30/11), 10h [CONFIRMAR política].
- **Opt-in:** WhatsApp só com [opt_in_whatsapp] igual a sim; e-mail com consentimento ou relação de serviço [CONFIRMAR].
- **Template Meta:** pb_ausente_v1 [SUPOSIÇÃO de nome]; marketing ou utilidade conforme a Meta decidir; variáveis {{1}} nome, {{2}} área; botão "Turma". Submissão pendente.
- **Forma de sair:** "responda SAIR" no WhatsApp; descadastro no e-mail.

### 3.6 Registro de testes (a preencher depois dos envios)

| Mensagem | Variante A | Variante B | Métrica | Resultado | Decisão |
|---|---|---|---|---|---|
| M1 | quantas bolsas, 11 | qual especialidade | respostas | [preencher] | [preencher] |
| M2 | 11 bolsas, R$ 100,00 | prova é em 27/11 | abertura e clique | [preencher] | [preencher] |
| M3 | R$ 100,00 e 11 bolsas | você quer [área]? | cliques e respostas | [preencher] | [preencher] |
| M4 | 11 bolsas, R$ 100,00 | prova de [área] em 27/11 | abertura e clique | [preencher] | [preencher] |
| M5 | sexta tem prova | ficou dúvida? | cliques e respostas | [preencher] | [preencher] |
| M6 | quantas bolsas | o que saber em 1 minuto | abertura e clique | [preencher] | [preencher] |
| M7 | 5 dúvidas | quantas bolsas e nota | abertura e clique | [preencher] | [preencher] |
| M8 | prova na sexta | prova de [área] na sexta | abertura e clique | [preencher] | [preencher] |
| M9 | prova na sexta | alguma dúvida? | cliques e respostas | [preencher] | [preencher] |
| M10 a M15 | serviço: testar só presença (SIM em M12 e M13) | | taxa de resposta SIM e comparecimento | [preencher] | [preencher] |
| M16 a M20 | sem teste A e B (alta intenção) | | respostas, matrículas | [preencher] | [preencher] |

Sempre medir clique, resposta, inscrição e matrícula, não só abertura e leitura. Cada variante vai para metade do segmento, no mesmo horário.

---

## 4. Variações por área (para M3 e M4)

A versão por área troca [área], [praça], [link_da_prova] e a [frase_da_área]. A frase é hipótese de rotina [SUPOSIÇÃO], a validar com as conversas do WhatsApp de vendas que ainda não chegaram. Não é fala de aluno e não vira depoimento.

**Regra de liberação (estratégia de campanha, seções 3.2 e 3.4):** só as provas em D1 recebem a versão por área. D2, D3 e D4 entram apenas na lista da versão mestre (e só as que a Ufape confirmar). Provas de Goiânia só depois da correção do local; a Cardiologia de Goiânia também depois da correção dos links.

| Prova | [área] (nome no CRM) | Praça | Situação | Versão por área | [frase_da_área] (hipótese) |
|---|---|---|---|---|---|
| 68645 | Clínica Médica e Emergência Veterinária | São Paulo | D1 | Liberada | Se o paciente crítico do plantão é o que você quer dominar, esta prova é um caminho. |
| 68648 | Endocrinologia de Pequenos Animais | São Paulo | D1 | Liberada | Se o paciente endócrino que exige acompanhamento de longo prazo faz parte da sua rotina, vale conhecer esta prova. |
| 68654 | Neurologia e Neurocirurgia Veterinária | São Paulo | D1 | Liberada, sem juntar com o Workshop de Neuromonitorização | Se você quer conduzir os casos neurológicos que hoje encaminha, esta prova pode ser o primeiro passo. |
| 68657 | Oncologia Veterinária | São Paulo | D1 | Liberada | Se você quer conduzir o paciente oncológico com protocolo e segurança, esta prova abre o caminho. |
| 68658 | Patologia Clínica Veterinária | São Paulo | D1 | Liberada | Se você quer fechar o caso sem depender do laboratório ou do colega, esta prova pode ajudar na decisão. |
| 68659 | Pneumologia Veterinária | São Paulo | D1 | Liberada | Se o paciente com doença respiratória é o que você quer aprofundar, esta prova é uma porta de entrada. |
| 68661 | Ultrassonografia em Pequenos Animais | São Paulo | D1 | Liberada | Se você quer fazer o exame de imagem na sua própria clínica, esta prova é uma porta de entrada. |
| 68640 | Anestesiologia Veterinária | Goiânia | D1 | Bloqueada: local de Goiânia | Se a segurança do protocolo anestésico na rotina é o que você quer aprofundar, esta prova pode ajudar. |
| 68642 | Cardiologia Veterinária | Goiânia | D1 | Bloqueada: local de Goiânia e links invertidos | Se o paciente cardiopata faz parte da sua rotina e você quer dominá-lo, esta prova é um caminho. |
| 68644 | Clínica Cirúrgica de Cães e Gatos | Goiânia | D1 | Bloqueada: local de Goiânia | Se você quer operar na própria clínica com mais segurança, esta prova é um caminho. |
| 68646 | Dermatologia Veterinária | São Paulo | D2 | Só mestre (destino: turma começa em 28/11, A-C2) | - |
| 68651 | Hematologia Veterinária | São Paulo | D2 | Só mestre (destino: turma começa em 28/11, A-C2) | - |
| 68647 | Diagnóstico por Imagem | São Paulo | D2 | Só mestre (destino a decidir, A-C2) | - |
| 68650 | Gastroenterologia Veterinária | São Paulo | D2 | Só mestre (turma de 07/11 começa antes da prova, A-C2) | - |
| 68639 | Anestesiologia Veterinária | São Paulo | D3 | Só mestre (destino a decidir, A-C2) | - |
| 68641 | Cardiologia Veterinária | São Paulo | D3 | Só mestre (sem turma de Cardiologia futura em SP; links invertidos) | - |
| 68660 | Terapia Intensiva Veterinária | São Paulo | D3 | Só mestre (destino a decidir, A-C2) | - |
| 68643 | Clínica Cirúrgica de Cães e Gatos | São Paulo | D3 | Só mestre (destino a decidir, A-C2) | - |
| 68652 | Medicina de Felinos | São Paulo | D4 | Fora da mensagem até confirmar [CONFIRMAR destino]; página com regras contraditórias e frase de certificação | - |
| 68649 | Endoscopia Veterinária | São Paulo | D4 | Fora da mensagem até confirmar [CONFIRMAR destino] | - |
| 68653 | Nefrologia e Urologia Veterinária | São Paulo | D4 | Fora da mensagem até confirmar [CONFIRMAR destino] | - |
| 68655 | Odontologia Veterinária | São Paulo | D4 | Fora da mensagem até confirmar [CONFIRMAR destino] | - |

Oftalmologia (68656) não tem prova: fora da campanha. Nenhuma mensagem cita Oftalmologia como prova.

Total conferido: 10 em D1, 4 em D2, 4 em D3 e 4 em D4, igual a 22.

Cadência de Neurologia: o público fala também com o Workshop de Neuromonitorização (20 e 21/11, linha Eventos). Não juntar as duas ofertas na mesma mensagem e respeitar o limite semanal somado.

---

## 5. Destino provável por prova (consulta interna, não é texto de mensagem)

Fonte: catálogo, seção 2, na leitura da estratégia de campanha. É leitura da squad a partir do catálogo: o destino real de cada prova é da Ufape (A-C2). Nenhuma mensagem de convite usa esta tabela. O [condição_da_turma] só é liberado depois da confirmação. Preços são os do site em 26/10/2026, todos no cartão ou boleto, com matrícula de R$ 250,00 salvo onde indicado.

| Prova | Turma candidata (catálogo) | Início | CH | Modalidade | Condição completa do catálogo |
|---|---|---|---|---|---|
| 68640 Anestesiologia, Goiânia | 68609 Pós-graduação em Anestesiologia Veterinária, turma VIII | 24/04/2027 | 500 h | Semipresencial | 30x de R$ 1.081,67; total R$ 32.450,00; matrícula R$ 250,00 |
| 68642 Cardiologia, Goiânia | 289 Pós-graduação em Cardiologia Veterinária, turma II | 20/03/2027 | 500 h | Semipresencial | 30x de R$ 1.180,00; total R$ 35.400,00; matrícula R$ 250,00 |
| 68644 Clínica Cirúrgica, Goiânia | 68632 Pós-graduação em Clínica Cirúrgica de Cães e Gatos, turma V | 10/04/2027 | 500 h | Presencial | 30x de R$ 1.100,00; total R$ 33.000,00; matrícula R$ 250,00 |
| 68645 Clínica Médica e Emergência, SP | 68635 Pós-graduação em Clínica Médica e Emergência de Pequenos Animais, turma V | 10/04/2027 | 750 h | Semipresencial | 30x de R$ 1.100,00; total R$ 33.000,00; matrícula R$ 250,00 |
| 68648 Endocrinologia, SP | 68617 Pós-graduação em Endocrinologia de Pequenos Animais (turma diverge entre planilha e site: citar sem número de turma) | 17/04/2027 | 500 h | Semipresencial | 30x de R$ 1.200,00; total R$ 36.000,00; matrícula R$ 250,00 |
| 68654 Neurologia, SP | 68616 Pós-graduação em Neurologia e Neurocirurgia Veterinária, turma IX | 08/05/2027 | 500 h | Semipresencial | 30x de R$ 1.192,40; total R$ 35.772,00; matrícula R$ 250,00 |
| 68657 Oncologia, SP | 68628 Pós-graduação em Oncologia Veterinária (turma diverge: citar sem número de turma) | 10/04/2027 | 500 h | Semipresencial | 30x de R$ 1.298,00; total R$ 38.940,00; matrícula R$ 250,00 |
| 68658 Patologia Clínica, SP | 68615 Pós-graduação em Patologia Clínica, turma VII | 20/03/2027 | 500 h | Semipresencial | 30x de R$ 1.180,00; total R$ 35.400,00; matrícula R$ 250,00 |
| 68659 Pneumologia, SP | 68636 Pós-graduação em Pneumologia Veterinária, turma VIII (fonte só no site: data [CONFIRMAR] com a planilha) | 17/04/2027 | 500 h | Semipresencial | 30x de R$ 1.265,00; total R$ 37.950,00; matrícula R$ 250,00 |
| 68661 Ultrassonografia, SP | 68629 Pós Graduação em Ultrassonografia de Pequenos Animais, turma III (fonte só no site: data [CONFIRMAR] com a planilha) | 22/05/2027 | 360 h | Semipresencial | 24x de R$ 685,67; total R$ 16.456,00; matrícula R$ 350,00 |
| 68646 Dermatologia, SP | 68610 começa em 28/11/2026, um dia depois da prova: [CONFIRMAR destino] | 28/11/2026 | 500 h | Semipresencial | A decisão de A-C2 vem antes de qualquer citação |
| 68651 Hematologia, SP | 68608 começa em 28/11/2026, um dia depois da prova: [CONFIRMAR destino] | 28/11/2026 | 500 h | Semipresencial | A decisão de A-C2 vem antes de qualquer citação |
| 68647 Diagnóstico por Imagem, SP | 68604 começa em 31/10/2026, antes da prova; 68611 sem data: [CONFIRMAR destino] | - | - | - | - |
| 68650 Gastroenterologia, SP | 68606 começa em 07/11/2026, antes da prova: [CONFIRMAR destino] | - | - | - | - |
| 68639 Anestesiologia, SP | Sem Anestesiologia Veterinária aberta em SP; 657 e 359 são outros cursos e a 359 tem pré-requisito: [CONFIRMAR destino] | - | - | - | - |
| 68641 Cardiologia, SP | Sem Cardiologia aberta em SP: [CONFIRMAR destino] | - | - | - | - |
| 68660 Terapia Intensiva, SP | Só a 68623, em Goiânia: [CONFIRMAR destino] | - | - | - | - |
| 68643 Clínica Cirúrgica, SP | Sem turma aberta em SP: [CONFIRMAR destino] | - | - | - | - |
| 68652 Medicina de Felinos, SP | Sem turma aberta: [CONFIRMAR destino] | - | - | - | - |
| 68649 Endoscopia, SP | Sem turma aberta: [CONFIRMAR destino] | - | - | - | - |
| 68653 Nefrologia e Urologia, SP | Sem turma aberta: [CONFIRMAR destino] | - | - | - | - |
| 68655 Odontologia, SP | Sem turma aberta: [CONFIRMAR destino] | - | - | - | - |

---

## 6. Respostas prontas para o time de vendas

Para uso em conversa no WhatsApp de vendas (São Paulo: (11) 91366-9290; Goiânia: (62) 9420-1847) e por e-mail. Não é envio em massa. Tom de colega para colega, frases curtas. Cada resposta traz a fonte e o cuidado. Regras do time: não prometer bolsa, aprovação, vaga, emprego ou renda; não calcular valor de curso com bolsa; não comentar outra instituição; não dizer que "restam poucas vagas" (não há número de vagas restantes no catálogo); não afirmar nada sobre certificação.

**Resposta 1. Quantas bolsas tem?**
> "São 11 bolsas por prova: 2 de 50% (com monitoria), 4 de 25% e 5 de 10%. Cada especialidade tem a sua prova, com as mesmas regras."

Fonte: contexto/pos-graduacao.md e fichas das provas. Cuidado: nunca dizer "bolsa de 50%" sem a distribuição completa; não dizer "garantida". O que a monitoria exige e a ordem de distribuição das 11 bolsas: [CONFIRMAR]. Se perguntarem, diga que vai confirmar.

**Resposta 2. Qual a nota?**
> "A nota de corte é 7,0, que equivale a 70% de acerto. A prova tem questões de múltipla escolha e dissertativas. Em caso de empate, a Ufape faz análise de currículo."

Fonte: contexto/pos-graduacao.md e ficha 68639. Cuidado: dizer "nota de corte" e não "nota para passar com bolsa". O que acontece com quem atinge 7,0 e fica sem bolsa: [CONFIRMAR] (ver M18). Não responder por conta própria.

**Resposta 3. A bolsa serve para qual turma?**
> Enquanto a Ufape não confirmar o destino: "Boa pergunta. Vou confirmar com a coordenação para qual turma a bolsa da prova de [área] vale e já te respondo."
>
> Depois da confirmação (D1): "A bolsa da prova de [área] vale para a Pós-graduação em [área], [praça], turma com início em [data]. A condição da turma é: [parcelas]x de R$ [valor da parcela], total de R$ [total], matrícula de R$ [matrícula]."

Fonte: nenhuma página traz o destino. A tabela da seção 5 é leitura da squad, não resposta oficial. Cuidado por situação: D1, só depois da confirmação; D2 (Dermatologia e Hematologia, turmas que começam em 28/11, e Imagem e Gastroenterologia, turmas que começam antes da prova), D3 e D4: não indicar turma e não sugerir esperar a prova para entrar com bolsa; encaminhar a pergunta à pessoa do marketing (A-C2).

**Resposta 4. Posso acumular a bolsa com outro desconto?**
> "Não. A bolsa da prova não é acumulativa e é intransferível: não soma com outra condição e não passa para outra pessoa. Se você tem outra condição, como desconto de ex-aluno, eu confirmo qual vale para o seu caso antes de você decidir."

Fonte: ficha 68639 e contexto. Cuidado: a regra do desconto de ex-aluno está em [PREENCHER] em contexto/ufape-geral.md; não explicar o desconto até a Ufape escrever. Promoções de turma (por exemplo, a de 20% da Pós-graduação em Medicina Interna Equina) não se combinam com a bolsa.

**Resposta 5. A prova é online? E a pós?**
> "A prova é presencial, em São Paulo ou em Goiânia, conforme a especialidade: sexta, 27/11, das 9h às 13h. A página não tem versão online. A maioria das turmas de pós é semipresencial: um módulo por mês, em fim de semana, com aulas online e módulos práticos presenciais obrigatórios. A Pós-graduação em Clínica Cirúrgica de Cães e Gatos de Goiânia é presencial."

Fonte: catálogo (seções 2 e 3), contexto/pos-graduacao.md. Cuidado: não oferecer EAD (a turma EAD está em "verificar" no catálogo e não pode ser divulgada).

**Resposta 6. Quanto custa a pós?**
> "Depende da turma. Para a [turma], o investimento é [parcelas]x de R$ [valor], total de R$ [total], mais matrícula de R$ [matrícula]. O valor com a bolsa aplicada não calculo por mensagem: o time de matrícula informa com todas as condições quando o resultado sair."
>
> A inscrição na prova custa R$ 100,00, à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão.

Fonte: catálogo, seção 2 (valores por turma na seção 5 deste arquivo). Cuidado: citar o valor da turma só depois de confirmado o destino e sempre com parcelas, valor da parcela, total e matrícula. Nunca calcular a mensalidade com a bolsa. Se a pessoa pedir o cálculo, responder: "A Ufape informa o valor com a bolsa aplicada junto com as condições da matrícula." Como e sobre o que a bolsa incide (mensalidades, matrícula): [CONFIRMAR].

**Resposta 7. Quanto custa a prova e como pago?**
> "A inscrição é R$ 100,00, à vista no Pix ou boleto, ou 1x de R$ 100,00 no cartão. Eu te passo o link da prova da sua especialidade."

Fonte: catálogo, seção 3. Cuidado: reembolso da inscrição não está publicado (resposta 11).

**Resposta 8. Onde e a que horas? O que eu levo?**
> "Sexta, 27/11, das 9h às 13h. Em São Paulo, é na Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista. Leve documento com foto. Celular e relógio não são permitidos no dia da prova."

Fonte: ficha 68639 e contexto/ufape-geral.md. Cuidado: para provas de Goiânia, não passar endereço até a Ufape confirmar (a página 68640 mostra o endereço de São Paulo): "Vou confirmar o local da prova de Goiânia e já te passo." Tolerância de atraso: [CONFIRMAR].

**Resposta 9. O que cai na prova?**
> "A prova tem questões de múltipla escolha e dissertativas. Vou confirmar com a coordenação se há conteúdo programático da sua especialidade e te passo."

Fonte: ficha 68639 e contexto. Cuidado: a página da prova de Felinos tem conteúdo e bibliografia, mas está fora desta régua. Nenhuma outra prova traz programa: não inventar tema nem material de estudo.

**Resposta 10. Quando sai o resultado e o que vem depois?**
> "O resultado sai por WhatsApp ou e-mail na data que a Ufape divulgar. Depois disso, são 2 dias úteis para recurso e 10 dias úteis para a matrícula, se houver bolsa."

Fonte: contexto e ficha 68639. Cuidado: a data de divulgação não está publicada [CONFIRMAR]; não prometer data. Em Felinos, o prazo de matrícula aparece como 10 e como 7 dias úteis: não citar.

**Resposta 11. Se eu não for bem ou não puder ir, perco os R$ 100,00?**
> "A inscrição é o valor para fazer a prova. A regra sobre ausência e devolução eu confirmo com a Ufape antes de te responder."

Fonte: nenhuma página traz a política. Cuidado: não prometer devolução, crédito nem nova prova [CONFIRMAR].

**Resposta 12. A turma pode não abrir?**
> "Pode. A turma é confirmada quando atinge o número mínimo de alunos. A Ufape orienta comprar passagem e hotel só depois da confirmação da turma."

Fonte: contexto/pos-graduacao.md. Cuidado: não citar o número mínimo: a página da prova diz 15 e as páginas de curso dizem 20 [CONFIRMAR]. Sem "últimas vagas" e sem contagem de vagas.

**Resposta 13. Preciso ser formado em Medicina Veterinária para fazer a prova?**
> "A pós é voltada a médicos veterinários formados. O requisito exato de inscrição na prova eu confirmo com a Ufape."

Fonte: contexto/pos-graduacao.md (público-alvo). Cuidado: a página da prova não traz o requisito [CONFIRMAR]; algumas páginas de curso citam graduandos, e isso precisa de confirmação antes de qualquer resposta.

**Resposta 14. Dá para entrar na pós sem fazer a prova?**
> "Dá para falar com o time de matrícula sobre a turma com as condições normais: parcelas, total e matrícula, como estão no site. A prova é uma forma de buscar bolsa, não é a única porta."

Fonte: catálogo, seção 2. Cuidado: só citar turma com status "aberto" no catálogo. Turmas em "verificar" não são divulgadas.

**Resposta 15. Estou olhando a prova de outra instituição.**
> "Posso te explicar com clareza como funciona a nossa: inscrição de R$ 100,00, 11 bolsas por prova, nota de corte 7,0 e as regras da página. Se quiser, te passo o link."

Cuidado: não comparar, não citar nome, taxa, bolsa ou data de outra instituição, nem em tom neutro. Se a pessoa insistir na comparação, dizer apenas que só fala das condições da Ufape e avisar a pessoa do marketing (pendência A-C4).

**Resposta 16. Esse curso tem certificado reconhecido? Dá título de especialista?**
> "Essa pergunta eu encaminho para a secretaria, que responde com o texto oficial: (11) 97492-8443 (WhatsApp) ou duvidas@intercursos.com.br, de segunda a sexta, das 9h às 18h."

Cuidado: nenhuma frase de certificação, reconhecimento ou validade por escrito, até a regulação aprovar o texto [PREENCHER COM A REGULAÇÃO]. Não responder por analogia nem com o que o site publica.

**Resposta 17. Tem prova de Oftalmologia? E a minha especialidade não aparece na lista.**
> Oftalmologia: "Não há prova de bolsa aberta de Oftalmologia agora. Para a turma de Oftalmologia, posso te explicar as condições do site."
>
> Especialidade sem prova na lista: "Vou conferir se a sua especialidade tem prova aberta e já te respondo."

Fonte: catálogo, seção 3 (68656 encerrada). Cuidado: para Medicina de Felinos, Endoscopia, Nefrologia e Urologia e Odontologia, a prova consta como aberta, mas o destino está em [CONFIRMAR]; usar a resposta 3 e não vender a prova como porta para uma turma até a confirmação.

---

## 7. Auditorias

### 7.1 auditorias/07-email-e-whatsapp.md

| Item | Resultado | Observação |
|---|---|---|
| Consentimento e descadastro funcionando (opt-in de WhatsApp registrado, saída simples nos dois canais) | Parcial | Saída escrita em todas as mensagens ("responda SAIR", botão "Sair", link de descadastro). O registro do opt-in e o funcionamento do descadastro dependem do CRM e da ferramenta de e-mail [CONFIRMAR]. Nenhum envio sem [opt_in_whatsapp] igual a sim |
| Cada mensagem tem um objetivo | Atendido | Objetivo único declarado em M1 a M20 |
| Assuntos e primeiras linhas são honestos | Atendido | Cinco por mensagem, sem escassez, sem prazo inventado, sem "bolsa garantida". "Quantas bolsas? São 11" e "R$ 100,00" são fatos da página. Assuntos de resultado não revelam a nota |
| Segmentos recebem mensagens relevantes para a etapa | Atendido | Convite para quem não se inscreveu; confirmação, véspera e dia para quem se inscreveu; resultado por grupo (com bolsa, sem bolsa, não atingiu, ausente). Versão por área só para D1 liberada |
| Réguas têm regras de saída | Atendido | Seção 1: inscreveu, respondeu, SAIR, bloqueou, prova fora do ar, matriculou |
| Resultados registrados para cada envio | Pendente | Tabela de registro de testes na seção 3.6, a preencher depois dos envios. Nenhum envio ocorreu |
| Cliques, respostas e conversões medidos, não só aberturas | Parcial | UTM definida e métricas na seção 1. Depende do CRM, do GA4 e dos eventos de inscrição [CONFIRMAR] |
| WhatsApp só em horário comercial, frequência humana e template da Meta | Parcial | Envios às 10h e 14h em dia útil; limite de 2 WhatsApp por semana. M15 (8h) só com janela aprovada. Nomes e variáveis dos templates definidos em cada mensagem; aprovação da Meta pendente |

### 7.2 auditorias/conformidade-educacional.md

| Bloco | Item | Resultado |
|---|---|---|
| Dados do curso | Nome, modalidade, carga horária e turno batem com o catálogo | Atendido: o nome segue "Pós-graduação em [área]"; modalidade e valores de turma estão na seção 5 e vêm das seções 2 e 3 do catálogo; as turmas "só no site" e com turma divergente estão marcadas |
| Dados do curso | Status "aberto" | Atendido: só as provas com status "aberto" entram; o CRM confere antes de cada envio; Oftalmologia (68656) e as 13 provas antigas ficam fora |
| Dados do curso | Modalidade clara | Atendido: prova presencial; pós semipresencial na maioria; 68632 presencial |
| Regulação | Pós lato sensu sem frase de reconhecimento | Atendido: nenhuma frase de certificação, validade ou nota institucional em nenhuma mensagem; resposta 16 encaminha para a secretaria |
| Regulação | Nota institucional | Atendido: nenhuma |
| Promessas | Sem promessa de emprego, salário, promoção, aprovação ou bolsa garantida | Atendido: os textos dizem "se atingir a nota de corte e receber uma das bolsas"; resultado e destino dependem da Ufape |
| Promessas | Dados de empregabilidade ou satisfação | Atendido: nenhum usado |
| Promessas | Superlativos | Atendido: nenhum |
| Promessas | Comparação com concorrente | Atendido: nenhuma comparação e nenhum concorrente citado; a resposta 15 proíbe comentar outra instituição |
| Preço e condições | Preço completo | Atendido: a inscrição de R$ 100,00 mostra a forma de pagamento; qualquer valor de turma, quando liberado, leva parcelas, valor da parcela, total e matrícula; nenhum valor de curso com bolsa calculado |
| Preço e condições | Bolsa com regra, público elegível e prazo | Parcial: regras de quantidade, percentual, nota de corte, prazos de recurso e de matrícula e não acumulação estão em todas as mensagens relevantes; turma de destino, regra do aprovado sem bolsa e monitoria estão [CONFIRMAR] e travam M18 e o bloco de turma |
| Preço e condições | Urgência real | Atendido: só a data real da prova (27/11) e prazos reais do resultado; nenhuma frase de escassez; reta final sem "inscrições até" |
| Preço e condições | Financiamento ou programas públicos | Atendido: nenhum citado |
| Pessoas e dados | Autorização de imagem | Atendido: sem foto, docente, aluno ou aprovado nomeado |
| Pessoas e dados | Menores | Não se aplica (público formado) |
| Pessoas e dados | Formulário com finalidade e política de privacidade | Pendente: o rodapé do e-mail leva o link da política; o checkout da prova precisa mostrar finalidade e política [CONFIRMAR no site] |
| Pessoas e dados | WhatsApp e e-mail só com consentimento e forma fácil de sair | Atendido no texto; registro do consentimento [CONFIRMAR] |
| Pessoas e dados | Nenhum dado pessoal na peça ou nos arquivos | Atendido: só campos entre colchetes |
| Plataformas | Páginas de destino entregam o que a mensagem promete | Parcial: página de Goiânia com endereço de São Paulo, links de Cardiologia invertidos e regras de Felinos contraditórias bloqueiam os envios correspondentes |
| Anúncios | Itens de anúncio (Meta e Google) | Não se aplica: a régua é de e-mail e WhatsApp |

Resultado: aprovado para revisão do qa-de-marketing e da pessoa do marketing com bloqueios. Pode ir para aprovação: M1, M2, M5 a M17 e M19 e M20 (com a ressalva de M20), M3 e M4 só para as provas liberadas em São Paulo na seção 4. Bloqueado: M3 e M4 de Goiânia (local e links), toda mensagem de provas D2, D3 e D4 por área, o bloco de turma (A-C2), M18 (regra do aprovado sem bolsa), M15 (janela de WhatsApp às 8h), toda menção a prazo de inscrição e a data de resultado (A-C3). Revisado por: copy-de-mensagens (autoavaliação). qa-de-marketing e pessoa do marketing: pendente. Data: 26/10/2026.

---

## 8. Próximo passo

1. Pessoa do marketing: aprovar os textos (A-C7) e encaminhar à Ufape as perguntas de A-C2 e A-C3 (destino das provas, data do resultado, prazo de inscrição, local de Goiânia, regra do aprovado sem bolsa, política de ausência).
2. CRM: confirmar o registro de opt-in, os campos da seção 2 e submeter os templates à Meta (marketing e utilidade).
3. **Próximo agente sugerido: otimizacao-de-mensagens**, com este arquivo, depois que houver o primeiro envio de M1 a M4 e os resultados de abertura, clique e resposta do registro de testes.

---

## Lista 1. Fatos (com fonte)

- 22 provas de bolsa com status "aberto" e data de 27/11/2026, 19 em São Paulo e 3 em Goiânia (68640, 68642, 68644). Fonte: contexto/catalogo-de-cursos.md, seção 3.
- Inscrição de R$ 100,00 à vista (Pix ou boleto) ou 1x de R$ 100,00 no cartão. Fonte: catálogo, seção 3.
- Prova presencial, das 9h às 13h, de múltipla escolha e dissertativas; nota de corte 7,0 (mínimo de 70% de acerto); 2 dias úteis para recurso; 10 dias úteis para a matrícula; bolsa não acumulativa e intransferível; desempate por análise de currículo; resultado por WhatsApp e/ou e-mail. Fonte: contexto/pos-graduacao.md e ficha 68639.
- 11 bolsas por prova: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Fonte: contexto/pos-graduacao.md e ficha 68639.
- Levar documento com foto; celular e relógios não são permitidos no dia da prova. Fonte: ficha 68639.
- Endereço da prova de São Paulo: Av. 9 de Julho, 3939, esquina com Honduras, 765, Jardim Paulista, São Paulo, SP, 01407-100. Fonte: ficha 68639 e contexto/ufape-geral.md.
- A página 68640 (Goiânia) mostra o endereço de São Paulo; links de Cardiologia (68641 e 68642) invertidos; a página 68652 (Felinos) traz regras contraditórias e frase de certificação. Fonte: estratégia de campanha, seções 2.3 e 3.3.
- Turma mínima: 15 na página da prova e 20 nas páginas de curso. Fonte: contexto/pos-graduacao.md.
- Turmas candidatas, datas e condições da seção 5. Fonte: catálogo, seção 2.
- Contatos oficiais: secretaria (11) 97492-8443 (WhatsApp), (11) 5054-1204, duvidas@intercursos.com.br, segunda a sexta, das 9h às 18h; vendas São Paulo (11) 91366-9290; vendas Goiânia (62) 9420-1847. Fonte: contexto/ufape-geral.md.
- Workshop de Neuromonitorização em 20 e 21/11/2026. Fonte: docs/execucao-2026-10-26.md, decisão 6.
- 26/10/2026 é segunda-feira; 03/11 é terça, 27/11 é sexta. Fonte: estratégia de campanha, seção 5 (dias da semana calculados a partir dela).
- Voz da marca: precisa, próxima, transparente; sem emoji em e-mail; sem assumir leitor homem. Fonte: estrategia-de-marca-geral, seções 3 e 5 (voz ainda [SUPOSIÇÃO] da Ufape).

## Lista 2. Suposições

- [SUPOSIÇÃO] Janela comercial de WhatsApp de segunda a sexta, das 9h às 18h.
- [SUPOSIÇÃO] Limite de 2 WhatsApp e 2 e-mails de campanha por contato por semana.
- [SUPOSIÇÃO] Padrão de UTM e nomes dos templates da Meta (pb_*), e a classificação (marketing ou utilidade), que a Meta decide.
- [SUPOSIÇÃO] A base permite segmentar por [área_de_interesse] e por [segmento] (lead e ex-aluno); sem isso, só a versão mestre.
- [SUPOSIÇÃO] Ganchos por área da seção 4 (hipóteses da pesquisa de persona, sem fala real de aluno).
- [SUPOSIÇÃO] Os horários de envio (10h, 14h, 7h e 8h) e os dias, dentro do calendário da estratégia de campanha.
- [SUPOSIÇÃO] Feriados de 02/11 e 20/11 afetam o ritmo de resposta e a contagem de dias úteis; a contagem oficial é da Ufape.
- [SUPOSIÇÃO] Mensagem de serviço ao inscrito pode ser enviada com base na relação de serviço, mesmo para quem saiu das mensagens de campanha (a Ufape confirma).
- [SUPOSIÇÃO] "Sem pressa de decisão" em M19 só vale se a turma tiver prazo que permita; o time ajusta com data real.
- [SUPOSIÇÃO] As provas "sem turma futura aberta" (D4) seguem à venda; a Ufape confirma.
- [SUPOSIÇÃO] Destino provável das provas D1 (seção 5), leitura da squad a partir do catálogo.

## Lista 3. Dados que faltam

- [CONFIRMAR] Turma de destino de cada uma das 22 provas; especialmente Dermatologia (68646) e Hematologia (68651), que têm turma abrindo em 28/11, e 68652, 68649, 68653 e 68655, sem turma aberta (A-C2).
- [CONFIRMAR] Prazo de inscrição nas provas (hoje nenhuma mensagem diz "inscrições até").
- [CONFIRMAR] Data de divulgação do resultado, canal para pedir recurso e calendário de dias úteis.
- [CONFIRMAR] Critério de distribuição das 11 bolsas, regra do aprovado sem bolsa, lista de espera e o que a monitoria exige.
- [CONFIRMAR] Sobre o que incide a bolsa (mensalidades, matrícula) e quem informa o valor com a bolsa aplicada.
- [CONFIRMAR] Local da prova em Goiânia (68640, 68642 e 68644); correção dos links de Cardiologia.
- [CONFIRMAR] Regras de Felinos (canal do resultado, prazo de 10 ou 7 dias, composição) e retirada da frase de certificação da página.
- [CONFIRMAR] Turma mínima (15 ou 20) e data em que a turma é confirmada.
- [CONFIRMAR] Política de ausência, de reembolso da inscrição e de nova prova.
- [CONFIRMAR] Requisito de inscrição na prova (médico veterinário formado).
- [CONFIRMAR] Tolerância de atraso e horário de abertura do local da prova.
- [CONFIRMAR] Conteúdo programático por especialidade (só a ficha de Felinos traz).
- [CONFIRMAR] Se existe página que reúna as provas ([link_mestre]); se não, M2 e M8 usam o link do WhatsApp de vendas.
- [CONFIRMAR] CRM, ferramenta de e-mail, registro de opt-in, alcance do "SAIR" nas mensagens de serviço, finalidade e política de privacidade no checkout.
- [CONFIRMAR] Quem aprova e-mail e WhatsApp em massa (tabela em contexto/ufape-geral.md).
- [CONFIRMAR] Regra do desconto de ex-aluno (contexto/ufape-geral.md está em [PREENCHER]).
- [PREENCHER COM A REGULAÇÃO] Texto oficial de certificação: nenhuma mensagem usa; a resposta 16 encaminha para a secretaria.
- [CONFIRMAR NO CATÁLOGO] Regras da prova de bolsa como coluna do catálogo (hoje em contexto/pos-graduacao.md e nas fichas).
- [CONFIRMAR] Metas de inscritos, comparecimento e matrículas (nenhuma meta existe hoje).

## Fontes

Internas: docs/execucao-2026-10-26.md; CLAUDE.md; contexto/ufape-geral.md; contexto/pos-graduacao.md; contexto/catalogo-de-cursos.md; contexto/cursos/pos/68639-prova-de-bolsa-de-estudos-para-anestesiologia-veterinaria.md; templates/mensagem.md; .claude/skills/assuntos-de-email/SKILL.md; .claude/skills/mapear-regua/SKILL.md; saidas/06-geracao-de-demanda/estrategia-de-campanha-pos-2026-10-26.md; saidas/01-inteligencia-de-mercado/pesquisa-de-persona-pos-2026-10-26.md; saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md; auditorias/07-email-e-whatsapp.md; auditorias/conformidade-educacional.md.

Externas: nenhuma.
