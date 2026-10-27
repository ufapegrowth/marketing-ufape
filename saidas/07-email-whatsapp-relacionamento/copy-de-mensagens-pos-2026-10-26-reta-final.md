# Mensagens de reta final, véspera e pós-início das turmas 707, 68604 e 68606

- Agente: copy-de-mensagens (departamento 07, E-mail, WhatsApp e Relacionamento), camada 3, onda 1
- Linha: pos
- Data: 26/10/2026 (prazo no plano do cmo: 28/10/2026)
- Formato: templates/mensagem.md, repetido por mensagem e por canal
- Status: rascunho para o qa-de-marketing e para aprovação humana. Nada foi enviado, publicado ou pago. Os textos são para o CRM enviar só a quem deu opt-in e demonstrou interesse nessas turmas.
- Entradas lidas:
  - docs/execucao-2026-10-26.md
  - CLAUDE.md
  - contexto/ufape-geral.md
  - contexto/pos-graduacao.md
  - contexto/catalogo-de-cursos.md (seção 2; seção 3 para as provas 68647 e 68650)
  - contexto/cursos/pos/707-pos-graduacao-em-oftalmologia-veterinaria.md
  - contexto/cursos/pos/68604-pos-graduacao-em-diagnostico-por-imagem-aplicado-a-clinica-medica-e-ci.md
  - contexto/cursos/pos/68606-pos-graduacao-em-gastroenterologia-veterinaria.md
  - contexto/cursos/pos/68629-pos-graduacao-em-ultrassonografia-de-pequenos-animais.md (próxima turma da área de 68604)
  - contexto/cursos/pos/68647-prova-de-bolsa-de-estudos-para-diagnostico-por-imagem.md (regras das provas)
  - templates/mensagem.md
  - .claude/skills/assuntos-de-email/SKILL.md
  - saidas/02-estrategia-e-posicionamento/estrategia-de-oferta-pos-2026-10-26.md (texto-padrão de preço, seções 2.1 e 4, propostas PR2 e PR4)
  - saidas/02-estrategia-e-posicionamento/posicionamento-pos-2026-10-26.md (variações A9, A5 e A6)
  - saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md (seções 0 e 1, A5 e A6; parcial)
  - saidas/11-midia-paga/gestor-de-midia-geral-2026-10-26.md (seção 5, decisões para 707, 68604 e 68606)
  - saidas/02-estrategia-e-posicionamento/estrategia-de-marca-geral-2026-10-26.md (voz, seções 5 a 7)
  - auditorias/07-email-e-whatsapp.md e auditorias/conformidade-educacional.md
- Não abri faculdade.ufape.com.br. Nenhuma busca na web.
- Dados pessoais: nenhum. Nome do lead entra só como variável do CRM no momento do envio. Docentes aparecem só como coordenação, com nome e titulação como na ficha, todos marcados [CONFIRMAR autorização].

---

## 0. Como ler e o que o time precisa decidir antes de enviar

### 0.1 Objetivo único de cada mensagem

| Mensagem | Objetivo único |
|---|---|
| Reta final | Levar o lead a abrir a página da turma ou falar com vendas para entrar na turma |
| Véspera | Dizer o que fazer hoje para entrar: comprar na página ou falar com vendas |
| Pós-início | Para quem não entrou: apresentar o próximo passo da área (outra turma, ou lista de interesse), sem pressão |

Cada mensagem tem uma chamada para ação. Na véspera, a chamada é "entrar na turma", com dois caminhos oficiais (página ou vendas) que levam ao mesmo resultado. No WhatsApp, só um link por mensagem.

### 0.2 Conflito entre duas regras e como foi resolvido

O pedido manda citar a condição da 1ª mensalidade como está na ficha. A estrategia-de-oferta (seção 2.1, regra 3) manda tirar essa frase das turmas em que o prazo já venceu (707, 68604 e 68606), porque dizer "pague até 30 dias antes do início" a quem não pode cumprir induz a erro.

Solução adotada: a mensagem cita a condição da ficha e diz com clareza que o prazo já passou, terminando em "fale com o time para saber como entrar na turma" (frase CL1 abaixo). Assim a condição aparece como está na página e o lead não é enganado. Se a Ufape preferir a regra da oferta, basta apagar a primeira frase de CL1. Decisão: cmo e Ufape.

**CL1 (condição da 1ª mensalidade, usada nas mensagens de reta final e véspera):**
"A página da turma informa que a 1ª mensalidade é paga até 30 dias antes do início. Esse prazo já passou para esta turma: fale com o time de vendas para saber como entrar."

### 0.3 Bloqueios de envio (nada sai antes de resolver)

| # | Bloqueio | Quem resolve | Efeito se não resolver |
|---|---|---|---|
| B1 | Autorização de uso do nome e da titulação da coordenação | Ufape | Apagar a linha de coordenação de todas as mensagens (cada uma tem a linha separada, marcada COORD) |
| B2 | Política de entrada em turma já iniciada e depois do módulo 1 (PR4) | Ufape | Usar só a frase CL1 e as respostas provisórias da seção 5 |
| B3 | Status da turma (confirmada ou não) e data de confirmação (PR2) | Ufape | Nenhuma mensagem diz "turma confirmada". A linha opcional TC só entra com confirmação escrita |
| B4 | Templates do WhatsApp aprovados pela Meta (nove templates, seção 6) | Pessoa do marketing que administra o WhatsApp Business API [CONFIRMAR quem] | Sem template aprovado, só vale mensagem livre dentro da janela de 24 h depois de uma resposta do lead |
| B5 | Lista de interesse (mecanismo e responsável) para o pós-início | Ufape e CRM | Trocar a mensagem pós-início por "o time de vendas responde dúvidas" sem a oferta da lista |
| B6 | Destino das provas 68647 e 68650 (variante com prova do pós-início) | Ufape | A variante com prova não é enviada; vale a variante com lista de interesse |
| B7 | Opt-in registrado por canal, com data e finalidade, e supressão de quem já comprou ou saiu | CRM | Lead sem opt-in não recebe |

### 0.4 Regras de envio (valem para as nove mensagens)

1. Segmento: lead com interesse registrado na turma (código no CRM), opt-in do canal, sem matrícula na turma e sem opt-out. Quem já comprou sai da lista antes de cada envio. Quem está em atendimento ativo com vendas fica pausado.
2. WhatsApp só em dia útil, das 9h às 18h, só para quem deu opt-in, com a opção "Parar de receber" no botão do template e a resposta SAIR. E-mail com link de descadastro.
3. Frequência: no máximo 3 mensagens de WhatsApp por lead e por turma em 15 dias (reta final, véspera, pós-início) [SUPOSIÇÃO de regra, a validar]. Cada mensagem tem um follow-up curto, previsto na própria seção.
4. Sem "últimas vagas", "vagas limitadas", número de vagas restantes, "corra", contador, "garanta" ou prazo que não existe. A única data de urgência é a data de início, que é real.
5. Sem frase de certificação, nota do MEC, promessa de título, emprego, renda ou aprovação. Sem comparação com concorrente.
6. Nome do curso sempre "Pós-graduação em <área>".
7. Link de turma com UTM [SUPOSIÇÃO de padrão, a confirmar com o arquivista de UTM do time]: ?utm_source=<canal>&utm_medium=crm&utm_campaign=<código>-<etapa>. Etapas: reta-final, vespera, pos-inicio.

### 0.5 Campos do CRM usados em todas as mensagens

| Campo | Uso |
|---|---|
| primeiro_nome | variável {{1}} do template e saudação do e-mail |
| turma_interesse (código) | segmento e UTM |
| opt_in_whatsapp, opt_in_email (sim ou não, data, finalidade) | condição de envio |
| matriculado_turma (sim ou não) | supressão |
| optout (data e canal) | supressão |
| etapa_envio (reta_final, vespera, pos_inicio) | controle de frequência |
| resultado_envio (entregue, lido, clique, resposta, SAIR) | auditoria e medição |
| lista_interesse_<área> (sim ou não, data) | pós-início, após B5 |
| motivo_perda (campo livre fechado: preço, tempo, viagem, turma, outro) | aprendizado do pós-início |

### 0.6 Datas de envio propostas [SUPOSIÇÃO, sujeitas à aprovação]

| Turma | Reta final | Véspera | Pós-início |
|---|---|---|---|
| 707 (início 30/10, sexta) | 28/10 (quarta), 10h | 29/10 (quinta), 10h | 04/11 (quarta), 10h |
| 68604 (início 31/10, sábado) | 28/10 (quarta), 14h | 30/10 (sexta), 10h | 04/11 (quarta), 14h |
| 68606 (início 07/11, sábado) | 03/11 (terça), 10h (02/11 é feriado) | 06/11 (sexta), 10h | 11/11 (quarta), 10h |

Sábado e domingo não recebem WhatsApp. Por isso a véspera de 68604 e 68606 sai na sexta.

---

## 1. Turma 707: Pós-graduação em Oftalmologia Veterinária

### 1.1 Dados usados e fonte

| Dado | Valor | Fonte |
|---|---|---|
| Curso e turma | Pós-graduação em Oftalmologia Veterinária, turma VII | catálogo, seção 2 |
| Início | 30/10/2026 (planilha). O site mostra 30 e 31/10 e 01/11 | catálogo; ficha |
| Local | São Paulo, Av. 9 de Julho, 3939 | catálogo; ficha |
| Modalidade, carga, módulos | Semipresencial, 600 h, 24 módulos | catálogo (modalidade e carga); módulos: ficha [CONFIRMAR NO CATÁLOGO] |
| Preço | 30x de R$ 1.590,00 no cartão ou boleto, total de R$ 47.700,00, matrícula de R$ 250,00 | catálogo |
| 1ª mensalidade | "deverá ser paga com 30 dias de antecedência da data de seu início" | ficha [CONFIRMAR NO CATÁLOGO] |
| Turma mínima | 20 alunos | ficha [CONFIRMAR NO CATÁLOGO] |
| Módulo 1 | 30/10 a 01/11/2026, online: introdução e bases da oftalmologia | ficha [CONFIRMAR NO CATÁLOGO] |
| Horários | Sexta 14h às 20h, sábado 8h às 17h30, domingo 8h às 12h | ficha [CONFIRMAR NO CATÁLOGO] |
| Primeiro módulo presencial | Módulo 4, 29 a 31/01/2027 | ficha [CONFIRMAR NO CATÁLOGO] |
| Formato | Aulas teóricas online e ao vivo, aulas gravadas na plataforma para revisão, aulas práticas presenciais na sede, cada aluno com microscópio individual, atendimentos em mutirões supervisionados. Presenciais e práticas não são transmitidos | ficha [CONFIRMAR NO CATÁLOGO] |
| Coordenação (COORD) | Dra. Andrea Barbosa, Dra. Angélica Safatle, Dra. Juliana Jorge | ficha [CONFIRMAR autorização] |
| Professores listados | 19 | ficha |
| Link | https://faculdade.ufape.com.br/produto/707/pos-graduacao-em-oftalmologia-veterinaria | ficha |
| Status | aberto | catálogo |
| Prova de bolsa | Nenhuma (a 68656 está fora do ar) | catálogo, seção 3 |
| Próxima turma da área | Nenhuma no catálogo de 26/10/2026 | catálogo, seção 2 |

Texto-padrão de preço (TP-707): "Investimento: 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00."

Linha de turma mínima (TM): "Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada."

### 1.2 Reta final (28/10)

**Objetivo:** levar o lead a abrir a página da turma VII ou falar com vendas para entrar na turma.
**Segmento:** lead com interesse em 707, com opt-in, sem matrícula.

#### E-mail

Assuntos (5):
1. Oftalmologia Veterinária: a turma VII começa em 30/10
2. Pós-graduação em Oftalmologia Veterinária: cronograma e condições da turma VII
3. O módulo 1 de Oftalmologia é online: veja como entrar na turma VII
4. 600 h, 24 módulos: o que acontece na Pós-graduação em Oftalmologia Veterinária
5. Como entrar na turma VII de Oftalmologia Veterinária

Escolhidos para teste: **A = 1** (data direta), **B = 3** (fato do formato que reduz a barreira de começar).

Texto de pré-visualização: Semipresencial, 600 h, São Paulo. Parcelas, total e matrícula dentro.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começa em 30/10/2026, em São Paulo.
>
> O curso forma médicos veterinários para a clínica e a cirurgia oftalmológica. É semipresencial: 600 h em 24 módulos, com teoria online e ao vivo, aulas gravadas para revisão e prática presencial na sede, com um microscópio por aluno. Presenciais e práticas não são transmitidos. O módulo 1 é online, de 30/10 a 01/11 (sexta das 14h às 20h, sábado das 8h às 17h30, domingo das 8h às 12h). O primeiro módulo presencial é o 4, de 29 a 31/01/2027. O cronograma completo está na página e pode mudar conforme a necessidade das aulas.
>
> COORD: A coordenação é de Dra. Andrea Barbosa, Dra. Angélica Safatle e Dra. Juliana Jorge. A página lista 19 professores.
>
> Investimento: 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00.
>
> {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada.
>
> Para ver o cronograma e entrar na turma: [Ver a página da turma VII]
>
> Se preferir conversar, o time de vendas de São Paulo responde pelo WhatsApp (11) 91366-9290. Dúvidas de secretaria: (11) 97492-8443, de segunda a sexta, das 9h às 18h.
>
> Faculdade UFAPE

Chamada para ação: botão "Ver a página da turma VII" (link com UTM 707-reta-final).
Rodapé: "Você recebe este e-mail porque demonstrou interesse nos cursos da Faculdade UFAPE. Para parar de receber, clique em descadastrar. Faculdade UFAPE, Av. 9 de Julho, 3939, São Paulo, SP. Política de privacidade: [CONFIRMAR link]."
Follow-up (e-mail, 1 dia útil depois, só para quem não abriu, assunto B se A foi o primeiro): "Olá, {primeiro_nome}. Só para o caso de a mensagem de ontem ter passado batida: a turma VII de Oftalmologia Veterinária começa em 30/10, e o módulo 1 é online. O cronograma e as condições estão aqui: [link]. Para parar de receber, use o descadastro."

#### WhatsApp (template)

Primeiras linhas (5), que aparecem na notificação:
1. Olá, {{1}}. A turma VII de Oftalmologia Veterinária começa em 30/10.
2. {{1}}, o cronograma da Pós-graduação em Oftalmologia Veterinária está publicado.
3. Olá, {{1}}. Você se interessou pela Pós-graduação em Oftalmologia Veterinária: veja como entrar na turma VII.
4. Olá, {{1}}. Sobre a Pós-graduação em Oftalmologia Veterinária: o módulo 1 é online.
5. {{1}}, 600 h de Oftalmologia Veterinária: veja a turma VII.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (nome sugerido: pos_707_reta_final_v1; categoria marketing):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começa em 30/10/2026, em São Paulo. É semipresencial, com 600 h e 24 módulos: teoria online e prática presencial na sede. O módulo 1 é online.
>
> COORD: Coordenação: Dra. Andrea Barbosa, Dra. Angélica Safatle e Dra. Juliana Jorge.
>
> Investimento: 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00. A página informa que a 1ª mensalidade é paga até 30 dias antes do início. Esse prazo já passou: fale com o time de vendas para saber como entrar na turma. Turma mínima de 20 alunos.

Botões: [Ver a página da turma] (URL com UTM, a única ligação da mensagem) e [Parar de receber] (resposta rápida). Texto de rodapé do template: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Ver a página da turma".
Variáveis: {{1}} = primeiro_nome; sufixo dinâmico do botão = UTM da turma e da etapa.
Follow-up WhatsApp: nenhum reenvio do mesmo template. A mensagem de véspera (1.3) cumpre esse papel. Se o lead responder, vendas segue a seção 5.
Opt-in de WhatsApp confirmado: só quem tem registro no CRM (sim).
Template aprovado pela Meta: [CONFIRMAR aprovação de pos_707_reta_final_v1].
Forma de sair: botão "Parar de receber" e resposta SAIR.

### 1.3 Véspera (29/10, "começa amanhã, sexta")

**Objetivo:** dizer o que fazer para entrar. **Segmento:** lead de 707 que não comprou e não respondeu à reta final.

#### E-mail

Assuntos (5):
1. Amanhã começa a turma VII de Oftalmologia Veterinária
2. Módulo 1 de Oftalmologia, de sexta a domingo: como entrar na turma
3. O que fazer hoje para entrar na turma VII de Oftalmologia
4. A turma VII começa neste fim de semana: horários do módulo 1
5. Oftalmologia Veterinária: compre pela página ou fale com vendas

Escolhidos: **A = 3**, **B = 4**.
Texto de pré-visualização: Módulo 1 online, de 30/10 a 01/11. Veja os horários e as duas formas de entrar.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começa amanhã, sexta, 30/10/2026. O módulo 1 vai até domingo, 01/11, e é online: sexta das 14h às 20h, sábado das 8h às 17h30 e domingo das 8h às 12h.
>
> Para entrar na turma você tem duas formas:
> 1. Comprar pela página da turma: [link]
> 2. Falar com o time de vendas de São Paulo, pelo WhatsApp (11) 91366-9290.
>
> Investimento: 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00. {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada. O primeiro módulo presencial é só em 29 a 31/01/2027.
>
> TC (só com confirmação escrita da Ufape): A Ufape confirmou a formação da turma.
>
> Faculdade UFAPE

Chamada para ação: entrar na turma (botão da página; o telefone de vendas está no texto).
Follow-up (e-mail, 30/10 às 8h, só para quem não abriu): assunto "Hoje começa o módulo 1 de Oftalmologia Veterinária"; corpo: "Olá, {primeiro_nome}. O módulo 1 da turma VII começa hoje, às 14h, online. Para entrar: [link] ou vendas (11) 91366-9290. Para parar de receber, use o descadastro."
Rodapé e descadastro como em 1.2.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. Amanhã começa a turma VII de Oftalmologia Veterinária.
2. {{1}}, o módulo 1 de Oftalmologia é de sexta a domingo, online.
3. Olá, {{1}}. Para entrar na turma VII de Oftalmologia, são duas formas.
4. {{1}}, a turma VII de Oftalmologia começa neste fim de semana.
5. Olá, {{1}}. Horários do módulo 1 de Oftalmologia Veterinária.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (pos_707_vespera_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começa amanhã, sexta, 30/10/2026. O módulo 1 é online e vai até domingo: sexta das 14h às 20h, sábado das 8h às 17h30, domingo das 8h às 12h.
>
> Para entrar: compre pela página (botão abaixo) ou fale com vendas de São Paulo, (11) 91366-9290.
>
> Investimento: 30x de R$ 1.590,00 no cartão ou boleto (total de R$ 47.700,00), mais matrícula de R$ 250,00. A 1ª mensalidade, segundo a página, é paga até 30 dias antes do início; esse prazo já passou, então o time orienta como entrar. Turma mínima de 20 alunos.

Botões: [Comprar pela página] e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Variáveis: {{1}} primeiro_nome; sufixo do botão com UTM 707-vespera.
Follow-up: nenhum no WhatsApp (a turma já terá começado). Quem responder segue a seção 5.
Template aprovado pela Meta: [CONFIRMAR pos_707_vespera_v1].

### 1.4 Pós-início (04/11): para quem não entrou

**Objetivo:** oferecer o próximo passo da área sem pressão. Não há outra turma de Oftalmologia Veterinária no catálogo de 26/10/2026 e não há prova de bolsa da área (68656 fora do ar). O próximo passo é a lista de interesse [CONFIRMAR mecanismo, B5].
**Segmento:** lead de 707 sem matrícula.

#### E-mail

Assuntos (5):
1. Oftalmologia Veterinária: quer ser avisado sobre uma nova turma?
2. A turma VII começou. E agora?
3. Pós-graduação em Oftalmologia Veterinária: lista de interesse
4. Sobre a Pós-graduação em Oftalmologia Veterinária: um aviso e uma pergunta
5. Oftalmologia Veterinária: seguimos à disposição

Escolhidos: **A = 1**, **B = 4**.
Texto de pré-visualização: Sem pressão: só para registrar seu interesse.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começou em 30/10/2026. Hoje não há outra turma de Oftalmologia Veterinária aberta no nosso catálogo.
>
> Se você quer ser avisado caso uma nova turma seja aberta, responda este e-mail com a palavra LISTA, e o time de vendas registra o seu interesse. Quando houver turma, você recebe as datas, o cronograma e as condições completas.
>
> Se ainda tem dúvida sobre a turma VII, o time de vendas de São Paulo responde pelo WhatsApp (11) 91366-9290.
>
> Faculdade UFAPE

Chamada para ação: responder LISTA (sem link).
Follow-up (e-mail, 3 dias úteis depois, só para quem não abriu): assunto "Oftalmologia Veterinária: seu interesse continua registrado?"; corpo de duas linhas com a mesma chamada. Sem terceiro envio.
Rodapé e descadastro como em 1.2.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. A turma VII de Oftalmologia Veterinária já começou.
2. {{1}}, quer ser avisado se abrir nova turma de Oftalmologia Veterinária?
3. Olá, {{1}}. Um aviso sobre a Pós-graduação em Oftalmologia Veterinária.
4. {{1}}, sobre Oftalmologia Veterinária: sem pressão, só uma pergunta.
5. Olá, {{1}}. Lista de interesse de Oftalmologia Veterinária.

Escolhidas: **A = 2**, **B = 4**.

Corpo do template (pos_707_pos_inicio_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VII da Pós-graduação em Oftalmologia Veterinária começou em 30/10/2026. Hoje não há outra turma de Oftalmologia Veterinária aberta no nosso catálogo.
>
> Se quiser ser avisado caso uma nova turma seja aberta, toque em "Quero ser avisado". Se ainda tem dúvida sobre a turma VII, o time de vendas responde por aqui.

Botões (só respostas rápidas, nenhum link): [Quero ser avisado] e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Quero ser avisado" (grava lista_interesse_oftalmologia = sim e a data).
Follow-up WhatsApp: nenhum.
Template aprovado pela Meta: [CONFIRMAR pos_707_pos_inicio_v1].

---

## 2. Turma 68604: Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária

### 2.1 Dados usados e fonte

| Dado | Valor | Fonte |
|---|---|---|
| Curso e turma | Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária, turma VI | catálogo, seção 2 |
| Início | 31/10/2026 (planilha). O site mostra 31/10 e 01/11 | catálogo; ficha |
| Local | São Paulo, Av. 9 de Julho, 3939 | catálogo; ficha. O CEP da ficha (01428-001) difere do das outras turmas: não vai para a peça |
| Modalidade, carga, módulos | Semipresencial, 500 h, 24 módulos | catálogo; módulos: ficha [CONFIRMAR NO CATÁLOGO] |
| Preço | 30x de R$ 1.000,00 no cartão ou boleto, total de R$ 30.000,00, matrícula de R$ 250,00 | catálogo |
| 1ª mensalidade | "deverá ser paga com 30 dias de antecedência da data de seu início" | ficha [CONFIRMAR NO CATÁLOGO] |
| Turma mínima | 20 alunos | ficha [CONFIRMAR NO CATÁLOGO] |
| Módulo 1 | 31/10 e 01/11/2026, online: introdução à radiologia, proteção radiológica e normativas; introdução à ultrassonografia e ajustes do equipamento | ficha [CONFIRMAR NO CATÁLOGO] |
| Primeiro módulo presencial | Módulo 4, fevereiro de 2027 (a ficha não traz o dia) | ficha [CONFIRMAR NO CATÁLOGO] |
| Conteúdo | Radiografia, ultrassonografia, tomografia computadorizada e ressonância magnética, associando os achados às informações clínicas | ficha [CONFIRMAR NO CATÁLOGO] |
| Presenciais e práticas | Não são transmitidos nem disponibilizados | ficha [CONFIRMAR NO CATÁLOGO] |
| Coordenação (COORD) | M.V. Carlos Fotin | ficha [CONFIRMAR autorização] |
| Professores listados | 11 | ficha |
| Link | https://faculdade.ufape.com.br/produto/68604/pos-graduacao-em-diagnostico-por-imagem-aplicado-a-clinica-medica-e-cirurgica-veterinaria | ficha |
| Status | aberto | catálogo |
| Atenção | A turma 68611 tem o mesmo nome e está em "verificar" (sem data). Nunca usar o link ou o código dela | catálogo |
| Prova de bolsa da área | 68647, São Paulo, 27/11/2026, R$ 100,00 (aberto). Destino não confirmado | catálogo, seção 3 |
| Próxima turma da área (A5) | 68629, Pós-graduação em Ultrassonografia de Pequenos Animais, turma III, 22/05/2027 (planilha ausente, só no site), semipresencial, 360 h, 18 módulos, 24x de R$ 685,67, total de R$ 16.456,00, matrícula de R$ 350,00 | catálogo; ficha [CONFIRMAR NO CATÁLOGO a data, que vem só do site] |

Texto-padrão de preço (TP-68604): "Investimento: 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00."

### 2.2 Reta final (28/10)

**Objetivo:** levar o lead a abrir a página da turma VI ou falar com vendas para entrar na turma.

#### E-mail

Assuntos (5):
1. Diagnóstico por Imagem: a turma VI começa em 31/10
2. Pós-graduação em Diagnóstico por Imagem: cronograma e condições da turma VI
3. O módulo 1 de Diagnóstico por Imagem é online: veja como entrar na turma VI
4. Radiografia, ultrassom, tomografia e ressonância: o que cobre a turma VI
5. Como entrar na turma VI de Diagnóstico por Imagem

Escolhidos: **A = 1**, **B = 4**.
Texto de pré-visualização: Semipresencial, 500 h, São Paulo. Parcelas, total e matrícula dentro.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária começa em 31/10/2026, em São Paulo.
>
> O curso aprofunda a realização e a interpretação de imagens radiográficas, ultrassonográficas, tomográficas e de ressonância magnética, sempre ligadas ao caso clínico. É semipresencial: 500 h em 24 módulos. O módulo 1 é online, em 31/10 e 01/11, e trata de radiologia, proteção radiológica, normativas e ajustes do equipamento de ultrassom. O primeiro módulo presencial é o 4, em fevereiro de 2027. Presenciais e práticas não são transmitidos. O cronograma completo está na página e pode mudar conforme a necessidade das aulas.
>
> COORD: A coordenação é de M.V. Carlos Fotin. A página lista 11 professores.
>
> Investimento: 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00.
>
> {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada.
>
> Para ver o cronograma e entrar na turma: [Ver a página da turma VI]
>
> Se preferir conversar, o time de vendas de São Paulo responde pelo WhatsApp (11) 91366-9290. Dúvidas de secretaria: (11) 97492-8443, de segunda a sexta, das 9h às 18h.
>
> Faculdade UFAPE

Chamada para ação: botão "Ver a página da turma VI" (UTM 68604-reta-final).
Rodapé e descadastro como em 1.2.
Follow-up (e-mail, 1 dia útil depois, só para quem não abriu): "Olá, {primeiro_nome}. A turma VI de Diagnóstico por Imagem começa em 31/10, e o módulo 1 é online. Cronograma e condições: [link]. Para parar de receber, use o descadastro."

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. A turma VI de Diagnóstico por Imagem começa em 31/10.
2. {{1}}, o cronograma da Pós-graduação em Diagnóstico por Imagem está publicado.
3. Olá, {{1}}. Você se interessou pela Pós-graduação em Diagnóstico por Imagem: veja como entrar na turma VI.
4. Olá, {{1}}. Sobre Diagnóstico por Imagem: o módulo 1 é online.
5. {{1}}, radiografia, ultrassom, tomografia e ressonância: veja a turma VI.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (pos_68604_reta_final_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária começa em 31/10/2026, em São Paulo. É semipresencial, com 500 h e 24 módulos: teoria online e prática presencial. O módulo 1 é online.
>
> COORD: Coordenação: M.V. Carlos Fotin.
>
> Investimento: 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00. A página informa que a 1ª mensalidade é paga até 30 dias antes do início. Esse prazo já passou: fale com o time de vendas para saber como entrar na turma. Turma mínima de 20 alunos.

Botões: [Ver a página da turma] (UTM) e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Ver a página da turma".
Variáveis: {{1}} primeiro_nome; sufixo do botão com UTM.
Follow-up: nenhum reenvio; a véspera cumpre o papel.
Template aprovado pela Meta: [CONFIRMAR pos_68604_reta_final_v1].

### 2.3 Véspera (30/10, "começa amanhã, sábado")

**Objetivo:** dizer o que fazer para entrar.

#### E-mail

Assuntos (5):
1. Amanhã começa a turma VI de Diagnóstico por Imagem
2. Módulo 1 de Diagnóstico por Imagem, sábado e domingo: como entrar na turma
3. O que fazer hoje para entrar na turma VI de Diagnóstico por Imagem
4. A turma VI começa neste fim de semana
5. Diagnóstico por Imagem: compre pela página ou fale com vendas

Escolhidos: **A = 3**, **B = 4**.
Texto de pré-visualização: Módulo 1 online, em 31/10 e 01/11. As duas formas de entrar.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária começa amanhã, sábado, 31/10/2026. O módulo 1 é online e acontece em 31/10 e 01/11.
>
> Para entrar na turma você tem duas formas:
> 1. Comprar pela página da turma: [link]
> 2. Falar com o time de vendas de São Paulo, pelo WhatsApp (11) 91366-9290.
>
> Investimento: 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00. {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada. O primeiro módulo presencial é só em fevereiro de 2027.
>
> TC (só com confirmação escrita da Ufape): A Ufape confirmou a formação da turma.
>
> Faculdade UFAPE

Chamada para ação: entrar na turma.
Follow-up (e-mail): nenhum no dia do início (sábado, fora do envio comercial). Quem não abriu recebe só o pós-início.
Rodapé e descadastro como em 1.2.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. Amanhã começa a turma VI de Diagnóstico por Imagem.
2. {{1}}, o módulo 1 de Diagnóstico por Imagem é neste fim de semana, online.
3. Olá, {{1}}. Para entrar na turma VI, são duas formas.
4. {{1}}, a turma VI de Diagnóstico por Imagem começa neste fim de semana.
5. Olá, {{1}}. Como entrar na turma VI de Diagnóstico por Imagem.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (pos_68604_vespera_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária começa amanhã, sábado, 31/10/2026. O módulo 1 é online, em 31/10 e 01/11.
>
> Para entrar: compre pela página (botão abaixo) ou fale com vendas de São Paulo, (11) 91366-9290.
>
> Investimento: 30x de R$ 1.000,00 no cartão ou boleto (total de R$ 30.000,00), mais matrícula de R$ 250,00. A 1ª mensalidade, segundo a página, é paga até 30 dias antes do início; esse prazo já passou, então o time orienta como entrar. Turma mínima de 20 alunos.

Botões: [Comprar pela página] e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Variáveis: {{1}} primeiro_nome; sufixo do botão com UTM 68604-vespera.
Follow-up: nenhum.
Template aprovado pela Meta: [CONFIRMAR pos_68604_vespera_v1].

### 2.4 Pós-início (04/11): para quem não entrou

**Objetivo:** apresentar a próxima turma da mesma área sem pressão. A turma VI começou. A próxima turma da área (A5) no catálogo é a 68629, Pós-graduação em Ultrassonografia de Pequenos Animais, que é **outro curso** (foco no ultrassom, 360 h). A mensagem diz isso com clareza. Não há outra turma de Diagnóstico por Imagem aberta (a 68611 está em "verificar" e não é mencionada).
**Segmento:** lead de 68604 sem matrícula.

#### E-mail

Assuntos (5):
1. Diagnóstico por Imagem: uma turma de ultrassonografia começa em 22/05/2027
2. A turma VI começou. A próxima turma da área é de ultrassonografia
3. Pós-graduação em Ultrassonografia de Pequenos Animais: cronograma da turma III
4. Imagem na clínica: quatro módulos de prática com o aparelho
5. Sobre a Pós-graduação em Diagnóstico por Imagem: um aviso e um caminho

Escolhidos: **A = 3**, **B = 2**.
Texto de pré-visualização: É outro curso, com foco no ultrassom. Veja se faz sentido para você.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem Aplicado à Clínica Médica e Cirúrgica Veterinária começou em 31/10/2026.
>
> Na mesma área, a próxima turma aberta no catálogo é a turma III da Pós-graduação em Ultrassonografia de Pequenos Animais, com início em 22/05/2027, em São Paulo. É outro curso: tem foco no ultrassom (360 h, 18 módulos, semipresencial) e quatro módulos de prática presencial, que não são transmitidos. O cronograma está na página.
>
> Investimento: 24x de R$ 685,67 no cartão ou boleto (total de R$ 16.456,00), mais matrícula de R$ 350,00. A 1ª mensalidade é paga até 30 dias antes do início. Turma mínima de 20 alunos: compre passagem e hotel só depois de a turma ser confirmada.
>
> Para ver o cronograma: [Ver a página da turma III]
>
> Se preferir ser avisado quando houver uma nova turma de Diagnóstico por Imagem, responda este e-mail com a palavra LISTA. Dúvidas: vendas de São Paulo, WhatsApp (11) 91366-9290.
>
> Faculdade UFAPE

Chamada para ação: botão "Ver a página da turma III" (UTM 68629-pos-inicio).
Observação: o segundo caminho (LISTA) é uma saída de cortesia, e não uma segunda chamada principal. Se o qa entender como segunda chamada, apagar o parágrafo da lista e deixar só o link.
Follow-up (e-mail, 3 dias úteis depois, só para quem não abriu): assunto "Ultrassonografia de Pequenos Animais: cronograma da turma III"; corpo curto com o link. Sem terceiro envio.
Rodapé e descadastro como em 1.2.
Pendência: a data de 68629 vem só do site (a planilha não tem a turma). [CONFIRMAR NO CATÁLOGO] antes do envio.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. A turma VI de Diagnóstico por Imagem já começou.
2. {{1}}, na mesma área há uma turma de ultrassonografia em 22/05/2027.
3. Olá, {{1}}. Um aviso sobre a Pós-graduação em Diagnóstico por Imagem.
4. {{1}}, sobre Diagnóstico por Imagem: outro curso da área, sem pressão.
5. Olá, {{1}}. Próxima turma da área de imagem: Ultrassonografia de Pequenos Animais.

Escolhidas: **A = 2**, **B = 4**.

Corpo do template (pos_68604_pos_inicio_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma VI da Pós-graduação em Diagnóstico por Imagem começou em 31/10/2026. Na mesma área, a próxima turma aberta é a III da Pós-graduação em Ultrassonografia de Pequenos Animais, em 22/05/2027, em São Paulo. É outro curso: foco no ultrassom, 360 h, quatro módulos de prática presencial.
>
> Investimento: 24x de R$ 685,67 no cartão ou boleto (total de R$ 16.456,00), mais matrícula de R$ 350,00. A 1ª mensalidade é paga até 30 dias antes do início. Turma mínima de 20 alunos: compre passagem e hotel só depois de a turma ser confirmada.

Botões: [Ver o cronograma] (URL de 68629 com UTM, a única ligação) e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Ver o cronograma".
Follow-up WhatsApp: nenhum.
Template aprovado pela Meta: [CONFIRMAR pos_68604_pos_inicio_v1].

**Variante com prova de bolsa (enviar só depois de a Ufape confirmar o destino da prova 68647, B6).** Substituir o segundo parágrafo do e-mail, ou a segunda frase do template, por: "Existe também a prova de bolsa de Diagnóstico por Imagem, em São Paulo, em 27/11/2026, das 9h às 13h, presencial. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Quem é aprovado tem até 10 dias úteis para fazer a matrícula. A bolsa não é acumulativa nem transferível. A turma de destino é [CONFIRMAR: informada pela Ufape]." Não usar "bolsa de até 50%" sozinho e não prometer bolsa nem aprovação. Sem destino confirmado, não enviar esta variante.

---

## 3. Turma 68606: Pós-graduação em Gastroenterologia Veterinária

### 3.1 Dados usados e fonte

| Dado | Valor | Fonte |
|---|---|---|
| Curso e turma | Pós-graduação em Gastroenterologia Veterinária, turma IX | catálogo, seção 2 |
| Início | 07/11/2026 (planilha). O site mostra 7 e 8/11 | catálogo; ficha |
| Local | São Paulo, Av. 9 de Julho, 3939 | catálogo; ficha |
| Modalidade, carga, módulos | Semipresencial, 500 h, 24 módulos | catálogo; módulos: ficha [CONFIRMAR NO CATÁLOGO] |
| Preço | 30x de R$ 1.180,00 no cartão ou boleto, total de R$ 35.400,00, matrícula de R$ 250,00 | catálogo |
| 1ª mensalidade | "deverá ser paga até 30 dias de antecedência da data de seu início" | ficha [CONFIRMAR NO CATÁLOGO] |
| Turma mínima | 20 alunos | ficha [CONFIRMAR NO CATÁLOGO] |
| Módulo 1 | 07 e 08/11/2026, online: semiologia e fisiologia gastrointestinal | ficha [CONFIRMAR NO CATÁLOGO] |
| Primeiro módulo presencial | Módulo 6, 17 e 18/04/2027: anatomia prática, práticas de cirurgia esofágica, gástrica e intestinal, parasitologia ou transplante fecal. Outros presenciais: módulo 13 (endoscopia, novembro de 2027) e módulo 21 (videocirurgia, cirurgia pancreática e hepatobiliar, julho de 2028) | ficha [CONFIRMAR NO CATÁLOGO] |
| Presenciais e práticas | Não são transmitidos nem disponibilizados | ficha [CONFIRMAR NO CATÁLOGO] |
| Grupo de casos | "Grupo para discussão de casos entre os alunos e os coordenadores" | ficha (texto da página) [CONFIRMAR NO CATÁLOGO] |
| Coordenação (COORD) | Esp. Maria Carolina Pappalardo | ficha [CONFIRMAR autorização] |
| Professores listados | 38 | ficha |
| Link | https://faculdade.ufape.com.br/produto/68606/pos-graduacao-em-gastroenterologia-veterinaria | ficha |
| Status | aberto | catálogo |
| Prova de bolsa da área | 68650, São Paulo, 27/11/2026, R$ 100,00 (aberto). A turma já começou antes do resultado: destino incerto | catálogo, seção 3; estrategia-de-oferta, 3.2 |
| Próxima turma da área | Nenhuma no catálogo de 26/10/2026 | catálogo, seção 2 |

Texto-padrão de preço (TP-68606): "Investimento: 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00."

### 3.2 Reta final (03/11)

**Objetivo:** levar o lead a abrir a página da turma IX ou falar com vendas para entrar na turma. Não juntar com a prova de bolsa na mesma peça.

#### E-mail

Assuntos (5):
1. Gastroenterologia Veterinária: a turma IX começa em 07/11
2. Pós-graduação em Gastroenterologia Veterinária: cronograma e condições da turma IX
3. O módulo 1 de Gastroenterologia é online: veja como entrar na turma IX
4. Do vômito crônico à hepatopatia: o que cobre a turma IX
5. Como entrar na turma IX de Gastroenterologia Veterinária

Escolhidos: **A = 1**, **B = 4**.
Texto de pré-visualização: Semipresencial, 500 h, São Paulo. Parcelas, total e matrícula dentro.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começa em 07/11/2026, em São Paulo.
>
> O programa percorre o trato digestivo: semiologia, laboratório, imagem, esôfago, estômago, intestino, pâncreas e fígado, além de emergências e oncologia. É semipresencial: 500 h em 24 módulos. O módulo 1 é online, em 07 e 08/11 (semiologia e fisiologia gastrointestinal). O primeiro módulo presencial é o 6, em 17 e 18/04/2027, com anatomia prática e prática de cirurgia esofágica, gástrica e intestinal. Presenciais e práticas não são transmitidos. A página prevê ainda um grupo para discussão de casos entre alunos e coordenação. O cronograma completo está na página e pode mudar conforme a necessidade das aulas.
>
> COORD: A coordenação é de Esp. Maria Carolina Pappalardo. A página lista 38 professores.
>
> Investimento: 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00.
>
> {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada.
>
> Para ver o cronograma e entrar na turma: [Ver a página da turma IX]
>
> Se preferir conversar, o time de vendas de São Paulo responde pelo WhatsApp (11) 91366-9290. Dúvidas de secretaria: (11) 97492-8443, de segunda a sexta, das 9h às 18h.
>
> Faculdade UFAPE

Chamada para ação: botão "Ver a página da turma IX" (UTM 68606-reta-final).
Rodapé e descadastro como em 1.2.
Follow-up (e-mail, 1 dia útil depois, só para quem não abriu): "Olá, {primeiro_nome}. A turma IX de Gastroenterologia Veterinária começa em 07/11, e o módulo 1 é online. Cronograma e condições: [link]. Para parar de receber, use o descadastro."

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. A turma IX de Gastroenterologia Veterinária começa em 07/11.
2. {{1}}, o cronograma da Pós-graduação em Gastroenterologia Veterinária está publicado.
3. Olá, {{1}}. Você se interessou pela Pós-graduação em Gastroenterologia Veterinária: veja como entrar na turma IX.
4. Olá, {{1}}. Sobre Gastroenterologia Veterinária: o módulo 1 é online.
5. {{1}}, 500 h de Gastroenterologia Veterinária: veja a turma IX.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (pos_68606_reta_final_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começa em 07/11/2026, em São Paulo. É semipresencial, com 500 h e 24 módulos: teoria online e prática presencial. O módulo 1 é online.
>
> COORD: Coordenação: Esp. Maria Carolina Pappalardo.
>
> Investimento: 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00. A página informa que a 1ª mensalidade é paga até 30 dias antes do início. Esse prazo já passou: fale com o time de vendas para saber como entrar na turma. Turma mínima de 20 alunos.

Botões: [Ver a página da turma] (UTM) e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Ver a página da turma".
Variáveis: {{1}} primeiro_nome; sufixo do botão com UTM.
Follow-up: nenhum reenvio; a véspera cumpre o papel.
Template aprovado pela Meta: [CONFIRMAR pos_68606_reta_final_v1].

### 3.3 Véspera (06/11, "começa amanhã, sábado")

**Objetivo:** dizer o que fazer para entrar.

#### E-mail

Assuntos (5):
1. Amanhã começa a turma IX de Gastroenterologia Veterinária
2. Módulo 1 de Gastroenterologia, sábado e domingo: como entrar na turma
3. O que fazer hoje para entrar na turma IX de Gastroenterologia
4. A turma IX começa neste fim de semana
5. Gastroenterologia Veterinária: compre pela página ou fale com vendas

Escolhidos: **A = 3**, **B = 4**.
Texto de pré-visualização: Módulo 1 online, em 07 e 08/11. As duas formas de entrar.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começa amanhã, sábado, 07/11/2026. O módulo 1 é online e acontece em 07 e 08/11.
>
> Para entrar na turma você tem duas formas:
> 1. Comprar pela página da turma: [link]
> 2. Falar com o time de vendas de São Paulo, pelo WhatsApp (11) 91366-9290.
>
> Investimento: 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00. {CL1} Turma mínima de 20 alunos. Compre passagem e hotel só depois de a turma ser confirmada. O primeiro módulo presencial é só em 17 e 18/04/2027.
>
> TC (só com confirmação escrita da Ufape): A Ufape confirmou a formação da turma.
>
> Faculdade UFAPE

Chamada para ação: entrar na turma.
Follow-up (e-mail): nenhum no sábado. Quem não abriu recebe só o pós-início.
Rodapé e descadastro como em 1.2.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. Amanhã começa a turma IX de Gastroenterologia Veterinária.
2. {{1}}, o módulo 1 de Gastroenterologia é neste fim de semana, online.
3. Olá, {{1}}. Para entrar na turma IX, são duas formas.
4. {{1}}, a turma IX de Gastroenterologia começa neste fim de semana.
5. Olá, {{1}}. Como entrar na turma IX de Gastroenterologia Veterinária.

Escolhidas: **A = 1**, **B = 4**.

Corpo do template (pos_68606_vespera_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começa amanhã, sábado, 07/11/2026. O módulo 1 é online, em 07 e 08/11.
>
> Para entrar: compre pela página (botão abaixo) ou fale com vendas de São Paulo, (11) 91366-9290.
>
> Investimento: 30x de R$ 1.180,00 no cartão ou boleto (total de R$ 35.400,00), mais matrícula de R$ 250,00. A 1ª mensalidade, segundo a página, é paga até 30 dias antes do início; esse prazo já passou, então o time orienta como entrar. Turma mínima de 20 alunos.

Botões: [Comprar pela página] e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Variáveis: {{1}} primeiro_nome; sufixo do botão com UTM 68606-vespera.
Follow-up: nenhum.
Template aprovado pela Meta: [CONFIRMAR pos_68606_vespera_v1].

### 3.4 Pós-início (11/11): para quem não entrou

**Objetivo:** oferecer o próximo passo da área sem pressão. Não há outra turma de Gastroenterologia Veterinária aberta no catálogo. A prova de bolsa 68650 existe (27/11/2026, São Paulo), mas o destino não está confirmado e a turma IX já começou; por isso o caminho padrão é a lista de interesse, e a prova entra só em variante gated (B6).
**Segmento:** lead de 68606 sem matrícula.

#### E-mail

Assuntos (5):
1. Gastroenterologia Veterinária: quer ser avisado sobre uma nova turma?
2. A turma IX começou. E agora?
3. Pós-graduação em Gastroenterologia Veterinária: lista de interesse
4. Sobre a Pós-graduação em Gastroenterologia Veterinária: um aviso e uma pergunta
5. Gastroenterologia Veterinária: seguimos à disposição

Escolhidos: **A = 1**, **B = 4**.
Texto de pré-visualização: Sem pressão: só para registrar seu interesse.

Corpo:

> Olá, {primeiro_nome}.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começou em 07/11/2026. Hoje não há outra turma de Gastroenterologia Veterinária aberta no nosso catálogo.
>
> Se você quer ser avisado caso uma nova turma seja aberta, responda este e-mail com a palavra LISTA, e o time de vendas registra o seu interesse. Quando houver turma, você recebe as datas, o cronograma e as condições completas.
>
> Se ainda tem dúvida sobre a turma IX, o time de vendas de São Paulo responde pelo WhatsApp (11) 91366-9290.
>
> Faculdade UFAPE

Chamada para ação: responder LISTA (sem link).
Follow-up (e-mail, 3 dias úteis depois, só para quem não abriu): assunto "Gastroenterologia Veterinária: seu interesse continua registrado?"; duas linhas, mesma chamada. Sem terceiro envio.
Rodapé e descadastro como em 1.2.

#### WhatsApp (template)

Primeiras linhas (5):
1. Olá, {{1}}. A turma IX de Gastroenterologia Veterinária já começou.
2. {{1}}, quer ser avisado se abrir nova turma de Gastroenterologia Veterinária?
3. Olá, {{1}}. Um aviso sobre a Pós-graduação em Gastroenterologia Veterinária.
4. {{1}}, sobre Gastroenterologia Veterinária: sem pressão, só uma pergunta.
5. Olá, {{1}}. Lista de interesse de Gastroenterologia Veterinária.

Escolhidas: **A = 2**, **B = 4**.

Corpo do template (pos_68606_pos_inicio_v1):

> Olá, {{1}}. Aqui é da Faculdade UFAPE.
>
> A turma IX da Pós-graduação em Gastroenterologia Veterinária começou em 07/11/2026. Hoje não há outra turma de Gastroenterologia Veterinária aberta no nosso catálogo.
>
> Se quiser ser avisado caso uma nova turma seja aberta, toque em "Quero ser avisado". Se ainda tem dúvida sobre a turma IX, o time de vendas responde por aqui.

Botões (só respostas rápidas, nenhum link): [Quero ser avisado] e [Parar de receber]. Rodapé: "Responda SAIR para não receber mais mensagens."
Chamada para ação: botão "Quero ser avisado" (grava lista_interesse_gastroenterologia = sim e a data).
Follow-up WhatsApp: nenhum.
Template aprovado pela Meta: [CONFIRMAR pos_68606_pos_inicio_v1].

**Variante com prova de bolsa (só depois de a Ufape confirmar o destino da prova 68650, B6).** Acrescentar, antes do pedido de lista: "Existe também a prova de bolsa de Gastroenterologia, em São Paulo, em 27/11/2026, das 9h às 13h, presencial. Inscrição de R$ 100,00 (Pix, boleto ou 1x no cartão). Cada prova tem 11 bolsas: 2 de 50% (monitoria), 4 de 25% e 5 de 10%. Nota de corte 7,0. Quem é aprovado tem até 10 dias úteis para fazer a matrícula. A bolsa não é acumulativa nem transferível. A turma de destino é [CONFIRMAR: informada pela Ufape]." Com a prova, a chamada principal passa a ser a página da prova (um link no e-mail; botão de URL no template, que então precisa de novo nome e nova aprovação). Sem destino confirmado, não enviar.

---

## 4. Resumo dos nove templates do WhatsApp

| Nome sugerido | Turma e etapa | Variáveis | Botões | Aprovação Meta |
|---|---|---|---|---|
| pos_707_reta_final_v1 | 707, reta final | {{1}} primeiro nome; sufixo de UTM no botão | URL (página da turma), resposta rápida (Parar de receber) | [CONFIRMAR] |
| pos_707_vespera_v1 | 707, véspera | idem | URL (comprar pela página), Parar de receber | [CONFIRMAR] |
| pos_707_pos_inicio_v1 | 707, pós-início | {{1}} | resposta rápida (Quero ser avisado), Parar de receber | [CONFIRMAR] |
| pos_68604_reta_final_v1 | 68604, reta final | {{1}}; sufixo de UTM | URL, Parar de receber | [CONFIRMAR] |
| pos_68604_vespera_v1 | 68604, véspera | idem | URL, Parar de receber | [CONFIRMAR] |
| pos_68604_pos_inicio_v1 | 68604, pós-início (68629) | idem | URL (página de 68629), Parar de receber | [CONFIRMAR] |
| pos_68606_reta_final_v1 | 68606, reta final | idem | URL, Parar de receber | [CONFIRMAR] |
| pos_68606_vespera_v1 | 68606, véspera | idem | URL, Parar de receber | [CONFIRMAR] |
| pos_68606_pos_inicio_v1 | 68606, pós-início | {{1}} | resposta rápida (Quero ser avisado), Parar de receber | [CONFIRMAR] |

Notas: categoria marketing; idioma português do Brasil; o texto de cada template tem o preço, a data e a turma fixos (por isso só uma variável de nome). Os nomes são sugestão [SUPOSIÇÃO]. A linha COORD sai do corpo do template se a autorização (B1) não vier. Se a aprovação da Meta atrasar, vale mensagem livre só dentro da janela de 24 h depois de uma resposta do lead.

---

## 5. Respostas prontas para vendas

Uso: atendimento humano no WhatsApp de vendas (São Paulo: (11) 91366-9290) e na secretaria. Cada pergunta tem a resposta provisória, que pode ser usada hoje porque só diz o que a página diz, e a resposta final, que só vale depois de a Ufape confirmar a regra. Nenhuma resposta promete entrada, reposição, reembolso, bolsa, certificação ou resultado. Quem responde confirma na hora a turma e a data da pessoa. Nenhum dado pessoal vai para arquivo de trabalho.

### 5.1 "Ainda dá para entrar depois do início?" [CONFIRMAR política, PR4]

- **Resposta provisória (usar hoje):** "Boa pergunta. Vou confirmar com a coordenação a regra de entrada para a turma [VII, VI ou IX] e te respondo por aqui. Enquanto isso, o módulo 1 é online e o primeiro módulo presencial só acontece em [data da turma, tabela abaixo]."
- **Resposta final (só com a regra escrita pela Ufape):** "Dá para entrar na turma até [módulo ou data-limite informada pela Ufape]. A 1ª mensalidade vence [regra de entrada tardia]. Posso te passar o link de compra agora?"
- Não afirmar prazo, módulo-limite nem reposição enquanto não houver regra escrita.

Primeiro módulo presencial por turma: 707, módulo 4, 29 a 31/01/2027; 68604, módulo 4, fevereiro de 2027 (sem dia na ficha); 68606, módulo 6, 17 e 18/04/2027.

### 5.2 "A turma está confirmada?" [CONFIRMAR, PR2]

- **Resposta provisória:** "A turma abre com no mínimo 20 alunos. Eu confirmo com a coordenação o status da turma [VII, VI ou IX] e te aviso por aqui. A orientação da página é comprar passagem e hotel só depois de a turma ser confirmada. O módulo 1 é online, então não precisa de viagem agora."
- **Resposta final (só com confirmação escrita):** "A Ufape confirmou a formação da turma em [data]. [Seguir com o que fazer para entrar.]"
- Se a Ufape ainda não confirmou: nunca dizer "turma garantida", "confirmada" ou "vai fechar". Não citar número de alunos matriculados nem vagas restantes (não existe número no catálogo).

### 5.3 "Como funciona o módulo presencial?"

Resposta-base: "O curso é semipresencial: a teoria é online e a prática é presencial, na sede, em São Paulo (Av. 9 de Julho, 3939). As aulas presenciais e práticas não são transmitidas nem disponibilizadas. O cronograma pode mudar conforme a necessidade das aulas, e a versão atual está na página."

Complemento por turma (dados das fichas, [CONFIRMAR NO CATÁLOGO]):

| Turma | O que dizer sobre o presencial |
|---|---|
| 707 | Presenciais em módulos como o 4 (29 a 31/01/2027), com práticas de cirurgia e microcirurgia ocular, um microscópio por aluno e supervisão de professores e monitores. A página fala também em atendimentos clínicos reais em mutirões supervisionados. Horários dos módulos: sexta 14h às 20h, sábado 8h às 17h30, domingo 8h às 12h |
| 68604 | Presenciais com prática de radiologia, ultrassom e, pelo cronograma, também de anatomia, que a ficha chama de aula prática. O primeiro é o módulo 4, em fevereiro de 2027. A ficha não traz o dia: confirmar antes de falar |
| 68606 | Três módulos presenciais: o 6 (17 e 18/04/2027, anatomia prática e cirurgia digestiva), o 13 (endoscopia, novembro de 2027) e o 21 (videocirurgia, cirurgia pancreática e hepatobiliar, julho de 2028). Datas do 13 e do 21 só com mês na ficha para o 21: confirmar o dia |

Não dizer "estude no seu ritmo", "flexível" nem prometer hospedagem ou ressarcimento de passagem. A página diz que a Ufape não se responsabiliza pelo ressarcimento de passagens e hospedagem em caso de adiamento por força maior.

### 5.4 "E se eu perder o primeiro módulo?" [CONFIRMAR]

- **Resposta provisória:** "O módulo 1 é online. Eu confirmo com a coordenação como fica o acesso ao conteúdo de quem entra depois do início e te respondo por aqui. A página informa que aulas presenciais e práticas não são transmitidas nem disponibilizadas."
- No caso de 707, a página diz que as aulas teóricas ficam gravadas na plataforma para revisão. Dá para citar isso como texto da página, sem prometer que vale para quem entra depois do início [CONFIRMAR].
- **Resposta final (só com a regra escrita):** "Quem entra depois do módulo 1 [regra de reposição informada pela Ufape]."
- Não prometer reposição de módulo presencial. A regra de reposição não existe no catálogo (PR10).

### 5.5 Perguntas que costumam vir junto

| Pergunta | Resposta |
|---|---|
| Qual é o preço? | Usar o texto-padrão da turma (TP-707, TP-68604 ou TP-68606): parcelas, valor, total e matrícula. Não arredondar, não calcular desconto, não dizer "só", "apenas" nem "cabe no bolso" |
| Tem desconto ou bolsa? | Não prometer. 707: não há prova de bolsa aberta. 68604 e 68606: existe prova de bolsa da área em 27/11/2026, mas o destino é [CONFIRMAR]; só passar as regras da prova. Desconto para aluno ou ex-aluno: sem regra escrita, não oferecer |
| E o reembolso, se a turma não abrir? | A página diz que pedidos de reembolso dos valores de inscrição só são devidos se a turma não for confirmada. O que entra em "valores de inscrição" a Ufape ainda não definiu: "Vou confirmar com o financeiro (financeiro@intercursos.com.br) e te respondo" [CONFIRMAR]. Não prometer devolução de matrícula nem de mensalidade |
| O certificado vale? Tem MEC? | Não responder por mensagem. "A secretaria passa o texto oficial sobre a certificação do curso: (11) 97492-8443, duvidas@intercursos.com.br." [PREENCHER COM A REGULAÇÃO] |
| Posso pagar a 1ª mensalidade depois? | Não afirmar. Dizer que a página fala em 1ª mensalidade até 30 dias antes do início, que esse prazo já passou, e que o time confirma a condição de entrada [CONFIRMAR, PR4] |
| Posso falar com a coordenação? | Não repassar contato de docente. Encaminhar o pedido à coordenação acadêmica [CONFIRMAR canal] |
| Quero parar de receber mensagens | Registrar optout no CRM na hora, confirmar em uma frase e não enviar mais nada |

---

## 6. Auditoria de e-mail e WhatsApp (auditorias/07-email-e-whatsapp.md)

Rodada pelo agente em 26/10/2026. A conferência final é do qa-de-marketing.

| Item | Resultado | Observação |
|---|---|---|
| Consentimento e descadastro funcionando (opt-in registrado para WhatsApp, forma simples de sair nos dois canais) | Atendido no texto, pendente na operação | Botão "Parar de receber", resposta SAIR e link de descadastro em todas as mensagens. O opt-in por canal, com data e finalidade, precisa estar no CRM antes do envio (B7) |
| Cada mensagem tem um objetivo | Atendido | Seção 0.1. Véspera com dois caminhos para o mesmo objetivo (entrar). Na 68604 pós-início, o parágrafo da LISTA é saída de cortesia: se o qa entender como segunda chamada, apagar |
| Assuntos e primeiras linhas são honestos | Atendido | 135 assuntos e primeiras linhas conferidos: sem "últimas", "corra", "garanta", contador, número de vagas, "bolsa garantida" ou prazo inexistente. A única data de urgência é a de início, que é real |
| Segmentos recebem mensagens relevantes para a etapa da jornada | Atendido | Reta final, véspera e pós-início, com supressão de quem comprou, saiu ou está em atendimento |
| Réguas têm regras de saída | Atendido | Seção 0.4: supressão por matrícula e por optout, no máximo 3 WhatsApp por lead e turma em 15 dias [SUPOSIÇÃO], sem terceiro envio de e-mail |
| Resultados registrados para cada envio | Pendente de operação | Campos resultado_envio e etapa_envio na seção 0.5. O registro de testes A e B segue a skill assuntos-de-email, depois dos envios |
| Cliques, respostas e conversões medidos, não só aberturas e leituras | Atendido no desenho | UTM por turma e etapa (seção 0.4), resposta LISTA e botão "Quero ser avisado" gravados, conversão pela compra na página (código da turma) |
| WhatsApp só em horário comercial, com frequência humana e template aprovado pela Meta | Atendido no desenho, pendente de aprovação | Dias úteis, 9h às 18h, nove templates (seção 4) em [CONFIRMAR] aprovação (B4) |

Resultado: aprovado para revisão humana, com os bloqueios B1 a B7 da seção 0.3 abertos. Nenhuma mensagem sai antes deles.

## 7. Auditoria de conformidade educacional (auditorias/conformidade-educacional.md)

| Item | Resultado | Observação |
|---|---|---|
| Nome, modalidade, carga horária, duração e turno batem com o catálogo | Atendido | 707: semipresencial, 600 h. 68604: semipresencial, 500 h. 68606: semipresencial, 500 h. 68629: semipresencial, 360 h. Número de módulos (24 e 18) vem só das fichas [CONFIRMAR NO CATÁLOGO] |
| Curso com status "aberto" | Atendido | 707, 68604, 68606 e 68629 estão "aberto". A 68629 tem a data só no site [CONFIRMAR] |
| Modalidade clara e correta | Atendido | "Semipresencial" com teoria online e prática presencial. Nenhuma turma é chamada de EAD ou de presencial integral |
| Pós lato sensu sem "reconhecida pelo MEC" e sem texto de validade | Atendido | Nenhuma frase de certificação, nota do MEC ou selo. As fichas têm "CERTIFICADO PELO MEC" e a squad não repete |
| Curso livre sem diploma | Não se aplica | Nenhum curso livre citado |
| Nota MEC só com fonte | Não se aplica | Nenhuma nota citada |
| Nenhuma promessa de emprego, salário, promoção, aprovação ou sucesso | Atendido | Nenhuma peça fala de resultado profissional. Descrição do curso usa só o que a ficha diz que o curso faz |
| Empregabilidade e satisfação com fonte | Não se aplica | Nenhum dado citado |
| Superlativos só com fonte | Atendido | Nenhum "melhor", "maior", "referência nacional", "único", "renomados" |
| Comparação com concorrente | Não se aplica | Nenhuma comparação |
| Preço com valor, parcelas e condições completas, sem esconder matrícula ou reajuste | Atendido | Em toda mensagem: parcelas, valor da parcela, total e matrícula, copiados do catálogo. Condição da 1ª mensalidade explicitada (CL1). Reajuste: o catálogo não traz regra de reajuste da Pós [CONFIRMAR] |
| Bolsa e desconto com regra, público e validade | Atendido | Nenhuma bolsa ou desconto prometido. A variante com prova traz a distribuição completa (2 de 50% em monitoria, 4 de 25%, 5 de 10%), nota de corte, prazo de matrícula, regra de não acumulação e exige destino confirmado |
| Urgência real | Atendido | Só a data de início. Sem "últimas vagas", sem vagas restantes |
| Prouni, Fies ou financiamento próprio | Atendido | Não citados. "No cartão ou boleto" como no catálogo |
| Depoimentos, fotos e vídeos com autorização | Atendido | Nenhum usado. Docentes só na linha COORD, com nome e titulação da ficha, a remover se B1 não vier |
| Menores de idade | Não se aplica | Público é médico veterinário formado |
| Formulários com finalidade e política de privacidade | Pendente | Rodapé de e-mail com finalidade e [CONFIRMAR link da política de privacidade] |
| WhatsApp e e-mail só com consentimento e forma fácil de sair | Atendido no desenho | Seção 0.4 e B7 |
| Nenhum dado pessoal de aluno ou candidato na peça ou nos arquivos | Atendido | Só variáveis do CRM ({{1}} e {primeiro_nome}) preenchidas no envio. Nenhum telefone pessoal. Os telefones citados são os contatos oficiais |
| Anúncios (Meta e Google) | Não se aplica | Mensagens diretas, não anúncios |
| Página de destino entrega o que a mensagem promete | Atendido, com conferência | As mensagens prometem cronograma, preço e compra, que a página tem. Conferir no dia do envio se o preço e a data da página batem com o catálogo e se o link é o de 68604 (e não o de 68611) |

Resultado: aprovado para revisão humana, com bloqueios abertos (autorização da coordenação, política de entrada tardia, status de confirmação da turma, aprovação dos templates, lista de interesse, destino das provas, política de privacidade). Revisado por: copy-de-mensagens (agente). Revisão do qa-de-marketing e aprovação humana: pendentes. Data: 26/10/2026.

---

## 8. Divergências e cuidados encontrados nos arquivos de entrada

1. As fichas de 707, 68604 e 68606 trazem "CERTIFICADO PELO MEC" ou o título "CERTIFICAÇÃO DO MEC". Nada disso foi usado.
2. O CEP da ficha de 68604 (01428-001) é diferente do das outras turmas (01407-100), embora o endereço seja o mesmo. Nenhuma mensagem cita CEP. Corrigir na página é pedido ao site.
3. O número de módulos (24 e 18) e as datas de módulos aparecem só nas fichas, não no catálogo. Estão marcados [CONFIRMAR NO CATÁLOGO] nas tabelas de dados.
4. A 68629 não tem data na planilha ("só no site"). A data de 22/05/2027 precisa de conferência antes do envio do pós-início da 68604.
5. A mensagem das áreas A5 e A6 em saidas/02-estrategia-e-posicionamento/mensagens-pos-2026-10-26.md usa o fim "Fale com o time para saber como entrar na turma". Este arquivo mantém essa frase e acrescenta a condição da ficha (CL1), por pedido do cmo. Se o cmo preferir só a frase, remover a primeira oração de CL1.
6. Mídia paga (gestor-de-midia, seção 5): a pausa dos anúncios de 707, 68604 e 68606 acontece na data de início, salvo política de entrada. As mensagens de pós-início não dependem dessa política: não oferecem entrada na turma que começou.

---

## 9. Arquivos de entrada: fatos, suposições e dados que faltam

### Fatos (com fonte)

- 707: turma VII, São Paulo, semipresencial, 600 h, início 30/10/2026, 30x de R$ 1.590,00, total de R$ 47.700,00, matrícula de R$ 250,00, status aberto (catálogo, seção 2).
- 68604: turma VI, São Paulo, semipresencial, 500 h, início 31/10/2026, 30x de R$ 1.000,00, total de R$ 30.000,00, matrícula de R$ 250,00, aberto (catálogo, seção 2).
- 68606: turma IX, São Paulo, semipresencial, 500 h, início 07/11/2026, 30x de R$ 1.180,00, total de R$ 35.400,00, matrícula de R$ 250,00, aberto (catálogo, seção 2).
- 68629: turma III, São Paulo, semipresencial, 360 h, início 22/05/2027, 24x de R$ 685,67, total de R$ 16.456,00, matrícula de R$ 350,00, aberto, fonte só no site (catálogo, seção 2).
- Provas de bolsa 68647 (Diagnóstico por Imagem) e 68650 (Gastroenterologia): São Paulo, 27/11/2026, R$ 100,00, abertas. 68656 (Oftalmologia) encerrada, link fora do ar (catálogo, seção 3).
- Regras das provas: 11 bolsas (2 de 50% em monitoria, 4 de 25%, 5 de 10%), nota de corte 7,0, 10 dias úteis para a matrícula, bolsa não acumulativa e intransferível (ficha 68647; contexto/pos-graduacao.md).
- Coordenação: 707, Dra. Andrea Barbosa, Dra. Angélica Safatle, Dra. Juliana Jorge; 68604, M.V. Carlos Fotin; 68606, Esp. Maria Carolina Pappalardo (fichas).
- Cronograma, horários, turma mínima de 20, regra da 1ª mensalidade, orientação sobre passagem e hotel, regra de reembolso dos "valores de inscrição" e a regra de que presenciais e práticas não são transmitidos: fichas (dados só de ficha, [CONFIRMAR NO CATÁLOGO]).
- Contatos oficiais: vendas São Paulo (11) 91366-9290; secretaria (11) 97492-8443, (11) 5054-1204, duvidas@intercursos.com.br, segunda a sexta, 9h às 18h; financeiro@intercursos.com.br (contexto/ufape-geral.md).
- Nenhum número de vagas restantes, matrículas ou leads existe no catálogo (docs/execucao-2026-10-26.md).

### Suposições [SUPOSIÇÃO]

- Datas e horários de envio da seção 0.6.
- Limite de 3 WhatsApp por lead e turma em 15 dias.
- Padrão de UTM (utm_source, utm_medium, utm_campaign por código e etapa).
- Nomes dos templates da Meta.
- Que o lead com "interesse registrado" na turma tem opt-in válido de finalidade compatível (a tarefa descreve o segmento como opt-in).
- Horário comercial de WhatsApp igual ao da secretaria, das 9h às 18h, em dia útil.
- Resposta provisória de vendas "vou confirmar e te respondo por aqui" como texto seguro até a regra existir.

### Dados que faltam [CONFIRMAR]

- Autorização de uso do nome e da titulação da coordenação das três turmas.
- Política de entrada depois do início e depois do módulo 1; regra de reposição de módulo (PR4, PR10).
- Status de confirmação da turma e data de confirmação (PR2); o que entra nos "valores de inscrição" do reembolso.
- Aprovação pela Meta dos nove templates; quem administra o WhatsApp Business API.
- Mecanismo e responsável pela lista de interesse; se existe "avise-me" para essas áreas.
- Destino das provas 68647 e 68650 (variante com prova).
- Link da política de privacidade para o rodapé do e-mail.
- Data de início de 68629 na planilha (hoje só no site) e dia do primeiro módulo presencial de 68604 (a ficha só traz fevereiro de 2027).
- Horário de atendimento do WhatsApp de vendas de São Paulo (o horário conhecido é o da secretaria).
- Regra de reajuste das mensalidades da Pós (o catálogo não traz).
- Responsável por aprovar e-mail e WhatsApp em massa (tabela de aprovação vazia em contexto/ufape-geral.md).
